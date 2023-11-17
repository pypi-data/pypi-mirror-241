"""sonusai genmixdb

usage: genmixdb [-hvmfs] LOC

options:
   -h, --help
   -v, --verbose    Be verbose.
   -m, --mix        Save mixture data. [default: False].
   -f, --ft         Save feature/truth_f data. [default: False].
   -s, --segsnr     Save segsnr data. [default: False].

Create mixture database data for training and evaluation. Optionally, also create mixture audio and feature/truth data.

genmixdb creates a database of training and evaluation feature and truth data generation information. It allows
the choice of audio neural-network feature types that are supported by the Aaware real-time front-end and truth
data that is synchronized frame-by-frame with the feature data.

Here are some examples:

#### Adding target data
Suppose you have an audio file which is an example, or target, of what you want to
recognize or detect. Of course, for training a NN you also need truth data for that
file (also called labels). If you don't already have it, genmixdb can create truth using
energy-based sound detection on each frame of the feature data. You can also select
different feature types. Here's an example:

genmixdb target_gfr32ts2

where target_gfr32ts2 contains config.yml with the following inside:
---
feature: gfr32ts2

targets:
  - name: data/target.wav

target_augmentations:
  - normalize: -3.5
...

The mixture database is written to a JSON file (mixdb.json) in the same directory that contains the config.yml file.

#### Target data mix with noise and augmentation

genmixdb mix_gfr32ts2.yml

where mix_gfr32ts2.yml contains:
---
feature: gfr32ts2

targets:
  - name: data/target.wav

target_augmentations:
  - normalize: -3.5
    pitch: [-3, 0, 3]
    tempo: [0.8, 1, 1.2]

noises:
  - name: data/noise.wav

noise_augmentations:
  - normalize: -3.5

snrs:
  - 20
...

In this example a time-domain mixture is created and feature data is calculated as
specified by 'feature: gfr32ts2'. Various feature types are available which vary in
spectral and temporal resolution (4 ms or higher), and other feature algorithm
parameters. The total feature size, dimension, and #frames for mixture is reported
in the log file (the log file name is genmixdb.log).

Truth (labels) can be automatically created per feature output frame based on sound
energy detection. By default, these are appended to the feature data in a single HDF5
output file. By default, truth/label generation is turned on with default algorithm
and threshold levels (see truth section) and a single class, i.e., detecting a single
type of sound. The truth format is a single float per class representing the
probability of activity/presence, and multi-class truth/labels are possible by
specifying the number of classes and either a scalar index or a vector of indices in
which to put the truth result. For example, 'num_class: 3' and  'truth_index: 2' adds
a 1x3 vector to the feature data with truth put in index 2 (others would be 0) for
data/target.wav being an audio clip from sound type of class 2.

The mixture is created with potential data augmentation functions in the following way:
1. apply noise augmentation rule
2. apply target augmentation rule
3. adjust noise gain for specific SNR
4. add augmented noise to augmented target

The mixture length is the target length by default, and the noise signal is repeated
if it is shorter, or trimmed if longer.

#### Target and noise using path lists

Target and noise audio is specified as a list containing text files, audio files, and
file globs. Text files are processed with items on each line where each item can be a
text file, an audio file, or a file glob. Each item will be searched for audio files
which can be WAV, MP3, FLAC, AIFF, or OGG format with any sample rate, bit depth, or
channel count. All audio files will be converted to 16 kHz, 16-bit, single channel
format before processing. For example,

genmixdb dog-bark.yml

where dog-bark.yml contains:
---
targets:
  - name: slib/dog-outside/*.wav
  - name: slib/dog-inside/*.wav

will find all .wav files in the specified directories and process them as targets.

"""
from dataclasses import dataclass

from sonusai import logger
from sonusai.mixture import MRecord
from sonusai.mixture import MixtureDatabase


@dataclass
class MPGlobal:
    mixdb: MixtureDatabase = None
    save_mix: bool = None
    save_ft: bool = None
    save_segsnr: bool = None


MP_GLOBAL = MPGlobal()


def genmixdb(location: str,
             save_mix: bool = False,
             save_ft: bool = False,
             save_segsnr: bool = False,
             logging: bool = True,
             show_progress: bool = False,
             test: bool = False) -> MixtureDatabase:
    from random import seed

    import yaml
    from tqdm import tqdm

    from sonusai import SonusAIError
    from sonusai import logger
    from sonusai.mixture import Augmentation
    from sonusai.mixture import SAMPLE_BYTES
    from sonusai.mixture import SAMPLE_RATE
    from sonusai.mixture import add_cba_to_target_augmentation_table
    from sonusai.mixture import balance_targets
    from sonusai.mixture import generate_mixtures
    from sonusai.mixture import get_augmentations
    from sonusai.mixture import get_augmented_targets
    from sonusai.mixture import get_ir_files
    from sonusai.mixture import get_noise_files
    from sonusai.mixture import get_target_files
    from sonusai.mixture import initialize_db
    from sonusai.mixture import load_config
    from sonusai.mixture import log_duration_and_sizes
    from sonusai.mixture import populate_asr_manifest_table
    from sonusai.mixture import populate_class_label_table
    from sonusai.mixture import populate_class_weights_threshold_table
    from sonusai.mixture import populate_impulse_response_table
    from sonusai.mixture import populate_mixture_table
    from sonusai.mixture import populate_noise_augmentation_table
    from sonusai.mixture import populate_noise_table
    from sonusai.mixture import populate_random_snr_table
    from sonusai.mixture import populate_snr_table
    from sonusai.mixture import populate_spectral_mask_table
    from sonusai.mixture import populate_target_augmentation_table
    from sonusai.mixture import populate_target_table
    from sonusai.mixture import populate_top_table
    from sonusai.mixture import update_mixid_width
    from sonusai.utils import dataclass_from_dict
    from sonusai.utils import human_readable_size
    from sonusai.utils import pp_tqdm_imap
    from sonusai.utils import seconds_to_hms

    config = load_config(location)
    initialize_db(location=location, test=test)

    mixdb = MixtureDatabase(location=location, test=test)

    populate_top_table(location, config, test)
    populate_asr_manifest_table(location, config, test)
    populate_class_label_table(location, config, test)
    populate_class_weights_threshold_table(location, config, test)
    populate_random_snr_table(location, config, test)
    populate_snr_table(location, config, test)
    populate_spectral_mask_table(location, config, test)

    seed(mixdb.seed)

    if logging:
        logger.debug(f'Seed: {mixdb.seed}')
        logger.debug('Configuration:')
        logger.debug(yaml.dump(config))

    if logging:
        logger.info('Collecting targets')
    target_files = get_target_files(config, show_progress=show_progress)
    if len(target_files) == 0:
        raise SonusAIError('Canceled due to no targets')
    populate_target_table(location, target_files, test)
    if logging:
        logger.debug('List of targets:')
        logger.debug(yaml.dump([target.name for target in mixdb.targets], default_flow_style=False))
        logger.debug('')

    if logging:
        logger.info('Collecting noises')
    noise_files = get_noise_files(config, show_progress=show_progress)
    populate_noise_table(location, noise_files, test)
    if logging:
        logger.debug('List of noises:')
        logger.debug(yaml.dump([noise.name for noise in mixdb.noises], default_flow_style=False))
        logger.debug('')

    if logging:
        logger.info('Collecting impulse responses')
    impulse_response_files = get_ir_files(config, show_progress=show_progress)
    populate_impulse_response_table(location, impulse_response_files, test)
    if logging:
        logger.debug('List of impulse responses:')
        logger.debug(
            yaml.dump([impulse_response for impulse_response in mixdb.impulse_responses], default_flow_style=False))
        logger.debug('')

    if logging:
        logger.info('Collecting target augmentations')
    target_augmentations = get_augmentations(rules=config['target_augmentations'], num_ir=mixdb.num_impulse_responses)
    class_balancing_augmentation = dataclass_from_dict(Augmentation, config['class_balancing_augmentation'])
    populate_target_augmentation_table(location, target_augmentations, test)
    if logging:
        for mixup in mixdb.mixups:
            logger.debug(f'Expanded list of target augmentations for mixup of {mixup}:')
            for target_augmentation in mixdb.target_augmentations_for_mixup(mixup):
                logger.debug(f'- {target_augmentation}')
            logger.debug('')

    if logging:
        logger.info('Collecting noise augmentations')
    noise_augmentations = get_augmentations(rules=config['noise_augmentations'], num_ir=mixdb.num_impulse_responses)
    populate_noise_augmentation_table(location, noise_augmentations, test)
    if logging:
        logger.debug('Expanded list of noise augmentations:')
        for noise_augmentation in mixdb.noise_augmentations:
            logger.debug(f'- {noise_augmentation}')
        logger.debug('')

    if logging:
        logger.debug(f'SNRs: {mixdb.snrs}\n')
        logger.debug(f'Random SNRs: {mixdb.random_snrs}\n')
        logger.debug(f'Noise mix mode: {mixdb.noise_mix_mode}\n')
        logger.debug(f'Spectral masks:')
        for spectral_mask in mixdb.spectral_masks:
            logger.debug(f'- {spectral_mask}')
        logger.debug('')

    if mixdb.truth_mutex and any(mixup > 1 for mixup in mixdb.mixups):
        raise SonusAIError(f'Mutex truth mode is not compatible with mixup')

    if logging:
        logger.info('Collecting augmented targets')
    augmented_targets = get_augmented_targets(target_files, target_augmentations)
    if config['class_balancing']:
        augmented_targets, target_augmentations = balance_targets(
            augmented_targets=augmented_targets,
            targets=target_files,
            target_augmentations=target_augmentations,
            class_balancing_augmentation=class_balancing_augmentation,
            num_classes=mixdb.num_classes,
            truth_mutex=mixdb.truth_mutex,
            num_ir=mixdb.num_impulse_responses,
            first_cba_id=mixdb.first_cba_id)
        add_cba_to_target_augmentation_table(location, target_augmentations[mixdb.first_cba_id:], test)

    total_noise_files = mixdb.num_noises * mixdb.num_noise_augmentations
    aug_noise_audio_samples = mixdb.augmented_noise_samples

    total_target_files = len(augmented_targets)
    aug_target_audio_samples = mixdb.augmented_target_samples

    if logging:
        raw_target_audio_samples = sum([targets.samples for targets in mixdb.targets])
        raw_noise_audio_duration = sum([noises.duration for noises in mixdb.noises])

        logger.info('')
        logger.info(f'Raw target audio: {mixdb.num_targets} files, '
                    f'{human_readable_size(raw_target_audio_samples * SAMPLE_BYTES, 1)}, '
                    f'{seconds_to_hms(seconds=raw_target_audio_samples / SAMPLE_RATE)}')
        logger.info(f'Raw noise audio: {mixdb.num_noises} files, '
                    f'{human_readable_size(raw_noise_audio_duration * SAMPLE_RATE * SAMPLE_BYTES, 1)}, '
                    f'{seconds_to_hms(seconds=raw_noise_audio_duration)}')

        logger.info('')
        logger.info(f'Augmented target audio: {total_target_files} files, '
                    f'{human_readable_size(aug_target_audio_samples * SAMPLE_BYTES, 1)}, '
                    f'{seconds_to_hms(seconds=aug_target_audio_samples / SAMPLE_RATE)}')
        logger.info(f'Augmented noise audio: {total_noise_files} files, '
                    f'{human_readable_size(aug_noise_audio_samples * SAMPLE_BYTES, 1)}, '
                    f'{seconds_to_hms(seconds=aug_noise_audio_samples / SAMPLE_RATE)}')

    used_noise_files, used_noise_samples, mrecords = generate_mixtures(
        noise_mix_mode=mixdb.noise_mix_mode,
        augmented_targets=augmented_targets,
        target_files=target_files,
        target_augmentations=target_augmentations,
        noise_files=noise_files,
        noise_augmentations=noise_augmentations,
        spectral_masks=mixdb.spectral_masks,
        all_snrs=mixdb.all_snrs,
        mixups=mixdb.mixups,
        num_classes=mixdb.num_classes,
        truth_mutex=mixdb.truth_mutex,
        feature_step_samples=mixdb.feature_step_samples)

    total_mixtures = len(mrecords)
    update_mixid_width(location, total_mixtures, test)
    if logging:
        logger.info('')
        logger.info(f'Found {total_mixtures:,} mixtures to process')

    total_duration = float(sum([mrecord.samples for mrecord in mrecords])) / SAMPLE_RATE

    if logging:
        log_duration_and_sizes(total_duration=total_duration,
                               num_classes=mixdb.num_classes,
                               feature_step_samples=mixdb.feature_step_samples,
                               num_bands=mixdb.fg_num_bands,
                               stride=mixdb.fg_stride,
                               desc='Estimated')
        logger.info(f'Feature shape:        '
                    f'{mixdb.fg_stride} x {mixdb.fg_num_bands} '
                    f'({mixdb.fg_stride * mixdb.fg_num_bands} total params)')
        logger.info(f'Feature samples:      {mixdb.feature_samples} samples ({mixdb.feature_ms} ms)')
        logger.info(f'Feature step samples: {mixdb.feature_step_samples} samples ({mixdb.feature_step_ms} ms)')
        logger.info('')

    # Fill in the details
    if logging:
        logger.info('Generating mixtures')
    progress = tqdm(total=total_mixtures, disable=not show_progress)
    mrecords = pp_tqdm_imap(_process_mrecord, mrecords,
                            progress=progress,
                            initializer=_initializer,
                            initargs=(location, save_mix, save_ft, save_segsnr, test))
    progress.close()

    populate_mixture_table(location, mrecords, test)

    total_samples = mixdb.total_samples()
    total_duration = float(total_samples / SAMPLE_RATE)

    if logging:
        log_duration_and_sizes(total_duration=total_duration,
                               num_classes=mixdb.num_classes,
                               feature_step_samples=mixdb.feature_step_samples,
                               num_bands=mixdb.fg_num_bands,
                               stride=mixdb.fg_stride,
                               desc='Actual')
        noise_files_percent = (float(used_noise_files) / float(total_noise_files)) * 100
        noise_samples_percent = (float(used_noise_samples) / float(aug_noise_audio_samples)) * 100
        logger.info('')
        logger.info(f'Used {noise_files_percent:,.0f}% of augmented noise files')
        logger.info(f'Used {noise_samples_percent:,.0f}% of augmented noise audio')
        logger.info('')

    if not test:
        mixdb = MixtureDatabase(location)
        mixdb.save()
        if logging:
            logger.info(f'Wrote mixture database to {location}')

    return mixdb


def _initializer(location: str, save_mix: bool, save_ft: bool, save_segsnr: bool, test: bool) -> None:
    MP_GLOBAL.mixdb = MixtureDatabase(location, test)
    MP_GLOBAL.save_mix = save_mix
    MP_GLOBAL.save_ft = save_ft
    MP_GLOBAL.save_segsnr = save_segsnr


def _process_mrecord(mrecord: MRecord) -> MRecord:
    from typing import Any

    from sonusai.mixture import get_ft
    from sonusai.mixture import get_segsnr
    from sonusai.mixture import get_truth_t
    from sonusai.mixture import update_mrecord
    from sonusai.mixture import write_mixture_data
    from sonusai.mixture import write_mrecord_metadata

    with_data = MP_GLOBAL.save_mix or MP_GLOBAL.save_ft
    mixdb = MP_GLOBAL.mixdb

    mrecord, genmix_data = update_mrecord(mixdb, mrecord, with_data)

    if with_data:
        write_data: list[tuple[str, Any]] = []

        if MP_GLOBAL.save_mix:
            write_data.append(('targets', genmix_data.targets))
            write_data.append(('noise', genmix_data.noise))
            write_data.append(('mixture', genmix_data.mixture))

        if MP_GLOBAL.save_ft:
            truth_t = get_truth_t(mixdb=mixdb,
                                  mrecord=mrecord,
                                  targets=genmix_data.targets,
                                  noise=genmix_data.noise)
            feature, truth_f = get_ft(mixdb=mixdb,
                                      mrecord=mrecord,
                                      mixture=genmix_data.mixture,
                                      truth_t=truth_t)
            write_data.append(('feature', feature))
            write_data.append(('truth_f', truth_f))

            if MP_GLOBAL.save_segsnr:
                segsnr = get_segsnr(mixdb=mixdb,
                                    mrecord=mrecord,
                                    target=genmix_data.target,
                                    noise=genmix_data.noise)
                write_data.append(('segsnr', segsnr))

        write_mixture_data(mixdb, mrecord, write_data)
        write_mrecord_metadata(mixdb, mrecord)

    return mrecord


def main() -> None:
    from docopt import docopt

    import sonusai
    from sonusai.utils import trim_docstring

    args = docopt(trim_docstring(__doc__), version=sonusai.__version__, options_first=True)

    verbose = args['--verbose']
    save_mix = args['--mix']
    save_ft = args['--ft']
    save_segsnr = args['--segsnr']
    location = args['LOC']

    import time
    from os import makedirs
    from os import remove
    from os.path import exists
    from os.path import isdir
    from os.path import join

    from sonusai import create_file_handler
    from sonusai import initial_log_messages
    from sonusai import update_console_handler
    from sonusai.utils import seconds_to_hms

    start_time = time.monotonic()

    if exists(location) and not isdir(location):
        remove(location)

    makedirs(location, exist_ok=True)

    create_file_handler(join(location, 'genmixdb.log'))
    update_console_handler(verbose)
    initial_log_messages('genmixdb')

    logger.info(f'Creating mixture database for {location}')
    logger.info('')

    genmixdb(location=location,
             save_mix=save_mix,
             save_ft=save_ft,
             save_segsnr=save_segsnr,
             show_progress=True)

    end_time = time.monotonic()
    logger.info(f'Completed in {seconds_to_hms(seconds=end_time - start_time)}')
    logger.info('')


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        logger.info('Canceled due to keyboard interrupt')
        raise SystemExit(0)
