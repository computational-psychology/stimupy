import numpy as np
from stimuli.utils import resolution


__all__ = [
    "gaussian",   
]


def gaussian(
    visual_size=None,
    ppd=None,
    shape=None,
    sigma=None,
    orientation=0,
    intensity_max=1.,
    ):
    """ Create a Gaussian (envelop)

    Parameters
    ----------
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of image, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of image, in pixels
    sigma : float or (float, float)
        Sigma auf Gaussian in degree visual angle (y, x)
    orientation : float
        Orientation of Gaussian in degree (default 0)
    intensity_max : float
        Maximal intensity value of Gaussian

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img")
        and additional keys containing stimulus parameters
    """
    if isinstance(sigma, (float, int)):
        sigma = (sigma, sigma)

    # Resolve resolution
    shape, visual_size, ppd = resolution.resolve(shape, visual_size, ppd)

    # Image coordinates
    x = np.linspace(-visual_size.width / 2.0, visual_size.width / 2.0, shape.width)
    y = np.linspace(-visual_size.height / 2.0, visual_size.height / 2.0, shape.height)
    yy, xx = np.meshgrid(y, x)
    
    # set center to (0, 0)
    center = (0, 0)

    # convert orientation parameter to radians
    theta = np.deg2rad(orientation)

    # determine a, b, c coefficients
    a = (np.cos(theta)**2 / (2*sigma[0]**2)) +\
        (np.sin(theta)**2 / (2*sigma[1]**2))
    b = -(np.sin(2*theta) / (4*sigma[0]**2)) +\
        (np.sin(2*theta) / (4*sigma[1]**2))
    c = (np.sin(theta)**2 / (2*sigma[0]**2)) +\
        (np.cos(theta)**2 / (2*sigma[1]**2))

    # create Gaussian
    gaussian = np.exp(-(a*(xx-center[0])**2 +
                      2*b*(xx-center[0])*(yy-center[1]) +
                      c*(yy-center[1])**2))
    gaussian = gaussian / gaussian.max() * intensity_max
    
    stim = {
        "img": gaussian,
        "sigma": sigma,
        "orientation": orientation,
        "visual_size": visual_size,
        "shape": shape,
        "ppd": ppd,
        }
    return stim
