import numpy as np

from stimuli.components import draw_regions, mask_elements, resolve_grating_params
from stimuli.components.gaussians import gaussian
from stimuli.utils import resolution

__all__ = [
    "square_wave",
    "sine_wave",
    "gabor",
    "staircase",
]


def mask_bars(
    edges,
    shape=None,
    visual_size=None,
    ppd=None,
    orientation="horizontal",
    rotation=0.0,
    origin="corner",
):
    """Generate mask with integer indices for sequential bars

    Parameters
    ----------
    edges : Sequence[Number, ...]
        upper-limit, in degrees visual angle, of each bar
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of image, in pixels
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of image, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    orientation : "vertical" or "horizontal" (default)
        orientation of the grating
    rotation : float
        rotation of grating in degrees (default: 0)
    origin : "corner", "mean" or "center"
        if "corner": set origin to upper left corner (default)
        if "mean": set origin to hypothetical image center
        if "center": set origin to real center (closest existing value to mean)

    Returns
    ----------
    dict[str, Any]
        mask with integer index for each bar (key: "mask"),
        and additional keys containing stimulus parameters
    """

    return mask_elements(
        edges=edges,
        orientation=orientation,
        rotation=rotation,
        origin=origin,
        shape=shape,
        visual_size=visual_size,
        ppd=ppd,
    )


def shift_edges(
        edges,
        ppd=None,
        phase_shift=None,
        phase_width=None,
        intensity_bars=None,
        origin=None,
        ):
    """Function to shift edges

    Parameters
    ----------
    edges : Sequence[Number, ...]
        upper-limit, in degrees visual angle, of each bar
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    phase_shift : float
        phase shift of grating in degrees
    phase_width : float
        width of individual phase in visual angle
    intensity_bars : Sequence[float, float]
        intensity value for the two bars
    origin : "corner", "mean" or "center"
        if "corner": set origin to upper left corner (default)
        if "mean": set origin to hypothetical image center
        if "center": set origin to real center (closest existing value to mean)

    Returns
    ----------
    Updated edges and intensity_bars
    """

    phase_shift = phase_shift % 360
    edges = np.array(edges)
    
    if phase_shift != 0:
        if phase_shift > 0 and phase_shift <= 180:
            intensity_bars = (intensity_bars[1], intensity_bars[0])
    
        phase_shift_deg = phase_shift * phase_width / 180
        phase_shift_deg = np.round(phase_shift_deg * ppd) / ppd

        edges = edges + phase_shift_deg
        
        if phase_shift > 0 and phase_shift <= 180:
            edges = np.append(phase_shift_deg, edges)
        elif phase_shift > 180:
            edges = np.append([phase_shift_deg - phase_width, phase_shift_deg], edges)

    return list(edges), intensity_bars


def square_wave(
    visual_size=None,
    ppd=None,
    shape=None,
    frequency=None,
    n_bars=None,
    bar_width=None,
    period="ignore",
    rotation=0,
    phase_shift=0,
    intensity_bars=(1.0, 0.0),
    origin="corner",
    round_phase_width=True,
):
    """Draw square-wave grating (set of bars) of given spatial frequency

    Parameters
    ----------
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of image, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of image, in pixels
    frequency : Number, or None (default)
        spatial frequency of grating, in cycles per degree visual angle
    n_bars : int, or None (default)
        number of bars in the grating
    bar_width : Number, or None (default)
        width of a single bar, in degrees visual angle
    period : "even", "odd", "either" or "ignore" (default)
        ensure whether the grating has "even" number of phases, "odd"
        number of phases, either or whether not to round the number of
        phases ("ignore")
    rotation : float
        rotation of grating in degrees (default: 0 = horizontal)
    phase_shift : float
        phase shift of grating in degrees
    intensity_bars : Sequence[float, ...]
        intensity value for each bar, by default (1.0, 0.0).
        Can specify as many intensities as n_bars;
        If fewer intensities are passed than n_bars, cycles through intensities

    Returns
    ----------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for each target (key: "mask"),
        and additional keys containing stimulus parameters
    """

    # Try to resolve resolution
    try:
        shape, visual_size, ppd = resolution.resolve(shape=shape, visual_size=visual_size, ppd=ppd)
    except ValueError:
        ppd = resolution.validate_ppd(ppd)
        shape = resolution.validate_shape(shape)
        visual_size = resolution.validate_visual_size(visual_size)

    alpha = [np.abs(np.cos(np.deg2rad(rotation))), np.abs(np.sin(np.deg2rad(rotation)))]

    if None not in shape:
        length = np.round(alpha[0] * shape.width + alpha[1] * shape.height)
    else:
        length = None

    if None not in visual_size:
        visual_angle = alpha[0] * visual_size.width + alpha[1] * visual_size.height
    else:
        visual_angle = None

    if None not in ppd:
        ppd_1D = ppd.horizontal
    else:
        ppd_1D = None

    # Resolve params
    params = resolve_grating_params(
        length=length,
        visual_angle=visual_angle,
        n_phases=n_bars,
        phase_width=bar_width,
        ppd=ppd_1D,
        frequency=frequency,
        period=period,
        round_phase_width=round_phase_width,
    )
    length = params["length"]
    ppd_1D = params["ppd"]
    visual_angle = params["visual_angle"]

    # Determine size/shape of whole image
    if None in shape:
        shape = [length*alpha[1], length*alpha[0]]
        if np.round(alpha[1], 5) == 0:
            shape[0] = shape[1]
        if np.round(alpha[0], 5) == 0:
            shape[1] = shape[0]

    if None in ppd:
        ppd = (ppd_1D, ppd_1D)

    if None in visual_size:
        visual_size = resolution.visual_size_from_shape_ppd(shape=shape, ppd=ppd)

    shape = resolution.validate_shape(shape)
    visual_size = resolution.validate_visual_size(visual_size)
    ppd = resolution.validate_ppd(ppd)
    
    # Phase shift:
    edges = params["edges"]
    edges, intensities = shift_edges(
        edges=edges,
        ppd=ppd[0],
        phase_shift=phase_shift,
        phase_width=params["phase_width"],
        intensity_bars=intensity_bars,
        origin=origin
        )

    # Get bars mask
    stim = mask_bars(
        edges=edges,
        shape=shape,
        visual_size=visual_size,
        ppd=ppd,
        orientation="rotated",
        rotation=rotation,
        origin=origin,
    )

    # Draw image
    stim["img"] = draw_regions(stim["mask"], intensities=intensities)

    return {
        **stim,
        "frequency": params["frequency"],
        "bar_width": params["phase_width"],
        "n_bars": params["n_phases"],
        "period": params["period"],
        "intensity_bars": intensity_bars,
    }


def sine_wave(
    shape=None,
    visual_size=None,
    ppd=None,
    frequency=None,
    n_bars=None,
    bar_width=None,
    period="ignore",
    rotation=0,
    phase_shift=0,
    intensity_bars=(0.0, 1.0),
    origin="corner",
):
    """Draw sine-wave grating (set of bars) of given spatial frequency

    Parameters
    ----------
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of image, in pixels
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of image, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    frequency : Number, or None (default)
        spatial frequency of grating, in cycles per degree visual angle
    n_bars : int, or None (default)
        number of bars in the grating
    bar_width : Number, or None (default)
        width of a single bar, in degrees visual angle
    period : "even", "odd", "either" or "ignore" (default)
        ensure whether the grating has "even" number of phases, "odd"
        number of phases, either or whether not to round the number of
        phases ("ignore")
    rotation : float
        rotation of grating in degrees (default: 0 = horizontal)
    phase_shift : float
        phase shift of grating in degrees
    intensity_bars : Sequence[float, ...]
        maximal intensity value for each bar, by default (0.0, 1.0).
    origin : "corner", "mean" or "center"
        if "corner": set origin to upper left corner (default)
        if "mean": set origin to hypothetical image center
        if "center": set origin to real center (closest existing value to mean)

    Returns
    ----------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for each target (key: "mask"),
        and additional keys containing stimulus parameters
    """

    # Try to resolve resolution
    try:
        shape, visual_size, ppd = resolution.resolve(shape=shape, visual_size=visual_size, ppd=ppd)
    except ValueError:
        ppd = resolution.validate_ppd(ppd)
        shape = resolution.validate_shape(shape)
        visual_size = resolution.validate_visual_size(visual_size)

    alpha = [np.abs(np.cos(np.deg2rad(rotation))), np.abs(np.sin(np.deg2rad(rotation)))]

    if shape.width is not None:
        length = np.round(alpha[0] * shape.width + alpha[1] * shape.height)
    else:
        length = None

    if visual_size.width is not None:
        visual_angle = alpha[0] * visual_size.width + alpha[1] * visual_size.height
    else:
        visual_angle = None

    if ppd.horizontal is not None:
        ppd_1D = ppd.horizontal
    else:
        ppd_1D = None

    # Resolve params
    params = resolve_grating_params(
        length=length,
        visual_angle=visual_angle,
        n_phases=n_bars,
        phase_width=bar_width,
        ppd=ppd_1D,
        frequency=frequency,
        period=period,
        round_phase_width=False,
    )
    length = params["length"]
    ppd_1D = params["ppd"]
    visual_angle = params["visual_angle"]

    # Determine size/shape of whole image
    if None in shape:
        shape = [length*alpha[1], length*alpha[0]]
        if np.round(alpha[1], 5) == 0:
            shape[0] = shape[1]
        if np.round(alpha[0], 5) == 0:
            shape[1] = shape[0]

    if None in ppd:
        ppd = (ppd_1D, ppd_1D)

    if None in visual_size:
        visual_size = resolution.visual_size_from_shape_ppd(shape=shape, ppd=ppd)

    shape = resolution.validate_shape(shape)
    visual_size = resolution.validate_visual_size(visual_size)
    ppd = resolution.validate_ppd(ppd)

    # Get bars mask
    stim = mask_bars(
        edges=params["edges"],
        shape=shape,
        visual_size=visual_size,
        ppd=ppd,
        orientation="rotated",
        rotation=rotation,
        origin=origin,
    )

    # Draw image
    stim["img"] = np.sin(
        params["frequency"] * 2 * np.pi * stim["distances"] + np.deg2rad(phase_shift)
    )
    stim["img"] = stim["img"] / 2 + 0.5
    stim["img"] = stim["img"] * (intensity_bars[1] - intensity_bars[0]) + intensity_bars[0]

    return {
        **stim,
        "frequency": params["frequency"],
        "bar_width": params["phase_width"],
        "n_bars": params["n_phases"],
        "period": params["period"],
        "phase_shift": phase_shift,
    }


def gabor(
    shape=None,
    visual_size=None,
    ppd=None,
    frequency=None,
    bar_width=None,
    sigma=None,
    period="ignore",
    rotation=0,
    phase_shift=0,
    intensity_bars=(0.0, 1.0),
    origin="mean",
):
    """Draw sine-wave grating (set of bars) of given spatial frequency

    Parameters
    ----------
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of image, in pixels
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of image, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    frequency : Number, or None (default)
        spatial frequency of grating, in cycles per degree visual angle
    bar_width : Number, or None (default)
        width of a single bar, in degrees visual angle
    sigma : float or (float, float)
        sigma of Gaussian in degree visual angle (y, x)
    period : "even", "odd", "either" or "ignore" (default)
        ensure whether the grating has "even" number of phases, "odd"
        number of phases, either or whether not to round the number of
        phases ("ignore")
    rotation : float
        rotation of grating in degrees (default: 0 = horizontal)
    phase_shift : float
        phase shift of grating in degrees
    intensity_bars : Sequence[float, ...]
        maximal intensity value for each bar, by default (0.0, 1.0).
    origin : "corner", "mean" or "center"
        if "corner": set origin to upper left corner
        if "mean": set origin to hypothetical image center (default)
        if "center": set origin to real center (closest existing value to mean)

    Returns
    ----------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for each target (key: "mask"),
        and additional keys containing stimulus parameters
    """
    stim = sine_wave(
        shape=shape,
        visual_size=visual_size,
        ppd=ppd,
        frequency=frequency,
        bar_width=bar_width,
        period=period,
        rotation=rotation,
        phase_shift=phase_shift,
        intensity_bars=intensity_bars,
        origin=origin,
    )

    gaussian_window = gaussian(
        visual_size=visual_size,
        ppd=ppd,
        sigma=sigma,
        origin=origin,
    )
    mean_int = (intensity_bars[0] + intensity_bars[1]) / 2
    stim["img"] = (stim["img"]-mean_int) * gaussian_window["img"] + mean_int

    return {
        **stim,
        "sigma": sigma,
    }


def staircase(
    shape=None,
    visual_size=None,
    ppd=None,
    frequency=None,
    n_bars=None,
    bar_width=None,
    period="either",
    rotation=0,
    intensity_bars=(1.0, 0.0),
):
    """Draw a luminance staircase

    Parameters
    ----------
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of image, in pixels
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of image, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    frequency : Number, or None (default)
        spatial frequency of grating, in cycles per degree visual angle
    n_bars : int, or None (default)
        number of bars in the grating
    bar_width : Number, or None (default)
        width of a single bar, in degrees visual angle
    period : "even", "odd", "either" or "ignore" (default)
        ensure whether the grating has "even" number of phases, "odd"
        number of phases, either or whether not to round the number of
        phases ("ignore")
    rotation : float
        rotation of grating in degrees (default: 0 = horizontal)
    intensity_bars : Sequence[float, ...]
        intensity value for each bar, by default (1.0, 0.0).
        Can specify as many intensities as n_bars;
        If fewer intensities are passed than n_bars, cycles through intensities

    Returns
    ----------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for each target (key: "mask"),
        and additional keys containing stimulus parameters
    """

    # Try to resolve resolution
    try:
        shape, visual_size, ppd = resolution.resolve(shape=shape, visual_size=visual_size, ppd=ppd)
    except ValueError:
        ppd = resolution.validate_ppd(ppd)
        shape = resolution.validate_shape(shape)
        visual_size = resolution.validate_visual_size(visual_size)

    alpha = [np.abs(np.cos(np.deg2rad(rotation))), np.abs(np.sin(np.deg2rad(rotation)))]

    if None not in shape:
        length = np.round(alpha[0] * shape.width + alpha[1] * shape.height)
    else:
        length = None

    if None not in visual_size:
        visual_angle = alpha[0] * visual_size.width + alpha[1] * visual_size.height
    else:
        visual_angle = None

    if None not in ppd:
        ppd_1D = ppd.horizontal
    else:
        ppd_1D = None

    # Resolve params
    params = resolve_grating_params(
        length=length,
        visual_angle=visual_angle,
        n_phases=n_bars,
        phase_width=bar_width,
        ppd=ppd_1D,
        frequency=frequency,
        period=period,
    )
    length = params["length"]
    ppd_1D = params["ppd"]
    visual_angle = params["visual_angle"]

    # Determine size/shape of whole image
    if None in shape:
        shape = [length*alpha[1], length*alpha[0]]
        if np.round(alpha[1], 5) == 0:
            shape[0] = shape[1]
        if np.round(alpha[0], 5) == 0:
            shape[1] = shape[0]

    if None in ppd:
        ppd = (ppd_1D, ppd_1D)

    if None in visual_size:
        visual_size = resolution.visual_size_from_shape_ppd(shape=shape, ppd=ppd)

    shape = resolution.validate_shape(shape)
    visual_size = resolution.validate_visual_size(visual_size)
    ppd = resolution.validate_ppd(ppd)

    # Get bars mask
    stim = mask_bars(
        edges=params["edges"],
        shape=shape,
        visual_size=visual_size,
        ppd=ppd,
        orientation="rotated",
        rotation=rotation,
        origin="corner",
    )

    # Draw image
    if len(intensity_bars) == 2:
        intensity_bars = np.linspace(intensity_bars[0], intensity_bars[1], int(params["n_phases"]))
    stim["img"] = draw_regions(stim["mask"], intensities=intensity_bars)

    return {
        **stim,
        "frequency": params["frequency"],
        "bar_width": params["phase_width"],
        "n_bars": params["n_phases"],
        "period": params["period"],
    }
    return


if __name__ == "__main__":
    from stimuli.utils.plotting import plot_stimuli

    rotation = 45
    origin = "center"
    phase_shift = 0

    p1 = {
        "visual_size": (10, 5),
        "ppd": 10,
        "n_bars": 11,
        "phase_shift": phase_shift,
    }

    p2 = {
        "visual_size": 5,
        "ppd": 10,
        "frequency": 2,
        "phase_shift": phase_shift,
    }

    p3 = {
        "visual_size": 15,
        "ppd": 10,
        "bar_width": 3.5,
        "period": "odd",
        "phase_shift": phase_shift,
    }

    p4 = {
        "visual_size": 15,
        "ppd": 10,
        "bar_width": 3.5,
        "period": "ignore",
    }

    p5 = {
        "ppd": 20,
        "n_bars": 6,
        "frequency": 2.0,
        "period": "ignore",
    }

    stims = {
        "n_bars": square_wave(**p1, rotation=rotation, origin=origin),
        "even": square_wave(**p2, rotation=rotation, origin=origin),
        "odd": square_wave(**p3, rotation=rotation, origin=origin),
        "ignore": square_wave(**p4, rotation=rotation, origin=origin),
        "no_size": square_wave(**p5, rotation=rotation, origin=origin),
        "sine_n_bars": sine_wave(**p1, rotation=rotation, origin=origin),
        "sine_even": sine_wave(**p2, rotation=rotation, origin=origin),
        "sine_odd": sine_wave(**p3, rotation=rotation, origin=origin),
        "sine_ignore": sine_wave(**p4, rotation=rotation, origin=origin),
        "sine_no_size": sine_wave(**p5, rotation=rotation, origin=origin),
        "gabor_even": gabor(**p2, sigma=1, rotation=rotation, origin=origin),
        "gabor_odd": gabor(**p3, sigma=5, rotation=rotation, origin=origin),
        "gabor_ignore": gabor(**p4, sigma=3, rotation=rotation, origin=origin),
        "staircase": staircase(**p5, rotation=rotation),
    }
    plot_stimuli(stims, mask=False)
