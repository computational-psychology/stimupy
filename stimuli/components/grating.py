import numpy as np
from stimuli.components import draw_regions, mask_elements, resolve_grating_params
from stimuli.utils import resolution

__all__ = [
    "square_wave",
]


def mask_bars(
    edges,
    shape=None,
    visual_size=None,
    ppd=None,
    orientation="horizontal",
    rotation=0.,
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
        origin=(0.0, 0.0),
        shape=shape,
        visual_size=visual_size,
        ppd=ppd,
    )


def square_wave(
    shape=None,
    visual_size=None,
    ppd=None,
    frequency=None,
    n_bars=None,
    bar_width=None,
    period="ignore",
    rotation=0,
    intensity_bars=(1.0, 0.0),
):
    """Draw square-wave grating (set of bars) of given spatial frequency

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
    period : "full", "half", "ignore" (default)
        whether to ensure the grating only has "full" periods,
        half "periods", or no guarantees ("ignore")
    rotation : float
        rotation of grating in degrees
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
    
    alpha = [np.abs(np.cos(np.deg2rad(rotation))),
             np.abs(np.sin(np.deg2rad(rotation)))]
    
    if shape.width is not None:
        length = np.round(alpha[0]*shape.width + alpha[1]*shape.height)
    else:
        length = None
    
    if visual_size.width is not None:
        visual_angle = alpha[0]*visual_size.width + alpha[1]*visual_size.height
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
    )
    length = params["length"]
    ppd_1D = params["ppd"]
    visual_angle = params["visual_angle"]
    
    if shape.width is None:
        shape = (length, length)    # TODO: use trigonometry to calculate actual shape
    
    if visual_size.width is None:
        visual_size = np.array(shape) / ppd_1D
    
    if ppd.horizontal is None:
        ppd = (ppd_1D, ppd_1D)

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
    )

    # Draw image
    stim["img"] = draw_regions(stim["mask"], intensities=intensity_bars)

    return {
        **stim,
        "frequency": params["frequency"],
        "bar_width": params["phase_width"],
        "n_bars": params["n_phases"],
        "period": params["period"],
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
    intensity_range=(0., 1.),
):
    """Draw square-wave grating (set of bars) of given spatial frequency

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
    period : "full", "half", "ignore" (default)
        whether to ensure the grating only has "full" periods,
        half "periods", or no guarantees ("ignore")
    rotation : float
        rotation of grating in degrees
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
    
    alpha = [np.abs(np.cos(np.deg2rad(rotation))),
             np.abs(np.sin(np.deg2rad(rotation)))]
    
    if shape.width is not None:
        length = np.round(alpha[0]*shape.width + alpha[1]*shape.height)
    else:
        length = None
    
    if visual_size.width is not None:
        visual_angle = alpha[0]*visual_size.width + alpha[1]*visual_size.height
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
    )
    length = params["length"]
    ppd_1D = params["ppd"]
    visual_angle = params["visual_angle"]
    
    if shape.width is None:
        shape = (length, length)    # TODO: use trigonometry to calculate actual shape
    
    if visual_size.width is None:
        visual_size = np.array(shape) / ppd_1D
    
    if ppd.horizontal is None:
        ppd = (ppd_1D, ppd_1D)

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
    )

    # Draw image
    stim["img"] = np.sin(params["frequency"] * 2 * np.pi * stim["distances"]) / 2 + 0.5
    stim["img"] = stim["img"] * (intensity_range[1] - intensity_range[0]) + intensity_range[0]

    return {
        **stim,
        "frequency": params["frequency"],
        "bar_width": params["phase_width"],
        "n_bars": params["n_phases"],
        "period": params["period"],
    }


if __name__ == "__main__":
    from stimuli.utils.plotting import plot_stimuli
    rotation = 45

    p1 = {
        "visual_size": (10, 5),
        "ppd": 10,
        "n_bars": 11,
        "rotation": rotation,
    }

    p2 = {
        "visual_size": 5,
        "ppd": 10,
        "frequency": 2,
        # "period": "odd",
        "rotation": rotation,
    }

    p3 = {
        "visual_size": 15,
        "ppd": 10,
        "bar_width": 3.5,
        "period": "odd",
        "rotation": rotation,
    }

    p4 = {
        "visual_size": 15,
        "ppd": 10,
        "bar_width": 3.5,
        "period": "ignore",
        "rotation": rotation,
    }
    
    p5 = {
        "ppd": 20,
        "n_bars": 6,
        "frequency": 2.,
        "period": "ignore",
        "rotation": rotation,
    }

    stims = {
        "n_bars": square_wave(**p1),
        "even": square_wave(**p2),
        "odd": square_wave(**p3),
        "ignore": square_wave(**p4),
        "no_size": square_wave(**p5),
        
        "sine_n_bars": sine_wave(**p1),
        "sine_even": sine_wave(**p2),
        "sine_odd": sine_wave(**p3),
        "sine_ignore": sine_wave(**p4),
        "sine_no_size": sine_wave(**p5),
    }
    plot_stimuli(stims)
