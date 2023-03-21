import itertools

import numpy as np

from stimupy.components import draw_regions, waves

__all__ = [
    "sine_linear",
    "square_linear",
    # "staircase_linear",
    # "sine_radial",
    # "square_radial",
    # "sine_cityblock",
    # "square_cityblock",
    # "sine_angular",
    # "square_angular",
]


def sine_linear(
    visual_size=None,
    ppd=None,
    shape=None,
    frequency=None,
    n_bars=None,
    bar_width=None,
    period="ignore",
    rotation=0,
    phase_shift=0,
    intensities=(0.0, 1.0),
    target_indices=(),
    intensity_target=0.5,
    origin="corner",
    round_phase_width=True,
):
    """Linear (horizontal, vertical, oblique) sine-wave grating, with some phase(s) as target(s)

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
    intensities : Sequence[float, float] or None (default)
        min and max intensity of sine-wave
    target_indices : int, or Sequence[int, ...]
        indices segments where targets will be placed
    intensity_target : float, or Sequence[float, ...], optional
        intensity value for each target, by default 0.5.
        Can specify as many intensities as number of target_indices;
        If fewer intensities are passed than target_indices, cycles through intensities
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
        mask with integer index for each target (key: "target_mask"),
        and additional keys containing stimulus parameters
    """
    if len(intensities) != 2:
        raise ValueError("intensities should be [float, float]")

    lst = [visual_size, ppd, shape, frequency, n_bars, bar_width]
    if len([x for x in lst if x is not None]) < 3:
        raise ValueError(
            "'grating' needs 3 non-None arguments for resolving from 'visual_size', "
            "'ppd', 'shape', 'frequency', 'n_bars', 'bar_width'"
        )

    if rotation % 180 == 0.0:
        base_type = "horizontal"
    elif rotation % 180 == 90.0:
        base_type = "vertical"
    else:
        base_type = "rotated"

    # Spatial square-wave grating
    stim = waves.sine(
        visual_size=visual_size,
        ppd=ppd,
        shape=shape,
        frequency=frequency,
        n_phases=n_bars,
        phase_width=bar_width,
        period=period,
        rotation=rotation,
        phase_shift=phase_shift,
        intensities=intensities,
        origin=origin,
        round_phase_width=round_phase_width,
        base_type=base_type,
    )

    # Repackage output
    stim["n_bars"] = stim.pop("n_phases")
    stim["bar_width"] = stim.pop("phase_width")
    stim.pop("base_type")

    # Resolve targets
    if target_indices is not None and target_indices != ():
        # Create target-mask
        if isinstance(target_indices, (int)):
            target_indices = [target_indices]

        targets_mask = np.zeros_like(stim["grating_mask"])
        for target_idx, bar_idx in enumerate(target_indices):
            targets_mask = np.where(
                stim["grating_mask"] == (bar_idx + 1), target_idx + 1, targets_mask
            )
        targets_mask = targets_mask.astype(int)
        stim["target_mask"] = targets_mask

        # Place target(s)
        if isinstance(intensity_target, (int, float)):
            intensities = [intensity_target]
            intensities = itertools.cycle(intensities)
        for target_idx, intensity in zip(np.unique(targets_mask[targets_mask > 0]), intensities):
            stim["img"] = np.where(targets_mask == target_idx, intensity, stim["img"])

    return stim


def square_linear(
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
    target_indices=(),
    intensity_target=0.5,
    origin="corner",
    round_phase_width=True,
):
    """Linear (horizontal, vertical, oblique) square-wave grating (set of bars), with some bar(s) as target(s)

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
    target_indices : int, or Sequence[int, ...]
        indices segments where targets will be placed
    intensity_target : float, or Sequence[float, ...], optional
        intensity value for each target, by default 0.5.
        Can specify as many intensities as number of target_indices;
        If fewer intensities are passed than target_indices, cycles through intensities
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
        mask with integer index for each target (key: "target_mask"),
        and additional keys containing stimulus parameters
    """
    lst = [visual_size, ppd, shape, frequency, n_bars, bar_width]
    if len([x for x in lst if x is not None]) < 3:
        raise ValueError(
            "'grating' needs 3 non-None arguments for resolving from 'visual_size', "
            "'ppd', 'shape', 'frequency', 'n_bars', 'bar_width'"
        )

    # Spatial square-wave grating
    stim = waves.square(
        visual_size=visual_size,
        ppd=ppd,
        shape=shape,
        frequency=frequency,
        n_phases=n_bars,
        phase_width=bar_width,
        period=period,
        rotation=rotation,
        phase_shift=phase_shift,
        origin=origin,
        round_phase_width=round_phase_width,
        base_type="rotated",
    )

    # Adjust intensities to passed-in values
    stim["img"] = draw_regions(mask=stim["grating_mask"], intensities=intensity_bars)

    # Repackage output
    stim["n_bars"] = stim.pop("n_phases")
    stim["bar_width"] = stim.pop("phase_width")
    stim["intensity_bars"] = stim.pop("intensities")
    stim.pop("base_type")

    # Resolve targets
    if target_indices is not None and target_indices != ():
        # Create target-mask
        if isinstance(target_indices, (int)):
            target_indices = [target_indices]

        targets_mask = np.zeros_like(stim["grating_mask"])
        for target_idx, bar_idx in enumerate(target_indices):
            targets_mask = np.where(
                stim["grating_mask"] == (bar_idx + 1), target_idx + 1, targets_mask
            )
        targets_mask = targets_mask.astype(int)
        stim["target_mask"] = targets_mask

        # Place target(s)
        if isinstance(intensity_target, (int, float)):
            intensities = [intensity_target]
            intensities = itertools.cycle(intensities)
        for target_idx, intensity in zip(np.unique(targets_mask[targets_mask > 0]), intensities):
            stim["img"] = np.where(targets_mask == target_idx, intensity, stim["img"])

    return stim


def overview(**kwargs):
    """Generate example stimuli from this module

    Returns
    -------
    stims : dict
        dict with all stimuli containing individual stimulus dicts.
    """
    default_params = {"visual_size": 15, "ppd": 30}
    default_params.update(kwargs)

    grating_params = {
        "period": "ignore",
        "phase_shift": 0,
        "round_phase_width": False,
        "target_indices": (0, 5),
    }

    # fmt: off
    stimuli = {
        "sine wave - horizontal": sine_linear(**default_params, **grating_params, bar_width=1, rotation=0),
        "sine wave - vertical": sine_linear(**default_params, **grating_params, bar_width=1, rotation=90),
        "sine wave - oblique": sine_linear(**default_params, **grating_params, bar_width=1, rotation=45),

        "square wave - horizontal": square_linear(**default_params, **grating_params, bar_width=1, rotation=0),
        "square wave - vertical": square_linear(**default_params, **grating_params, bar_width=1, rotation=90),
        "square wave - oblique": square_linear(**default_params, **grating_params, bar_width=1, rotation=45),


        # "sine wave - radial": sine(**default_params, **grating_params, base_type="radial"),
        # "sine wave - angular": sine(**default_params, **grating_params, base_type="angular"),
        # "sine wave - cityblock": sine(**default_params, **grating_params, base_type="cityblock"),

        # "square wave - radial": square(**default_params, **grating_params, base_type="radial"),
        # "square wave - angular": square(**default_params, **grating_params, base_type="angular"),
        # "square wave - cityblock": square(**default_params, **grating_params, base_type="cityblock"),

        "square wave - multiple intensitites": square_linear(**default_params, **grating_params, bar_width=3.5, rotation=0, intensity_bars=(0, 0.25, 0.75)),
    }
    # fmt: on

    return stimuli


if __name__ == "__main__":
    from stimupy.utils import plot_stimuli

    stims = overview()
    plot_stimuli(stims, mask=False, save=None)
