import numpy as np

from stimupy.components.shapes import disc, rectangle
from stimupy.stimuli import bullseyes
from stimupy.utils import make_two_sided, pad_by_visual_size, pad_to_shape, resolution

__all__ = [
    "generalized",
    "basic",
    "square",
    "circular",
    "with_dots",
    "dotted",
    "basic_two_sided",
    "square_two_sided",
    "circular_two_sided",
    "with_dots_two_sided",
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
    rotation=0.0,
):
    """Simultaneous contrast stimulus with free target placement

    Parameters
    ----------
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of image, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of image, in pixels
    target_size : float or (float, float)
        size [height, width] of the target, in degrees visual angle
    target_position : float or (float, float)
        position of the target in degree visual angle (height, width);
        if None, place target centrally
    intensity_background : float, optional
        intensity value for background, by default 0.0
    intensity_target : float, optional
        intensity value for target, by default 0.5
    rotation : float, optional
        rotation (in degrees), counterclockwise, by default 0.0 (horizontal)


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
        rotation=rotation,
    )

    stim["target_mask"] = stim.pop("rectangle_mask")
    stim["target_size"] = stim.pop("rectangle_size")
    stim["target_position"] = stim.pop("rectangle_position")
    stim["intensity_target"] = stim.pop("intensity_rectangle")

    return stim


def basic(
    visual_size=None,
    ppd=None,
    shape=None,
    target_size=None,
    intensity_background=0.0,
    intensity_target=0.5,
):
    """Simultaneous contrast stimulus with central target

    Parameters
    ----------
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of image, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of image, in pixels
    target_size : float or (float, float)
        size [height, width] of the target, in degrees visual angle
    intensity_background : float, optional
        intensity value for background, by default 0.0
    intensity_target : float, optional
        intensity value for target, by default 0.5

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
        shape=shape,
        target_size=target_size,
        target_position=None,
        intensity_background=intensity_background,
        intensity_target=intensity_target,
    )
    return stim


def square(
    target_radius,
    visual_size=None,
    ppd=None,
    shape=None,
    surround_radius=None,
    rotation=0.0,
    intensity_surround=0.0,
    intensity_background=0.5,
    intensity_target=0.5,
    origin="mean",
):
    """Simultaneous contrast stimulus with square target and surround field

    Parameters
    ----------
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of image, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of image, in pixels
    target_radius : float
        radius of target, in degrees visual angle
    surround_radius : float
        radius of surround context field, in degrees visual angle
    rotation : float, optional
        rotation (in degrees), counterclockwise, by default 0.0 (horizontal)
    intensity_surrond : float, optional
        intensity of surround context field, by default 0.0
    intensity_background : float, optional
        intensity value of background, by default 0.5
    intensity_target : float, or Sequence[float, ...], optional
        intensity value for each target, by default 0.5.
    origin : "corner", "mean" or "center"
        if "corner": set origin to upper left corner
        if "mean": set origin to hypothetical image center (default)
        if "center": set origin to real center (closest existing value to mean)

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for each frame (key: "target_mask"),
        and additional keys containing stimulus parameters
    """
    stim = bullseyes.rectangular_generalized(
        radii=(target_radius, surround_radius),
        visual_size=visual_size,
        ppd=ppd,
        shape=shape,
        rotation=rotation,
        intensity_frames=(0.0, intensity_surround),
        intensity_background=intensity_background,
        intensity_target=intensity_target,
        origin=origin,
    )
    return stim


def circular(
    target_radius,
    visual_size=None,
    ppd=None,
    shape=None,
    surround_radius=None,
    intensity_surround=0.0,
    intensity_background=0.5,
    intensity_target=0.5,
    origin="mean",
):
    """Simultaneous contrast stimulus with circular target and surround field

    Parameters
    ----------
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of image, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of image, in pixels
    target_radius : float
        radius of target, in degrees visual angle
    surround_radius : float
        radius of surround context field, in degrees visual angle
    rotation : float, optional
        rotation (in degrees), counterclockwise, by default 0.0 (horizontal)
    intensity_surrond : float, optional
        intensity of surround context field, by default 0.0
    intensity_background : float (optional)
        intensity value of background, by default 0.5
    intensity_target : float, or Sequence[float, ...], optional
        intensity value for each target, by default 0.5.
        Can specify as many intensities as number of target_indices;
        If fewer intensities are passed than target_indices, cycles through intensities
    origin : "corner", "mean" or "center"
        if "corner": set origin to upper left corner
        if "mean": set origin to hypothetical image center (default)
        if "center": set origin to real center (closest existing value to mean)

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for each frame (key: "target_mask"),
        and additional keys containing stimulus parameters
    """
    stim = bullseyes.circular_generalized(
        radii=(target_radius, surround_radius),
        visual_size=visual_size,
        ppd=ppd,
        shape=shape,
        intensity_rings=(0.0, intensity_surround),
        intensity_background=intensity_background,
        intensity_target=intensity_target,
        origin=origin,
    )
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


generalized_two_sided = make_two_sided(
    generalized,
    two_sided_params=(
        "target_size",
        "target_position",
        "rotation",
        "intensity_target",
        "intensity_background",
    ),
)


basic_two_sided = make_two_sided(
    basic, two_sided_params=("target_size", "intensity_target", "intensity_background")
)


square_two_sided = make_two_sided(
    square,
    two_sided_params=(
        "target_radius",
        "surround_radius",
        "rotation",
        "intensity_target",
        "intensity_surround",
        "intensity_background",
    ),
)


circular_two_sided = make_two_sided(
    circular,
    two_sided_params=(
        "target_radius",
        "surround_radius",
        "intensity_target",
        "intensity_surround",
        "intensity_background",
    ),
)


with_dots_two_sided = make_two_sided(
    with_dots, two_sided_params=("intensity_dots", "intensity_background", "intensity_target")
)


dotted_two_sided = make_two_sided(
    dotted, two_sided_params=("intensity_target", "intensity_background", "intensity_dots")
)


def overview(**kwargs):
    """Generate example stimuli from this module

    Returns
    -------
    stims : dict
        dict with all stimuli containing individual stimulus dicts.
    """
    default_params = {
        "ppd": 40,
    }
    default_params.update(kwargs)

    dot_params = {
        "n_dots": 5,
        "dot_radius": 2,
        "distance": 0.05,
        "target_shape": 3,
    }

    # fmt: off
    stimuli = {
        "sbc_generalized": generalized(**default_params, visual_size=10, target_size=(3, 4), target_position=(1, 2)),
        "sbc_basic": basic(**default_params, visual_size=10, target_size=3),
        "sbc_square": square(**default_params, visual_size=10, target_radius=1, surround_radius=2),
        "sbc_circular": circular(**default_params, visual_size=10, target_radius=1, surround_radius=2),
        "sbc_with_dots": with_dots(**default_params, **dot_params),
        "sbc_dotted": dotted(**default_params, **dot_params),

        "sbc_2sided": basic_two_sided(**default_params, visual_size=10, target_size=2, intensity_background=(0.0, 1.0)),
        "sbc_square_2sided": square_two_sided(**default_params, visual_size=10, target_radius=1, surround_radius=2, intensity_surround=(1.0, 0.0)),
        "sbc_circular_2sided": circular_two_sided(**default_params, visual_size=10, target_radius=1, surround_radius=2, intensity_surround=(1.0, 0.0)),
        "sbc_with_dots_2sided": with_dots_two_sided(**default_params, **dot_params, intensity_background=(0.0, 1.0), intensity_dots=(1.0, 0.0)),
        "sbc_dotted_2sided": dotted_two_sided(**default_params, **dot_params, intensity_background=(0.0, 1.0), intensity_dots=(1.0, 0.0)),
    }
    # fmt: on

    return stimuli


if __name__ == "__main__":
    from stimupy.utils import plot_stimuli

    stims = overview()
    plot_stimuli(stims, mask=False, save=None)
