from functools import cached_property
from functools import lru_cache
from itertools import product
from sqlite3 import Connection
from sqlite3 import Cursor
from typing import Any
from typing import Optional

from sonusai.mixture.types import AudioF
from sonusai.mixture.types import AudioT
from sonusai.mixture.types import AudiosF
from sonusai.mixture.types import AudiosT
from sonusai.mixture.types import Augmentation
from sonusai.mixture.types import Augmentations
from sonusai.mixture.types import ClassCount
from sonusai.mixture.types import Feature
from sonusai.mixture.types import FeatureGeneratorConfig
from sonusai.mixture.types import FeatureGeneratorInfo
from sonusai.mixture.types import GeneralizedIDs
from sonusai.mixture.types import ImpulseResponseFiles
from sonusai.mixture.types import MRecord
from sonusai.mixture.types import MRecords
from sonusai.mixture.types import NoiseFile
from sonusai.mixture.types import NoiseFiles
from sonusai.mixture.types import Segsnr
from sonusai.mixture.types import SpectralMask
from sonusai.mixture.types import SpectralMasks
from sonusai.mixture.types import TargetFile
from sonusai.mixture.types import TargetFiles
from sonusai.mixture.types import TransformConfig
from sonusai.mixture.types import Truth
from sonusai.mixture.types import UniversalSNR


def db_file(location: str, test: bool = False) -> str:
    from os.path import join

    if test:
        name = 'mixdb_test.db'
    else:
        name = 'mixdb.db'

    return join(location, name)


def db_connection(location: str, create: bool = False, readonly: bool = True, test: bool = False) -> Connection:
    import sqlite3
    from os import remove
    from os.path import exists

    from sonusai import SonusAIError

    name = db_file(location, test)
    if create and exists(name):
        remove(name)

    if not create and not exists(name):
        raise SonusAIError(f'Could not find mixture database in {location}')

    if not create and readonly:
        name += '?mode=ro'

    connection = sqlite3.connect('file:' + name, uri=True)
    # connection.set_trace_callback(print)
    return connection


class SQLiteContextManager:
    def __init__(self, location: str, test: bool = False) -> None:
        self.location = location
        self.test = test

    def __enter__(self) -> Cursor:
        self.con = db_connection(location=self.location, test=self.test)
        self.cur = self.con.cursor()
        return self.cur

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.con.close()


class MixtureDatabase:
    def __init__(self, location: str, test: bool = False) -> None:
        from functools import partial

        self.location = location
        self.db = partial(SQLiteContextManager, self.location, test)

    @cached_property
    def json(self) -> str:
        from .helpers import to_mrecord_jsons
        from .types import MixtureDatabaseConfig

        config = MixtureDatabaseConfig(
            asr_manifest=self.asr_manifests,
            class_balancing=self.class_balancing,
            class_labels=self.class_labels,
            class_weights_threshold=self.class_weights_thresholds,
            feature=self.feature,
            first_cba_id=self.first_cba_id,
            ir_files=self.impulse_responses,
            mixtures=to_mrecord_jsons(self.mixtures),
            noise_augmentations=self.noise_augmentations,
            noise_mix_mode=self.noise_mix_mode,
            noises=self.noises,
            num_classes=self.num_classes,
            random_snrs=self.random_snrs,
            seed=self.seed,
            snrs=self.snrs,
            spectral_masks=self.spectral_masks,
            target_augmentations=self.target_augmentations,
            targets=self.targets,
            truth_mutex=self.truth_mutex,
            truth_reduction_function=self.truth_reduction_function
        )
        return config.to_json(indent=2)

    def save(self) -> None:
        """Save the MixtureDatabase as a JSON file
        """
        from os.path import join

        json_name = join(self.location, 'mixdb.json')
        with open(file=json_name, mode='w') as file:
            file.write(self.json)

    def target_asr_data(self, t_id: int) -> str | None:
        """Get the ASR data for the given target ID

        :param t_id: Target ID
        :return: ASR text or None
        """
        from .tokenized_shell_vars import tokenized_expand

        name, _ = tokenized_expand(self.target(t_id).name)
        return self.asr_manifest_data.get(name, None)

    def mixture_asr_data(self, m_id: int) -> list[str | None]:
        """Get the ASR data for the given mixid

        :param m_id: Zero-based mixture ID
        :return: List of ASR text or None
        """
        return [self.target_asr_data(mixup.target_id) for mixup in self.mixture(m_id).mixups]

    @cached_property
    def asr_manifest_data(self) -> dict[str, str]:
        """Get ASR data

        Each line of a manifest file should be in the following format:

        {"audio_filepath": "/path/to/audio.wav", "text": "the transcription of the utterance", "duration": 23.147}

        The audio_filepath field should provide an absolute path to the audio file corresponding to the utterance. The
        text field should contain the full transcript for the utterance, and the duration field should reflect the
        duration of the utterance in seconds.

        Each entry in the manifest (describing one audio file) should be bordered by '{' and '}' and must be contained
        on one line. The fields that describe the file should be separated by commas, and have the form
        "field_name": value, as shown above.

        Since the manifest specifies the path for each utterance, the audio files do not have to be located in the same
        directory as the manifest, or even in any specific directory structure.

        The manifest dictionary consists of key/value pairs where the keys are target file names and the values are ASR
        text.
        """
        import json

        from sonusai import SonusAIError
        from .tokenized_shell_vars import tokenized_expand

        expected_keys = ['audio_filepath', 'text', 'duration']

        def _error_preamble(e_name: str, e_line_num: int) -> str:
            return f'Invalid entry in ASR manifest {e_name} line {e_line_num}'

        asr_manifest_data: dict[str, str] = {}

        for name in self.asr_manifests:
            expanded_name, _ = tokenized_expand(name)
            with open(file=expanded_name, mode='r') as f:
                line_num = 1
                for line in f:
                    result = json.loads(line.strip())

                    for key in expected_keys:
                        if key not in result:
                            SonusAIError(f'{_error_preamble(name, line_num)}: missing field "{key}"')

                    for key in result.keys():
                        if key not in expected_keys:
                            SonusAIError(f'{_error_preamble(name, line_num)}: unknown field "{key}"')

                    key, _ = tokenized_expand(result['audio_filepath'])
                    value = result['text']

                    if key in asr_manifest_data:
                        SonusAIError(f'{_error_preamble(name, line_num)}: entry already exists')

                    asr_manifest_data[key] = value

                    line_num += 1

        return asr_manifest_data

    @cached_property
    def fg_config(self) -> FeatureGeneratorConfig:
        return FeatureGeneratorConfig(feature_mode=self.feature,
                                      num_classes=self.num_classes,
                                      truth_mutex=self.truth_mutex)

    @cached_property
    def fg_info(self) -> FeatureGeneratorInfo:
        from .helpers import get_feature_generator_info

        return get_feature_generator_info(self.fg_config)

    @cached_property
    def seed(self) -> int:
        with self.db() as c:
            return int(c.execute("SELECT top.seed from top").fetchone()[0])

    @cached_property
    def num_classes(self) -> int:
        with self.db() as c:
            return int(c.execute("SELECT top.num_classes from top").fetchone()[0])

    @cached_property
    def truth_mutex(self) -> bool:
        with self.db() as c:
            return bool(c.execute("SELECT top.truth_mutex from top").fetchone()[0])

    @cached_property
    def truth_reduction_function(self) -> str:
        with self.db() as c:
            return str(c.execute("SELECT top.truth_reduction_function from top").fetchone()[0])

    @lru_cache
    def augmented_noise_length(self, noise_id: int, noise_augmentation_id: int) -> int:
        from .augmentation import estimate_augmented_length_from_length

        return estimate_augmented_length_from_length(length=self.noise(noise_id).samples,
                                                     tempo=self.noise_augmentation(noise_augmentation_id).tempo)

    @cached_property
    def noise_mix_mode(self) -> str:
        with self.db() as c:
            return str(c.execute("SELECT top.noise_mix_mode from top").fetchone()[0])

    @cached_property
    def class_balancing(self) -> bool:
        with self.db() as c:
            return bool(c.execute("SELECT top.class_balancing from top").fetchone()[0])

    @cached_property
    def feature(self) -> str:
        with self.db() as c:
            return str(c.execute("SELECT top.feature from top").fetchone()[0])

    @cached_property
    def fg_decimation(self) -> int:
        return self.fg_info.decimation

    @cached_property
    def fg_stride(self) -> int:
        return self.fg_info.stride

    @cached_property
    def fg_step(self) -> int:
        return self.fg_info.step

    @cached_property
    def fg_num_bands(self) -> int:
        return self.fg_info.num_bands

    @cached_property
    def ft_config(self) -> TransformConfig:
        return self.fg_info.ft_config

    @cached_property
    def eft_config(self) -> TransformConfig:
        return self.fg_info.eft_config

    @cached_property
    def it_config(self) -> TransformConfig:
        return self.fg_info.it_config

    @cached_property
    def transform_frame_ms(self) -> float:
        from .constants import SAMPLE_RATE

        return float(self.ft_config.R) / float(SAMPLE_RATE / 1000)

    @cached_property
    def feature_ms(self) -> float:
        return self.transform_frame_ms * self.fg_decimation * self.fg_stride

    @cached_property
    def feature_samples(self) -> int:
        return self.ft_config.R * self.fg_decimation * self.fg_stride

    @cached_property
    def feature_step_ms(self) -> float:
        return self.transform_frame_ms * self.fg_decimation * self.fg_step

    @cached_property
    def feature_step_samples(self) -> int:
        return self.ft_config.R * self.fg_decimation * self.fg_step

    @cached_property
    def first_cba_id(self) -> int:
        with self.db() as c:
            return int(c.execute("SELECT top.first_cba_id from top").fetchone()[0])

    @cached_property
    def all_snrs(self) -> list[UniversalSNR]:
        return ([UniversalSNR(is_random=False, raw_value=snr) for snr in self.snrs] +
                [UniversalSNR(is_random=True, raw_value=snr) for snr in self.random_snrs])

    @cached_property
    def augmented_target_samples(self) -> int:
        from itertools import product

        from .augmentation import estimate_augmented_length_from_length

        it = list(product(*[self.target_ids, self.target_augmentation_ids]))
        return sum([estimate_augmented_length_from_length(
            length=self.target(fi).samples,
            tempo=self.target_augmentation(ai).tempo,
            length_common_denominator=self.feature_step_samples) for fi, ai, in it])

    @cached_property
    def augmented_noise_samples(self) -> int:
        it = list(product(*[self.noise_ids, self.noise_augmentation_ids]))
        return sum([self.augmented_noise_length(fi, ai) for fi, ai in it])

    def total_samples(self, mixids: GeneralizedIDs = '*') -> int:
        return sum([self.mixture(m_id).samples for m_id in self.mixids_to_list(mixids)])

    def total_transform_frames(self, mixids: GeneralizedIDs = '*') -> int:
        return self.total_samples(mixids) // self.ft_config.R

    def total_feature_frames(self, mixids: GeneralizedIDs = '*') -> int:
        return self.total_samples(mixids) // self.feature_step_samples

    def mixture_transform_frames(self, samples: int) -> int:
        return samples // self.ft_config.R

    def mixture_feature_frames(self, samples: int) -> int:
        return samples // self.feature_step_samples

    def mixids_to_list(self, mixids: Optional[GeneralizedIDs] = None) -> list[int]:
        """Resolve generalized mixture IDs to a list of integers

        :param mixids: Generalized mixture IDs
        :return: List of mixture ID integers
        """
        from .helpers import generic_ids_to_list

        return generic_ids_to_list(self.num_mixtures, mixids)

    @cached_property
    def asr_manifests(self) -> list[str]:
        """Get ASR manifests from db

        :return: ASR manifests
        """
        with self.db() as c:
            return [str(item[0]) for item in c.execute("SELECT asr_manifest.manifest FROM asr_manifest").fetchall()]

    @cached_property
    def class_labels(self) -> list[str]:
        """Get class labels from db

        :return: Class labels
        """
        with self.db() as c:
            return [str(item[0]) for item in
                    c.execute("SELECT class_label.label FROM class_label ORDER BY class_label.id").fetchall()]

    @cached_property
    def class_weights_thresholds(self) -> list[float]:
        """Get class weights thresholds from db

        :return: Class weights thresholds
        """
        with self.db() as c:
            return [float(item[0]) for item in
                    c.execute("SELECT class_weights_threshold.threshold FROM class_weights_threshold").fetchall()]

    @cached_property
    def random_snrs(self) -> list[str]:
        """Get random snrs from db

        :return: Random SNRs
        """
        with self.db() as c:
            return [str(item[0]) for item in c.execute("SELECT random_snr.snr FROM random_snr").fetchall()]

    @cached_property
    def snrs(self) -> list[float]:
        """Get snrs from db

        :return: SNRs
        """
        with self.db() as c:
            return [float(item[0]) for item in c.execute("SELECT snr.snr FROM snr").fetchall()]

    @cached_property
    def spectral_masks(self) -> SpectralMasks:
        """Get spectral masks from db

        :return: Spectral masks
        """
        with self.db() as c:
            results = c.execute(
                "SELECT spectral_mask.f_max_width, f_num, t_max_width, t_num, t_max_percent FROM spectral_mask")
            return [SpectralMask(f_max_width=spectral_mask[0],
                                 f_num=spectral_mask[1],
                                 t_max_width=spectral_mask[2],
                                 t_num=spectral_mask[3],
                                 t_max_percent=spectral_mask[4]) for spectral_mask in results.fetchall()]

    @lru_cache
    def spectral_mask(self, sm_id: int) -> SpectralMask:
        """Get spectral mask with ID from db

        :param sm_id: Spectral mask ID
        :return: Spectral mask
        """
        with self.db() as c:
            spectral_mask = c.execute(
                "SELECT spectral_mask.f_max_width, f_num, t_max_width, t_num, t_max_percent " +
                "FROM spectral_mask " +
                "WHERE ? = spectral_mask.id",
                (sm_id,)).fetchone()
            return SpectralMask(f_max_width=spectral_mask[0],
                                f_num=spectral_mask[1],
                                t_max_width=spectral_mask[2],
                                t_num=spectral_mask[3],
                                t_max_percent=spectral_mask[4])

    @cached_property
    def targets(self) -> TargetFiles:
        """Get targets from db

        :return: TargetFiles
        """
        import json

        from .types import TruthSetting
        from .types import TruthSettings

        with self.db() as c:
            target_files: TargetFiles = []
            for target in c.execute("SELECT target.name, samples, target_level_type, id FROM target").fetchall():
                truth_settings: TruthSettings = []
                for ts in c.execute(
                        "SELECT truth_setting.setting " +
                        "FROM truth_setting, target_truth_setting " +
                        "WHERE ? = target_truth_setting.target_id " +
                        "AND truth_setting.id = target_truth_setting.truth_setting_id",
                        (target[3],)).fetchall():
                    entry = json.loads(ts[0])
                    truth_settings.append(TruthSetting(config=entry.get('config', None),
                                                       function=entry.get('function', None),
                                                       index=entry.get('index', None)))
                target_files.append(TargetFile(name=target[0],
                                               samples=target[1],
                                               target_level_type=target[2],
                                               truth_settings=truth_settings))
            return target_files

    @cached_property
    def target_ids(self) -> list[int]:
        """Get target IDs from db

        :return: List of target IDs
        """
        with self.db() as c:
            return [int(item[0]) for item in c.execute("SELECT target.id FROM target").fetchall()]

    @lru_cache
    def target(self, t_id: int) -> TargetFile:
        """Get target with ID from db

        :param t_id: Target ID
        :return: Target
        """
        import json

        from .types import TruthSetting
        from .types import TruthSettings

        with self.db() as c:
            target = c.execute("SELECT target.name, samples, target_level_type FROM target WHERE ? = target.id",
                               (t_id,)).fetchone()

            truth_settings: TruthSettings = []
            for ts in c.execute(
                    "SELECT truth_setting.setting " +
                    "FROM truth_setting, target_truth_setting " +
                    "WHERE ? = target_truth_setting.target_id " +
                    "AND truth_setting.id = target_truth_setting.truth_setting_id",
                    (t_id,)).fetchall():
                entry = json.loads(ts[0])
                truth_settings.append(TruthSetting(config=entry.get('config', None),
                                                   function=entry.get('function', None),
                                                   index=entry.get('index', None)))
            return TargetFile(name=target[0],
                              samples=target[1],
                              target_level_type=target[2],
                              truth_settings=truth_settings)

    @cached_property
    def num_targets(self) -> int:
        """Get number of targets from db

        :return: Number of targets
        """
        with self.db() as c:
            return int(c.execute("SELECT count(target.id) FROM target").fetchone()[0])

    @cached_property
    def noises(self) -> NoiseFiles:
        """Get noises from db

        :return: Noises
        """
        with self.db() as c:
            return [NoiseFile(name=noise[0], samples=noise[1]) for noise in
                    c.execute("SELECT noise.name, samples FROM noise").fetchall()]

    @cached_property
    def noise_ids(self) -> list[int]:
        """Get noise IDs from db

        :return: List of noise IDs
        """
        with self.db() as c:
            return [int(item[0]) for item in c.execute("SELECT noise.id FROM noise").fetchall()]

    @lru_cache
    def noise(self, n_id: int) -> NoiseFile:
        """Get noise with ID from db

        :param n_id: Noise ID
        :return: Noise
        """
        with self.db() as c:
            noise = c.execute("SELECT noise.name, samples FROM noise WHERE ? = noise.id",
                              (n_id,)).fetchone()
            return NoiseFile(name=noise[0], samples=noise[1])

    @cached_property
    def num_noises(self) -> int:
        """Get number of noises from db

        :return: Number of noises
        """
        with self.db() as c:
            return int(c.execute("SELECT count(noise.id) FROM noise").fetchone()[0])

    @cached_property
    def impulse_responses(self) -> ImpulseResponseFiles:
        """Get impulse responses from db

        :return: Impulse responses
        """
        with self.db() as c:
            return [str(impulse_response[0]) for impulse_response in
                    c.execute("SELECT impulse_response.file FROM impulse_response").fetchall()]

    @cached_property
    def impulse_response_ids(self) -> list[int]:
        """Get impulse response IDs from db

        :return: List of impulse response IDs
        """
        with self.db() as c:
            return [int(item[0]) for item in c.execute("SELECT impulse_response.id FROM impulse_response").fetchall()]

    @lru_cache
    def impulse_response(self, ir_id: int) -> str:
        """Get impulse response with ID from db

        :param ir_id: Impulse response ID
        :return: Noise
        """
        with self.db() as c:
            return str(c.execute("SELECT impulse_response.file FROM impulse_response WHERE ? = impulse_response.id",
                                 (ir_id + 1,)).fetchone()[0])

    @cached_property
    def num_impulse_responses(self) -> int:
        """Get number of impulse responses from db

        :return: Number of impulse responses
        """
        with self.db() as c:
            return int(c.execute("SELECT count(impulse_response.id) FROM impulse_response").fetchone()[0])

    @cached_property
    def target_augmentations(self) -> Augmentations:
        """Get target augmentations from db

        :return: Target augmentations
        """
        from .helpers import to_augmentation

        with self.db() as c:
            return [to_augmentation(entry) for entry in c.execute(
                "SELECT target_augmentation.normalize, pitch, tempo, gain, eq1, eq2, eq3, lpf, ir, count, mixup " +
                "FROM target_augmentation").fetchall()]

    @cached_property
    def target_augmentation_ids(self) -> list[int]:
        """Get target augmentation IDs from db

        :return: List of target augmentation IDs
        """
        with self.db() as c:
            return [int(item[0]) for item in
                    c.execute("SELECT target_augmentation.id FROM target_augmentation").fetchall()]

    @lru_cache
    def target_augmentation(self, ta_id: int) -> Augmentation:
        """Get target augmentation with ID from db

        :param ta_id: Noise ID
        :return: Target augmentation
        """
        from .helpers import to_augmentation

        with self.db() as c:
            return to_augmentation(c.execute(
                "SELECT target_augmentation.normalize, pitch, tempo, gain, eq1, eq2, eq3, lpf, ir, count, mixup " +
                "FROM target_augmentation " +
                "WHERE ? = target_augmentation.id",
                (ta_id,)).fetchone())

    @cached_property
    def num_target_augmentations(self) -> int:
        """Get number of target augmentations from db

        :return: Number of target augmentations
        """
        with self.db() as c:
            return int(c.execute("SELECT count(target_augmentation.id) FROM target_augmentation").fetchone()[0])

    @cached_property
    def mixups(self) -> list[int]:
        """Get mixup values used

        :return: Mixup values used
        """
        with self.db() as c:
            return list(set([int(item[0]) for item in
                             c.execute("SELECT target_augmentation.mixup FROM target_augmentation").fetchall()]))

    @lru_cache
    def target_augmentations_for_mixup(self, mixup: int) -> Augmentations:
        """Get target augmentations for a given mixup value

        :param mixup: Mixup value of interest
        :return: Target augmentations
        """
        from .helpers import to_augmentation

        with self.db() as c:
            entries = c.execute(
                "SELECT target_augmentation.normalize, pitch, tempo, gain, eq1, eq2, eq3, lpf, ir, count, mixup " +
                "FROM target_augmentation " +
                "WHERE ? = target_augmentation.mixup",
                (mixup,)).fetchall()
            return [to_augmentation(entry) for entry in entries]

    @cached_property
    def noise_augmentations(self) -> Augmentations:
        """Get noise augmentations from db

        :return: Noise augmentations
        """
        from .helpers import to_augmentation

        with self.db() as c:
            return [to_augmentation(entry) for entry in c.execute(
                "SELECT noise_augmentation.normalize, pitch, tempo, gain, eq1, eq2, eq3, lpf, ir, count, mixup " +
                "FROM noise_augmentation").fetchall()]

    @cached_property
    def noise_augmentation_ids(self) -> list[int]:
        """Get noise augmentation IDs from db

        :return: List of noise augmentation IDs
        """
        with self.db() as c:
            return [int(item[0]) for item in
                    c.execute("SELECT noise_augmentation.id FROM noise_augmentation").fetchall()]

    @lru_cache
    def noise_augmentation(self, na_id: int) -> Augmentation:
        """Get noise augmentation with ID from db

        :param na_id: Noise ID
        :return: Noise augmentation
        """
        from .helpers import to_augmentation

        with self.db() as c:
            return to_augmentation(c.execute(
                "SELECT noise_augmentation.normalize, pitch, tempo, gain, eq1, eq2, eq3, lpf, ir, count, mixup " +
                "FROM noise_augmentation " +
                "WHERE ? = noise_augmentation.id",
                (na_id,)).fetchone())

    @cached_property
    def num_noise_augmentations(self) -> int:
        """Get number of noise augmentations from db

        :return: Number of noise augmentations
        """
        with self.db() as c:
            return int(c.execute("SELECT count(noise_augmentation.id) FROM noise_augmentation").fetchone()[0])

    @cached_property
    def mixtures(self) -> MRecords:
        """Get mixtures from db

        :return: Mixtures
        """
        from .helpers import to_mrecord
        from .types import Mixup

        with self.db() as c:
            mrecords: MRecords = []
            for mrecord in c.execute(
                    "SELECT mixture.name, noise_augmentation_id, noise_id, noise_offset, noise_snr_gain, random_snr, " +
                    "samples, snr, spectral_mask_id, spectral_mask_seed, target_snr_gain, id " +
                    "FROM mixture").fetchall():
                mixups = [Mixup(target_id=item[0],
                                target_augmentation_id=item[1],
                                target_gain=item[2]) for item in
                          c.execute(
                              "SELECT mixup.target_id, target_augmentation_id, target_gain " +
                              "FROM mixup, mixture_mixup " +
                              "WHERE ? = mixture_mixup.mixture_id AND mixup.id = mixture_mixup.mixup_id",
                              (mrecord[11],)).fetchall()]
                mrecords.append(to_mrecord(mrecord, mixups))
            return mrecords

    @cached_property
    def mixture_ids(self) -> list[int]:
        """Get mixture IDs from db

        :return: List of zero-based mixture IDs
        """
        with self.db() as c:
            return [int(item[0]) - 1 for item in c.execute("SELECT mixture.id FROM mixture").fetchall()]

    @lru_cache
    def mixture(self, m_id: int) -> MRecord:
        """Get mixture with ID from db

        :param m_id: Zero-based mixture ID
        :return: Mixture
        """
        from .helpers import to_mrecord
        from .types import Mixup
        from .types import Mixups

        with self.db() as c:
            mrecord = c.execute(
                "SELECT mixture.name, noise_augmentation_id, noise_id, noise_offset, noise_snr_gain, random_snr, " +
                "samples, snr, spectral_mask_id, spectral_mask_seed, target_snr_gain, id " +
                "FROM mixture " +
                "WHERE ? = mixture.id",
                (m_id + 1,)).fetchone()

            mixups: Mixups = []
            for mixup in c.execute(
                    "SELECT mixup.target_id, target_augmentation_id, target_gain " +
                    "FROM mixup, mixture_mixup " +
                    "WHERE ? = mixture_mixup.mixture_id AND mixup.id = mixture_mixup.mixup_id",
                    (mrecord[11],)).fetchall():
                mixups.append(Mixup(target_id=mixup[0],
                                    target_augmentation_id=mixup[1],
                                    target_gain=mixup[2]))
            return to_mrecord(mrecord, mixups)

    @cached_property
    def mixid_width(self) -> int:
        with self.db() as c:
            return int(c.execute("SELECT top.mixid_width from top").fetchone()[0])

    def location_filename(self, name: str) -> str:
        """Add the location to the given file name

        :param name: File name
        :return: Location added
        """
        from os.path import join

        return join(self.location, name)

    def mixture_filename(self, m_id: int) -> str:
        """Get the HDF5 file name for the give mixture ID

        :param m_id: Zero-based mixture ID
        :return: File name
        """
        return self.location_filename(self.mixture(m_id).name)

    @cached_property
    def num_mixtures(self) -> int:
        """Get number of mixtures from db

        :return: Number of mixtures
        """
        with self.db() as c:
            return int(c.execute("SELECT count(mixture.id) FROM mixture").fetchone()[0])

    def read_mixture_data(self, m_id: int, items: list[str] | str) -> Any:
        """Read mixture data from a mixture HDF5 file

        :param m_id: Zero-based mixture ID
        :param items: String(s) of dataset(s) to retrieve
        :return: Data (or tuple of data)
        """
        from .helpers import read_mixture_data

        return read_mixture_data(self.location_filename(self.mixture(m_id).name), items)

    def read_target_audio(self, t_id: int) -> AudioT:
        """Read target audio

        :param t_id: Target ID
        :return: Target audio
        """
        from .audio import read_audio

        return read_audio(self.target(t_id).name)

    def augmented_noise_audio(self, mixture: MRecord) -> AudioT:
        """Get augmented noise audio

        :param mixture: Mixture
        :return: Augmented noise audio
        """
        from .audio import read_audio
        from .audio import read_ir
        from .augmentation import apply_augmentation
        from .augmentation import apply_ir

        noise = self.noise(mixture.noise_id)
        noise_augmentation = self.noise_augmentation(mixture.noise_augmentation_id)

        audio = read_audio(noise.name)
        audio = apply_augmentation(audio, noise_augmentation)
        if noise_augmentation.ir is not None:
            audio = apply_ir(audio, read_ir(self.impulse_response(noise_augmentation.ir)))

        return audio

    def mixture_targets(self, m_id: int, force: bool = False) -> AudiosT:
        """Get the list of augmented target audio data (one per target in the mixup) for the given mixture ID

        :param m_id: Zero-based mixture ID
        :param force: Force computing data from original sources regardless of whether cached data exists
        :return: List of augmented target audio data (one per target in the mixup)
        """
        from sonusai import SonusAIError
        from .augmentation import apply_augmentation
        from .augmentation import apply_gain
        from .augmentation import pad_audio_to_length

        if not force:
            targets = self.read_mixture_data(m_id, 'targets')
            if targets is not None:
                return list(targets)

        mixture = self.mixture(m_id)
        if mixture is None:
            raise SonusAIError(f'Could not find mixture for m_id: {m_id}')

        targets = []
        for mixup in mixture.mixups:
            target = self.read_target_audio(mixup.target_id)
            target = apply_augmentation(audio=target,
                                        augmentation=self.target_augmentation(mixup.target_augmentation_id),
                                        length_common_denominator=self.feature_step_samples)
            target = apply_gain(audio=target, gain=mixture.target_snr_gain)
            target = pad_audio_to_length(audio=target, length=mixture.samples)
            targets.append(target)

        return targets

    def mixture_targets_f(self,
                          m_id: int,
                          targets: Optional[AudiosT] = None,
                          force: bool = False) -> AudiosF:
        """Get the list of augmented target transform data (one per target in the mixup) for the given mixture ID

        :param m_id: Zero-based mixture ID
        :param targets: List of augmented target audio data (one per target in the mixup)
        :param force: Force computing data from original sources regardless of whether cached data exists
        :return: List of augmented target transform data (one per target in the mixup)
        """
        from .helpers import forward_transform

        if targets is None:
            targets = self.mixture_targets(m_id, force)

        return [forward_transform(target, self.ft_config) for target in targets]

    def mixture_target(self,
                       m_id: int,
                       targets: Optional[AudiosT] = None,
                       force: bool = False) -> AudioT:
        """Get the augmented target audio data for the given mixture ID

        :param m_id: Zero-based mixture ID
        :param targets: List of augmented target audio data (one per target in the mixup)
        :param force: Force computing data from original sources regardless of whether cached data exists
        :return: Augmented target audio data
        """
        from .helpers import get_target

        if not force:
            target = self.read_mixture_data(m_id, 'target')
            if target is not None:
                return target

        if targets is None:
            targets = self.mixture_targets(m_id, force)

        return get_target(self, self.mixture(m_id), targets)

    def mixture_target_f(self,
                         m_id: int,
                         targets: Optional[AudiosT] = None,
                         target: Optional[AudioT] = None,
                         force: bool = False) -> AudioF:
        """Get the augmented target transform data for the given mixture ID

        :param m_id: Zero-based mixture ID
        :param targets: List of augmented target audio data (one per target in the mixup)
        :param target: Augmented target audio for the given mixid
        :param force: Force computing data from original sources regardless of whether cached data exists
        :return: Augmented target transform data
        """
        from .helpers import forward_transform

        if target is None:
            target = self.mixture_target(m_id, targets, force)

        return forward_transform(target, self.ft_config)

    def mixture_noise(self,
                      m_id: int,
                      force: bool = False) -> AudioT:
        """Get the augmented noise audio data for the given mixture ID

        :param m_id: Zero-based mixture ID
        :param force: Force computing data from original sources regardless of whether cached data exists
        :return: Augmented noise audio data
        """
        from .audio import get_next_noise
        from .augmentation import apply_gain

        if not force:
            noise = self.read_mixture_data(m_id, 'noise')
            if noise is not None:
                return noise

        mixture = self.mixture(m_id)
        noise = self.augmented_noise_audio(mixture)
        noise = get_next_noise(audio=noise, offset=mixture.noise_offset, length=mixture.samples)
        return apply_gain(audio=noise, gain=mixture.noise_snr_gain)

    def mixture_noise_f(self,
                        m_id: int,
                        noise: Optional[AudioT] = None,
                        force: bool = False) -> AudioF:
        """Get the augmented noise transform for the given mixture ID

        :param m_id: Zero-based mixture ID
        :param noise: Augmented noise audio data
        :param force: Force computing data from original sources regardless of whether cached data exists
        :return: Augmented noise transform data
        """
        from .helpers import forward_transform

        if noise is None:
            noise = self.mixture_noise(m_id, force)

        return forward_transform(noise, self.ft_config)

    def mixture_mixture(self,
                        m_id: int,
                        targets: Optional[AudiosT] = None,
                        target: Optional[AudioT] = None,
                        noise: Optional[AudioT] = None,
                        force: bool = False) -> AudioT:
        """Get the mixture audio data for the given mixture ID

        :param m_id: Zero-based mixture ID
        :param targets: List of augmented target audio data (one per target in the mixup)
        :param target: Augmented target audio data
        :param noise: Augmented noise audio data
        :param force: Force computing data from original sources regardless of whether cached data exists
        :return: Mixture audio data
        """
        if not force:
            mixture = self.read_mixture_data(m_id, 'mixture')
            if mixture is not None:
                return mixture

        if target is None:
            target = self.mixture_target(m_id, targets)

        if noise is None:
            noise = self.mixture_noise(m_id)

        return target + noise

    def mixture_mixture_f(self,
                          m_id: int,
                          targets: Optional[AudiosT] = None,
                          target: Optional[AudioT] = None,
                          noise: Optional[AudioT] = None,
                          mixture: Optional[AudioT] = None,
                          force: bool = False) -> AudioF:
        """Get the mixture transform for the given mixture ID

        :param m_id: Zero-based mixture ID
        :param targets: List of augmented target audio data (one per target in the mixup)
        :param target: Augmented target audio data
        :param noise: Augmented noise audio data
        :param mixture: Mixture audio data
        :param force: Force computing data from original sources regardless of whether cached data exists
        :return: Mixture transform data
        """
        from .helpers import forward_transform

        if mixture is None:
            mixture = self.mixture_mixture(m_id, targets, target, noise, force)

        return forward_transform(mixture, self.ft_config)

    def mixture_truth_t(self,
                        m_id: int,
                        targets: Optional[AudiosT] = None,
                        noise: Optional[AudioT] = None,
                        force: bool = False) -> Truth:
        """Get the truth_t data for the given mixture ID

        :param m_id: Zero-based mixture ID
        :param targets: List of augmented target audio data (one per target in the mixup) for the given mixture ID
        :param noise: Augmented noise audio data for the given mixture ID
        :param force: Force computing data from original sources regardless of whether cached data exists
        :return: truth_t data
        """
        from .helpers import get_truth_t

        if not force:
            truth_t = self.read_mixture_data(m_id, 'truth_t')
            if truth_t is not None:
                return truth_t

        if targets is None:
            targets = self.mixture_targets(m_id)

        if noise is None:
            noise = self.mixture_noise(m_id)

        return get_truth_t(self, self.mixture(m_id), targets, noise)

    def mixture_segsnr_t(self,
                         m_id: int,
                         targets: Optional[AudiosT] = None,
                         target: Optional[AudioT] = None,
                         noise: Optional[AudioT] = None,
                         force: bool = False) -> Segsnr:
        """Get the segsnr_t data for the given mixture ID

        :param m_id: Zero-based mixture ID
        :param targets: List of augmented target audio data (one per target in the mixup)
        :param target: Augmented target audio data
        :param noise: Augmented noise audio data
        :param force: Force computing data from original sources regardless of whether cached data exists
        :return: segsnr_t data
        """
        from .helpers import get_segsnr_t

        if not force:
            segsnr_t = self.read_mixture_data(m_id, 'segsnr_t')
            if segsnr_t is not None:
                return segsnr_t

        if target is None:
            target = self.mixture_target(m_id, targets)

        if noise is None:
            noise = self.mixture_noise(m_id)

        return get_segsnr_t(self, self.mixture(m_id), target, noise)

    def mixture_segsnr(self,
                       m_id: int,
                       segsnr_t: Optional[Segsnr] = None,
                       targets: Optional[AudiosT] = None,
                       target: Optional[AudioT] = None,
                       noise: Optional[AudioT] = None,
                       force: bool = False) -> Segsnr:
        """Get the segsnr data for the given mixture ID

        :param m_id: Zero-based mixture ID
        :param segsnr_t: segsnr_t data
        :param targets: List of augmented target audio data (one per target in the mixup)
        :param target: Augmented target audio data
        :param noise: Augmented noise audio data
        :param force: Force computing data from original sources regardless of whether cached data exists
        :return: segsnr data
        """
        if not force:
            segsnr = self.read_mixture_data(m_id, 'segsnr')
            if segsnr is not None:
                return segsnr

            segsnr_t = self.read_mixture_data(m_id, 'segsnr_t')
            if segsnr_t is not None:
                return segsnr_t[0::self.ft_config.R]

        if segsnr_t is None:
            segsnr_t = self.mixture_segsnr_t(m_id, targets, target, noise)

        return segsnr_t[0::self.ft_config.R]

    def mixture_ft(self,
                   m_id: int,
                   targets: Optional[AudiosT] = None,
                   target: Optional[AudioT] = None,
                   noise: Optional[AudioT] = None,
                   mixture_f: Optional[AudioF] = None,
                   mixture: Optional[AudioT] = None,
                   truth_t: Optional[Truth] = None,
                   force: bool = False) -> tuple[Feature, Truth]:
        """Get the feature and truth_f data for the given mixture ID

        :param m_id: Zero-based mixture ID
        :param targets: List of augmented target audio data (one per target in the mixup)
        :param target: Augmented target audio data
        :param noise: Augmented noise audio data
        :param mixture_f: Mixture transform data
        :param mixture: Mixture audio data
        :param truth_t: truth_t
        :param force: Force computing data from original sources regardless of whether cached data exists
        :return: Tuple of (feature, truth_f) data
        """
        from dataclasses import asdict

        import numpy as np
        from pyaaware import FeatureGenerator

        from .spectral_mask import apply_spectral_mask
        from .truth import truth_reduction

        if not force:
            feature, truth_f = self.read_mixture_data(m_id, ['feature', 'truth_f'])
            if feature is not None and truth_f is not None:
                return feature, truth_f

        if mixture_f is None:
            mixture_f = self.mixture_mixture_f(m_id=m_id,
                                               targets=targets,
                                               target=target,
                                               noise=noise,
                                               mixture=mixture)

        if truth_t is None:
            truth_t = self.mixture_truth_t(m_id=m_id, targets=targets, noise=noise)

        m = self.mixture(m_id)
        transform_frames = self.mixture_transform_frames(m.samples)
        feature_frames = self.mixture_feature_frames(m.samples)

        if truth_t is None:
            truth_t = np.zeros((m.samples, self.num_classes), dtype=np.float32)

        feature = np.empty((feature_frames, self.fg_stride, self.fg_num_bands), dtype=np.float32)
        truth_f = np.empty((feature_frames, self.num_classes), dtype=np.complex64)

        fg = FeatureGenerator(**asdict(self.fg_config))
        feature_frame = 0
        for transform_frame in range(transform_frames):
            indices = slice(transform_frame * self.ft_config.R, (transform_frame + 1) * self.ft_config.R)
            fg.execute(mixture_f[transform_frame],
                       truth_reduction(truth_t[indices], self.truth_reduction_function))

            if fg.eof():
                feature[feature_frame] = fg.feature()
                truth_f[feature_frame] = fg.truth()
                feature_frame += 1

        if m.spectral_mask_id is not None:
            feature = apply_spectral_mask(feature=feature,
                                          spectral_mask=self.spectral_mask(int(m.spectral_mask_id)),
                                          seed=m.spectral_mask_seed)

        if np.isreal(truth_f).all():
            return feature, truth_f.real

        return feature, truth_f

    def mixture_feature(self,
                        m_id: int,
                        targets: Optional[AudiosT] = None,
                        noise: Optional[AudioT] = None,
                        mixture: Optional[AudioT] = None,
                        truth_t: Optional[Truth] = None,
                        force: bool = False) -> Feature:
        """Get the feature data for the given mixture ID

        :param m_id: Zero-based mixture ID
        :param targets: List of augmented target audio data (one per target in the mixup)
        :param noise: Augmented noise audio data
        :param mixture: Mixture audio data
        :param truth_t: truth_t
        :param force: Force computing data from original sources regardless of whether cached data exists
        :return: Feature data
        """
        feature, _ = self.mixture_ft(m_id=m_id,
                                     targets=targets,
                                     noise=noise,
                                     mixture=mixture,
                                     truth_t=truth_t,
                                     force=force)
        return feature

    def mixture_truth_f(self,
                        m_id: int,
                        targets: Optional[AudiosT] = None,
                        noise: Optional[AudioT] = None,
                        mixture: Optional[AudioT] = None,
                        truth_t: Optional[Truth] = None,
                        force: bool = False) -> Truth:
        """Get the truth_f data for the given mixture ID

        :param m_id: Zero-based mixture ID
        :param targets: List of augmented target audio data (one per target in the mixup)
        :param noise: Augmented noise audio data
        :param mixture: Mixture audio data
        :param truth_t: truth_t
        :param force: Force computing data from original sources regardless of whether cached data exists
        :return: truth_f data
        """
        _, truth_f = self.mixture_ft(m_id=m_id,
                                     targets=targets,
                                     noise=noise,
                                     mixture=mixture,
                                     truth_t=truth_t,
                                     force=force)
        return truth_f

    def mixture_class_count(self,
                            m_id: int,
                            targets: Optional[AudiosT] = None,
                            noise: Optional[AudioT] = None,
                            truth_t: Optional[Truth] = None) -> ClassCount:
        """Compute the number of samples for which each truth index is active for the given mixture ID

        :param m_id: Zero-based mixture ID
        :param targets: List of augmented target audio (one per target in the mixup)
        :param noise: Augmented noise audio
        :param truth_t: truth_t
        :return: List of class counts
        """
        import numpy as np

        if truth_t is None:
            truth_t = self.mixture_truth_t(m_id, targets, noise)

        class_count = [0] * self.num_classes
        num_classes = self.num_classes
        if self.truth_mutex:
            num_classes -= 1
        for cl in range(num_classes):
            class_count[cl] = int(np.sum(truth_t[:, cl] >= self.class_weights_thresholds[cl]))

        return class_count
