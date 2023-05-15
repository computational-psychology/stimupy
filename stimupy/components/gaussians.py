import numpy as np

from stimupy.components import image_base
from stimupy.components.shapes import ellipse

__all__ = [
    "gaussian",
]


def gaussian(
    visual_size=None,
    ppd=None,
    shape=None,
    sigma=None,
    rotation=0.0,
    intensity_max=1.0,
    origin="mean",
):
    """Create a Gaussian (envelop)

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
    rotation : float, optional
        rotation (in degrees), counterclockwise, by default 0.0
    intensity_max : float
        Maximal intensity value of Gaussian
    origin : "corner", "mean" or "center"
        if "corner": set origin to upper left corner
        if "mean": set origin to hypothetical image center (default)
        if "center": set origin to real center (closest existing value to mean)

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img")
        ellipse-like mask with sigma radius and integer index (key: "gaussian_mask"),
        and additional keys containing stimulus parameters
    """
    if sigma is None:
        raise ValueError("gaussian() missing argument 'sigma' which is not 'None'")
    if isinstance(sigma, (float, int)):
        sigma = (sigma, sigma)

    # Resolve resolutions and get distances
    base = image_base(
        visual_size=visual_size,
        ppd=ppd,
        shape=shape,
        rotation=rotation,
        origin=origin,
    )
    xx = base["horizontal"]
    yy = base["vertical"]

    # convert rotation parameter to radians
    theta = np.deg2rad(-rotation)

    # determine a, b, c coefficients
    a = (np.cos(theta) ** 2 / (2 * sigma[1] ** 2)) + (np.sin(theta) ** 2 / (2 * sigma[0] ** 2))
    b = -(np.sin(2 * theta) / (4 * sigma[1] ** 2)) + (np.sin(2 * theta) / (4 * sigma[0] ** 2))
    c = (np.sin(theta) ** 2 / (2 * sigma[1] ** 2)) + (np.cos(theta) ** 2 / (2 * sigma[0] ** 2))

    # create Gaussian
    gaussian = np.exp(-(a * xx**2 + 2 * b * xx * yy + c * yy**2))
    gaussian = gaussian / gaussian.max() * intensity_max

    # create mask as ellipse with sigma radius
    mask = ellipse(
        visual_size=visual_size,
        ppd=ppd,
        shape=shape,
        radius=sigma,
        rotation=rotation,
        origin=origin,
        restrict_size=False,
    )["ellipse_mask"]

    stim = {
        "img": gaussian,
        "gaussian_mask": mask.astype(int),
        "sigma": sigma,
        "rotation": rotation,
        "visual_size": base["visual_size"],
        "shape": base["shape"],
        "ppd": base["ppd"],
        "intensity_max": intensity_max,
        "origin": origin,
    }
    return stim


def overview(**kwargs):
    """Generate example stimuli from this module

    Returns
    -------
    stims : dict
        dict with all stimuli containing individual stimulus dicts.
    """
    default_params = {
        "visual_size": 10,
        "ppd": 10,
    }
    default_params.update(kwargs)

    # fmt: off
    stimuli = {
        "gaussians_gaussian": gaussian(**default_params, sigma=(3, 1.5), rotation=70),}
    # fmt: on

    return stimuli


if __name__ == "__main__":
    from stimupy.utils import plot_stimuli

    stims = overview()
    plot_stimuli(stims, mask=False, save=None)
