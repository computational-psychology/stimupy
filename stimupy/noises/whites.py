import numpy as np

from stimupy.noises.utils import pseudo_white_spectrum
from stimupy.utils import resolution
from stimupy.utils.contrast_conversions import adapt_intensity_range

__all__ = [
    "white",
]


def white(
    visual_size=None,
    ppd=None,
    shape=None,
    intensity_range=(0, 1),
    pseudo_noise=False,
):
    """Draw white noise texture

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
    # Resolve resolution
    shape, visual_size, ppd = resolution.resolve(shape=shape, visual_size=visual_size, ppd=ppd)

    if len(np.unique(ppd)) > 1:
        raise ValueError("ppd should be equal in x and y direction")

    if pseudo_noise:
        # Create white noise with frequency amplitude of 1 everywhere
        white_noise_fft = pseudo_white_spectrum(shape)

        # ifft
        white_noise = np.fft.ifft2(np.fft.ifftshift(white_noise_fft))
        white_noise = np.real(white_noise)
    else:
        # Create white noise and fft
        white_noise = np.random.rand(*shape) * 2.0 - 1.0

    # Adjust intensity range:
    white_noise = adapt_intensity_range(white_noise, intensity_range[0], intensity_range[1])

    stim = {
        "img": white_noise,
        "noise_mask": None,
        "visual_size": visual_size,
        "ppd": ppd,
        "shape": shape,
        "pseudo_noise": pseudo_noise,
        "intensity_range": [white_noise.min(), white_noise.max()],
    }
    return stim


if __name__ == "__main__":
    from stimupy.utils import plot_stimuli

    params = {
        "visual_size": 10,
        "ppd": 20,
        "pseudo_noise": True,
    }

    stims = {
        "White noise": white(**params),
    }
    plot_stimuli(stims, mask=True, save=None)
