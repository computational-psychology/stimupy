import itertools

import numpy as np

from stimuli.utils import resize_array, resolution


def disc_and_rings(
    radii,
    intensities,
    shape=None,
    visual_size=None,
    ppd=None,
    background_intensity=0.0,
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
        shape [height, width] in pixels
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    background : float (optional)
        value of background, by defaul 0.0
    supersampling : int (optional)
        supersampling-factor used for anti-aliasing, by default 5

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img")
        and additional keys containing stimulus parameters
    """

    # Check visual_size
    visual_size = resolution.validate_visual_size(visual_size)
    if visual_size.height is None:
        if visual_size.width is not None:
            visual_height = visual_size.width
        else:
            visual_height = np.max(radii) * 2
    elif visual_size.height < np.max(radii) * 2:
        raise ValueError(
            f"Largest radius {np.max(radii)} does not fit in visual size {visual_size}"
        )
    else:
        visual_height = visual_size.height

    if visual_size.width is None:
        if visual_size.height is not None:
            visual_width = visual_size.height
        else:
            visual_width = np.max(radii) * 2
    elif visual_size.width < np.max(radii) * 2:
        raise ValueError(
            f"Largest radius {np.max(radii)} does not fit in visual size {visual_size}"
        )
    else:
        visual_width = visual_size.width

    # Resolve resolution
    shape, visual_size, ppd = resolution.resolve(shape, (visual_height, visual_width), ppd)

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
    img = np.ones(super_shape) * background_intensity

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
    background_intensity=0.0,
    supersampling=5,
):
    """Draw a central disc

    Parameters
    ----------
    radii : Sequence[Number]
        outer radii of rings (& disc) in degree visual angle
    intensity : Number
        intensity value of disc, by default 1.0
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] in pixels
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    background : float (optional)
        value of background, by default 0.0
    supersampling : int (optional)
        supersampling-factor used for anti-aliasing, by default 5.

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
        background_intensity=background_intensity,
        supersampling=supersampling,
    )
    return stim


def ring(
    radii,
    intensity=1.0,
    shape=None,
    visual_size=None,
    ppd=None,
    background_intensity=0.0,
    supersampling=5,
):

    intensity = [intensity]

    if len(radii) != 2:
        raise ValueError("Can only pass exactly 2 radii")
    if len(intensity) != 1:
        raise ValueError("Can only pass 1 intensity")

    stim = disc_and_rings(
        radii=radii,
        intensities=[background_intensity, intensity],
        shape=shape,
        visual_size=visual_size,
        ppd=ppd,
        background_intensity=background_intensity,
        supersampling=supersampling,
    )
    return stim


annulus = ring
