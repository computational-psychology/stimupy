"""
@author: lynnschmittwilken
"""

import numpy as np
from stimuli.utils import bandpass_filter, degrees_to_pixels
from stimuli.noises.utils import pseudo_white_spectrum


def narrowband(
    visual_size=(10, 20),
    ppd=40.0,
    center_frequency=3,
    bandwidth=1.0,
    rms_contrast=0.2,
    pseudo_noise=True,
):
    """
    Function to create narrowband noise.

    Parameters
    ----------
    visual_size : float or (float, float)
        size of the stimulus in degrees of visual angle (height, width)
    ppd : int
        pixels per degree (visual angle)
    center_frequency : float
        noise center frequency in cpd
    bandwidth : float
        bandwidth of the noise in octaves
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

    # We calculate sigma to eventuate given bandwidth (in octaves)
    sigma = (
        center_frequency
        / ((2.0**bandwidth + 1) * np.sqrt(2.0 * np.log(2.0)))
        * (2.0**bandwidth - 1)
    )

    # Prepare spatial frequency axes and create bandpass filter:
    fy = np.fft.fftshift(np.fft.fftfreq(shape[0], d=1.0 / ppd))
    fx = np.fft.fftshift(np.fft.fftfreq(shape[1], d=1.0 / ppd))
    Fx, Fy = np.meshgrid(fx, fy)
    bp_filter = bandpass_filter(Fy, Fx, center_frequency, sigma)

    if pseudo_noise:
        # Create white noise with frequency amplitude of 1 everywhere
        white_noise_fft = pseudo_white_spectrum(shape)
    else:
        # Create white noise and fft
        white_noise = np.random.rand(*shape) * 2.0 - 1.0
        white_noise_fft = np.fft.fftshift(np.fft.fft2(white_noise))

    # Filter white noise with bandpass filter
    narrow_noise_fft = white_noise_fft * bp_filter

    # ifft
    narrow_noise = np.fft.ifft2(np.fft.ifftshift(narrow_noise_fft))
    narrow_noise = np.real(narrow_noise)

    # Adjust noise rms contrast:
    narrow_noise = rms_contrast * narrow_noise / narrow_noise.std()

    params = {
        "visual_size": visual_size,
        "shape": narrow_noise.shape,
        "ppd": ppd,
        "rms_contrast": rms_contrast,
        "center_frequency": center_frequency,
        "sigma": sigma,
        "pseudo_noise": pseudo_noise,
        "intensity_range": [narrow_noise.min(), narrow_noise.max()],
    }
    return {"img": narrow_noise, **params}


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    from stimuli.utils import plot_stimuli

    stims = {
        "Narrowband noise - 3cpd": narrowband(center_frequency=3.0),
        "Narrowband noise - 9cpd": narrowband(center_frequency=9.0),
    }
    ax = plot_stimuli(stims)
    plt.show()
