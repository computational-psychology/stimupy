import numpy as np

from stimupy.noises import pseudo_white_spectrum
from stimupy.utils import resolution
from stimupy.utils.contrast_conversions import adapt_intensity_range

__all__ = [
    "one_over_f",
    "pink",
    "brown",
]


def one_over_f(
    visual_size=None,
    ppd=None,
    shape=None,
    exponent=None,
    intensity_range=(0, 1),
    pseudo_noise=False,
):
    """Draw 1 / (f**exponent) noise texture

    Parameters
    ----------
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of grating, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of grating, in pixels
    exponent
        exponent used to create 1 / (f**exponent) noise
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
    if exponent is None:
        raise ValueError("one_over_f() missing argument 'exponent' which is not 'None'")
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

    # Adjust intensity range:
    noise = adapt_intensity_range(noise, intensity_range[0], intensity_range[1])

    stim = {
        "img": noise,
        "noise_mask": None,
        "visual_size": visual_size,
        "ppd": ppd,
        "shape": shape,
        "exponent": exponent,
        "pseudo_noise": pseudo_noise,
        "intensity_range": [noise.min(), noise.max()],
    }
    return stim


def pink(
    visual_size=None,
    ppd=None,
    shape=None,
    intensity_range=(0, 1),
    pseudo_noise=False,
):
    """Draw pink (1 / f) noise texture

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
    pseudo_noise : bool
        if True, generate pseudo-random noise with ideal power spectrum

    Returns
    -------
    A stimulus dictionary with the noise array ['img']
    """

    stim = one_over_f(
        visual_size=visual_size,
        ppd=ppd,
        exponent=1.0,
        intensity_range=intensity_range,
        pseudo_noise=pseudo_noise,
    )
    return stim


def brown(
    visual_size=None,
    ppd=None,
    shape=None,
    intensity_range=(0, 1),
    pseudo_noise=False,
):
    """Draw brown (1 / (f**2.0)) noise texture

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
    pseudo_noise : bool
        if True, generate pseudo-random noise with ideal power spectrum

    Returns
    -------
    A stimulus dictionary with the noise array ['img']
    """

    stim = one_over_f(
        visual_size=visual_size,
        ppd=ppd,
        exponent=2.0,
        intensity_range=intensity_range,
        pseudo_noise=pseudo_noise,
    )
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
        "naturals_one-over-f": one_over_f(**default_params, exponent=0.5),
        "naturals_pink": pink(**default_params),
        "naturals_brown": brown(**default_params),}
    # fmt: on

    return stimuli


if __name__ == "__main__":
    from stimupy.utils import plot_stimuli

    stims = overview()
    plot_stimuli(stims, mask=False, save=None)
