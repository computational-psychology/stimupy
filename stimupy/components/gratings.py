import numpy as np

from stimupy.components import draw_regions, draw_sine_wave
from stimupy.utils.utils import round_to_vals

# import warnings


__all__ = [
    "sine_wave",
    "square_wave",
    "staircase",
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
    -------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for each bar (key: "grating_mask"),
        and additional keys containing stimulus parameters
    """

    if len(intensity_bars) != 2:
        raise ValueError("intensity_bars should be [float, float]")

    lst = [visual_size, ppd, shape, frequency, n_bars, bar_width]
    if len([x for x in lst if x is not None]) < 3:
        raise ValueError(
            "'sine_wave()' needs 3 non-None arguments for resolving from 'visual_size', "
            "'ppd', 'shape', 'frequency', 'n_bars', 'bar_width'"
        )

    sw = draw_sine_wave(
        visual_size=visual_size,
        ppd=ppd,
        shape=shape,
        frequency=frequency,
        n_phases=n_bars,
        phase_width=bar_width,
        period=period,
        rotation=rotation,
        phase_shift=phase_shift,
        intensities=intensity_bars,
        origin=origin,
        round_phase_width=round_phase_width,
        base_type="rotated",
    )

    # Create stimulus dict
    stim = {
        "img": sw["img"],
        "grating_mask": sw["mask"].astype(int),
        "visual_size": sw["visual_size"],
        "ppd": sw["ppd"],
        "shape": sw["shape"],
        "rotation": rotation,
        "origin": origin,
        "frequency": sw["frequency"],
        "bar_width": sw["phase_width"],
        "n_bars": sw["n_phases"],
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
    intensity_bars=(0.0, 1.0),
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
        min and max intensity of square-wave, by default (0.0, 1.0)
    origin : "corner", "mean" or "center"
        if "corner": set origin to upper left corner (default)
        if "mean": set origin to hypothetical image center
        if "center": set origin to real center (closest existing value to mean)
    round_phase_width : Bool
        if True, round width of bars given resolution

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for each bar (key: "grating_mask"),
        and additional keys containing stimulus parameters
    """

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
    -------
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
        intensity_bars = np.linspace(
            intensity_bars[0], intensity_bars[1], int(np.ceil(stim["n_bars"]))
        )

    # Use grating_mask to draw staircase
    stim["img"] = draw_regions(mask=stim["grating_mask"], intensities=intensity_bars)
    stim["intensity_bars"] = intensity_bars
    return stim


if __name__ == "__main__":
    from stimupy.utils.plotting import plot_stimuli

    rotation = 90
    origin = "center"
    phase_shift = 30

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

    p6 = {
        "visual_size": 4.0,
        "ppd": 20,
        "bar_width": 0.08,
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
        "staircase": staircase(**p5, rotation=rotation),
    }
    plot_stimuli(stims, mask=False)
    plot_stimuli(stims, mask=True)
