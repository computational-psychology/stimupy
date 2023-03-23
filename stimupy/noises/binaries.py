import numpy as np

from stimupy.utils import resolution
from stimupy.utils.contrast_conversions import adapt_intensity_range

__all__ = [
    "binary",
]


def binary(
    visual_size=None,
    ppd=None,
    shape=None,
    intensity_range=(0, 1),
):
    """Draw binary noise texture

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
    binary_noise = adapt_intensity_range(binary_noise, intensity_range[0], intensity_range[1])

    stim = {
        "img": binary_noise,
        "noise_mask": None,
        "visual_size": visual_size,
        "ppd": ppd,
        "shape": shape,
        "intensity_range": [binary_noise.min(), binary_noise.max()],
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
        "ppd": 10,
    }
    default_params.update(kwargs)

    # fmt: off
    stimuli = {
        "binaries_binary": binary(**default_params),}
    # fmt: on

    return stimuli


if __name__ == "__main__":
    from stimupy.utils import plot_stimuli

    stims = overview()
    plot_stimuli(stims, mask=False, save=None)
