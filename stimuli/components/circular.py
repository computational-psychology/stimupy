import copy
import itertools

import numpy as np

from stimuli.utils import resize_array, resolution


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

    # Try to resolve resolution
    try:
        shape, visual_size, ppd = resolution.resolve(shape=shape, visual_size=visual_size, ppd=ppd)
    except ValueError:
        ppd = resolution.validate_ppd(ppd)
        shape = resolution.validate_shape(shape)
        visual_size = resolution.validate_visual_size(visual_size)

    # Try to resolve number and width(s) of rings

    # ring_width = degrees_per_ring = 1 / rings_per_degree = 1 / (2*frequency)
    if ring_width is not None:
        rings_pd = 1 / ring_width
        if frequency is not None and rings_pd != 2 * frequency:
            raise ValueError(f"ring_width {ring_width} and frequency {frequency} don't match")
    elif frequency is not None:
        rings_pd = 2 * frequency
    else:  # both are None:
        rings_pd = None

    # Logic here is that ring_width expresses "degrees per ring",
    # which we can invert to rings_per_degree, analogous to ppd:
    # n_rings = rings_per_degree * n_degrees
    # is analogous to
    # pix = ppd * n_degrees
    # Thus we can resolve the number and spacing of rings also as a resolution

    # What is the smaller axis of visual_size?
    try:
        min_vis_angle = np.min([i for i in visual_size if i is not None]) / 2
    except ValueError:
        min_vis_angle = None

    try:
        n_rings, min_vis_angle, rings_pd = resolution.resolve_1D(
            length=n_rings, visual_angle=min_vis_angle, ppd=rings_pd
        )
        min_vis_angle = min_vis_angle * 2
        ring_width = 1 / rings_pd
        frequency = rings_pd / 2
    except Exception as e:
        raise Exception("Could not resolve grating frequency, ring_width, n_rings") from e

    # Now resolve resolution
    shape, visual_size, ppd = resolution.resolve(
        shape=shape, visual_size=(min_vis_angle, min_vis_angle), ppd=ppd
    )

    # Determine radii
    radii = [*itertools.accumulate(itertools.repeat(ring_width, n_rings))]

    return {
        "shape": shape,
        "visual_size": visual_size,
        "ppd": ppd,
        "frequency": frequency,
        "ring_width": ring_width,
        "n_rings": n_rings,
        "radii": radii,
    }


def ring_masks(
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

    # Resolve resolution
    shape, visual_size, ppd = resolution.resolve(shape, visual_size, ppd)

    # Create image-base: compute visual angle from center for every pixel
    x = np.linspace(-visual_size.width / 2.0, visual_size.width / 2.0, shape.width)
    y = np.linspace(-visual_size.height / 2.0, visual_size.height / 2.0, shape.height)
    distances = np.sqrt(x[np.newaxis, :] ** 2 + y[:, np.newaxis] ** 2)
    mask = np.zeros(shape, dtype=int)

    # Draw rings with integer idx-value
    for radius, idx in zip(reversed(radii), reversed(range(len(radii)))):
        mask[distances < radius] = int(idx + 1)

    # Assemble output
    params = {
        "shape": shape,
        "visual_size": visual_size,
        "ppd": ppd,
        "radii": radii,
    }
    return {"mask": mask, **params}


def disc_and_rings(
    radii,
    intensities,
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
    intensities : Sequence[Number, ...]
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
    params = ring_masks(radii, shape, visual_size, ppd)
    shape = params["shape"]

    # Supersample shape (in pixels), to allow for antialiasing
    super_shape = resolution.validate_shape((shape[0] * supersampling, shape[1] * supersampling))

    # Create image array
    img = np.ones(super_shape) * intensity_background

    # Compute distance from center of array for every pixel, cap at 1.0
    x = np.linspace(-visual_size.width / 2.0, visual_size.width / 2.0, super_shape.width)
    y = np.linspace(-visual_size.height / 2.0, visual_size.height / 2.0, super_shape.height)
    distances = np.sqrt(x[np.newaxis, :] ** 2 + y[:, np.newaxis] ** 2)

    # Draw rings
    ints = [*itertools.islice(itertools.cycle(intensities), len(radii))]
    for radius, intensity in zip(reversed(radii), reversed(ints)):
        img[distances < radius] = intensity

    # Downsample the stimulus by local averaging along rows and columns
    sampler = resize_array(np.eye(img.shape[0] // supersampling), (1, supersampling))
    img = np.dot(sampler, np.dot(img, sampler.T)) / supersampling**2

    # Assemble output
    params.update(
        {
            "intensities": intensities,
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

    radius = [radius]
    intensity = [intensity]

    if len(radius) != 1:
        raise ValueError("Can only pass 1 radius")
    if len(intensity) != 1:
        raise ValueError("Can only pass 1 intensity")

    stim = disc_and_rings(
        radii=radius,
        intensities=intensity,
        shape=shape,
        visual_size=visual_size,
        ppd=ppd,
        intensity_background=intensity_background,
        supersampling=supersampling,
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
    intensity = [intensity]

    if len(radii) != 2:
        raise ValueError("Can only pass exactly 2 radii")
    if len(intensity) != 1:
        raise ValueError("Can only pass 1 intensity")

    stim = disc_and_rings(
        radii=radii,
        intensities=[intensity_background, intensity],
        shape=shape,
        visual_size=visual_size,
        ppd=ppd,
        intensity_background=intensity_background,
        supersampling=supersampling,
    )
    return stim


annulus = ring


def circular_grating(
    shape=None,
    visual_size=None,
    ppd=None,
    frequency=None,
    n_rings=None,
    ring_width=None,
    intensities=[1, 0],
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
        intensity value for each ring, from inside to out, by default [1,0]
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
        intensities=intensities,
        supersampling=supersampling,
    )

    # Assemble output
    return {**stim, **params}
