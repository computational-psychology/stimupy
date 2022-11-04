"""
@author: lynnschmittwilken
"""

import numpy as np
from stimuli.utils import degrees_to_pixels
from stimuli.noises.utils import pseudo_white_spectrum


def pink(
    visual_size=(10, 10),
    ppd=40.,
    rms_contrast=0.2,
    exponent=1.,
    pseudo_noise=True,
):
    """
    Function to create  1 / (f**exponent) noise.

    Parameters
    ----------
    visual_size : float or (float, float)
        size of the stimulus in degrees of visual angle (height, width)
    ppd : int
        pixels per degree (visual angle)
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
    if isinstance(visual_size, (float, int)):
        visual_size = (visual_size, visual_size)

    shape = degrees_to_pixels(visual_size, ppd)

    # Prepare spatial frequency axes and create bandpass filter:
    fy = np.fft.fftshift(np.fft.fftfreq(shape[0], d=1./ppd))
    fx = np.fft.fftshift(np.fft.fftfreq(shape[1], d=1./ppd))
    Fx, Fy = np.meshgrid(fx, fy)

    # Create 2d array with 1 / (f**exponent)
    f = np.sqrt(Fy**2. + Fx**2.)
    f = f**exponent
    f[f == 0.] = 1.  # Prevent division by zero (DC is zero anyways)

    if pseudo_noise:
        # Create white noise with frequency amplitude of 1 everywhere
        white_noise_fft = pseudo_white_spectrum(shape)
    else:
        # Create white noise and fft
        white_noise = np.random.rand(*shape) * 2. - 1.
        white_noise_fft = np.fft.fftshift(np.fft.fft2(white_noise))

    # Create 1/f noise:
    pink_noise_fft = white_noise_fft / f

    # ifft
    pink_noise = np.fft.ifft2(np.fft.ifftshift(pink_noise_fft))
    pink_noise = np.real(pink_noise)

    # Adjust noise rms contrast:
    pink_noise = rms_contrast * pink_noise / pink_noise.std()

    params = {
        "visual_size": visual_size,
        "shape": pink_noise.shape,
        "ppd": ppd,
        "rms_contrast": rms_contrast,
        "exponent": exponent,
        "pseudo_noise": pseudo_noise,
        "intensity_range": [pink_noise.min(), pink_noise.max()],
        }
    return {"img": pink_noise, **params}


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    from stimuli.utils import plot_stimuli

    stims = {
        "Pink noise": pink(exponent=1.),
        "Brown noise": pink(exponent=2.),
    }
    ax = plot_stimuli(stims)
    plt.show()
