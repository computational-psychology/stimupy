import itertools

import numpy as np

from stimuli.utils import degrees_to_pixels, resolution


def resolve_grating_params(
    shape=None,
    visual_size=None,
    ppd=None,
    frequency=None,
    n_phases=None,
    phase_width=None,
    period="ignore",
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

    if period not in ["ignore", "full", "half"]:
        raise TypeError(f"period not understood: {period}")

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
    try:
        n_phases, visual_angle, phases_pd = resolution.resolve_1D(
            length=n_phases, visual_angle=visual_size.width, ppd=phases_pd
        )
        phase_width = 1 / phases_pd
        frequency = phases_pd / 2
    except Exception as e:
        raise Exception("Could not resolve grating frequency, phase_width, n_phases") from e

    # Now resolve resolution
    visual_width = visual_size.width if visual_size.width is not None else visual_angle
    visual_height = visual_size.height if visual_size.height is not None else visual_angle
    shape, visual_size, ppd = resolution.resolve(
        shape=shape, visual_size=(visual_height, visual_width), ppd=ppd
    )

    # Check that frequency does not exceed Nyquist limit:
    if frequency > ppd.horizontal / 2:
        raise ValueError(
            f"Grating frequency ({frequency}) should not exceed Nyquist limit"
            f" {ppd.horizontal/2} (ppd/2)"
        )

    # Ensure full/half period:
    # pixels_per_period = resolution.pix_from_visual_angle_ppd_1D(
    #     visual_angle=phase_width * 2, ppd=ppd.horizontal
    # )
    # if pixels_per_period % 2:
    #     frequency_old = frequency
    #     frequency = 1.0 / pixels_per_period * ppd.horizontal
    #     raise ValueError(
    #         "Warning: Square-wave frequency changed"
    #         f" from {frequency_old} to {frequency},"
    #         " to ensure an even-numbered cycle width"
    #     )

    # length = shape.width
    # if period == "full":
    #     length = (length // pixels_per_period) * pixels_per_period
    # elif period == "half":
    #     length = (length // pixels_per_period) * pixels_per_period + pixels_per_period / 2
    # length = int(length)

    return {
        "shape": shape,
        "visual_size": visual_size,
        "ppd": ppd,
        "frequency": frequency,
        "phase_width": phase_width,
        "n_phases": n_phases,
        "period": period,
    }


def mask_bars(
    shape=None,
    visual_size=None,
    ppd=None,
    frequency=None,
    n_bars=None,
    bar_width=None,
    period="ignore",
    orientation="horizontal",
):
    # Resolve params
    params = resolve_grating_params(
        shape=shape,
        visual_size=visual_size,
        n_phases=n_bars,
        phase_width=bar_width,
        ppd=ppd,
        frequency=frequency,
        period=period,
    )
    shape = params["shape"]
    visual_size = params["visual_size"]
    ppd = params["ppd"]

    # Create image-base:
    x = np.linspace(0, visual_size.width, shape.width)
    y = np.linspace(0, visual_size.height, shape.height)
    xx, yy = np.meshgrid(x, y)
    mask = np.zeros(shape, dtype=int)

    # Determine bar edges
    bar_edges = [
        *itertools.accumulate(itertools.repeat(params["phase_width"], int(params["n_phases"])))
    ]

    # Mask bars
    distances = xx
    for idx, edge in zip(reversed(range(len(bar_edges))), reversed(bar_edges)):
        mask[distances <= edge] = int(idx + 1)

    return {
        "mask": mask,
        **params,
    }


def square_wave(
    shape=None,
    visual_size=None,
    ppd=None,
    frequency=None,
    n_bars=None,
    bar_width=None,
    intensity_bars=(0.0, 1.0),
    period="ignore",
):
    """
    Create a horizontal square wave of given spatial frequency.

    Parameters
    ----------
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of image, in pixels
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of image, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    frequency : float
        the spatial frequency of the wave in cycles per degree
    intensities : (float, float)
        intensity values for phases (bars)
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

    # Get bars mask
    stim = mask_bars(
        shape=shape,
        visual_size=visual_size,
        ppd=ppd,
        frequency=frequency,
        n_bars=n_bars,
        bar_width=bar_width,
        period=period,
    )
    mask = stim["mask"]

    # Draw bars
    img = np.zeros(mask.shape)
    ints = [*itertools.islice(itertools.cycle(intensity_bars), len(np.unique(mask)))]
    for bar_idx, intensity in zip(np.unique(mask), ints):
        img = np.where(mask == bar_idx, intensity, img)

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
