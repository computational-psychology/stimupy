"""
@author: lynnschmittwilken
"""

import numpy as np
from stimuli.utils import resolution
from stimuli.utils.contrast_conversions import adapt_intensity_range


__all__ = [
    "binary",
]

def binary(
    visual_size=None,
    ppd=None,
    shape=None,
    intensity_range=(0, 1),
):
    """
    Function to create white noise.

    Parameters
    ----------
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of grating, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of grating, in pixels
    intensity_range : Sequence[Number, Number]
        minimum and maximum intensity value; default: (0, 1)

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        and additional keys containing stimulus parameters
    """
    # Resolve resolution
    shape, visual_size, ppd = resolution.resolve(shape=shape, visual_size=visual_size, ppd=ppd)
    
    if len(np.unique(ppd)) > 1:
        raise ValueError("ppd should be equal in x and y direction")

    binary_noise = np.random.randint(0, 2, size=shape) - 0.5

    # Adjust intensity range:
    binary_noise = adapt_intensity_range({"img": binary_noise}, intensity_range[0], intensity_range[1])["img"]

    stim = {
        "img": binary_noise,
        "noise_mask": None,
        "visual_size": visual_size,
        "ppd": ppd,
        "shape": shape,
        "intensity_range": [binary_noise.min(), binary_noise.max()],
    }
    return stim


if __name__ == "__main__":
    from stimuli.utils import plot_stimuli
    
    params = {
        "visual_size": 10,
        "ppd": 10,
        }

    stims = {
        "Binary noise": binary(**params),
    }
    plot_stimuli(stims, mask=True, save=None)
