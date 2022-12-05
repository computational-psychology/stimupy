import numpy as np

from stimuli.utils import degrees_to_pixels, resolution


def resolve_grating_params(
    shape=None,
    visual_size=None,
    ppd=None,
    frequency=None,
    n_phases=None,
    phase_width=None,
):
    """Resolve (if possible) spatial parameters for a grating

    Gratings take the regular resolution parameters (shape, ppd, visual_size).
    In addition, there has to be an additional specification
    of the frequency, number and with of phases (e.g., bars).
    This can be done in two ways:
    a phase_width (in degrees) and n_phases,
    and/or by specifying the spatial frequency of the grating (in cycles per degree)

    The total shape (in pixels) and visual size (in degrees) has to match the
    specification of the phases and their widths.
    Thus, not all 6 parameters have to be specified, as long as the both the resolution
    and the distribution of phases can be resolved.

    Note: all phases in a grating have the same width

    Parameters
    ----------
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of image, in pixels
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of image, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    frequency : Number, or None (default)
        spatial frequency of grating, in cycles per degree
    n_phases : int, or None (default)
        number of phases (e.g., bars), i.e., half the number of full periods
    phase_width : Number, or None (default)
        width of a single phase (e.g., bar), in degrees

    Returns
    -------
    dict[str, Any]
        dictionary with all six resolution & size parameters resolved.
    """

    # Try to resolve resolution
    try:
        shape, visual_size, ppd = resolution.resolve(shape=shape, visual_size=visual_size, ppd=ppd)
    except ValueError:
        ppd = resolution.validate_ppd(ppd)
        shape = resolution.validate_shape(shape)
        visual_size = resolution.validate_visual_size(visual_size)

    # Try to resolve number and width(s) of phases:
    # Logic here is that phase_width expresses "degrees per phase",
    # which we can convert to "phases_per_degree"
    # phase_width = degrees_per_phase = 1 / phases_per_degree = 1 / (2*frequency)
    if phase_width is not None:
        phases_pd = 1 / phase_width
        if frequency is not None and phases_pd != 2 * frequency:
            raise ValueError(f"phase_width {phase_width} and frequency {frequency} don't match")
    elif frequency is not None:
        phases_pd = 2 * frequency
    else:  # both are None:
        phases_pd = None

    # Logic here is that phase_width expresses "degrees per phase",
    # which we can invert to phases_per_degree, analogous to ppd:
    # n_phases = phases_per_degree * n_degrees
    # is analogous to
    # pix = ppd * n_degrees
    # Thus we can resolve the number and spacing of phases also as a resolution

    # What is the smaller axis of visual_size?
    try:
        min_vis_angle = np.min([i for i in visual_size if i is not None]) / 2
    except ValueError:
        min_vis_angle = None

    try:
        n_phases, min_vis_angle, phases_pd = resolution.resolve_1D(
            length=n_phases, visual_angle=min_vis_angle, ppd=phases_pd
        )
        min_vis_angle = min_vis_angle * 2
        phase_width = 1 / phases_pd
        frequency = phases_pd / 2
    except Exception as e:
        raise Exception("Could not resolve grating frequency, phase_width, n_phases") from e

    # Now resolve resolution
    shape, visual_size, ppd = resolution.resolve(
        shape=shape, visual_size=(min_vis_angle, min_vis_angle), ppd=ppd
    )

    return {
        "shape": shape,
        "visual_size": visual_size,
        "ppd": ppd,
        "frequency": frequency,
        "phase_width": phase_width,
        "n_phases": n_phases,
    }


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
