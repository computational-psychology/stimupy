import itertools

import numpy as np

from stimupy.components.shapes import cross as cross_shape
from stimupy.components.shapes import rectangle as rectangle_shape
from stimupy.utils import pad_dict_to_shape, resolution, stack_dicts

__all__ = [
    "rectangle_generalized",
    "rectangle",
    "rectangle_two_sided",
    "cross_generalized",
    "cross",
    "cross_two_sided",
    "equal",
    "equal_two_sided",
]


def rectangle_generalized(
    visual_size=None,
    ppd=None,
    shape=None,
    target_size=None,
    target_position=None,
    covers_size=None,
    covers_x=None,
    covers_y=None,
    intensity_background=0.0,
    intensity_target=0.5,
    intensity_covers=1.0,
):
    """Rectangular target and rectangular covers added with flexible number of covers and flexible target and cover placement

    Parameters
    ----------
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of grating, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of grating, in pixels
    target_size : float or (float, float)
        size of the target in degrees of visual angle (height, width)
    target_position : float or (float, float)
        coordinates where to place the target
    covers_size : float or (float, float)
        size of the covers in degrees of visual angle (height, width)
    covers_x : tuple of floats
        x coordinates of covers; as many covers as there are coordinates
    covers_y : tuple of floats
        y coordinates of covers; as many covers as there are coordinates
    intensity_background : float
        intensity value for background
    intensity_target : float
        intensity value for target
    intensity_covers : Sequence[Number, ...] or Number
        intensity value for covers

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for the target (key: "target_mask"),
        and additional keys containing stimulus parameters

    References
    ----------
    Blakeslee, B., & McCourt, M. E. (1999).
        A multiscale spatial ﬁltering account
        of the White eﬀect, simultaneous brightness contrast and grating induction.
        Vision Research, 39, 4361-4377.
    Pessoa, L., Baratoff, G., Neumann, H., & Todorovic, D. (1998).
        Lightness and junctions: variations on White's display.
        Investigative Ophthalmology and Visual Science (Supplement), 39, S159.
    Todorovic, D. (1997).
        Lightness and junctions. Perception, 26, 379-395.
    """
    if target_size is None:
        raise ValueError(
            "rectangle_generalized() missing argument 'target_size' which is not 'None'"
        )
    if covers_size is None:
        raise ValueError(
            "rectangle_generalized() missing argument 'covers_size' which is not 'None'"
        )
    if covers_x is None:
        raise ValueError("rectangle_generalized() missing argument 'covers_x' which is not 'None'")
    if covers_y is None:
        raise ValueError("rectangle_generalized() missing argument 'covers_y' which is not 'None'")

    # Resolve resolution
    shape, visual_size, ppd = resolution.resolve(shape=shape, visual_size=visual_size, ppd=ppd)
    if len(np.unique(ppd)) > 1:
        raise ValueError("ppd should be equal in x and y direction")

    if isinstance(covers_size, (float, int)):
        covers_size = (covers_size, covers_size)
    if len(covers_x) != len(covers_y):
        raise ValueError("Need as many x- as y-coordinates")

    # Create image with square
    stim = rectangle_shape(
        visual_size=visual_size,
        ppd=ppd,
        rectangle_size=target_size,
        rectangle_position=target_position,
        intensity_background=intensity_background,
        intensity_rectangle=intensity_target,
    )
    img = stim["img"]
    mask = stim["rectangle_mask"]

    # Add covers
    cheight, cwidth = resolution.lengths_from_visual_angles_ppd(
        covers_size, np.unique(ppd), round=False
    )
    cx = resolution.lengths_from_visual_angles_ppd(covers_x, np.unique(ppd), round=False)
    cy = resolution.lengths_from_visual_angles_ppd(covers_y, np.unique(ppd), round=False)

    cheight = int(np.round(cheight))
    cwidth = int(np.round(cwidth))
    cx = np.round(cx).astype(int)
    cy = np.round(cy).astype(int)

    if isinstance(intensity_covers, (float, int)):
        int_cov = [
            intensity_covers,
        ]
    else:
        int_cov = list(intensity_covers)
    int_cov = itertools.cycle(int_cov)

    for i in range(len(covers_x)):
        img[cy[i] : cy[i] + cheight, cx[i] : cx[i] + cwidth] = next(int_cov)
        mask[cy[i] : cy[i] + cheight, cx[i] : cx[i] + cwidth] = 0
        if cy[i] + cheight > shape[0] or cx[i] + cwidth > shape[1]:
            raise ValueError("Covers do not fully fit into stimulus")

    stim["img"] = img
    stim["target_mask"] = mask.astype(int)
    stim["visual_size"] = visual_size
    stim["ppd"] = ppd
    stim["shape"] = shape
    stim["target_size"] = stim["rectangle_size"]
    stim["target_position"] = stim["rectangle_position"]
    stim["intensity_target"] = stim["intensity_rectangle"]
    stim["covers_size"] = covers_size
    stim["covers_x"] = covers_x
    stim["covers_y"] = covers_y
    stim["intensity_covers"] = intensity_covers
    del stim["rectangle_size"]
    del stim["rectangle_position"]
    del stim["intensity_rectangle"]
    return stim


def rectangle(
    visual_size=None,
    ppd=None,
    shape=None,
    target_size=None,
    target_position=None,
    covers_size=None,
    covers_offset=None,
    intensity_background=0.0,
    intensity_target=0.5,
    intensity_covers=1.0,
):
    """Rectangular target in the center and four rectangular covers added symmetrically around target center

    Parameters
    ----------
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of grating, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of grating, in pixels
    target_size : float or (float, float)
        size of the target in degrees of visual angle (height, width)
    target_position : float or (float, float)
        coordinates where to place the target
    covers_size : float or (float, float)
        size of covers in degrees of visual angle (height, width)
    covers_offset : float or (float, float)
        distance from cover center to target center in (y, x)
    intensity_background : float
        intensity value for background
    intensity_target : float
        intensity value for target
    intensity_covers : Sequence[Number, ...] or Number
        intensity value for covers

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for the target (key: "target_mask"),
        and additional keys containing stimulus parameters

    References
    ----------
    Blakeslee, B., & McCourt, M. E. (1999).
        A multiscale spatial ﬁltering account
        of the White eﬀect, simultaneous brightness contrast and grating induction.
        Vision Research, 39, 4361-4377.
    Pessoa, L., Baratoff, G., Neumann, H., & Todorovic, D. (1998).
        Lightness and junctions: variations on White's display.
        Investigative Ophthalmology and Visual Science (Supplement), 39, S159.
    Todorovic, D. (1997).
        Lightness and junctions. Perception, 26, 379-395.
    """
    if target_size is None:
        raise ValueError("rectangle() missing argument 'target_size' which is not 'None'")
    if covers_size is None:
        raise ValueError("rectangle() missing argument 'covers_size' which is not 'None'")
    if covers_offset is None:
        raise ValueError("rectangle() missing argument 'covers_offset' which is not 'None'")

    # Resolve resolution
    shape, visual_size, ppd = resolution.resolve(shape=shape, visual_size=visual_size, ppd=ppd)
    if len(np.unique(ppd)) > 1:
        raise ValueError("ppd should be equal in x and y direction")

    if isinstance(covers_size, (float, int)):
        covers_size = (covers_size, covers_size)
    if isinstance(covers_offset, (float, int)):
        covers_offset = (covers_offset, covers_offset)

    # Calculate placement of covers for generalized function:
    cy, cx = np.array(visual_size) / 2
    y1 = cy - covers_offset[0] - covers_size[0] / 2
    x1 = cx - covers_offset[1] - covers_size[1] / 2
    y2 = cy + covers_offset[0] - covers_size[0] / 2
    x2 = cx + covers_offset[1] - covers_size[1] / 2

    stim = rectangle_generalized(
        visual_size=visual_size,
        ppd=ppd,
        target_size=target_size,
        target_position=target_position,
        covers_size=covers_size,
        covers_x=(x1, x2, x2, x1),
        covers_y=(y1, y2, y1, y2),
        intensity_background=intensity_background,
        intensity_target=intensity_target,
        intensity_covers=intensity_covers,
    )
    return stim


def rectangle_two_sided(
    visual_size=None,
    ppd=None,
    shape=None,
    target_size=None,
    covers_size=None,
    covers_offset=None,
    intensity_backgrounds=(0.0, 1.0),
    intensity_target=0.5,
    intensity_covers=(1.0, 0.0),
):
    """
    Two-sided Todorovic's illusion with rectangular target in the center and four
    rectangular covers added symmetrically around target center

    Parameters
    ----------
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of grating, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of grating, in pixels
    target_size : float or (float, float)
        size of the target in degrees of visual angle (height, width)
    covers_size : float or (float, float)
        size of covers in degrees of visual angle (height, width)
    covers_offset : float or (float, float)
        distance from cover center to target center in (y, x)
    intensity_background : Sequence[Number, Number]
        intensity values for backgrounds
    intensity_target : float
        intensity value for target
    intensity_covers : Sequence[Number, Number]
        intensity values for covers

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for the target (key: "target_mask"),
        and additional keys containing stimulus parameters

    References
    ----------
    Blakeslee, B., & McCourt, M. E. (1999).
        A multiscale spatial ﬁltering account
        of the White eﬀect, simultaneous brightness contrast and grating induction.
        Vision Research, 39, 4361-4377.
    Pessoa, L., Baratoff, G., Neumann, H., & Todorovic, D. (1998).
        Lightness and junctions: variations on White's display.
        Investigative Ophthalmology and Visual Science (Supplement), 39, S159.
    Todorovic, D. (1997).
        Lightness and junctions. Perception, 26, 379-395.
    """

    # Resolve resolution
    shape, visual_size, ppd = resolution.resolve(shape=shape, visual_size=visual_size, ppd=ppd)

    stim1 = rectangle(
        visual_size=(visual_size[0], visual_size[1] / 2),
        ppd=ppd,
        target_size=target_size,
        covers_size=covers_size,
        covers_offset=covers_offset,
        intensity_background=intensity_backgrounds[0],
        intensity_target=intensity_target,
        intensity_covers=intensity_covers[0],
    )

    stim2 = rectangle(
        visual_size=(visual_size[0], visual_size[1] / 2),
        ppd=ppd,
        target_size=target_size,
        covers_size=covers_size,
        covers_offset=covers_offset,
        intensity_background=intensity_backgrounds[1],
        intensity_target=intensity_target,
        intensity_covers=intensity_covers[1],
    )

    stim = stack_dicts(stim1, stim2)
    del stim["intensity_background"]
    del stim["target_position"]
    stim["intensity_backgrounds"] = intensity_backgrounds
    stim["intensity_covers"] = intensity_covers
    stim["target_positions"] = (stim1["target_position"], stim2["target_position"])
    stim["shape"] = shape
    stim["visual_size"] = visual_size
    return stim


def cross_generalized(
    visual_size=None,
    ppd=None,
    shape=None,
    cross_size=None,
    cross_thickness=None,
    covers_size=None,
    covers_x=None,
    covers_y=None,
    intensity_background=0.0,
    intensity_target=0.5,
    intensity_covers=1.0,
):
    """Cross target and rectangular covers added with flexible number of covers and flexible cover placement

    Parameters
    ----------
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of grating, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of grating, in pixels
    cross_size : float or (float, float)
        size of target cross in visual angle
    cross_thickness : float
        thickness of target cross in visual angle
    covers_size : float or (float, float)
        size of covers in degrees visual angle (height, width)
    covers_x : tuple of floats
        x coordinates of covers; as many covers as there are coordinates
    covers_y : tuple of floats
        y coordinates of covers; as many covers as there are coordinates
    intensity_background : float
        intensity value for background
    intensity_target : float
        intensity value for target
    intensity_covers : Sequence[Number, ...] or Number
        intensity value for covers

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for the target (key: "target_mask"),
        and additional keys containing stimulus parameters

    References
    ----------
    Blakeslee, B., & McCourt, M. E. (1999).
        A multiscale spatial ﬁltering account
        of the White eﬀect, simultaneous brightness contrast and grating induction.
        Vision Research, 39, 4361-4377.
    Pessoa, L., Baratoff, G., Neumann, H., & Todorovic, D. (1998).
        Lightness and junctions: variations on White's display.
        Investigative Ophthalmology and Visual Science (Supplement), 39, S159.
    Todorovic, D. (1997).
        Lightness and junctions. Perception, 26, 379-395.
    """
    if cross_size is None:
        raise ValueError("cross_generalized() missing argument 'cross_size' which is not 'None'")
    if cross_thickness is None:
        raise ValueError(
            "cross_generalized() missing argument 'cross_thickness' which is not 'None'"
        )
    if covers_size is None:
        raise ValueError("cross_generalized() missing argument 'covers_size' which is not 'None'")
    if covers_x is None:
        raise ValueError("cross_generalized() missing argument 'covers_x' which is not 'None'")
    if covers_y is None:
        raise ValueError("cross_generalized() missing argument 'covers_y' which is not 'None'")

    # Resolve resolution
    shape, visual_size, ppd = resolution.resolve(shape=shape, visual_size=visual_size, ppd=ppd)
    ppd = np.unique(ppd)[0]

    if not isinstance(ppd, (float, int)):
        raise ValueError("ppd should be equal in x and y direction")
    if isinstance(covers_x, (float, int)):
        covers_x = (covers_x,)
    if isinstance(covers_y, (float, int)):
        covers_y = (covers_y,)
    if len(covers_x) != len(covers_y):
        raise ValueError("Need as many x- as y-coordinates")
    if isinstance(covers_size, (float, int)):
        covers_size = (covers_size, covers_size)
    if isinstance(cross_size, (float, int)):
        cross_size = (cross_size, cross_size)

    if cross_size[0] < cross_thickness or cross_size[1] < cross_thickness:
        raise ValueError("cross_size needs to be larger than cross_thickness")

    stim = cross_shape(
        visual_size=cross_size,
        ppd=ppd,
        cross_size=cross_size,
        cross_arm_ratios=1,
        cross_thickness=cross_thickness,
        intensity_background=intensity_background,
        intensity_cross=intensity_target,
    )

    stim = pad_dict_to_shape(stim, shape=shape, pad_value=intensity_background)
    img = stim["img"]
    mask = stim["cross_mask"]

    cheight, cwidth = resolution.lengths_from_visual_angles_ppd(
        covers_size, np.unique(ppd), round=False
    )
    cx = resolution.lengths_from_visual_angles_ppd(covers_x, np.unique(ppd), round=False)
    cy = resolution.lengths_from_visual_angles_ppd(covers_y, np.unique(ppd), round=False)

    cheight = int(np.round(cheight))
    cwidth = int(np.round(cwidth))
    cx = np.round(cx).astype(int)
    cy = np.round(cy).astype(int)

    if isinstance(intensity_covers, (float, int)):
        int_cov = [
            intensity_covers,
        ]
    else:
        int_cov = list(intensity_covers)
    int_cov = itertools.cycle(int_cov)

    for i in range(len(covers_x)):
        img[cy[i] : cy[i] + cheight, cx[i] : cx[i] + cwidth] = next(int_cov)
        mask[cy[i] : cy[i] + cheight, cx[i] : cx[i] + cwidth] = 0
        if cy[i] + cheight > shape[0] or cx[i] + cwidth > shape[1]:
            raise ValueError("Covers do not fully fit into stimulus")

    stim["img"] = img
    stim["target_mask"] = mask.astype(int)
    stim["target_size"] = stim["cross_size"]
    stim["intensity_target"] = intensity_target
    stim["covers_size"] = covers_size
    stim["covers_x"] = covers_x
    stim["covers_y"] = covers_y
    stim["intensity_covers"] = intensity_covers
    stim["visual_size"] = visual_size
    stim["ppd"] = ppd
    stim["shape"] = shape
    del (stim["cross_size"], stim["intensity_cross"], stim["cross_mask"])
    return stim


def cross(
    visual_size=None,
    ppd=None,
    shape=None,
    cross_size=None,
    cross_thickness=None,
    covers_size=None,
    intensity_background=0.0,
    intensity_target=0.5,
    intensity_covers=1.0,
):
    """Cross target and four rectangular covers added at inner cross corners

    Parameters
    ----------
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of grating, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of grating, in pixels
    cross_size : float or (float, float)
        size of target cross in visual angle
    cross_thickness : float
        thickness of target cross in visual angle
    covers_size : float or (float, float)
        size of covers in degrees of visual angle (height, width)
    intensity_background : float
        intensity value for background
    intensity_target : float
        intensity value for target
    intensity_covers : Sequence[Number, ...] or Number
        intensity value for covers

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for the target (key: "target_mask"),
        and additional keys containing stimulus parameters

    References
    ----------
    Blakeslee, B., & McCourt, M. E. (1999).
        A multiscale spatial ﬁltering account
        of the White eﬀect, simultaneous brightness contrast and grating induction.
        Vision Research, 39, 4361-4377.
    Pessoa, L., Baratoff, G., Neumann, H., & Todorovic, D. (1998).
        Lightness and junctions: variations on White's display.
        Investigative Ophthalmology and Visual Science (Supplement), 39, S159.
    Todorovic, D. (1997).
        Lightness and junctions. Perception, 26, 379-395.
    """
    if cross_size is None:
        raise ValueError("cross() missing argument 'cross_size' which is not 'None'")
    if cross_thickness is None:
        raise ValueError("cross() missing argument 'cross_thickness' which is not 'None'")
    if covers_size is None:
        raise ValueError("cross() missing argument 'covers_size' which is not 'None'")

    # Resolve resolution
    shape, visual_size, ppd = resolution.resolve(shape=shape, visual_size=visual_size, ppd=ppd)
    if len(np.unique(ppd)) > 1:
        raise ValueError("ppd should be equal in x and y direction")
    if isinstance(covers_size, (float, int)):
        covers_size = (covers_size, covers_size)

    # Calculate placement of covers for generalized function:
    ppd = np.unique(ppd)[0]
    cy = np.floor(shape[0] / 2) / ppd
    cx = np.floor(shape[1] / 2) / ppd
    ct = np.ceil(cross_thickness * ppd)
    ct = (ct + (ct % 2)) / ppd
    ct_half = ct / 2

    y1 = cy - cross_thickness / 2 - covers_size[0]
    x1 = cx - cross_thickness / 2 - covers_size[1]
    y2 = cy + ct_half
    x2 = cx + ct_half

    stim = cross_generalized(
        visual_size=visual_size,
        ppd=ppd,
        cross_size=cross_size,
        cross_thickness=ct,
        covers_size=covers_size,
        covers_x=(x1, x2, x2, x1),
        covers_y=(y1, y2, y1, y2),
        intensity_background=intensity_background,
        intensity_target=intensity_target,
        intensity_covers=intensity_covers,
    )
    return stim


def cross_two_sided(
    visual_size=None,
    ppd=None,
    shape=None,
    cross_size=None,
    cross_thickness=None,
    covers_size=None,
    intensity_backgrounds=(0.0, 1.0),
    intensity_target=0.5,
    intensity_covers=(1.0, 0.0),
):
    """Two-sided with cross target and four rectangular covers added at inner cross corners

    Parameters
    ----------
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of grating, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of grating, in pixels
    cross_size : float or (float, float)
        size of target cross in visual angle
    cross_thickness : float
        thickness of target cross in visual angle
    covers_size : float or (float, float)
        size of covers in degrees of visual angle (height, width)
    intensity_backgrounds : Sequence[Number, Number]
        intensity values for backgrounds
    intensity_target : float
        intensity value for target
    intensity_covers : Sequence[Number, Number]
        intensity values for covers

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for the target (key: "target_mask"),
        and additional keys containing stimulus parameters

    References
    ----------
    Blakeslee, B., & McCourt, M. E. (1999).
        A multiscale spatial ﬁltering account
        of the White eﬀect, simultaneous brightness contrast and grating induction.
        Vision Research, 39, 4361-4377.
    Pessoa, L., Baratoff, G., Neumann, H., & Todorovic, D. (1998).
        Lightness and junctions: variations on White's display.
        Investigative Ophthalmology and Visual Science (Supplement), 39, S159.
    Todorovic, D. (1997).
        Lightness and junctions. Perception, 26, 379-395.
    """

    # Resolve resolution
    shape, visual_size, ppd = resolution.resolve(shape=shape, visual_size=visual_size, ppd=ppd)

    stim1 = cross(
        visual_size=(visual_size[0], visual_size[1] / 2),
        ppd=ppd,
        cross_size=cross_size,
        cross_thickness=cross_thickness,
        covers_size=covers_size,
        intensity_background=intensity_backgrounds[0],
        intensity_target=intensity_target,
        intensity_covers=intensity_covers[0],
    )

    stim2 = cross(
        visual_size=(visual_size[0], visual_size[1] / 2),
        ppd=ppd,
        cross_size=cross_size,
        cross_thickness=cross_thickness,
        covers_size=covers_size,
        intensity_background=intensity_backgrounds[1],
        intensity_target=intensity_target,
        intensity_covers=intensity_covers[1],
    )

    stim = stack_dicts(stim1, stim2)
    del stim["intensity_background"]
    stim["intensity_backgrounds"] = intensity_backgrounds
    stim["intensity_covers"] = intensity_covers
    stim["shape"] = shape
    stim["visual_size"] = visual_size
    return stim


def equal(
    visual_size=None,
    ppd=None,
    shape=None,
    cross_size=None,
    cross_thickness=None,
    intensity_background=0.0,
    intensity_target=0.5,
    intensity_covers=1.0,
):
    """Cross target and four rectangular covers added at inner cross corners

    Parameters
    ----------
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of grating, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of grating, in pixels
    cross_size : float or (float, float)
        size of target cross in visual angle
    cross_thickness : float
        thickness of target cross in visual angle
    intensity_background : float
        intensity value for background
    intensity_target : float
        intensity value for target
    intensity_covers : float
        intensity value for covers

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for the target (key: "target_mask"),
        and additional keys containing stimulus parameters

    References
    ----------
    Blakeslee, B., & McCourt, M. E. (1999).
        A multiscale spatial ﬁltering account
        of the White eﬀect, simultaneous brightness contrast and grating induction.
        Vision Research, 39, 4361-4377.
    Pessoa, L., Baratoff, G., Neumann, H., & Todorovic, D. (1998).
        Lightness and junctions: variations on White's display.
        Investigative Ophthalmology and Visual Science (Supplement), 39, S159.
    Todorovic, D. (1997).
        Lightness and junctions. Perception, 26, 379-395.
    """
    if cross_size is None:
        raise ValueError("equal() missing argument 'cross_size' which is not 'None'")
    if cross_thickness is None:
        raise ValueError("equal() missing argument 'cross_thickness' which is not 'None'")

    if isinstance(cross_size, (float, int)):
        cross_size = (cross_size, cross_size)

    # Resolve resolution
    shape, visual_size, ppd = resolution.resolve(shape=shape, visual_size=visual_size, ppd=ppd)
    if len(np.unique(ppd)) > 1:
        raise ValueError("ppd should be equal in x and y direction")

    # Calculate placement of covers for generalized function:
    ppd = np.unique(ppd)[0]
    c1 = (np.ceil(cross_size[0] / 2 * ppd - cross_thickness / 2 * ppd + 1)) / ppd
    c2 = (np.ceil(cross_size[1] / 2 * ppd - cross_thickness / 2 * ppd + 1)) / ppd
    covers_size = (c1, c2)

    # covers_size = ((cross_size[0] - cross_thickness) / 2, (cross_size[1] - cross_thickness) / 2)

    stim = cross(
        visual_size=visual_size,
        ppd=ppd,
        shape=shape,
        cross_size=cross_size,
        cross_thickness=cross_thickness,
        covers_size=covers_size,
        intensity_background=intensity_background,
        intensity_target=intensity_target,
        intensity_covers=intensity_covers,
    )

    window = rectangle_shape(
        visual_size=visual_size,
        ppd=ppd,
        shape=shape,
        rectangle_size=cross_size,
    )

    stim["img"] = np.where(window["rectangle_mask"], stim["img"], intensity_background)
    stim["target_mask"] = np.where(window["rectangle_mask"], stim["target_mask"], 0).astype(int)
    return stim


def equal_two_sided(
    visual_size=None,
    ppd=None,
    shape=None,
    cross_size=None,
    cross_thickness=None,
    intensity_backgrounds=(0.0, 1.0),
    intensity_target=0.5,
    intensity_covers=(1.0, 0.0),
):
    """Two-sided with cross target and four rectangular covers added at inner cross corners

    Parameters
    ----------
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of grating, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of grating, in pixels
    cross_size : float or (float, float)
        size of target cross in visual angle
    cross_thickness : float
        thickness of target cross in visual angle
    intensity_background : float
        intensity value for background
    intensity_target : float
        intensity value for target
    intensity_covers : float
        intensity value for covers

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for the target (key: "target_mask"),
        and additional keys containing stimulus parameters

    References
    ----------
    Blakeslee, B., & McCourt, M. E. (1999).
        A multiscale spatial ﬁltering account
        of the White eﬀect, simultaneous brightness contrast and grating induction.
        Vision Research, 39, 4361-4377.
    Pessoa, L., Baratoff, G., Neumann, H., & Todorovic, D. (1998).
        Lightness and junctions: variations on White's display.
        Investigative Ophthalmology and Visual Science (Supplement), 39, S159.
    Todorovic, D. (1997).
        Lightness and junctions. Perception, 26, 379-395.
    """

    # Resolve resolution
    shape, visual_size, ppd = resolution.resolve(shape=shape, visual_size=visual_size, ppd=ppd)

    stim1 = equal(
        visual_size=(visual_size[0], visual_size[1] / 2),
        ppd=ppd,
        cross_size=cross_size,
        cross_thickness=cross_thickness,
        intensity_background=intensity_backgrounds[0],
        intensity_target=intensity_target,
        intensity_covers=intensity_covers[0],
    )

    stim2 = equal(
        visual_size=(visual_size[0], visual_size[1] / 2),
        ppd=ppd,
        cross_size=cross_size,
        cross_thickness=cross_thickness,
        intensity_background=intensity_backgrounds[1],
        intensity_target=intensity_target,
        intensity_covers=intensity_covers[1],
    )

    stim = stack_dicts(stim1, stim2)
    del stim["intensity_background"]
    stim["intensity_backgrounds"] = intensity_backgrounds
    stim["intensity_covers"] = intensity_covers
    stim["shape"] = shape
    stim["visual_size"] = visual_size
    return stim


def overview(**kwargs):
    """Generate example stimuli from this module

    Returns
    -------
    stims : dict
        dict with all stimuli containing individual stimulus dicts.
    """
    default_params = {
        "visual_size": 10,
        "ppd": 30,
    }
    default_params.update(kwargs)

    rectangle_params = {
        "target_size": 3,
        "covers_size": 1.5,
    }

    cross_params = {
        "cross_size": 4,
        "cross_thickness": 1.5,
    }
    # fmt: off
    stimuli = {
        "todorovic_rectangle": rectangle(**default_params, **rectangle_params, covers_offset=1.5),
        "todorovic_rectangle_general": rectangle_generalized(**default_params, **rectangle_params, target_position=3.5, covers_x=(2, 6), covers_y=(2, 6)),
        "todorovic_rectangle_2sided": rectangle_two_sided(**default_params, **rectangle_params, covers_offset=1),
        "todorovic_cross": cross(**default_params, **cross_params, covers_size=2),
        "todorovic_cross_general": cross_generalized(**default_params, **cross_params, covers_size=2, covers_x=(2, 6), covers_y=(2, 6)),
        "todorovic_cross_2sided": cross_two_sided(**default_params, **cross_params, covers_size=1),
        "todorovic_equal": equal(**default_params, **cross_params,),
        "todorovic_equal_2sided": equal_two_sided(**default_params, **cross_params,),
    }
    # fmt: on

    return stimuli


if __name__ == "__main__":
    from stimupy.utils import plot_stimuli

    stims = overview()
    plot_stimuli(stims, mask=False, save=None)
