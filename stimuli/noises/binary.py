"""
@author: lynnschmittwilken
"""

import numpy as np
from stimuli.utils import resolution


__all__ = [
    "binary",
]

def binary(
    visual_size=None,
    ppd=None,
    shape=None,
    rms_contrast=None,
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
    rms_contrast : float
        rms contrast of noise.

    Returns
    -------
    A stimulus dictionary with the noise array ['img']
    """
    # Resolve resolution
    shape, visual_size, ppd = resolution.resolve(shape=shape, visual_size=visual_size, ppd=ppd)
    
    if len(np.unique(ppd)) > 1:
        raise ValueError("ppd should be equal in x and y direction")

    binary_noise = np.random.randint(0, 2, size=shape) - 0.5

    # Adjust noise rms contrast:
    binary_noise = rms_contrast * binary_noise / binary_noise.std()

    params = {
        "visual_size": visual_size,
        "ppd": ppd,
        "shape": shape,
        "rms_contrast": rms_contrast,
        "intensity_range": [binary_noise.min(), binary_noise.max()],
    }
    return {"img": binary_noise, "mask": None, **params}


if __name__ == "__main__":
    from stimuli.utils import plot_stimuli
    
    params = {
        "visual_size": 10,
        "ppd": 10,
        "rms_contrast": 0.2,
        }

    stims = {
        "Binary noise": binary(**params),
    }
    plot_stimuli(stims, mask=True, save=None, vmin=-0.5, vmax=0.5)
