from dataclasses import dataclass
from dataclasses import field
from typing import Optional
from typing import TypeAlias

import numpy as np
import numpy.typing as npt
from dataclasses_json import DataClassJsonMixin

AudioT: TypeAlias = npt.NDArray[np.float32]
AudiosT: TypeAlias = list[AudioT]

ListAudiosT: TypeAlias = list[AudiosT]

Truth: TypeAlias = npt.NDArray[np.float32]
Segsnr: TypeAlias = npt.NDArray[np.float32]

AudioF: TypeAlias = npt.NDArray[np.complex64]
AudiosF: TypeAlias = list[AudioF]

EnergyT: TypeAlias = npt.NDArray[np.float32]
EnergyF: TypeAlias = npt.NDArray[np.float32]

Feature: TypeAlias = npt.NDArray[np.float32]

Predict: TypeAlias = npt.NDArray[np.float32]

Location: TypeAlias = str

# Json type defined to maintain compatibility with DataClassJsonMixin
Json: TypeAlias = dict | list | str | int | float | bool | None


class DataClassSonusAIMixin(DataClassJsonMixin):
    def __str__(self):
        return f'{self.to_dict()}'

    # Override DataClassJsonMixin to remove dictionary keys with values of None
    def to_dict(self, encode_json=False) -> dict[str, Json]:
        def del_none(d):
            if isinstance(d, dict):
                for key, value in list(d.items()):
                    if value is None:
                        del d[key]
                    elif isinstance(value, dict):
                        del_none(value)
                    elif isinstance(value, list):
                        for item in value:
                            del_none(item)
            elif isinstance(d, list):
                for item in d:
                    del_none(item)
            return d

        return del_none(super().to_dict(encode_json))


@dataclass(frozen=True)
class TruthSetting(DataClassSonusAIMixin):
    config: Optional[dict] = None
    function: Optional[str] = None
    index: Optional[list[int]] = None

    def __hash__(self):
        return hash(self.to_json())

    def __eq__(self, other):
        return isinstance(other, TruthSetting) and hash(self) == hash(other)


TruthSettings: TypeAlias = list[TruthSetting]
OptionalNumberStr: TypeAlias = Optional[float | int | str]
OptionalListNumberStr: TypeAlias = Optional[list[float | int | str]]


@dataclass
class Augmentation(DataClassSonusAIMixin):
    normalize: OptionalNumberStr = None
    pitch: OptionalNumberStr = None
    tempo: OptionalNumberStr = None
    gain: OptionalNumberStr = None
    eq1: OptionalListNumberStr = None
    eq2: OptionalListNumberStr = None
    eq3: OptionalListNumberStr = None
    lpf: OptionalNumberStr = None
    ir: OptionalNumberStr = None
    count: Optional[int] = None
    mixup: Optional[int] = 1


Augmentations: TypeAlias = list[Augmentation]


@dataclass
class TargetFile(DataClassSonusAIMixin):
    name: Location
    samples: int
    truth_settings: TruthSettings
    class_balancing_augmentation: Optional[Augmentation] = None
    target_level_type: Optional[str] = None

    @property
    def duration(self) -> float:
        from .constants import SAMPLE_RATE

        return self.samples / SAMPLE_RATE


TargetFiles: TypeAlias = list[TargetFile]


@dataclass
class AugmentedTarget(DataClassSonusAIMixin):
    target_id: int
    target_augmentation_id: int


AugmentedTargets: TypeAlias = list[AugmentedTarget]


@dataclass
class NoiseFile(DataClassSonusAIMixin):
    name: Location
    samples: int

    @property
    def duration(self) -> float:
        from .constants import SAMPLE_RATE

        return self.samples / SAMPLE_RATE


NoiseFiles: TypeAlias = list[NoiseFile]
ClassCount: TypeAlias = list[int]

GeneralizedIDs: TypeAlias = str | int | list[int] | range


@dataclass(frozen=True)
class TruthFunctionConfig(DataClassSonusAIMixin):
    feature: str
    mutex: bool
    num_classes: int
    target_gain: float
    config: Optional[dict] = None
    function: Optional[str] = None
    index: Optional[list[int]] = None


@dataclass
class GenMixData:
    targets: Optional[AudiosT] = None
    target: Optional[AudioT] = None
    noise: Optional[AudioT] = None
    mixture: Optional[AudioT] = None
    truth_t: Optional[Truth] = None
    segsnr_t: Optional[Segsnr] = None


@dataclass
class GenFTData:
    feature: Optional[Feature] = None
    truth_f: Optional[Truth] = None
    segsnr: Optional[Segsnr] = None


@dataclass
class ImpulseResponseData:
    name: Location
    sample_rate: int
    data: AudioT

    @property
    def length(self) -> int:
        return len(self.data)


ImpulseResponseFiles: TypeAlias = list[Location]


@dataclass(frozen=True)
class SpectralMask(DataClassSonusAIMixin):
    f_max_width: int
    f_num: int
    t_max_width: int
    t_num: int
    t_max_percent: int


SpectralMasks: TypeAlias = list[SpectralMask]


@dataclass
class Mixup(DataClassSonusAIMixin):
    target_id: Optional[int] = None
    target_augmentation_id: Optional[int] = None
    target_gain: Optional[float] = None


Mixups = list[Mixup]


@dataclass
class MRecord(DataClassSonusAIMixin):
    mixups: Optional[Mixups] = None
    name: Optional[Location] = None
    noise_augmentation_id: Optional[int] = None
    noise_id: Optional[int] = None
    noise_offset: Optional[int] = None
    noise_snr_gain: Optional[float] = None
    random_snr: Optional[bool] = None
    samples: Optional[int] = None
    snr: Optional[float] = None
    spectral_mask_id: Optional[int] = None
    spectral_mask_seed: Optional[int] = None
    target_snr_gain: Optional[float] = None

    @property
    def target_id(self) -> list[int]:
        return [item.target_id for item in self.mixups]

    @property
    def target_augmentation_id(self) -> list[int]:
        return [item.target_augmentation_id for item in self.mixups]

    @property
    def target_gain(self) -> list[float]:
        return [item.target_gain for item in self.mixups]


MRecords = list[MRecord]


@dataclass
class MRecordJSON(DataClassSonusAIMixin):
    name: Optional[Location] = None
    noise_augmentation_id: Optional[int] = None
    noise_id: Optional[int] = None
    noise_offset: Optional[int] = None
    noise_snr_gain: Optional[float] = None
    random_snr: Optional[bool] = None
    samples: Optional[int] = None
    snr: Optional[float] = None
    spectral_mask_id: Optional[int] = None
    spectral_mask_seed: Optional[int] = None
    target_augmentation_id: Optional[list[int]] = None
    target_id: Optional[list[int]] = None
    target_gain: Optional[list[float]] = None
    target_snr_gain: Optional[float] = None


MRecordJSONs = list[MRecordJSON]


@dataclass(frozen=True)
class UniversalSNR:
    is_random: bool
    raw_value: float | str

    @property
    def value(self) -> float:
        if self.is_random:
            from .augmentation import evaluate_random_rule

            return float(evaluate_random_rule(str(self.raw_value)))

        return float(self.raw_value)


@dataclass(frozen=True)
class TransformConfig:
    N: int
    R: int
    bin_start: int
    bin_end: int
    ttype: str


@dataclass(frozen=True)
class FeatureGeneratorConfig:
    feature_mode: str
    num_classes: int
    truth_mutex: bool


@dataclass(frozen=True)
class FeatureGeneratorInfo:
    decimation: int
    stride: int
    step: int
    num_bands: int
    ft_config: TransformConfig
    eft_config: TransformConfig
    it_config: TransformConfig


@dataclass
class MixtureDatabaseConfig(DataClassSonusAIMixin):
    asr_manifest: list[Location] = field(default_factory=list)
    class_balancing: Optional[bool] = False
    class_labels: Optional[list[str]] = None
    class_weights_threshold: Optional[list[float]] = None
    feature: Optional[str] = None
    first_cba_id: Optional[int] = None
    ir_files: Optional[ImpulseResponseFiles] = None
    mixtures: Optional[MRecordJSONs] = None
    noise_augmentations: Optional[Augmentations] = None
    noise_mix_mode: Optional[str] = 'exhaustive'
    noises: Optional[NoiseFiles] = None
    num_classes: Optional[int] = None
    random_snrs: Optional[list[str]] = None
    seed: Optional[int] = 0
    snrs: Optional[list[float]] = None
    spectral_masks: Optional[SpectralMasks] = None
    target_augmentations: Optional[Augmentations] = None
    targets: Optional[TargetFiles] = None
    truth_mutex: Optional[bool] = None
    truth_reduction_function: Optional[str] = None
