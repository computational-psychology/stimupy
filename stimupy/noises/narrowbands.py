import numpy as np

from stimupy.noises import pseudo_white_spectrum
from stimupy.utils import resolution, bandpass
from stimupy.utils.contrast_conversions import adapt_intensity_range

__all__ = [
    "narrowband",
]


def narrowband(
    visual_size=None,
    ppd=None,
    shape=None,
    center_frequency=None,
    bandwidth=None,
    intensity_range=(0, 1),
    pseudo_noise=False,
):
    """Draw narrowband noise texture

    Parameters
    ----------
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of grating, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of grating, in pixels
    center_frequency : float
        noise center frequency in cpd
    bandwidth : float
        bandwidth of the noise in octaves
    intensity_range : Sequence[Number, Number]
        minimum and maximum intensity value; default: (0, 1)
    pseudo_noise : bool
        if True, generate pseudo-random noise with ideal power spectrum.

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        and additional keys containing stimulus parameters
    """
    if center_frequency is None:
        raise ValueError("narrowband() missing argument 'center_frequency' which is not 'None'")
    if bandwidth is None:
        raise ValueError("narrowband() missing argument 'bandwidth' which is not 'None'")

    # Resolve resolution
    shape, visual_size, ppd = resolution.resolve(shape=shape, visual_size=visual_size, ppd=ppd)

    if len(np.unique(ppd)) > 1:
        raise ValueError("ppd should be equal in x and y direction")

    bp = bandpass(
        visual_size=visual_size, ppd=ppd, center_frequency=center_frequency, bandwidth=bandwidth
    )["img"]

    if pseudo_noise:
        # Create white noise with frequency amplitude of 1 everywhere
        white_noise_fft = pseudo_white_spectrum(shape)
    else:
        # Create white noise and fft
        white_noise = np.random.rand(*shape) * 2.0 - 1.0
        white_noise_fft = np.fft.fftshift(np.fft.fft2(white_noise))

    # Filter white noise with bandpass filter
    narrow_noise_fft = white_noise_fft * bp

    # ifft
    narrow_noise = np.fft.ifft2(np.fft.ifftshift(narrow_noise_fft))
    narrow_noise = np.real(narrow_noise)

    # Adjust intensity range:
    narrow_noise = adapt_intensity_range(narrow_noise, intensity_range[0], intensity_range[1])

    stim = {
        "img": narrow_noise,
        "noise_mask": None,
        "visual_size": visual_size,
        "ppd": ppd,
        "shape": shape,
        "center_frequency": center_frequency,
        "bandwidth": bandwidth,
        "pseudo_noise": pseudo_noise,
        "intensity_range": [narrow_noise.min(), narrow_noise.max()],
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
        "ppd": 20,
    }
    default_params.update(kwargs)

    # fmt: off
    stimuli = {
        "narrowbands_narrowband3": narrowband(**default_params, center_frequency=3, bandwidth=1),
        "narrowbands_narrowband9": narrowband(**default_params, center_frequency=9, bandwidth=1),}
    # fmt: on

    return stimuli


if __name__ == "__main__":
    from stimupy.utils import plot_stimuli

    stims = overview()
    plot_stimuli(stims, mask=False, save=None)
