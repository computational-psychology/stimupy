"""Stimuli from White (1981)
https://doi.org/10.1068/p100215

This module reproduces most of the stimuli used by White (1981) as they were
described in that paper.

Each stimulus is provided by a separate function,
a full list can be found as stimuli.papers.white1981.__all__

The output of each of these functions is a stimulus dictionary.

For a visual representation of all the stimuli and their mask,
simply run this module as a script:

    $ python stimuli/papers/white1981.py

Attributes
----------
__all__ (list of str): list of all stimulus-functions
    that are exported by this module when executing
        >>> from stimuli.papers.white1981 import *

References
-----------
White, M. (1981). The effect of the nature of the surround on the perceived
    lightness of grey bars within square-wave test grating. Perception, 10,
    215–230. https://doi.org/10.1068/p100215
"""

import numpy as np

from stimuli import illusions
from stimuli.illusions import grating_ as lynn_grating

# TODO: PPD can only be multiples of 12 (2*frequency) -> warning or error?

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

PPD = 36
VISUAL_SIZE = 4.3592
TARGET_SIZE = 0.7696
FREQUENCY = 6.
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


def square_white(ppd=PPD):
    """A square on a white background from White (1981), Fig. 2
    Stimulus size: 4.3592 x 4.3592 deg
    Target size: 0.7696 x 0.7696 deg

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
    White, M. (1981). The effect of the nature of the surround on the perceived
        lightness of grey bars within square-wave test grating. Perception, 10,
        215–230.
    """

    params = {
        "visual_size": VISUAL_SIZE,
        "ppd": ppd,
        "target_size": TARGET_SIZE,
        "intensity_background": v3,
        "intensity_target": v2,
    }

    stim = illusions.sbc.simultaneous_contrast(**params)
    return stim


def square_black(ppd=PPD):
    """A square on a black background from White (1981), Fig. 2
    Stimulus size: 4.3592 x 4.3592 deg
    Target size: 0.7696 x 0.7696 deg

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
    White, M. (1981). The effect of the nature of the surround on the perceived
        lightness of grey bars within square-wave test grating. Perception, 10,
        215–230.
    """

    params = {
        "visual_size": VISUAL_SIZE,
        "ppd": ppd,
        "target_size": TARGET_SIZE,
        "intensity_background": v1,
        "intensity_target": v2,
    }

    stim = illusions.sbc.simultaneous_contrast(**params)
    return stim


def grating_white_white(ppd=PPD):
    """A white-gray grating on white background from White (1981), Fig. 2
    Stimulus size: 4.3592 x 4.3592 deg
    Target size: 0.7696 x 0.7696 deg
    Grating frequency: about 6 cpd

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
    White, M. (1981). The effect of the nature of the surround on the perceived
        lightness of grey bars within square-wave test grating. Perception, 10,
        215–230.
    """

    params = {
        "visual_size": VISUAL_SIZE,
        "ppd": ppd,
        "target_size": TARGET_SIZE,
        "frequency": FREQUENCY,
        "intensity_background": v3,
        "intensity_bars": (v3, v2),
        "intensity_target": v2,
        "period": "half",
    }
    stim = lynn_grating.grating_uniform(**params)
    
    # Rotate
    stim["img"] = np.rot90(stim["img"])
    stim["mask"] = np.rot90(stim["mask"])
    return stim


def grating_white_black(ppd=PPD):
    """A white-gray grating on black background from White (1981), Fig. 2
    Stimulus size: 4.3592 x 4.3592 deg
    Target size: 0.7696 x 0.7696 deg
    Grating frequency: about 6 cpd

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
    White, M. (1981). The effect of the nature of the surround on the perceived
        lightness of grey bars within square-wave test grating. Perception, 10,
        215–230.
    """

    params = {
        "visual_size": VISUAL_SIZE,
        "ppd": ppd,
        "target_size": TARGET_SIZE,
        "frequency": FREQUENCY,
        "intensity_background": v1,
        "intensity_bars": (v3, v2),
        "intensity_target": v2,
        "period": "half",
    }
    stim = lynn_grating.grating_uniform(**params)
    
    # Rotate
    stim["img"] = np.rot90(stim["img"])
    stim["mask"] = np.rot90(stim["mask"])
    return stim


def grating_black_white(ppd=PPD):
    """A black-gray grating on white background from White (1981), Fig. 2
    Stimulus size: 4.3592 x 4.3592 deg
    Target size: 0.7696 x 0.7696 deg
    Grating frequency: about 6 cpd

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
    White, M. (1981). The effect of the nature of the surround on the perceived
        lightness of grey bars within square-wave test grating. Perception, 10,
        215–230.
    """

    params = {
        "visual_size": VISUAL_SIZE,
        "ppd": ppd,
        "target_size": TARGET_SIZE,
        "frequency": FREQUENCY,
        "intensity_background": v3,
        "intensity_bars": (v1, v2),
        "intensity_target": v2,
        "period": "half",
    }
    stim = lynn_grating.grating_uniform(**params)
    
    # Rotate
    stim["img"] = np.rot90(stim["img"])
    stim["mask"] = np.rot90(stim["mask"])
    return stim


def grating_black_black(ppd=PPD):
    """A black-gray grating on black background from White (1981), Fig. 2
    Stimulus size: 4.3592 x 4.3592 deg
    Target size: 0.7696 x 0.7696 deg
    Grating frequency: about 6 cpd

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
    White, M. (1981). The effect of the nature of the surround on the perceived
        lightness of grey bars within square-wave test grating. Perception, 10,
        215–230.
    """

    params = {
        "visual_size": VISUAL_SIZE,
        "ppd": ppd,
        "target_size": TARGET_SIZE,
        "frequency": FREQUENCY,
        "intensity_background": v1,
        "intensity_bars": (v1, v2),
        "intensity_target": v2,
        "period": "half",
    }
    stim = lynn_grating.grating_uniform(**params)
    
    # Rotate
    stim["img"] = np.rot90(stim["img"])
    stim["mask"] = np.rot90(stim["mask"])
    return stim


def grating_white_in(ppd=PPD):
    """A white-gray grating on an in-phase grating from White (1981), Fig. 3
    Stimulus size: 4.3592 x 4.3592 deg
    Target size: 0.7696 x 0.7696 deg
    Grating frequency: about 6 cpd

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
    White, M. (1981). The effect of the nature of the surround on the perceived
        lightness of grey bars within square-wave test grating. Perception, 10,
        215–230.
    """

    params = {
        "visual_size": VISUAL_SIZE,
        "ppd": ppd,
        "target_size": TARGET_SIZE - TARGET_SIZE/9.,
        "frequency": FREQUENCY,
        "intensity_bars": (v1, v3),
        "intensity_target": (None, v2),
        "period": "half",
    }
    stim = lynn_grating.grating_grating(**params)
    
    # Rotate
    stim["img"] = np.rot90(stim["img"])
    stim["mask"] = np.rot90(stim["mask"])
    return stim


def grating_black_in(ppd=PPD):
    """A black-gray grating on an in-phase grating from White (1981), Fig. 3
    Stimulus size: 4.3592 x 4.3592 deg
    Target size: 0.7696 x 0.7696 deg
    Grating frequency: about 6 cpd

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
    White, M. (1981). The effect of the nature of the surround on the perceived
        lightness of grey bars within square-wave test grating. Perception, 10,
        215–230.
    """

    params = {
        "visual_size": VISUAL_SIZE,
        "ppd": ppd,
        "target_size": TARGET_SIZE - TARGET_SIZE/9.,
        "frequency": FREQUENCY,
        "intensity_bars": (v3, v1),
        "intensity_target": (None, v2),
        "period": "half",
    }
    stim = lynn_grating.grating_grating(**params)
    
    # Rotate
    stim["img"] = np.rot90(stim["img"])
    stim["mask"] = np.rot90(stim["mask"])
    return stim


def grating_white_out(ppd=PPD):
    """A white-gray grating on an out-of-phase grating from White (1981), Fig. 3
    Stimulus size: 4.3592 x 4.3592 deg
    Target size: 0.7696 x 0.7696 deg
    Grating frequency: about 6 cpd

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
    White, M. (1981). The effect of the nature of the surround on the perceived
        lightness of grey bars within square-wave test grating. Perception, 10,
        215–230.
    """

    params = {
        "visual_size": VISUAL_SIZE,
        "ppd": ppd,
        "target_size": TARGET_SIZE - TARGET_SIZE/9.,
        "frequency": FREQUENCY,
        "intensity_bars": (v3, v1),
        "intensity_target": (None, v2),
        "period": "half",
    }
    stim = lynn_grating.grating_grating_shifted(**params)
    
    # Rotate
    stim["img"] = np.rot90(stim["img"])
    stim["mask"] = np.rot90(stim["mask"])
    return stim


def grating_black_out(ppd=PPD):
    """A black-gray grating on an out-of-phase grating from White (1981), Fig. 3
    Stimulus size: 4.3592 x 4.3592 deg
    Target size: 0.7696 x 0.7696 deg
    Grating frequency: about 6 cpd

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
    White, M. (1981). The effect of the nature of the surround on the perceived
        lightness of grey bars within square-wave test grating. Perception, 10,
        215–230.
    """

    params = {
        "visual_size": VISUAL_SIZE,
        "ppd": ppd,
        "target_size": TARGET_SIZE - TARGET_SIZE/9.,
        "frequency": FREQUENCY,
        "intensity_bars": (v1, v3),
        "intensity_target": (None, v2),
        "period": "half",
    }
    stim = lynn_grating.grating_grating_shifted(**params)
    
    # Rotate
    stim["img"] = np.rot90(stim["img"])
    stim["mask"] = np.rot90(stim["mask"])
    return stim


def grating_white_orthogonal(ppd=PPD):
    """A white-gray grating on an orthogonal grating from White (1981), Fig. 3
    Stimulus size: 4.3592 x 4.3592 deg
    Target size: 1.1117 x 0.6841 deg on a parallelogram
    Grating frequency: about 6 cpd

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
    White, M. (1981). The effect of the nature of the surround on the perceived
        lightness of grey bars within square-wave test grating. Perception, 10,
        215–230.
    """

    params = {
        "visual_size": VISUAL_SIZE,
        "ppd": ppd,
        "parallelogram_size": (0.6841, 1.1117, 1.1117/2),
        "frequency": FREQUENCY,
        "intensity_bars": (v3, v1),
        "intensity_innerbars": (v3, v2),
        "intensity_target": v2,
        "period": "full",
    }
    stim = lynn_grating.grating_grating_parallelogram(**params)
    
    # Rotate
    stim["img"] = np.rot90(stim["img"])
    stim["mask"] = np.rot90(stim["mask"])
    return stim


def grating_black_orthogonal(ppd=PPD):
    """A black-gray grating on an orthogonal grating from White (1981), Fig. 3
    Stimulus size: 4.3592 x 4.3592 deg
    Target size: 1.1117 x 0.6841 deg on a parallelogram
    Grating frequency: about 6 cpd

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
    White, M. (1981). The effect of the nature of the surround on the perceived
        lightness of grey bars within square-wave test grating. Perception, 10,
        215–230.
    """

    params = {
        "visual_size": VISUAL_SIZE,
        "ppd": ppd,
        "parallelogram_size": (0.6841, 1.1117, 1.1117/2),
        "frequency": FREQUENCY,
        "intensity_bars": (v3, v1),
        "intensity_innerbars": (v1, v2),
        "intensity_target": v2,
        "period": "full",
    }
    stim = lynn_grating.grating_grating_parallelogram(**params)
    
    # Rotate
    stim["img"] = np.rot90(stim["img"])
    stim["mask"] = np.rot90(stim["mask"])
    return stim


if __name__ == "__main__":
    from stimuli.utils import plot_stimuli

    stims = gen_all(skip=True)
    plot_stimuli(stims, mask=False)
