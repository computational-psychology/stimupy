import numpy as np

from stimuli.components.circular import disc
from stimuli.components.shapes import rectangle
from stimuli.utils import pad_by_visual_size, resolution

__all__ = [
    "simultaneous_contrast_generalized",
    "simultaneous_contrast",
    "sbc_with_dots",
    "dotted_sbc",
]


def simultaneous_contrast_generalized(
    visual_size=None,
    ppd=None,
    shape=None,
    target_size=None,
    target_position=None,
    intensity_background=0.0,
    intensity_target=0.5,
):
    """
    Simultaneous contrast stimulus with free target placement.

    Parameters
    ----------
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of grating, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of grating, in pixels
    target_size : float or (float, float)
        size of the target in degree visual angle (height, width)
    target_position : float or (float, float)
        position of the target in degree visual angle (height, width);
        if None, place target centrally
    intensity_background : float
        intensity value for background
    intensity_target : float
        intensity value for target

    Returns
    -------
    A stimulus dictionary with the stimulus ['img'] and target mask ['mask']

    References
    ----------
    Chevreul, M. (1855). The principle of harmony and contrast of colors.
    """
    # Resolve resolution
    shape, visual_size, ppd = resolution.resolve(shape=shape, visual_size=visual_size, ppd=ppd)
    if len(np.unique(ppd)) > 1:
        raise ValueError("ppd should be equal in x and y direction")

    stim = rectangle(
        visual_size=visual_size,
        ppd=int(np.unique(ppd)),
        rectangle_size=target_size,
        rectangle_position=target_position,
        intensity_background=intensity_background,
        intensity_rectangle=intensity_target,
    )

    stim["visual_size"] = visual_size
    stim["ppd"] = ppd
    stim["shape"] = shape
    stim["target_size"] = stim["rectangle_size"]
    stim["target_position"] = stim["rectangle_position"]
    stim["intensity_target"] = stim["intensity_rectangle"]
    return stim


def simultaneous_contrast(
    visual_size=None,
    ppd=None,
    shape=None,
    target_size=None,
    intensity_background=0.0,
    intensity_target=0.5,
):
    """
    Simultaneous contrast stimulus with central target.

    Parameters
    ----------
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of grating, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of grating, in pixels
    target_size : float or (float, float)
        size of the target in degree visual angle (height, width)
    intensity_background : float
        intensity value for background
    intensity_target : float
        intensity value for target

    Returns
    -------
    A stimulus dictionary with the stimulus ['img'] and target mask ['mask']

    References
    ----------
    Chevreul, M. (1855). The principle of harmony and contrast of colors.
    """

    stim = simultaneous_contrast_generalized(
        visual_size=visual_size,
        ppd=ppd,
        target_size=target_size,
        target_position=None,
        intensity_background=intensity_background,
        intensity_target=intensity_target,
    )
    return stim


def sbc_with_dots(
    ppd=None,
    n_dots=None,
    dot_radius=None,
    distance=None,
    target_shape=None,
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

    References
    ----------
    Bressan, P., & Kramer, P. (2008). Gating of remote effects on lightness. Journal
        of Vision, 8(2), 16–16. https://doi.org/10.1167/8.2.16
    """

    # n_dots = number of dots vertical, horizontal, analogous to degrees
    n_dots = resolution.validate_visual_size(n_dots)

    # target shape = is in number of dots
    target_shape = resolution.validate_visual_size(target_shape)

    # Figure out pixels_per_dot
    padding = (distance / 2.0,)
    patch = disc(
        radius=dot_radius,
        ppd=ppd,
        intensity_background=0.0,
        intensity=intensity_dots,
    )["img"]
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
        visual_size=img_visual_size,
        ppd=ppd,
        rectangle_size=rect_visual_size,
        rectangle_position=(tposy, tposx),
        intensity_background=intensity_background,
        intensity_rectangle=intensity_target,
    )["img"]
    mask = np.zeros(img.shape)
    mask[img == intensity_target] = 1

    patch = np.tile(patch, (int(n_dots[0]), int(n_dots[1])))
    indices_dots = np.where((patch != 0))
    img[indices_dots] = intensity_dots
    mask[indices_dots] = 0

    stim = {
        "img": img,
        "mask": mask.astype(int),
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

    return stim


def dotted_sbc(
    ppd=None,
    n_dots=None,
    dot_radius=None,
    distance=None,
    target_shape=None,
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

    References
    ----------
    Bressan, P., & Kramer, P. (2008). Gating of remote effects on lightness. Journal
        of Vision, 8(2), 16–16. https://doi.org/10.1167/8.2.16
    """

    # n_dots = number of dots vertical, horizontal, analogous to degrees
    n_dots = resolution.validate_visual_size(n_dots)

    # target shape = is in number of dots
    target_shape = resolution.validate_visual_size(target_shape)

    # Figure out pixels_per_dot
    padding = (distance / 2.0,)
    patch = disc(
        radius=dot_radius,
        ppd=ppd,
        intensity_background=0.0,
        intensity=intensity_dots,
    )["img"]
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
        visual_size=img_visual_size,
        ppd=ppd,
        rectangle_size=rect_visual_size,
        rectangle_position=(tposy, tposx),
        intensity_background=intensity_background,
        intensity_rectangle=intensity_target,
    )["img"]
    img = np.ones(sbc.shape) * intensity_background

    patch = np.tile(patch, (int(n_dots[0]), int(n_dots[1])))
    indices_dots_back = np.where((patch != 0) & (sbc == intensity_background))
    indices_dots_target = np.where((patch != 0) & (sbc == intensity_target))
    img[indices_dots_back] = intensity_dots
    img[indices_dots_target] = intensity_target
    mask = np.zeros(img.shape)
    mask[indices_dots_target] = 1

    stim = {
        "img": img,
        "mask": mask.astype(int),
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

    return stim


if __name__ == "__main__":
    from stimuli.utils import plot_stimuli

    stims = {
        "SBC - generalized": simultaneous_contrast_generalized(
            visual_size=10, ppd=10, target_size=5, target_position=(0, 2)
        ),
        "SBC": simultaneous_contrast(visual_size=10, ppd=10, target_size=5),
        "SBC with dots": sbc_with_dots(
            ppd=20, n_dots=5, dot_radius=3, distance=0.5, target_shape=3
        ),
        "Dotted SBC": dotted_sbc(ppd=20, n_dots=5, dot_radius=3, distance=0.5, target_shape=3),
    }
    plot_stimuli(stims, mask=True, save=None)
