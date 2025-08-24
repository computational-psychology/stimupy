"""Stimuli from White (1981)

This module reproduces most of the stimuli used by White (1981)
as they were described in that paper.

Each stimulus is provided by a separate function,
which can be listed using

    >>> import stimupy.papers.white1981
    >>> help(stimupy.papers.white1981)

The output of each of these functions is a stimulus dictionary.

For a visual representation of all the stimuli and their mask,
simply run this module from the shell

    $ python -m stimuli.papers.white1981

or from within python

    >>> from stimupy.utils import plot_stimuli
    >>> from stimupy.papers import white1981
    >>> plot_stimuli(white1981.gen_all())

References
-----------
White, M. (1981).
    The effect of the nature of the surround on the perceived lightness
    of grey bars within square-wave test grating.
    Perception, 10, 215-230.
    https://doi.org/10.1068/p100215
"""

import copy
import logging
import warnings

import numpy as np

import stimupy

# Get module level logger
logger = logging.getLogger("stimupy.papers.white1981")

__all__ = [
    "square_white",
    "square_black",
    "grating_white_white",
    "grating_white_black",
    "grating_black_white",
    "grating_black_black",
    "grating_white_in",
    "grating_black_in",
    "grating_white_out",
    "grating_black_out",
    "grating_white_orthogonal",
    "grating_black_orthogonal",
]

VISUAL_SIZE = 4.0  # originally 4.3592 deg
TARGET_SIZE = 0.72  # originally 0.7696 deg
BAR_WIDTH = 0.08  # originally 0.0855 deg

PPD = 50
ROTATION = 90
v1, v2, v3 = 0.0, 0.5, 1.0


def gen_all(ppd=PPD, skip=False):
    stims = {}  # save the stimulus-dicts in a larger dict, with name as key
    for stim_name in __all__:
        logger.info(f"Generating white1981.{stim_name}")

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


def resolve_bar_width(bar_width=BAR_WIDTH, ppd=PPD):
    bar_width_old = copy.deepcopy(bar_width)
    bar_width = np.round(bar_width * ppd) / ppd

    if bar_width_old != bar_width:
        warnings.warn(
            f"Rounding bar_width because of ppd; {bar_width_old} -> {bar_width}. "
            "This will also effect the stimulus size."
        )
    return bar_width


def square_white(ppd=PPD):
    """A square on a white background from White (1981), Fig. 2
    Stimulus size: 4.0 x 4.0 deg (originally 4.3592 deg)
    Target size: 0.72 x 0.72 deg (originally 0.7696 deg)

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
    White, M. (1981).
        The effect of the nature of the surround on the perceived lightness
        of grey bars within square-wave test grating.
        Perception, 10, 215-230.
        https://doi.org/10.1068/p100215
    """

    params = {
        "visual_size": VISUAL_SIZE,
        "ppd": ppd,
        "target_size": TARGET_SIZE,
        "intensity_background": v3,
        "intensity_target": v2,
    }

    stim = stimupy.sbcs.basic(**params)
    return stim


def square_black(ppd=PPD):
    """A square on a black background from White (1981), Fig. 2
    Stimulus size: 4.0 x 4.0 deg (originally 4.3592 deg)
    Target size: 0.72 x 0.72 deg (originally 0.7696 deg)

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
    White, M. (1981).
        The effect of the nature of the surround on the perceived lightness
        of grey bars within square-wave test grating.
        Perception, 10, 215-230.
        https://doi.org/10.1068/p100215
    """

    params = {
        "visual_size": VISUAL_SIZE,
        "ppd": ppd,
        "target_size": TARGET_SIZE,
        "intensity_background": v1,
        "intensity_target": v2,
    }

    stim = stimupy.sbcs.basic(**params)
    return stim


def grating_white_white(ppd=PPD):
    """A white-gray grating on white background from White (1981), Fig. 2
    Stimulus size: 4.0 x 4.0 deg (originally 4.3592 deg)
    Target size: 0.72 x 0.72 deg (originally 0.7696 deg)
    Bar width: 0.08 deg (originally 0.0855 deg)

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
    White, M. (1981).
        The effect of the nature of the surround on the perceived lightness
        of grey bars within square-wave test grating.
        Perception, 10, 215-230.
        https://doi.org/10.1068/p100215
    """
    bar_width = resolve_bar_width(BAR_WIDTH, ppd)

    params = {
        "visual_size": VISUAL_SIZE,
        "ppd": ppd,
        "n_bars": 9,
        "bar_width": bar_width,
        "rotation": ROTATION,
        "intensity_background": v3,
        "intensity_bars": (v2, v3),
        "intensity_target": v2,
        "target_indices": (2, 4, 6, 8),
    }
    stim = stimupy.gratings.on_uniform(**params)
    stim["target_mask"] = np.where(stim["target_mask"] != 0, 1, 0)
    return stim


def grating_white_black(ppd=PPD):
    """A white-gray grating on black background from White (1981), Fig. 2
    Stimulus size: 4.0 x 4.0 deg (originally 4.3592 deg)
    Target size: 0.72 x 0.72 deg (originally 0.7696 deg)
    Bar width: 0.08 deg (originally 0.0855 deg)

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
    White, M. (1981).
        The effect of the nature of the surround on the perceived lightness
        of grey bars within square-wave test grating.
        Perception, 10, 215-230.
        https://doi.org/10.1068/p100215
    """
    bar_width = resolve_bar_width(BAR_WIDTH, ppd)

    params = {
        "visual_size": VISUAL_SIZE,
        "ppd": ppd,
        "grating_size": bar_width * 9,
        "bar_width": bar_width,
        "rotation": ROTATION,
        "intensity_background": v1,
        "intensity_bars": (v2, v3),
        "intensity_target": v2,
        "target_indices": (2, 4, 6, 8),
    }
    stim = stimupy.gratings.on_uniform(**params)
    stim["target_mask"] = np.where(stim["target_mask"] != 0, 1, 0)
    return stim


def grating_black_white(ppd=PPD):
    """A black-gray grating on white background from White (1981), Fig. 2
    Stimulus size: 4.0 x 4.0 deg (originally 4.3592 deg)
    Target size: 0.72 x 0.72 deg (originally 0.7696 deg)
    Bar width: 0.08 deg (originally 0.0855 deg)

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
    White, M. (1981).
        The effect of the nature of the surround on the perceived lightness
        of grey bars within square-wave test grating.
        Perception, 10, 215-230.
        https://doi.org/10.1068/p100215
    """
    bar_width = resolve_bar_width(BAR_WIDTH, ppd)

    params = {
        "visual_size": VISUAL_SIZE,
        "ppd": ppd,
        "grating_size": bar_width * 9,
        "bar_width": bar_width,
        "rotation": ROTATION,
        "intensity_background": v3,
        "intensity_bars": (v2, v1),
        "intensity_target": v2,
        "target_indices": (2, 4, 6, 8),
    }
    stim = stimupy.gratings.on_uniform(**params)
    stim["target_mask"] = np.where(stim["target_mask"] != 0, 1, 0)
    return stim


def grating_black_black(ppd=PPD):
    """A black-gray grating on black background from White (1981), Fig. 2
    Stimulus size: 4.0 x 4.0 deg (originally 4.3592 deg)
    Target size: 0.72 x 0.72 deg (originally 0.7696 deg)
    Bar width: 0.08 deg (originally 0.0855 deg)

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
    White, M. (1981).
        The effect of the nature of the surround on the perceived lightness
        of grey bars within square-wave test grating.
        Perception, 10, 215-230.
        https://doi.org/10.1068/p100215
    """
    bar_width = resolve_bar_width(BAR_WIDTH, ppd)

    params = {
        "visual_size": VISUAL_SIZE,
        "ppd": ppd,
        "grating_size": bar_width * 9,
        "bar_width": bar_width,
        "rotation": ROTATION,
        "intensity_background": v1,
        "intensity_bars": (v2, v1),
        "intensity_target": v2,
        "target_indices": (2, 4, 6, 8),
    }
    stim = stimupy.gratings.on_uniform(**params)
    stim["target_mask"] = np.where(stim["target_mask"] != 0, 1, 0)
    return stim


def grating_white_in(ppd=PPD):
    """A white-gray grating on an in-phase grating from White (1981), Fig. 3
    Stimulus size: 4.08 x 4.08 deg (originally 4.3592 deg)
    Target size: 0.72 x 0.72 deg (originally 0.7696 deg)
    Bar width: 0.08 deg (originally 0.0855 deg)

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
    White, M. (1981).
        The effect of the nature of the surround on the perceived lightness
        of grey bars within square-wave test grating.
        Perception, 10, 215-230.
        https://doi.org/10.1068/p100215
    """
    bar_width = resolve_bar_width(BAR_WIDTH, ppd)

    small_params = {
        "bar_width": bar_width,
        "n_bars": 9,
        "ppd": ppd,
        "rotation": ROTATION,
        "intensity_bars": (v1, v3),
        "intensity_target": v2,
        "target_indices": (2, 4, 6, 8),
    }
    large_params = {
        "bar_width": bar_width,
        "visual_size": 51 * bar_width,
        "ppd": ppd,
        "rotation": ROTATION,
        "intensity_bars": (v3, v1),
    }
    stim = stimupy.gratings.on_grating(
        small_grating_params=small_params,
        large_grating_params=large_params,
    )

    stim["target_mask"] = np.where(stim["target_mask"] != 0, 1, 0)
    return stim


def grating_black_in(ppd=PPD):
    """A black-gray grating on an in-phase grating from White (1981), Fig. 3
    Stimulus size: 4.08 x 4.08 deg (originally 4.3592 deg)
    Target size: 0.72 x 0.72 deg (originally 0.7696 deg)
    Bar width: 0.08 deg (originally 0.0855 deg)

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
    White, M. (1981).
        The effect of the nature of the surround on the perceived lightness
        of grey bars within square-wave test grating.
        Perception, 10, 215-230.
        https://doi.org/10.1068/p100215
    """
    bar_width = resolve_bar_width(BAR_WIDTH, ppd)

    small_params = {
        "bar_width": bar_width,
        "n_bars": 9,
        "ppd": ppd,
        "rotation": ROTATION,
        "intensity_bars": (v3, v1),
        "intensity_target": v2,
        "target_indices": (2, 4, 6, 8),
    }
    large_params = {
        "bar_width": bar_width,
        "visual_size": 51 * bar_width,
        "ppd": ppd,
        "rotation": ROTATION,
        "intensity_bars": (v1, v3),
    }
    stim = stimupy.gratings.on_grating(
        small_grating_params=small_params,
        large_grating_params=large_params,
    )

    stim["target_mask"] = np.where(stim["target_mask"] != 0, 1, 0)
    return stim


def grating_white_out(ppd=PPD):
    """A white-gray grating on an out-of-phase grating from White (1981), Fig. 3
    Stimulus size: 4.0 x 4.0 deg (originally 4.3592 deg)
    Target size: 0.72 x 0.72 deg (originally 0.7696 deg)
    Bar width: 0.08 deg (originally 0.0855 deg)

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
    White, M. (1981).
        The effect of the nature of the surround on the perceived lightness
        of grey bars within square-wave test grating.
        Perception, 10, 215-230.
        https://doi.org/10.1068/p100215
    """
    bar_width = resolve_bar_width(BAR_WIDTH, ppd)

    small_params = {
        "bar_width": bar_width,
        "visual_size": (50 * bar_width, 9 * bar_width),
        "ppd": ppd,
        "rotation": -ROTATION,
        "intensity_bars": (v1, v3),
        "intensity_target": v2,
        "target_indices": (24, 26, 28, 30),
    }
    large_params = {
        "bar_width": bar_width,
        "visual_size": 50 * bar_width,
        "ppd": ppd,
        "rotation": -ROTATION,
        "intensity_bars": (v3, v1),
    }
    stim = stimupy.gratings.on_grating(
        small_grating_params=small_params,
        large_grating_params=large_params,
    )

    stim["target_mask"] = np.where(stim["target_mask"] != 0, 1, 0)
    return stim


def grating_black_out(ppd=PPD):
    """A black-gray grating on an out-of-phase grating from White (1981), Fig. 3
    Stimulus size: 4.0 x 4.0 deg (originally 4.3592 deg)
    Target size: 0.72 x 0.72 deg (originally 0.7696 deg)
    Bar width: 0.08 deg (originally 0.0855 deg)

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
    White, M. (1981).
        The effect of the nature of the surround on the perceived lightness
        of grey bars within square-wave test grating.
        Perception, 10, 215-230.
        https://doi.org/10.1068/p100215
    """
    bar_width = resolve_bar_width(BAR_WIDTH, ppd)

    small_params = {
        "bar_width": bar_width,
        "visual_size": (50 * bar_width, 9 * bar_width),
        "ppd": ppd,
        "rotation": -ROTATION,
        "intensity_bars": (v3, v1),
        "intensity_target": v2,
        "target_indices": (24, 26, 28, 30),
    }
    large_params = {
        "bar_width": bar_width,
        "visual_size": 50 * bar_width,
        "ppd": ppd,
        "rotation": -ROTATION,
        "intensity_bars": (v1, v3),
    }
    stim = stimupy.gratings.on_grating(
        small_grating_params=small_params,
        large_grating_params=large_params,
    )

    stim["target_mask"] = np.where(stim["target_mask"] != 0, 1, 0)
    return stim


def grating_white_orthogonal(ppd=PPD):
    """A white-gray grating on an orthogonal grating from White (1981), Fig. 3
    Stimulus size: 4.0 x 4.0 deg (originally 4.3592 deg)
    Target size: 0.72 x 1.36 deg (originally 0.6841 x 1.1117 deg)
    Bar width: 0.08 deg (originally 0.0855 deg)

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
    White, M. (1981).
        The effect of the nature of the surround on the perceived lightness
        of grey bars within square-wave test grating.
        Perception, 10, 215-230.
        https://doi.org/10.1068/p100215
    """
    bar_width = resolve_bar_width(BAR_WIDTH, ppd)

    small_params = {
        "visual_size": (17 * bar_width, 9 * bar_width),
        "bar_width": bar_width,
        "ppd": ppd,
        "rotation": ROTATION + 90,
        "intensity_bars": (v2, v3),
        "intensity_target": v2,
        "target_indices": (2, 4, 6, 8),
    }
    large_params = {
        "bar_width": bar_width,
        "visual_size": 51 * bar_width,
        "ppd": ppd,
        "rotation": ROTATION,
        "intensity_bars": (v3, v1),
    }
    stim = stimupy.gratings.on_grating_masked(
        small_grating_params=small_params,
        large_grating_params=large_params,
        mask_size=(9 * bar_width, 9 * bar_width, 8 * bar_width),
        mask_rotation=ROTATION,
    )

    stim["target_mask"] = np.where(stim["target_mask"] != 0, 1, 0)
    return stim


def grating_black_orthogonal(ppd=PPD):
    """A black-gray grating on an orthogonal grating from White (1981), Fig. 3
    Stimulus size: 4.0 x 4.0 deg (originally 4.3592 deg)
    Target size: 0.72 x 1.36 deg (originally 0.6841 x 1.1117 deg)
    Bar width: 0.08 deg (originally 0.0855 deg)

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
    White, M. (1981).
        The effect of the nature of the surround on the perceived lightness
        of grey bars within square-wave test grating.
        Perception, 10, 215-230.
        https://doi.org/10.1068/p100215
    """
    bar_width = resolve_bar_width(BAR_WIDTH, ppd)

    small_params = {
        "visual_size": (17 * bar_width, 9 * bar_width),
        "bar_width": bar_width,
        "ppd": ppd,
        "rotation": ROTATION + 90,
        "intensity_bars": (v3, v1),
        "intensity_target": v2,
        "target_indices": (2, 4, 6, 8),
    }
    large_params = {
        "bar_width": bar_width,
        "visual_size": 51 * bar_width,
        "ppd": ppd,
        "rotation": ROTATION,
        "intensity_bars": (v1, v3),
    }
    stim = stimupy.gratings.on_grating_masked(
        small_grating_params=small_params,
        large_grating_params=large_params,
        mask_size=(9 * bar_width, 9 * bar_width, 8 * bar_width),
        mask_rotation=ROTATION,
    )

    stim["target_mask"] = np.where(stim["target_mask"] != 0, 1, 0)
    return stim


if __name__ == "__main__":
    from stimupy.utils import plot_stimuli

    # Log to console at INFO level
    logger.setLevel(logging.INFO)
    logger.addHandler(logging.StreamHandler())

    stims = gen_all(skip=True)
    plot_stimuli(stims, mask=False)
