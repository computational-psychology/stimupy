"""Stimuli from Domijan (2015) https://doi.org/10.3389/fnhum.2015.00093

This module reproduces all of the stimuli used by Domijan (2015)
as they were provided to the model described in that paper.
Since the stimulus sizes were only defined in pixel-space,
there is some ambiguity with respect to the stimulus sizes in
degrees visual angle.
To help solve this ambiguity, we approximated a realistic resolution
of the stimuli (ppd = 10) which is set as default value.
However, because of the ambiguity, it is possible to change the
stimulus sizes by providing at least two of the following: a shape
(in pixels), a visual_size (in degrees) and/or a resolution (in ppd).

Each stimulus is provided by a separate function,
a full list can be found as stimuli.papers.domijan2015.__all__

The output of each of these functions is a stimulus dictionary.

For a visual representation of all the stimuli and their mask,
simply run this module as a script:

    $ python stimuli/papers/domijan2015.py

Attributes
----------
__all__ (list of str): list of all stimulus-functions
    that are exported by this module when executing
        >>> from stimuli.papers.domijan2015 import *

References
-----------
Domijan, D. (2015). A neurocomputational account of the role of contour
facilitation in brightness perception. Frontiers in Human Neuroscience,
9, 93. https://doi.org/10.3389/fnhum.2015.00093
"""

import numpy as np

from stimuli import illusions
from stimuli.utils import pad_by_visual_size
from stimuli.utils.resolution import resolve

# TODO: Add warning when stimulus shape or visual_size is different from what requested!

__all__ = [
    "dungeon",
    "cube",
    "grating",
    "rings",
    "bullseye",
    "simultaneous_brightness_contrast",
    "white",
    "benary",
    "todorovic",
    "checkerboard_contrast_contrast",
    "checkerboard",
    "checkerboard_extended",
    "white_yazdanbakhsh",
    "white_anderson",
    "white_howe",
]

# Default values:
PPD = 10
PAD = True
SHAPES = {
    "dungeon": (110, 220),
    "cube": (100, 200),
    "grating": (100, 220),
    "rings": (100, 200),
    "bullseye": (100, 200),
    "simultaneous_brightness_contrast": (100, 200),
    "white": (80, 80),
    "benary": (100, 100),
    "todorovic": (100, 200),
    "checkerboard_contrast_contrast": (80, 160),
    "checkerboard": (80, 80),
    "checkerboard_extended": (80, 80),
    "white_yazdanbakhsh": (80, 80),
    "white_anderson": (100, 100),
    "white_howe": (100, 100),
}

VSIZES = {
    "dungeon": np.array(SHAPES["dungeon"]) / PPD,
    "cube": np.array(SHAPES["cube"]) / PPD,
    "grating": np.array(SHAPES["grating"]) / PPD,
    "rings": np.array(SHAPES["rings"]) / PPD,
    "bullseye": np.array(SHAPES["bullseye"]) / PPD,
    "simultaneous_brightness_contrast": np.array(SHAPES["simultaneous_brightness_contrast"]) / PPD,
    "white": np.array(SHAPES["white"]) / PPD,
    "benary": np.array(SHAPES["benary"]) / PPD,
    "todorovic": np.array(SHAPES["todorovic"]) / PPD,
    "checkerboard_contrast_contrast": np.array(SHAPES["checkerboard_contrast_contrast"]) / PPD,
    "checkerboard": np.array(SHAPES["checkerboard"]) / PPD,
    "checkerboard_extended": np.array(SHAPES["checkerboard_extended"]) / PPD,
    "white_yazdanbakhsh": np.array(SHAPES["white_yazdanbakhsh"]) / PPD,
    "white_anderson": np.array(SHAPES["white_anderson"]) / PPD,
    "white_howe": np.array(SHAPES["white_howe"]) / PPD,
}

v1, v2, v3 = 0.0, 0.5, 1.0


def gen_all(ppd=PPD, skip=False):
    stims = {}  # save the stimulus-dicts in a larger dict, with name as key
    for stim_name in __all__:
        print(f"Generating domijan2015.{stim_name}")

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


def resolve_input(inpt):
    if isinstance(inpt, (float, int)):
        inpt = (inpt, None)
    if inpt is None:
        inpt = (None, None)
    if len(inpt) > 2:
        raise ValueError("argument has too many dimensions")
    return inpt


def get_conversion_1d(original_shape, shape, visual_size, ppd):
    if shape is None and (visual_size is None or ppd is None):
        raise ValueError("You need to define two out of ppd, shape and visual_size")
    if visual_size is None and (shape is None or ppd is None):
        raise ValueError("You need to define two out of ppd, shape and visual_size")

    if shape is not None and ppd is not None:
        conversion_fac = shape / original_shape * PPD / ppd

    if visual_size is not None and ppd is not None:
        conversion_fac = visual_size / original_shape * PPD

    if shape is not None and visual_size is not None and ppd is not None:
        ppd_calc = int(np.round(shape / visual_size))
        assert ppd_calc == ppd
        conversion_fac = shape / original_shape * PPD / ppd

    if shape is not None and visual_size is not None and ppd is None:
        ppd = int(np.round(shape / visual_size))
        conversion_fac = shape / original_shape * PPD / ppd
    return conversion_fac / PPD


def get_conversion_2d(original_shape, shape, visual_size, ppd):
    try:
        c1 = get_conversion_1d(original_shape[0], shape[0], visual_size[0], ppd)
    except Exception:
        c1 = None

    try:
        c2 = get_conversion_1d(original_shape[1], shape[1], visual_size[1], ppd)
    except Exception:
        c2 = c1

    if c1 is None:
        c1 = c2
    if c1 != c2:
        raise ValueError(
            "Requested shape/visual_size is impossible given the stimulus defaults. "
            "Consider setting either the height or width to None"
        )
    return c1


def dungeon(shape=SHAPES["dungeon"], ppd=PPD, visual_size=VSIZES["dungeon"]):
    """Dungeon illusion, Domijan (2015) Fig 6A

    Parameters
    ----------
    shape : None, int or (int/None, int/None)
        Stimulus shape in deg, (height, width), default: (110, 220)
        If None, will infer shape from ppd and visual size.
        If int, it will be used as height.
        If either height=None or width=None, the other will be inferred.
    ppd : int
        Resolution of stimulus in pixels per degree. (default: 10)
    visual_size : None, int or (int/None, int/None)
        Stimulus size in degree, (height, width), default: (11, 22)
        If None, will infer size from shape and ppd.
        If int, it will be used as height.
        If either height=None or width=None, the other will be inferred.

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "mask")
        and additional keys containing stimulus parameters

    References
    -----------
    Domijan, D. (2015). A neurocomputational account of the role of contour
        facilitation in brightness perception. Frontiers in Human Neuroscience,
        9, 93. https://doi.org/10.3389/fnhum.2015.00093
    """

    shape = resolve_input(shape)
    visual_size = resolve_input(visual_size)
    c = get_conversion_2d(SHAPES["dungeon"], shape, visual_size, ppd)
    shape, visual_size, ppd = resolve(None, np.array(SHAPES["dungeon"]) * c, ppd)
    ppd = ppd[0]

    params = {
        "ppd": ppd,
        "n_cells": 5,
        "target_radius": 1,
        "cell_size": 10.0 * c,
    }

    stim1 = illusions.dungeon.dungeon_illusion(
        **params,
        intensity_background=v1,
        intensity_grid=v3,
        intensity_target=v2,
    )

    stim2 = illusions.dungeon.dungeon_illusion(
        **params,
        intensity_background=v3,
        intensity_grid=v1,
        intensity_target=v2,
    )

    padding = np.array((9.0, 11.0)) * c
    stim1["img"] = pad_by_visual_size(stim1["img"], padding, ppd, v1)
    stim1["mask"] = pad_by_visual_size(stim1["mask"], padding, ppd, 0)
    stim2["img"] = pad_by_visual_size(stim2["img"], padding, ppd, v3)
    stim2["mask"] = pad_by_visual_size(stim2["mask"], padding, ppd, 0)

    # Stacking
    img = np.hstack([stim1["img"], stim2["img"]])
    mask = np.hstack([stim1["mask"], stim2["mask"] * 2])

    params.update(
        original_shape=SHAPES["dungeon"],
        original_ppd=PPD,
        original_visual_size=np.array(SHAPES["dungeon"]) / PPD,
        original_range=(1, 9),
        intensity_range=(v1, v3),
        visual_size=np.array(img.shape) / ppd,
        shape=img.shape,
    )
    return {"img": img, "mask": mask, **params}


def cube(shape=SHAPES["cube"], ppd=PPD, visual_size=VSIZES["cube"]):
    """Cube illusion, Domijan (2015) Fig 6B

    Parameters
    ----------
    shape : None, int or (int/None, int/None)
        Stimulus shape in deg, (height, width), default: (100, 200)
        If None, will infer shape from ppd and visual size.
        If int, it will be used as height.
        If either height=None or width=None, the other will be inferred.
    ppd : int
        Resolution of stimulus in pixels per degree. (default: 10)
    visual_size : None, int or (int/None, int/None)
        Stimulus size in degree, (height, width), default: (10, 20)
        If None, will infer size from shape and ppd.
        If int, it will be used as height.
        If either height=None or width=None, the other will be inferred.

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "mask")
        and additional keys containing stimulus parameters

    References
    -----------
    Domijan, D. (2015). A neurocomputational account of the role of contour
        facilitation in brightness perception. Frontiers in Human Neuroscience,
        9, 93. https://doi.org/10.3389/fnhum.2015.00093
    """

    shape = resolve_input(shape)
    visual_size = resolve_input(visual_size)
    c = get_conversion_2d(SHAPES["cube"], shape, visual_size, ppd)
    shape, visual_size, ppd = resolve(None, np.array(SHAPES["cube"]) * c, ppd)
    ppd = ppd[0]

    params = {
        "ppd": ppd,
        "n_cells": 4,
        "target_length": 2,
        "cell_long": 15.0 * c,
        "cell_short": 11.0 * c,
        "corner_cell_width": 18.0 * c,
        "corner_cell_height": 18.0 * c,
        "cell_spacing": 5.0 * c,
        "occlusion_overlap": np.array((7,) * 4) * c,
    }

    stim1 = illusions.cube.cube_illusion(
        **params,
        intensity_background=v1,
        intensity_grid=v3,
        intensity_target=v2,
    )
    stim2 = illusions.cube.cube_illusion(
        **params,
        intensity_background=v3,
        intensity_grid=v1,
        intensity_target=v2,
    )

    # Padding
    padding = np.array((9.0, 10.0)) * c
    img1 = pad_by_visual_size(stim1["img"], padding, ppd, v1)
    mask1 = pad_by_visual_size(stim1["mask"], padding, ppd, 0)
    img2 = pad_by_visual_size(stim2["img"], padding, ppd, v3)
    mask2 = pad_by_visual_size(stim2["mask"], padding, ppd, 0)

    # Increase target index of right stimulus half
    mask2 = mask2 + 1
    mask2[mask2 == 1] = 0

    # Stacking
    img = np.hstack([img1, img2])
    mask = np.hstack([mask1, mask2])

    params.update(
        original_shape=SHAPES["cube"],
        original_ppd=PPD,
        original_visual_size=np.array(SHAPES["cube"]) / PPD,
        original_range=(1, 9),
        intensity_range=(v1, v3),
        visual_size=np.array(img.shape) / ppd,
        shape=img.shape,
    )
    return {"img": img, "mask": mask, **params}


def grating(shape=SHAPES["grating"], ppd=PPD, visual_size=VSIZES["grating"]):
    """Grating illusion, Domijan (2015) Fig 6C

    Parameters
    ----------
    shape : None, int or (int/None, int/None)
        Stimulus shape in deg, (height, width), default: (100, 220)
        If None, will infer shape from ppd and visual size.
        If int, it will be used as height.
        If either height=None or width=None, the other will be inferred.
    ppd : int
        Resolution of stimulus in pixels per degree. (default: 10)
    visual_size : None, int or (int/None, int/None)
        Stimulus size in degree, (height, width), default: (10, 22)
        If None, will infer size from shape and ppd.
        If int, it will be used as height.
        If either height=None or width=None, the other will be inferred.

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "mask")
        and additional keys containing stimulus parameters

    References
    -----------
    Domijan, D. (2015). A neurocomputational account of the role of contour
        facilitation in brightness perception. Frontiers in Human Neuroscience,
        9, 93. https://doi.org/10.3389/fnhum.2015.00093
    """

    shape = resolve_input(shape)
    visual_size = resolve_input(visual_size)
    c = get_conversion_2d(SHAPES["grating"], shape, visual_size, ppd)
    shape, visual_size, ppd = resolve(None, np.array(SHAPES["grating"]) * c, ppd)
    ppd = ppd[0]

    params = {
        "ppd": ppd,
        "n_bars": 9,
        "target_indices": (4,),
        "bar_shape": (81 * c, 10 * c),
    }

    stim1 = illusions.grating.grating_illusion(
        **params,
        intensity_bars=(v3, v1),
        intensity_target=v2,
    )
    stim2 = illusions.grating.grating_illusion(
        **params,
        intensity_bars=(v1, v3),
        intensity_target=v2,
    )

    # Padding
    padding = np.array(((9.0, 10.0), (9.0, 11.0))) * c
    img1 = pad_by_visual_size(stim1["img"], padding, ppd, v1)
    mask1 = pad_by_visual_size(stim1["mask"], padding, ppd, 0)
    img2 = pad_by_visual_size(stim2["img"], padding, ppd, v3)
    mask2 = pad_by_visual_size(stim2["mask"], padding, ppd, 0)

    # Increase target index of right stimulus half
    mask2 = mask2 + 1
    mask2[mask2 == 1] = 0

    # Stacking
    img = np.hstack([img1, img2])
    mask = np.hstack([mask1, mask2])

    params.update(
        original_shape=SHAPES["grating"],
        original_ppd=PPD,
        original_visual_size=np.array(SHAPES["grating"]) / PPD,
        original_range=(1, 9),
        intensity_range=(v1, v3),
        visual_size=np.array(img.shape) / ppd,
        shape=img.shape,
    )
    return {"img": img, "mask": mask, **params}


def rings(shape=SHAPES["rings"], ppd=PPD, visual_size=VSIZES["rings"]):
    """Ring patterns, Domijan (2015) Fig 7A

    Parameters
    ----------
    shape : None, int or (int/None, int/None)
        Stimulus shape in deg, (height, width), default: (100, 200)
        If None, will infer shape from ppd and visual size.
        If int, it will be used as height.
        If either height=None or width=None, the other will be inferred.
    ppd : int
        Resolution of stimulus in pixels per degree. (default: 10)
    visual_size : None, int or (int/None, int/None)
        Stimulus size in degree, (height, width), default: (10, 20)
        If None, will infer size from shape and ppd.
        If int, it will be used as height.
        If either height=None or width=None, the other will be inferred.

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "mask")
        and additional keys containing stimulus parameters

    References
    -----------
    Domijan, D. (2015). A neurocomputational account of the role of contour
        facilitation in brightness perception. Frontiers in Human Neuroscience,
        9, 93. https://doi.org/10.3389/fnhum.2015.00093
    """

    shape = resolve_input(shape)
    visual_size = resolve_input(visual_size)
    c = get_conversion_2d(SHAPES["rings"], shape, visual_size, ppd)
    shape, visual_size, ppd = resolve(None, np.array(SHAPES["rings"]) * c, ppd)
    ppd = ppd[0]

    params = {
        "ppd": ppd,
        "n_rings": 8,
        "ring_width": 5.0 * c,
    }

    stim1 = illusions.rings.ring_stimulus(
        **params,
        target_idx=4,
        intensity_rings=(v1, v3),
        intensity_target=v2,
    )
    stim2 = illusions.rings.ring_stimulus(
        **params,
        target_idx=3,
        intensity_rings=(v1, v3),
        intensity_target=v2,
    )

    # Padding
    padding = np.array((9.0, 10.0)) * c
    img1 = pad_by_visual_size(stim1["img"], padding, ppd, v1)
    mask1 = pad_by_visual_size(stim1["mask"], padding, ppd, 0)
    img2 = pad_by_visual_size(stim2["img"], padding, ppd, v1)
    mask2 = pad_by_visual_size(stim2["mask"], padding, ppd, 0)

    # Increase target index of right stimulus half
    mask2 = mask2 + 1
    mask2[mask2 == 1] = 0

    # Stacking
    img = np.hstack([img1, img2])
    mask = np.hstack([mask1, mask2])

    params.update(
        original_shape=SHAPES["rings"],
        original_ppd=PPD,
        original_visual_size=np.array(SHAPES["rings"]) / PPD,
        original_range=(1, 9),
        intensity_range=(v1, v3),
        visual_size=np.array(img.shape) / ppd,
        shape=img.shape,
        target_idx_left=4,
        target_idx_right=3,
    )
    return {"img": img, "mask": mask, **params}


def bullseye(shape=SHAPES["bullseye"], ppd=PPD, visual_size=VSIZES["bullseye"]):
    """Bullseye illusion, Domijan (2015) Fig 7B

    Parameters
    ----------
    shape : None, int or (int/None, int/None)
        Stimulus shape in deg, (height, width), default: (100, 200)
        If None, will infer shape from ppd and visual size.
        If int, it will be used as height.
        If either height=None or width=None, the other will be inferred.
    ppd : int
        Resolution of stimulus in pixels per degree. (default: 10)
    visual_size : None, int or (int/None, int/None)
        Stimulus size in degree, (height, width), default: (10, 20)
        If None, will infer size from shape and ppd.
        If int, it will be used as height.
        If either height=None or width=None, the other will be inferred.

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "mask")
        and additional keys containing stimulus parameters

    References
    -----------
    Domijan, D. (2015). A neurocomputational account of the role of contour
        facilitation in brightness perception. Frontiers in Human Neuroscience,
        9, 93. https://doi.org/10.3389/fnhum.2015.00093
    """

    shape = resolve_input(shape)
    visual_size = resolve_input(visual_size)
    c = get_conversion_2d(SHAPES["bullseye"], shape, visual_size, ppd)
    shape, visual_size, ppd = resolve(None, np.array(SHAPES["bullseye"]) * c, ppd)
    ppd = ppd[0]

    params = {
        "ppd": ppd,
        "n_rings": 8,
        "ring_width": 5.0 * c,
    }

    stim1 = illusions.bullseye.bullseye_stimulus(
        **params,
        intensity_rings=(v1, v3),
        intensity_target=v2,
    )
    stim2 = illusions.bullseye.bullseye_stimulus(
        **params,
        intensity_rings=(v3, v1),
        intensity_target=v2,
    )

    # Padding
    padding = np.array((9.0, 10.0)) * c
    img1 = pad_by_visual_size(stim1["img"], padding, ppd, v1)
    mask1 = pad_by_visual_size(stim1["mask"], padding, ppd, 0)
    img2 = pad_by_visual_size(stim2["img"], padding, ppd, v1)
    mask2 = pad_by_visual_size(stim2["mask"], padding, ppd, 0)

    # Increase target index of right stimulus half
    mask2 = mask2 + 1
    mask2[mask2 == 1] = 0

    # Stacking
    img = np.hstack([img1, img2])
    mask = np.hstack([mask1, mask2])

    params.update(
        original_shape=SHAPES["bullseye"],
        original_ppd=PPD,
        original_visual_size=np.array(SHAPES["bullseye"]) / PPD,
        original_range=(1, 9),
        intensity_range=(v1, v3),
        visual_size=np.array(img.shape) / ppd,
        shape=img.shape,
    )
    return {"img": img, "mask": mask, **params}


def simultaneous_brightness_contrast(
    shape=SHAPES["simultaneous_brightness_contrast"],
    ppd=PPD,
    visual_size=VSIZES["simultaneous_brightness_contrast"],
):
    """Simultaneous brightness contrast, Domijan (2015) Fig 7C

    Parameters
    ----------
    shape : None, int or (int/None, int/None)
        Stimulus shape in deg, (height, width), default: (100, 200)
        If None, will infer shape from ppd and visual size.
        If int, it will be used as height.
        If either height=None or width=None, the other will be inferred.
    ppd : int
        Resolution of stimulus in pixels per degree. (default: 10)
    visual_size : None, int or (int/None, int/None)
        Stimulus size in degree, (height, width), default: (10, 20)
        If None, will infer size from shape and ppd.
        If int, it will be used as height.
        If either height=None or width=None, the other will be inferred.

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "mask")
        and additional keys containing stimulus parameters

    References
    -----------
    Domijan, D. (2015). A neurocomputational account of the role of contour
        facilitation in brightness perception. Frontiers in Human Neuroscience,
        9, 93. https://doi.org/10.3389/fnhum.2015.00093
    """

    shape = resolve_input(shape)
    visual_size = resolve_input(visual_size)
    c = get_conversion_2d(SHAPES["simultaneous_brightness_contrast"], shape, visual_size, ppd)
    shape, visual_size, ppd = resolve(
        None, np.array(SHAPES["simultaneous_brightness_contrast"]) * c, ppd
    )
    ppd = ppd[0]

    params = {
        "visual_size": visual_size[0],
        "ppd": ppd,
        "target_size": (21 * c, 21 * c),
        "target_pos": (39 * c, 39 * c),
    }

    stim1 = illusions.sbc.simultaneous_contrast_generalized(
        **params,
        intensity_background=v3,
        intensity_target=v2,
    )
    stim2 = illusions.sbc.simultaneous_contrast_generalized(
        **params,
        intensity_background=v1,
        intensity_target=v2,
    )

    # Increase target index of right stimulus half
    mask2 = stim2["mask"] + 1
    mask2[mask2 == 1] = 0

    # Stacking
    img = np.hstack([stim1["img"], stim2["img"]])
    mask = np.hstack([stim1["mask"], mask2])

    params.update(
        original_shape=SHAPES["simultaneous_brightness_contrast"],
        original_ppd=PPD,
        original_visual_size=np.array(SHAPES["simultaneous_brightness_contrast"]) / PPD,
        original_range=(1, 9),
        intensity_range=(v1, v3),
        visual_size=np.array(img.shape) / ppd,
        shape=img.shape,
    )
    return {"img": img, "mask": mask, **params}


def white(shape=SHAPES["white"], ppd=PPD, visual_size=VSIZES["white"], pad=PAD):
    """White stimulus, Domijan (2015) Fig 8A

    Parameters
    ----------
    shape : None, int or (int/None, int/None)
        Stimulus shape in deg, (height, width), default: (80, 80)
        If None, will infer shape from ppd and visual size.
        If int, it will be used as height.
        If either height=None or width=None, the other will be inferred.
    ppd : int
        Resolution of stimulus in pixels per degree. (default: 10)
    visual_size : None, int or (int/None, int/None)
        Stimulus size in degree, (height, width), default: (80, 80)
        If None, will infer size from shape and ppd.
        If int, it will be used as height.
        If either height=None or width=None, the other will be inferred.
    pad : bool
        If True, include original padding (default: False)

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "mask")
        and additional keys containing stimulus parameters

    References
    -----------
    Domijan, D. (2015). A neurocomputational account of the role of contour
        facilitation in brightness perception. Frontiers in Human Neuroscience,
        9, 93. https://doi.org/10.3389/fnhum.2015.00093
    """

    shape = resolve_input(shape)
    visual_size = resolve_input(visual_size)
    c = get_conversion_2d(SHAPES["white"], shape, visual_size, ppd)
    shape, visual_size, ppd = resolve(None, np.array(SHAPES["white"]) * c, ppd)
    ppd = ppd[0]

    params = {
        "visual_size": visual_size,
        "ppd": ppd,
        "grating_frequency": 4.0 / visual_size[1],
        "target_indices": (2, 5),
        "target_size": 21 * c,
        "period": "full",
    }

    stim = illusions.whites.white(
        **params,
        intensity_bars=(v1, v3),
        intensity_target=v2,
    )

    if pad:
        padding = np.array((9.0, 11.0)) * c
        stim["img"] = pad_by_visual_size(stim["img"], padding, ppd, pad_value=v2)
        stim["mask"] = pad_by_visual_size(stim["mask"], padding, ppd, pad_value=0)
        params["padding"] = padding

    original_shape_np = np.array(SHAPES["white"])
    original_visual_np = np.array(original_shape_np) / PPD
    original_shape = original_shape_np + 20
    original_visual_size = original_shape / PPD
    params.update(
        original_shape=original_shape,
        original_ppd=PPD,
        original_visual_size=original_visual_size,
        original_shape_no_padding=original_shape_np,
        original_visual_size_no_padding=original_visual_np,
        original_range=(1, 9),
        intensity_range=(v1, v3),
        visual_size=np.array(stim["img"].shape) / ppd,
        shape=stim["img"].shape,
    )
    return {**stim, **params}


def benary(shape=SHAPES["benary"], ppd=PPD, visual_size=VSIZES["benary"]):
    """Benarys cross, Domijan (2015) Fig 8B

    Parameters
    ----------
    shape : None, int or (int/None, int/None)
        Stimulus shape in deg, (height, width), default: (100, 100)
        If None, will infer shape from ppd and visual size.
        If int, it will be used as height.
        If either height=None or width=None, the other will be inferred.
    ppd : int
        Resolution of stimulus in pixels per degree. (default: 10)
    visual_size : None, int or (int/None, int/None)
        Stimulus size in degree, (height, width), default: (10, 10)
        If None, will infer size from shape and ppd.
        If int, it will be used as height.
        If either height=None or width=None, the other will be inferred.

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "mask")
        and additional keys containing stimulus parameters

    References
    -----------
    Domijan, D. (2015). A neurocomputational account of the role of contour
        facilitation in brightness perception. Frontiers in Human Neuroscience,
        9, 93. https://doi.org/10.3389/fnhum.2015.00093
    """

    shape = resolve_input(shape)
    visual_size = resolve_input(visual_size)
    c = get_conversion_2d(SHAPES["benary"], shape, visual_size, ppd)
    shape, visual_size, ppd = resolve(None, np.array(SHAPES["benary"]) * c, ppd)
    ppd = ppd[0]

    params = {
        "visual_size": 81 * c,
        "ppd": ppd,
        "cross_thickness": 21 * c,
        "target_size": 11 * c,
    }

    stim = illusions.benary_cross.benarys_cross_rectangles(
        **params,
        intensity_background=v3,
        intensity_cross=v1,
        intensity_target=v2,
    )

    # Padding
    padding = np.array((9, 10.0)) * c
    stim["img"] = pad_by_visual_size(stim["img"], padding, ppd, pad_value=1.0)
    stim["mask"] = pad_by_visual_size(stim["mask"], padding, ppd, pad_value=0)

    params.update(
        original_shape=SHAPES["benary"],
        original_ppd=PPD,
        original_visual_size=np.array(SHAPES["benary"]) / PPD,
        original_range=(1, 9),
        intensity_range=(v1, v3),
        visual_size=np.array(stim["img"].shape) / ppd,
        shape=stim["img"].shape,
    )
    return {**stim, **params}


def todorovic(shape=SHAPES["todorovic"], ppd=PPD, visual_size=VSIZES["todorovic"]):
    """Todorovic stimulus, Domijan (2015) Fig 9A

    Parameters
    ----------
    shape : None, int or (int/None, int/None)
        Stimulus shape in deg, (height, width), default: (100, 200)
        If None, will infer shape from ppd and visual size.
        If int, it will be used as height.
        If either height=None or width=None, the other will be inferred.
    ppd : int
        Resolution of stimulus in pixels per degree. (default: 10)
    visual_size : None, int or (int/None, int/None)
        Stimulus size in degree, (height, width), default: (10, 20)
        If None, will infer size from shape and ppd.
        If int, it will be used as height.
        If either height=None or width=None, the other will be inferred.

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "mask")
        and additional keys containing stimulus parameters

    References
    -----------
    Domijan, D. (2015). A neurocomputational account of the role of contour
        facilitation in brightness perception. Frontiers in Human Neuroscience,
        9, 93. https://doi.org/10.3389/fnhum.2015.00093
    """

    # Note: Compared to original, targets are moved by one pixel
    shape = resolve_input(shape)
    visual_size = resolve_input(visual_size)
    c = get_conversion_2d(SHAPES["todorovic"], shape, visual_size, ppd)
    shape, visual_size, ppd = resolve(None, np.array(SHAPES["todorovic"]) * c, ppd)
    ppd = ppd[0]

    params = {
        "visual_size": visual_size[0],
        "ppd": ppd,
        "target_size": 41 * c,
        "covers_size": 31 * c,
        "covers_offset": 20 * c,
    }

    stim1 = illusions.todorovic.todorovic_rectangle(
        **params,
        intensity_background=0.0,
        intensity_target=0.5,
        intensity_covers=1.0,
    )
    stim2 = illusions.todorovic.todorovic_rectangle(
        **params,
        intensity_background=1.0,
        intensity_target=0.5,
        intensity_covers=0.0,
    )

    # Increase target index of right stimulus half
    mask2 = stim2["mask"] + 1
    mask2[mask2 == 1] = 0

    # Stacking
    img = np.hstack([stim1["img"], stim2["img"]])
    mask = np.hstack([stim1["mask"], mask2])

    params.update(
        original_shape=SHAPES["todorovic"],
        original_ppd=PPD,
        original_visual_size=np.array(SHAPES["todorovic"]) / PPD,
        original_range=(1, 9),
        intensity_range=(v1, v3),
        visual_size=np.array(img.shape) / ppd,
        shape=img.shape,
    )
    return {"img": img, "mask": mask, **params}


def checkerboard_contrast_contrast(
    shape=SHAPES["checkerboard_contrast_contrast"],
    ppd=PPD,
    visual_size=VSIZES["checkerboard_contrast_contrast"],
    pad=PAD,
):
    """Checkerboard contrast-contrast effect, Domijan (2015) Fig 9B

    Parameters
    ----------
    shape : None, int or (int/None, int/None)
        Stimulus shape in deg, (height, width), default: (80, 160)
        If None, will infer shape from ppd and visual size.
        If int, it will be used as height.
        If either height=None or width=None, the other will be inferred.
    ppd : int
        Resolution of stimulus in pixels per degree. (default: 10)
    visual_size : None, int or (int/None, int/None)
        Stimulus size in degree, (height, width), default: (8, 16)
        If None, will infer size from shape and ppd.
        If int, it will be used as height.
        If either height=None or width=None, the other will be inferred.
    pad : bool
        If True, include original padding (default: False)

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "mask")
        and additional keys containing stimulus parameters

    References
    -----------
    Domijan, D. (2015). A neurocomputational account of the role of contour
        facilitation in brightness perception. Frontiers in Human Neuroscience,
        9, 93. https://doi.org/10.3389/fnhum.2015.00093
    """

    shape = resolve_input(shape)
    visual_size = resolve_input(visual_size)
    conversion_fac = get_conversion_2d(
        SHAPES["checkerboard_contrast_contrast"], shape, visual_size, ppd
    )
    shape, visual_size, ppd = resolve(
        None, np.array(SHAPES["checkerboard_contrast_contrast"]) * conversion_fac, ppd
    )
    ppd = ppd[0]

    params = {
        "ppd": ppd,
        "check_visual_size": 10 * conversion_fac,
        "target_shape": (4, 4),
        "tau": 0.5,
        "alpha": 0.5,
        "intensity_low": v1,
        "intensity_high": v3,
    }

    stim1 = illusions.checkerboards.contrast_contrast(
        **params,
        board_shape=(8, 8),
    )

    stim2 = illusions.checkerboards.contrast_contrast(
        **params,
        board_shape=(4, 4),
    )

    # Increase target index of right stimulus half
    img2, mask2 = stim2["img"], stim2["mask"] + 1
    mask2[mask2 == 1] = 0

    # Padding
    padding = 20.0 * conversion_fac
    if pad:
        padding1 = np.array((9.0, 11.0)) * conversion_fac
        padding = np.array(padding1) + padding
        stim1["img"] = pad_by_visual_size(stim1["img"], padding1, ppd=ppd, pad_value=v2)
        stim1["mask"] = pad_by_visual_size(stim1["mask"], padding1, ppd=ppd, pad_value=0)
        params["padding"] = padding1
    img2 = pad_by_visual_size(img2, padding, ppd=ppd, pad_value=v2)
    mask2 = pad_by_visual_size(mask2, padding, ppd=ppd, pad_value=0)

    # Stacking
    img = np.hstack([stim1["img"], img2])
    mask = np.hstack([stim1["mask"], mask2])

    original_shape_np = np.array(SHAPES["checkerboard_contrast_contrast"])
    original_visual_np = np.array(original_shape_np) / PPD
    original_shape = original_shape_np + 20
    original_visual_size = original_shape / PPD
    params.update(
        original_shape=original_shape,
        original_ppd=PPD,
        original_visual_size=original_visual_size,
        original_shape_no_padding=original_shape_np,
        original_visual_size_no_padding=original_visual_np,
        original_range=(1, 9),
        intensity_range=(v1, v3),
        visual_size=np.array(img.shape) / ppd,
        shape=img.shape,
        board_shape_left=(8, 8),
        board_shape_right=(4, 4),
    )

    return {"img": img, "mask": mask, **params}


def checkerboard(
    shape=SHAPES["checkerboard"], ppd=PPD, visual_size=VSIZES["checkerboard"], pad=PAD
):
    """Classic checkerboard contrast with single-check targets, Domijan (2015) Fig 10A

    Parameters
    ----------
    shape : None, int or (int/None, int/None)
        Stimulus shape in deg, (height, width), default: (80, 80)
        If None, will infer shape from ppd and visual size.
        If int, it will be used as height.
        If either height=None or width=None, the other will be inferred.
    ppd : int
        Resolution of stimulus in pixels per degree. (default: 10)
    visual_size : None, int or (int/None, int/None)
        Stimulus size in degree, (height, width), default: (8, 8)
        If None, will infer size from shape and ppd.
        If int, it will be used as height.
        If either height=None or width=None, the other will be inferred.
    pad : bool
        If True, include original padding (default: False)

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "mask")
        and additional keys containing stimulus parameters

    References
    -----------
    Domijan, D. (2015). A neurocomputational account of the role of contour
        facilitation in brightness perception. Frontiers in Human Neuroscience,
        9, 93. https://doi.org/10.3389/fnhum.2015.00093
    """

    shape = resolve_input(shape)
    visual_size = resolve_input(visual_size)
    conversion_fac = get_conversion_2d(SHAPES["checkerboard"], shape, visual_size, ppd)
    shape, visual_size, ppd = resolve(None, np.array(SHAPES["checkerboard"]) * conversion_fac, ppd)
    ppd = ppd[0]

    params = {
        "ppd": ppd,
        "board_shape": (8, 8),
        "check_visual_size": (10 * conversion_fac, 10 * conversion_fac),
        "targets": [(3, 2), (5, 5)],
        "extend_targets": False,
        "intensity_low": 0,
        "intensity_high": 1,
        "intensity_target": 0.5,
    }
    stim = illusions.checkerboards.checkerboard(**params)

    if pad:
        padding = np.array((9.0, 11.0)) * conversion_fac
        stim["img"] = pad_by_visual_size(stim["img"], padding, ppd=ppd, pad_value=v2)
        stim["mask"] = pad_by_visual_size(stim["mask"], padding, ppd=ppd, pad_value=0)
        params["padding"] = padding

    original_shape_np = np.array(SHAPES["checkerboard"])
    original_visual_np = np.array(original_shape_np) / PPD
    original_shape = original_shape_np + 20
    original_visual_size = original_shape / PPD
    params.update(
        original_shape=original_shape,
        original_ppd=PPD,
        original_visual_size=original_visual_size,
        original_shape_no_padding=original_shape_np,
        original_visual_size_no_padding=original_visual_np,
        original_range=(1, 9),
        intensity_range=(v1, v3),
        visual_size=np.array(stim["img"].shape) / ppd,
        shape=stim["img"].shape,
    )

    return {**stim, **params}


def checkerboard_extended(
    shape=SHAPES["checkerboard_extended"],
    ppd=PPD,
    visual_size=VSIZES["checkerboard_extended"],
    pad=PAD,
):
    """Checkerboard contrast with cross-like targets, Domijan (2015) Fig 10B

    Parameters
    ----------
    shape : None, int or (int/None, int/None)
        Stimulus shape in deg, (height, width), default: (80, 80)
        If None, will infer shape from ppd and visual size.
        If int, it will be used as height.
        If either height=None or width=None, the other will be inferred.
    ppd : int
        Resolution of stimulus in pixels per degree. (default: 10)
    visual_size : None, int or (int/None, int/None)
        Stimulus size in degree, (height, width), default: (8, 8)
        If None, will infer size from shape and ppd.
        If int, it will be used as height.
        If either height=None or width=None, the other will be inferred.
    pad : bool
        If True, include original padding (default: False)

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "mask")
        and additional keys containing stimulus parameters

    References
    -----------
    Domijan, D. (2015). A neurocomputational account of the role of contour
        facilitation in brightness perception. Frontiers in Human Neuroscience,
        9, 93. https://doi.org/10.3389/fnhum.2015.00093
    """

    shape = resolve_input(shape)
    visual_size = resolve_input(visual_size)
    conversion_fac = get_conversion_2d(SHAPES["checkerboard_extended"], shape, visual_size, ppd)
    shape, visual_size, ppd = resolve(
        None, np.array(SHAPES["checkerboard_extended"]) * conversion_fac, ppd
    )
    ppd = ppd[0]

    params = {
        "ppd": ppd,
        "board_shape": (8, 8),
        "check_visual_size": (10 * conversion_fac, 10 * conversion_fac),
        "targets": [(3, 2), (5, 5)],
        "extend_targets": True,
        "intensity_low": 0,
        "intensity_high": 1,
        "intensity_target": 0.5,
    }
    stim = illusions.checkerboards.checkerboard(**params)

    if pad:
        padding = np.array((9.0, 11.0)) * conversion_fac
        stim["img"] = pad_by_visual_size(stim["img"], padding, ppd=ppd, pad_value=v2)
        stim["mask"] = pad_by_visual_size(stim["mask"], padding, ppd=ppd, pad_value=0)
        params["padding"] = padding

    original_shape_np = np.array(SHAPES["checkerboard_extended"])
    original_visual_np = np.array(original_shape_np) / PPD
    original_shape = original_shape_np + 20
    original_visual_size = original_shape / PPD
    params.update(
        original_shape=original_shape,
        original_ppd=PPD,
        original_visual_size=original_visual_size,
        original_shape_no_padding=original_shape_np,
        original_visual_size_no_padding=original_visual_np,
        original_range=(1, 9),
        intensity_range=(v1, v3),
        visual_size=np.array(stim["img"].shape) / ppd,
        shape=stim["img"].shape,
    )

    return {**stim, **params}


def white_yazdanbakhsh(
    shape=SHAPES["white_yazdanbakhsh"], ppd=PPD, visual_size=VSIZES["white_yazdanbakhsh"], pad=PAD
):
    """Yazdanbakhsh variation of White stimulus, Domijan (2015) Fig 11A

    Parameters
    ----------
    shape : None, int or (int/None, int/None)
        Stimulus shape in deg, (height, width), default: (80, 80)
        If None, will infer shape from ppd and visual size.
        If int, it will be used as height.
        If either height=None or width=None, the other will be inferred.
    ppd : int
        Resolution of stimulus in pixels per degree. (default: 10)
    visual_size : None, int or (int/None, int/None)
        Stimulus size in degree, (height, width), default: (8, 8)
        If None, will infer size from shape and ppd.
        If int, it will be used as height.
        If either height=None or width=None, the other will be inferred.
    pad : bool
        If True, include original padding (default: False)

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "mask")
        and additional keys containing stimulus parameters

    References
    -----------
    Domijan, D. (2015). A neurocomputational account of the role of contour
        facilitation in brightness perception. Frontiers in Human Neuroscience,
        9, 93. https://doi.org/10.3389/fnhum.2015.00093
    """

    shape = resolve_input(shape)
    visual_size = resolve_input(visual_size)
    c = get_conversion_2d(SHAPES["white_yazdanbakhsh"], shape, visual_size, ppd)
    shape, visual_size, ppd = resolve(None, np.array(SHAPES["white_yazdanbakhsh"]) * c, ppd)
    ppd = ppd[0]

    params = {
        "visual_size": visual_size,
        "ppd": ppd,
        "grating_frequency": 4.0 / visual_size[1],
        "target_indices_top": (2,),
        "target_indices_bottom": (5,),
        "target_center_offset": 0.0,
        "target_size": visual_size[0] / 4.0,
        "gap_size": visual_size[0] / 10.0,
        "period": "full",
    }

    stim = illusions.whites.white_yazdanbakhsh(
        **params,
        intensity_bars=(v1, v3),
        intensity_target=v2,
        intensity_stripes=(v3, v1),
    )

    if pad:
        padding = np.array((9.0, 11.0)) * c
        stim["img"] = pad_by_visual_size(stim["img"], padding, ppd=ppd, pad_value=v2)
        stim["mask"] = pad_by_visual_size(stim["mask"], padding, ppd=ppd, pad_value=0)
        params["padding"] = padding

    original_shape_np = np.array(SHAPES["white_yazdanbakhsh"])
    original_visual_np = np.array(original_shape_np) / PPD
    original_shape = original_shape_np + 20
    original_visual_size = original_shape / PPD
    params.update(
        original_shape=original_shape,
        original_ppd=PPD,
        original_visual_size=original_visual_size,
        original_shape_no_padding=original_shape_np,
        original_visual_size_no_padding=original_visual_np,
        original_range=(1, 9),
        intensity_range=(v1, v3),
        visual_size=np.array(stim["img"].shape) / ppd,
        shape=stim["img"].shape,
    )
    return {**stim, **params}


def white_anderson(
    shape=SHAPES["white_anderson"], ppd=PPD, visual_size=VSIZES["white_anderson"], pad=PAD
):
    """Anderson variation of White stimulus, Domijan (2015) Fig 11B

    Parameters
    ----------
    shape : None, int or (int/None, int/None)
        Stimulus shape in deg, (height, width), default: (100, 100)
        If None, will infer shape from ppd and visual size.
        If int, it will be used as height.
        If either height=None or width=None, the other will be inferred.
    ppd : int
        Resolution of stimulus in pixels per degree. (default: 10)
    visual_size : None, int or (int/None, int/None)
        Stimulus size in degree, (height, width), default: (10, 10)
        If None, will infer size from shape and ppd.
        If int, it will be used as height.
        If either height=None or width=None, the other will be inferred.
    pad : bool
        If True, include original padding (default: False)

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "mask")
        and additional keys containing stimulus parameters

    References
    -----------
    Domijan, D. (2015). A neurocomputational account of the role of contour
        facilitation in brightness perception. Frontiers in Human Neuroscience,
        9, 93. https://doi.org/10.3389/fnhum.2015.00093
    """

    shape = resolve_input(shape)
    visual_size = resolve_input(visual_size)
    c = get_conversion_2d(SHAPES["white_anderson"], shape, visual_size, ppd)
    shape, visual_size, ppd = resolve(None, np.array(SHAPES["white_anderson"]) * c, ppd)
    ppd = ppd[0]

    params = {
        "visual_size": visual_size,
        "ppd": ppd,
        "grating_frequency": 5.0 / visual_size[1],
        "target_indices_top": (2,),
        "target_indices_bottom": (7,),
        "target_center_offset": visual_size[0] / 10.0,
        "target_size": visual_size[0] / 5.0,
        "stripe_center_offset": visual_size[0] / 5.0,
        "stripe_size": visual_size[0] / 5.0,
        "period": "full",
    }

    stim = illusions.whites.white_anderson(
        **params,
        intensity_bars=(v3, v1),
        intensity_target=v2,
        intensity_stripes=(v1, v3),
    )

    if pad:
        padding = np.array((9.0, 11.0)) * c
        stim["img"] = pad_by_visual_size(stim["img"], padding, ppd=ppd, pad_value=v2)
        stim["mask"] = pad_by_visual_size(stim["mask"], padding, ppd=ppd, pad_value=0)
        params["padding"] = padding

    original_shape_np = np.array(SHAPES["white_anderson"])
    original_visual_np = np.array(original_shape_np) / PPD
    original_shape = original_shape_np + 20
    original_visual_size = original_shape / PPD
    params.update(
        original_shape=original_shape,
        original_ppd=PPD,
        original_visual_size=original_visual_size,
        original_shape_no_padding=original_shape_np,
        original_visual_size_no_padding=original_visual_np,
        original_range=(1, 9),
        intensity_range=(v1, v3),
        visual_size=np.array(stim["img"].shape) / ppd,
        shape=stim["img"].shape,
    )
    return {**stim, **params}


def white_howe(shape=SHAPES["white_howe"], ppd=PPD, visual_size=VSIZES["white_howe"], pad=PAD):
    """Howe variation of White stimulus, Domijan (2015) Fig 11C

    Parameters
    ----------
    shape : None, int or (int/None, int/None)
        Stimulus shape in deg, (height, width), default: (100, 100)
        If None, will infer shape from ppd and visual size.
        If int, it will be used as height.
        If either height=None or width=None, the other will be inferred.
    ppd : int
        Resolution of stimulus in pixels per degree. (default: 10)
    visual_size : None, int or (int/None, int/None)
        Stimulus size in degree, (height, width), default: (10, 10)
        If None, will infer size from shape and ppd.
        If int, it will be used as height.
        If either height=None or width=None, the other will be inferred.
    pad : bool
        If True, include original padding (default: False)

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "mask")
        and additional keys containing stimulus parameters

    References
    -----------
    Domijan, D. (2015). A neurocomputational account of the role of contour
        facilitation in brightness perception. Frontiers in Human Neuroscience,
        9, 93. https://doi.org/10.3389/fnhum.2015.00093
    """

    shape = resolve_input(shape)
    visual_size = resolve_input(visual_size)
    c = get_conversion_2d(SHAPES["white_howe"], shape, visual_size, ppd)
    shape, visual_size, ppd = resolve(None, np.array(SHAPES["white_howe"]) * c, ppd)
    ppd = ppd[0]

    params = {
        "visual_size": visual_size,
        "ppd": ppd,
        "grating_frequency": 5.0 / visual_size[1],
        "target_indices_top": (2,),
        "target_indices_bottom": (7,),
        "target_center_offset": visual_size[0] / 5.0,
        "target_size": visual_size[0] / 5.0,
        "period": "full",
    }

    stim = illusions.whites.white_howe(
        **params,
        intensity_bars=(v3, v1),
        intensity_target=v2,
        intensity_stripes=(v1, v3),
    )

    if pad:
        padding = np.array((9.0, 11.0)) * c
        stim["img"] = pad_by_visual_size(stim["img"], padding, ppd=ppd, pad_value=v2)
        stim["mask"] = pad_by_visual_size(stim["mask"], padding, ppd=ppd, pad_value=0)
        params["padding"] = padding

    original_shape_np = np.array(SHAPES["white_howe"])
    original_visual_np = np.array(original_shape_np) / PPD
    original_shape = original_shape_np + 20
    original_visual_size = original_shape / PPD
    params.update(
        original_shape=original_shape,
        original_ppd=PPD,
        original_visual_size=original_visual_size,
        original_shape_no_padding=original_shape_np,
        original_visual_size_no_padding=original_visual_np,
        original_range=(1, 9),
        intensity_range=(v1, v3),
        visual_size=np.array(stim["img"].shape) / ppd,
        shape=stim["img"].shape,
    )
    return {**stim, **params}


if __name__ == "__main__":
    from stimuli.utils import plot_stimuli

    stims = gen_all(skip=True)
    plot_stimuli(stims, mask=False)
