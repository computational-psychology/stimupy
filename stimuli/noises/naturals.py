"""
@author: lynnschmittwilken
"""

import numpy as np
from stimuli.utils import resolution
from stimuli.noises.utils import pseudo_white_spectrum


__all__ = [
    "one_over_f",
    "pink",
    "brown",
]

def one_over_f(
    visual_size=None,
    ppd=None,
    shape=None,
    rms_contrast=None,
    exponent=None,
    pseudo_noise=False,
):
    """
    Function to create  1 / (f**exponent) noise.

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
    exponent
        exponent used to create 1 / (f**exponent) noise.
    pseudo_noise : bool
        if True, generate pseudo-random noise with ideal power spectrum.

    Returns
    -------
    A stimulus dictionary with the noise array ['img']
    """
    # Resolve resolution
    shape, visual_size, ppd = resolution.resolve(shape=shape, visual_size=visual_size, ppd=ppd)
    
    if len(np.unique(ppd)) > 1:
        raise ValueError("ppd should be equal in x and y direction")

    # Prepare spatial frequency axes and create bandpass filter:
    fy = np.fft.fftshift(np.fft.fftfreq(shape[0], d=1.0 / np.unique(ppd)))
    fx = np.fft.fftshift(np.fft.fftfreq(shape[1], d=1.0 / np.unique(ppd)))
    Fx, Fy = np.meshgrid(fx, fy)

    # Create 2d array with 1 / (f**exponent)
    f = np.sqrt(Fy**2.0 + Fx**2.0)
    f = f**exponent
    f[f == 0.0] = 1.0  # Prevent division by zero (DC is zero anyways)

    if pseudo_noise:
        # Create white noise with frequency amplitude of 1 everywhere
        white_noise_fft = pseudo_white_spectrum(shape)
    else:
        # Create white noise and fft
        white_noise = np.random.rand(*shape) * 2.0 - 1.0
        white_noise_fft = np.fft.fftshift(np.fft.fft2(white_noise))

    # Create 1/f noise:
    noise_fft = white_noise_fft / f

    # ifft
    noise = np.fft.ifft2(np.fft.ifftshift(noise_fft))
    noise = np.real(noise)

    # Adjust noise rms contrast:
    noise = rms_contrast * noise / noise.std()

    stim = {
        "img": noise,
        "mask": None,
        "visual_size": visual_size,
        "ppd": ppd,
        "shape": shape,
        "rms_contrast": rms_contrast,
        "exponent": exponent,
        "pseudo_noise": pseudo_noise,
        "intensity_range": [noise.min(), noise.max()],
    }
    return stim


def pink(
    visual_size=None,
    ppd=None,
    shape=None,
    rms_contrast=None,
    pseudo_noise=False,
):
    """
    Function to create  1 / (f**exponent) noise.

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
    pseudo_noise : bool
        if True, generate pseudo-random noise with ideal power spectrum.

    Returns
    -------
    A stimulus dictionary with the noise array ['img']
    """
    
    stim = one_over_f(
        visual_size=visual_size,
        ppd=ppd,
        rms_contrast=rms_contrast,
        exponent=1.0,
        pseudo_noise=pseudo_noise)
    return stim


def brown(
    visual_size=None,
    ppd=None,
    shape=None,
    rms_contrast=None,
    pseudo_noise=False,
):
    """
    Function to create  1 / (f**exponent) noise.

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
    pseudo_noise : bool
        if True, generate pseudo-random noise with ideal power spectrum.

    Returns
    -------
    A stimulus dictionary with the noise array ['img']
    """
    
    stim = one_over_f(
        visual_size=visual_size,
        ppd=ppd,
        rms_contrast=rms_contrast,
        exponent=2.0,
        pseudo_noise=pseudo_noise)
    return stim


if __name__ == "__main__":
    from stimuli.utils import plot_stimuli
    params = {
        "visual_size": 10,
        "ppd": 20,
        "rms_contrast": 0.2,
        "pseudo_noise": True,
        }

    stims = {
        "One over f": one_over_f(**params, exponent=0.5),
        "Pink noise": pink(**params),
        "Brown noise": brown(**params),
    }
    plot_stimuli(stims, mask=True, save=None, vmin=-0.5, vmax=0.5)