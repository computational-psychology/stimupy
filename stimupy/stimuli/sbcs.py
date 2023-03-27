import numpy as np

from stimupy.components.shapes import disc, rectangle
from stimupy.utils import pad_by_visual_size, pad_to_shape, resolution, stack_dicts

__all__ = [
    "generalized",
    "basic",
    "two_sided",
    "with_dots",
    "with_dots_two_sided",
    "dotted",
    "dotted_two_sided",
]


def generalized(
    visual_size=None,
    ppd=None,
    shape=None,
    target_size=None,
    target_position=None,
    intensity_background=0.0,
    intensity_target=0.5,
):
    """Simultaneous contrast stimulus with free target placement.

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
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for the target (key: "target_mask"),
        and additional keys containing stimulus parameters

    References
    ----------
    Chevreul, M. (1855).
        The principle of harmony and contrast of colors.
    """
    if target_size is None:
        raise ValueError("generalized() missing argument 'target_size' which is not 'None'")

    stim = rectangle(
        visual_size=visual_size,
        ppd=ppd,
        shape=shape,
        rectangle_size=target_size,
        rectangle_position=target_position,
        intensity_background=intensity_background,
        intensity_rectangle=intensity_target,
    )

    stim["target_mask"] = stim["rectangle_mask"]
    stim["target_size"] = stim["rectangle_size"]
    stim["target_position"] = stim["rectangle_position"]
    stim["intensity_target"] = stim["intensity_rectangle"]
    del (
        stim["rectangle_mask"],
        stim["rectangle_size"],
        stim["rectangle_position"],
        stim["intensity_rectangle"],
    )
    return stim


def basic(
    visual_size=None,
    ppd=None,
    shape=None,
    target_size=None,
    intensity_background=0.0,
    intensity_target=0.5,
):
    """Simultaneous contrast stimulus with central target.

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
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for the target (key: "target_mask"),
        and additional keys containing stimulus parameters

    References
    ----------
    Chevreul, M. (1855).
        The principle of harmony and contrast of colors.
    """
    if target_size is None:
        raise ValueError("basic() missing argument 'target_size' which is not 'None'")

    stim = generalized(
        visual_size=visual_size,
        ppd=ppd,
        target_size=target_size,
        target_position=None,
        intensity_background=intensity_background,
        intensity_target=intensity_target,
    )
    return stim


def two_sided(
    visual_size=None,
    ppd=None,
    shape=None,
    target_size=None,
    intensity_backgrounds=(0.0, 1.0),
    intensity_target=0.5,
):
    """Two-sided simultaneous contrast display with central targets.

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
    intensity_background : Sequence[Number, Number]
        intensity values for backgrounds
    intensity_target : float
        intensity value for target

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for the target (key: "target_mask"),
        and additional keys containing stimulus parameters

    References
    ----------
    Chevreul, M. (1855).
        The principle of harmony and contrast of colors.
    """
    if target_size is None:
        raise ValueError("two_sided() missing argument 'target_size' which is not 'None'")

    # Resolve resolution
    shape, visual_size, ppd = resolution.resolve(shape=shape, visual_size=visual_size, ppd=ppd)

    stim1 = basic(
        visual_size=(visual_size[0], visual_size[1] / 2),
        ppd=ppd,
        target_size=target_size,
        intensity_background=intensity_backgrounds[0],
        intensity_target=intensity_target,
    )

    stim2 = basic(
        visual_size=(visual_size[0], visual_size[1] / 2),
        ppd=ppd,
        target_size=target_size,
        intensity_background=intensity_backgrounds[1],
        intensity_target=intensity_target,
    )

    stim = stack_dicts(stim1, stim2)
    del stim["intensity_background"]
    del stim["target_position"]
    stim["intensity_backgrounds"] = intensity_backgrounds
    stim["target_positions"] = (stim1["target_position"], stim2["target_position"])
    stim["shape"] = shape
    stim["visual_size"] = visual_size
    return stim


def with_dots(
    visual_size=None,
    ppd=None,
    shape=None,
    n_dots=None,
    dot_radius=None,
    distance=None,
    target_shape=None,
    intensity_background=0.0,
    intensity_dots=1.0,
    intensity_target=0.5,
):
    """Simultaneous contrast stimulus with dots

    Parameters
    ----------
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of grating, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of grating, in pixels
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
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for the target (key: "target_mask"),
        and additional keys containing stimulus parameters

    References
    ----------
    Bressan, P., & Kramer, P. (2008).
        Gating of remote effects on lightness.
        Journal of Vision, 8(2), 16-16.
        https://doi.org/10.1167/8.2.16
    """
    if n_dots is None:
        raise ValueError("with_dots() missing argument 'n_dots' which is not 'None'")
    if dot_radius is None:
        raise ValueError("with_dots() missing argument 'dot_radius' which is not 'None'")
    if distance is None:
        raise ValueError("with_dots() missing argument 'distance' which is not 'None'")
    if target_shape is None:
        raise ValueError("with_dots() missing argument 'target_shape' which is not 'None'")

    # n_dots = number of dots vertical, horizontal, analogous to degrees
    n_dots = resolution.validate_visual_size(n_dots)

    if shape is None and visual_size is None:
        visual_size = (
            n_dots[0] * dot_radius * 2 + n_dots[0] * distance,
            n_dots[1] * dot_radius * 2 + n_dots[1] * distance,
        )

    # Resolve resolution
    shape, visual_size, ppd = resolution.resolve(shape=shape, visual_size=visual_size, ppd=ppd)
    if len(np.unique(ppd)) > 1:
        raise ValueError("ppd should be equal in x and y direction")

    # target shape = is in number of dots
    target_shape = resolution.validate_visual_size(target_shape)

    # Figure out pixels_per_dot
    padding = (distance / 2.0,)
    patch = disc(
        radius=dot_radius,
        ppd=ppd,
        intensity_background=0.0,
        intensity_disc=1,
    )["img"]
    patch = pad_by_visual_size(img=patch, padding=padding, ppd=ppd, pad_value=0.0)
    pixels_per_dot = patch.shape
    patch = np.tile(patch, (int(n_dots[0]), int(n_dots[1])))

    # Target shape = target n_dots * pixels_per_dot
    rect_shape = resolution.shape_from_visual_size_ppd(
        visual_size=target_shape, ppd=pixels_per_dot
    )
    rect_visual_size = resolution.visual_size_from_shape_ppd(shape=rect_shape, ppd=ppd)

    try:
        patch = pad_to_shape(patch, shape, 0)
    except Exception:
        raise ValueError("visual_size or shape_argument are too small. Advice: set to None")

    # Create the sbc in the background:
    img_shape = patch.shape

    sbc = rectangle(
        shape=img_shape,
        ppd=ppd,
        rectangle_size=rect_visual_size,
        intensity_background=intensity_background,
        intensity_rectangle=intensity_target,
    )

    img = np.where(patch == 1, intensity_dots, sbc["img"])
    mask = np.where(patch == 1, 0, sbc["rectangle_mask"])

    stim = {
        "img": img,
        "target_mask": mask.astype(int),
        "shape": shape,
        "visual_size": visual_size,
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


def with_dots_two_sided(
    visual_size=None,
    ppd=None,
    shape=None,
    n_dots=None,
    dot_radius=None,
    distance=None,
    target_shape=None,
    intensity_backgrounds=(0.0, 1.0),
    intensity_dots=(1.0, 0.0),
    intensity_target=0.5,
):
    """Two-sided simultaneous contrast stimulus with dots

    Parameters
    ----------
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of grating, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of grating, in pixels
    n_dots : int or (int, int)
        stimulus size defined as the number of dots in y and x-directions
    dot_radius : float
        radius of dots
    distance : float
        distance between dots in degree visual angle
    target_shape : int or (int, int)
        target shape defined as the number of dots that fit into the target
    intensity_backgrounds : Sequence[Number, Number]
        intensity values for background
    intensity_dots : Sequence[Number, Number]
        intensity values for dots
    intensity_target : float
        intensity value for target

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for the target (key: "target_mask"),
        and additional keys containing stimulus parameters

    References
    ----------
    Bressan, P., & Kramer, P. (2008).
        Gating of remote effects on lightness.
        Journal of Vision, 8(2), 16-16.
        https://doi.org/10.1167/8.2.16
    """

    # Resolve resolution
    try:
        shape, visual_size, ppd = resolution.resolve(shape=shape, visual_size=visual_size, ppd=ppd)
        visual_size_ = (visual_size[0], visual_size[1] / 2)
    except resolution.TooManyUnknownsError:
        visual_size_ = None

    stim1 = with_dots(
        visual_size=visual_size_,
        ppd=ppd,
        n_dots=n_dots,
        dot_radius=dot_radius,
        distance=distance,
        target_shape=target_shape,
        intensity_background=intensity_backgrounds[0],
        intensity_dots=intensity_dots[0],
        intensity_target=intensity_target,
    )

    stim2 = with_dots(
        visual_size=visual_size_,
        ppd=ppd,
        n_dots=n_dots,
        dot_radius=dot_radius,
        distance=distance,
        target_shape=target_shape,
        intensity_background=intensity_backgrounds[1],
        intensity_dots=intensity_dots[1],
        intensity_target=intensity_target,
    )

    stim = stack_dicts(stim1, stim2)
    del stim["intensity_background"]
    stim["intensity_backgrounds"] = intensity_backgrounds
    stim["intensity_dots"] = intensity_dots
    return stim


def dotted(
    visual_size=None,
    ppd=None,
    shape=None,
    n_dots=None,
    dot_radius=None,
    distance=None,
    target_shape=None,
    intensity_background=0.0,
    intensity_dots=1.0,
    intensity_target=0.5,
):
    """Dotted simultaneous contrast

    Parameters
    ----------
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of grating, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of grating, in pixels
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
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for the targets (key: "target_mask"),
        and additional keys containing stimulus parameters

    References
    ----------
    Bressan, P., & Kramer, P. (2008).
        Gating of remote effects on lightness.
        Journal of Vision, 8(2), 16-16.
        https://doi.org/10.1167/8.2.16
    """
    if n_dots is None:
        raise ValueError("dotted() missing argument 'n_dots' which is not 'None'")
    if dot_radius is None:
        raise ValueError("dotted() missing argument 'dot_radius' which is not 'None'")
    if distance is None:
        raise ValueError("dotted() missing argument 'distance' which is not 'None'")
    if target_shape is None:
        raise ValueError("dotted() missing argument 'target_shape' which is not 'None'")

    # n_dots = number of dots vertical, horizontal, analogous to degrees
    n_dots = resolution.validate_visual_size(n_dots)

    if shape is None and visual_size is None:
        visual_size = (
            n_dots[0] * dot_radius * 2 + n_dots[0] * distance,
            n_dots[1] * dot_radius * 2 + n_dots[1] * distance,
        )

    # Resolve resolution
    shape, visual_size, ppd = resolution.resolve(shape=shape, visual_size=visual_size, ppd=ppd)
    if len(np.unique(ppd)) > 1:
        raise ValueError("ppd should be equal in x and y direction")

    # target shape = is in number of dots
    target_shape = resolution.validate_visual_size(target_shape)

    # Figure out pixels_per_dot
    padding = (distance / 2.0,)
    patch = disc(
        radius=dot_radius,
        ppd=ppd,
        intensity_background=0.0,
        intensity_disc=1.0,
    )["img"]
    patch = pad_by_visual_size(img=patch, padding=padding, ppd=ppd, pad_value=0.0)
    pixels_per_dot = patch.shape
    patch = np.tile(patch, (int(n_dots[0]), int(n_dots[1])))

    # Target shape = target n_dots * pixels_per_dot
    rect_shape = resolution.shape_from_visual_size_ppd(
        visual_size=target_shape, ppd=pixels_per_dot
    )
    rect_visual_size = resolution.visual_size_from_shape_ppd(shape=rect_shape, ppd=ppd)

    try:
        patch = pad_to_shape(patch, shape, 0)
    except Exception:
        raise ValueError("visual_size or shape_argument are too small. Advice: set to None")

    # Create the sbc and img:
    img_shape = patch.shape
    sbc = rectangle(
        shape=img_shape,
        ppd=ppd,
        rectangle_size=rect_visual_size,
        intensity_background=intensity_background,
        intensity_rectangle=intensity_target,
    )

    img = np.where(patch, intensity_dots, intensity_background)
    img = np.where(patch + sbc["rectangle_mask"] == 2, intensity_target, img)
    mask = np.where(patch + sbc["rectangle_mask"] == 2, 1, 0)

    stim = {
        "img": img,
        "target_mask": mask.astype(int),
        "shape": shape,
        "visual_size": visual_size,
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


def dotted_two_sided(
    visual_size=None,
    ppd=None,
    shape=None,
    n_dots=None,
    dot_radius=None,
    distance=None,
    target_shape=None,
    intensity_backgrounds=(0.0, 1.0),
    intensity_dots=(1.0, 0.0),
    intensity_target=0.5,
):
    """Two-sided dotted simultaneous contrast stimulus

    Parameters
    ----------
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of grating, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of grating, in pixels
    n_dots : int or (int, int)
        stimulus size defined as the number of dots in y and x-directions
    dot_radius : float
        radius of dots
    distance : float
        distance between dots in degree visual angle
    target_shape : int or (int, int)
        target shape defined as the number of dots that fit into the target
    intensity_background : equence[Number, Number]
        intensity values for background
    intensity_dots : equence[Number, Number]
        intensity values for dots
    intensity_target : float
        intensity value for target

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for the targets (key: "target_mask"),
        and additional keys containing stimulus parameters

    References
    ----------
    Bressan, P., & Kramer, P. (2008).
        Gating of remote effects on lightness.
        Journal of Vision, 8(2), 16-16.
        https://doi.org/10.1167/8.2.16
    """

    # Resolve resolution
    try:
        shape, visual_size, ppd = resolution.resolve(shape=shape, visual_size=visual_size, ppd=ppd)
        visual_size_ = (visual_size[0], visual_size[1] / 2)
    except resolution.TooManyUnknownsError:
        visual_size_ = None

    stim1 = dotted(
        visual_size=visual_size_,
        ppd=ppd,
        n_dots=n_dots,
        dot_radius=dot_radius,
        distance=distance,
        target_shape=target_shape,
        intensity_background=intensity_backgrounds[0],
        intensity_dots=intensity_dots[0],
        intensity_target=intensity_target,
    )

    stim2 = dotted(
        visual_size=visual_size_,
        ppd=ppd,
        n_dots=n_dots,
        dot_radius=dot_radius,
        distance=distance,
        target_shape=target_shape,
        intensity_background=intensity_backgrounds[1],
        intensity_dots=intensity_dots[1],
        intensity_target=intensity_target,
    )

    stim = stack_dicts(stim1, stim2)
    del stim["intensity_background"]
    stim["intensity_backgrounds"] = intensity_backgrounds
    stim["intensity_dots"] = intensity_dots
    return stim


def overview(**kwargs):
    """Generate example stimuli from this module

    Returns
    -------
    stims : dict
        dict with all stimuli containing individual stimulus dicts.
    """
    default_params = {
        "ppd": 30,
    }
    default_params.update(kwargs)

    # fmt: off
    stimuli = {
        "sbc_generalized": generalized(**default_params, visual_size=10, target_size=(3,4), target_position=(1, 2)),
        "sbc_basic": basic(**default_params, visual_size=10, target_size=3),
        "sbc_2sided": two_sided(**default_params, visual_size=10, target_size=2),
        "sbc_with_dots": with_dots(**default_params, n_dots=5, dot_radius=2, distance=0.5, target_shape=3),
        "sbc_with_dots_2sided": with_dots_two_sided(**default_params, n_dots=5, dot_radius=2, distance=0.5, target_shape=3),
        "sbc_dotted": dotted(**default_params, n_dots=5, dot_radius=2, distance=0.5, target_shape=3),
        "sbc_dotted_2sided": dotted_two_sided(**default_params, n_dots=5, dot_radius=2, distance=0.5, target_shape=3),
    }
    # fmt: on

    return stimuli


if __name__ == "__main__":
    from stimupy.utils import plot_stimuli

    stims = overview()
    plot_stimuli(stims, mask=True, save=None)
