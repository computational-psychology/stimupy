"""Stimuli from Murray (2020) https://doi.org/10/gh57gf

This module reproduces most of the stimuli used by Murray (2020)
as they were provided to the model described in that paper but
normalized between 0 and 1.
The stimuli are show in Fig 1 of the paper.
NOTE that the Haze illusion (Fig 1m) is not provided.

Each stimulus is provided by a separate function,
a full list can be found as stimupy.papers.murray2020.__all__

The output of each of these functions is a stimulus dictionary.

For a visual representation of all the stimuli and their mask,
simply run this module as a script:

    $ python stimuli/papers/murray2020.py

Attributes
----------
__all__ (list of str): list of all stimulus-functions
    that are exported by this module when executing
        >>> from stimupy.papers.murray2020 import *

References
-----------
Murray, R. F. (2020).
    A model of lightness perception
    guided by probabilistic assumptions about lighting and reflectance.
    Journal of Vision, 20(7), 28.
    https://doi.org/10/gh57gf
"""

import os.path

import numpy as np
import scipy.io

import stimupy
from stimupy.utils import pad_dict_by_visual_size, rotate_dict

__all__ = [
    "argyle",
    "argyle_control",
    "argyle_long",
    "snake",
    "snake_control",
    "koffka_adelson",
    "koffka_broken",
    "koffka_connected",
    "checkassim",
    "simcon",
    "simcon_articulated",
    "white",
]

data_dir = os.path.dirname(__file__)
mat_fname = os.path.join(data_dir, "murray2020.mat")
mat_content = scipy.io.loadmat(mat_fname)

PPD = 16 / 8.0
PAD = True


def gen_all(skip=False):
    stims = {}  # save the stimulus-dicts in a larger dict, with name as key
    for stim_name in __all__:
        print(f"Generating murray2020.{stim_name}")

        # Get a reference to the actual function
        func = globals()[stim_name]
        try:
            stim = func()

            # Accumulate
            stims[stim_name] = stim
        except NotImplementedError as e:
            if not skip:
                raise e
            # Skip stimuli that aren't implemented
            print("-- not implemented")
            pass

    return stims


def get_mask(target1, target2, shape):
    mask = np.zeros(shape)

    # Convert MATLAB 1-based index to numpy 0-based index
    target1 = target1 - 1
    target2 = target2 - 1

    # Fill target1 mask
    for x in range(target1[1], target1[3] + 1):
        for y in range(target1[0], target1[2] + 1):
            mask[y][x] = 1

    # Fill target2 mask
    for x in range(target2[1], target2[3] + 1):
        for y in range(target2[0], target2[2] + 1):
            mask[y, x] = 2

    mask = np.array(mask, dtype=int)

    return mask


def argyle(ppd=PPD):
    """Argyle illusion, Murray (2020) Fig 1a

    Parameters
    ----------
    ppd : int
        Resolution of stimulus in pixels per degree. (default: 32)

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "target_mask")
        and additional keys containing stimulus parameters

    References
    ----------
    Murray, R. F. (2020).
        A model of lightness perception
        guided by probabilistic assumptions about lighting and reflectance.
        Journal of Vision, 20(7), 28.
        https://doi.org/10/gh57gf
    """

    a = mat_content["argyle"]
    img = np.array(((a[0])[0])[0])
    target1 = np.array((((a[0])[0])[1])[0])
    target2 = np.array((((a[0])[0])[2])[0])
    mask = get_mask(target1, target2, img.shape)

    img = img.repeat(repeats=int(ppd / PPD), axis=0).repeat(repeats=int(ppd / PPD), axis=1)
    mask = mask.repeat(repeats=int(ppd / PPD), axis=0).repeat(repeats=int(ppd / PPD), axis=1)

    # Normalize intensity values to [0, 1]
    original_range = (img.min(), img.max())
    normed_img = (img - img.min()) / (img.max() - img.min())

    experimental_data = {
        "mean_proportion_expected": 0.4875,
        "CI95_proportion_expected": (-0.154903, 0.154903),
    }

    params = {
        "visual_size": np.array(normed_img.shape) / ppd,
        "shape": normed_img.shape,
        "ppd": ppd,
        "intensity_range": (0.0, 1.0),
        "original_range": original_range,
        "experimental_data": experimental_data,
    }
    return {"img": normed_img, "target_mask": mask, **params}


def argyle_control(ppd=PPD):
    """Argyle control figure, Murray (2020) Fig 1c

    Parameters
    ----------
    ppd : int
        Resolution of stimulus in pixels per degree. (default: 32)

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "target_mask")
        and additional keys containing stimulus parameters

    References
    ----------
    Murray, R. F. (2020).
        A model of lightness perception
        guided by probabilistic assumptions about lighting and reflectance.
        Journal of Vision, 20(7), 28.
        https://doi.org/10/gh57gf
    """

    a = mat_content["argyle_control"]
    img = np.array(((a[0])[0])[0])
    target1 = np.array((((a[0])[0])[1])[0])
    target2 = np.array((((a[0])[0])[2])[0])
    mask = get_mask(target1, target2, img.shape)

    img = img.repeat(repeats=int(ppd / PPD), axis=0).repeat(repeats=int(ppd / PPD), axis=1)
    mask = mask.repeat(repeats=int(ppd / PPD), axis=0).repeat(repeats=int(ppd / PPD), axis=1)

    # Normalize intensity values to [0, 1]
    original_range = (img.min(), img.max())
    normed_img = (img - img.min()) / (img.max() - img.min())

    experimental_data = {
        "mean_proportion_expected": 0.35,
        "CI95_proportion_expected": (-0.147814, 0.147814),
    }

    stim = {
        "img": normed_img,
        "target_mask": mask.astype(int),
        "visual_size": np.array(normed_img.shape) / ppd,
        "shape": normed_img.shape,
        "ppd": ppd,
        "intensity_range": (0.0, 1.0),
        "original_range": original_range,
        "experimental_data": experimental_data,
    }
    return stim


def argyle_long(ppd=PPD):
    """Long-range Argyle illusion, Murray (2020) Fig 1b

    Parameters
    ----------
    ppd : int
        Resolution of stimulus in pixels per degree. (default: 32)

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "target_mask")
        and additional keys containing stimulus parameters

    References
    ----------
    Murray, R. F. (2020).
        A model of lightness perception
        guided by probabilistic assumptions about lighting and reflectance.
        Journal of Vision, 20(7), 28.
        https://doi.org/10/gh57gf
    """

    a = mat_content["argyle_long"]
    img = np.array(((a[0])[0])[0])
    target1 = np.array((((a[0])[0])[1])[0])
    target2 = np.array((((a[0])[0])[2])[0])
    mask = get_mask(target1, target2, img.shape)

    img = img.repeat(repeats=int(ppd / PPD), axis=0).repeat(repeats=int(ppd / PPD), axis=1)
    mask = mask.repeat(repeats=int(ppd / PPD), axis=0).repeat(repeats=int(ppd / PPD), axis=1)

    # Normalize intensity values to [0, 1]
    original_range = (img.min(), img.max())
    normed_img = (img - img.min()) / (img.max() - img.min())

    experimental_data = {
        "mean_proportion_expected": 0.6,
        "CI95_proportion_expected": (-0.151821, 0.151821),
    }

    stim = {
        "img": normed_img,
        "target_mask": mask.astype(int),
        "visual_size": np.array(normed_img.shape) / ppd,
        "shape": normed_img.shape,
        "ppd": ppd,
        "intensity_range": (0.0, 1.0),
        "original_range": original_range,
        "experimental_data": experimental_data,
    }
    return stim


def snake(ppd=PPD):
    """Snake illusion, Murray (2020) Fig 1i

    Parameters
    ----------
    ppd : int
        Resolution of stimulus in pixels per degree. (default: 32)

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "target_mask")
        and additional keys containing stimulus parameters

    References
    ----------
    Murray, R. F. (2020).
        A model of lightness perception
        guided by probabilistic assumptions about lighting and reflectance.
        Journal of Vision, 20(7), 28.
        https://doi.org/10/gh57gf
    """

    a = mat_content["snake"]
    img = np.array(((a[0])[0])[0])
    target1 = np.array((((a[0])[0])[1])[0])
    target2 = np.array((((a[0])[0])[2])[0])
    mask = get_mask(target1, target2, img.shape)

    img = img.repeat(repeats=int(ppd / PPD), axis=0).repeat(repeats=int(ppd / PPD), axis=1)
    mask = mask.repeat(repeats=int(ppd / PPD), axis=0).repeat(repeats=int(ppd / PPD), axis=1)

    # Normalize intensity values to [0, 1]
    original_range = (img.min(), img.max())
    normed_img = (img - img.min()) / (img.max() - img.min())

    experimental_data = {
        "mean_proportion_expected": 0.9625,
        "CI95_proportion_expected": (-0.0588765, 0.0588765),
    }

    stim = {
        "img": normed_img,
        "target_mask": mask.astype(int),
        "visual_size": np.array(normed_img.shape) / ppd,
        "shape": normed_img.shape,
        "ppd": ppd,
        "intensity_range": (0.0, 1.0),
        "original_range": original_range,
        "experimental_data": experimental_data,
    }
    return stim


def snake_control(ppd=PPD):
    """Snake control figure, Murray (2020) Fig 1j

    Parameters
    ----------
    ppd : int
        Resolution of stimulus in pixels per degree. (default: 32)

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "target_mask")
        and additional keys containing stimulus parameters

    References
    ----------
    Murray, R. F. (2020).
        A model of lightness perception
        guided by probabilistic assumptions about lighting and reflectance.
        Journal of Vision, 20(7), 28.
        https://doi.org/10/gh57gf
    """

    a = mat_content["snake_control"]
    img = np.array(((a[0])[0])[0])
    target1 = np.array((((a[0])[0])[1])[0])
    target2 = np.array((((a[0])[0])[2])[0])
    mask = get_mask(target1, target2, img.shape)

    img = img.repeat(repeats=int(ppd / PPD), axis=0).repeat(repeats=int(ppd / PPD), axis=1)
    mask = mask.repeat(repeats=int(ppd / PPD), axis=0).repeat(repeats=int(ppd / PPD), axis=1)

    # Normalize intensity values to [0, 1]
    original_range = (img.min(), img.max())
    normed_img = (img - img.min()) / (img.max() - img.min())

    experimental_data = {
        "mean_proportion_expected": 0.8,
        "CI95_proportion_expected": (-0.123961, 0.123961),
    }

    stim = {
        "img": normed_img,
        "target_mask": mask.astype(int),
        "visual_size": np.array(normed_img.shape) / ppd,
        "shape": normed_img.shape,
        "ppd": ppd,
        "intensity_range": (0.0, 1.0),
        "original_range": original_range,
        "experimental_data": experimental_data,
    }
    return stim


def koffka_adelson(ppd=PPD):
    """Koffka-Adelson figure, Murray (2020) Fig 1e

    Parameters
    ----------
    ppd : int
        Resolution of stimulus in pixels per degree. (default: 32)

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "target_mask")
        and additional keys containing stimulus parameters

    References
    ----------
    Murray, R. F. (2020).
        A model of lightness perception
        guided by probabilistic assumptions about lighting and reflectance.
        Journal of Vision, 20(7), 28.
        https://doi.org/10/gh57gf
    """

    a = mat_content["koffka_adelson"]
    img = np.array(((a[0])[0])[0])
    target1 = np.array((((a[0])[0])[1])[0])
    target2 = np.array((((a[0])[0])[2])[0])
    mask = get_mask(target1, target2, img.shape)

    img = img.repeat(repeats=int(ppd / PPD), axis=0).repeat(repeats=int(ppd / PPD), axis=1)
    mask = mask.repeat(repeats=int(ppd / PPD), axis=0).repeat(repeats=int(ppd / PPD), axis=1)

    # Normalize intensity values to [0, 1]
    original_range = (img.min(), img.max())
    normed_img = (img - img.min()) / (img.max() - img.min())

    experimental_data = {
        "mean_proportion_expected": 0.8375,
        "CI95_proportion_expected": (-0.114326, 0.114326),
    }

    stim = {
        "img": normed_img,
        "target_mask": mask.astype(int),
        "visual_size": np.array(normed_img.shape) / ppd,
        "shape": normed_img.shape,
        "ppd": ppd,
        "intensity_range": (0.0, 1.0),
        "original_range": original_range,
        "experimental_data": experimental_data,
    }
    return stim


def koffka_broken(ppd=PPD):
    """Koffka ring, broken, Murray (2020) Fig 1d

    Parameters
    ----------
    ppd : int
        Resolution of stimulus in pixels per degree. (default: 32)

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "target_mask")
        and additional keys containing stimulus parameters

    References
    ----------
    Murray, R. F. (2020).
        A model of lightness perception
        guided by probabilistic assumptions about lighting and reflectance.
        Journal of Vision, 20(7), 28.
        https://doi.org/10/gh57gf
    """

    a = mat_content["koffka_broken"]
    img = np.array(((a[0])[0])[0])
    target1 = np.array((((a[0])[0])[1])[0])
    target2 = np.array((((a[0])[0])[2])[0])
    mask = get_mask(target1, target2, img.shape)

    img = img.repeat(repeats=int(ppd / PPD), axis=0).repeat(repeats=int(ppd / PPD), axis=1)
    mask = mask.repeat(repeats=int(ppd / PPD), axis=0).repeat(repeats=int(ppd / PPD), axis=1)

    # Normalize intensity values to [0, 1]
    original_range = (img.min(), img.max())
    normed_img = (img - img.min()) / (img.max() - img.min())

    experimental_data = {
        "mean_proportion_expected": 0.8,
        "CI95_proportion_expected": (-0.123961, 0.123961),
    }

    stim = {
        "img": normed_img,
        "target_mask": mask.astype(int),
        "visual_size": np.array(normed_img.shape) / ppd,
        "shape": normed_img.shape,
        "ppd": ppd,
        "intensity_range": (0.0, 1.0),
        "original_range": original_range,
        "experimental_data": experimental_data,
    }
    return stim


def koffka_connected(ppd=PPD):
    """Koffka ring, connected, Murray (2020) Fig 1f

    Parameters
    ----------
    ppd : int
        Resolution of stimulus in pixels per degree. (default: 32)

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "target_mask")
        and additional keys containing stimulus parameters

    References
    ----------
    Murray, R. F. (2020).
        A model of lightness perception
        guided by probabilistic assumptions about lighting and reflectance.
        Journal of Vision, 20(7), 28.
        https://doi.org/10/gh57gf
    """

    a = mat_content["koffka_connected"]
    img = np.array(((a[0])[0])[0])
    target1 = np.array((((a[0])[0])[1])[0])
    target2 = np.array((((a[0])[0])[2])[0])
    mask = get_mask(target1, target2, img.shape)

    img = img.repeat(repeats=int(ppd / PPD), axis=0).repeat(repeats=int(ppd / PPD), axis=1)
    mask = mask.repeat(repeats=int(ppd / PPD), axis=0).repeat(repeats=int(ppd / PPD), axis=1)

    # Normalize intensity values to [0, 1]
    original_range = (img.min(), img.max())
    normed_img = (img - img.min()) / (img.max() - img.min())

    experimental_data = {
        "mean_proportion_expected": 0.6,
        "CI95_proportion_expected": (-0.151821, 0.151821),
    }

    stim = {
        "img": normed_img,
        "target_mask": mask.astype(int),
        "visual_size": np.array(normed_img.shape) / ppd,
        "shape": normed_img.shape,
        "ppd": ppd,
        "intensity_range": (0.0, 1.0),
        "original_range": original_range,
        "experimental_data": experimental_data,
    }
    return stim


def checkassim(ppd=PPD, pad=PAD):
    """Checkerboard assimilation, Murray (2020) Fig 1h

    Parameters
    ----------
    ppd : int
        Resolution of stimulus in pixels per degree. (default: 32)

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "target_mask")
        and additional keys containing stimulus parameters

    References
    ----------
    Murray, R. F. (2020).
        A model of lightness perception
        guided by probabilistic assumptions about lighting and reflectance.
        Journal of Vision, 20(7), 28.
        https://doi.org/10/gh57gf
    """

    params = {
        "ppd": ppd,
        "board_shape": (7, 10),
        "check_visual_size": 1 / PPD,
        "target_indices": ((3, 6), (3, 3)),
        "extend_targets": False,
        "intensity_checks": (17.5, 70.0),
        "intensity_target": 35.0,
    }
    stim = stimupy.checkerboards.checkerboard(
        **params,
    )

    if pad:
        padding = np.array(((4, 5), (3, 3))) / PPD
        stim = pad_dict_by_visual_size(stim, padding, ppd=ppd, pad_value=35.0)
        params["padding"] = padding

    # Normalize intensity values to [0, 1]
    original_range = (stim["img"].min(), stim["img"].max())
    stim["img"] = (stim["img"] - stim["img"].min()) / (stim["img"].max() - stim["img"].min())

    experimental_data = {
        "mean_proportion_expected": 0.8625,
        "CI95_proportion_expected": (-0.106723, 0.106723),
    }

    params.update(
        visual_size=np.array(stim["img"].shape) / ppd,
        shape=stim["img"].shape,
        original_range=original_range,
        intensity_range=(0.0, 1.0),
        experimental_data=experimental_data,
    )
    return {**stim, **params}


def simcon(ppd=PPD):
    """Classic simultaneous contrast figure, Murray (2020) Fig 1k

    Parameters
    ----------
    ppd : int
        Resolution of stimulus in pixels per degree. (default: 32)

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "target_mask")
        and additional keys containing stimulus parameters

    References
    ----------
    Murray, R. F. (2020).
        A model of lightness perception
        guided by probabilistic assumptions about lighting and reflectance.
        Journal of Vision, 20(7), 28.
        https://doi.org/10/gh57gf
    """

    a = mat_content["simcon"]
    img = np.array(((a[0])[0])[0])
    target1 = np.array((((a[0])[0])[1])[0])
    target2 = np.array((((a[0])[0])[2])[0])
    mask = get_mask(target1, target2, img.shape)

    img = img.repeat(repeats=int(ppd / PPD), axis=0).repeat(repeats=int(ppd / PPD), axis=1)
    mask = mask.repeat(repeats=int(ppd / PPD), axis=0).repeat(repeats=int(ppd / PPD), axis=1)

    # Normalize intensity values to [0, 1]
    original_range = (img.min(), img.max())
    normed_img = (img - img.min()) / (img.max() - img.min())

    experimental_data = {
        "mean_proportion_expected": 0.925,
        "CI95_proportion_expected": (-0.0816258, 0.0816258),
    }

    stim = {
        "img": normed_img,
        "target_mask": mask.astype(int),
        "visual_size": np.array(normed_img.shape) / ppd,
        "shape": normed_img.shape,
        "ppd": ppd,
        "intensity_range": (0.0, 1.0),
        "original_range": original_range,
        "experimental_data": experimental_data,
    }
    return stim


def simcon_articulated(ppd=PPD):
    """Articulated simultaneous contrast figure, Murray (2020) Fig 1l

    Parameters
    ----------
    ppd : int
        Resolution of stimulus in pixels per degree. (default: 32)

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "target_mask")
        and additional keys containing stimulus parameters

    References
    ----------
    Murray, R. F. (2020).
        A model of lightness perception
        guided by probabilistic assumptions about lighting and reflectance.
        Journal of Vision, 20(7), 28.
        https://doi.org/10/gh57gf
    """

    a = mat_content["simcon_articulated"]
    img = np.array(((a[0])[0])[0])
    target1 = np.array((((a[0])[0])[1])[0])
    target2 = np.array((((a[0])[0])[2])[0])
    mask = get_mask(target1, target2, img.shape)

    img = img.repeat(repeats=int(ppd / PPD), axis=0).repeat(repeats=int(ppd / PPD), axis=1)
    mask = mask.repeat(repeats=int(ppd / PPD), axis=0).repeat(repeats=int(ppd / PPD), axis=1)

    # Normalize intensity values to [0, 1]
    original_range = (img.min(), img.max())
    normed_img = (img - img.min()) / (img.max() - img.min())

    experimental_data = {
        "mean_proportion_expected": 1.0,
        "CI95_proportion_expected": (-0.0, 0.0),
    }

    stim = {
        "img": normed_img,
        "target_mask": mask.astype(int),
        "visual_size": np.array(normed_img.shape) / ppd,
        "shape": normed_img.shape,
        "ppd": ppd,
        "intensity_range": (0.0, 1.0),
        "original_range": original_range,
        "experimental_data": experimental_data,
    }
    return stim


def white(ppd=PPD):
    """White's illusion, Murray (2020) Fig 1A

    Parameters
    ----------
    ppd : int
        Resolution of stimulus in pixels per degree. (default: 32)

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "target_mask")
        and additional keys containing stimulus parameters

    References
    ----------
    Murray, R. F. (2020).
        A model of lightness perception
        guided by probabilistic assumptions about lighting and reflectance.
        Journal of Vision, 20(7), 28.
        https://doi.org/10/gh57gf
    """

    params = {
        "ppd": ppd,
        "visual_size": (8.0, 8.0),
        "frequency": 4.0 / 8.0,
        "target_indices_top": (1, 3, 5),
        "target_indices_bottom": (2, 4, 6),
        "target_center_offset": 2,
        "target_heights": 2,
        "intensity_bars": (70, 17.5),
        "intensity_target": 35.0,
        "period": "even",
    }

    stim = stimupy.whites.white_two_rows(**params)
    stim = rotate_dict(stim)
    reduced_mask = np.where(stim["target_mask"] == 2, 2, 0)
    reduced_mask = np.where(stim["target_mask"] == 5, 1, reduced_mask).astype(int)

    # Normalize intensity values to [0, 1]
    img = stim["img"]
    original_range = (img.min(), img.max())
    normed_img = (img - img.min()) / (img.max() - img.min())

    experimental_data = {
        "mean_proportion_expected": 0.95,
        "CI95_proportion_expected": (-0.0675418, 0.0675418),
    }

    params.update(
        visual_size=np.array(normed_img.shape) / ppd,
        shape=normed_img.shape,
        original_range=original_range,
        intensity_range=(0.0, 1.0),
        experimental_data=experimental_data,
    )
    return {"img": normed_img, "target_mask": reduced_mask, **params}


if __name__ == "__main__":
    from stimupy.utils import plot_stimuli

    # Generate all stimuli exported in __all__
    stims = gen_all(skip=True)
    plot_stimuli(stims, mask=True)
