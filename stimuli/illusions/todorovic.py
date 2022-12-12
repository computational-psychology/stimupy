import numpy as np

from stimuli.components import cross, rectangle
from stimuli.utils import degrees_to_pixels, pad_to_visual_size


__all__ = [
    "todorovic_rectangle_generalized",
    "todorovic_rectangle",
    "todorovic_cross_generalized",
    "todorovic_cross",
]

def todorovic_rectangle_generalized(
    visual_size=None,
    ppd=None,
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
    visual_size : float or (float, float)
        size of the stimulus in degrees of visual angle (height, width)
    ppd : int
        pixels per degree (visual angle)
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
    -------
    A stimulus dictionary with the stimulus ['img'] and target mask ['mask']

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

    if isinstance(visual_size, (float, int)):
        visual_size = (visual_size, visual_size)
    if isinstance(covers_size, (float, int)):
        covers_size = (covers_size, covers_size)
    if len(covers_x) != len(covers_y):
        raise ValueError("Need as many x- as y-coordinates")

    # Create image with square
    stim = rectangle(
        visual_size=visual_size,
        ppd=ppd,
        rectangle_size=target_size,
        rectangle_position=target_position,
        intensity_background=intensity_background,
        intensity_rectangle=intensity_target,
        )
    img = stim["img"]
    mask = stim["mask"]

    # Add covers
    cheight, cwidth = degrees_to_pixels(covers_size, ppd)
    cx = degrees_to_pixels(covers_x, ppd)
    cy = degrees_to_pixels(covers_y, ppd)

    if np.max(cx) < np.min(cx) + cwidth or np.max(cy) < np.min(cy) + cheight:
        raise ValueError("Covers overlap")

    for i in range(len(covers_x)):
        img[cy[i] : cy[i] + cheight, cx[i] : cx[i] + cwidth] = intensity_covers
        mask[cy[i] : cy[i] + cheight, cx[i] : cx[i] + cwidth] = 0
        if cy[i] + cheight > visual_size[0] * ppd or cx[i] + cwidth > visual_size[1] * ppd:
            raise ValueError("Covers do not fully fit into stimulus")

    stim["img"] = img
    stim["mask"] = mask.astype(int)
    stim["target_size"] = stim["rectangle_size"]
    stim["target_position"] = stim["rectangle_position"]
    stim["intensity_target"] = stim["intensity_rectangle"]
    stim["covers_size"] = covers_size
    stim["covers_x"] = covers_x
    stim["covers_y"] = covers_y
    stim["intensity_covers"] = intensity_covers
    return stim


def todorovic_rectangle(
    visual_size=None,
    ppd=None,
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
    visual_size : float or (float, float)
        size of the stimulus in degrees of visual angle (height, width)
    ppd : int
        pixels per degree (visual angle)
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
    -------
    A stimulus dictionary with the stimulus ['img'] and target mask ['mask']

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
    if isinstance(visual_size, (float, int)):
        visual_size = (visual_size, visual_size)
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

    stim = todorovic_rectangle_generalized(
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


def todorovic_cross_generalized(
    visual_size=None,
    ppd=None,
    cross_size=None,
    cross_arm_ratios=None,
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
    visual_size : (float, float)
        size of the stimulus in degrees of visual angle (height, width)
    ppd : int
        pixels per degree (visual angle)
    cross_size : 
        
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
    -------
    A stimulus dictionary with the stimulus ['img'] and target mask ['mask']

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

    if isinstance(visual_size, (float, int)):
        visual_size = (visual_size, visual_size)
    if isinstance(cross_size, (float, int)):
        cross_size = (cross_size, cross_size)
    if isinstance(covers_size, (float, int)):
        covers_size = (covers_size, covers_size)

    if len(covers_x) != len(covers_y):
        raise ValueError("Need as many x- as y-coordinates")
    if (cross_size[0] > visual_size[0]) or (cross_size[1] > visual_size[1]):
        raise ValueError("Cross larger than image")
    if np.min(cross_size) <= cross_thickness:
        raise ValueError("cross_size needs to be larger than cross_thickness")

    stim = cross(
        visual_size=cross_size,
        ppd=ppd,
        cross_arm_ratios=cross_arm_ratios,
        cross_thickness=cross_thickness,
        intensity_background=intensity_background,
        intensity_cross=intensity_target,
        )
    
    img, mask = stim["img"], stim["mask"]
    img = pad_to_visual_size(img, visual_size=visual_size, ppd=ppd, pad_value=intensity_background)
    mask = pad_to_visual_size(mask, visual_size=visual_size, ppd=ppd, pad_value=0)

    cheight, cwidth = degrees_to_pixels(covers_size, ppd)
    cx = degrees_to_pixels(covers_x, ppd)
    cy = degrees_to_pixels(covers_y, ppd)

    for i in range(len(covers_x)):
        img[cy[i] : cy[i] + cheight, cx[i] : cx[i] + cwidth] = intensity_covers
        mask[cy[i] : cy[i] + cheight, cx[i] : cx[i] + cwidth] = 0
        if cy[i] + cheight > visual_size[0] * ppd or cx[i] + cwidth > visual_size[1] * ppd:
            raise ValueError("Covers do not fully fit into stimulus")
    
    stim["img"] = img
    stim["mask"] = mask.astype(int)
    stim["target_size"] = stim["visual_size"]
    stim["intensity_target"] = stim["intensity_cross"]
    stim["covers_size"] = covers_size
    stim["covers_x"] = covers_x
    stim["covers_y"] = covers_y
    stim["intensity_covers"] = intensity_covers
    stim["visual_size"] = visual_size
    stim["shape"] = img.shape
    return stim


def todorovic_cross(
    visual_size=None,
    ppd=None,
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
    visual_size : float or (float, float)
        size of the stimulus in degrees of visual angle (height, width)
    ppd : int
        pixels per degree (visual angle)
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
    -------
    A stimulus dictionary with the stimulus ['img'] and target mask ['mask']

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
    if isinstance(visual_size, (float, int)):
        visual_size = (visual_size, visual_size)
    if isinstance(covers_size, (float, int)):
        covers_size = (covers_size, covers_size)

    # Calculate placement of covers for generalized function:
    cy, cx = np.floor(np.array(visual_size) * ppd / 2) / ppd
    ct = np.ceil(cross_thickness * ppd)
    ct = (ct + (ct % 2)) / ppd
    ct_half = ct / 2

    y1 = cy - ct_half - covers_size[0]
    x1 = cx - ct_half - covers_size[1]
    y2 = cy + ct_half
    x2 = cx + ct_half

    stim = todorovic_cross_generalized(
        visual_size=visual_size,
        ppd=ppd,
        cross_size=cross_size,
        cross_arm_ratios=1.,
        cross_thickness=ct,
        covers_size=covers_size,
        covers_x=(x1, x2, x2, x1),
        covers_y=(y1, y2, y1, y2),
        intensity_background=intensity_background,
        intensity_target=intensity_target,
        intensity_covers=intensity_covers,
    )
    return stim


if __name__ == "__main__":
    from stimuli.utils import plot_stimuli
    
    params = {
        "visual_size": 10,
        "ppd": 10,
        }

    stims = {
        "Todorovic rectangle": todorovic_rectangle(**params, target_size=4, covers_size=2, covers_offset=2),
        "Todorovic rectangle, flex": todorovic_rectangle_generalized(**params,
                                                                     target_size=4, 
                                                                     target_position=3,
                                                                     covers_size=2,
                                                                     covers_x=(2, 6),
                                                                     covers_y=(2, 6)),
        "Todorovic cross": todorovic_cross(**params, cross_size=4, cross_thickness=2, covers_size=2),
        "Todorovic cross, flex": todorovic_cross_generalized(**params,
                                                             cross_size=4,
                                                             cross_arm_ratios=1.,
                                                             cross_thickness=2,
                                                             covers_size=2,
                                                             covers_x=(2, 6),
                                                             covers_y=(2, 6)),
        }
    plot_stimuli(stims, mask=True, save=None)
