import numpy as np

from stimuli.components import disc, rectangle
from stimuli.utils import pad_by_visual_size, resolution


def simultaneous_contrast_generalized(
    visual_size=(2.0, 2.0),
    ppd=10,
    target_size=(2.0, 2.0),
    target_pos=(1.0, 1.0),
    intensity_background=0.0,
    intensity_target=0.5,
):
    """
    Simultaneous contrast stimulus with free target placement.

    Parameters
    ----------
    visual_size : float or (float, float)
        size of the stimulus in degrees of visual angle (height, width)
    ppd : int
        pixels per degree (visual angle)
    target_size : float or (float, float)
        size of the target in degree visual angle (height, width)
    target_pos : float or (float, float)
        size of the target in degree visual angle (height, width)
    intensity_background : float
        intensity value for background
    intensity_target : float
        intensity value for target

    Returns
    -------
    A stimulus dictionary with the stimulus ['img'] and target mask ['mask']
    """

    if isinstance(visual_size, (float, int)):
        visual_size = (visual_size, visual_size)
    if isinstance(target_size, (float, int)):
        target_size = (target_size, target_size)
    if isinstance(target_pos, (float, int)):
        target_pos = (target_pos, target_pos)

    if target_size[0] > visual_size[0] or target_size[1] > visual_size[1]:
        raise ValueError("Requested target is larger than stimulus")
    if (
        target_size[0] + target_pos[0] > visual_size[0]
        or target_size[1] + target_pos[1] > visual_size[1]
    ):
        raise ValueError("Target does not fully fit into the stimulus")

    img = rectangle(
        ppd, visual_size, target_size, target_pos, intensity_background, intensity_target
    )
    mask = rectangle(ppd, visual_size, target_size, target_pos, 0, 1)

    params = {
        "shape": img.shape,
        "visual_size": np.array(img.shape) / ppd,
        "ppd": ppd,
        "target_size": target_size,
        "target_pos": target_pos,
        "intensity_background": intensity_background,
        "intensity_target": intensity_target,
    }

    return {"img": img, "mask": mask, **params}


def simultaneous_contrast(
    visual_size=(2.0, 3.0),
    ppd=10,
    target_size=(1.0, 0.5),
    intensity_background=0.0,
    intensity_target=0.5,
):
    """
    Simultaneous contrast stimulus with central target.

    Parameters
    ----------
    visual_size : float or (float, float)
        size of the stimulus in degrees of visual angle (height, width)
    ppd : int
        pixels per degree (visual angle)
    target_size : float or (float, float)
        size of the target in degree visual angle (height, width)
    intensity_background : float
        intensity value for background
    intensity_target : float
        intensity value for target

    Returns
    -------
    A stimulus dictionary with the stimulus ['img'] and target mask ['mask']
    """
    if isinstance(visual_size, (float, int)):
        visual_size = (visual_size, visual_size)
    if isinstance(target_size, (float, int)):
        target_size = (target_size, target_size)

    # Rectangle should be placed centrally
    t_pos = (
        visual_size[0] / 2.0 - target_size[0] / 2.0,
        visual_size[1] / 2.0 - target_size[1] / 2.0,
    )
    stim = simultaneous_contrast_generalized(
        visual_size, ppd, target_size, t_pos, intensity_background, intensity_target
    )
    return stim


def sbc_with_dots(
    ppd=10,
    n_dots=(8, 9),
    dot_radius=3.0,
    distance=1.0,
    target_shape=(4, 3),
    intensity_background=0.0,
    intensity_dots=1.0,
    intensity_target=0.5,
):
    """
    Simultaneous contrast stimulus with dots

    Parameters
    ----------
    ppd : int
        pixels per degree (visual angle)
    n_dots : int or (int, int)
        stimulus size defined as the number of dots in y and x-directions
    dot_radius : float
        radius of dots
    distance : float
        distance between dots in degree visual angle
    target_shape : int or (int, int)
        target shape defined as the number of dots that fit into the target
    intensity_background : float
        intensity value for background
    intensity_dots : float
        intensity value for dots
    intensity_target : float
        intensity value for target

    Returns
    -------
    A stimulus dictionary with the stimulus ['img'] and target mask ['mask']
    """

    # n_dots = number of dots vertical, horizontal, analogous to degrees
    n_dots = resolution.validate_visual_size(n_dots)

    # target shape = is in number of dots
    target_shape = resolution.validate_visual_size(target_shape)

    # Figure out pixels_per_dot
    padding = (distance / 2.0,)
    patch = disc(ppd, dot_radius, intensity_background=0.0, intensity_disc=intensity_dots)
    patch = pad_by_visual_size(img=patch, padding=padding, ppd=ppd, pad_value=0.0)
    pixels_per_dot = patch.shape

    # Img total shape = n_dots * pixels_per_dot
    img_shape = resolution.shape_from_visual_size_ppd(visual_size=n_dots, ppd=pixels_per_dot)
    img_visual_size = resolution.visual_size_from_shape_ppd(shape=img_shape, ppd=ppd)

    # Target shape = target n_dots * pixels_per_dot
    rect_shape = resolution.shape_from_visual_size_ppd(
        visual_size=target_shape, ppd=pixels_per_dot
    )
    rect_visual_size = resolution.visual_size_from_shape_ppd(shape=rect_shape, ppd=ppd)

    # Create the sbc in the background:
    tposy = (img_visual_size.height - rect_visual_size.height) / 2.0
    tposx = (img_visual_size.width - rect_visual_size.width) / 2.0
    img = rectangle(
        ppd,
        im_size=img_visual_size,
        rect_size=rect_visual_size,
        rect_pos=(tposy, tposx),
        intensity_background=intensity_background,
        intensity_rectangle=intensity_target,
    )
    mask = np.zeros(img.shape)
    mask[img == intensity_target] = 1

    patch = np.tile(patch, (int(n_dots[0]), int(n_dots[1])))
    indices_dots = np.where((patch != 0))
    img[indices_dots] = intensity_dots
    mask[indices_dots] = 0

    params = {
        "shape": img.shape,
        "visual_size": np.array(img.shape) / ppd,
        "ppd": ppd,
        "n_dots": n_dots,
        "dot_radius": dot_radius,
        "distance": distance,
        "target_shape": target_shape,
        "intensity_background": intensity_background,
        "intensity_dots": intensity_dots,
        "intensity_target": intensity_target,
    }

    return {"img": img, "mask": mask, **params}


def dotted_sbc(
    ppd=10,
    n_dots=(8, 9),
    dot_radius=3.0,
    distance=1.0,
    target_shape=(4, 3),
    intensity_background=0.0,
    intensity_dots=1.0,
    intensity_target=0.5,
):
    """
    Simultaneous contrast stimulus with dots

    Parameters
    ----------
    ppd : int
        pixels per degree (visual angle)
    n_dots : int or (int, int)
        stimulus size defined as the number of dots in y and x-directions
    dot_radius : float
        radius of dots
    distance : float
        distance between dots in degree visual angle
    target_shape : int or (int, int)
        target shape defined as the number of dots that fit into the target
    intensity_background : float
        intensity value for background
    intensity_dots : float
        intensity value for dots
    intensity_target : float
        intensity value for target

    Returns
    -------
    A stimulus dictionary with the stimulus ['img'] and target mask ['mask']
    """

    # n_dots = number of dots vertical, horizontal, analogous to degrees
    n_dots = resolution.validate_visual_size(n_dots)

    # target shape = is in number of dots
    target_shape = resolution.validate_visual_size(target_shape)

    # Figure out pixels_per_dot
    padding = (distance / 2.0,)
    patch = disc(ppd, dot_radius, intensity_background=0.0, intensity_disc=intensity_dots)
    patch = pad_by_visual_size(img=patch, padding=padding, ppd=ppd, pad_value=0.0)
    pixels_per_dot = patch.shape

    # Img total shape = n_dots * pixels_per_dot
    img_shape = resolution.shape_from_visual_size_ppd(visual_size=n_dots, ppd=pixels_per_dot)
    img_visual_size = resolution.visual_size_from_shape_ppd(shape=img_shape, ppd=ppd)

    # Target shape = target n_dots * pixels_per_dot
    rect_shape = resolution.shape_from_visual_size_ppd(
        visual_size=target_shape, ppd=pixels_per_dot
    )
    rect_visual_size = resolution.visual_size_from_shape_ppd(shape=rect_shape, ppd=ppd)

    # Create the sbc and img:
    tposy = (img_visual_size.height - rect_visual_size.height) / 2.0
    tposx = (img_visual_size.width - rect_visual_size.width) / 2.0
    sbc = rectangle(
        ppd,
        im_size=img_visual_size,
        rect_size=rect_visual_size,
        rect_pos=(tposy, tposx),
        intensity_background=intensity_background,
        intensity_rectangle=intensity_target,
    )
    img = np.ones(sbc.shape) * intensity_background

    patch = np.tile(patch, (int(n_dots[0]), int(n_dots[1])))
    indices_dots_back = np.where((patch != 0) & (sbc == intensity_background))
    indices_dots_target = np.where((patch != 0) & (sbc == intensity_target))
    img[indices_dots_back] = intensity_dots
    img[indices_dots_target] = intensity_target
    mask = np.zeros(img.shape)
    mask[indices_dots_target] = 1

    params = {
        "shape": img.shape,
        "visual_size": np.array(img.shape) / ppd,
        "ppd": ppd,
        "n_dots": n_dots,
        "dot_radius": dot_radius,
        "distance": distance,
        "target_shape": target_shape,
        "intensity_background": intensity_background,
        "intensity_dots": intensity_dots,
        "intensity_target": intensity_target,
    }

    return {"img": img, "mask": mask, **params}


if __name__ == "__main__":
    import matplotlib.pyplot as plt

    from stimuli.utils import plot_stimuli

    stims = {
        "SBC": simultaneous_contrast(),
        "SBC with dots": sbc_with_dots(),
        "Dotted SBC": dotted_sbc(),
    }

    plot_stimuli(stims, mask=True)
    plt.show()
