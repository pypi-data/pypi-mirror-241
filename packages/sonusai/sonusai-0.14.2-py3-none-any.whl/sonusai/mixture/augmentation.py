from sonusai.mixture.torchaudio_augmentation import apply_torchaudio_augmentation
from sonusai.mixture.torchaudio_augmentation import apply_torchaudio_ir
from sonusai.mixture.types import AudioT
from sonusai.mixture.types import Augmentation
from sonusai.mixture.types import Augmentations
from sonusai.mixture.types import ImpulseResponseData
from sonusai.mixture.types import OptionalNumberStr


def get_augmentations(rules: list[dict] | dict, num_ir: int = 0) -> Augmentations:
    """Generate augmentations from list of input rules

    :param rules: Dictionary of augmentation config rule[s]
    :param num_ir: Number of impulse responses in config
    :return: List of augmentations
    """
    from sonusai.utils import dataclass_from_dict
    from .types import Augmentation

    processed_rules: list[dict] = []
    if not isinstance(rules, list):
        rules = [rules]

    for rule in rules:
        rule = _parse_ir(rule, num_ir)
        expand_rules(expanded_rules=processed_rules, rule=rule)

    processed_rules = randomize_rules(rules=processed_rules, num_ir=num_ir)

    return [dataclass_from_dict(Augmentation, processed_rule) for processed_rule in processed_rules]


def expand_rules(expanded_rules: list[dict], rule: dict) -> None:
    """Expand rules

    :param expanded_rules: Working list of expanded rules
    :param rule: Rule to process
    """
    from copy import deepcopy
    from numbers import Number

    from sonusai import SonusAIError
    from .constants import VALID_AUGMENTATIONS

    for key, value in list(rule.items()):
        if value is None:
            del rule[key]

    # replace old 'eq' rule with new 'eq1' rule to allow both for backward compatibility
    rule = {'eq1' if key == 'eq' else key: value for key, value in rule.items()}

    for key in rule:
        if key not in VALID_AUGMENTATIONS:
            nice_list = '\n'.join([f'  {item}' for item in VALID_AUGMENTATIONS])
            raise SonusAIError(f'Invalid augmentation: {key}.\nValid augmentations are:\n{nice_list}')

        if key in ['eq1', 'eq2', 'eq3']:
            # EQ must be a list of length 3 or a list of length 3 lists
            valid = True
            multiple = False
            if isinstance(rule[key], list):
                if any(isinstance(el, list) for el in rule[key]):
                    multiple = True
                    for value in rule[key]:
                        if not isinstance(value, list) or len(value) != 3:
                            valid = False
                else:
                    if len(rule[key]) != 3:
                        valid = False
            else:
                valid = False

            if not valid:
                raise SonusAIError(f'Invalid augmentation value for {key}: {rule[key]}')

            if multiple:
                for value in rule[key]:
                    expanded_rule = deepcopy(rule)
                    expanded_rule[key] = deepcopy(value)
                    expand_rules(expanded_rules, expanded_rule)
                return

        elif key in ['count', 'mixup']:
            pass

        else:
            if isinstance(rule[key], list):
                for value in rule[key]:
                    if isinstance(value, list):
                        raise SonusAIError(f'Invalid augmentation value for {key}: {rule[key]}')
                    expanded_rule = deepcopy(rule)
                    expanded_rule[key] = deepcopy(value)
                    expand_rules(expanded_rules, expanded_rule)
                return
            elif not isinstance(rule[key], Number):
                if not rule[key].startswith('rand'):
                    raise SonusAIError(f'Invalid augmentation value for {key}: {rule[key]}')

    expanded_rules.append(rule)


def randomize_rules(rules: list[dict], num_ir: int = 0) -> list[dict]:
    """Randomize rules

    :param rules: List of rules
    :param num_ir: Number of impulse responses in config
    :return: List of randomized rules
    """
    out_rules = []
    for in_rule in rules:
        if rule_has_rand(in_rule):
            count = 1
            if 'count' in in_rule and in_rule['count'] is not None:
                count = in_rule['count']
                del in_rule['count']
            for i in range(count):
                out_rules.append(generate_random_rule(in_rule, num_ir))
        else:
            out_rules.append(in_rule)
    return out_rules


def generate_random_rule(rule: dict, num_ir: int = 0) -> dict:
    """Generate a new rule from a rule that contains 'rand' directives

    :param rule: Rule
    :param num_ir: Number of impulse responses in config
    :return: Randomized rule
    """
    from copy import deepcopy
    from random import randint

    out_rule = deepcopy(rule)
    for key in out_rule:
        if key == 'ir' and out_rule[key] == 'rand':
            # IR is special case
            if num_ir == 0:
                out_rule[key] = None
            else:
                out_rule[key] = randint(0, num_ir - 1)
        else:
            out_rule[key] = evaluate_random_rule(str(out_rule[key]))

        # convert EQ values from strings to numbers
        if key in ['eq1', 'eq2', 'eq3']:
            for n in range(3):
                if isinstance(out_rule[key][n], str):
                    out_rule[key][n] = eval(out_rule[key][n])

    return out_rule


def rule_has_rand(rule: dict) -> bool:
    """Determine if any keys in the given rule contain 'rand'

    :param rule: Rule
    :return: True if rule contains 'rand'
    """
    for key in rule:
        if 'rand' in str(rule[key]):
            return True

    return False


def estimate_augmented_length_from_length(length: int,
                                          tempo: OptionalNumberStr = None,
                                          length_common_denominator: int = 1) -> int:
    """Estimate the length of audio after augmentation

    :param length: Number of samples in audio
    :param tempo: Tempo rule
    :param length_common_denominator: Pad resulting audio to be a multiple of this
    :return: Estimated length of augmented audio
    """
    import numpy as np

    if tempo is not None:
        length = int(np.round(length / float(tempo)))

    length += get_pad_length(length, length_common_denominator)

    return length


def estimate_augmented_length_from_audio(audio: AudioT,
                                         tempo: OptionalNumberStr = None,
                                         length_common_denominator: int = 1) -> int:
    """Estimate the length of audio after augmentation

    :param audio: Audio
    :param tempo: Tempo rule
    :param length_common_denominator: Pad resulting audio to be a multiple of this
    :return: Estimated length of augmented audio
    """
    return estimate_augmented_length_from_length(len(audio),
                                                 tempo=tempo,
                                                 length_common_denominator=length_common_denominator)


def get_mixups(augmentations: Augmentations) -> list[int]:
    """Get a list of mixup values used

    :param augmentations: List of augmentations
    :return: List of mixup values used
    """
    return sorted(list(set([augmentation.mixup for augmentation in augmentations])))


def get_augmentation_indices_for_mixup(augmentations: Augmentations, mixup: int) -> list[int]:
    """Get a list of augmentation indices for a given mixup value

    :param augmentations: List of augmentations
    :param mixup: Mixup value of interest
    :return: List of augmentation indices
    """
    indices = []
    for idx, augmentation in enumerate(augmentations):
        if mixup == augmentation.mixup:
            indices.append(idx)

    return indices


def _pad_audio(audio: AudioT, length_common_denominator: int = 1) -> AudioT:
    """Pad audio to be a multiple of given value

    :param audio: Audio
    :param length_common_denominator: Pad resulting audio to be a multiple of this
    :return: Padded audio
    """
    import numpy as np

    return np.pad(array=audio, pad_width=(0, get_pad_length(len(audio), length_common_denominator)))


def get_pad_length(length: int, length_common_denominator: int) -> int:
    """Get the number of pad samples needed

    :param length: Length of original
    :param length_common_denominator: Desired length will be a multiple of this
    :return: Number of pad samples required
    """
    mod = int(length % length_common_denominator)
    return length_common_denominator - mod if mod else 0


def pad_audio_to_length(audio: AudioT, length: int) -> AudioT:
    """Pad audio to given length

    :param audio: Audio
    :param length: Length of output
    :return: Padded audio
    """
    import numpy as np

    return np.pad(array=audio, pad_width=(0, length - len(audio)))


def apply_gain(audio: AudioT, gain: float) -> AudioT:
    """Apply gain to audio

    :param audio: Audio
    :param gain: Amount of gain
    :return: Adjusted audio
    """
    return audio * gain


def evaluate_random_rule(rule: str) -> str | float:
    """Evaluate 'rand' directive

    :param rule: Rule
    :return: Resolved value
    """
    import re
    from random import uniform

    from .constants import RAND_PATTERN

    def rand_repl(m):
        return f'{uniform(float(m.group(1)), float(m.group(4))):.2f}'

    return eval(re.sub(RAND_PATTERN, rand_repl, rule))


def _parse_ir(rule: dict, num_ir: int) -> dict:
    from sonusai import SonusAIError
    from .helpers import generic_ids_to_list

    if 'ir' not in rule:
        return rule

    ir = rule['ir']

    if ir is None:
        return rule

    if isinstance(ir, str):
        if ir == 'rand':
            return rule

        rule['ir'] = generic_ids_to_list(num_ir, ir)
        return rule

    if isinstance(ir, list):
        if not all(item in range(num_ir) for item in ir):
            raise SonusAIError(f'Invalid ir of {ir}')
        return rule

    if isinstance(ir, int):
        if ir not in range(num_ir):
            raise SonusAIError(f'Invalid ir of {ir}')
        return rule

    raise SonusAIError(f'Invalid ir of {ir}')


def apply_augmentation(audio: AudioT,
                       augmentation: Augmentation,
                       length_common_denominator: int = 1) -> AudioT:
    """Apply augmentations to audio data

    :param audio: Audio
    :param augmentation: Augmentation rule
    :param length_common_denominator: Pad resulting audio to be a multiple of this
    :return: Augmented audio
    """
    return apply_torchaudio_augmentation(audio, augmentation, length_common_denominator)


def apply_ir(audio: AudioT, ir: ImpulseResponseData) -> AudioT:
    """Apply impulse response to audio data

    :param audio: Audio
    :param ir: Impulse response data
    :return: Augmented audio
    """
    return apply_torchaudio_ir(audio, ir)
