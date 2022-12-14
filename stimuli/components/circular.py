import copy
import itertools

import numpy as np

from stimuli.components import mask_elements
from stimuli.components.components import image_base, resolve_grating_params
from stimuli.utils import resize_array, resolution

__all__ = [
    "disc_and_rings",
    "disc",
    "ring",
    "grating",
]


def resolve_circular_params(
    shape=None,
    visual_size=None,
    ppd=None,
    frequency=None,
    n_rings=None,
    ring_width=None,
):
    """Resolve (if possible) spatial parameters for circular grating, i.e., set of rings

    Circular grating / rings component takes the regular resolution parameters
    (shape, ppd, visual_size). In addition, there has to be an additional specification
    of the number of rings, and their width. This can be done in two ways:
    a ring_width (in degrees) and n_rings, and/or by specifying the spatial frequency
    of a circular grating (in cycles per degree)

    The total shape (in pixels) and visual size (in degrees) has to match the
    specification of the rings and their widths.
    Thus, not all 6 parameters have to be specified, as long as the both the resolution
    and the distribution of rings can be resolved.

    Note: all rings in a grating have the same width -- if more control is required
    see disc_and_rings

    Parameters
    ----------
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of image, in pixels
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of image, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    frequency : Number, or None (default)
        spatial frequency of circular grating, in cycles per degree
    n_rings : int, or None (default)
        number of rings
    ring_width : Number, or None (default)
        width of a single ring, in degrees

    Returns
    -------
    dict[str, Any]
        dictionary with all six resolution & size parameters resolved.
    """

    # Resolve params
    shape = resolution.validate_shape(shape)
    ppd = resolution.validate_ppd(ppd)
    visual_size = resolution.validate_visual_size(visual_size)

    length = np.array(shape).min() / 2 if None not in shape else None
    ppd_1D = np.array(ppd).min() if None not in ppd else None
    visual_angle = np.array(visual_size).min() / 2 if None not in visual_size else None
    params = resolve_grating_params(
        length=length,
        visual_angle=visual_angle,
        n_phases=n_rings,
        phase_width=ring_width,
        ppd=ppd_1D,
        frequency=frequency,
        # period=period,
    )
    shape = resolution.validate_shape(params["length"] * 2)
    visual_size = resolution.validate_visual_size(params["visual_angle"] * 2)
    ppd = resolution.validate_ppd(params["ppd"])

    return {
        "shape": shape,
        "visual_size": visual_size,
        "ppd": ppd,
        "frequency": params["frequency"],
        "ring_width": params["phase_width"],
        "n_rings": n_rings,
        # "period": params["period"],
        "radii": params["edges"],
    }


def mask_rings(
    radii,
    shape=None,
    visual_size=None,
    ppd=None,
):
    """Generate mask with integer indices for rings

    Parameters
    ----------
    radii : Sequence[Number]
        outer radii of rings (& disc) in degree visual angle
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of image, in pixels
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of image, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]

    Returns
    -------
    dict[str, Any]
        dict with the mask (key: "mask")
        and additional keys containing stimulus parameters

    Raises
    ------
    ValueError
        if largest radius does not fit in visual size
    """

    # no axes are None; check if fits
    if visual_size.height < np.max(radii) * 2 or visual_size.width < np.max(radii) * 2:
        raise ValueError(
            f"Largest radius {np.max(radii)} does not fit in visual size {visual_size}"
        )

    # Mark elements with integer idx-value
    return mask_elements(
        orientation="radial",
        edges=radii,
        rotation=0.0,
        shape=shape,
        visual_size=visual_size,
        ppd=ppd,
    )


def disc_and_rings(
    radii,
    intensity_rings,
    shape=None,
    visual_size=None,
    ppd=None,
    intensity_background=0.5,
    supersampling=1,
):
    """Draw a central solid disc with zero or more solid rings (annuli)

    Parameters
    ----------
    radii : Sequence[Number]
        outer radii of rings (& disc) in degree visual angle
    intensity_rings : Sequence[Number, ...]
        intensity value for each ring, from inside to out.
        If fewer intensities are passed than number of radii, cycles through intensities
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of image, in pixels
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of image, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    intensity_background : float (optional)
        value of background, by default 0.5
    supersampling : int (optional)
        supersampling-factor used for anti-aliasing, by default 5.
        Warning: produces smoother circles but might introduce gradients that affect vision!

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img")
        and additional keys containing stimulus parameters
    """

    # Try to resolve resolution;
    try:
        shape, visual_size, ppd = resolution.resolve(shape, visual_size, ppd)
    except ValueError:
        # Check visual_size
        visual_size = resolution.validate_visual_size(visual_size)

    if visual_size == (None, None):
        # Two axes are None; make image large enought to fit
        visual_size = resolution.validate_visual_size(np.max(radii) * 2)
    elif None in visual_size:
        # one axis is None; make square
        visual_size = [x for x in visual_size if x is not None]
        visual_size = resolution.validate_visual_size(visual_size)

    # Get masks for rings
    params = mask_rings(radii, shape, visual_size, ppd)
    shape = params["shape"]

    # Supersample shape (in pixels), to allow for antialiasing
    super_shape = resolution.validate_shape((shape[0] * supersampling, shape[1] * supersampling))

    # Draw rings
    base = image_base(shape=super_shape, visual_size=visual_size)
    distances = base["radial"]

    img = np.ones(super_shape) * intensity_background
    ints = [*itertools.islice(itertools.cycle(intensity_rings), len(radii))]
    for radius, intensity in zip(reversed(radii), reversed(ints)):
        img[distances < radius] = intensity

    # Downsample the stimulus by local averaging along rows and columns
    sampler = resize_array(np.eye(img.shape[0] // supersampling), (1, supersampling))
    img = np.dot(sampler, np.dot(img, sampler.T)) / supersampling**2

    # Assemble output
    params.update(
        {
            "intensities": intensity_rings,
            "supersampling": supersampling,
        }
    )
    return {"img": img, **params}


def disc(
    radius,
    intensity=1.0,
    shape=None,
    visual_size=None,
    ppd=None,
    intensity_background=0.5,
    supersampling=1,
):
    """Draw a central disc

    Essentially, `dics(radius)` is an alias for `ring(radii=[0, radius])`

    Parameters
    ----------
    radius : Number
        outer radius of disc in degree visual angle
    intensity : Number
        intensity value of disc, by default 1.0
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of image, in pixels
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of image, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    background : float (optional)
        value of background, by default 0.5
    supersampling : int (optional)
        supersampling-factor used for anti-aliasing, by default 1.
        Warning: produces smoother circles but might introduce gradients that affect vision!

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img")
        and additional keys containing stimulus parameters
    """

    radius = np.array(radius)
    intensity = np.array(intensity)

    if radius.size != 1:
        raise ValueError("Can only pass 1 radius")
    if intensity.size != 1:
        raise ValueError("Can only pass 1 intensity")

    stim = ring(
        radii=[0, radius],
        intensity=intensity,
        visual_size=visual_size,
        ppd=ppd,
        intensity_background=intensity_background,
        supersampling=supersampling,
        shape=shape,
    )
    return stim


def ring(
    radii,
    intensity=1.0,
    shape=None,
    visual_size=None,
    ppd=None,
    intensity_background=0.5,
    supersampling=1,
):
    """Draw a ring (annulus)

    Parameters
    ----------
    radii : Sequence[Number, Number]
        inner and outer radius of ring in degree visual angle
    intensity : Number
        intensity value of ring, by default 1.0
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of image, in pixels
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of image, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    intensity_background : float (optional)
        intensity value of background, by default 0.5
    supersampling : int (optional)
        supersampling-factor used for anti-aliasing, by default 5.
        Warning: produces smoother circles but might introduce gradients that affect vision!

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img")
        and additional keys containing stimulus parameters

    Raises
    ------
    ValueError
        if passed in less/more than 2 radii (inner, outer)
    ValueError
        if passed in less/more than 1 intensity
    """

    # Try to resolve resolution
    shape, visual_size, ppd = resolution.resolve(shape=shape, visual_size=visual_size, ppd=ppd)

    if len(radii) != 2:
        raise ValueError("Can only pass exactly 2 radii")
    if len([intensity]) != 1:
        raise ValueError("Can only pass 1 intensity")

    if radii[1] is None:
        radii[1] = np.max(visual_size) / 2

    stim = disc_and_rings(
        radii=radii,
        intensity_rings=[intensity_background, intensity],
        shape=shape,
        visual_size=visual_size,
        ppd=ppd,
        intensity_background=intensity_background,
        supersampling=supersampling,
    )
    return stim


annulus = ring


def grating(
    shape=None,
    visual_size=None,
    ppd=None,
    frequency=None,
    n_rings=None,
    ring_width=None,
    intensity_rings=(1.0, 0.0),
    intensity_background=0.5,
    supersampling=1,
):
    """Draw a circular grating, i.e., set of rings

    Parameters
    ----------
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of image, in pixels
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of image, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    frequency : Number, or None (default)
        spatial frequency of circular grating, in cycles per degree
    n_rings : int, or None (default)
        number of rings
    ring_width : Number, or None (default)
        width of a single ring, in degrees
    intensities : Sequence[Number, ...]
        intensity value for each ring, from inside to out, by default (1.0, 0.0).
        If fewer intensities are passed than number of radii, cycles through intensities
    intensity_background : float (optional)
        intensity value of background, by default 0.5
    supersampling : int (optional)
        supersampling-factor used for anti-aliasing, by default 1.
        Warning: produces smoother circles but might introduce gradients that affect vision!

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img")
        and additional keys containing stimulus parameters
    """

    # Resolve grating
    params = resolve_circular_params(shape, visual_size, ppd, frequency, n_rings, ring_width)

    # Clean-up params for passing through
    stim_params = copy.deepcopy(params)
    stim_params.pop("n_rings", None)
    stim_params.pop("ring_width", None)
    stim_params.pop("frequency", None)

    # Draw stim
    stim = disc_and_rings(
        **stim_params,
        intensity_background=intensity_background,
        intensity_rings=intensity_rings,
        supersampling=supersampling,
    )

    # Assemble output
    return {**stim, **params}
