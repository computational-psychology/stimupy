"""Stimuli from White & White (1985)
https://doi.org/10.1016/0042-6989(85)90049-5

This module reproduces most of the stimuli used by White & White (1985) as
they were described in that paper.

Each stimulus is provided by a separate function,
a full list can be found as stimuli.papers.white1985.__all__

The output of each of these functions is a stimulus dictionary.

For a visual representation of all the stimuli and their mask,
simply run this module as a script:

    $ python stimuli/papers/white1985.py

Attributes
----------
__all__ (list of str): list of all stimulus-functions
    that are exported by this module when executing
        >>> from stimuli.papers.white1985 import *

References
-----------
White, M. & White, T. (1985). Counterphase lightness induction. Vision
    research, 25 (9), 1331-1335. https://doi.org/10.1016/0042-6989(85)90049-5
"""

# TODO: in the original paper, the 0-phase condition starts on different
# bars when comparing wide + square. To me, this is confusing. Keep or correct?

import numpy as np

from stimuli.illusions import grating_ as lynn_grating

__all__ = [
    "wide_0phase",
    "wide_36phase",
    "wide_72phase",
    "wide_108phase",
    "wide_144phase",
    "wide_180phase",
    "square_0phase",
    "square_36phase",
    "square_72phase",
    "square_108phase",
    "square_144phase",
    "square_180phase",
]

VISUAL_SIZE = 3.5
PPD = 36
WIDE_WIDTH = 0.75
SQUARE_WIDTH = 0.15
FREQUENCY = 3.5
TARGET_REPETITIONS = 4
v1, v2, v3 = 0.0, 0.5, 1.0


def gen_all(ppd=PPD, skip=False):
    stims = {}  # save the stimulus-dicts in a larger dict, with name as key
    for stim_name in __all__:
        print(f"Generating white1981.{stim_name}")

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
            print("-- not implemented")
            pass

    return stims


def wide_0phase(ppd=PPD):
    """A square-wave grating with four bars that are in phase as shown in
    White & White (1985), Fig. 2
    Stimulus size: 3.5 x 3.5 deg
    Target bars: 0.15 x 0.75 deg
    Grating frequency: 3.5 cpd

    Parameters
    ----------
    ppd : int
        Resolution of stimulus in pixels per degree.

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "mask")
        and additional keys containing stimulus parameters

    References
    -----------
    White, M. & White, T. (1985). Counterphase lightness induction. Vision research,
        25 (9), 1331-1335. https://doi.org/10.1016/0042-6989(85)90049-5
    """

    params = {
        "visual_size": VISUAL_SIZE,
        "ppd": ppd,
        "frequency": FREQUENCY,
        "target_height": WIDE_WIDTH,
        "target_repetitions": TARGET_REPETITIONS,
        "target_phase": 0.,
        "intensity_bars": (v1, v3),
        "intensity_target": v2,
        "period": "half",
    }

    stim = lynn_grating.counterphase_induction(**params)

    # Rotate
    stim["img"] = np.rot90(stim["img"])
    stim["mask"] = np.rot90(stim["mask"]).astype(int)
    stim["target_width"] = stim["target_height"]
    del stim["target_height"]
    return stim


def wide_36phase(ppd=PPD):
    """A square-wave grating with four bars that are 36 deg out-of-phase as
    shown in White & White (1985), Fig. 2
    Stimulus size: 3.5 x 3.5 deg
    Target bars: 0.15 x 0.75 deg
    Grating frequency: 3.5 cpd

    Parameters
    ----------
    ppd : int
        Resolution of stimulus in pixels per degree.

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "mask")
        and additional keys containing stimulus parameters

    References
    -----------
    White, M. & White, T. (1985). Counterphase lightness induction. Vision research,
        25 (9), 1331-1335. https://doi.org/10.1016/0042-6989(85)90049-5
    """

    params = {
        "visual_size": VISUAL_SIZE,
        "ppd": ppd,
        "frequency": FREQUENCY,
        "target_height": WIDE_WIDTH,
        "target_repetitions": TARGET_REPETITIONS,
        "target_phase": -36.,
        "intensity_bars": (v1, v3),
        "intensity_target": v2,
        "period": "half",
    }

    stim = lynn_grating.counterphase_induction(**params)

    # Rotate
    stim["img"] = np.rot90(stim["img"])
    stim["mask"] = np.rot90(stim["mask"]).astype(int)
    stim["target_width"] = stim["target_height"]
    del stim["target_height"]
    return stim


def wide_72phase(ppd=PPD):
    """A square-wave grating with four bars that are 72 deg out-of-phase as
    shown in White & White (1985), Fig. 2
    Stimulus size: 3.5 x 3.5 deg
    Target bars: 0.15 x 0.75 deg
    Grating frequency: 3.5 cpd

    Parameters
    ----------
    ppd : int
        Resolution of stimulus in pixels per degree.

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "mask")
        and additional keys containing stimulus parameters

    References
    -----------
    White, M. & White, T. (1985). Counterphase lightness induction. Vision research,
        25 (9), 1331-1335. https://doi.org/10.1016/0042-6989(85)90049-5
    """

    params = {
        "visual_size": VISUAL_SIZE,
        "ppd": ppd,
        "frequency": FREQUENCY,
        "target_height": WIDE_WIDTH,
        "target_repetitions": TARGET_REPETITIONS,
        "target_phase": -72.,
        "intensity_bars": (v1, v3),
        "intensity_target": v2,
        "period": "half",
    }

    stim = lynn_grating.counterphase_induction(**params)

    # Rotate
    stim["img"] = np.rot90(stim["img"])
    stim["mask"] = np.rot90(stim["mask"]).astype(int)
    stim["target_width"] = stim["target_height"]
    del stim["target_height"]
    return stim


def wide_108phase(ppd=PPD):
    """A square-wave grating with four bars that are 108 deg out-of-phase as
    shown in White & White (1985), Fig. 2
    Stimulus size: 3.5 x 3.5 deg
    Target bars: 0.15 x 0.75 deg
    Grating frequency: 3.5 cpd

    Parameters
    ----------
    ppd : int
        Resolution of stimulus in pixels per degree.

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "mask")
        and additional keys containing stimulus parameters

    References
    -----------
    White, M. & White, T. (1985). Counterphase lightness induction. Vision research,
        25 (9), 1331-1335. https://doi.org/10.1016/0042-6989(85)90049-5
    """

    params = {
        "visual_size": VISUAL_SIZE,
        "ppd": ppd,
        "frequency": FREQUENCY,
        "target_height": WIDE_WIDTH,
        "target_repetitions": TARGET_REPETITIONS,
        "target_phase": -108.,
        "intensity_bars": (v1, v3),
        "intensity_target": v2,
        "period": "half",
    }

    stim = lynn_grating.counterphase_induction(**params)

    # Rotate
    stim["img"] = np.rot90(stim["img"])
    stim["mask"] = np.rot90(stim["mask"]).astype(int)
    stim["target_width"] = stim["target_height"]
    del stim["target_height"]
    return stim


def wide_144phase(ppd=PPD):
    """A square-wave grating with four bars that are 144 deg out-of-phase as
    shown in White & White (1985), Fig. 2
    Stimulus size: 3.5 x 3.5 deg
    Target bars: 0.15 x 0.75 deg
    Grating frequency: 3.5 cpd

    Parameters
    ----------
    ppd : int
        Resolution of stimulus in pixels per degree.

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "mask")
        and additional keys containing stimulus parameters

    References
    -----------
    White, M. & White, T. (1985). Counterphase lightness induction. Vision research,
        25 (9), 1331-1335. https://doi.org/10.1016/0042-6989(85)90049-5
    """

    params = {
        "visual_size": VISUAL_SIZE,
        "ppd": ppd,
        "frequency": FREQUENCY,
        "target_height": WIDE_WIDTH,
        "target_repetitions": TARGET_REPETITIONS,
        "target_phase": -144.,
        "intensity_bars": (v1, v3),
        "intensity_target": v2,
        "period": "half",
    }

    stim = lynn_grating.counterphase_induction(**params)

    # Rotate
    stim["img"] = np.rot90(stim["img"])
    stim["mask"] = np.rot90(stim["mask"]).astype(int)
    stim["target_width"] = stim["target_height"]
    del stim["target_height"]
    return stim


def wide_180phase(ppd=PPD):
    """A square-wave grating with four bars that are 180 deg out-of-phase as
    shown in White & White (1985), Fig. 2
    Stimulus size: 3.5 x 3.5 deg
    Target bars: 0.15 x 0.75 deg
    Grating frequency: 3.5 cpd

    Parameters
    ----------
    ppd : int
        Resolution of stimulus in pixels per degree.

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "mask")
        and additional keys containing stimulus parameters

    References
    -----------
    White, M. & White, T. (1985). Counterphase lightness induction. Vision research,
        25 (9), 1331-1335. https://doi.org/10.1016/0042-6989(85)90049-5
    """

    params = {
        "visual_size": VISUAL_SIZE,
        "ppd": ppd,
        "frequency": FREQUENCY,
        "target_height": WIDE_WIDTH,
        "target_repetitions": TARGET_REPETITIONS,
        "target_phase": -180.,
        "intensity_bars": (v1, v3),
        "intensity_target": v2,
        "period": "half",
    }

    stim = lynn_grating.counterphase_induction(**params)

    # Rotate
    stim["img"] = np.rot90(stim["img"])
    stim["mask"] = np.rot90(stim["mask"]).astype(int)
    stim["target_width"] = stim["target_height"]
    del stim["target_height"]
    return stim


def square_0phase(ppd=PPD):
    """A square-wave grating with four squares that are in phase as shown in
    White & White (1985), Fig. 3
    Stimulus size: 3.5 x 3.5 deg
    Target squares: 0.15 x 0.15 deg
    Grating frequency: 3.5 cpd

    Parameters
    ----------
    ppd : int
        Resolution of stimulus in pixels per degree.

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "mask")
        and additional keys containing stimulus parameters

    References
    -----------
    White, M. & White, T. (1985). Counterphase lightness induction. Vision research,
        25 (9), 1331-1335. https://doi.org/10.1016/0042-6989(85)90049-5
    """

    params = {
        "visual_size": VISUAL_SIZE,
        "ppd": ppd,
        "frequency": FREQUENCY,
        "target_height": SQUARE_WIDTH,
        "target_repetitions": TARGET_REPETITIONS,
        "target_phase": 0.,
        "intensity_bars": (v1, v3),
        "intensity_target": v2,
        "period": "half",
    }

    stim = lynn_grating.counterphase_induction(**params)

    # Rotate
    stim["img"] = np.rot90(stim["img"])
    stim["mask"] = np.rot90(stim["mask"]).astype(int)
    stim["target_width"] = stim["target_height"]
    del stim["target_height"]
    return stim


def square_36phase(ppd=PPD):
    """A square-wave grating with four squares that are 36 deg out-of-phase as
    shown in White & White (1985), Fig. 3
    Stimulus size: 3.5 x 3.5 deg
    Target squares: 0.15 x 0.15 deg
    Grating frequency: 3.5 cpd

    Parameters
    ----------
    ppd : int
        Resolution of stimulus in pixels per degree.

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "mask")
        and additional keys containing stimulus parameters

    References
    -----------
    White, M. & White, T. (1985). Counterphase lightness induction. Vision research,
        25 (9), 1331-1335. https://doi.org/10.1016/0042-6989(85)90049-5
    """

    params = {
        "visual_size": VISUAL_SIZE,
        "ppd": ppd,
        "frequency": FREQUENCY,
        "target_height": SQUARE_WIDTH,
        "target_repetitions": TARGET_REPETITIONS,
        "target_phase": -36.,
        "intensity_bars": (v1, v3),
        "intensity_target": v2,
        "period": "half",
    }

    stim = lynn_grating.counterphase_induction(**params)

    # Rotate
    stim["img"] = np.rot90(stim["img"])
    stim["mask"] = np.rot90(stim["mask"]).astype(int)
    stim["target_width"] = stim["target_height"]
    del stim["target_height"]
    return stim


def square_72phase(ppd=PPD):
    """A square-wave grating with four squares that are 72 deg out-of-phase as
    shown in White & White (1985), Fig. 3
    Stimulus size: 3.5 x 3.5 deg
    Target squares: 0.15 x 0.15 deg
    Grating frequency: 3.5 cpd

    Parameters
    ----------
    ppd : int
        Resolution of stimulus in pixels per degree.

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "mask")
        and additional keys containing stimulus parameters

    References
    -----------
    White, M. & White, T. (1985). Counterphase lightness induction. Vision research,
        25 (9), 1331-1335. https://doi.org/10.1016/0042-6989(85)90049-5
    """

    params = {
        "visual_size": VISUAL_SIZE,
        "ppd": ppd,
        "frequency": FREQUENCY,
        "target_height": SQUARE_WIDTH,
        "target_repetitions": TARGET_REPETITIONS,
        "target_phase": -72.,
        "intensity_bars": (v1, v3),
        "intensity_target": v2,
        "period": "half",
    }

    stim = lynn_grating.counterphase_induction(**params)

    # Rotate
    stim["img"] = np.rot90(stim["img"])
    stim["mask"] = np.rot90(stim["mask"]).astype(int)
    stim["target_width"] = stim["target_height"]
    del stim["target_height"]
    return stim


def square_108phase(ppd=PPD):
    """A square-wave grating with four squares that are 108 deg out-of-phase as
    shown in White & White (1985), Fig. 3
    Stimulus size: 3.5 x 3.5 deg
    Target squares: 0.15 x 0.15 deg
    Grating frequency: 3.5 cpd

    Parameters
    ----------
    ppd : int
        Resolution of stimulus in pixels per degree.

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "mask")
        and additional keys containing stimulus parameters

    References
    -----------
    White, M. & White, T. (1985). Counterphase lightness induction. Vision research,
        25 (9), 1331-1335. https://doi.org/10.1016/0042-6989(85)90049-5
    """

    params = {
        "visual_size": VISUAL_SIZE,
        "ppd": ppd,
        "frequency": FREQUENCY,
        "target_height": SQUARE_WIDTH,
        "target_repetitions": TARGET_REPETITIONS,
        "target_phase": -108.,
        "intensity_bars": (v1, v3),
        "intensity_target": v2,
        "period": "half",
    }

    stim = lynn_grating.counterphase_induction(**params)

    # Rotate
    stim["img"] = np.rot90(stim["img"])
    stim["mask"] = np.rot90(stim["mask"]).astype(int)
    stim["target_width"] = stim["target_height"]
    del stim["target_height"]
    return stim


def square_144phase(ppd=PPD):
    """A square-wave grating with four squares that are 144 deg out-of-phase as
    shown in White & White (1985), Fig. 3
    Stimulus size: 3.5 x 3.5 deg
    Target squares: 0.15 x 0.15 deg
    Grating frequency: 3.5 cpd

    Parameters
    ----------
    ppd : int
        Resolution of stimulus in pixels per degree.

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "mask")
        and additional keys containing stimulus parameters

    References
    -----------
    White, M. & White, T. (1985). Counterphase lightness induction. Vision research,
        25 (9), 1331-1335. https://doi.org/10.1016/0042-6989(85)90049-5
    """

    params = {
        "visual_size": VISUAL_SIZE,
        "ppd": ppd,
        "frequency": FREQUENCY,
        "target_height": SQUARE_WIDTH,
        "target_repetitions": TARGET_REPETITIONS,
        "target_phase": -144.,
        "intensity_bars": (v1, v3),
        "intensity_target": v2,
        "period": "half",
    }

    stim = lynn_grating.counterphase_induction(**params)

    # Rotate
    stim["img"] = np.rot90(stim["img"])
    stim["mask"] = np.rot90(stim["mask"]).astype(int)
    stim["target_width"] = stim["target_height"]
    del stim["target_height"]
    return stim


def square_180phase(ppd=PPD):
    """A square-wave grating with four squares that are 180 deg out-of-phase as
    shown in White & White (1985), Fig. 3
    Stimulus size: 3.5 x 3.5 deg
    Target squares: 0.15 x 0.15 deg
    Grating frequency: 3.5 cpd

    Parameters
    ----------
    ppd : int
        Resolution of stimulus in pixels per degree.

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "mask")
        and additional keys containing stimulus parameters

    References
    -----------
    White, M. & White, T. (1985). Counterphase lightness induction. Vision research,
        25 (9), 1331-1335. https://doi.org/10.1016/0042-6989(85)90049-5
    """

    params = {
        "visual_size": VISUAL_SIZE,
        "ppd": ppd,
        "frequency": FREQUENCY,
        "target_height": SQUARE_WIDTH,
        "target_repetitions": TARGET_REPETITIONS,
        "target_phase": -180.,
        "intensity_bars": (v1, v3),
        "intensity_target": v2,
        "period": "half",
    }

    stim = lynn_grating.counterphase_induction(**params)

    # Rotate
    stim["img"] = np.rot90(stim["img"])
    stim["mask"] = np.rot90(stim["mask"]).astype(int)
    stim["target_width"] = stim["target_height"]
    del stim["target_height"]
    return stim


if __name__ == "__main__":
    from stimuli.utils import plot_stimuli

    stims = gen_all(skip=True)
    plot_stimuli(stims, mask=False)
