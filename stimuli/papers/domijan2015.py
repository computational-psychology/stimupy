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
from stimuli.utils import pad_by_visual_size, pad_to_shape, resolution

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
    "dungeon": resolution.visual_size_from_shape_ppd(shape=SHAPES["dungeon"], ppd=PPD),
    "cube": resolution.visual_size_from_shape_ppd(shape=SHAPES["cube"], ppd=PPD),
    "grating": resolution.visual_size_from_shape_ppd(shape=SHAPES["grating"], ppd=PPD),
    "rings": resolution.visual_size_from_shape_ppd(shape=SHAPES["rings"], ppd=PPD),
    "bullseye": resolution.visual_size_from_shape_ppd(shape=SHAPES["bullseye"], ppd=PPD),
    "simultaneous_brightness_contrast": resolution.visual_size_from_shape_ppd(
        shape=SHAPES["simultaneous_brightness_contrast"], ppd=PPD
    ),
    "white": resolution.visual_size_from_shape_ppd(shape=SHAPES["white"], ppd=PPD),
    "benary": resolution.visual_size_from_shape_ppd(shape=SHAPES["benary"], ppd=PPD),
    "todorovic": resolution.visual_size_from_shape_ppd(shape=SHAPES["todorovic"], ppd=PPD),
    "checkerboard_contrast_contrast": resolution.visual_size_from_shape_ppd(
        shape=SHAPES["checkerboard_contrast_contrast"], ppd=PPD
    ),
    "checkerboard": resolution.visual_size_from_shape_ppd(shape=SHAPES["checkerboard"], ppd=PPD),
    "checkerboard_extended": resolution.visual_size_from_shape_ppd(
        shape=SHAPES["checkerboard_extended"], ppd=PPD
    ),
    "white_yazdanbakhsh": resolution.visual_size_from_shape_ppd(
        shape=SHAPES["white_yazdanbakhsh"], ppd=PPD
    ),
    "white_anderson": resolution.visual_size_from_shape_ppd(
        shape=SHAPES["white_anderson"], ppd=PPD
    ),
    "white_howe": resolution.visual_size_from_shape_ppd(shape=SHAPES["white_howe"], ppd=PPD),
}

v1, v2, v3 = 0.0, 0.5, 1.0


def gen_all(ppd=PPD, skip=False):
    stims = {}  # save the stimulus-dicts in a larger dict, with name as key
    for stim_name in __all__:
        print(f"Generating domijan2015.{stim_name}")

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


def resolve(shape, visual_size, ppd, original_visual_size):

    # Put in canonical form
    shape = resolution.validate_shape(shape)
    visual_size = resolution.validate_visual_size(visual_size)
    ppd = resolution.validate_ppd(ppd)

    # Try to resolve height; get resizing_factor from that
    try:
        _, visual_angle, ppd1 = resolution.resolve_1D(
            length=shape.height, visual_angle=visual_size.height, ppd=ppd.vertical
        )
        v1 = visual_angle / original_visual_size[0]
    except Exception:
        v1 = None
        ppd1 = None

    # Try to resolve width; get resizing_factor from that
    try:
        _, visual_angle, ppd2 = resolution.resolve_1D(
            length=shape.width, visual_angle=visual_size.width, ppd=ppd.horizontal
        )
        v2 = visual_angle / original_visual_size[1]
    except Exception:
        v2 = None
        ppd2 = None

    # Same resizing factor?
    visual_resize = [i for i in (v1, v2) if i is not None]
    visual_resize = np.unique(visual_resize)
    if len(visual_resize) != 1:
        # Different resizing factors -> not allowed
        raise ValueError(
            "Requested shape/visual_size is impossible given the stimulus defaults. "
            "Consider setting either the height or width to None"
        )
    else:
        # Same factor, resolve resolution using that
        visual_resize = visual_resize[0]
        ppd = np.unique([i for i in (ppd1, ppd2) if i is not None])
        shape, visual_size, ppd = resolution.resolve(
            shape, np.array(original_visual_size) * visual_resize, ppd
        )

    return shape, visual_size, ppd, visual_resize


def dungeon(shape=SHAPES["dungeon"], visual_size=VSIZES["dungeon"], ppd=PPD):
    """Dungeon illusion, Domijan (2015) Fig 6A

    Parameters
    ----------
    shape : Sequence[Number, Number], Number, or None
        shape [height, width] in pixels, default: (110, 220)
    visual_size : Sequence[Number, Number], Number, or None
        visual size [height, width] in degrees, default: 10
    ppd : Sequence[Number, Number], Number, or None
        pixels per degree [vertical, horizontal], default: (11, 22)

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img") and target mask (key: "mask")
        and additional keys containing stimulus parameters

    References
    -----------
    Domijan, D. (2015). A neurocomputational account of the role of contour
        facilitation in brightness perception. Frontiers in Human Neuroscience,
        9, 93. https://doi.org/10.3389/fnhum.2015.00093
    """

    # Resolve resolution
    shape, visual_size, ppd, visual_resize = resolve(shape, visual_size, ppd, VSIZES["dungeon"])
    ppd = ppd[0]

    # Define parameters for each side
    params = {
        "ppd": ppd,
        "n_cells": 5,
        "target_radius": 1,
        "cell_size": 1.0 * visual_resize,
    }

    # Generate each side
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
    stim2["mask"] *= 2

    # Pad
    padding = np.array((0.9, 1.1)) * visual_resize
    stim1["img"] = pad_by_visual_size(stim1["img"], padding, ppd, v1)
    stim1["mask"] = pad_by_visual_size(stim1["mask"], padding, ppd, 0)
    stim2["img"] = pad_by_visual_size(stim2["img"], padding, ppd, v3)
    stim2["mask"] = pad_by_visual_size(stim2["mask"], padding, ppd, 0)

    # Stacking
    img = np.hstack([stim1["img"], stim2["img"]])
    mask = np.hstack([stim1["mask"], stim2["mask"]]).astype(int)

    params.update(
        original_shape=SHAPES["dungeon"],
        original_ppd=PPD,
        original_visual_size=VSIZES["dungeon"],
        original_range=(1, 9),
        intensity_range=(v1, v3),
        visual_size=resolution.visual_size_from_shape_ppd(img.shape, ppd),
        shape=img.shape,
    )
    return {"img": img, "mask": mask, **params}


def cube(shape=SHAPES["cube"], visual_size=VSIZES["cube"], ppd=PPD):
    """Cube illusion, Domijan (2015) Fig 6B

    Parameters
    ----------
    shape : Sequence[Number, Number], Number, or None
        shape [height, width] in pixels, default: (100, 200)
    visual_size : Sequence[Number, Number], Number, or None
        visual size [height, width] in degrees, default: 10
    ppd : Sequence[Number, Number], Number, or None
        pixels per degree [vertical, horizontal], default: (10, 20)

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img") and target mask (key: "mask")
        and additional keys containing stimulus parameters

    References
    -----------
    Domijan, D. (2015). A neurocomputational account of the role of contour
        facilitation in brightness perception. Frontiers in Human Neuroscience,
        9, 93. https://doi.org/10.3389/fnhum.2015.00093
    """

    # Resolve resolution
    shape, visual_size, ppd, visual_resize = resolve(shape, visual_size, ppd, VSIZES["cube"])
    ppd = ppd[0]

    params = {
        "ppd": ppd,
        "n_cells": 4,
        "target_length": 2,
        "cell_long": 1.5 * visual_resize,
        "cell_short": 1.1 * visual_resize,
        "corner_cell_width": 1.8 * visual_resize,
        "corner_cell_height": 1.8 * visual_resize,
        "cell_spacing": 0.5 * visual_resize,
        "occlusion_overlap": np.array((0.7,) * 4) * visual_resize,
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
    padding = np.array((0.9, 1.0)) * visual_resize
    img1 = pad_by_visual_size(stim1["img"], padding, ppd, v1)
    mask1 = pad_by_visual_size(stim1["mask"], padding, ppd, 0)
    img2 = pad_by_visual_size(stim2["img"], padding, ppd, v3)
    mask2 = pad_by_visual_size(stim2["mask"], padding, ppd, 0)

    # Increase target index of right stimulus half
    mask2 *= 2

    # Stacking
    img = np.hstack([img1, img2])
    mask = np.hstack([mask1, mask2]).astype(int)

    params.update(
        original_shape=SHAPES["cube"],
        original_ppd=PPD,
        original_visual_size=VSIZES["cube"],
        original_range=(1, 9),
        intensity_range=(v1, v3),
        visual_size=resolution.visual_size_from_shape_ppd(img.shape, ppd),
        shape=img.shape,
    )
    return {"img": img, "mask": mask, **params}


def grating(shape=SHAPES["grating"], visual_size=VSIZES["grating"], ppd=PPD):
    """Grating illusion, Domijan (2015) Fig 6C

    Parameters
    ----------
    shape : Sequence[Number, Number], Number, or None
        shape [height, width] in pixels, default: (100, 220)
    visual_size : Sequence[Number, Number], Number, or None
        visual size [height, width] in degrees, default: 10
    ppd : Sequence[Number, Number], Number, or None
        pixels per degree [vertical, horizontal], default: (10, 22)

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img") and target mask (key: "mask")
        and additional keys containing stimulus parameters

    References
    -----------
    Domijan, D. (2015). A neurocomputational account of the role of contour
        facilitation in brightness perception. Frontiers in Human Neuroscience,
        9, 93. https://doi.org/10.3389/fnhum.2015.00093
    """

    # Resolve resolution
    shape, visual_size, ppd, visual_resize = resolve(shape, visual_size, ppd, VSIZES["grating"])
    ppd = ppd[0]

    params = {
        "ppd": ppd,
        "n_bars": 9,
        "target_indices": (4,),
        "bar_shape": (8.1 * visual_resize, 1.0 * visual_resize),
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
    padding = np.array(((0.9, 1.0), (0.9, 1.1))) * visual_resize
    img1 = pad_by_visual_size(stim1["img"], padding, ppd, v1)
    mask1 = pad_by_visual_size(stim1["mask"], padding, ppd, 0)
    img2 = pad_by_visual_size(stim2["img"], padding, ppd, v3)
    mask2 = pad_by_visual_size(stim2["mask"], padding, ppd, 0)

    # Increase target index of right stimulus half
    mask2 *= 2

    # Stacking
    img = np.hstack([img1, img2])
    mask = np.hstack([mask1, mask2]).astype(int)

    params.update(
        original_shape=SHAPES["grating"],
        original_ppd=PPD,
        original_visual_size=VSIZES["grating"],
        original_range=(1, 9),
        intensity_range=(v1, v3),
        visual_size=resolution.visual_size_from_shape_ppd(img.shape, ppd),
        shape=img.shape,
    )
    return {"img": img, "mask": mask, **params}


def rings(shape=SHAPES["rings"], visual_size=VSIZES["rings"], ppd=PPD):
    """Ring patterns, Domijan (2015) Fig 7A

    Parameters
    ----------
    shape : Sequence[Number, Number], Number, or None
        shape [height, width] in pixels, default: (100, 200)
    visual_size : Sequence[Number, Number], Number, or None
        visual size [height, width] in degrees, default: 10
    ppd : Sequence[Number, Number], Number, or None
        pixels per degree [vertical, horizontal], default: (10, 20)

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img") and target mask (key: "mask")
        and additional keys containing stimulus parameters

    References
    -----------
    Domijan, D. (2015). A neurocomputational account of the role of contour
        facilitation in brightness perception. Frontiers in Human Neuroscience,
        9, 93. https://doi.org/10.3389/fnhum.2015.00093
    """

    # Resolve resolution
    shape, visual_size, ppd, visual_resize = resolve(shape, visual_size, ppd, VSIZES["rings"])
    ppd = ppd[0]

    params = {
        "ppd": ppd,
        "n_rings": 8,
        "ring_width": 0.5 * visual_resize,
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
    stim1["img"] = pad_to_shape(stim1["img"], shape=np.array(shape) / (1, 2), pad_value=v1)
    stim1["mask"] = pad_to_shape(stim1["mask"], shape=np.array(shape) / (1, 2), pad_value=0)
    stim2["img"] = pad_to_shape(stim2["img"], shape=np.array(shape) / (1, 2), pad_value=v1)
    stim2["mask"] = pad_to_shape(stim2["mask"], shape=np.array(shape) / (1, 2), pad_value=0)

    # Increase target index of right stimulus half
    stim2["mask"] *= 2

    # Stacking
    img = np.hstack([stim1["img"], stim2["img"]])
    mask = np.hstack([stim1["mask"], stim2["mask"]]).astype(int)

    params.update(
        original_shape=SHAPES["rings"],
        original_ppd=PPD,
        original_visual_size=VSIZES["rings"],
        original_range=(1, 9),
        intensity_range=(v1, v3),
        visual_size=resolution.visual_size_from_shape_ppd(img.shape, ppd),
        shape=img.shape,
        target_idx_left=4,
        target_idx_right=3,
    )
    return {"img": img, "mask": mask, **params}


def bullseye(shape=SHAPES["bullseye"], visual_size=VSIZES["bullseye"], ppd=PPD):
    """Bullseye illusion, Domijan (2015) Fig 7B

    Parameters
    ----------
    shape : Sequence[Number, Number], Number, or None
        shape [height, width] in pixels, default: (100, 200)
    visual_size : Sequence[Number, Number], Number, or None
        visual size [height, width] in degrees, default: 10
    ppd : Sequence[Number, Number], Number, or None
        pixels per degree [vertical, horizontal], default: (10, 20)

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img") and target mask (key: "mask")
        and additional keys containing stimulus parameters

    References
    -----------
    Domijan, D. (2015). A neurocomputational account of the role of contour
        facilitation in brightness perception. Frontiers in Human Neuroscience,
        9, 93. https://doi.org/10.3389/fnhum.2015.00093
    """

    # Resolve resolution
    shape, visual_size, ppd, visual_resize = resolve(shape, visual_size, ppd, VSIZES["bullseye"])
    ppd = ppd[0]

    params = {
        "ppd": ppd,
        "n_rings": 8,
        "ring_width": 0.5 * visual_resize,
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
    stim1["img"] = pad_to_shape(stim1["img"], shape=np.array(shape) / (1, 2), pad_value=v1)
    stim1["mask"] = pad_to_shape(stim1["mask"], shape=np.array(shape) / (1, 2), pad_value=0)
    stim2["img"] = pad_to_shape(stim2["img"], shape=np.array(shape) / (1, 2), pad_value=v1)
    stim2["mask"] = pad_to_shape(stim2["mask"], shape=np.array(shape) / (1, 2), pad_value=0)

    # Increase target index of right stimulus half
    stim2["mask"] *= 2

    # Stacking
    img = np.hstack([stim1["img"], stim2["img"]])
    mask = np.hstack([stim1["mask"], stim2["mask"]]).astype(int)

    params.update(
        original_shape=SHAPES["bullseye"],
        original_ppd=PPD,
        original_visual_size=VSIZES["bullseye"],
        original_range=(1, 9),
        intensity_range=(v1, v3),
        visual_size=resolution.visual_size_from_shape_ppd(img.shape, ppd),
        shape=img.shape,
    )
    return {"img": img, "mask": mask, **params}


def simultaneous_brightness_contrast(
    shape=SHAPES["simultaneous_brightness_contrast"],
    visual_size=VSIZES["simultaneous_brightness_contrast"],
    ppd=PPD,
):
    """Simultaneous brightness contrast, Domijan (2015) Fig 7C

    Parameters
    ----------
    shape : Sequence[Number, Number], Number, or None
        shape [height, width] in pixels, default: (100, 200)
    visual_size : Sequence[Number, Number], Number, or None
        visual size [height, width] in degrees, default: 10
    ppd : Sequence[Number, Number], Number, or None
        pixels per degree [vertical, horizontal], default: (10, 20)

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img") and target mask (key: "mask")
        and additional keys containing stimulus parameters

    References
    -----------
    Domijan, D. (2015). A neurocomputational account of the role of contour
        facilitation in brightness perception. Frontiers in Human Neuroscience,
        9, 93. https://doi.org/10.3389/fnhum.2015.00093
    """

    # Resolve resolution
    shape, visual_size, ppd, visual_resize = resolve(
        shape, visual_size, ppd, VSIZES["simultaneous_brightness_contrast"]
    )
    ppd = ppd[0]

    params = {
        "visual_size": visual_size[0],
        "ppd": ppd,
        "target_size": (2.1 * visual_resize, 2.1 * visual_resize),
        "target_position": (3.9 * visual_resize, 3.9 * visual_resize),
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
    stim2["mask"] *= 2

    # Stacking
    img = np.hstack([stim1["img"], stim2["img"]])
    mask = np.hstack([stim1["mask"], stim2["mask"]]).astype(int)

    params.update(
        original_shape=SHAPES["simultaneous_brightness_contrast"],
        original_ppd=PPD,
        original_visual_size=VSIZES["simultaneous_brightness_contrast"],
        original_range=(1, 9),
        intensity_range=(v1, v3),
        visual_size=resolution.visual_size_from_shape_ppd(img.shape, ppd),
        shape=img.shape,
    )
    return {"img": img, "mask": mask, **params}


def white(shape=SHAPES["white"], visual_size=VSIZES["white"], ppd=PPD, pad=PAD):
    """White stimulus, Domijan (2015) Fig 8A

    Parameters
    ----------
    shape : Sequence[Number, Number], Number, or None
        shape [height, width] in pixels, default: (80, 80)
    visual_size : Sequence[Number, Number], Number, or None
        visual size [height, width] in degrees, default: 10
    ppd : Sequence[Number, Number], Number, or None
        pixels per degree [vertical, horizontal], default: (8, 8)
    pad : bool
        If True, include original padding (default: False)

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img") and target mask (key: "mask")
        and additional keys containing stimulus parameters

    References
    -----------
    Domijan, D. (2015). A neurocomputational account of the role of contour
        facilitation in brightness perception. Frontiers in Human Neuroscience,
        9, 93. https://doi.org/10.3389/fnhum.2015.00093
    """

    # Resolve resolution
    shape, visual_size, ppd, visual_resize = resolve(shape, visual_size, ppd, VSIZES["white"])
    ppd = ppd[0]

    params = {
        "visual_size": visual_size,
        "ppd": ppd,
        "grating_frequency": 4.0 / visual_size[1],
        "target_indices": (2, 5),
        "target_size": 2.1 * visual_resize,
        "period": "full",
    }

    stim = illusions.whites.white(
        **params,
        intensity_bars=(v1, v3),
        intensity_target=v2,
    )

    if pad:
        padding = np.array((0.9, 1.1)) * visual_resize
        stim["img"] = pad_by_visual_size(stim["img"], padding, ppd, pad_value=v2)
        stim["mask"] = pad_by_visual_size(stim["mask"], padding, ppd, pad_value=0).astype(int)
        params["padding"] = padding

    original_shape_np = SHAPES["white"]
    original_shape = np.array(original_shape_np) + 20
    original_visual_size = resolution.visual_size_from_shape_ppd(original_shape, PPD)
    params.update(
        original_shape=original_shape,
        original_ppd=PPD,
        original_visual_size=original_visual_size,
        original_shape_no_padding=original_shape_np,
        original_visual_size_no_padding=VSIZES["white"],
        original_range=(1, 9),
        intensity_range=(v1, v3),
        visual_size=resolution.visual_size_from_shape_ppd(stim["img"].shape, ppd),
        shape=stim["img"].shape,
    )
    return {**stim, **params}


def benary(shape=SHAPES["benary"], visual_size=VSIZES["benary"], ppd=PPD):
    """Benarys cross, Domijan (2015) Fig 8B

    Parameters
    ----------
    shape : Sequence[Number, Number], Number, or None
        shape [height, width] in pixels, default: (100, 100)
    visual_size : Sequence[Number, Number], Number, or None
        visual size [height, width] in degrees, default: 10
    ppd : Sequence[Number, Number], Number, or None
        pixels per degree [vertical, horizontal], default: (10, 10)

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img") and target mask (key: "mask")
        and additional keys containing stimulus parameters

    References
    -----------
    Domijan, D. (2015). A neurocomputational account of the role of contour
        facilitation in brightness perception. Frontiers in Human Neuroscience,
        9, 93. https://doi.org/10.3389/fnhum.2015.00093
    """

    # Resolve resolution
    shape, visual_size, ppd, visual_resize = resolve(shape, visual_size, ppd, VSIZES["benary"])
    ppd = ppd[0]

    params = {
        "visual_size": 8.1 * visual_resize,
        "ppd": ppd,
        "cross_thickness": 2.1 * visual_resize,
        "target_size": 1.1 * visual_resize,
    }

    stim = illusions.benary_cross.benarys_cross_rectangles(
        **params,
        intensity_background=v3,
        intensity_cross=v1,
        intensity_target=v2,
    )

    # Padding
    padding = np.array((0.9, 1.0)) * visual_resize
    stim["img"] = pad_by_visual_size(stim["img"], padding, ppd, pad_value=1.0)
    stim["mask"] = pad_by_visual_size(stim["mask"], padding, ppd, pad_value=0).astype(int)

    params.update(
        original_shape=SHAPES["benary"],
        original_ppd=PPD,
        original_visual_size=VSIZES["benary"],
        original_range=(1, 9),
        intensity_range=(v1, v3),
        visual_size=resolution.visual_size_from_shape_ppd(stim["img"].shape, ppd),
        shape=stim["img"].shape,
    )
    return {**stim, **params}


def todorovic(shape=SHAPES["todorovic"], visual_size=VSIZES["todorovic"], ppd=PPD):
    """Todorovic stimulus, Domijan (2015) Fig 9A

    Parameters
    ----------
    shape : Sequence[Number, Number], Number, or None
        shape [height, width] in pixels, default: (100, 200)
    visual_size : Sequence[Number, Number], Number, or None
        visual size [height, width] in degrees, default: 10
    ppd : Sequence[Number, Number], Number, or None
        pixels per degree [vertical, horizontal], default: (10, 20)

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img") and target mask (key: "mask")
        and additional keys containing stimulus parameters

    References
    -----------
    Domijan, D. (2015). A neurocomputational account of the role of contour
        facilitation in brightness perception. Frontiers in Human Neuroscience,
        9, 93. https://doi.org/10.3389/fnhum.2015.00093
    """

    # Note: Compared to original, targets are moved by one pixel
    # Resolve resolution
    shape, visual_size, ppd, visual_resize = resolve(shape, visual_size, ppd, VSIZES["todorovic"])
    ppd = ppd[0]

    params = {
        "visual_size": visual_size[0],
        "ppd": ppd,
        "target_size": 4.1 * visual_resize,
        "covers_size": 3.1 * visual_resize,
        "covers_offset": 2.0 * visual_resize,
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
    stim2["mask"] *= 2

    # Stacking
    img = np.hstack([stim1["img"], stim2["img"]])
    mask = np.hstack([stim1["mask"], stim2["mask"]]).astype(int)

    params.update(
        original_shape=SHAPES["todorovic"],
        original_ppd=PPD,
        original_visual_size=VSIZES["todorovic"],
        original_range=(1, 9),
        intensity_range=(v1, v3),
        visual_size=resolution.visual_size_from_shape_ppd(img.shape, ppd),
        shape=img.shape,
    )
    return {"img": img, "mask": mask, **params}


def checkerboard_contrast_contrast(
    shape=SHAPES["checkerboard_contrast_contrast"],
    visual_size=VSIZES["checkerboard_contrast_contrast"],
    ppd=PPD,
    pad=PAD,
):
    """Checkerboard contrast-contrast effect, Domijan (2015) Fig 9B

    Parameters
    ----------
    shape : Sequence[Number, Number], Number, or None
        shape [height, width] in pixels, default: (80, 160)
    visual_size : Sequence[Number, Number], Number, or None
        visual size [height, width] in degrees, default: 10
    ppd : Sequence[Number, Number], Number, or None
        pixels per degree [vertical, horizontal], default: (8, 16)
    pad : bool
        If True, include original padding (default: False)

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img") and target mask (key: "mask")
        and additional keys containing stimulus parameters

    References
    -----------
    Domijan, D. (2015). A neurocomputational account of the role of contour
        facilitation in brightness perception. Frontiers in Human Neuroscience,
        9, 93. https://doi.org/10.3389/fnhum.2015.00093
    """

    # Resolve resolution
    shape, visual_size, ppd, visual_resize = resolve(
        shape, visual_size, ppd, VSIZES["checkerboard_contrast_contrast"]
    )

    params = {
        "ppd": ppd,
        "check_visual_size": 1.0 * visual_resize,
        "target_shape": (4, 4),
        "tau": 0.5,
        "alpha": 0.5,
        "intensity_low": v1,
        "intensity_high": v3,
    }

    # Large checkerboard, embedded target region
    stim1 = illusions.checkerboards.contrast_contrast(
        **params,
        board_shape=(8, 8),
    )

    # Isolated target region (smaller checkerboard)
    stim2 = illusions.checkerboards.contrast_contrast(
        **params,
        board_shape=(4, 4),
    )

    # Put smaller checkerboard on background (equally large as large checkerboard)
    stim2["img"] = pad_to_shape(stim2["img"], stim1["img"].shape, pad_value=v2)
    stim2["mask"] = pad_to_shape(stim2["mask"], stim1["mask"].shape, pad_value=0)

    # Increase target index of right stimulus half
    stim2["mask"] *= 2

    # Overall padding
    if pad:
        padding = np.array((0.9, 1.1)) * visual_resize
        stim1["img"] = pad_by_visual_size(stim1["img"], padding, ppd=ppd, pad_value=v2)
        stim1["mask"] = pad_by_visual_size(stim1["mask"], padding, ppd=ppd, pad_value=0)
        stim2["img"] = pad_by_visual_size(stim2["img"], padding, ppd=ppd, pad_value=v2)
        stim2["mask"] = pad_by_visual_size(stim2["mask"], padding, ppd=ppd, pad_value=0)
        params["padding"] = padding

    # Stacking
    img = np.hstack([stim1["img"], stim2["img"]])
    mask = np.hstack([stim1["mask"], stim2["mask"]]).astype(int)

    # Output
    original_shape_np = np.array(SHAPES["checkerboard_contrast_contrast"])
    original_shape = original_shape_np + np.array((20, 40))
    original_visual_size = resolution.visual_size_from_shape_ppd(original_shape, PPD)
    params.update(
        original_shape=original_shape,
        original_ppd=PPD,
        original_visual_size=original_visual_size,
        original_shape_no_padding=original_shape_np,
        original_visual_size_no_padding=VSIZES["checkerboard_contrast_contrast"],
        original_range=(1, 9),
        intensity_range=(v1, v3),
        visual_size=resolution.visual_size_from_shape_ppd(img.shape, ppd),
        shape=img.shape,
        board_shape_left=(8, 8),
        board_shape_right=(4, 4),
    )

    return {"img": img, "mask": mask, **params}


def checkerboard(
    shape=SHAPES["checkerboard"], visual_size=VSIZES["checkerboard"], ppd=PPD, pad=PAD
):
    """Classic checkerboard contrast with single-check targets, Domijan (2015) Fig 10A

    Parameters
    ----------
    shape : Sequence[Number, Number], Number, or None
        shape [height, width] in pixels, default: (80, 80)
    visual_size : Sequence[Number, Number], Number, or None
        visual size [height, width] in degrees, default: 10
    ppd : Sequence[Number, Number], Number, or None
        pixels per degree [vertical, horizontal], default: (8, 8)
    pad : bool
        If True, include original padding (default: False)

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img") and target mask (key: "mask")
        and additional keys containing stimulus parameters

    References
    -----------
    Domijan, D. (2015). A neurocomputational account of the role of contour
        facilitation in brightness perception. Frontiers in Human Neuroscience,
        9, 93. https://doi.org/10.3389/fnhum.2015.00093
    """

    # Resolve resolution
    shape, visual_size, ppd, visual_resize = resolve(
        shape, visual_size, ppd, VSIZES["checkerboard"]
    )

    params = {
        "ppd": ppd,
        "board_shape": (8, 8),
        "check_visual_size": (1.0 * visual_resize, 1.0 * visual_resize),
        "targets": [(3, 2), (5, 5)],
        "extend_targets": False,
        "intensity_low": 0,
        "intensity_high": 1,
        "intensity_target": 0.5,
    }
    stim = illusions.checkerboards.checkerboard(**params)

    if pad:
        padding = np.array((0.9, 1.1)) * visual_resize
        stim["img"] = pad_by_visual_size(stim["img"], padding, ppd=ppd, pad_value=v2)
        stim["mask"] = pad_by_visual_size(stim["mask"], padding, ppd=ppd, pad_value=0).astype(int)
        params["padding"] = padding

    original_shape_np = SHAPES["checkerboard"]
    original_shape = np.array(original_shape_np) + 20
    original_visual_size = resolution.visual_size_from_shape_ppd(original_shape, PPD)
    params.update(
        original_shape=original_shape,
        original_ppd=PPD,
        original_visual_size=original_visual_size,
        original_shape_no_padding=original_shape_np,
        original_visual_size_no_padding=VSIZES["checkerboard"],
        original_range=(1, 9),
        intensity_range=(v1, v3),
        visual_size=resolution.visual_size_from_shape_ppd(stim["img"].shape, ppd),
        shape=stim["img"].shape,
    )

    return {**stim, **params}


def checkerboard_extended(
    shape=SHAPES["checkerboard_extended"],
    visual_size=VSIZES["checkerboard_extended"],
    ppd=PPD,
    pad=PAD,
):
    """Checkerboard contrast with cross-like targets, Domijan (2015) Fig 10B

    Parameters
    ----------
    shape : Sequence[Number, Number], Number, or None
        shape [height, width] in pixels, default: (80, 80)
    visual_size : Sequence[Number, Number], Number, or None
        visual size [height, width] in degrees, default: 10
    ppd : Sequence[Number, Number], Number, or None
        pixels per degree [vertical, horizontal], default: (8, 8)
    pad : bool
        If True, include original padding (default: False)

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img") and target mask (key: "mask")
        and additional keys containing stimulus parameters

    References
    -----------
    Domijan, D. (2015). A neurocomputational account of the role of contour
        facilitation in brightness perception. Frontiers in Human Neuroscience,
        9, 93. https://doi.org/10.3389/fnhum.2015.00093
    """

    # Resolve resolution
    shape, visual_size, ppd, visual_resize = resolve(
        shape, visual_size, ppd, VSIZES["checkerboard_extended"]
    )

    params = {
        "ppd": ppd,
        "board_shape": (8, 8),
        "check_visual_size": (1.0 * visual_resize, 1.0 * visual_resize),
        "targets": [(3, 2), (5, 5)],
        "extend_targets": True,
        "intensity_low": 0,
        "intensity_high": 1,
        "intensity_target": 0.5,
    }
    stim = illusions.checkerboards.checkerboard(**params)

    if pad:
        padding = np.array((0.9, 1.1)) * visual_resize
        stim["img"] = pad_by_visual_size(stim["img"], padding, ppd=ppd, pad_value=v2)
        stim["mask"] = pad_by_visual_size(stim["mask"], padding, ppd=ppd, pad_value=0).astype(int)
        params["padding"] = padding

    original_shape_np = SHAPES["checkerboard_extended"]
    original_shape = np.array(original_shape_np) + 20
    original_visual_size = resolution.visual_size_from_shape_ppd(original_shape, PPD)
    params.update(
        original_shape=original_shape,
        original_ppd=PPD,
        original_visual_size=original_visual_size,
        original_shape_no_padding=original_shape_np,
        original_visual_size_no_padding=VSIZES["checkerboard_extended"],
        original_range=(1, 9),
        intensity_range=(v1, v3),
        visual_size=resolution.visual_size_from_shape_ppd(stim["img"].shape, ppd),
        shape=stim["img"].shape,
    )

    return {**stim, **params}


def white_yazdanbakhsh(
    shape=SHAPES["white_yazdanbakhsh"], visual_size=VSIZES["white_yazdanbakhsh"], ppd=PPD, pad=PAD
):
    """Yazdanbakhsh variation of White stimulus, Domijan (2015) Fig 11A

    Parameters
    ----------
    shape : Sequence[Number, Number], Number, or None
        shape [height, width] in pixels, default: (80, 80)
    visual_size : Sequence[Number, Number], Number, or None
        visual size [height, width] in degrees, default: 10
    ppd : Sequence[Number, Number], Number, or None
        pixels per degree [vertical, horizontal], default: (8, 8)
    pad : bool
        If True, include original padding (default: False)

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img") and target mask (key: "mask")
        and additional keys containing stimulus parameters

    References
    -----------
    Domijan, D. (2015). A neurocomputational account of the role of contour
        facilitation in brightness perception. Frontiers in Human Neuroscience,
        9, 93. https://doi.org/10.3389/fnhum.2015.00093
    """

    # Resolve resolution
    shape, visual_size, ppd, visual_resize = resolve(
        shape, visual_size, ppd, VSIZES["white_yazdanbakhsh"]
    )
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
        padding = np.array((0.9, 1.1)) * visual_resize
        stim["img"] = pad_by_visual_size(stim["img"], padding, ppd=ppd, pad_value=v2)
        stim["mask"] = pad_by_visual_size(stim["mask"], padding, ppd=ppd, pad_value=0).astype(int)
        params["padding"] = padding

    original_shape_np = SHAPES["white_yazdanbakhsh"]
    original_shape = np.array(original_shape_np) + 20
    original_visual_size = resolution.visual_size_from_shape_ppd(original_shape, PPD)
    params.update(
        original_shape=original_shape,
        original_ppd=PPD,
        original_visual_size=original_visual_size,
        original_shape_no_padding=original_shape_np,
        original_visual_size_no_padding=VSIZES["white_yazdanbakhsh"],
        original_range=(1, 9),
        intensity_range=(v1, v3),
        visual_size=resolution.visual_size_from_shape_ppd(stim["img"].shape, ppd),
        shape=stim["img"].shape,
    )
    return {**stim, **params}


def white_anderson(
    shape=SHAPES["white_anderson"], visual_size=VSIZES["white_anderson"], ppd=PPD, pad=PAD
):
    """Anderson variation of White stimulus, Domijan (2015) Fig 11B

    Parameters
    ----------
    shape : Sequence[Number, Number], Number, or None
        shape [height, width] in pixels, default: (100, 100)
    visual_size : Sequence[Number, Number], Number, or None
        visual size [height, width] in degrees, default: 10
    ppd : Sequence[Number, Number], Number, or None
        pixels per degree [vertical, horizontal], default: (10, 10)
    pad : bool
        If True, include original padding (default: False)

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img") and target mask (key: "mask")
        and additional keys containing stimulus parameters

    References
    -----------
    Domijan, D. (2015). A neurocomputational account of the role of contour
        facilitation in brightness perception. Frontiers in Human Neuroscience,
        9, 93. https://doi.org/10.3389/fnhum.2015.00093
    """

    # Resolve resolution
    shape, visual_size, ppd, visual_resize = resolve(
        shape, visual_size, ppd, VSIZES["white_anderson"]
    )
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
        padding = np.array((0.9, 1.1)) * visual_resize
        stim["img"] = pad_by_visual_size(stim["img"], padding, ppd=ppd, pad_value=v2)
        stim["mask"] = pad_by_visual_size(stim["mask"], padding, ppd=ppd, pad_value=0).astype(int)
        params["padding"] = padding

    original_shape_np = SHAPES["white_anderson"]
    original_shape = np.array(original_shape_np) + 20
    original_visual_size = resolution.visual_size_from_shape_ppd(original_shape, PPD)
    params.update(
        original_shape=original_shape,
        original_ppd=PPD,
        original_visual_size=original_visual_size,
        original_shape_no_padding=original_shape_np,
        original_visual_size_no_padding=VSIZES["white_anderson"],
        original_range=(1, 9),
        intensity_range=(v1, v3),
        visual_size=resolution.visual_size_from_shape_ppd(stim["img"].shape, ppd),
        shape=stim["img"].shape,
    )
    return {**stim, **params}


def white_howe(shape=SHAPES["white_howe"], visual_size=VSIZES["white_howe"], ppd=PPD, pad=PAD):
    """Howe variation of White stimulus, Domijan (2015) Fig 11C

    Parameters
    ----------
    shape : Sequence[Number, Number], Number, or None
        shape [height, width] in pixels, default: (100, 100)
    visual_size : Sequence[Number, Number], Number, or None
        visual size [height, width] in degrees, default: 10
    ppd : Sequence[Number, Number], Number, or None
        pixels per degree [vertical, horizontal], default: (10, 10)
    pad : bool
        If True, include original padding (default: False)

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img") and target mask (key: "mask")
        and additional keys containing stimulus parameters

    References
    -----------
    Domijan, D. (2015). A neurocomputational account of the role of contour
        facilitation in brightness perception. Frontiers in Human Neuroscience,
        9, 93. https://doi.org/10.3389/fnhum.2015.00093
    """

    # Resolve resolution
    shape, visual_size, ppd, visual_resize = resolve(shape, visual_size, ppd, VSIZES["white_howe"])
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
        padding = np.array((0.9, 1.1)) * visual_resize
        stim["img"] = pad_by_visual_size(stim["img"], padding, ppd=ppd, pad_value=v2)
        stim["mask"] = pad_by_visual_size(stim["mask"], padding, ppd=ppd, pad_value=0).astype(int)
        params["padding"] = padding

    original_shape_np = SHAPES["white_howe"]
    original_shape = np.array(original_shape_np) + 20
    original_visual_size = resolution.visual_size_from_shape_ppd(original_shape, PPD)
    params.update(
        original_shape=original_shape,
        original_ppd=PPD,
        original_visual_size=original_visual_size,
        original_shape_no_padding=original_shape_np,
        original_visual_size_no_padding=VSIZES["white_howe"],
        original_range=(1, 9),
        intensity_range=(v1, v3),
        visual_size=resolution.visual_size_from_shape_ppd(stim["img"].shape, ppd),
        shape=stim["img"].shape,
    )
    return {**stim, **params}


if __name__ == "__main__":
    from stimuli.utils import plot_stimuli

    stims = gen_all(skip=True)
    plot_stimuli(stims, mask=False)
