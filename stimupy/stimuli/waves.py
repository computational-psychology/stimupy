import itertools

import numpy as np

from stimupy.components import draw_regions, waves
from stimupy.components.shapes import disc, rectangle

__all__ = [
    "sine_linear",
    "square_linear",
    "staircase_linear",
    "sine_radial",
    "square_radial",
    "staircase_radial",
    "sine_rectilinear",
    "square_rectilinear",
    "staircase_rectilinear",
    "sine_angular",
    "square_angular",
    "staircase_angular",
]


def add_targets(wave_stim, target_indices, intensity_target):
    # Create target-mask
    if isinstance(target_indices, (int)):
        target_indices = [target_indices]

    targets_mask = np.zeros_like(wave_stim["grating_mask"])
    for target_idx, bar_idx in enumerate(target_indices):
        targets_mask = np.where(
            wave_stim["grating_mask"] == (bar_idx + 1), target_idx + 1, targets_mask
        )
    targets_mask = targets_mask.astype(int)
    wave_stim["target_mask"] = targets_mask

    # Place target(s)
    if isinstance(intensity_target, (int, float)):
        intensities = [intensity_target]
        intensities = itertools.cycle(intensities)
    for target_idx, intensity in zip(np.unique(targets_mask[targets_mask > 0]), intensities):
        wave_stim["img"] = np.where(targets_mask == target_idx, intensity, wave_stim["img"])

    return wave_stim


def sine_linear(
    visual_size=None,
    ppd=None,
    shape=None,
    frequency=None,
    n_bars=None,
    bar_width=None,
    period="ignore",
    rotation=0.0,
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
    rotation : float, optional
        rotation (in degrees), counterclockwise, by default 0.0 (horizonal)
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
        distance_metric = "horizontal"
    elif rotation % 180 == 90.0:
        distance_metric = "vertical"
    else:
        distance_metric = "oblique"

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
        distance_metric=distance_metric,
    )

    # Repackage output
    stim["n_bars"] = stim.pop("n_phases")
    stim["bar_width"] = stim.pop("phase_width")
    stim.pop("distance_metric")

    # Add targets(?)
    if target_indices is not None and target_indices != ():
        stim = add_targets(stim, target_indices=target_indices, intensity_target=intensity_target)

    stim["target_indices"] = target_indices
    stim["intensity_target"] = intensity_target
    return stim


def square_linear(
    visual_size=None,
    ppd=None,
    shape=None,
    frequency=None,
    n_bars=None,
    bar_width=None,
    period="ignore",
    rotation=0.0,
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
    rotation : float, optional
        rotation (in degrees), counterclockwise, by default 0.0 (horizonal)
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
        distance_metric="oblique",
    )

    # Adjust intensities to passed-in values
    stim["img"] = draw_regions(mask=stim["grating_mask"], intensities=intensity_bars)

    # Repackage output
    stim["n_bars"] = stim.pop("n_phases")
    stim["bar_width"] = stim.pop("phase_width")
    stim["intensity_bars"] = stim.pop("intensities")
    stim.pop("distance_metric")

    # Add targets(?)
    if target_indices is not None and target_indices != ():
        stim = add_targets(stim, target_indices=target_indices, intensity_target=intensity_target)

    stim["target_indices"] = target_indices
    stim["intensity_target"] = intensity_target
    return stim


def staircase_linear(
    visual_size=None,
    ppd=None,
    shape=None,
    frequency=None,
    n_bars=None,
    bar_width=None,
    period="ignore",
    rotation=0.0,
    phase_shift=0,
    intensity_bars=(0.0, 1.0),
    target_indices=(),
    intensity_target=0.5,
    origin="corner",
    round_phase_width=True,
):
    """Linear staircase, with some bar(s) as target(s)

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
    rotation : float, optional
        rotation (in degrees), counterclockwise, by default 0.0 (horizonal)
    phase_shift : float
        phase shift of grating in degrees
    intensity_bars : Sequence[float, float] or Sequence[float, ...]
        min and max intensity of sine-wave, by default (0.0, 1.0).
        Can also specify as many intensities as n_bars
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
    intensity_bars : Sequence[float, ...]
        if len(intensity_bars)==2, intensity range of staircase (default 0.0, 1.0);
        if len(intensity_bars)>2, intensity value for each bar.
        Can specify as many intensity_bars as n_bars.
        If fewer intensity_bars are passed than n_bars, cycles through intensities.


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
    stim = waves.staircase(
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
        distance_metric="oblique",
        intensities=intensity_bars,
    )

    # Repackage output
    stim["n_bars"] = stim.pop("n_phases")
    stim["bar_width"] = stim.pop("phase_width")
    stim["intensity_bars"] = stim.pop("intensities")
    stim.pop("distance_metric")

    # Add targets(?)
    if target_indices is not None and target_indices != ():
        stim = add_targets(stim, target_indices=target_indices, intensity_target=intensity_target)

    stim["target_indices"] = target_indices
    stim["intensity_target"] = intensity_target
    return stim


def sine_radial(
    visual_size=None,
    ppd=None,
    shape=None,
    frequency=None,
    n_rings=None,
    ring_width=None,
    period="ignore",
    rotation=0.0,
    phase_shift=0,
    intensities=(0.0, 1.0),
    target_indices=(),
    intensity_target=0.5,
    origin="mean",
    round_phase_width=True,
    clip=False,
    intensity_background=0.5,
):
    """Circular sine-wave grating (set of rings) over the whole image, with some ring(s) as target(s)

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
    n_rings : int, or None (default)
        number of rings
    ring_width : Number, or None (default)
        width of a single ring, in degrees
    period : "even", "odd", "either" or "ignore" (default)
        ensure whether the grating has "even" number of phases, "odd"
        number of phases, either or whether not to round the number of
        phases ("ignore")
    rotation : float, optional
        rotation (in degrees), counterclockwise, by default 0.0 (horizonal)
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
        if "corner": set origin to upper left corner
        if "mean": set origin to hypothetical image center (default)
        if "center": set origin to real center (closest existing value to mean)
    round_phase_width : Bool
        if True, round width of rings given resolution
    clip : Bool
        if True, clip stimulus to image size (default: False)
    intensity_background : float (optional)
        intensity value of background (if clipped), by default 0.5

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for each target (key: "target_mask"),
        and additional keys containing stimulus parameters
    """
    if len(intensities) != 2:
        raise ValueError("intensity_rings should be [float, float]")

    lst = [visual_size, ppd, shape, frequency, n_rings, ring_width]
    if len([x for x in lst if x is not None]) < 3:
        raise ValueError(
            "'grating' needs 3 non-None arguments for resolving from 'visual_size', "
            "'ppd', 'shape', 'frequency', 'n_rings', 'rings_width'"
        )

    # Spatial square-wave grating
    stim = waves.sine(
        visual_size=visual_size,
        ppd=ppd,
        shape=shape,
        frequency=frequency,
        n_phases=n_rings,
        phase_width=ring_width,
        period=period,
        rotation=rotation,
        phase_shift=phase_shift,
        intensities=intensities,
        origin=origin,
        round_phase_width=round_phase_width,
        distance_metric="radial",
    )

    # Repackage output
    stim["n_rings"] = stim.pop("n_phases")
    stim["ring_width"] = stim.pop("phase_width")
    stim.pop("distance_metric")

    # Clip?
    if clip:
        csize = min(stim["visual_size"]) / 2.0
        circle = disc(
            visual_size=stim["visual_size"],
            ppd=stim["ppd"],
            radius=csize,
            origin=origin,
        )
        stim["img"] = np.where(circle["ring_mask"], stim["img"], intensity_background)
        stim["grating_mask"] = np.where(circle["ring_mask"], stim["grating_mask"], 0)

    # Resolve target parameters
    if target_indices is not None and target_indices != ():
        stim = add_targets(stim, target_indices=target_indices, intensity_target=intensity_target)

    stim["target_indices"] = target_indices
    stim["intensity_target"] = intensity_target
    stim["clip"] = clip
    stim["intensity_background"] = intensity_background
    return stim


def square_radial(
    visual_size=None,
    ppd=None,
    shape=None,
    frequency=None,
    n_rings=None,
    ring_width=None,
    period="ignore",
    rotation=0.0,
    phase_shift=0,
    intensity_rings=(1.0, 0.0),
    target_indices=(),
    intensity_target=0.5,
    origin="mean",
    round_phase_width=True,
    clip=False,
    intensity_background=0.5,
):
    """Circular square-wave grating (set of rings) over the whole image, with some ring(s) as target(s)

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
    n_rings : int, or None (default)
        number of rings in the grating
    ring_width : Number, or None (default)
        width of a single ring, in degrees visual angle
    period : "even", "odd", "either" or "ignore" (default)
        ensure whether the grating has "even" number of phases, "odd"
        number of phases, either or whether not to round the number of
        phases ("ignore")
    rotation : float, optional
        rotation (in degrees), counterclockwise, by default 0.0 (horizonal)
    phase_shift : float
        phase shift of grating in degrees
    intensity_rings : Sequence[float, float]
        intensity value for each ring, by default (1.0, 0.0).
    target_indices : int, or Sequence[int, ...]
        indices segments where targets will be placed
    intensity_target : float, or Sequence[float, ...], optional
        intensity value for each target, by default 0.5.
        Can specify as many intensities as number of target_indices;
        If fewer intensities are passed than target_indices, cycles through intensities
    origin : "corner", "mean" or "center"
        if "corner": set origin to upper left corner
        if "mean": set origin to hypothetical image center (default)
        if "center": set origin to real center (closest existing value to mean)
    round_phase_width : Bool
        if True, round width of rings given resolution
    clip : Bool
        if True, clip stimulus to image size (default: False)
    intensity_background : float (optional)
        intensity value of background (if clipped), by default 0.5

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for each target (key: "target_mask"),
        and additional keys containing stimulus parameters
    """
    lst = [visual_size, ppd, shape, frequency, n_rings, ring_width]
    if len([x for x in lst if x is not None]) < 3:
        raise ValueError(
            "'grating' needs 3 non-None arguments for resolving from 'visual_size', "
            "'ppd', 'shape', 'frequency', 'n_rings', 'ring_width'"
        )

    # Spatial square-wave grating
    stim = waves.square(
        visual_size=visual_size,
        ppd=ppd,
        shape=shape,
        frequency=frequency,
        n_phases=n_rings,
        phase_width=ring_width,
        period=period,
        rotation=rotation,
        phase_shift=phase_shift,
        origin=origin,
        round_phase_width=round_phase_width,
        distance_metric="radial",
    )

    # Adjust intensities to passed-in values
    stim["img"] = draw_regions(mask=stim["grating_mask"], intensities=intensity_rings)

    # Repackage output
    stim["n_rings"] = stim.pop("n_phases")
    stim["ring_width"] = stim.pop("phase_width")
    stim["intensity_rings"] = stim.pop("intensities")
    stim.pop("distance_metric")

    # Clip?
    if clip:
        csize = min(stim["visual_size"]) / 2.0
        circle = disc(
            visual_size=stim["visual_size"],
            ppd=stim["ppd"],
            radius=csize,
            origin=origin,
        )
        stim["img"] = np.where(circle["ring_mask"], stim["img"], intensity_background)
        stim["grating_mask"] = np.where(circle["ring_mask"], stim["grating_mask"], 0)

    # Resolve target parameters
    if target_indices is not None and target_indices != ():
        stim = add_targets(stim, target_indices=target_indices, intensity_target=intensity_target)

    stim["target_indices"] = target_indices
    stim["intensity_target"] = intensity_target
    stim["clip"] = clip
    stim["intensity_background"] = intensity_background
    return stim


def staircase_radial(
    visual_size=None,
    ppd=None,
    shape=None,
    frequency=None,
    n_rings=None,
    ring_width=None,
    period="ignore",
    rotation=0.0,
    phase_shift=0,
    intensity_rings=(1.0, 0.0),
    target_indices=(),
    intensity_target=0.5,
    origin="mean",
    round_phase_width=True,
    clip=False,
    intensity_background=0.5,
):
    """Radial staircase, with some ring(s) as target(s)

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
    n_rings : int, or None (default)
        number of rings in the grating
    ring_width : Number, or None (default)
        width of a single ring, in degrees visual angle
    period : "even", "odd", "either" or "ignore" (default)
        ensure whether the grating has "even" number of phases, "odd"
        number of phases, either or whether not to round the number of
        phases ("ignore")
    rotation : float, optional
        rotation (in degrees), counterclockwise, by default 0.0 (horizonal)
    phase_shift : float
        phase shift of grating in degrees
    intensity_rings : Sequence[float, ...]
        if len(intensity_rings)==2, intensity range of staircase (default 0.0, 1.0);
        if len(intensity_rings)>2, intensity value for each ring.
        Can specify as many intensity_rings as n_rings.
        If fewer intensity_bars are passed than n_rings, cycles through intensities.
    target_indices : int, or Sequence[int, ...]
        indices segments where targets will be placed
    intensity_target : float, or Sequence[float, ...], optional
        intensity value for each target, by default 0.5.
        Can specify as many intensities as number of target_indices;
        If fewer intensities are passed than target_indices, cycles through intensities
    origin : "corner", "mean" or "center"
        if "corner": set origin to upper left corner
        if "mean": set origin to hypothetical image center (default)
        if "center": set origin to real center (closest existing value to mean)
    round_phase_width : Bool
        if True, round width of rings given resolution
    clip : Bool
        if True, clip stimulus to image size (default: False)
    intensity_background : float (optional)
        intensity value of background (if clipped), by default 0.5

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for each target (key: "target_mask"),
        and additional keys containing stimulus parameters
    """
    lst = [visual_size, ppd, shape, frequency, n_rings, ring_width]
    if len([x for x in lst if x is not None]) < 3:
        raise ValueError(
            "'grating' needs 3 non-None arguments for resolving from 'visual_size', "
            "'ppd', 'shape', 'frequency', 'n_rings', 'ring_width'"
        )

    # Spatial square-wave grating
    stim = waves.staircase(
        visual_size=visual_size,
        ppd=ppd,
        shape=shape,
        frequency=frequency,
        n_phases=n_rings,
        phase_width=ring_width,
        period=period,
        rotation=rotation,
        phase_shift=phase_shift,
        origin=origin,
        round_phase_width=round_phase_width,
        distance_metric="radial",
        intensities=intensity_rings,
    )

    # Repackage output
    stim["n_rings"] = stim.pop("n_phases")
    stim["ring_width"] = stim.pop("phase_width")
    stim["intensity_rings"] = stim.pop("intensities")
    stim.pop("distance_metric")

    # Clip?
    if clip:
        csize = min(stim["visual_size"]) / 2.0
        circle = disc(
            visual_size=stim["visual_size"],
            ppd=stim["ppd"],
            radius=csize,
            origin=origin,
        )
        stim["img"] = np.where(circle["ring_mask"], stim["img"], intensity_background)
        stim["grating_mask"] = np.where(circle["ring_mask"], stim["grating_mask"], 0)

    # Resolve target parameters
    if target_indices is not None and target_indices != ():
        stim = add_targets(stim, target_indices=target_indices, intensity_target=intensity_target)

    stim["target_indices"] = target_indices
    stim["intensity_target"] = intensity_target
    stim["clip"] = clip
    stim["intensity_background"] = intensity_background
    return stim


def sine_rectilinear(
    visual_size=None,
    ppd=None,
    shape=None,
    frequency=None,
    n_frames=None,
    frame_width=None,
    period="ignore",
    rotation=0.0,
    phase_shift=0,
    intensities=(0.0, 1.0),
    target_indices=(),
    intensity_target=0.5,
    origin="mean",
    round_phase_width=True,
    clip=False,
    intensity_background=0.5,
):
    """Rectilinear sine-wave grating (set of frames) over the whole image, with some frame(s) as target(s)

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
    n_frames : int, or None (default)
        number of frames
    frame_width : Number, or None (default)
        width of a single frame, in degrees
    period : "even", "odd", "either" or "ignore" (default)
        ensure whether the grating has "even" number of phases, "odd"
        number of phases, either or whether not to round the number of
        phases ("ignore")
    rotation : float, optional
        rotation (in degrees), counterclockwise, by default 0.0 (horizonal)
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
        if "corner": set origin to upper left corner
        if "mean": set origin to hypothetical image center (default)
        if "center": set origin to real center (closest existing value to mean)
    round_phase_width : Bool
        if True, round width of frames given resolution
    clip : Bool
        if True, clip stimulus to image size (default: False)
    intensity_background : float (optional)
        intensity value of background (if clipped), by default 0.5

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for each target (key: "target_mask"),
        and additional keys containing stimulus parameters
    """
    if len(intensities) != 2:
        raise ValueError("intensity_frames should be [float, float]")

    lst = [visual_size, ppd, shape, frequency, n_frames, frame_width]
    if len([x for x in lst if x is not None]) < 3:
        raise ValueError(
            "'grating' needs 3 non-None arguments for resolving from 'visual_size', "
            "'ppd', 'shape', 'frequency', 'n_frames', 'frames_width'"
        )

    # Spatial square-wave grating
    stim = waves.sine(
        visual_size=visual_size,
        ppd=ppd,
        shape=shape,
        frequency=frequency,
        n_phases=n_frames,
        phase_width=frame_width,
        period=period,
        rotation=rotation,
        phase_shift=phase_shift,
        intensities=intensities,
        origin=origin,
        round_phase_width=round_phase_width,
        distance_metric="rectilinear",
    )

    # Repackage output
    stim["n_frames"] = stim.pop("n_phases")
    stim["frame_width"] = stim.pop("phase_width")
    stim.pop("distance_metric")

    # Clip?
    if clip:
        if origin == "corner":
            rsize = min(stim["visual_size"]) / 2
            rect = rectangle(
                visual_size=stim["visual_size"],
                ppd=stim["ppd"],
                rectangle_size=rsize,
                rectangle_position=(0, 0),
            )
        else:
            rsize = min(stim["visual_size"])
            rect = rectangle(
                visual_size=stim["visual_size"],
                ppd=stim["ppd"],
                rectangle_size=rsize,
            )
        stim["img"] = np.where(rect["rectangle_mask"], stim["img"], intensity_background)
        stim["grating_mask"] = np.where(rect["rectangle_mask"], stim["grating_mask"], 0)

    # Add targets(?)
    if target_indices is not None and target_indices != ():
        stim = add_targets(stim, target_indices=target_indices, intensity_target=intensity_target)

    stim["target_indices"] = target_indices
    stim["intensity_target"] = intensity_target
    stim["clip"] = clip
    stim["intensity_background"] = intensity_background
    return stim


def square_rectilinear(
    visual_size=None,
    ppd=None,
    shape=None,
    frequency=None,
    n_frames=None,
    frame_width=None,
    period="ignore",
    rotation=0.0,
    phase_shift=0,
    intensity_frames=(1.0, 0.0),
    target_indices=(),
    intensity_target=0.5,
    origin="mean",
    round_phase_width=True,
    clip=False,
    intensity_background=0.5,
):
    """Rectilinear square-wave grating (set of frames) over the whole image, with
    some frame(s) as target(s)

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
    n_frames : int, or None (default)
        number of frames in the grating
    frame_width : Number, or None (default)
        width of a single frame, in degrees visual angle
    period : "even", "odd", "either" or "ignore" (default)
        ensure whether the grating has "even" number of phases, "odd"
        number of phases, either or whether not to round the number of
        phases ("ignore")
    rotation : float, optional
        rotation (in degrees), counterclockwise, by default 0.0 (horizonal)
    phase_shift : float
        phase shift of grating in degrees
    intensity_frames : Sequence[float, float]
        intensity value for each frame, by default (1.0, 0.0).
    target_indices : int, or Sequence[int, ...]
        indices segments where targets will be placed
    intensity_target : float, or Sequence[float, ...], optional
        intensity value for each target, by default 0.5.
        Can specify as many intensities as number of target_indices;
        If fewer intensities are passed than target_indices, cycles through intensities
    origin : "corner", "mean" or "center"
        if "corner": set origin to upper left corner
        if "mean": set origin to hypothetical image center (default)
        if "center": set origin to real center (closest existing value to mean)
    round_phase_width : Bool
        if True, round width of frames given resolution
    clip : Bool
        if True, clip stimulus to image size (default: False)
    intensity_background : float (optional)
        intensity value of background (if clipped), by default 0.5

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for each target (key: "target_mask"),
        and additional keys containing stimulus parameters
    """
    lst = [visual_size, ppd, shape, frequency, n_frames, frame_width]
    if len([x for x in lst if x is not None]) < 3:
        raise ValueError(
            "'grating' needs 3 non-None arguments for resolving from 'visual_size', "
            "'ppd', 'shape', 'frequency', 'n_frames', 'frame_width'"
        )

    # Spatial square-wave grating
    stim = waves.square(
        visual_size=visual_size,
        ppd=ppd,
        shape=shape,
        frequency=frequency,
        n_phases=n_frames,
        phase_width=frame_width,
        period=period,
        rotation=rotation,
        phase_shift=phase_shift,
        origin=origin,
        round_phase_width=round_phase_width,
        distance_metric="rectilinear",
    )

    # Adjust intensities to passed-in values
    stim["img"] = draw_regions(mask=stim["grating_mask"], intensities=intensity_frames)

    # Repackage output
    stim["n_frames"] = stim.pop("n_phases")
    stim["frame_width"] = stim.pop("phase_width")
    stim["intensity_frames"] = stim.pop("intensities")
    stim.pop("distance_metric")

    # Clip?
    if clip:
        if origin == "corner":
            rsize = min(stim["visual_size"]) / 2
            rect = rectangle(
                visual_size=stim["visual_size"],
                ppd=stim["ppd"],
                rectangle_size=rsize,
                rectangle_position=(0, 0),
            )
        else:
            rsize = min(stim["visual_size"])
            rect = rectangle(
                visual_size=stim["visual_size"],
                ppd=stim["ppd"],
                rectangle_size=rsize,
            )
        stim["img"] = np.where(rect["rectangle_mask"], stim["img"], intensity_background)
        stim["grating_mask"] = np.where(rect["rectangle_mask"], stim["grating_mask"], 0)

    # Add targets(?)
    if target_indices is not None and target_indices != ():
        stim = add_targets(stim, target_indices=target_indices, intensity_target=intensity_target)

    stim["target_indices"] = target_indices
    stim["intensity_target"] = intensity_target
    stim["clip"] = clip
    stim["intensity_background"] = intensity_background
    return stim


def staircase_rectilinear(
    visual_size=None,
    ppd=None,
    shape=None,
    frequency=None,
    n_frames=None,
    frame_width=None,
    period="ignore",
    rotation=0.0,
    phase_shift=0,
    intensity_frames=(0.0, 1.0),
    target_indices=(),
    intensity_target=0.5,
    origin="mean",
    round_phase_width=True,
    clip=False,
    intensity_background=0.5,
):
    """Rectiinear staircase, with some frame(s) as target(s)

    Parameters
    ----------
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
    n_frames : int, or None (default)
        number of frames in the grating
    frame_width : Number, or None (default)
        width of a single frame, in degrees visual angle
    period : "even", "odd", "either" or "ignore" (default)
        ensure whether the grating has "even" number of phases, "odd"
        number of phases, either or whether not to round the number of
        phases ("ignore")
    rotation : float, optional
        rotation (in degrees), counterclockwise, by default 0.0 (horizonal)
    phase_shift : float
        phase shift of grating in degrees
    intensity_frames : Sequence[float, ...]
        if len(intensity_frames)==2, intensity range of staircase (default 0.0, 1.0);
        if len(intensity_frames)>2, intensity value for each frame.
        Can specify as many intensity_frames as n_frames.
        If fewer intensity_frames are passed than n_frames, cycles through intensities.
    target_indices : int, or Sequence[int, ...]
        indices segments where targets will be placed
    intensity_target : float, or Sequence[float, ...], optional
        intensity value for each target, by default 0.5.
        Can specify as many intensities as number of target_indices;
        If fewer intensities are passed than target_indices, cycles through intensities
    origin : "corner", "mean" or "center"
        if "corner": set origin to upper left corner
        if "mean": set origin to hypothetical image center (default)
        if "center": set origin to real center (closest existing value to mean)
    round_phase_width : Bool
        if True, round width of frames given resolution
    clip : Bool
        if True, clip stimulus to image size (default: False)
    intensity_background : float (optional)
        intensity value of background (if clipped), by default 0.5

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for each target (key: "target_mask"),
        and additional keys containing stimulus parameters
    """
    lst = [visual_size, ppd, shape, frequency, n_frames, frame_width]
    if len([x for x in lst if x is not None]) < 3:
        raise ValueError(
            "'grating' needs 3 non-None arguments for resolving from 'visual_size', "
            "'ppd', 'shape', 'frequency', 'n_frames', 'frame_width'"
        )

    # Spatial square-wave grating
    stim = waves.staircase(
        visual_size=visual_size,
        ppd=ppd,
        shape=shape,
        frequency=frequency,
        n_phases=n_frames,
        phase_width=frame_width,
        period=period,
        rotation=rotation,
        phase_shift=phase_shift,
        origin=origin,
        round_phase_width=round_phase_width,
        distance_metric="rectilinear",
        intensities=intensity_frames,
    )

    # Repackage output
    stim["n_frames"] = stim.pop("n_phases")
    stim["frame_width"] = stim.pop("phase_width")
    stim["intensity_frames"] = stim.pop("intensities")
    stim.pop("distance_metric")

    # Clip?
    if clip:
        if origin == "corner":
            rsize = min(stim["visual_size"]) / 2
            rect = rectangle(
                visual_size=stim["visual_size"],
                ppd=stim["ppd"],
                rectangle_size=rsize,
                rectangle_position=(0, 0),
            )
        else:
            rsize = min(stim["visual_size"])
            rect = rectangle(
                visual_size=stim["visual_size"],
                ppd=stim["ppd"],
                rectangle_size=rsize,
            )
        stim["img"] = np.where(rect["rectangle_mask"], stim["img"], intensity_background)
        stim["grating_mask"] = np.where(rect["rectangle_mask"], stim["grating_mask"], 0)

    # Add targets(?)
    if target_indices is not None and target_indices != ():
        stim = add_targets(stim, target_indices=target_indices, intensity_target=intensity_target)

    stim["target_indices"] = target_indices
    stim["intensity_target"] = intensity_target
    stim["clip"] = clip
    stim["intensity_background"] = intensity_background
    return stim


def sine_angular(
    visual_size=None,
    ppd=None,
    shape=None,
    frequency=None,
    n_segments=None,
    segment_width=None,
    period="ignore",
    rotation=0.0,
    phase_shift=0,
    intensities=(0.0, 1.0),
    target_indices=(),
    intensity_target=0.5,
    origin="mean",
    round_phase_width=True,
):
    """Angular sine-wave grating (set of segments) over the whole image, with some segment(s) as target(s)

    Parameters
    ----------
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of image, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of image, in pixels
    frequency : Number, or None (default)
        spatial frequency of grating, in cycles per image
    n_segments : int, or None (default)
        number of segments
    segment_width : Number, or None (default)
        width of a single segment, in degrees
    period : "even", "odd", "either" or "ignore" (default)
        ensure whether the grating has "even" number of phases, "odd"
        number of phases, either or whether not to round the number of
        phases ("ignore")
    rotation : float, optional
        rotation (in degrees), counterclockwise, by default 0.0 (horizonal)
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
        if True, round width of segments given resolution

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for each target (key: "target_mask"),
        and additional keys containing stimulus parameters
    """
    if len(intensities) != 2:
        raise ValueError("intensity_segments should be [float, float]")

    lst = [visual_size, ppd, shape, frequency, n_segments, segment_width]
    if len([x for x in lst if x is not None]) < 3:
        raise ValueError(
            "'grating' needs 3 non-None arguments for resolving from 'visual_size', "
            "'ppd', 'shape', 'frequency', 'n_segments', 'segments_width'"
        )

    # Spatial square-wave grating
    stim = waves.sine(
        visual_size=visual_size,
        ppd=ppd,
        shape=shape,
        frequency=frequency,
        n_phases=n_segments,
        phase_width=segment_width,
        period=period,
        rotation=rotation,
        phase_shift=phase_shift,
        intensities=intensities,
        origin=origin,
        round_phase_width=round_phase_width,
        distance_metric="angular",
    )

    # Repackage output
    stim["n_segments"] = stim.pop("n_phases")
    stim["segment_width"] = stim.pop("phase_width")
    stim.pop("distance_metric")
    stim["target_indices"] = target_indices
    stim["intensity_target"] = intensity_target

    # Resolve target parameters
    if target_indices is not None and target_indices != ():
        if isinstance(target_indices, (int)):
            target_indices = [
                target_indices,
            ]
        if isinstance(intensity_target, (int, float)):
            intensity_target = [
                intensity_target,
            ]
        intensity_target = itertools.cycle(intensity_target)

        # Place target(s)
        targets_mask = np.zeros_like(stim["grating_mask"])
        for target_idx, (segment_idx, intensity) in enumerate(
            zip(target_indices, intensity_target)
        ):
            targets_mask = np.where(
                stim["grating_mask"] == (segment_idx + 1), target_idx + 1, targets_mask
            )
            stim["img"] = np.where(targets_mask == (target_idx + 1), intensity, stim["img"])
        stim["target_mask"] = targets_mask.astype(int)

    return stim


def square_angular(
    visual_size=None,
    ppd=None,
    shape=None,
    frequency=None,
    n_segments=None,
    segment_width=None,
    period="ignore",
    rotation=0.0,
    phase_shift=0,
    intensity_segments=(1.0, 0.0),
    target_indices=(),
    intensity_target=0.5,
    origin="mean",
    round_phase_width=True,
):
    """Angular square-wave grating (set of segments) over the whole image, with some segment(s) as target(s)

    Parameters
    ----------
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of image, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of image, in pixels
    frequency : Number, or None (default)
        spatial frequency of grating, in cycles per image
    n_segments : int, or None (default)
        number of segments in the grating
    segment_width : Number, or None (default)
        width of a single segment, in degrees visual angle
    period : "even", "odd", "either" or "ignore" (default)
        ensure whether the grating has "even" number of phases, "odd"
        number of phases, either or whether not to round the number of
        phases ("ignore")
    rotation : float, optional
        rotation (in degrees), counterclockwise, by default 0.0 (horizonal)
    phase_shift : float
        phase shift of grating in degrees
    intensity_segments : Sequence[float, ...]
        intensity value for each segment, by default (1.0, 0.0).
        Can specify as many intensities as n_segments;
        If fewer intensities are passed than n_segments, cycles through intensities
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
        if True, round width of segments given resolution

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for each target (key: "target_mask"),
        and additional keys containing stimulus parameters
    """
    lst = [visual_size, ppd, shape, frequency, n_segments, segment_width]
    if len([x for x in lst if x is not None]) < 3:
        raise ValueError(
            "'grating' needs 3 non-None arguments for resolving from 'visual_size', "
            "'ppd', 'shape', 'frequency', 'n_segments', 'segment_width'"
        )

    # Spatial square-wave grating
    stim = waves.square(
        visual_size=visual_size,
        ppd=ppd,
        shape=shape,
        frequency=frequency,
        n_phases=n_segments,
        phase_width=segment_width,
        period=period,
        rotation=rotation,
        phase_shift=phase_shift,
        origin=origin,
        round_phase_width=round_phase_width,
        distance_metric="angular",
    )

    # Adjust intensities to passed-in values
    stim["img"] = draw_regions(mask=stim["grating_mask"], intensities=intensity_segments)

    # Repackage output
    stim["n_segments"] = stim.pop("n_phases")
    stim["segment_width"] = stim.pop("phase_width")
    stim["intensity_segments"] = stim.pop("intensities")
    stim.pop("distance_metric")
    stim["target_indices"] = target_indices
    stim["intensity_target"] = intensity_target

    # Resolve target parameters
    if target_indices is not None and target_indices != ():
        if isinstance(target_indices, (int)):
            target_indices = [
                target_indices,
            ]
        if isinstance(intensity_target, (int, float)):
            intensity_target = [
                intensity_target,
            ]
        intensity_target = itertools.cycle(intensity_target)

        # Place target(s)
        targets_mask = np.zeros_like(stim["grating_mask"])
        for target_idx, (segment_idx, intensity) in enumerate(
            zip(target_indices, intensity_target)
        ):
            targets_mask = np.where(
                stim["grating_mask"] == (segment_idx + 1), target_idx + 1, targets_mask
            )
            stim["img"] = np.where(targets_mask == (target_idx + 1), intensity, stim["img"])
        stim["target_mask"] = targets_mask.astype(int)

    return stim


def staircase_angular(
    visual_size=None,
    ppd=None,
    shape=None,
    frequency=None,
    n_segments=None,
    segment_width=None,
    period="ignore",
    rotation=0.0,
    phase_shift=0,
    intensity_segments=(0.0, 1.0),
    target_indices=(),
    intensity_target=0.5,
    origin="center",
    round_phase_width=True,
):
    """Angular staircase, with some segment(s) as target(s)

    Parameters
    ----------
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of image, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of image, in pixels
    frequency : Number, or None (default)
        spatial frequency of grating, in cycles per image
    n_segments : int, or None (default)
        number of segments in the grating
    segment_width : Number, or None (default)
        width of a single segment, in degrees visual angle
    period : "even", "odd", "either" or "ignore" (default)
        ensure whether the grating has "even" number of phases, "odd"
        number of phases, either or whether not to round the number of
        phases ("ignore")
    rotation : float, optional
        rotation (in degrees), counterclockwise, by default 0.0 (horizonal)
    phase_shift : float
        phase shift of grating in degrees
    intensity_segments : Sequence[float, ...]
        if len(intensity_segments)==2, intensity range of staircase (default 0.0, 1.0);
        if len(intensity_segments)>2, intensity value for each segment.
        Can specify as many intensity_segments as n_segments.
        If fewer intensity_segments are passed than n_segments, cycles through intensities.
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
        if True, round width of segments given resolution

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for each target (key: "target_mask"),
        and additional keys containing stimulus parameters
    """
    lst = [visual_size, ppd, shape, frequency, n_segments, segment_width]
    if len([x for x in lst if x is not None]) < 3:
        raise ValueError(
            "'grating' needs 3 non-None arguments for resolving from 'visual_size', "
            "'ppd', 'shape', 'frequency', 'n_segments', 'segment_width'"
        )

    # Spatial square-wave grating
    stim = waves.staircase(
        visual_size=visual_size,
        ppd=ppd,
        shape=shape,
        frequency=frequency,
        n_phases=n_segments,
        phase_width=segment_width,
        period=period,
        rotation=rotation,
        phase_shift=phase_shift,
        origin=origin,
        round_phase_width=round_phase_width,
        distance_metric="angular",
    )

    # Repackage output
    stim["n_segments"] = stim.pop("n_phases")
    stim["segment_width"] = stim.pop("phase_width")
    stim["intensity_segments"] = stim.pop("intensities")
    stim.pop("distance_metric")

    # Add targets(?)
    if target_indices is not None and target_indices != ():
        stim = add_targets(stim, target_indices=target_indices, intensity_target=intensity_target)

    stim["target_indices"] = target_indices
    stim["intensity_target"] = intensity_target
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
    }

    grating_params2 = {
        "period": "ignore",
        "phase_shift": 0,
        "round_phase_width": False,
        "target_indices": (2, 5),
    }

    # fmt: off
    stimuli = {
        "sine_wave_linear": sine_linear(**default_params, **grating_params, bar_width=1, rotation=45),
        "sine_wave_radial": sine_radial(**default_params, **grating_params, ring_width=1),
        "sine_wave_rectilinear": sine_rectilinear(**default_params, **grating_params, frame_width=1),
        "sine_wave_angular": sine_angular(**default_params, **grating_params, n_segments=10),


        "square_wave_linear": square_linear(**default_params, **grating_params, bar_width=1, rotation=45),
        "square_wave_radial": square_radial(**default_params, **grating_params, ring_width=1),
        "square_wave_rectilinear": square_rectilinear(**default_params, **grating_params, frame_width=1, clip=True),
        "square_wave_angular": square_angular(**default_params, **grating_params, n_segments=10),

        "staircase_linear": staircase_linear(**default_params, **grating_params, frequency=0.4),
        "staircase_radial": staircase_radial(**default_params, **grating_params, frequency=0.4),
        "staircase_rectilinear": staircase_rectilinear(**default_params, **grating_params, frequency=0.4),
        "staircase_angular": staircase_angular(**default_params, **grating_params, n_segments=10),

        "sine_wave_linear_with_targets": sine_linear(**default_params, **grating_params2, bar_width=1, rotation=45),
        "sine_wave_radial_with_targets": sine_radial(**default_params, **grating_params2, ring_width=1),
        "sine_wave_rectilinear_with_targets": sine_rectilinear(**default_params, **grating_params2, frame_width=1),
        "sine_wave_angular_with_targets": sine_angular(**default_params, **grating_params2, n_segments=10),


        "square_wave_linear_with_targets": square_linear(**default_params, **grating_params2, bar_width=1, rotation=45),
        "square_wave_radial_with_targets": square_radial(**default_params, **grating_params2, ring_width=1),
        "square_wave_rectilinear_with_targets": square_rectilinear(**default_params, **grating_params2, frame_width=1, clip=True),
        "square_wave_angular_with_targets": square_angular(**default_params, **grating_params2, n_segments=10),

        "staircase_linear_with_targets": staircase_linear(**default_params, **grating_params2, frequency=0.4),
        "staircase_radial_with_targets": staircase_radial(**default_params, **grating_params2, frequency=0.4),
        "staircase_rectilinear_with_targets": staircase_rectilinear(**default_params, **grating_params2, frequency=0.4),
        "staircase_angular_with_targets": staircase_angular(**default_params, **grating_params2, n_segments=10),
    }
    # fmt: on

    return stimuli


if __name__ == "__main__":
    from stimupy.utils import plot_stimuli

    stims = overview()
    plot_stimuli(stims, mask=False, save=None)
