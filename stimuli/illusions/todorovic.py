import numpy as np

from stimuli.components import cross, rectangle
from stimuli.utils import degrees_to_pixels, pad_to_shape


def todorovic_rectangle_generalized(
    visual_size=10,
    ppd=10,
    target_size=(4.0, 4.0),
    target_pos=(3.0, 3.0),
    covers_size=(2.0, 2.0),
    covers_posx=(2.0, 6.0, 2.0, 6.0),
    covers_posy=(2.0, 6.0, 6.0, 2.0),
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
    target_pos : float or (float, float)
        coordinates where to place the target
    covers_size : float or (float, float)
        size of the covers in degrees of visual angle (height, width)
    covers_posx : tuple of floats
        x coordinates of covers; as many covers as there are coordinates
    covers_posy : tuple of floats
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
    """

    if isinstance(visual_size, (float, int)):
        visual_size = (visual_size, visual_size)
    if isinstance(covers_size, (float, int)):
        covers_size = (covers_size, covers_size)
    if len(covers_posx) != len(covers_posy):
        raise ValueError("Need as many x- as y-coordinates")

    # Create image with square
    img = rectangle(
        ppd, visual_size, target_size, target_pos, intensity_background, intensity_target
    )

    # Add covers
    cheight, cwidth = degrees_to_pixels(covers_size, ppd)
    cposx = degrees_to_pixels(covers_posx, ppd)
    cposy = degrees_to_pixels(covers_posy, ppd)

    if np.max(cposx) < np.min(cposx) + cwidth or np.max(cposy) < np.min(cposy) + cheight:
        raise ValueError("Covers overlap")

    for i in range(len(covers_posx)):
        img[cposy[i] : cposy[i] + cheight, cposx[i] : cposx[i] + cwidth] = intensity_covers
        if cposy[i] + cheight > visual_size[0] * ppd or cposx[i] + cwidth > visual_size[1] * ppd:
            raise ValueError("Covers do not fully fit into stimulus")

    mask = np.copy(img)
    mask[mask == intensity_background] = 0
    mask[mask == intensity_covers] = 0
    mask[mask == intensity_target] = 1

    params = {
        "shape": img.shape,
        "visual_size": np.array(img.shape) / ppd,
        "ppd": ppd,
        "target_size": target_size,
        "target_pos": target_pos,
        "covers_size": covers_size,
        "covers_posx": covers_posx,
        "covers_posy": covers_posy,
        "intensity_background": intensity_background,
        "intensity_target": intensity_target,
        "intensity_covers": intensity_covers,
    }

    return {"img": img, "mask": mask, **params}


def todorovic_rectangle(
    visual_size=(10, 10),
    ppd=10,
    target_size=(4, 4),
    covers_size=(3.0, 3.0),
    covers_offset=(2.0, 2.0),
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
    """
    if isinstance(visual_size, (float, int)):
        visual_size = (visual_size, visual_size)
    if isinstance(target_size, (float, int)):
        target_size = (target_size, target_size)
    if isinstance(covers_size, (float, int)):
        covers_size = (covers_size, covers_size)
    if isinstance(covers_offset, (float, int)):
        covers_offset = (covers_offset, covers_offset)

    # Calculate placement of target and covers for generalized function:
    tpos = np.array(visual_size) / 2 - np.array(target_size) / 2
    y1 = tpos[0] + target_size[0] / 2 - covers_offset[0] - covers_size[0] / 2
    x1 = tpos[1] + target_size[1] / 2 - covers_offset[1] - covers_size[1] / 2
    y2 = tpos[0] + target_size[0] / 2 + covers_offset[0] - covers_size[0] / 2
    x2 = tpos[1] + target_size[1] / 2 + covers_offset[1] - covers_size[1] / 2

    stim = todorovic_rectangle_generalized(
        visual_size=visual_size,
        ppd=ppd,
        target_size=target_size,
        target_pos=tpos,
        covers_size=covers_size,
        covers_posx=(x1, x2, x2, x1),
        covers_posy=(y1, y2, y1, y2),
        intensity_background=intensity_background,
        intensity_target=intensity_target,
        intensity_covers=intensity_covers,
    )
    return stim


def todorovic_cross_generalized(
    visual_size=(12.0, 12.0),
    ppd=10,
    target_arms_size=(4.0, 4.0, 4.0, 4.0),
    target_thickness=2.0,
    covers_size=2.0,
    covers_posx=(3.0, 7.0, 3.0, 7.0),
    covers_posy=(3.0, 7.0, 7.0, 3.0),
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
    target_arms_size : (float, float, float)
        size of the target's arms in degrees visual angle in form (top, bottom, left, right)
    target_thickness : float
        thickness of target cross
    covers_size : float or (float, float)
        size of covers in degrees visual angle (height, width)
    covers_posx : tuple of floats
        x coordinates of covers; as many covers as there are coordinates
    covers_posy : tuple of floats
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
    """

    if isinstance(visual_size, (float, int)):
        visual_size = (visual_size, visual_size)
    if isinstance(covers_size, (float, int)):
        covers_size = (covers_size, covers_size)
    if len(covers_posx) != len(covers_posy):
        raise ValueError("Need as many x- as y-coordinates")

    img = cross(ppd, target_arms_size, target_thickness, intensity_background, intensity_target)
    if img.shape[0] > visual_size[0] * ppd or img.shape[1] > visual_size[1] * ppd:
        raise ValueError("your cross does not fit in requested stimulus size")
    img = pad_to_shape(img, np.array(visual_size) * ppd, pad_value=intensity_background)

    cheight, cwidth = degrees_to_pixels(covers_size, ppd)
    cposx = degrees_to_pixels(covers_posx, ppd)
    cposy = degrees_to_pixels(covers_posy, ppd)

    for i in range(len(covers_posx)):
        img[cposy[i] : cposy[i] + cheight, cposx[i] : cposx[i] + cwidth] = intensity_covers
        if cposy[i] + cheight > visual_size[0] * ppd or cposx[i] + cwidth > visual_size[1] * ppd:
            raise ValueError("Covers do not fully fit into stimulus")

    mask = np.copy(img)
    mask[mask == intensity_background] = 0
    mask[mask == intensity_covers] = 0
    mask[mask == intensity_target] = 1

    params = {
        "shape": img.shape,
        "visual_size": np.array(img.shape) / ppd,
        "ppd": ppd,
        "target_arms_size": target_arms_size,
        "target_thickness": target_thickness,
        "covers_size": covers_size,
        "covers_posx": covers_posx,
        "covers_posy": covers_posy,
        "intensity_background": intensity_background,
        "intensity_target": intensity_target,
        "intensity_covers": intensity_covers,
    }

    return {"img": img, "mask": mask, **params}


def todorovic_cross(
    visual_size=(10, 10),
    ppd=32,
    target_arms_size=3.0,
    target_thickness=1.0,
    covers_size=3.2,
    intensity_background=1.0,
    intensity_target=0.5,
    intensity_covers=0.0,
):
    """
    Todorovic's illusion with cross target and four rectangular covers added at inner cross corners

    Parameters
    ----------
    visual_size : float or (float, float)
        size of the stimulus in degrees of visual angle (height, width)
    ppd : int
        pixels per degree (visual angle)
    target_arms_size : float or (float, float)
        size of target arms in degrees of visual angle (top/bottom, right/left)
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
    """
    if isinstance(visual_size, (float, int)):
        visual_size = (visual_size, visual_size)
    if isinstance(target_arms_size, (float, int)):
        target_arms_size = (target_arms_size, target_arms_size)
    if isinstance(covers_size, (float, int)):
        covers_size = (covers_size, covers_size)
    if len(target_arms_size) != 2:
        raise ValueError("target_arms_size should be single number of (float, float)")

    # Calculate placement of target and covers for generalized function:
    center = np.array(visual_size) / 2
    t2 = np.ceil(target_thickness * ppd / 2) / ppd * 2
    y1 = center[0] - t2 / 2 - covers_size[0]
    x1 = center[1] - t2 / 2 - covers_size[1]
    y2 = center[0] + t2 / 2
    x2 = center[1] + t2 / 2

    arm_size = (target_arms_size[0], target_arms_size[0], target_arms_size[1], target_arms_size[1])
    stim = todorovic_cross_generalized(
        visual_size=visual_size,
        ppd=ppd,
        target_arms_size=arm_size,
        target_thickness=t2,
        covers_size=covers_size,
        covers_posx=(x1, x2, x2, x1),
        covers_posy=(y1, y2, y1, y2),
        intensity_background=intensity_background,
        intensity_target=intensity_target,
        intensity_covers=intensity_covers,
    )

    return stim


if __name__ == "__main__":
    import matplotlib.pyplot as plt

    from stimuli.utils import plot_stimuli

    stims = {
        "Todorovic rectangle": todorovic_rectangle(),
        "Todorovic rectangle, flex": todorovic_rectangle_generalized(),
        "Todorovic cross": todorovic_cross(),
        "Todorovic cross, flex": todorovic_cross_generalized(),
    }
    plot_stimuli(stims)
    plt.show()
