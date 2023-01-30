import numpy as np

from stimuli.components.shapes import cross as cross_shape
from stimuli.components.shapes import rectangle as rectangle_shape
from stimuli.utils import degrees_to_pixels, pad_dict_to_shape, resolution

__all__ = [
    "rectangle_generalized",
    "rectangle",
    "cross_generalized",
    "cross",
    "equal",
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
    """
    Todorovic's illusion with rectangular target and rectangular covers added with flexible
    number of covers and flexible target and cover placement

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
    intensity_covers : float
        intensity value for covers

    Returns
    ----------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for the target (key: "target_mask"),
        and additional keys containing stimulus parameters

    References
    -----------
    Blakeslee, B., & McCourt, M. E. (1999). A multiscale spatial ﬁltering account of the
        White eﬀect, simultaneous brightness contrast and grating induction. Vision
        Research, 39, 4361–4377.
    Pessoa, L., Baratoff, G., Neumann, H., & Todorovic, D. (1998). Lightness and junctions:
        variations on White’s display. Investigative Ophthalmology and Visual Science
        (Supplement), 39, S159.
    Todorovic, D. (1997). Lightness and junctions. Perception, 26, 379–395.
    """
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
    mask = stim["shape_mask"]

    # Add covers
    cheight, cwidth = degrees_to_pixels(covers_size, ppd)
    cx = degrees_to_pixels(covers_x, np.unique(ppd))
    cy = degrees_to_pixels(covers_y, np.unique(ppd))

    if np.max(cx) < np.min(cx) + cwidth or np.max(cy) < np.min(cy) + cheight:
        raise ValueError("Covers overlap")

    for i in range(len(covers_x)):
        img[cy[i] : cy[i] + cheight, cx[i] : cx[i] + cwidth] = intensity_covers
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
    return stim


def rectangle(
    visual_size=None,
    ppd=None,
    shape=None,
    target_size=None,
    covers_size=None,
    covers_offset=None,
    intensity_background=0.0,
    intensity_target=0.5,
    intensity_covers=1.0,
):
    """
    Todorovic's illusion with rectangular target in the center and four rectangular covers added
    symmetrically around target center

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
    intensity_background : float
        intensity value for background
    intensity_target : float
        intensity value for target
    intensity_covers : float
        intensity value for covers

    Returns
    ----------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for the target (key: "target_mask"),
        and additional keys containing stimulus parameters

    References
    -----------
    Blakeslee, B., & McCourt, M. E. (1999). A multiscale spatial ﬁltering account of the
        White eﬀect, simultaneous brightness contrast and grating induction. Vision
        Research, 39, 4361–4377.
    Pessoa, L., Baratoff, G., Neumann, H., & Todorovic, D. (1998). Lightness and junctions:
        variations on White’s display. Investigative Ophthalmology and Visual Science
        (Supplement), 39, S159.
    Todorovic, D. (1997). Lightness and junctions. Perception, 26, 379–395.
    """
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
        target_position=None,
        covers_size=covers_size,
        covers_x=(x1, x2, x2, x1),
        covers_y=(y1, y2, y1, y2),
        intensity_background=intensity_background,
        intensity_target=intensity_target,
        intensity_covers=intensity_covers,
    )
    return stim


def cross_generalized(
    visual_size=None,
    ppd=None,
    shape=None,
    cross_size=None,
    cross_arm_ratios=1,
    cross_thickness=None,
    covers_size=None,
    covers_x=None,
    covers_y=None,
    intensity_background=0.0,
    intensity_target=0.5,
    intensity_covers=1.0,
):
    """
    Todorovic's illusion with cross target and rectangular covers added with flexible number of
    covers and flexible cover placement

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
    cross_arm_ratios : float or (float, float)
        ratio used to create arms (up-down, left-right)
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
    intensity_covers : float
        intensity value for covers

    Returns
    ----------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for the target (key: "target_mask"),
        and additional keys containing stimulus parameters

    References
    -----------
    Blakeslee, B., & McCourt, M. E. (1999). A multiscale spatial ﬁltering account of the
        White eﬀect, simultaneous brightness contrast and grating induction. Vision
        Research, 39, 4361–4377.
    Pessoa, L., Baratoff, G., Neumann, H., & Todorovic, D. (1998). Lightness and junctions:
        variations on White’s display. Investigative Ophthalmology and Visual Science
        (Supplement), 39, S159.
    Todorovic, D. (1997). Lightness and junctions. Perception, 26, 379–395.
    """
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

    stim = cross_shape(
        visual_size=cross_size,
        ppd=ppd,
        cross_size=cross_size,
        cross_arm_ratios=cross_arm_ratios,
        cross_thickness=cross_thickness,
        intensity_background=intensity_background,
        intensity_cross=intensity_target,
    )

    stim = pad_dict_to_shape(stim, shape=shape, pad_value=intensity_background)
    img = stim["img"]
    mask = stim["shape_mask"]

    cheight, cwidth = degrees_to_pixels(covers_size, ppd)
    cx = degrees_to_pixels(covers_x, ppd)
    cy = degrees_to_pixels(covers_y, ppd)

    for i in range(len(covers_x)):
        img[cy[i] : cy[i] + cheight, cx[i] : cx[i] + cwidth] = intensity_covers
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
    del (stim["cross_size"], stim["intensity_cross"], stim["shape_mask"])
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
    """
    Todorovic's illusion with cross target and four rectangular covers added at inner cross corners

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
    intensity_covers : float
        intensity value for covers

    Returns
    ----------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for the target (key: "target_mask"),
        and additional keys containing stimulus parameters

    References
    -----------
    Blakeslee, B., & McCourt, M. E. (1999). A multiscale spatial ﬁltering account of the
        White eﬀect, simultaneous brightness contrast and grating induction. Vision
        Research, 39, 4361–4377.
    Pessoa, L., Baratoff, G., Neumann, H., & Todorovic, D. (1998). Lightness and junctions:
        variations on White’s display. Investigative Ophthalmology and Visual Science
        (Supplement), 39, S159.
    Todorovic, D. (1997). Lightness and junctions. Perception, 26, 379–395.
    """
    # Resolve resolution
    shape, visual_size, ppd = resolution.resolve(shape=shape, visual_size=visual_size, ppd=ppd)
    if len(np.unique(ppd)) > 1:
        raise ValueError("ppd should be equal in x and y direction")
    if isinstance(covers_size, (float, int)):
        covers_size = (covers_size, covers_size)

    # Calculate placement of covers for generalized function:
    ppd = np.unique(ppd)[0]
    cy, cx = np.floor(np.array(visual_size) * ppd / 2) / ppd
    ct = np.ceil(cross_thickness * ppd)
    ct = (ct + (ct % 2)) / ppd
    ct_half = ct / 2

    y1 = cy - ct_half - covers_size[0]
    x1 = cx - ct_half - covers_size[1]
    y2 = cy + ct_half
    x2 = cx + ct_half

    stim = cross_generalized(
        visual_size=visual_size,
        ppd=ppd,
        cross_size=cross_size,
        cross_arm_ratios=1.0,
        cross_thickness=ct,
        covers_size=covers_size,
        covers_x=(x1, x2, x2, x1),
        covers_y=(y1, y2, y1, y2),
        intensity_background=intensity_background,
        intensity_target=intensity_target,
        intensity_covers=intensity_covers,
    )
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
    """
    Todorovic's illusion with cross target and four rectangular covers added at inner cross corners

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
    ----------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for the target (key: "target_mask"),
        and additional keys containing stimulus parameters

    References
    -----------
    Blakeslee, B., & McCourt, M. E. (1999). A multiscale spatial ﬁltering account of the
        White eﬀect, simultaneous brightness contrast and grating induction. Vision
        Research, 39, 4361–4377.
    Pessoa, L., Baratoff, G., Neumann, H., & Todorovic, D. (1998). Lightness and junctions:
        variations on White’s display. Investigative Ophthalmology and Visual Science
        (Supplement), 39, S159.
    Todorovic, D. (1997). Lightness and junctions. Perception, 26, 379–395.
    """
    if isinstance(cross_size, (float, int)):
        cross_size = (cross_size, cross_size)

    covers_size = ((cross_size[0] - cross_thickness) / 2, (cross_size[1] - cross_thickness) / 2)

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
    return stim


if __name__ == "__main__":
    from stimuli.utils import plot_stimuli

    p1 = {
        "visual_size": 10,
        "ppd": 10,
        "target_size": 4,
        "covers_size": 2,
    }
    
    p2 = {
        "visual_size": 10,
        "ppd": 10,
        "cross_size": 4,
        "cross_thickness": 2,
    }

    stims = {
        "rectangle": rectangle(**p1, covers_offset=2),
        "rectangle_general": rectangle_generalized(**p1, target_position=3, covers_x=(2, 6), covers_y=(2, 6)),
        "cross": cross(**p2, covers_size=2),
        "cross_general": cross_generalized(**p2, covers_size=2, covers_x=(2, 6), covers_y=(2, 6)),
        "equal": equal(**p2),
    }
    plot_stimuli(stims, mask=True, save=None)
