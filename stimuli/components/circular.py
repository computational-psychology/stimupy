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
    # Logic here is that ring_width expresses "degrees per ring",
    # which we can invert to rings_per_degree, analogous to ppd:
    # n_rings = rings_per_degree * n_degrees
    # is analogous to
    # pix = ppd * n_degrees
    # Thus we can resolve the number and spacing of rings also as a resolution

    # ring_width = 1 / rings_per_degree = 1 / (2*frequency)
    if ring_width is None and frequency is not None:
        ring_width = 1 / (2 * frequency)

    rings_pd = 1 / ring_width if ring_width is not None else None
    try:
        min_vis_angle = np.min([i for i in visual_size if i is not None]) / 2
    except ValueError:
        min_vis_angle = None

    n_rings, min_vis_angle, rings_pd = resolution.resolve_1D(
        length=n_rings, visual_angle=min_vis_angle, ppd=rings_pd
    )
    min_vis_angle = min_vis_angle * 2
    ring_width = 1 / rings_pd

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
        "ring_width": ring_width,
        "n_rings": n_rings,
        "radii": radii,
    }


def disc_and_rings(
    radii,
    intensities,
    shape=None,
    visual_size=None,
    ppd=None,
    intensity_background=0.0,
    supersampling=5,
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
        value of background, by default 0.0
    supersampling : int (optional)
        supersampling-factor used for anti-aliasing, by default 5

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

    # no axes are None; check if fits
    if visual_size.height < np.max(radii) * 2 or visual_size.width < np.max(radii) * 2:
        raise ValueError(
            f"Largest radius {np.max(radii)} does not fit in visual size {visual_size}"
        )

    # Resolve resolution
    shape, visual_size, ppd = resolution.resolve(shape, visual_size, ppd)

    # Convert radii to pixels
    radii = np.unique(radii)
    radii_px = []
    for radius in radii:
        radius_px, _, _ = resolution.resolve_1D(length=None, visual_angle=radius, ppd=ppd[0])
        radii_px.append(radius_px)
    radii_px = np.sort(radii_px)

    # Create stimulus at 5 times size to allow for supersampling antialiasing
    if shape is None:
        shape = [radii_px.max() * 2, radii_px.max() * 2]

    # Supersample shape (in pixels), to allow for antialiasing
    super_shape = (shape[0] * supersampling, shape[1] * supersampling)

    # Create image array
    img = np.ones(super_shape) * intensity_background

    # Compute distance from center of array for every pixel, cap at 1.0
    x = np.linspace(-img.shape[1] / 2.0, img.shape[1] / 2.0, img.shape[1])
    y = np.linspace(-img.shape[0] / 2.0, img.shape[0] / 2.0, img.shape[0])
    distances = np.sqrt(x[np.newaxis, :] ** 2 + y[:, np.newaxis] ** 2)

    # Draw rings
    ints = [*itertools.islice(itertools.cycle(intensities), len(radii_px))]
    for radius, intensity in zip(reversed(radii_px * supersampling), reversed(ints)):
        img[distances < radius] = intensity

    # Downsample the stimulus by local averaging along rows and columns
    sampler = resize_array(np.eye(img.shape[0] // supersampling), (1, supersampling))
    img = np.dot(sampler, np.dot(img, sampler.T)) / supersampling**2

    # Assemble output
    params = {
        "visual_size": visual_size,
        "ppd": ppd,
        "radii": radii,
        "intensities": intensities,
        "supersampling": supersampling,
    }
    return {"img": img, **params}


def disc(
    radius,
    intensity=1.0,
    shape=None,
    visual_size=None,
    ppd=None,
    intensity_background=0.0,
    supersampling=5,
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
        value of background, by default 0.0
    supersampling : int (optional)
        supersampling-factor used for anti-aliasing, by default 5

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
    intensity_background=0.0,
    supersampling=5,
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
        intensity value of background, by default 0.0
    supersampling : int (optional)
        supersampling-factor used for anti-aliasing, by default 5

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
    intensity_background=0.0,
    supersampling=5,
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
        intensity value of background, by default 0.0
    supersampling : int (optional)
        supersampling-factor used for anti-aliasing, by default 5

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
