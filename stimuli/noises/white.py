"""
@author: lynnschmittwilken
"""

import numpy as np
from stimuli.utils import degrees_to_pixels
from stimuli.noises.utils import pseudo_white_spectrum


__all__ = [
    "white",
]

def white(
    visual_size=None,
    ppd=None,
    rms_contrast=None,
    pseudo_noise=False,
):
    """
    Function to create white noise.

    Parameters
    ----------
    visual_size : float or (float, float)
        size of the stimulus in degrees of visual angle (height, width)
    ppd : int
        pixels per degree (visual angle)
    rms_contrast : float
        rms contrast of noise.
    pseudo_noise : bool
        if True, generate pseudo-random noise with ideal power spectrum.

    Returns
    -------
    A stimulus dictionary with the noise array ['img']
    """
    if isinstance(visual_size, (float, int)):
        visual_size = (visual_size, visual_size)

    shape = degrees_to_pixels(visual_size, ppd)

    if pseudo_noise:
        # Create white noise with frequency amplitude of 1 everywhere
        white_noise_fft = pseudo_white_spectrum(shape)

        # ifft
        white_noise = np.fft.ifft2(np.fft.ifftshift(white_noise_fft))
        white_noise = np.real(white_noise)
    else:
        # Create white noise and fft
        white_noise = np.random.rand(*shape) * 2.0 - 1.0

    # Adjust noise rms contrast:
    white_noise = rms_contrast * white_noise / white_noise.std()

    params = {
        "visual_size": visual_size,
        "shape": white_noise.shape,
        "ppd": ppd,
        "rms_contrast": rms_contrast,
        "pseudo_noise": pseudo_noise,
        "intensity_range": [white_noise.min(), white_noise.max()],
    }
    return {"img": white_noise, "mask": None, **params}


if __name__ == "__main__":
    from stimuli.utils import plot_stimuli
    
    params = {
        "visual_size": 10,
        "ppd": 20,
        "rms_contrast": 0.2,
        "pseudo_noise": True,
        }

    stims = {
        "White noise": white(**params),
    }
    plot_stimuli(stims, mask=True, save=None, vmin=-0.5, vmax=0.5)
