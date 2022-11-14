import numpy as np

from stimuli.utils import resolution


def img_angles(visual_size=None, ppd=None, shape=None):
    """Matrix of angle (relative to center) for each pixel

    Parameters
    ----------
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of image, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of image, in pixels

    Returns
    -------
    numpy.ndarray
        array of shape, with the angle (in rad) relative to center point, for each pixel
    """

    # Resolve resolution
    shape, visual_size, ppd = resolution.resolve(shape, visual_size, ppd)

    # Image coordinates
    x = np.linspace(-visual_size.width / 2.0, visual_size.width / 2.0, shape.width)
    y = np.linspace(-visual_size.height / 2.0, visual_size.height / 2.0, shape.height)
    yy, xx = np.meshgrid(y, x)

    # Rotate image coordinates
    img_angles = -np.arctan2(xx, yy)
    img_angles %= 2 * np.pi

    return img_angles
