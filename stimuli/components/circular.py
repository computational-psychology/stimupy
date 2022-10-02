import numpy as np
from stimuli.utils import degrees_to_pixels, resize_array


def disc_and_rings(
    radii,
    intensities,
    shape=None,
    visual_size=None,
    ppd=None,
    background=0.0,
    supersampling=5,
):
    """
    Draw a central solid disc with one or more solid rings (annuli)

    Parameters
    ----------
    radii : Sequence[Number]
        outer radii of rings (& disc) in degree visual angle
    intensities : Sequence[Number]
        intensity values of (disc &) rings
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] in pixels
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    background : float (optional)
        value of background. Default is 0.0
    supersampling : int (optional)
        supersampling-factor used for anti-aliasing. Default is 5.

    Returns
    -------
    A 2d-array with disc and rings
    """

    # Convert radii to pixels
    radii_px = degrees_to_pixels(radii, ppd)

    # Create stimulus at 5 times size to allow for supersampling antialiasing
    if shape is None:
        shape = [radii_px.max() * 2, radii_px.max() * 2]

    # Supersample shape (in pixels), to allow for antialiasing
    shape = (shape[0] * supersampling, shape[1] * supersampling)

    # Create image array
    img = np.ones(shape) * background

    # Compute distance from center of array for every pixel, cap at 1.0
    x = np.linspace(-img.shape[1] / 2.0, img.shape[1] / 2.0, img.shape[1])
    y = np.linspace(-img.shape[0] / 2.0, img.shape[0] / 2.0, img.shape[0])
    distances = np.sqrt(x[np.newaxis, :] ** 2 + y[:, np.newaxis] ** 2)

    # Draw rings
    for radius, intensity in zip(radii_px[::-1] * supersampling, intensities[::-1]):
        img[distances < radius] = intensity

    # Downsample the stimulus by local averaging along rows and columns
    sampler = resize_array(np.eye(img.shape[0] // supersampling), (1, supersampling))
    img = np.dot(sampler, np.dot(img, sampler.T)) / supersampling**2
    return img


def disc(
    ppd=20,
    radius=3,
    vback=0.0,
    vdisc=1.0,
    ssf=5,
):
    """
    Create a central disc

    Parameters
    ----------
    ppd : int
        pixels per degree (visual angle)
    radius : float
        radius of disc in degree visual angle
    vback : float
        value of background
    vdisc : float
        value of disc
    ssf : int (optional)
          the supersampling-factor used for anti-aliasing. Default is 5.

    Returns
    -------
    A 2d-array with a disc
    """
    radius = [radius]
    vdisc = [vdisc]

    if len(radius) > 1:
        raise ValueError("Too many radii passed")
    if len(vdisc) > 1:
        raise ValueError("Too many values for discs passed")

    img = disc_and_rings(
        radii=radius, intensities=vdisc, ppd=ppd, background=vback, supersampling=ssf
    )
    return img
