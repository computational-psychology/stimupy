import numpy as np
import warnings

from stimupy.components import resolve_grating_params, image_base, draw_regions
from stimupy.components.gaussians import gaussian
from stimupy.utils import resolution
from stimupy.utils.contrast_conversions import adapt_intensity_range
from stimupy.utils.utils import round_to_vals

__all__ = [
    "sine_wave",
    "square_wave",
    "staircase",
    "gabor",
    "plaid",
]


def sine_wave(
    visual_size=None,
    ppd=None,
    shape=None,
    frequency=None,
    n_bars=None,
    bar_width=None,
    period="ignore",
    rotation=0,
    phase_shift=0,
    intensity_bars=(0.0, 1.0),
    origin="center",
    round_phase_width=False,
):
    """Draw sine-wave grating (set of bars) of given spatial frequency

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
    intensity_bars : Sequence[float, float]
        min and max intensity of sine-wave, by default (0.0, 1.0)
    origin : "corner", "mean" or "center"
        if "corner": set origin to upper left corner (default)
        if "mean": set origin to hypothetical image center
        if "center": set origin to real center (closest existing value to mean)
    round_phase_width : Bool
        if True, round width of bars given resolution

    Returns
    ----------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for each bar (key: "grating_mask"),
        and additional keys containing stimulus parameters
    """
    
    if len(intensity_bars) != 2:
        raise ValueError("intensity_bars should be [float, float]")

    lst = [visual_size, ppd, shape, frequency, n_bars, bar_width]
    if len([x for x in lst if x is not None]) < 3:
        raise ValueError("'sine_wave()' needs 3 non-None arguments for resolving from 'visual_size', "
                         "'ppd', 'shape', 'frequency', 'n_bars', 'bar_width'")

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
    
    if rotation%90 != 0 and round_phase_width:
        round_phase_width = False
        warnings.warn("Rounding phase width is turned off for oblique gratings")

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
    
    # Set up coordinates
    base = image_base(shape=shape, visual_size=visual_size, ppd=ppd, rotation=rotation, origin=origin)
    distances = base["rotated"]
    distances = np.round(distances, 6)

    # Shift distances minimally to ensure proper behavior
    if origin == "corner":
        distances = adapt_intensity_range(distances, 1e-03, distances.max()-1e-03)
    else:
        distances = adapt_intensity_range(distances, distances.min()-1e-05, distances.max()-1e-05)

    # Draw image
    img = np.sin(params["frequency"] * 2 * np.pi * distances + np.deg2rad(phase_shift))
    img = adapt_intensity_range(img, intensity_bars[0], intensity_bars[1])
    
    # Create mask
    bar_width = params["phase_width"]
    phase_shift_ = (phase_shift%360)/180 * bar_width
    
    if origin == "corner":
        vals = np.arange(distances.min()+bar_width/2, distances.max()+bar_width*2, bar_width)
    else:
        vals = np.arange(distances.min(), distances.max()+bar_width*2, bar_width)

    mask = round_to_vals(distances, np.round(vals-phase_shift_, 6))
    for i, val in enumerate(np.unique(mask)):
        mask = np.where(mask==val, i+1, mask)
    
    # Create stimulus dict
    stim = {
        "img": img,
        "grating_mask": mask.astype(int),
        "visual_size": visual_size,
        "ppd": ppd,
        "shape": shape,
        "rotation": rotation,
        "origin": origin,
        "frequency": params["frequency"],
        "bar_width": bar_width,
        "n_bars": params["n_phases"],
        "period": period,
        "intensity_bars": intensity_bars,
        "phase_shift": phase_shift,
        }
    return stim


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
    intensity_bars : Sequence[float, float]
        min and max intensity of sine-wave, by default (1.0, 0.0)
        Can specify as many intensities as n_bars;
        If fewer intensities are passed than n_bars, cycles through intensities
    origin : "corner", "mean" or "center"
        if "corner": set origin to upper left corner (default)
        if "mean": set origin to hypothetical image center
        if "center": set origin to real center (closest existing value to mean)
    round_phase_width : Bool
        if True, round width of bars given resolution

    Returns
    ----------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for each bar (key: "grating_mask"),
        and additional keys containing stimulus parameters
    """
    intensity_bars = [intensity_bars[1], intensity_bars[0]]
    stim = sine_wave(
        visual_size=visual_size,
        ppd=ppd,
        shape=shape,
        frequency=frequency,
        n_bars=n_bars,
        bar_width=bar_width,
        period=period,
        rotation=rotation,
        phase_shift=phase_shift,
        intensity_bars=intensity_bars,
        origin=origin,
        round_phase_width=round_phase_width,
        )

    # Round sine-wave to create square wave
    stim["img"] = round_to_vals(stim["img"], intensity_bars)
    return stim


def staircase(
    visual_size=None,
    ppd=None,
    shape=None,
    frequency=None,
    n_bars=None,
    bar_width=None,
    period="either",
    rotation=0,
    intensity_bars=(0.0, 1.0),
    round_phase_width=True,
):
    """Draw a luminance staircase

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
    intensity_bars : Sequence[float, ...]
        if len(intensity_bars)==2, intensity range of staircase (default 0.0, 1.0);
        if len(intensity_bars)>2, intensity value for each bar.
        Can specify as many intensities as n_bars.
        If fewer intensities are passed than n_bars, cycles through intensities.
    round_phase_width : Bool
        if True, round width of bars given resolution

    Returns
    ----------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for each bar (key: "grating_mask"),
        and additional keys containing stimulus parameters
    """
    stim = square_wave(
        visual_size=visual_size,
        ppd=ppd,
        shape=shape,
        frequency=frequency,
        n_bars=n_bars,
        bar_width=bar_width,
        period=period,
        rotation=rotation,
        phase_shift=0,
        intensity_bars=(0, 1),
        origin="corner",
        round_phase_width=round_phase_width,
    )
    
    if len(intensity_bars) == 2:
        intensity_bars = np.linspace(intensity_bars[0], intensity_bars[1], int(np.ceil(stim["n_bars"])))
    
    # Use grating_mask to draw staircase
    stim["img"] = draw_regions(mask=stim["grating_mask"], intensities=intensity_bars)
    stim["intensity_bars"] = intensity_bars
    return stim


def gabor(
    visual_size=None,
    ppd=None,
    shape=None,
    frequency=None,
    bar_width=None,
    sigma=None,
    period="ignore",
    rotation=0,
    phase_shift=0,
    intensity_bars=(0.0, 1.0),
    origin="center",
):
    """Draw sine-wave grating (set of bars) of given spatial frequency

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
        mask with integer index for each bar (key: "grating_mask"),
        and additional keys containing stimulus parameters
    """
    if sigma is None:
        raise ValueError("gabor() missing argument 'sigma' which is not 'None'")

    stim = sine_wave(
        visual_size=visual_size,
        ppd=ppd,
        shape=shape,
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
    stim["img"] = (stim["img"] - mean_int) * gaussian_window["img"] + mean_int

    return {
        **stim,
        "sigma": sigma,
        "gaussian_mask": gaussian_window["gaussian_mask"],
    }


def plaid(
    grating_parameters1,
    grating_parameters2,
    weight1=1,
    weight2=1,
    sigma=None,
):
    """Create plaid consisting of two sine-wave gratings

    Parameters
    ----------
    grating_parameters1 : dict
        kwargs to generate first sine-wave grating
    grating_parameters2 : dict
        kwargs to generate second sine-wave grating
    weight1 : float
        weight of first grating (default: 1)
    weight2 : float
        weight of second grating (default: 1)
    sigma : float or (float, float)
        sigma of Gaussian window in degree visual angle (y, x)

    Returns
    ----------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for each bar (key: "grating_mask"),
        and additional keys containing stimulus parameters
    """
    if sigma is None:
        raise ValueError("plaid() missing argument 'sigma' which is not 'None'")

    # Create sine-wave gratings
    grating1 = sine_wave(**grating_parameters1)
    grating2 = sine_wave(**grating_parameters2)

    if grating1["shape"] != grating2["shape"]:
        raise ValueError("Gratings must have the same shape")
    if grating1["ppd"] != grating2["ppd"]:
        raise ValueError("Gratings must have same ppd")
    if grating1["origin"] != grating2["origin"]:
        raise ValueError("Grating origins must be the same")

    # Create Gaussian window
    window = gaussian(
        visual_size=grating1["visual_size"],
        ppd=grating1["ppd"],
        sigma=sigma,
        origin=grating1["origin"],
    )

    img = (weight1 * grating1["img"] + weight2 * grating2["img"]) * window["img"]
    img = img / (weight1 + weight2)

    # Update parameters
    grating1["img"] = img
    grating1["sigma"] = sigma
    grating1["grating_mask2"] = grating2["grating_mask"]
    grating1["frequency2"] = grating2["frequency"]
    grating1["bar_width2"] = grating2["bar_width"]
    grating1["n_bars2"] = grating2["n_bars"]
    grating1["gaussian_mask"] = window["gaussian_mask"]
    return grating1


if __name__ == "__main__":
    from stimupy.utils.plotting import plot_stimuli

    rotation = 90
    origin = "corner"
    phase_shift = 20

    p1 = {
        "visual_size": (10, 5),
        "ppd": 10,
        "n_bars": 11,
        "phase_shift": phase_shift,
    }

    p2 = {
        "visual_size": 5,
        "ppd": 20,
        "frequency": 2,
        "phase_shift": phase_shift,
    }

    p3 = {
        "visual_size": 15,
        "ppd": 10,
        "bar_width": 3.5,
        "period": "odd",
        "phase_shift": phase_shift,
        "origin": origin,
        "rotation": rotation,
    }

    p4 = {
        "visual_size": 15,
        "ppd": 10,
        "bar_width": 3.5,
        "period": "ignore",
        "origin": origin,
        "rotation": rotation + 90,
    }

    p5 = {
        "ppd": 20,
        "n_bars": 5,
        "bar_width": 4,
        "period": "ignore",
    }

    # p6 = {
    #     "visual_size": 4.0,
    #     "ppd": 20,
    #     "bar_width": 0.08,
    # }
    
    p6 = {
        "ppd": 20,
        "bar_width": 0.1,
        "n_bars": 9,
    }

    stims = {
        "n_bars": square_wave(**p1, rotation=rotation, origin=origin),
        "even": square_wave(**p2, rotation=rotation, origin=origin),
        "odd": square_wave(**p3),
        "ignore": square_wave(**p4),
        "no_size": square_wave(**p5, rotation=rotation, origin=origin),
        "tough_params": square_wave(**p6, rotation=rotation, origin=origin),
        "sine_n_bars": sine_wave(**p1, rotation=rotation, origin=origin),
        "sine_even": sine_wave(**p2, rotation=rotation, origin=origin),
        "sine_odd": sine_wave(**p3),
        "sine_ignore": sine_wave(**p4),
        "sine_no_size": sine_wave(**p5, rotation=rotation, origin=origin),
        "gabor_even": gabor(**p2, sigma=1, rotation=rotation, origin=origin),
        "gabor_odd": gabor(**p3, sigma=5),
        "gabor_ignore": gabor(**p4, sigma=3),
        "staircase": staircase(**p5, rotation=rotation),
        "plaid": plaid(p3, p4, sigma=4.0),
    }
    plot_stimuli(stims, mask=False)
