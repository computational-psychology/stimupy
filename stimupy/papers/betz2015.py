"""Stimuli and data from Betz, Shapley, Wichmann, & Maertens (2015)
https://doi.org/10.1167/15.14.1

This module reproduces all stimuli used by Betz, Shapley, Wichmann, & Maertens
(2015) with random noise instances, and provides the corresponding lightness
effect and the baseline effect for each subject.

Each stimulus is provided by a separate function,
which can be listed using

    >>> import stimupy.papers.betz2015
    >>> help(stimupy.papers.betz2015

The output of each of these functions is a stimulus dictionary.

For a visual representation of all the stimuli
simply run this module from the shell

    $ python -m stimupy.papers.betz2015

References
----------
Betz, T., Shapley, R., Wichmann, F. A., & Maertens, M. (2015).
    Noise masking of White's illusion exposes the weakness of
    current spatial filtering models of lightness perception.
    Journal of Vision, 15(14), 1,
    https://doi.org/10.1167/15.14.1.
"""

import logging
from pathlib import Path

import numpy as np
import pandas as pd

from stimupy.noises.narrowbands import narrowband as narrowband_noise
from stimupy.stimuli.whites import white, white_two_rows
from stimupy.utils import pad_dict_to_visual_size, rotate_dict

# Get module level logger
logger = logging.getLogger("stimupy.papers.betz2015")

__all__ = [
    # Stimuli used for human experiment
    "grating08_NB058_human",  # hsf grating
    "grating08_NB100_human",
    "grating08_NB173_human",
    "grating08_NB300_human",
    "grating08_NB520_human",
    "grating08_NB900_human",
    "grating04_NB058_human",  # msf grating
    "grating04_NB100_human",
    "grating04_NB173_human",
    "grating04_NB300_human",
    "grating04_NB520_human",
    "grating04_NB900_human",
    "grating02_NB058_human",  # lsf grating
    "grating02_NB100_human",
    "grating02_NB173_human",
    "grating02_NB300_human",
    "grating02_NB520_human",
    "grating02_NB900_human",
    # Stimuli used for modeling
    "grating08_NB058_model",  # hsf grating
    "grating08_NB100_model",
    "grating08_NB173_model",
    "grating08_NB300_model",
    "grating08_NB520_model",
    "grating08_NB900_model",
    "grating04_NB058_model",  # msf grating
    "grating04_NB100_model",
    "grating04_NB173_model",
    "grating04_NB300_model",
    "grating04_NB520_model",
    "grating04_NB900_model",
    "grating02_NB058_model",  # lsf grating
    "grating02_NB100_model",
    "grating02_NB173_model",
    "grating02_NB300_model",
    "grating02_NB520_model",
    "grating02_NB900_model",
]


# Default stimulus parameters
PPD = 80
VISUAL_SIZE = 16
NOISE_FREQS = [0.58, 1.0, 1.73, 3.0, 5.2, 9.0]  # in cpd
INTENSITY_BARS = (41.8, 46.2)  # cd/m2
MEAN_LUM = 44  # cd/m2
NOISE_CONTRAST = 0.2  # in rms (std / mean)

# Load experimental data
df = pd.read_csv(Path(__file__).parents[0] / "betz2015_data.csv")


# %% Functions to generate stimuli (components)
def gen_all(ppd=PPD, skip=False):
    """Generate all stimuli in the module.

    Parameters
    ----------
    ppd : float, optional
        Pixels per degree, used for setting the visual size, by default 80.
    skip : bool, optional
        If True, skip stimuli that aren't implemented, by default False.

    Returns
    -------
    dict
        Dictionary of all stimulus dicts, keyed by name.
    """
    stims = {}  # save the stimulus-dicts in a larger dict, with name as key
    for stim_name in __all__:
        logger.info(f"Generating betz2015.{stim_name}")

        # Get a reference to the actual function
        func = globals()[stim_name]
        try:
            stim = func(ppd=ppd)

            # Accumulate
            stims[stim_name] = stim
        except NotImplementedError as e:
            if not skip:
                raise e
            # Skip stimuli that aren't implemented
            logger.info("-- not implemented")
            pass

    return stims


def _white_stimulus(n_bars, bar_width, config="human", ppd=PPD):
    # Common parameters
    stim_params = {
        "ppd": ppd,
        "intensity_bars": INTENSITY_BARS,
        "intensity_target": MEAN_LUM,
    }

    # Specific grating params
    stim_params["n_bars"] = n_bars
    stim_params["bar_width"] = np.round(bar_width * ppd) / ppd
    stim_params["target_heights"] = stim_params["bar_width"]

    # Generate differently for human vs model
    if config == "human":
        stim = white(
            **stim_params,
            target_indices=n_bars // 2,
        )
    elif config == "model":
        stim = white_two_rows(
            **stim_params,
            target_indices_bottom=n_bars // 2,
            target_indices_top=(n_bars // 2) + 1,
            target_center_offset=stim_params["bar_width"] / 2 + 1,
        )

    # Final output
    stim = rotate_dict(stim, nrots=1)
    stim = pad_dict_to_visual_size(stim, VISUAL_SIZE, ppd, MEAN_LUM)
    return stim


def white08(ppd=PPD, config="human"):
    """White stimulus (0.8 cpd) for experiments from Betz (2015).

    Parameters
    ----------
    ppd : float
        Pixels per degree, used for setting the visual size.
    config : Literal["human", "model"]
        stimulus: for "human" experiments (1 target), or "model"ing (two targets)

    Returns
    -------
    dict of str
        Dictionary with the stimulus (key: "img") and additional keys containing stimulus parameters.

    References
    ----------
    Betz, T., Shapley, R., Wichmann, F. A., & Maertens, M. (2015).
        Noise masking of White's illusion exposes the weakness of current spatial
        filtering models of lightness perception. Journal of Vision, 15(14), 1,
        https://doi.org/10.1167/15.14.1.
    """
    return _white_stimulus(n_bars=12, bar_width=0.638, config=config, ppd=ppd)


def white04(ppd=PPD, config="human"):
    """White stimulus (0.4 cpd) for experiments from Betz (2015).

    Parameters
    ----------
    ppd : float
        Pixels per degree, used for setting the visual size.
    config : Literal["human", "model"]
        stimulus: for "human" experiments (1 target), or "model"ing (two targets)

    Returns
    -------
    dict of str
        Dictionary with the stimulus (key: "img") and additional keys containing stimulus parameters.

    Reference
    ----------
    Betz, T., Shapley, R., Wichmann, F. A., & Maertens, M. (2015).
        Noise masking of White's illusion exposes the weakness of current spatial
        filtering models of lightness perception. Journal of Vision, 15(14), 1,
        https://doi.org/10.1167/15.14.1.
    """
    return _white_stimulus(n_bars=6, bar_width=1.276, config=config, ppd=ppd)


def white02(ppd=PPD, config="human"):
    """White stimulus (0.2 cpd) for experiments from Betz (2015).

    Parameters
    ----------
    ppd : float
        Pixels per degree, used for setting the visual size.
    config : Literal["human", "model"]
        stimulus: for "human" experiments (1 target), or "model"ing (two targets)

    Returns
    -------
    dict of str
        Dictionary with the stimulus (key: "img") and additional keys containing stimulus parameters.

    Reference
    ----------
    Betz, T., Shapley, R., Wichmann, F. A., & Maertens, M. (2015).
        Noise masking of White's illusion exposes the weakness of current spatial
        filtering models of lightness perception. Journal of Vision, 15(14), 1,
        https://doi.org/10.1167/15.14.1.
    """
    return _white_stimulus(n_bars=4, bar_width=2.552, config=config, ppd=ppd)


def _create_noise(noise_freq, noise_contrast=NOISE_CONTRAST, mean_lum=MEAN_LUM, ppd=PPD, rng=None):
    # Create noise texture
    noise = narrowband_noise(
        visual_size=VISUAL_SIZE,
        ppd=ppd,
        center_frequency=noise_freq,
        bandwidth=1.0,
        pseudo_noise=True,
        rng=rng,
    )

    # Adjust contrast
    noise["img"] -= noise["img"].mean()  # center
    noise["img"] /= noise["img"].std()  # z-transform
    noise["img"] *= noise_contrast * mean_lum  # adjust contrast
    noise["contrast"] = noise_contrast

    noise["noise_frequency"] = noise.pop("center_frequency")

    return noise


def _mask_stim_with_noise(stim, noise_freq, rng=None):
    # Create noise
    noise = _create_noise(
        noise_freq=noise_freq, ppd=stim["ppd"], noise_contrast=NOISE_CONTRAST, rng=rng
    )

    # Combine
    stim["noise"] = noise.pop("img")
    stim["img"] += stim["noise"]
    stim.update(noise)

    return stim


# %% High spatial frequency grating: Human experiment
def grating08_NB058_human(ppd=PPD, rng=None):
    """White stimulus (0.8 cpd) masked with 0.58 cpd noise for human experiments from Betz (2015).

    Parameters
    ----------
    ppd : float
        Pixels per degree, used for setting the visual size.

    Returns
    -------
    dict of str
        Dictionary with the stimulus (key: "img") and additional keys containing stimulus parameters.

    Reference
    ----------
    Betz, T., Shapley, R., Wichmann, F. A., & Maertens, M. (2015).
        Noise masking of White's illusion exposes the weakness of current spatial
        filtering models of lightness perception. Journal of Vision, 15(14), 1,
        https://doi.org/10.1167/15.14.1.
    """
    # White's stimulus
    grating_freq = 0.8
    stim = white08(ppd=ppd, config="human")

    # Noise mask
    noise_freq = 0.58
    stim = _mask_stim_with_noise(stim, noise_freq, rng=rng)

    # Add experimental data
    stim["experimental_data"] = {
        "baseline_effect": df[
            (df.grating == grating_freq) & (df.noiseType == "baseline")
        ].reset_index(drop=True),
        "noise_effect": df[
            (df.grating == grating_freq) & (df.noiseType == str(noise_freq))
        ].reset_index(drop=True),
    }

    return stim


def grating08_NB100_human(ppd=PPD, rng=None):
    """White stimulus (0.8 cpd) masked with 1.00 cpd noise for human experiments from Betz (2015).

    Parameters
    ----------
    ppd : float
        Pixels per degree, used for setting the visual size.

    Returns
    -------
    dict of str
        Dictionary with the stimulus (key: "img") and additional keys containing stimulus parameters.

    Reference
    ----------
    Betz, T., Shapley, R., Wichmann, F. A., & Maertens, M. (2015).
        Noise masking of White's illusion exposes the weakness of current spatial
        filtering models of lightness perception. Journal of Vision, 15(14), 1,
        https://doi.org/10.1167/15.14.1.
    """
    # White's stimulus
    grating_freq = 0.8
    stim = white08(ppd=ppd, config="human")

    # Noise mask
    noise_freq = 1.00
    stim = _mask_stim_with_noise(stim, noise_freq, rng=rng)

    # Add experimental data
    stim["experimental_data"] = {
        "baseline_effect": df[
            (df.grating == grating_freq) & (df.noiseType == "baseline")
        ].reset_index(drop=True),
        "noise_effect": df[
            (df.grating == grating_freq) & (df.noiseType == str(noise_freq))
        ].reset_index(drop=True),
    }

    return stim


def grating08_NB173_human(ppd=PPD, rng=None):
    """White stimulus (0.8 cpd) masked with 1.73 cpd noise for human experiments from Betz (2015).

    Parameters
    ----------
    ppd : float
        Pixels per degree, used for setting the visual size.

    Returns
    -------
    dict of str
        Dictionary with the stimulus (key: "img") and additional keys containing stimulus parameters.

    Reference
    ----------
    Betz, T., Shapley, R., Wichmann, F. A., & Maertens, M. (2015).
        Noise masking of White's illusion exposes the weakness of current spatial
        filtering models of lightness perception. Journal of Vision, 15(14), 1,
        https://doi.org/10.1167/15.14.1.
    """
    # White's stimulus
    grating_freq = 0.8
    stim = white08(ppd=ppd, config="human")

    # Noise mask
    noise_freq = 1.73
    stim = _mask_stim_with_noise(stim, noise_freq, rng=rng)

    # Add experimental data
    stim["experimental_data"] = {
        "baseline_effect": df[
            (df.grating == grating_freq) & (df.noiseType == "baseline")
        ].reset_index(drop=True),
        "noise_effect": df[
            (df.grating == grating_freq) & (df.noiseType == str(noise_freq))
        ].reset_index(drop=True),
    }

    return stim


def grating08_NB300_human(ppd=PPD, rng=None):
    """White stimulus (0.8 cpd) masked with 3.00 cpd noise for human experiments from Betz (2015).

    Parameters
    ----------
    ppd : float
        Pixels per degree, used for setting the visual size.

    Returns
    -------
    dict of str
        Dictionary with the stimulus (key: "img") and additional keys containing stimulus parameters.

    Reference
    ----------
    Betz, T., Shapley, R., Wichmann, F. A., & Maertens, M. (2015).
        Noise masking of White's illusion exposes the weakness of current spatial
        filtering models of lightness perception. Journal of Vision, 15(14), 1,
        https://doi.org/10.1167/15.14.1.
    """
    # White's stimulus
    grating_freq = 0.8
    stim = white08(ppd=ppd, config="human")

    # Noise mask
    noise_freq = 3.00
    stim = _mask_stim_with_noise(stim, noise_freq, rng=rng)

    # Add experimental data
    stim["experimental_data"] = {
        "baseline_effect": df[
            (df.grating == grating_freq) & (df.noiseType == "baseline")
        ].reset_index(drop=True),
        "noise_effect": df[
            (df.grating == grating_freq) & (df.noiseType == str(noise_freq))
        ].reset_index(drop=True),
    }

    return stim


def grating08_NB520_human(ppd=PPD, rng=None):
    """White stimulus (0.8 cpd) masked with 5.20 cpd noise for human experiments from Betz (2015).

    Parameters
    ----------
    ppd : float
        Pixels per degree, used for setting the visual size.

    Returns
    -------
    dict of str
        Dictionary with the stimulus (key: "img") and additional keys containing stimulus parameters.

    Reference
    ----------
    Betz, T., Shapley, R., Wichmann, F. A., & Maertens, M. (2015).
        Noise masking of White's illusion exposes the weakness of current spatial
        filtering models of lightness perception. Journal of Vision, 15(14), 1,
        https://doi.org/10.1167/15.14.1.
    """
    # White's stimulus
    grating_freq = 0.8
    stim = white08(ppd=ppd, config="human")

    # Noise mask
    noise_freq = 5.20
    stim = _mask_stim_with_noise(stim, noise_freq, rng=rng)

    # Add experimental data
    stim["experimental_data"] = {
        "baseline_effect": df[
            (df.grating == grating_freq) & (df.noiseType == "baseline")
        ].reset_index(drop=True),
        "noise_effect": df[
            (df.grating == grating_freq) & (df.noiseType == str(noise_freq))
        ].reset_index(drop=True),
    }

    return stim


def grating08_NB900_human(ppd=PPD, rng=None):
    """White stimulus (0.8 cpd) masked with 9.00 cpd noise for human experiments from Betz (2015).

    Parameters
    ----------
    ppd : float
        Pixels per degree, used for setting the visual size.

    Returns
    -------
    dict of str
        Dictionary with the stimulus (key: "img") and additional keys containing stimulus parameters.

    Reference
    ----------
    Betz, T., Shapley, R., Wichmann, F. A., & Maertens, M. (2015).
        Noise masking of White's illusion exposes the weakness of current spatial
        filtering models of lightness perception. Journal of Vision, 15(14), 1,
        https://doi.org/10.1167/15.14.1.
    """
    # White's stimulus
    grating_freq = 0.8
    stim = white08(ppd=ppd, config="human")

    # Noise mask
    noise_freq = 9.00
    stim = _mask_stim_with_noise(stim, noise_freq, rng=rng)

    # Add experimental data
    stim["experimental_data"] = {
        "baseline_effect": df[
            (df.grating == grating_freq) & (df.noiseType == "baseline")
        ].reset_index(drop=True),
        "noise_effect": df[
            (df.grating == grating_freq) & (df.noiseType == str(noise_freq))
        ].reset_index(drop=True),
    }

    return stim


# %% Mid spatial frequency grating: Human experiment
def grating04_NB058_human(ppd=PPD, rng=None):
    """White stimulus (0.4 cpd) masked with 0.58 cpd noise for human experiments from Betz (2015).

    Parameters
    ----------
    ppd : float
        Pixels per degree, used for setting the visual size.

    Returns
    -------
    dict of str
        Dictionary with the stimulus (key: "img") and additional keys containing stimulus parameters.

    Reference
    ----------
    Betz, T., Shapley, R., Wichmann, F. A., & Maertens, M. (2015).
        Noise masking of White's illusion exposes the weakness of current spatial
        filtering models of lightness perception. Journal of Vision, 15(14), 1,
        https://doi.org/10.1167/15.14.1.
    """
    # White's stimulus
    grating_freq = 0.4
    stim = white08(ppd=ppd, config="human")
    noise_freq = 1.00
    stim = _mask_stim_with_noise(stim, noise_freq, rng=rng)
    noise_freq = 0.58
    stim = _mask_stim_with_noise(stim, noise_freq, rng=rng)

    # Add experimental data
    stim["experimental_data"] = {
        "baseline_effect": df[
            (df.grating == grating_freq) & (df.noiseType == "baseline")
        ].reset_index(drop=True),
        "noise_effect": df[
            (df.grating == grating_freq) & (df.noiseType == str(noise_freq))
        ].reset_index(drop=True),
    }

    return stim


def grating04_NB100_human(ppd=PPD, rng=None):
    """White stimulus (0.4 cpd) masked with 1.00 cpd noise for human experiments from Betz (2015).

    Parameters
    ----------
    ppd : float
        Pixels per degree, used for setting the visual size.

    Returns
    -------
    dict of str
        Dictionary with the stimulus (key: "img") and additional keys containing stimulus parameters.

    Reference
    ----------
    Betz, T., Shapley, R., Wichmann, F. A., & Maertens, M. (2015).
        Noise masking of White's illusion exposes the weakness of current spatial
        filtering models of lightness perception. Journal of Vision, 15(14), 1,
        https://doi.org/10.1167/15.14.1.
    """
    # White's stimulus
    grating_freq = 0.4
    stim = white08(ppd=ppd, config="human")
    noise_freq = 1.73
    stim = _mask_stim_with_noise(stim, noise_freq, rng=rng)
    noise_freq = 1.00
    stim = _mask_stim_with_noise(stim, noise_freq, rng=rng)

    # Add experimental data
    stim["experimental_data"] = {
        "baseline_effect": df[
            (df.grating == grating_freq) & (df.noiseType == "baseline")
        ].reset_index(drop=True),
        "noise_effect": df[
            (df.grating == grating_freq) & (df.noiseType == str(noise_freq))
        ].reset_index(drop=True),
    }

    return stim


def grating04_NB173_human(ppd=PPD, rng=None):
    """White stimulus (0.4 cpd) masked with 1.73 cpd noise for human experiments from Betz (2015).

    Parameters
    ----------
    ppd : float
        Pixels per degree, used for setting the visual size.

    Returns
    -------
    dict of str
        Dictionary with the stimulus (key: "img") and additional keys containing stimulus parameters.

    Reference
    ----------
    Betz, T., Shapley, R., Wichmann, F. A., & Maertens, M. (2015).
        Noise masking of White's illusion exposes the weakness of current spatial
        filtering models of lightness perception. Journal of Vision, 15(14), 1,
        https://doi.org/10.1167/15.14.1.
    """
    # White's stimulus
    grating_freq = 0.4
    stim = white04(ppd=ppd, config="human")

    # Noise mask
    noise_freq = 1.73
    stim = _mask_stim_with_noise(stim, noise_freq, rng=rng)

    # Add experimental data
    stim["experimental_data"] = {
        "baseline_effect": df[
            (df.grating == grating_freq) & (df.noiseType == "baseline")
        ].reset_index(drop=True),
        "noise_effect": df[
            (df.grating == grating_freq) & (df.noiseType == str(noise_freq))
        ].reset_index(drop=True),
    }

    return stim


def grating04_NB300_human(ppd=PPD, rng=None):
    """White stimulus (0.4 cpd) masked with 3.00 cpd noise for human experiments from Betz (2015).

    Parameters
    ----------
    ppd : float
        Pixels per degree, used for setting the visual size.

    Returns
    -------
    dict of str
        Dictionary with the stimulus (key: "img") and additional keys containing stimulus parameters.

    Reference
    ----------
    Betz, T., Shapley, R., Wichmann, F. A., & Maertens, M. (2015).
        Noise masking of White's illusion exposes the weakness of current spatial
        filtering models of lightness perception. Journal of Vision, 15(14), 1,
        https://doi.org/10.1167/15.14.1.
    """
    # White's stimulus
    grating_freq = 0.4
    stim = white04(ppd=ppd, config="human")

    # Noise mask
    noise_freq = 3.00
    stim = _mask_stim_with_noise(stim, noise_freq, rng=rng)

    # Add experimental data
    stim["experimental_data"] = {
        "baseline_effect": df[
            (df.grating == grating_freq) & (df.noiseType == "baseline")
        ].reset_index(drop=True),
        "noise_effect": df[
            (df.grating == grating_freq) & (df.noiseType == str(noise_freq))
        ].reset_index(drop=True),
    }

    return stim


def grating04_NB520_human(ppd=PPD, rng=None):
    """White stimulus (0.4 cpd) masked with 5.20 cpd noise for human experiments from Betz (2015).

    Parameters
    ----------
    ppd : float
        Pixels per degree, used for setting the visual size.

    Returns
    -------
    dict of str
        Dictionary with the stimulus (key: "img") and additional keys containing stimulus parameters.

    Reference
    ----------
    Betz, T., Shapley, R., Wichmann, F. A., & Maertens, M. (2015).
        Noise masking of White's illusion exposes the weakness of current spatial
        filtering models of lightness perception. Journal of Vision, 15(14), 1,
        https://doi.org/10.1167/15.14.1.
    """
    # White's stimulus
    grating_freq = 0.4
    stim = white04(ppd=ppd, config="human")

    # Noise mask
    noise_freq = 5.20
    stim = _mask_stim_with_noise(stim, noise_freq, rng=rng)

    # Add experimental data
    stim["experimental_data"] = {
        "baseline_effect": df[
            (df.grating == grating_freq) & (df.noiseType == "baseline")
        ].reset_index(drop=True),
        "noise_effect": df[
            (df.grating == grating_freq) & (df.noiseType == str(noise_freq))
        ].reset_index(drop=True),
    }

    return stim


def grating04_NB900_human(ppd=PPD, rng=None):
    """White stimulus (0.4 cpd) masked with 9.00 cpd noise for human experiments from Betz (2015).

    Parameters
    ----------
    ppd : float
        Pixels per degree, used for setting the visual size.

    Returns
    -------
    dict of str
        Dictionary with the stimulus (key: "img") and additional keys containing stimulus parameters.

    Reference
    ----------
    Betz, T., Shapley, R., Wichmann, F. A., & Maertens, M. (2015).
        Noise masking of White's illusion exposes the weakness of current spatial
        filtering models of lightness perception. Journal of Vision, 15(14), 1,
        https://doi.org/10.1167/15.14.1.
    """
    # White's stimulus
    grating_freq = 0.4
    stim = white04(ppd=ppd, config="human")

    # Noise mask
    noise_freq = 9.00
    stim = _mask_stim_with_noise(stim, noise_freq, rng=rng)

    # Add experimental data
    stim["experimental_data"] = {
        "baseline_effect": df[
            (df.grating == grating_freq) & (df.noiseType == "baseline")
        ].reset_index(drop=True),
        "noise_effect": df[
            (df.grating == grating_freq) & (df.noiseType == str(noise_freq))
        ].reset_index(drop=True),
    }

    return stim


# %% Low spatial frequency grating: Human experiment
def grating02_NB058_human(ppd=PPD, rng=None):
    """White stimulus (0.2 cpd) masked with 0.58 cpd noise for human experiments from Betz (2015).

    Parameters
    ----------
    ppd : float
        Pixels per degree, used for setting the visual size.

    Returns
    -------
    dict of str
        Dictionary with the stimulus (key: "img") and additional keys containing stimulus parameters.

    Reference
    ----------
    Betz, T., Shapley, R., Wichmann, F. A., & Maertens, M. (2015).
        Noise masking of White's illusion exposes the weakness of current spatial
        filtering models of lightness perception. Journal of Vision, 15(14), 1,
        https://doi.org/10.1167/15.14.1.
    """
    # White's stimulus
    grating_freq = 0.2
    stim = white02(ppd=ppd, config="human")

    # Noise mask
    noise_freq = 0.58
    stim = _mask_stim_with_noise(stim, noise_freq, rng=rng)

    # Add experimental data
    stim["experimental_data"] = {
        "baseline_effect": df[
            (df.grating == grating_freq) & (df.noiseType == "baseline")
        ].reset_index(drop=True),
        "noise_effect": df[
            (df.grating == grating_freq) & (df.noiseType == str(noise_freq))
        ].reset_index(drop=True),
    }

    return stim


def grating02_NB100_human(ppd=PPD, rng=None):
    """White stimulus (0.2 cpd) masked with 1.00 cpd noise for human experiments from Betz (2015).

    Parameters
    ----------
    ppd : float
        Pixels per degree, used for setting the visual size.

    Returns
    -------
    dict of str
        Dictionary with the stimulus (key: "img") and additional keys containing stimulus parameters.

    Reference
    ----------
    Betz, T., Shapley, R., Wichmann, F. A., & Maertens, M. (2015).
        Noise masking of White's illusion exposes the weakness of current spatial
        filtering models of lightness perception. Journal of Vision, 15(14), 1,
        https://doi.org/10.1167/15.14.1.
    """
    # White's stimulus
    grating_freq = 0.2
    stim = white02(ppd=ppd, config="human")

    # Noise mask
    noise_freq = 1.00
    stim = _mask_stim_with_noise(stim, noise_freq, rng=rng)

    # Add experimental data
    stim["experimental_data"] = {
        "baseline_effect": df[
            (df.grating == grating_freq) & (df.noiseType == "baseline")
        ].reset_index(drop=True),
        "noise_effect": df[
            (df.grating == grating_freq) & (df.noiseType == str(noise_freq))
        ].reset_index(drop=True),
    }

    return stim


def grating02_NB173_human(ppd=PPD, rng=None):
    """White stimulus (0.2 cpd) masked with 1.73 cpd noise for human experiments from Betz (2015).

    Parameters
    ----------
    ppd : float
        Pixels per degree, used for setting the visual size.

    Returns
    -------
    dict of str
        Dictionary with the stimulus (key: "img") and additional keys containing stimulus parameters.

    Reference
    ----------
    Betz, T., Shapley, R., Wichmann, F. A., & Maertens, M. (2015).
        Noise masking of White's illusion exposes the weakness of current spatial
        filtering models of lightness perception. Journal of Vision, 15(14), 1,
        https://doi.org/10.1167/15.14.1.
    """
    # White's stimulus
    grating_freq = 0.2
    stim = white02(ppd=ppd, config="human")

    # Noise mask
    noise_freq = 1.73
    stim = _mask_stim_with_noise(stim, noise_freq, rng=rng)

    # Add experimental data
    stim["experimental_data"] = {
        "baseline_effect": df[
            (df.grating == grating_freq) & (df.noiseType == "baseline")
        ].reset_index(drop=True),
        "noise_effect": df[
            (df.grating == grating_freq) & (df.noiseType == str(noise_freq))
        ].reset_index(drop=True),
    }

    return stim


def grating02_NB300_human(ppd=PPD, rng=None):
    """White stimulus (0.2 cpd) masked with 3.00 cpd noise for human experiments from Betz (2015).

    Parameters
    ----------
    ppd : float
        Pixels per degree, used for setting the visual size.

    Returns
    -------
    dict of str
        Dictionary with the stimulus (key: "img") and additional keys containing stimulus parameters.

    Reference
    ----------
    Betz, T., Shapley, R., Wichmann, F. A., & Maertens, M. (2015).
        Noise masking of White's illusion exposes the weakness of current spatial
        filtering models of lightness perception. Journal of Vision, 15(14), 1,
        https://doi.org/10.1167/15.14.1.
    """
    # White's stimulus
    grating_freq = 0.2
    stim = white02(ppd=ppd, config="human")

    # Noise mask
    noise_freq = 3.00
    stim = _mask_stim_with_noise(stim, noise_freq, rng=rng)

    # Add experimental data
    stim["experimental_data"] = {
        "baseline_effect": df[
            (df.grating == grating_freq) & (df.noiseType == "baseline")
        ].reset_index(drop=True),
        "noise_effect": df[
            (df.grating == grating_freq) & (df.noiseType == str(noise_freq))
        ].reset_index(drop=True),
    }

    return stim


def grating02_NB520_human(ppd=PPD, rng=None):
    """White stimulus (0.2 cpd) masked with 5.20 cpd noise for human experiments from Betz (2015).

    Parameters
    ----------
    ppd : float
        Pixels per degree, used for setting the visual size.

    Returns
    -------
    dict of str
        Dictionary with the stimulus (key: "img") and additional keys containing stimulus parameters.

    Reference
    ----------
    Betz, T., Shapley, R., Wichmann, F. A., & Maertens, M. (2015).
        Noise masking of White's illusion exposes the weakness of current spatial
        filtering models of lightness perception. Journal of Vision, 15(14), 1,
        https://doi.org/10.1167/15.14.1.
    """
    # White's stimulus
    grating_freq = 0.2
    stim = white02(ppd=ppd, config="human")

    # Noise mask
    noise_freq = 5.20
    stim = _mask_stim_with_noise(stim, noise_freq, rng=rng)

    # Add experimental data
    stim["experimental_data"] = {
        "baseline_effect": df[
            (df.grating == grating_freq) & (df.noiseType == "baseline")
        ].reset_index(drop=True),
        "noise_effect": df[
            (df.grating == grating_freq) & (df.noiseType == str(noise_freq))
        ].reset_index(drop=True),
    }

    return stim


def grating02_NB900_human(ppd=PPD, rng=None):
    """White stimulus (0.2 cpd) masked with 9.00 cpd noise for human experiments from Betz (2015).

    Parameters
    ----------
    ppd : float
        Pixels per degree, used for setting the visual size.

    Returns
    -------
    dict of str
        Dictionary with the stimulus (key: "img") and additional keys containing stimulus parameters.

    Reference
    ----------
    Betz, T., Shapley, R., Wichmann, F. A., & Maertens, M. (2015).
        Noise masking of White's illusion exposes the weakness of current spatial
        filtering models of lightness perception. Journal of Vision, 15(14), 1,
        https://doi.org/10.1167/15.14.1.
    """
    # White's stimulus
    grating_freq = 0.2
    stim = white04(ppd=ppd, config="human")

    # Noise mask
    noise_freq = 9.00
    stim = _mask_stim_with_noise(stim, noise_freq, rng=rng)

    # Add experimental data
    stim["experimental_data"] = {
        "baseline_effect": df[
            (df.grating == grating_freq) & (df.noiseType == "baseline")
        ].reset_index(drop=True),
        "noise_effect": df[
            (df.grating == grating_freq) & (df.noiseType == str(noise_freq))
        ].reset_index(drop=True),
    }

    return stim


# %% High spatial frequency grating: Modeling
def grating08_NB058_model(ppd=PPD, rng=None):
    """White stimulus (0.8 cpd) masked with 0.58 cpd noise for model simulations from Betz (2015).

    Parameters
    ----------
    ppd : float
        Pixels per degree, used for setting the visual size.

    Returns
    -------
    dict of str
        Dictionary with the stimulus (key: "img") and additional keys containing stimulus parameters.

    Reference
    ----------
    Betz, T., Shapley, R., Wichmann, F. A., & Maertens, M. (2015).
        Noise masking of White's illusion exposes the weakness of current spatial
        filtering models of lightness perception. Journal of Vision, 15(14), 1,
        https://doi.org/10.1167/15.14.1.
    """
    # White's stimulus
    grating_freq = 0.8
    stim = white08(ppd=ppd, config="model")

    # Noise mask
    noise_freq = 0.58
    stim = _mask_stim_with_noise(stim, noise_freq, rng=rng)

    # Add experimental data
    stim["experimental_data"] = {
        "baseline_effect": df[
            (df.grating == grating_freq) & (df.noiseType == "baseline")
        ].reset_index(drop=True),
        "noise_effect": df[
            (df.grating == grating_freq) & (df.noiseType == str(noise_freq))
        ].reset_index(drop=True),
    }

    return stim


def grating08_NB100_model(ppd=PPD, rng=None):
    """White stimulus (0.8 cpd) masked with 1.00 cpd noise for model simulations from Betz (2015).

    Parameters
    ----------
    ppd : float
        Pixels per degree, used for setting the visual size.

    Returns
    -------
    dict of str
        Dictionary with the stimulus (key: "img") and additional keys containing stimulus parameters.

    Reference
    ----------
    Betz, T., Shapley, R., Wichmann, F. A., & Maertens, M. (2015).
        Noise masking of White's illusion exposes the weakness of current spatial
        filtering models of lightness perception. Journal of Vision, 15(14), 1,
        https://doi.org/10.1167/15.14.1.
    """
    # White's stimulus
    grating_freq = 0.8
    stim = white08(ppd=ppd, config="model")

    # Noise mask
    noise_freq = 1.00
    stim = _mask_stim_with_noise(stim, noise_freq, rng=rng)

    # Add experimental data
    stim["experimental_data"] = {
        "baseline_effect": df[
            (df.grating == grating_freq) & (df.noiseType == "baseline")
        ].reset_index(drop=True),
        "noise_effect": df[
            (df.grating == grating_freq) & (df.noiseType == str(noise_freq))
        ].reset_index(drop=True),
    }

    return stim


def grating08_NB173_model(ppd=PPD, rng=None):
    """White stimulus (0.8 cpd) masked with 1.73 cpd noise for model simulations from Betz (2015).

    Parameters
    ----------
    ppd : float
        Pixels per degree, used for setting the visual size.

    Returns
    -------
    dict of str
        Dictionary with the stimulus (key: "img") and additional keys containing stimulus parameters.

    Reference
    ----------
    Betz, T., Shapley, R., Wichmann, F. A., & Maertens, M. (2015).
        Noise masking of White's illusion exposes the weakness of current spatial
        filtering models of lightness perception. Journal of Vision, 15(14), 1,
        https://doi.org/10.1167/15.14.1.
    """
    # White's stimulus
    grating_freq = 0.8
    stim = white08(ppd=ppd, config="model")

    # Noise mask
    noise_freq = 1.73
    stim = _mask_stim_with_noise(stim, noise_freq, rng=rng)

    # Add experimental data
    stim["experimental_data"] = {
        "baseline_effect": df[
            (df.grating == grating_freq) & (df.noiseType == "baseline")
        ].reset_index(drop=True),
        "noise_effect": df[
            (df.grating == grating_freq) & (df.noiseType == str(noise_freq))
        ].reset_index(drop=True),
    }

    return stim


def grating08_NB300_model(ppd=PPD, rng=None):
    """White stimulus (0.8 cpd) masked with 3.00 cpd noise for model simulations from Betz (2015).

    Parameters
    ----------
    ppd : float
        Pixels per degree, used for setting the visual size.

    Returns
    -------
    dict of str
        Dictionary with the stimulus (key: "img") and additional keys containing stimulus parameters.

    Reference
    ----------
    Betz, T., Shapley, R., Wichmann, F. A., & Maertens, M. (2015).
        Noise masking of White's illusion exposes the weakness of current spatial
        filtering models of lightness perception. Journal of Vision, 15(14), 1,
        https://doi.org/10.1167/15.14.1.
    """
    # White's stimulus
    grating_freq = 0.8
    stim = white08(ppd=ppd, config="model")

    # Noise mask
    noise_freq = 3.00
    stim = _mask_stim_with_noise(stim, noise_freq, rng=rng)

    # Add experimental data
    stim["experimental_data"] = {
        "baseline_effect": df[
            (df.grating == grating_freq) & (df.noiseType == "baseline")
        ].reset_index(drop=True),
        "noise_effect": df[
            (df.grating == grating_freq) & (df.noiseType == str(noise_freq))
        ].reset_index(drop=True),
    }

    return stim


def grating08_NB520_model(ppd=PPD, rng=None):
    """White stimulus (0.8 cpd) masked with 5.20 cpd noise for model simulations from Betz (2015).

    Parameters
    ----------
    ppd : float
        Pixels per degree, used for setting the visual size.

    Returns
    -------
    dict of str
        Dictionary with the stimulus (key: "img") and additional keys containing stimulus parameters.

    Reference
    ----------
    Betz, T., Shapley, R., Wichmann, F. A., & Maertens, M. (2015).
        Noise masking of White's illusion exposes the weakness of current spatial
        filtering models of lightness perception. Journal of Vision, 15(14), 1,
        https://doi.org/10.1167/15.14.1.
    """
    # White's stimulus
    grating_freq = 0.8
    stim = white08(ppd=ppd, config="model")

    # Noise mask
    noise_freq = 5.20
    stim = _mask_stim_with_noise(stim, noise_freq, rng=rng)

    # Add experimental data
    stim["experimental_data"] = {
        "baseline_effect": df[
            (df.grating == grating_freq) & (df.noiseType == "baseline")
        ].reset_index(drop=True),
        "noise_effect": df[
            (df.grating == grating_freq) & (df.noiseType == str(noise_freq))
        ].reset_index(drop=True),
    }

    return stim


def grating08_NB900_model(ppd=PPD, rng=None):
    """White stimulus (0.8 cpd) masked with 9.00 cpd noise for model simulations from Betz (2015).

    Parameters
    ----------
    ppd : float
        Pixels per degree, used for setting the visual size.

    Returns
    -------
    dict of str
        Dictionary with the stimulus (key: "img") and additional keys containing stimulus parameters.

    Reference
    ----------
    Betz, T., Shapley, R., Wichmann, F. A., & Maertens, M. (2015).
        Noise masking of White's illusion exposes the weakness of current spatial
        filtering models of lightness perception. Journal of Vision, 15(14), 1,
        https://doi.org/10.1167/15.14.1.
    """
    # White's stimulus
    grating_freq = 0.8
    stim = white08(ppd=ppd, config="model")

    # Noise mask
    noise_freq = 9.00
    stim = _mask_stim_with_noise(stim, noise_freq, rng=rng)

    # Add experimental data
    stim["experimental_data"] = {
        "baseline_effect": df[
            (df.grating == grating_freq) & (df.noiseType == "baseline")
        ].reset_index(drop=True),
        "noise_effect": df[
            (df.grating == grating_freq) & (df.noiseType == str(noise_freq))
        ].reset_index(drop=True),
    }

    return stim


# %% Mid spatial frequency grating: Modeling
def grating04_NB058_model(ppd=PPD, rng=None):
    """White stimulus (0.4 cpd) masked with 0.58 cpd noise for model simulations from Betz (2015).

    Parameters
    ----------
    ppd : float
        Pixels per degree, used for setting the visual size.

    Returns
    -------
    dict of str
        Dictionary with the stimulus (key: "img") and additional keys containing stimulus parameters.

    Reference
    ----------
    Betz, T., Shapley, R., Wichmann, F. A., & Maertens, M. (2015).
        Noise masking of White's illusion exposes the weakness of current spatial
        filtering models of lightness perception. Journal of Vision, 15(14), 1,
        https://doi.org/10.1167/15.14.1.
    """
    # White's stimulus
    grating_freq = 0.4
    stim = white04(ppd=ppd, config="model")

    # Noise mask
    noise_freq = 0.58
    stim = _mask_stim_with_noise(stim, noise_freq, rng=rng)

    # Add experimental data
    stim["experimental_data"] = {
        "baseline_effect": df[
            (df.grating == grating_freq) & (df.noiseType == "baseline")
        ].reset_index(drop=True),
        "noise_effect": df[
            (df.grating == grating_freq) & (df.noiseType == str(noise_freq))
        ].reset_index(drop=True),
    }

    return stim


def grating04_NB100_model(ppd=PPD, rng=None):
    """White stimulus (0.4 cpd) masked with 1.00 cpd noise for model simulations from Betz (2015).

    Parameters
    ----------
    ppd : float
        Pixels per degree, used for setting the visual size.

    Returns
    -------
    dict of str
        Dictionary with the stimulus (key: "img") and additional keys containing stimulus parameters.

    Reference
    ----------
    Betz, T., Shapley, R., Wichmann, F. A., & Maertens, M. (2015).
        Noise masking of White's illusion exposes the weakness of current spatial
        filtering models of lightness perception. Journal of Vision, 15(14), 1,
        https://doi.org/10.1167/15.14.1.
    """
    # White's stimulus
    grating_freq = 0.4
    stim = white04(ppd=ppd, config="model")

    # Noise mask
    noise_freq = 1.00
    stim = _mask_stim_with_noise(stim, noise_freq, rng=rng)

    # Add experimental data
    stim["experimental_data"] = {
        "baseline_effect": df[
            (df.grating == grating_freq) & (df.noiseType == "baseline")
        ].reset_index(drop=True),
        "noise_effect": df[
            (df.grating == grating_freq) & (df.noiseType == str(noise_freq))
        ].reset_index(drop=True),
    }

    return stim


def grating04_NB173_model(ppd=PPD, rng=None):
    """White stimulus (0.4 cpd) masked with 1.73 cpd noise for model simulations from Betz (2015).

    Parameters
    ----------
    ppd : float
        Pixels per degree, used for setting the visual size.

    Returns
    -------
    dict of str
        Dictionary with the stimulus (key: "img") and additional keys containing stimulus parameters.

    Reference
    ----------
    Betz, T., Shapley, R., Wichmann, F. A., & Maertens, M. (2015).
        Noise masking of White's illusion exposes the weakness of current spatial
        filtering models of lightness perception. Journal of Vision, 15(14), 1,
        https://doi.org/10.1167/15.14.1.
    """
    # White's stimulus
    grating_freq = 0.4
    stim = white04(ppd=ppd, config="model")

    # Noise mask
    noise_freq = 1.73
    stim = _mask_stim_with_noise(stim, noise_freq, rng=rng)

    # Add experimental data
    stim["experimental_data"] = {
        "baseline_effect": df[
            (df.grating == grating_freq) & (df.noiseType == "baseline")
        ].reset_index(drop=True),
        "noise_effect": df[
            (df.grating == grating_freq) & (df.noiseType == str(noise_freq))
        ].reset_index(drop=True),
    }

    return stim


def grating04_NB300_model(ppd=PPD, rng=None):
    """White stimulus (0.4 cpd) masked with 3.00 cpd noise for model simulations from Betz (2015).

    Parameters
    ----------
    ppd : float
        Pixels per degree, used for setting the visual size.

    Returns
    -------
    dict of str
        Dictionary with the stimulus (key: "img") and additional keys containing stimulus parameters.

    Reference
    ----------
    Betz, T., Shapley, R., Wichmann, F. A., & Maertens, M. (2015).
        Noise masking of White's illusion exposes the weakness of current spatial
        filtering models of lightness perception. Journal of Vision, 15(14), 1,
        https://doi.org/10.1167/15.14.1.
    """
    # White's stimulus
    grating_freq = 0.4
    stim = white04(ppd=ppd, config="model")

    # Noise mask
    noise_freq = 3.00
    stim = _mask_stim_with_noise(stim, noise_freq, rng=rng)

    # Add experimental data
    stim["experimental_data"] = {
        "baseline_effect": df[
            (df.grating == grating_freq) & (df.noiseType == "baseline")
        ].reset_index(drop=True),
        "noise_effect": df[
            (df.grating == grating_freq) & (df.noiseType == str(noise_freq))
        ].reset_index(drop=True),
    }

    return stim


def grating04_NB520_model(ppd=PPD, rng=None):
    """White stimulus (0.4 cpd) masked with 5.20 cpd noise for model simulations from Betz (2015).

    Parameters
    ----------
    ppd : float
        Pixels per degree, used for setting the visual size.

    Returns
    -------
    dict of str
        Dictionary with the stimulus (key: "img") and additional keys containing stimulus parameters.

    Reference
    ----------
    Betz, T., Shapley, R., Wichmann, F. A., & Maertens, M. (2015).
        Noise masking of White's illusion exposes the weakness of current spatial
        filtering models of lightness perception. Journal of Vision, 15(14), 1,
        https://doi.org/10.1167/15.14.1.
    """
    # White's stimulus
    grating_freq = 0.4
    stim = white04(ppd=ppd, config="model")

    # Noise mask
    noise_freq = 5.20
    stim = _mask_stim_with_noise(stim, noise_freq, rng=rng)

    # Add experimental data
    stim["experimental_data"] = {
        "baseline_effect": df[
            (df.grating == grating_freq) & (df.noiseType == "baseline")
        ].reset_index(drop=True),
        "noise_effect": df[
            (df.grating == grating_freq) & (df.noiseType == str(noise_freq))
        ].reset_index(drop=True),
    }

    return stim


def grating04_NB900_model(ppd=PPD, rng=None):
    """White stimulus (0.4 cpd) masked with 9.00 cpd noise for model simulations from Betz (2015).

    Parameters
    ----------
    ppd : float
        Pixels per degree, used for setting the visual size.

    Returns
    -------
    dict of str
        Dictionary with the stimulus (key: "img") and additional keys containing stimulus parameters.

    Reference
    ----------
    Betz, T., Shapley, R., Wichmann, F. A., & Maertens, M. (2015).
        Noise masking of White's illusion exposes the weakness of current spatial
        filtering models of lightness perception. Journal of Vision, 15(14), 1,
        https://doi.org/10.1167/15.14.1.
    """
    # White's stimulus
    grating_freq = 0.4
    stim = white04(ppd=ppd, config="model")

    # Noise mask
    noise_freq = 9.00
    stim = _mask_stim_with_noise(stim, noise_freq, rng=rng)

    # Add experimental data
    stim["experimental_data"] = {
        "baseline_effect": df[
            (df.grating == grating_freq) & (df.noiseType == "baseline")
        ].reset_index(drop=True),
        "noise_effect": df[
            (df.grating == grating_freq) & (df.noiseType == str(noise_freq))
        ].reset_index(drop=True),
    }

    return stim


# %% Low spatial frequency grating: Modeling
def grating02_NB058_model(ppd=PPD, rng=None):
    """White stimulus (0.2 cpd) masked with 0.58 cpd noise for model simulations from Betz (2015).

    Parameters
    ----------
    ppd : float
        Pixels per degree, used for setting the visual size.

    Returns
    -------
    dict of str
        Dictionary with the stimulus (key: "img") and additional keys containing stimulus parameters.

    Reference
    ----------
    Betz, T., Shapley, R., Wichmann, F. A., & Maertens, M. (2015).
        Noise masking of White's illusion exposes the weakness of current spatial
        filtering models of lightness perception. Journal of Vision, 15(14), 1,
        https://doi.org/10.1167/15.14.1.
    """
    # White's stimulus
    grating_freq = 0.2
    stim = white02(ppd=ppd, config="model")

    # Noise mask
    noise_freq = 0.58
    stim = _mask_stim_with_noise(stim, noise_freq, rng=rng)

    # Add experimental data
    stim["experimental_data"] = {
        "baseline_effect": df[
            (df.grating == grating_freq) & (df.noiseType == "baseline")
        ].reset_index(drop=True),
        "noise_effect": df[
            (df.grating == grating_freq) & (df.noiseType == str(noise_freq))
        ].reset_index(drop=True),
    }

    return stim


def grating02_NB100_model(ppd=PPD, rng=None):
    """White stimulus (0.2 cpd) masked with 1.00 cpd noise for model simulations from Betz (2015).

    Parameters
    ----------
    ppd : float
        Pixels per degree, used for setting the visual size.

    Returns
    -------
    dict of str
        Dictionary with the stimulus (key: "img") and additional keys containing stimulus parameters.

    Reference
    ----------
    Betz, T., Shapley, R., Wichmann, F. A., & Maertens, M. (2015).
        Noise masking of White's illusion exposes the weakness of current spatial
        filtering models of lightness perception. Journal of Vision, 15(14), 1,
        https://doi.org/10.1167/15.14.1.
    """
    # White's stimulus
    grating_freq = 0.2
    stim = white02(ppd=ppd, config="model")

    # Noise mask
    noise_freq = 1.00
    stim = _mask_stim_with_noise(stim, noise_freq, rng=rng)

    # Add experimental data
    stim["experimental_data"] = {
        "baseline_effect": df[
            (df.grating == grating_freq) & (df.noiseType == "baseline")
        ].reset_index(drop=True),
        "noise_effect": df[
            (df.grating == grating_freq) & (df.noiseType == str(noise_freq))
        ].reset_index(drop=True),
    }

    return stim


def grating02_NB173_model(ppd=PPD, rng=None):
    """White stimulus (0.2 cpd) masked with 1.73 cpd noise for model simulations from Betz (2015).

    Parameters
    ----------
    ppd : float
        Pixels per degree, used for setting the visual size.

    Returns
    -------
    dict of str
        Dictionary with the stimulus (key: "img") and additional keys containing stimulus parameters.

    Reference
    ----------
    Betz, T., Shapley, R., Wichmann, F. A., & Maertens, M. (2015).
        Noise masking of White's illusion exposes the weakness of current spatial
        filtering models of lightness perception. Journal of Vision, 15(14), 1,
        https://doi.org/10.1167/15.14.1.
    """
    # White's stimulus
    grating_freq = 0.2
    stim = white02(ppd=ppd, config="model")

    # Noise mask
    noise_freq = 1.73
    stim = _mask_stim_with_noise(stim, noise_freq, rng=rng)

    # Add experimental data
    stim["experimental_data"] = {
        "baseline_effect": df[
            (df.grating == grating_freq) & (df.noiseType == "baseline")
        ].reset_index(drop=True),
        "noise_effect": df[
            (df.grating == grating_freq) & (df.noiseType == str(noise_freq))
        ].reset_index(drop=True),
    }

    return stim


def grating02_NB300_model(ppd=PPD, rng=None):
    """White stimulus (0.2 cpd) masked with 3.00 cpd noise for model simulations from Betz (2015).

    Parameters
    ----------
    ppd : float
        Pixels per degree, used for setting the visual size.

    Returns
    -------
    dict of str
        Dictionary with the stimulus (key: "img") and additional keys containing stimulus parameters.

    Reference
    ----------
    Betz, T., Shapley, R., Wichmann, F. A., & Maertens, M. (2015).
        Noise masking of White's illusion exposes the weakness of current spatial
        filtering models of lightness perception. Journal of Vision, 15(14), 1,
        https://doi.org/10.1167/15.14.1.
    """
    # White's stimulus
    grating_freq = 0.2
    stim = white02(ppd=ppd, config="model")

    # Noise mask
    noise_freq = 3.00
    stim = _mask_stim_with_noise(stim, noise_freq, rng=rng)

    # Add experimental data
    stim["experimental_data"] = {
        "baseline_effect": df[
            (df.grating == grating_freq) & (df.noiseType == "baseline")
        ].reset_index(drop=True),
        "noise_effect": df[
            (df.grating == grating_freq) & (df.noiseType == str(noise_freq))
        ].reset_index(drop=True),
    }

    return stim


def grating02_NB520_model(ppd=PPD, rng=None):
    """White stimulus (0.2 cpd) masked with 5.20 cpd noise for model simulations from Betz (2015).

    Parameters
    ----------
    ppd : float
        Pixels per degree, used for setting the visual size.

    Returns
    -------
    dict of str
        Dictionary with the stimulus (key: "img") and additional keys containing stimulus parameters.

    Reference
    ----------
    Betz, T., Shapley, R., Wichmann, F. A., & Maertens, M. (2015).
        Noise masking of White's illusion exposes the weakness of current spatial
        filtering models of lightness perception. Journal of Vision, 15(14), 1,
        https://doi.org/10.1167/15.14.1.
    """
    # White's stimulus
    grating_freq = 0.2
    stim = white02(ppd=ppd, config="model")

    # Noise mask
    noise_freq = 5.20
    stim = _mask_stim_with_noise(stim, noise_freq, rng=rng)

    # Add experimental data
    stim["experimental_data"] = {
        "baseline_effect": df[
            (df.grating == grating_freq) & (df.noiseType == "baseline")
        ].reset_index(drop=True),
        "noise_effect": df[
            (df.grating == grating_freq) & (df.noiseType == str(noise_freq))
        ].reset_index(drop=True),
    }

    return stim


def grating02_NB900_model(ppd=PPD, rng=None):
    """White stimulus (0.2 cpd) masked with 9.00 cpd noise for model simulations from Betz (2015).

    Parameters
    ----------
    ppd : float
        Pixels per degree, used for setting the visual size.

    Returns
    -------
    dict of str
        Dictionary with the stimulus (key: "img") and additional keys containing stimulus parameters.

    Reference
    ----------
    Betz, T., Shapley, R., Wichmann, F. A., & Maertens, M. (2015).
        Noise masking of White's illusion exposes the weakness of current spatial
        filtering models of lightness perception. Journal of Vision, 15(14), 1,
        https://doi.org/10.1167/15.14.1.
    """
    # White's stimulus
    grating_freq = 0.2
    stim = white04(ppd=ppd, config="model")

    # Noise mask
    noise_freq = 9.00
    stim = _mask_stim_with_noise(stim, noise_freq, rng=rng)

    # Add experimental data
    stim["experimental_data"] = {
        "baseline_effect": df[
            (df.grating == grating_freq) & (df.noiseType == "baseline")
        ].reset_index(drop=True),
        "noise_effect": df[
            (df.grating == grating_freq) & (df.noiseType == str(noise_freq))
        ].reset_index(drop=True),
    }

    return stim


# %% Main script
if __name__ == "__main__":
    from stimupy.utils import plot_stimuli

    # Log to console at INFO level
    logger.setLevel(logging.INFO)
    logger.addHandler(logging.StreamHandler())

    stims = gen_all(skip=True)
    plot_stimuli(stims, mask=False, vmin=0, vmax=100)
