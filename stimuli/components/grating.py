import numpy as np

from stimuli.utils import degrees_to_pixels


def square_wave(
    visual_size=(10, 10),
    ppd=10,
    frequency=1,
    intensity_bars=(0.0, 1.0),
    period="ignore",
):
    """
    Create a horizontal square wave of given spatial frequency.

    Parameters
    ----------
    visual_size : float or (float, float)
        size of the image in degrees visual angle
    ppd : int
        pixels per degree (visual angle)
    frequency : float
        the spatial frequency of the wave in cycles per degree
    intensity_bars : (float, float)
        intensity values for bars
    period : string in ['ignore', 'full', 'half']
        specifies if the period of the wave is considered for stimulus dimensions.
            'ignore' simply converts degrees to pixels
            'full' rounds down to guarantee a full period
            'half' adds a half period to the size 'full' would yield.
        Default is 'ignore'.

    Returns
    -------
    A 2d-array with a square-wave grating
    """

    if period not in ["ignore", "full", "half"]:
        raise TypeError("period not understood: %s" % period)
    if frequency > ppd / 2:
        raise ValueError("The frequency is limited to ppd/2.")

    height, width = degrees_to_pixels(visual_size, ppd)
    pixels_per_cycle = degrees_to_pixels(1.0 / (frequency * 2), ppd) * 2
    frequency_used = 1.0 / pixels_per_cycle * ppd
    if degrees_to_pixels(1.0 / frequency, ppd) % 2 != 0:
        print(
            "Warning: Square-wave frequency changed from %f to %f ensure an even-numbered cycle"
            " width!" % (frequency, frequency_used)
        )

    if period == "full":
        width = (width // pixels_per_cycle) * pixels_per_cycle
    elif period == "half":
        width = (width // pixels_per_cycle) * pixels_per_cycle + pixels_per_cycle / 2
    width = int(width)

    img = np.ones((height, width)) * intensity_bars[1]

    index = [
        i + j
        for i in range(pixels_per_cycle // 2)
        for j in range(0, width, pixels_per_cycle)
        if i + j < width
    ]
    img[:, index] = intensity_bars[0]

    stim = {
        "img": img,
        "ppd": ppd,
        "visual_size": np.array(img.shape) / ppd,
        "shape": img.shape,
        "frequency": frequency,
        "intensity_bars": intensity_bars,
        "period": period,
    }
    return stim


def square_wave_grating(
    ppd=10,
    n_bars=8,
    bar_shape=(8.0, 1.0),
    intensity_bars=(0.0, 1.0),
):
    """
    Square-wave grating

    Parameters
    ----------
    ppd : int
        pixels per degree (visual angle)
    n_bars : int
        the number of vertical bars
    bar_shape : (float, float)
        bar height and width in degrees visual angle
    intensity_bars : (float, float)
        intensity values for bars

    Returns
    -------
    A 2d-array with a square-wave grating
    """

    bar_height_px, bar_width_px = degrees_to_pixels(bar_shape, ppd)
    img = np.ones([1, n_bars]) * intensity_bars[1]
    img[:, ::2] = intensity_bars[0]
    img = img.repeat(bar_width_px, axis=1).repeat(bar_height_px, axis=0)

    stim = {
        "img": img,
        "ppd": ppd,
        "visual_size": np.array(img.shape) / ppd,
        "shape": img.shape,
        "n_bars": n_bars,
        "bar_shape": bar_shape,
        "intensity_bars": intensity_bars,
    }
    return stim
