from typing import Any

from sonusai.mixture.mixdb import MixtureDatabase
from sonusai.mixture.types import AudioF
from sonusai.mixture.types import AudioT
from sonusai.mixture.types import AudiosT
from sonusai.mixture.types import Augmentation
from sonusai.mixture.types import Feature
from sonusai.mixture.types import FeatureGeneratorConfig
from sonusai.mixture.types import FeatureGeneratorInfo
from sonusai.mixture.types import GeneralizedIDs
from sonusai.mixture.types import MRecord
from sonusai.mixture.types import MRecordJSONs
from sonusai.mixture.types import MRecords
from sonusai.mixture.types import Mixups
from sonusai.mixture.types import Segsnr
from sonusai.mixture.types import TransformConfig
from sonusai.mixture.types import Truth


def generic_ids_to_list(num_ids: int, ids: GeneralizedIDs = None) -> list[int]:
    """Resolve generalized IDs to a list of integers

    :param num_ids: Total number of indices
    :param ids: Generalized IDs
    :return: List of ID integers
    """
    from sonusai import SonusAIError

    all_ids = list(range(num_ids))

    if ids is None:
        return all_ids

    if isinstance(ids, str):
        if ids == '*':
            return all_ids

        try:
            result = eval(f'{all_ids}[{ids}]')
            if not isinstance(result, list):
                result = [result]
            return result
        except NameError:
            raise SonusAIError(f'Empty ids {ids}')

    if isinstance(ids, range):
        result = list(ids)
    elif isinstance(ids, int):
        result = [ids]
    else:
        result = ids

    if not all(isinstance(x, int) and 0 <= x < num_ids for x in result):
        raise SonusAIError(f'Invalid entries in ids of {ids}')

    if not result:
        raise SonusAIError(f'Empty ids {ids}')

    return result


def get_feature_generator_info(fg_config: FeatureGeneratorConfig) -> FeatureGeneratorInfo:
    from dataclasses import asdict

    from pyaaware import FeatureGenerator

    from .types import FeatureGeneratorInfo
    from .types import TransformConfig

    fg = FeatureGenerator(**asdict(fg_config))

    return FeatureGeneratorInfo(
        decimation=fg.decimation,
        stride=fg.stride,
        step=fg.step,
        num_bands=fg.num_bands,
        ft_config=TransformConfig(N=fg.ftransform_N,
                                  R=fg.ftransform_R,
                                  bin_start=fg.bin_start,
                                  bin_end=fg.bin_end,
                                  ttype=fg.ftransform_ttype),
        eft_config=TransformConfig(N=fg.eftransform_N,
                                   R=fg.eftransform_R,
                                   bin_start=fg.bin_start,
                                   bin_end=fg.bin_end,
                                   ttype=fg.eftransform_ttype),
        it_config=TransformConfig(N=fg.itransform_N,
                                  R=fg.itransform_R,
                                  bin_start=fg.bin_start,
                                  bin_end=fg.bin_end,
                                  ttype=fg.itransform_ttype)
    )


def write_mixture_data(mixdb: MixtureDatabase,
                       mrecord: MRecord,
                       items: list[tuple[str, Any]] | tuple[str, Any]) -> None:
    """Write mixture data to a mixture HDF5 file

    :param mixdb: Mixture database
    :param mrecord: Mixture file name
    :param items: Tuple(s) of (name, data)
    """
    import h5py

    if not isinstance(items, list):
        items = [items]

    name = mixdb.location_filename(mrecord.name)
    with h5py.File(name=name, mode='a') as f:
        for item in items:
            if item[0] in f:
                del f[item[0]]
            f.create_dataset(name=item[0], data=item[1])


def mrecord_metadata(mixdb: MixtureDatabase, mrecord: MRecord) -> str:
    """Create a string of metadata for an MRecord

    :param mixdb: Mixture database
    :param mrecord: Mixture MRecord
    :return: String of metadata
    """
    metadata = ''
    for mi, mixup in enumerate(mrecord.mixups):
        target = mixdb.target(mixup.target_id)
        target_augmentation = mixdb.target_augmentation(mixup.target_augmentation_id)
        metadata += f'target {mi} name: {target.name}\n'
        metadata += f'target {mi} augmentation: {target_augmentation.to_dict()}\n'
        if target_augmentation.ir is None:
            ir_name = None
        else:
            ir_name = mixdb.impulse_response(target_augmentation.ir)
        metadata += f'target {mi} ir: {ir_name}\n'
        metadata += f'target {mi} target_gain: {mixup.target_gain}\n'
        truth_settings = target.truth_settings
        for tsi in range(len(truth_settings)):
            metadata += f'target {mi} truth index {tsi}: {truth_settings[tsi].index}\n'
            metadata += f'target {mi} truth function {tsi}: {truth_settings[tsi].function}\n'
            metadata += f'target {mi} truth config {tsi}: {truth_settings[tsi].config}\n'
        metadata += f'target {mi} asr: {mixdb.target_asr_data(mixup.target_id)}\n'
    noise = mixdb.noise(mrecord.noise_id)
    noise_augmentation = mixdb.noise_augmentation(mrecord.noise_augmentation_id)
    metadata += f'noise name: {noise.name}\n'
    metadata += f'noise augmentation: {noise_augmentation.to_dict()}\n'
    if noise_augmentation.ir is None:
        ir_name = None
    else:
        ir_name = mixdb.impulse_response(noise_augmentation.ir)
    metadata += f'noise ir: {ir_name}\n'
    metadata += f'noise offset: {mrecord.noise_offset}\n'
    metadata += f'snr: {float(mrecord.snr)}\n'
    metadata += f'random_snr: {mrecord.random_snr}\n'
    metadata += f'samples: {mrecord.samples}\n'
    metadata += f'target_snr_gain: {float(mrecord.target_snr_gain)}\n'
    metadata += f'noise_snr_gain: {float(mrecord.noise_snr_gain)}\n'

    return metadata


def write_mrecord_metadata(mixdb: MixtureDatabase, mrecord: MRecord) -> None:
    """Write MRecord metadata to a text file

    :param mixdb: Mixture database
    :param mrecord: Mixture MRecord
    """
    from os.path import splitext

    name = mixdb.location_filename(splitext(mrecord.name)[0] + '.txt')
    with open(file=name, mode='w') as f:
        f.write(mrecord_metadata(mixdb, mrecord))


def from_augmentation(augmentation: Augmentation) -> tuple[str, str, str, str, str, str, str, str, str, int, int]:
    import json

    return (json.dumps(augmentation.normalize),
            json.dumps(augmentation.pitch),
            json.dumps(augmentation.tempo),
            json.dumps(augmentation.gain),
            json.dumps(augmentation.eq1),
            json.dumps(augmentation.eq2),
            json.dumps(augmentation.eq3),
            json.dumps(augmentation.lpf),
            json.dumps(augmentation.ir),
            augmentation.count,
            augmentation.mixup)


def to_augmentation(entry: tuple[str, str, str, str, str, str, str, str, str, int, int]) -> Augmentation:
    import json

    from .types import Augmentation

    return Augmentation(
        normalize=json.loads(entry[0]),
        pitch=json.loads(entry[1]),
        tempo=json.loads(entry[2]),
        gain=json.loads(entry[3]),
        eq1=json.loads(entry[4]),
        eq2=json.loads(entry[5]),
        eq3=json.loads(entry[6]),
        lpf=json.loads(entry[7]),
        ir=json.loads(entry[8]),
        count=entry[9],
        mixup=entry[10])


def to_mrecord(entry: tuple[str, int, int, int, float, bool, int, float, int, int, float], mixups: Mixups) -> MRecord:
    from .types import MRecord

    return MRecord(mixups=mixups,
                   name=str(entry[0]),
                   noise_augmentation_id=int(entry[1]),
                   noise_id=int(entry[2]),
                   noise_offset=int(entry[3]),
                   noise_snr_gain=float(entry[4]),
                   random_snr=bool(entry[5]),
                   samples=int(entry[6]),
                   snr=float(entry[7]),
                   spectral_mask_id=int(entry[8]),
                   spectral_mask_seed=int(entry[9]),
                   target_snr_gain=float(entry[10]))


def to_mrecord_jsons(mrecords: MRecords) -> MRecordJSONs:
    from .types import MRecordJSON

    return [MRecordJSON(
        name=mrecord.name,
        noise_augmentation_id=mrecord.noise_augmentation_id - 1,
        noise_id=mrecord.noise_id - 1,
        noise_offset=mrecord.noise_offset,
        noise_snr_gain=mrecord.noise_snr_gain,
        random_snr=mrecord.random_snr,
        samples=mrecord.samples,
        snr=mrecord.snr,
        spectral_mask_id=mrecord.spectral_mask_id - 1,
        spectral_mask_seed=mrecord.spectral_mask_seed,
        target_augmentation_id=[item - 1 for item in mrecord.target_augmentation_id],
        target_id=[item - 1 for item in mrecord.target_id],
        target_gain=mrecord.target_gain,
        target_snr_gain=mrecord.target_snr_gain) for mrecord in mrecords]


def read_mixture_data(name: str, items: list[str] | str) -> Any:
    """Read mixture data from a mixture HDF5 file

    :param name: Mixture file name
    :param items: String(s) of dataset(s) to retrieve
    :return: Data (or tuple of data)
    """
    from os.path import exists
    from typing import Any

    import h5py
    import numpy as np

    from sonusai import SonusAIError

    def _get_dataset(file: h5py.File, d_name: str) -> Any:
        if d_name in file:
            return np.array(file[d_name])
        return None

    if not isinstance(items, list):
        items = [items]

    if exists(name):
        try:
            with h5py.File(name, 'r') as f:
                result = ([_get_dataset(f, item) for item in items])
        except Exception as e:
            raise SonusAIError(f'Error reading {name}: {e}')
    else:
        result = ([None for _ in items])

    if len(items) == 1:
        result = result[0]

    return result


def get_truth_t(mixdb: MixtureDatabase, mrecord: MRecord, targets: AudiosT, noise: AudioT) -> Truth:
    """Get the truth_t data for the given mixture MRecord

    :param mixdb: Mixture database
    :param mrecord: Mixture MRecord
    :param targets: List of augmented target audio data (one per target in the mixup) for the given mixture ID
    :param noise: Augmented noise audio data for the given mixture ID
    :return: truth_t data
    """
    import numpy as np

    from sonusai import SonusAIError
    from .truth import truth_function
    from .types import TruthFunctionConfig

    if not all(len(target) == mrecord.samples for target in targets):
        raise SonusAIError('Lengths of targets do not match length of mixture')

    if len(noise) != mrecord.samples:
        raise SonusAIError('Length of noise does not match length of mixture')

    truth_t = np.zeros((mrecord.samples, mixdb.num_classes), dtype=np.float32)
    for idx in range(len(targets)):
        for truth_setting in mixdb.target(mrecord.target_id[idx]).truth_settings:
            config = TruthFunctionConfig(
                feature=mixdb.feature,
                index=truth_setting.index,
                function=truth_setting.function,
                config=truth_setting.config,
                num_classes=mixdb.num_classes,
                mutex=mixdb.truth_mutex,
                target_gain=mrecord.target_gain[idx] * mrecord.target_snr_gain
            )
            truth_t += truth_function(target_audio=targets[idx], noise_audio=noise, config=config)

    return truth_t


def get_ft(mixdb: MixtureDatabase, mrecord: MRecord, mixture: AudioT, truth_t: Truth) -> tuple[Feature, Truth]:
    """Get the feature and truth_f data for the given mixture MRecord

    :param mixdb: Mixture database
    :param mrecord: Mixture MRecord
    :param mixture: Mixture audio data for the given mixid
    :param truth_t: truth_t for the given mixid
    :return: Tuple of (feature, truth_f) data
    """
    from dataclasses import asdict

    import numpy as np
    from pyaaware import FeatureGenerator

    from .spectral_mask import apply_spectral_mask
    from .truth import truth_reduction

    mixture_f = get_mixture_f(mixdb=mixdb, mixture=mixture)

    transform_frames = mixdb.mixture_transform_frames(mrecord.samples)
    feature_frames = mixdb.mixture_feature_frames(mrecord.samples)

    feature = np.empty((feature_frames, mixdb.fg_stride, mixdb.fg_num_bands), dtype=np.float32)
    truth_f = np.empty((feature_frames, mixdb.num_classes), dtype=np.complex64)

    fg = FeatureGenerator(**asdict(mixdb.fg_config))
    feature_frame = 0
    for transform_frame in range(transform_frames):
        indices = slice(transform_frame * mixdb.ft_config.R, (transform_frame + 1) * mixdb.ft_config.R)
        fg.execute(mixture_f[transform_frame],
                   truth_reduction(truth_t[indices], mixdb.truth_reduction_function))

        if fg.eof():
            feature[feature_frame] = fg.feature()
            truth_f[feature_frame] = fg.truth()
            feature_frame += 1

    if mrecord.spectral_mask_id is not None:
        feature = apply_spectral_mask(feature=feature,
                                      spectral_mask=mixdb.spectral_mask(mrecord.spectral_mask_id),
                                      seed=mrecord.spectral_mask_seed)

    if np.isreal(truth_f).all():
        return feature, truth_f.real

    return feature, truth_f  # type: ignore


def get_segsnr(mixdb: MixtureDatabase, mrecord: MRecord, target: AudioT, noise: AudioT) -> Segsnr:
    """Get the segsnr data for the given mixture MRecord

    :param mixdb: Mixture database
    :param mrecord: Mixture MRecord
    :param target: Augmented target audio data
    :param noise: Augmented noise audio data
    :return: segsnr data
    """
    segsnr_t = get_segsnr_t(mixdb=mixdb, mrecord=mrecord, target=target, noise=noise)
    return segsnr_t[0::mixdb.ft_config.R]


def get_segsnr_t(mixdb: MixtureDatabase, mrecord: MRecord, target: AudioT, noise: AudioT) -> Segsnr:
    """Get the segsnr_t data for the given mixture MRecord

    :param mixdb: Mixture database
    :param mrecord: Mixture MRecord
    :param target: Augmented target audio data
    :param noise: Augmented noise audio data
    :return: segsnr_t data
    """
    import numpy as np
    from pyaaware import AawareForwardTransform

    from sonusai import SonusAIError

    fft = AawareForwardTransform(N=mixdb.ft_config.N,
                                 R=mixdb.ft_config.R,
                                 bin_start=mixdb.ft_config.bin_start,
                                 bin_end=mixdb.ft_config.bin_end,
                                 ttype=mixdb.ft_config.ttype)

    segsnr_t = np.empty(mrecord.samples, dtype=np.float32)

    _, target_energy = fft.execute_all(target)
    _, noise_energy = fft.execute_all(noise)

    offsets = range(0, mrecord.samples, mixdb.ft_config.R)
    if len(target_energy) != len(offsets):
        raise SonusAIError(f'Number of frames in energy, {len(target_energy)},'
                           f' is not number of frames in mixture, {len(offsets)}')

    for idx, offset in enumerate(offsets):
        indices = slice(offset, offset + mixdb.ft_config.R)

        if noise_energy[idx] == 0:
            snr = np.float32(np.inf)
        else:
            snr = np.float32(target_energy[idx] / noise_energy[idx])

        segsnr_t[indices] = snr

    return segsnr_t


def get_target(mixdb: MixtureDatabase, mrecord: MRecord, targets: AudiosT) -> AudioT:
    """Get the augmented target audio data for the given mixture MRecord

    :param mixdb: Mixture database
    :param mrecord: Mixture MRecord
    :param targets: List of augmented target audio data (one per target in the mixup)
    :return: Sum of augmented target audio data
    """
    # Apply impulse responses to targets
    import numpy as np

    from .audio import read_ir
    from .augmentation import apply_ir

    targets_ir = []
    for idx, target in enumerate(targets):
        ir_idx = mixdb.target_augmentation(mrecord.target_augmentation_id[idx]).ir
        if ir_idx is not None:
            targets_ir.append(apply_ir(audio=target, ir=read_ir(mixdb.impulse_response(int(ir_idx)))))
        else:
            targets_ir.append(target)

    # Return sum of targets
    return np.sum(targets_ir, axis=0)


def get_mixture_f(mixdb: MixtureDatabase, mixture: AudioT) -> AudioF:
    """Get the mixture transform for the given mixture

    :param mixdb: Mixture database
    :param mixture: Mixture audio data for the given mixid
    :return: Mixture transform data
    """
    return forward_transform(mixture, mixdb.ft_config)


def forward_transform(audio: AudioT, config: TransformConfig) -> AudioF:
    """Transform time domain data into frequency domain using the forward transform config from the feature

    A new transform is used for each call; i.e., state is not maintained between calls to forward_transform().

    :param audio: Time domain data [samples]
    :param config: Transform configuration
    :return: Frequency domain data [frames, bins]
    """
    from pyaaware import AawareForwardTransform

    from .audio import calculate_transform_from_audio

    audio_f, _ = calculate_transform_from_audio(audio=audio,
                                                transform=AawareForwardTransform(N=config.N,
                                                                                 R=config.R,
                                                                                 bin_start=config.bin_start,
                                                                                 bin_end=config.bin_end,
                                                                                 ttype=config.ttype))
    return audio_f


def inverse_transform(transform: AudioF, config: TransformConfig, trim: bool = True) -> AudioT:
    """Transform frequency domain data into time domain using the inverse transform config from the feature

    A new transform is used for each call; i.e., state is not maintained between calls to inverse_transform().

    :param transform: Frequency domain data [frames, bins]
    :param config: Transform configuration
    :param trim: Removes starting samples so output waveform will be time-aligned with input waveform to the
                 transform
    :return: Time domain data [samples]
    """
    import numpy as np
    from pyaaware import AawareInverseTransform

    from .audio import calculate_audio_from_transform

    audio, _ = calculate_audio_from_transform(data=transform,
                                              transform=AawareInverseTransform(N=config.N,
                                                                               R=config.R,
                                                                               bin_start=config.bin_start,
                                                                               bin_end=config.bin_end,
                                                                               ttype=config.ttype,
                                                                               gain=np.float32(1)),
                                              trim=trim)
    return audio


def check_audio_files_exist(mixdb: MixtureDatabase) -> None:
    """Walk through all the noise and target audio files in a mixture database ensuring that they exist
    """
    from os.path import exists

    from sonusai import SonusAIError
    from .tokenized_shell_vars import tokenized_expand

    for noise in mixdb.noises:
        file_name, _ = tokenized_expand(noise.name)
        if not exists(file_name):
            raise SonusAIError(f'Could not find {file_name}')

    for target in mixdb.targets:
        file_name, _ = tokenized_expand(target.name)
        if not exists(file_name):
            raise SonusAIError(f'Could not find {file_name}')
