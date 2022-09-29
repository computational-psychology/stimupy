import numpy as np
from stimuli.utils import degrees_to_pixels, resize_array


def disc_and_rings(
    ppd=20,
    radii=(3, 6, 9),
    vback=0.0,
    vdiscs=(1.0, 0.0, 1.0),
    ssf=5,
):
    """
    Create a central disc with rings

    Parameters
    ----------
    ppd : int
        pixels per degree (visual angle)
    radii : tuple of floats
        radii of disc in degree visual angle
    vback : float
        value of background
    vdiscs : tuple of floats
        values of discs
    ssf : int (optional)
          the supersampling-factor used for anti-aliasing. Default is 5.

    Returns
    -------
    A 2d-array with a disc
    """
    radii_px = degrees_to_pixels(radii, ppd) * ssf

    # create stimulus at 5 times size to allow for supersampling antialiasing
    img = np.ones([radii_px.max() * 2, radii_px.max() * 2]) * vback

    # compute distance from center of array for every point, cap at 1.0
    x = np.linspace(-img.shape[1] / 2.0, img.shape[1] / 2.0, img.shape[1])
    y = np.linspace(-img.shape[0] / 2.0, img.shape[0] / 2.0, img.shape[0])
    dist = np.sqrt(x[np.newaxis, :] ** 2 + y[:, np.newaxis] ** 2)

    radii_px = radii_px[::-1]
    vdiscs = vdiscs[::-1]
    for radius, value in zip(radii_px, vdiscs):
        img[dist < radius] = value

    # downsample the stimulus by local averaging along rows and columns
    sampler = resize_array(np.eye(img.shape[0] // ssf), (1, ssf))
    img = np.dot(sampler, np.dot(img, sampler.T)) / ssf**2
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

    img = disc_and_rings(ppd, radius, vback, vdisc, ssf)
    return img
