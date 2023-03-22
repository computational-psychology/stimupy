"""Stimuli from White & White (1985)
https://doi.org/10.1016/0042-6989(85)90049-5

This module reproduces most of the stimuli used by White & White (1985) as
they were described in that paper.

Each stimulus is provided by a separate function,
a full list can be found as stimupy.papers.white1985.__all__

The output of each of these functions is a stimulus dictionary.

For a visual representation of all the stimuli and their mask,
simply run this module as a script:

    $ python stimuli/papers/white1985.py

Attributes
----------
__all__ (list of str): list of all stimulus-functions
    that are exported by this module when executing
        >>> from stimupy.papers.white1985 import *

References
-----------
White, M. & White, T. (1985).
    Counterphase lightness induction.
    Vision Research, 25 (9), 1331-1335.
    https://doi.org/10.1016/0042-6989(85)90049-5
"""

import copy
import warnings

import numpy as np

from stimupy import gratings

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

PPD = 50
BAR_WIDTH = 1 / 3.5 / 2
v1, v2, v3 = 0.0, 0.5, 1.0
START_PHASE1 = -180
START_PHASE2 = 0

COMMON_PARAMS = {
    "intensity_bars": (v1, v3),
    "intensity_target": v2,
    "distance_metric": "vertical",
}


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


def resolve_bar_width(bar_width=BAR_WIDTH, ppd=PPD):
    bar_width_old = copy.deepcopy(bar_width)
    bar_width = np.round(bar_width * ppd) / ppd

    if bar_width_old != bar_width:
        warnings.warn(
            f"Rounding bar_width because of ppd; {bar_width_old} -> {bar_width}. "
            "This will also effect the stimulus size."
        )
    return bar_width


def wide_0phase(ppd=PPD):
    """A square-wave grating with four bars that are in phase as shown in
    White & White (1985), Fig. 2
    Stimulus size: 3.5 x 3.5 deg
    Target bars: 0.14 x 0.75 deg (originally 0.15 x 0.75 deg)
    Grating frequency: ~3.5 cpd

    Parameters
    ----------
    ppd : int
        Resolution of stimulus in pixels per degree.

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "target_mask")
        and additional keys containing stimulus parameters

    References
    ----------
    White, M. & White, T. (1985).
        Counterphase lightness induction.
        Vision Research, 25 (9), 1331-1335.
        https://doi.org/10.1016/0042-6989(85)90049-5
    """

    bar_width = resolve_bar_width(BAR_WIDTH, ppd)

    params = {
        "visual_size": 25 * bar_width,
        "ppd": ppd,
        "bar_width": bar_width,
        "target_size": (bar_width * 9, 0.75),
        "target_phase_shift": START_PHASE1 + 0,
        **COMMON_PARAMS,
    }

    stim = gratings.phase_shifted(**params)
    stim["target_mask"] = np.where(stim["target_mask"] != 0, 1, 0)
    return stim


def wide_36phase(ppd=PPD):
    """A square-wave grating with four bars that are 36 deg out-of-phase as
    shown in White & White (1985), Fig. 2
    Stimulus size: 3.5 x 3.5 deg
    Target bars: 0.14 x 0.75 deg (originally 0.15 x 0.75 deg)
    Grating frequency: 3.5 cpd

    Parameters
    ----------
    ppd : int
        Resolution of stimulus in pixels per degree.

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "target_mask")
        and additional keys containing stimulus parameters

    References
    ----------
    White, M. & White, T. (1985).
        Counterphase lightness induction.
        Vision Research, 25 (9), 1331-1335.
        https://doi.org/10.1016/0042-6989(85)90049-5
    """
    bar_width = resolve_bar_width(BAR_WIDTH, ppd)

    params = {
        "visual_size": 25 * bar_width,
        "ppd": ppd,
        "bar_width": bar_width,
        "target_size": (bar_width * 9, 0.75),
        "target_phase_shift": START_PHASE1 + 36,
        **COMMON_PARAMS,
    }

    stim = gratings.phase_shifted(**params)
    stim["target_mask"] = np.where(stim["target_mask"] != 0, 1, 0)
    return stim


def wide_72phase(ppd=PPD):
    """A square-wave grating with four bars that are 72 deg out-of-phase as
    shown in White & White (1985), Fig. 2
    Stimulus size: 3.5 x 3.5 deg
    Target bars: 0.14 x 0.75 deg (originally 0.15 x 0.75 deg)
    Grating frequency: 3.5 cpd

    Parameters
    ----------
    ppd : int
        Resolution of stimulus in pixels per degree.

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "target_mask")
        and additional keys containing stimulus parameters

    References
    ----------
    White, M. & White, T. (1985).
        Counterphase lightness induction.
        Vision Research, 25 (9), 1331-1335.
        https://doi.org/10.1016/0042-6989(85)90049-5
    """

    bar_width = resolve_bar_width(BAR_WIDTH, ppd)

    params = {
        "visual_size": 25 * bar_width,
        "ppd": ppd,
        "bar_width": bar_width,
        "target_size": (bar_width * 9, 0.75),
        "target_phase_shift": START_PHASE1 + 72,
        **COMMON_PARAMS,
    }

    stim = gratings.phase_shifted(**params)
    stim["target_mask"] = np.where(stim["target_mask"] != 0, 1, 0)
    return stim


def wide_108phase(ppd=PPD):
    """A square-wave grating with four bars that are 108 deg out-of-phase as
    shown in White & White (1985), Fig. 2
    Stimulus size: 3.5 x 3.5 deg
    Target bars: 0.14 x 0.75 deg (originally 0.15 x 0.75 deg)
    Grating frequency: 3.5 cpd

    Parameters
    ----------
    ppd : int
        Resolution of stimulus in pixels per degree.

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "target_mask")
        and additional keys containing stimulus parameters

    References
    ----------
    White, M. & White, T. (1985).
        Counterphase lightness induction.
        Vision Research, 25 (9), 1331-1335.
        https://doi.org/10.1016/0042-6989(85)90049-5
    """

    bar_width = resolve_bar_width(BAR_WIDTH, ppd)

    params = {
        "visual_size": 25 * bar_width,
        "ppd": ppd,
        "bar_width": bar_width,
        "target_size": (bar_width * 9, 0.75),
        "target_phase_shift": START_PHASE1 + 108,
        **COMMON_PARAMS,
    }

    stim = gratings.phase_shifted(**params)
    stim["target_mask"] = np.where(stim["target_mask"] != 0, 1, 0)
    return stim


def wide_144phase(ppd=PPD):
    """A square-wave grating with four bars that are 144 deg out-of-phase as
    shown in White & White (1985), Fig. 2
    Stimulus size: 3.5 x 3.5 deg
    Target bars: 0.14 x 0.75 deg (originally 0.15 x 0.75 deg)
    Grating frequency: 3.5 cpd

    Parameters
    ----------
    ppd : int
        Resolution of stimulus in pixels per degree.

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "target_mask")
        and additional keys containing stimulus parameters

    References
    ----------
    White, M. & White, T. (1985).
        Counterphase lightness induction.
        Vision Research, 25 (9), 1331-1335.
        https://doi.org/10.1016/0042-6989(85)90049-5
    """

    bar_width = resolve_bar_width(BAR_WIDTH, ppd)

    params = {
        "visual_size": 25 * bar_width,
        "ppd": ppd,
        "bar_width": bar_width,
        "target_size": (bar_width * 9, 0.75),
        "target_phase_shift": START_PHASE1 + 144,
        **COMMON_PARAMS,
    }

    stim = gratings.phase_shifted(**params)
    stim["target_mask"] = np.where(stim["target_mask"] != 0, 1, 0)
    return stim


def wide_180phase(ppd=PPD):
    """A square-wave grating with four bars that are 180 deg out-of-phase as
    shown in White & White (1985), Fig. 2
    Stimulus size: 3.5 x 3.5 deg
    Target bars: 0.14 x 0.75 deg (originally 0.15 x 0.75 deg)
    Grating frequency: 3.5 cpd

    Parameters
    ----------
    ppd : int
        Resolution of stimulus in pixels per degree.

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "target_mask")
        and additional keys containing stimulus parameters

    References
    ----------
    White, M. & White, T. (1985).
        Counterphase lightness induction.
        Vision Research, 25 (9), 1331-1335.
        https://doi.org/10.1016/0042-6989(85)90049-5
    """

    bar_width = resolve_bar_width(BAR_WIDTH, ppd)

    params = {
        "visual_size": 25 * bar_width,
        "ppd": ppd,
        "bar_width": bar_width,
        "target_size": (bar_width * 9, 0.75),
        "target_phase_shift": START_PHASE1 + 180,
        **COMMON_PARAMS,
    }

    stim = gratings.phase_shifted(**params)
    stim["target_mask"] = np.where(stim["target_mask"] != 0, 1, 0)
    return stim


def square_0phase(ppd=PPD):
    """A square-wave grating with four squares that are in phase as shown in
    White & White (1985), Fig. 3
    Stimulus size: 3.5 x 3.5 deg
    Target bars: 0.14 x 0.14 deg (originally 0.15 x 0.15 deg)
    Grating frequency: 3.5 cpd

    Parameters
    ----------
    ppd : int
        Resolution of stimulus in pixels per degree.

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "target_mask")
        and additional keys containing stimulus parameters

    References
    ----------
    White, M. & White, T. (1985).
        Counterphase lightness induction.
        Vision Research, 25 (9), 1331-1335.
        https://doi.org/10.1016/0042-6989(85)90049-5
    """

    bar_width = resolve_bar_width(BAR_WIDTH, ppd)

    params = {
        "visual_size": 25 * bar_width,
        "ppd": ppd,
        "bar_width": bar_width,
        "target_size": (bar_width * 9, bar_width),
        "target_phase_shift": START_PHASE2 + 0,
        **COMMON_PARAMS,
    }

    stim = gratings.phase_shifted(**params)
    stim["target_mask"] = np.where(stim["target_mask"] != 0, 1, 0)
    return stim


def square_36phase(ppd=PPD):
    """A square-wave grating with four squares that are 36 deg out-of-phase as
    shown in White & White (1985), Fig. 3
    Stimulus size: 3.5 x 3.5 deg
    Target bars: 0.14 x 0.14 deg (originally 0.15 x 0.15 deg)
    Grating frequency: 3.5 cpd

    Parameters
    ----------
    ppd : int
        Resolution of stimulus in pixels per degree.

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "target_mask")
        and additional keys containing stimulus parameters

    References
    ----------
    White, M. & White, T. (1985).
        Counterphase lightness induction.
        Vision Research, 25 (9), 1331-1335.
        https://doi.org/10.1016/0042-6989(85)90049-5
    """

    bar_width = resolve_bar_width(BAR_WIDTH, ppd)

    params = {
        "visual_size": 25 * bar_width,
        "ppd": ppd,
        "bar_width": bar_width,
        "target_size": (bar_width * 9, bar_width),
        "target_phase_shift": START_PHASE2 + 36,
        **COMMON_PARAMS,
    }

    stim = gratings.phase_shifted(**params)
    stim["target_mask"] = np.where(stim["target_mask"] != 0, 1, 0)
    return stim


def square_72phase(ppd=PPD):
    """A square-wave grating with four squares that are 72 deg out-of-phase as
    shown in White & White (1985), Fig. 3
    Stimulus size: 3.5 x 3.5 deg
    Target bars: 0.14 x 0.14 deg (originally 0.15 x 0.15 deg)
    Grating frequency: 3.5 cpd

    Parameters
    ----------
    ppd : int
        Resolution of stimulus in pixels per degree.

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "target_mask")
        and additional keys containing stimulus parameters

    References
    ----------
    White, M. & White, T. (1985).
        Counterphase lightness induction.
        Vision Research, 25 (9), 1331-1335.
        https://doi.org/10.1016/0042-6989(85)90049-5
    """

    bar_width = resolve_bar_width(BAR_WIDTH, ppd)

    params = {
        "visual_size": 25 * bar_width,
        "ppd": ppd,
        "bar_width": bar_width,
        "target_size": (bar_width * 9, bar_width),
        "target_phase_shift": START_PHASE2 + 72,
        **COMMON_PARAMS,
    }

    stim = gratings.phase_shifted(**params)
    stim["target_mask"] = np.where(stim["target_mask"] != 0, 1, 0)
    return stim


def square_108phase(ppd=PPD):
    """A square-wave grating with four squares that are 108 deg out-of-phase as
    shown in White & White (1985), Fig. 3
    Stimulus size: 3.5 x 3.5 deg
    Target bars: 0.14 x 0.14 deg (originally 0.15 x 0.15 deg)
    Grating frequency: 3.5 cpd

    Parameters
    ----------
    ppd : int
        Resolution of stimulus in pixels per degree.

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "target_mask")
        and additional keys containing stimulus parameters

    References
    ----------
    White, M. & White, T. (1985).
        Counterphase lightness induction.
        Vision Research, 25 (9), 1331-1335.
        https://doi.org/10.1016/0042-6989(85)90049-5
    """

    bar_width = resolve_bar_width(BAR_WIDTH, ppd)

    params = {
        "visual_size": 25 * bar_width,
        "ppd": ppd,
        "bar_width": bar_width,
        "target_size": (bar_width * 9, bar_width),
        "target_phase_shift": START_PHASE2 + 108,
        **COMMON_PARAMS,
    }

    stim = gratings.phase_shifted(**params)
    stim["target_mask"] = np.where(stim["target_mask"] != 0, 1, 0)
    return stim


def square_144phase(ppd=PPD):
    """A square-wave grating with four squares that are 144 deg out-of-phase as
    shown in White & White (1985), Fig. 3
    Stimulus size: 3.5 x 3.5 deg
    Target bars: 0.14 x 0.14 deg (originally 0.15 x 0.15 deg)
    Grating frequency: 3.5 cpd

    Parameters
    ----------
    ppd : int
        Resolution of stimulus in pixels per degree.

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "target_mask")
        and additional keys containing stimulus parameters

    References
    ----------
    White, M. & White, T. (1985).
        Counterphase lightness induction.
        Vision Research, 25 (9), 1331-1335.
        https://doi.org/10.1016/0042-6989(85)90049-5
    """

    bar_width = resolve_bar_width(BAR_WIDTH, ppd)

    params = {
        "visual_size": 25 * bar_width,
        "ppd": ppd,
        "bar_width": bar_width,
        "target_size": (bar_width * 9, bar_width),
        "target_phase_shift": START_PHASE2 + 144,
        **COMMON_PARAMS,
    }

    stim = gratings.phase_shifted(**params)
    stim["target_mask"] = np.where(stim["target_mask"] != 0, 1, 0)
    return stim


def square_180phase(ppd=PPD):
    """A square-wave grating with four squares that are 180 deg out-of-phase as
    shown in White & White (1985), Fig. 3
    Stimulus size: 3.5 x 3.5 deg
    Target bars: 0.14 x 0.14 deg (originally 0.15 x 0.15 deg)
    Grating frequency: 3.5 cpd

    Parameters
    ----------
    ppd : int
        Resolution of stimulus in pixels per degree.

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "target_mask")
        and additional keys containing stimulus parameters

    References
    ----------
    White, M. & White, T. (1985).
        Counterphase lightness induction.
        Vision Research, 25 (9), 1331-1335.
        https://doi.org/10.1016/0042-6989(85)90049-5
    """

    bar_width = resolve_bar_width(BAR_WIDTH, ppd)

    params = {
        "visual_size": 25 * bar_width,
        "ppd": ppd,
        "bar_width": bar_width,
        "target_size": (bar_width * 9, bar_width),
        "target_phase_shift": START_PHASE2 + 180,
        **COMMON_PARAMS,
    }

    stim = gratings.phase_shifted(**params)
    stim["target_mask"] = np.where(stim["target_mask"] != 0, 1, 0)
    return stim


if __name__ == "__main__":
    from stimupy.utils import plot_stimuli

    stims = gen_all(skip=True)
    plot_stimuli(stims, mask=False)
