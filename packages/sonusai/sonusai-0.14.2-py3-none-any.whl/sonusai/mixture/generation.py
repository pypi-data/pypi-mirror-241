from sonusai.mixture.mixdb import MixtureDatabase
from sonusai.mixture.types import AudioT
from sonusai.mixture.types import AudiosT
from sonusai.mixture.types import Augmentations
from sonusai.mixture.types import AugmentedTargets
from sonusai.mixture.types import GenMixData
from sonusai.mixture.types import ImpulseResponseFiles
from sonusai.mixture.types import MRecord
from sonusai.mixture.types import MRecords
from sonusai.mixture.types import Mixups
from sonusai.mixture.types import NoiseFiles
from sonusai.mixture.types import SpectralMasks
from sonusai.mixture.types import TargetFiles
from sonusai.mixture.types import UniversalSNR


def config_file(location: str) -> str:
    from os.path import join

    return join(location, 'config.yml')


def initialize_db(location: str, test: bool = False) -> None:
    from .mixdb import db_connection

    con = db_connection(location=location, create=True, test=test)

    con.execute("""
    CREATE TABLE truth_setting(
    id INTEGER PRIMARY KEY NOT NULL,
    setting TEXT NOT NULL)
    """)

    con.execute("""
    CREATE TABLE target_augmentation(
    id INTEGER PRIMARY KEY NOT NULL,
    normalize TEXT,
    pitch TEXT,
    tempo TEXT,
    gain TEXT,
    eq1 TEXT,
    eq2 TEXT,
    eq3 TEXT,
    lpf TEXT,
    ir TEXT,
    count INTEGER,
    mixup INTEGER)
    """)

    con.execute("""
    CREATE TABLE noise_augmentation (
    id INTEGER PRIMARY KEY NOT NULL,
    normalize TEXT,
    pitch TEXT,
    tempo TEXT,
    gain TEXT,
    eq1 TEXT,
    eq2 TEXT,
    eq3 TEXT,
    lpf TEXT,
    ir TEXT,
    count INTEGER,
    mixup INTEGER)
    """)

    con.execute("""
    CREATE TABLE target (
    id INTEGER PRIMARY KEY NOT NULL,
    name TEXT NOT NULL,
    samples INTEGER NOT NULL,
    target_level_type TEXT NOT NULL)
    """)

    con.execute("""
    CREATE TABLE noise (
    id INTEGER PRIMARY KEY NOT NULL,
    name TEXT NOT NULL,
    samples INTEGER NOT NULL)
    """)

    con.execute("""
    CREATE TABLE top (
    id INTEGER PRIMARY KEY NOT NULL,
    version INTEGER NOT NULL,
    class_balancing BOOLEAN NOT NULL,
    feature TEXT NOT NULL,
    noise_mix_mode TEXT NOT NULL,
    num_classes INTEGER NOT NULL,
    seed INTEGER NOT NULL,
    truth_mutex BOOLEAN NOT NULL,
    truth_reduction_function TEXT NOT NULL,
    first_cba_id INTEGER NOT NULL,
    mixid_width INTEGER NOT NULL)
    """)

    con.execute("""
    CREATE TABLE asr_manifest (
    id INTEGER PRIMARY KEY NOT NULL,
    manifest TEXT NOT NULL)
    """)

    con.execute("""
    CREATE TABLE class_label (
    id INTEGER PRIMARY KEY NOT NULL,
    label TEXT NOT NULL)
    """)

    con.execute("""
    CREATE TABLE class_weights_threshold (
    id INTEGER PRIMARY KEY NOT NULL,
    threshold FLOAT NOT NULL)
    """)

    con.execute("""
    CREATE TABLE impulse_response (
    id INTEGER PRIMARY KEY NOT NULL,
    file TEXT NOT NULL)
    """)

    con.execute("""
    CREATE TABLE random_snr (
    id INTEGER PRIMARY KEY NOT NULL,
    snr TEXT NOT NULL)
    """)

    con.execute("""
    CREATE TABLE snr (
    id INTEGER PRIMARY KEY NOT NULL,
    snr FLOAT NOT NULL)
    """)

    con.execute("""
    CREATE TABLE spectral_mask (
    id INTEGER PRIMARY KEY NOT NULL,
    f_max_width INTEGER NOT NULL,
    f_num INTEGER NOT NULL,
    t_max_width INTEGER NOT NULL,
    t_num INTEGER NOT NULL,
    t_max_percent INTEGER NOT NULL)
    """)

    con.execute("""
    CREATE TABLE target_truth_setting (
    target_id INTEGER,
    truth_setting_id INTEGER,
    FOREIGN KEY(target_id) REFERENCES target (id),
    FOREIGN KEY(truth_setting_id) REFERENCES truth_setting (id))
    """)

    con.execute("""
    CREATE TABLE mixup (
    id INTEGER PRIMARY KEY NOT NULL,
    target_id INTEGER NOT NULL,
    target_augmentation_id INTEGER NOT NULL,
    target_gain FLOAT,
    FOREIGN KEY(target_id) REFERENCES target (id),
    FOREIGN KEY(target_augmentation_id) REFERENCES target_augmentation (id))
    """)

    con.execute("""
    CREATE TABLE mixture (
    id INTEGER PRIMARY KEY NOT NULL,
    name VARCHAR NOT NULL,
    noise_augmentation_id INTEGER NOT NULL,
    noise_id INTEGER NOT NULL,
    noise_offset INTEGER NOT NULL,
    noise_snr_gain FLOAT,
    random_snr BOOLEAN NOT NULL,
    samples INTEGER NOT NULL,
    snr FLOAT NOT NULL,
    spectral_mask_id INTEGER NOT NULL,
    spectral_mask_seed INTEGER NOT NULL,
    target_snr_gain FLOAT,
    FOREIGN KEY(noise_augmentation_id) REFERENCES noise_augmentation (id),
    FOREIGN KEY(noise_id) REFERENCES noise (id),
    FOREIGN KEY(spectral_mask_id) REFERENCES spectral_mask (id))
    """)

    con.execute("""
    CREATE TABLE mixture_mixup (
    mixture_id INTEGER,
    mixup_id INTEGER,
    FOREIGN KEY(mixture_id) REFERENCES mixture (id),
    FOREIGN KEY(mixup_id) REFERENCES mixup (id))
    """)

    con.commit()
    con.close()


def populate_top_table(location: str, config: dict, test: bool = False) -> None:
    """Populate top table
    """
    from sonusai import SonusAIError
    from .mixdb import db_connection

    if config['truth_mode'] not in ['normal', 'mutex']:
        raise SonusAIError(f'invalid truth_mode: {config["truth_mode"]}')
    truth_mutex = config['truth_mode'] == 'mutex'

    con = db_connection(location=location, readonly=False, test=test)
    con.execute("""
    INSERT INTO top (version, class_balancing, feature, noise_mix_mode, num_classes,
    seed, truth_mutex, truth_reduction_function, first_cba_id, mixid_width)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        1,
        config['class_balancing'],
        config['feature'],
        config['noise_mix_mode'],
        config['num_classes'],
        config['seed'],
        truth_mutex,
        config['truth_reduction_function'],
        0,
        0))
    con.commit()
    con.close()


def populate_asr_manifest_table(location: str, config: dict, test: bool = False) -> None:
    """Populate asr_manifest table
    """
    from .mixdb import db_connection

    con = db_connection(location=location, readonly=False, test=test)
    con.executemany("INSERT INTO asr_manifest (manifest) VALUES (?)",
                    [(item,) for item in config['asr_manifest']])
    con.commit()
    con.close()


def populate_class_label_table(location: str, config: dict, test: bool = False) -> None:
    """Populate class_label table
    """
    from .mixdb import db_connection

    con = db_connection(location=location, readonly=False, test=test)
    con.executemany("INSERT INTO class_label (label) VALUES (?)",
                    [(item,) for item in config['class_labels']])
    con.commit()
    con.close()


def populate_class_weights_threshold_table(location: str, config: dict, test: bool = False) -> None:
    """Populate class_weights_threshold table
    """
    from sonusai import SonusAIError
    from .mixdb import db_connection

    class_weights_threshold = config['class_weights_threshold']
    num_classes = config['num_classes']

    if not isinstance(class_weights_threshold, list):
        class_weights_threshold = [class_weights_threshold]

    if len(class_weights_threshold) == 1:
        class_weights_threshold = [class_weights_threshold[0]] * num_classes

    if len(class_weights_threshold) != num_classes:
        raise SonusAIError(f'invalid class_weights_threshold length: {len(class_weights_threshold)}')

    con = db_connection(location=location, readonly=False, test=test)
    con.executemany("INSERT INTO class_weights_threshold (threshold) VALUES (?)",
                    [(item,) for item in class_weights_threshold])
    con.commit()
    con.close()


def populate_random_snr_table(location: str, config: dict, test: bool = False) -> None:
    """Populate random_snr table
    """
    from .mixdb import db_connection

    con = db_connection(location=location, readonly=False, test=test)
    con.executemany("INSERT INTO random_snr (snr) VALUES (?)",
                    [(item,) for item in config['random_snrs']])
    con.commit()
    con.close()


def populate_snr_table(location: str, config: dict, test: bool = False) -> None:
    """Populate snr table
    """
    from .mixdb import db_connection

    con = db_connection(location=location, readonly=False, test=test)
    con.executemany("INSERT INTO snr (snr) VALUES (?)",
                    [(item,) for item in config['snrs']])
    con.commit()
    con.close()


def populate_spectral_mask_table(location: str, config: dict, test: bool = False) -> None:
    """Populate spectral_mask table
    """
    from .config import get_spectral_masks
    from .mixdb import db_connection

    con = db_connection(location=location, readonly=False, test=test)
    con.executemany("""
    INSERT INTO spectral_mask (f_max_width, f_num, t_max_width, t_num, t_max_percent) VALUES (?, ?, ?, ?, ?)
    """, [(item.f_max_width,
           item.f_num,
           item.t_max_width,
           item.t_num,
           item.t_max_percent) for item in get_spectral_masks(config)]
                    )
    con.commit()
    con.close()


def populate_target_table(location: str, target_files: TargetFiles, test: bool = False) -> None:
    """Populate target table
    """
    from .mixdb import db_connection

    con = db_connection(location=location, readonly=False, test=test)

    # Populate truth_setting table
    truth_settings: list[str] = []
    for truth_setting in [truth_setting for target_file in target_files
                          for truth_setting in target_file.truth_settings]:
        ts = truth_setting.to_json()
        if ts not in truth_settings:
            truth_settings.append(ts)
    con.executemany("INSERT INTO truth_setting (setting) VALUES (?)",
                    [(item,) for item in truth_settings])

    # Populate target table
    cur = con.cursor()
    for target_file in target_files:
        truth_setting_ids: list[int] = []
        for truth_setting in target_file.truth_settings:
            cur.execute("SELECT truth_setting.id FROM truth_setting WHERE ? = truth_setting.setting",
                        (truth_setting.to_json(),))
            truth_setting_ids.append(cur.fetchone()[0])

        cur.execute("INSERT INTO target (name, samples, target_level_type) VALUES (?, ?, ?)",
                    (target_file.name, target_file.samples, target_file.target_level_type))
        target_id = cur.lastrowid
        for truth_setting_id in truth_setting_ids:
            cur.execute("INSERT INTO target_truth_setting (target_id, truth_setting_id) VALUES (?, ?)",
                        (target_id, truth_setting_id))

    con.commit()
    con.close()


def populate_noise_table(location: str, noise_files: NoiseFiles, test: bool = False) -> None:
    """Populate noise table
    """
    from .mixdb import db_connection

    con = db_connection(location=location, readonly=False, test=test)
    con.executemany("INSERT INTO noise (name, samples) VALUES (?, ?)",
                    [(noise_file.name, noise_file.samples) for noise_file in noise_files])
    con.commit()
    con.close()


def populate_impulse_response_table(location: str, impulse_response_files: ImpulseResponseFiles,
                                    test: bool = False) -> None:
    """Populate impulse response table
    """
    from .mixdb import db_connection

    con = db_connection(location=location, readonly=False, test=test)
    con.executemany("INSERT INTO impulse_response (file) VALUES (?)",
                    [(impulse_response_file,) for impulse_response_file in impulse_response_files])
    con.commit()
    con.close()


def populate_target_augmentation_table(location: str, target_augmentations: Augmentations, test: bool = False) -> None:
    """Populate target augmentation table
    """
    from .helpers import from_augmentation
    from .mixdb import db_connection

    con = db_connection(location=location, readonly=False, test=test)
    con.executemany("""
    INSERT INTO target_augmentation (normalize, pitch, tempo, gain, eq1, eq2, eq3, lpf, ir, count, mixup)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, [from_augmentation(target_augmentation) for target_augmentation in target_augmentations])
    con.execute("UPDATE top SET first_cba_id=? WHERE top.id = ?", (len(target_augmentations), 1))
    con.commit()
    con.close()


def populate_noise_augmentation_table(location: str, noise_augmentations: Augmentations, test: bool = False) -> None:
    """Populate noise augmentation table
    """
    from .helpers import from_augmentation
    from .mixdb import db_connection

    con = db_connection(location=location, readonly=False, test=test)
    con.executemany("""
    INSERT INTO noise_augmentation (normalize, pitch, tempo, gain, eq1, eq2, eq3, lpf, ir, count, mixup)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, [from_augmentation(noise_augmentation) for noise_augmentation in noise_augmentations])
    con.commit()
    con.close()


def add_cba_to_target_augmentation_table(location: str, target_augmentations: Augmentations,
                                         test: bool = False) -> None:
    """Add class balancing augmentations target augmentation table
    """
    from .helpers import from_augmentation
    from .mixdb import db_connection

    con = db_connection(location=location, readonly=False, test=test)
    con.executemany("""
    INSERT INTO target_augmentation (normalize, pitch, tempo, gain, eq1, eq2, eq3, lpf, ir, count, mixup)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, [from_augmentation(target_augmentation) for target_augmentation in target_augmentations])
    con.commit()
    con.close()


def update_mixid_width(location: str, num_mixtures: int, test: bool = False) -> None:
    """Update the mixid width
    """
    from sonusai.utils.max_text_width import max_text_width
    from .mixdb import db_connection

    con = db_connection(location=location, readonly=False, test=test)
    con.execute("UPDATE top SET mixid_width=? WHERE top.id = ?", (max_text_width(num_mixtures), 1))
    con.commit()
    con.close()


def populate_mixture_table(location: str, mrecords: MRecords, test: bool = False) -> None:
    """Populate mixture table
    """
    from .mixdb import db_connection

    con = db_connection(location=location, readonly=False, test=test)

    # Populate mixup table
    mixups: list[tuple[int, int, float]] = []
    for mrecord in mrecords:
        for mrecord_mixup in mrecord.mixups:
            mixup = (mrecord_mixup.target_id, mrecord_mixup.target_augmentation_id, mrecord_mixup.target_gain)
            if mixup not in mixups:
                mixups.append(mixup)

    con.executemany("INSERT INTO mixup (target_id, target_augmentation_id, target_gain) VALUES (?, ?, ?)",
                    mixups)

    # Populate mixture table
    cur = con.cursor()
    for mrecord in mrecords:
        cur.execute("""
        INSERT INTO mixture (name, noise_augmentation_id, noise_id, noise_offset, noise_snr_gain, random_snr,
        samples, snr, spectral_mask_id, spectral_mask_seed, target_snr_gain)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            mrecord.name,
            mrecord.noise_augmentation_id,
            mrecord.noise_id,
            mrecord.noise_offset,
            mrecord.noise_snr_gain,
            mrecord.random_snr,
            mrecord.samples,
            mrecord.snr,
            mrecord.spectral_mask_id,
            mrecord.spectral_mask_seed,
            mrecord.target_snr_gain))

        mixture_id = cur.lastrowid
        for mrecord_mixup in mrecord.mixups:
            mixup_id = con.execute("""
            SELECT mixup.id
            FROM mixup
            WHERE ? = mixup.target_id AND ? = mixup.target_augmentation_id AND ? = mixup.target_gain
            """, (mrecord_mixup.target_id,
                  mrecord_mixup.target_augmentation_id,
                  mrecord_mixup.target_gain)).fetchone()[0]
            con.execute("INSERT INTO mixture_mixup (mixture_id, mixup_id) VALUES (?, ?)",
                        (mixture_id, mixup_id))

    con.commit()
    con.close()


def update_mrecord(mixdb: MixtureDatabase,
                   mrecord: MRecord,
                   with_data: bool = False) -> tuple[MRecord, GenMixData]:
    """Update mixture with name and gains

    :param mixdb: Mixture database
    :param mrecord: Mixture MRecord
    :param with_data: Return audio data
    :return: Generated audio data (if requested)
    """
    from .audio import get_next_noise
    from .augmentation import apply_gain
    from .helpers import get_target
    from .types import GenMixData

    noise_audio = _augmented_noise_audio(mixdb, mrecord)
    noise_audio = get_next_noise(audio=noise_audio, offset=mrecord.noise_offset, length=mrecord.samples)

    mrecord, target_audios = _initialize_target_audios(mixdb, mrecord)
    mrecord = _initialize_mixture_gains(mixdb=mixdb,
                                        mrecord=mrecord,
                                        target_audios=target_audios,
                                        noise_audio=noise_audio)

    mrecord.name = f'{int(mrecord.name):0{mixdb.mixid_width}}.h5'

    if not with_data:
        return mrecord, GenMixData()

    target_audios = [apply_gain(audio=target_audio, gain=mrecord.target_snr_gain) for target_audio in target_audios]
    noise_audio = apply_gain(audio=noise_audio, gain=mrecord.noise_snr_gain)
    target_audio = get_target(mixdb, mrecord, target_audios)
    mixture_audio = target_audio + noise_audio

    return mrecord, GenMixData(mixture=mixture_audio,
                               targets=target_audios,
                               target=target_audio,
                               noise=noise_audio)


def _augmented_noise_audio(mixdb: MixtureDatabase, mrecord: MRecord) -> AudioT:
    from .audio import read_audio
    from .audio import read_ir
    from .augmentation import apply_augmentation
    from .augmentation import apply_ir

    noise = mixdb.noise(mrecord.noise_id)
    noise_augmentation = mixdb.noise_augmentation(mrecord.noise_augmentation_id)

    audio = read_audio(noise.name)
    audio = apply_augmentation(audio, noise_augmentation)
    if noise_augmentation.ir is not None:
        audio = apply_ir(audio, read_ir(mixdb.impulse_response(noise_augmentation.ir)))

    return audio


def _initialize_target_audios(mixdb: MixtureDatabase, mrecord: MRecord) -> tuple[MRecord, AudiosT]:
    from .augmentation import apply_augmentation
    from .augmentation import pad_audio_to_length

    target_audios = []
    for mixup in mrecord.mixups:
        target_audio = mixdb.read_target_audio(mixup.target_id)
        target_augmentation = mixdb.target_augmentation(mixup.target_augmentation_id)
        target_audios.append(apply_augmentation(audio=target_audio,
                                                augmentation=target_augmentation,
                                                length_common_denominator=mixdb.feature_step_samples))

        # target_gain is used to back out the gain augmentation in order to return the target audio
        # to its normalized level when calculating truth (if needed).
        if target_augmentation.gain is not None:
            mixup.target_gain = 10 ** (float(target_augmentation.gain) / 20)
        else:
            mixup.target_gain = 1

    mrecord.samples = max([len(item) for item in target_audios])

    for idx in range(len(target_audios)):
        target_audios[idx] = pad_audio_to_length(audio=target_audios[idx], length=mrecord.samples)

    return mrecord, target_audios


def _initialize_mixture_gains(mixdb: MixtureDatabase,
                              mrecord: MRecord,
                              target_audios: AudiosT,
                              noise_audio: AudioT) -> MRecord:
    import numpy as np

    from sonusai import SonusAIError
    from sonusai.utils import asl_p56
    from sonusai.utils import db_to_linear

    target_audio = np.sum(target_audios, axis=0)

    if mrecord.snr < -96:
        # Special case for zeroing out target data
        mrecord.target_snr_gain = 0
        mrecord.noise_snr_gain = 1
        # Setting target_gain to zero will cause the truth to be all zeros.
        for mrecord_mixup in mrecord.mixups:
            mrecord_mixup.target_gain = 0
    elif mrecord.snr > 96:
        # Special case for zeroing out noise data
        mrecord.target_snr_gain = 1
        mrecord.noise_snr_gain = 0
    else:
        target_level_types = [target.target_level_type for target in
                              [mixdb.target(index) for index in mrecord.target_id]]
        if not all(target_level_type == target_level_types[0] for target_level_type in target_level_types):
            raise SonusAIError(f'Not all target_level_types in mixup are the same')

        target_level_type = target_level_types[0]
        match target_level_type:
            case 'default':
                target_energy = np.mean(np.square(target_audio))
            case 'speech':
                target_energy = asl_p56(target_audio)
            case _:
                raise SonusAIError(f'Unknown target_level_type: {target_level_type}')

        noise_energy = np.mean(np.square(noise_audio))
        if noise_energy == 0:
            noise_gain = 1
        else:
            noise_gain = np.sqrt(target_energy / noise_energy) / db_to_linear(mrecord.snr)

        # Check for noise_gain > 1 to avoid clipping
        if noise_gain > 1:
            mrecord.target_snr_gain = 1 / noise_gain
            mrecord.noise_snr_gain = 1
        else:
            mrecord.target_snr_gain = 1
            mrecord.noise_snr_gain = noise_gain

    # Check for clipping in mixture
    gain_adjusted_target_audio = target_audio * mrecord.target_snr_gain
    gain_adjusted_noise_audio = noise_audio * mrecord.noise_snr_gain
    mixture_audio = gain_adjusted_target_audio + gain_adjusted_noise_audio
    max_abs_audio = max(abs(mixture_audio))
    clip_level = db_to_linear(-0.25)
    if max_abs_audio > clip_level:
        # Clipping occurred; lower gains to bring audio within +/-1
        gain_adjustment = clip_level / max_abs_audio
        mrecord.target_snr_gain *= gain_adjustment
        mrecord.noise_snr_gain *= gain_adjustment

    return mrecord


def generate_mixtures(noise_mix_mode: str,
                      augmented_targets: AugmentedTargets,
                      target_files: TargetFiles,
                      target_augmentations: Augmentations,
                      noise_files: NoiseFiles,
                      noise_augmentations: Augmentations,
                      spectral_masks: SpectralMasks,
                      all_snrs: list[UniversalSNR],
                      mixups: list[int],
                      num_classes: int,
                      truth_mutex: bool,
                      feature_step_samples: int) -> tuple[int, int, MRecords]:
    """Generate mixtures

    :param noise_mix_mode: Noise mix mode
    :param augmented_targets: List of augmented targets
    :param target_files: List of target files
    :param target_augmentations: List of target augmentations
    :param noise_files: List of noise files
    :param noise_augmentations: List of noise augmentations
    :param spectral_masks: List of spectral masks
    :param all_snrs: List of all SNRs
    :param mixups: List of mixup values
    :param num_classes: Number of classes
    :param truth_mutex: Truth mutex mode
    :param feature_step_samples: Number of samples in a feature step
    :return: (Number of noise files used, number of noise samples used, list of mixture records)
    """
    from sonusai import SonusAIError

    if noise_mix_mode == 'exhaustive':
        return _exhaustive_noise_mix(augmented_targets=augmented_targets,
                                     target_files=target_files,
                                     target_augmentations=target_augmentations,
                                     noise_files=noise_files,
                                     noise_augmentations=noise_augmentations,
                                     spectral_masks=spectral_masks,
                                     all_snrs=all_snrs,
                                     mixups=mixups,
                                     num_classes=num_classes,
                                     truth_mutex=truth_mutex,
                                     feature_step_samples=feature_step_samples)

    if noise_mix_mode == 'non-exhaustive':
        return _non_exhaustive_noise_mix(augmented_targets=augmented_targets,
                                         target_files=target_files,
                                         target_augmentations=target_augmentations,
                                         noise_files=noise_files,
                                         noise_augmentations=noise_augmentations,
                                         spectral_masks=spectral_masks,
                                         all_snrs=all_snrs,
                                         mixups=mixups,
                                         num_classes=num_classes,
                                         truth_mutex=truth_mutex,
                                         feature_step_samples=feature_step_samples)

    if noise_mix_mode == 'non-combinatorial':
        return _non_combinatorial_noise_mix(augmented_targets=augmented_targets,
                                            target_files=target_files,
                                            target_augmentations=target_augmentations,
                                            noise_files=noise_files,
                                            noise_augmentations=noise_augmentations,
                                            spectral_masks=spectral_masks,
                                            all_snrs=all_snrs,
                                            mixups=mixups,
                                            num_classes=num_classes,
                                            truth_mutex=truth_mutex,
                                            feature_step_samples=feature_step_samples)

    raise SonusAIError(f'invalid noise_mix_mode: {noise_mix_mode}')


def _exhaustive_noise_mix(augmented_targets: AugmentedTargets,
                          target_files: TargetFiles,
                          target_augmentations: Augmentations,
                          noise_files: NoiseFiles,
                          noise_augmentations: Augmentations,
                          spectral_masks: SpectralMasks,
                          all_snrs: list[UniversalSNR],
                          mixups: list[int],
                          num_classes: int,
                          truth_mutex: bool,
                          feature_step_samples: int) -> tuple[int, int, MRecords]:
    """ Use every noise/augmentation with every target/augmentation
    """
    from random import randint

    import numpy as np

    from .augmentation import estimate_augmented_length_from_length
    from .targets import get_augmented_target_ids_for_mixup
    from .types import MRecord
    from .types import MRecords

    mrecords: MRecords = []
    m_id = 0
    used_noise_files = len(noise_files) * len(noise_augmentations)
    used_noise_samples = 0

    augmented_target_ids_for_mixups = [get_augmented_target_ids_for_mixup(augmented_targets=augmented_targets,
                                                                          targets=target_files,
                                                                          target_augmentations=target_augmentations,
                                                                          mixup=mixup,
                                                                          num_classes=num_classes,
                                                                          truth_mutex=truth_mutex) for mixup in mixups]
    for noise_file_index in range(len(noise_files)):
        for noise_augmentation_index in range(len(noise_augmentations)):
            noise_offset = 0
            noise_length = estimate_augmented_length_from_length(
                length=noise_files[noise_file_index].samples,
                tempo=noise_augmentations[noise_augmentation_index].tempo)

            for augmented_target_ids_for_mixup in augmented_target_ids_for_mixups:
                for augmented_target_ids in augmented_target_ids_for_mixup:
                    (mrecord_mixups,
                     target_length) = _get_target_info(augmented_target_ids=augmented_target_ids,
                                                       augmented_targets=augmented_targets,
                                                       target_files=target_files,
                                                       target_augmentations=target_augmentations,
                                                       feature_step_samples=feature_step_samples)

                    for spectral_mask_id in range(len(spectral_masks)):
                        for snr in all_snrs:
                            mrecords.append(MRecord(
                                mixups=mrecord_mixups,
                                name=str(m_id),
                                noise_id=noise_file_index + 1,
                                noise_offset=noise_offset,
                                noise_augmentation_id=noise_augmentation_index + 1,
                                samples=target_length,
                                snr=snr.value,
                                spectral_mask_id=spectral_mask_id + 1,
                                spectral_mask_seed=randint(0, np.iinfo('i').max),
                                random_snr=snr.is_random))
                            m_id += 1

                            noise_offset = int((noise_offset + target_length) % noise_length)
                            used_noise_samples += target_length

    return used_noise_files, used_noise_samples, mrecords


def _non_exhaustive_noise_mix(augmented_targets: AugmentedTargets,
                              target_files: TargetFiles,
                              target_augmentations: Augmentations,
                              noise_files: NoiseFiles,
                              noise_augmentations: Augmentations,
                              spectral_masks: SpectralMasks,
                              all_snrs: list[UniversalSNR],
                              mixups: list[int],
                              num_classes: int,
                              truth_mutex: bool,
                              feature_step_samples: int) -> tuple[int, int, MRecords]:
    """ Cycle through every target/augmentation without necessarily using all noise/augmentation combinations
    (reduced data set).
    """
    from random import randint

    import numpy as np

    from .targets import get_augmented_target_ids_for_mixup
    from .types import MRecord
    from .types import MRecords

    mrecords: MRecords = []
    m_id = 0
    used_noise_files = set()
    used_noise_samples = 0
    noise_offset = 0
    noise_id = 0
    noise_augmentation_id = 0

    augmented_target_indices_for_mixups = [get_augmented_target_ids_for_mixup(
        augmented_targets=augmented_targets,
        targets=target_files,
        target_augmentations=target_augmentations,
        mixup=mixup,
        num_classes=num_classes,
        truth_mutex=truth_mutex) for mixup in mixups]
    for mixup in augmented_target_indices_for_mixups:
        for augmented_target_indices in mixup:
            (mrecord_mixups,
             target_length) = _get_target_info(augmented_target_ids=augmented_target_indices,
                                               augmented_targets=augmented_targets,
                                               target_files=target_files,
                                               target_augmentations=target_augmentations,
                                               feature_step_samples=feature_step_samples)

            for spectral_mask_id in range(len(spectral_masks)):
                for snr in all_snrs:
                    used_noise_files.add(f'{noise_id}_{noise_augmentation_id}')
                    (noise_id,
                     noise_augmentation_id,
                     noise_offset) = _get_next_noise_offset(target_length=target_length,
                                                            noise_id=noise_id,
                                                            noise_augmentation_id=noise_augmentation_id,
                                                            noise_offset=noise_offset,
                                                            noise_files=noise_files,
                                                            noise_augmentations=noise_augmentations)

                    mrecords.append(MRecord(
                        mixups=mrecord_mixups,
                        name=str(m_id),
                        noise_id=noise_id + 1,
                        noise_augmentation_id=noise_augmentation_id + 1,
                        noise_offset=noise_offset,
                        samples=target_length,
                        snr=snr.value,
                        spectral_mask_id=spectral_mask_id + 1,
                        spectral_mask_seed=randint(0, np.iinfo('i').max),
                        random_snr=snr.is_random))
                    m_id += 1

                    noise_offset += target_length
                    used_noise_samples += target_length

    return len(used_noise_files), used_noise_samples, mrecords


def _non_combinatorial_noise_mix(augmented_targets: AugmentedTargets,
                                 target_files: TargetFiles,
                                 target_augmentations: Augmentations,
                                 noise_files: NoiseFiles,
                                 noise_augmentations: Augmentations,
                                 spectral_masks: SpectralMasks,
                                 all_snrs: list[UniversalSNR],
                                 mixups: list[int],
                                 num_classes: int,
                                 truth_mutex: bool,
                                 feature_step_samples: int) -> tuple[int, int, MRecords]:
    """ Combine a target/augmentation with a single cut of a noise/augmentation non-exhaustively
    (each target/augmentation does not use each noise/augmentation). Cut has random start and loop back to
    beginning if end of noise/augmentation is reached.
    """
    from random import choice
    from random import randint

    import numpy as np

    from .targets import get_augmented_target_ids_for_mixup
    from .types import MRecord
    from .types import MRecords

    mrecords: MRecords = []
    m_id = 0
    used_noise_files = set()
    used_noise_samples = 0
    noise_id = 0
    noise_augmentation_id = 0

    augmented_target_indices_for_mixups = [get_augmented_target_ids_for_mixup(
        augmented_targets=augmented_targets,
        targets=target_files,
        target_augmentations=target_augmentations,
        mixup=mixup,
        num_classes=num_classes,
        truth_mutex=truth_mutex) for mixup in mixups]
    for mixup in augmented_target_indices_for_mixups:
        for augmented_target_indices in mixup:
            (mrecord_mixups,
             target_length) = _get_target_info(augmented_target_ids=augmented_target_indices,
                                               augmented_targets=augmented_targets,
                                               target_files=target_files,
                                               target_augmentations=target_augmentations,
                                               feature_step_samples=feature_step_samples)

            for spectral_mask_id in range(len(spectral_masks)):
                for snr in all_snrs:
                    used_noise_files.add(f'{noise_id}_{noise_augmentation_id}')
                    (noise_id,
                     noise_augmentation_id,
                     noise_length) = _get_next_noise_indices(noise_is=noise_id,
                                                             noise_augmentation_id=noise_augmentation_id,
                                                             noise_files=noise_files,
                                                             noise_augmentations=noise_augmentations)

                    mrecords.append(MRecord(
                        mixups=mrecord_mixups,
                        name=str(m_id),
                        noise_id=noise_id + 1,
                        noise_augmentation_id=noise_augmentation_id + 1,
                        noise_offset=choice(range(noise_length)),
                        samples=target_length,
                        snr=snr.value,
                        spectral_mask_id=spectral_mask_id + 1,
                        spectral_mask_seed=randint(0, np.iinfo('i').max),
                        random_snr=snr.is_random))
                    m_id += 1

                    used_noise_samples += target_length

    return len(used_noise_files), used_noise_samples, mrecords


def _get_next_noise_indices(noise_is: int,
                            noise_augmentation_id: int,
                            noise_files: NoiseFiles,
                            noise_augmentations: Augmentations) -> tuple[int, int, int]:
    from .augmentation import estimate_augmented_length_from_length

    noise_augmentation_id += 1
    if noise_augmentation_id == len(noise_augmentations):
        noise_augmentation_id = 0
        noise_is += 1
        if noise_is == len(noise_files):
            noise_is = 0

    noise_length = estimate_augmented_length_from_length(length=noise_files[noise_is].samples,
                                                         tempo=noise_augmentations[noise_augmentation_id].tempo)
    return noise_is, noise_augmentation_id, noise_length


def _get_next_noise_offset(target_length: int,
                           noise_id: int,
                           noise_augmentation_id: int,
                           noise_offset: int,
                           noise_files: NoiseFiles,
                           noise_augmentations: Augmentations) -> tuple[int, int, int]:
    from sonusai import SonusAIError
    from .augmentation import estimate_augmented_length_from_length

    noise_length = estimate_augmented_length_from_length(length=noise_files[noise_id].samples,
                                                         tempo=noise_augmentations[noise_augmentation_id].tempo)
    if noise_offset + target_length >= noise_length:
        if noise_offset == 0:
            raise SonusAIError('Length of target audio exceeds length of noise audio')

        noise_offset = 0
        noise_augmentation_id += 1
        if noise_augmentation_id == len(noise_augmentations):
            noise_augmentation_id = 0
            noise_id += 1
            if noise_id == len(noise_files):
                noise_id = 0

    return noise_id, noise_augmentation_id, noise_offset


def _get_target_info(augmented_target_ids: list[int],
                     augmented_targets: AugmentedTargets,
                     target_files: TargetFiles,
                     target_augmentations: Augmentations,
                     feature_step_samples: int) -> tuple[Mixups, int]:
    from .augmentation import estimate_augmented_length_from_length
    from .types import Mixup
    from .types import Mixups

    mixups: Mixups = []
    target_length = 0
    for idx in augmented_target_ids:
        tfi = augmented_targets[idx].target_id
        tai = augmented_targets[idx].target_augmentation_id

        mixups.append(Mixup(target_id=tfi + 1, target_augmentation_id=tai + 1))

        target_length = max(estimate_augmented_length_from_length(length=target_files[tfi].samples,
                                                                  tempo=target_augmentations[tai].tempo,
                                                                  length_common_denominator=feature_step_samples),
                            target_length)
    return mixups, target_length
