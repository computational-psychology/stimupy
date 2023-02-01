import itertools
import numpy as np
from scipy.ndimage import gaussian_filter
import warnings

from stimuli.components.gratings import square_wave as square_wave_component
from stimuli.components.gratings import sine_wave
from stimuli.components.shapes import parallelogram, rectangle
from stimuli.utils import pad_dict_to_visual_size, pad_dict_to_shape, resolution

__all__ = [
    "square_wave",
    "uniform",
    "grating_masked",
    "grating",
    "counterphase_induction",
    "induction",
    "induction_blur",
]


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
    target_indices=(),
    intensity_target=0.5,
    origin="corner",
):
    """Spatial square-wave grating (set of bars), with some bar(s) as target(s)

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

    Returns
    ----------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for each target (key: "target_mask"),
        and additional keys containing stimulus parameters
    """

    # Spatial square-wave grating
    stim = square_wave_component(
        visual_size=visual_size,
        ppd=ppd,
        shape=shape,
        frequency=frequency,
        n_bars=n_bars,
        bar_width=bar_width,
        rotation=rotation,
        phase_shift=phase_shift,
        period=period,
        intensity_bars=intensity_bars,
        origin=origin,
        round_phase_width=True,
    )

    # Resolve target parameters
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
    for target_idx, (bar_idx, intensity) in enumerate(zip(target_indices, intensity_target)):
        targets_mask = np.where(stim["grating_mask"] == bar_idx, target_idx + 1, targets_mask)
        stim["img"] = np.where(targets_mask == target_idx + 1, intensity, stim["img"])

    # Update and return stimulus
    stim["target_mask"] = targets_mask.astype(int)
    return stim


def uniform(
    visual_size=None,
    ppd=None,
    shape=None,
    grating_size=None,
    frequency=None,
    n_bars=None,
    bar_width=None,
    period="ignore",
    rotation=0,
    phase_shift=0,
    intensity_bars=(1.0, 0.0),
    target_indices=(),
    intensity_target=0.5,
    intensity_background=0.5,
    origin="corner",
):
    """Spatial square-wave grating (set of bars), on a background

    Parameters
    ----------
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of image, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of image, in pixels
    grating_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of grating, in degrees
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
    intensity_background = float
        intensity value of background
    origin : "corner", "mean" or "center"
        if "corner": set origin to upper left corner (default)
        if "mean": set origin to hypothetical image center
        if "center": set origin to real center (closest existing value to mean)

    Returns
    ----------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for each target (key: "target_mask"),
        and additional keys containing stimulus parameters

    References
    ----------
    White, M. (1981). The effect of the nature of the surround on the perceived
        lightness of grey bars within square-wave test gratings. Perception, 10(2),
        215–230. https://doi.org/10.1068/p100215
    """

    # Resolve resolution
    shape, visual_size, ppd = resolution.resolve(shape=shape, visual_size=visual_size, ppd=ppd)

    # Spatial square-wave grating
    stim = square_wave(
        visual_size=grating_size,
        ppd=ppd,
        frequency=frequency,
        n_bars=n_bars,
        bar_width=bar_width,
        period=period,
        rotation=rotation,
        phase_shift=phase_shift,
        intensity_bars=intensity_bars,
        target_indices=target_indices,
        intensity_target=intensity_target,
        origin=origin,
    )

    # Padding
    stim = pad_dict_to_visual_size(stim, visual_size=visual_size, ppd=ppd, pad_value=intensity_background)

    # Repack
    stim.update(
        intensity_background=intensity_background,
        grating_size=stim["visual_size"],
        grating_shape=stim["shape"],
        shape=stim["img"].shape,
        visual_size=visual_size,
    )

    return stim


def grating_masked(
    small_grating_params,
    large_grating_params,
    mask_size=None,
    mask_rotation=None,
):
    """Grating with a parallelogram-like shape on a grating

    Parameters
    ----------
    small_grating_params : dict
        kwargs to generate small grating
    large_grating_params : dict
        kwargs to generate larger grating
    mask_size : Sequence[Number, Number, Number], Sequence[Number, Number], Number or None (default)
        size (height, width, depth) of parallelogram-like mask in degrees visual angle
    mask_rotation: float
        rotation of the mask in degree

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for each bar (key: "target_mask"),
        and additional keys containing stimulus parameters

    References
    ----------
    White, M. (1981). The effect of the nature of the surround on the perceived
        lightness of grey bars within square-wave test gratings. Perception, 10(2),
        215–230. https://doi.org/10.1068/p100215
    """
        
    # Create gratings
    small_grating = square_wave(**small_grating_params)
    large_grating = square_wave(**large_grating_params)
    
    if small_grating["ppd"] != large_grating["ppd"]:
        raise ValueError("Gratings must have same ppd")
    
    if mask_size is None:
        mask_size = small_grating["visual_size"]
    if mask_rotation is None:
        mask_rotation = 0

    window = parallelogram(
        ppd=small_grating["ppd"],
        shape=large_grating["shape"],
        parallelogram_size=mask_size,
        rotation=mask_rotation,
        )["img"]
    
    small_grating = pad_dict_to_shape(small_grating, large_grating["shape"])
    img = np.where(window, small_grating["img"], large_grating["img"])
    mask = np.where(window, small_grating["target_mask"], 0)

    stim = {
        "img": img,
        "target_mask": mask.astype(int),
        "bar_width_small": small_grating["bar_width"],
        "bar_width_large": large_grating["bar_width"],
    }
    return stim


def grating(
    small_grating_params,
    large_grating_params,
):
    """Grating on a grating

    Parameters
    ----------
    small_grating_params : dict
        kwargs to generate small grating
    large_grating_params : dict
        kwargs to generate larger grating

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for each target (key: "target_mask"),
        and additional keys containing stimulus parameters

    References
    ----------
    White, M. (1981). The effect of the nature of the surround on the perceived
        lightness of grey bars within square-wave test gratings. Perception, 10(2),
        215–230. https://doi.org/10.1068/p100215
    """

    stim = grating_masked(
        small_grating_params,
        large_grating_params,
        )
    return stim


def counterphase_induction(
    visual_size=None,
    ppd=None,
    shape=None,
    frequency=None,
    n_bars=None,
    bar_width=None,
    period="ignore",
    orientation="horizontal",
    phase_shift=0,
    intensity_bars=(1.0, 0.0),
    target_size=None,
    target_phase_shift=0,
    intensity_target=0.5,
    origin="corner",
):
    if orientation == "horizontal":
        rotation = 0
    elif orientation == "vertical":
        rotation = 90
    else:
        raise ValueError("orientation must be horizontal or vertical")
    
    # Spatial square-wave grating
    stim = square_wave_component(
        visual_size=visual_size,
        ppd=ppd,
        shape=shape,
        frequency=frequency,
        n_bars=n_bars,
        bar_width=bar_width,
        rotation=rotation,
        phase_shift=phase_shift,
        period=period,
        intensity_bars=intensity_bars,
        origin=origin,
        round_phase_width=True,
    )
    
    stim_target = square_wave_component(
        visual_size=target_size,
        ppd=stim["ppd"],
        bar_width=stim["bar_width"],
        rotation=rotation,
        phase_shift=0,
        period=period,
        intensity_bars=(intensity_target, 0),
        origin=origin,
        round_phase_width=True,
    )
    stim_target = pad_dict_to_shape(stim_target, stim["shape"], 0)
    cycle_px = stim_target["bar_width"] * stim_target["ppd"][0] * 2

    # Translate phase information into pixels
    target_phasea = np.abs(target_phase_shift)
    target_phasea = target_phasea % 360
    target_amount = target_phasea / 360.
    target_shift = target_amount * cycle_px
    target_shifti = int(np.round(target_shift))
    target_phasei = target_shifti / cycle_px * 360
    
    if target_shift != int(target_shift):
        s = np.sign(target_phase_shift)
        warnings.warn(f"Rounding phase; {target_phase_shift} -> {s*target_phasei}")

    # Shift targets by specified phase
    cy, cx = stim["shape"]
    if target_phase_shift < 0:
        if orientation == "horizontal":
            stim_target["img"][:, 0:cx-target_shifti] = stim_target["img"][:, target_shifti::]
            stim_target["grating_mask"][:, 0:cx-target_shifti] = stim_target["grating_mask"][:, target_shifti::]
        elif orientation == "vertical":
            stim_target["img"][0:cx-target_shifti, :] = stim_target["img"][target_shifti::, :]
            stim_target["grating_mask"][0:cx-target_shifti, :] = stim_target["grating_mask"][target_shifti::, :]
    else:
        if orientation == "horizontal":
            stim_target["img"][:, target_shifti::] = stim_target["img"][:, 0:cx-target_shifti]
            stim_target["grating_mask"][:, target_shifti::] = stim_target["grating_mask"][:, 0:cx-target_shifti]
        elif orientation == "vertical":
            stim_target["img"][target_shifti::, :] = stim_target["img"][0:cx-target_shifti, :]
            stim_target["grating_mask"][target_shifti::, :] = stim_target["grating_mask"][0:cx-target_shifti, :]

    # Add targets on grating
    mask_temp = np.ones(stim["shape"])
    mask_temp[stim_target["img"] == intensity_target] = 0
    img = stim["img"] * mask_temp + stim_target["img"]
    
    # Create target mask
    mask = np.where(stim_target["img"] == intensity_target, stim_target["grating_mask"], 0)
    unique_vals = np.unique(mask)
    for v in range(len(unique_vals)):
        mask[mask == unique_vals[v]] = v

    stim["img"] = img
    stim["target_mask"] = mask.astype(int)
    stim["target_phase_shift"] = target_phasei
    stim["target_size"] = stim_target["visual_size"]
    return stim


def induction(
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
    target_width=0.5,
    intensity_target=0.5,
    origin="corner",
):
    """
    Grating induction illusion using a sine-wave grating

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
    target_width : float
        width of target stripe in degrees visual angle
    intensity_target : float, or Sequence[float, ...], optional
        intensity value for each target, by default 0.5.
        Can specify as many intensities as number of target_indices;
        If fewer intensities are passed than target_indices, cycles through intensities
    origin : "corner", "mean" or "center"
        if "corner": set origin to upper left corner (default)
        if "mean": set origin to hypothetical image center
        if "center": set origin to real center (closest existing value to mean)

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for each target (key: "target_mask"),
        and additional keys containing stimulus parameters

    References
    ----------
    McCourt, M. E. (1982). A spatial frequency dependent grating-induction effect.
        Vision Research, 22, 119–134. https://doi.org/10.1016/0042-6989(82)90173-0
    """

    # Draw grating
    stim = sine_wave(
        shape=shape,
        visual_size=visual_size,
        ppd=ppd,
        frequency=frequency,
        n_bars=n_bars,
        bar_width=bar_width,
        period=period,
        rotation=rotation,
        phase_shift=phase_shift,
        intensity_bars=intensity_bars,
        origin=origin,
    )

    # Identify target region
    rectangle_size = (target_width, stim["visual_size"].width)

    target_mask = rectangle(
        rectangle_size=rectangle_size,
        ppd=stim["ppd"],
        visual_size=stim["visual_size"],
        intensity_background=0,
        intensity_rectangle=1,
    )

    # Superimpose
    stim["img"] = np.where(target_mask["shape_mask"], intensity_target, stim["img"])
    stim["target_mask"] = np.where(target_mask["shape_mask"], stim["grating_mask"], 0)
    return stim


def induction_blur(
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
    target_width=None,
    target_blur=0,
    intensity_target=0.5,
    origin="corner",
):
    """
    Grating induction illusion using a blurred square-wave grating

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
    target_width : float
        width of target stripe in degrees visual angle
    target_blur : float
        amount of Gaussian blur to blur square-wave grating (default: 0)
    intensity_target : float, or Sequence[float, ...], optional
        intensity value for each target, by default 0.5.
        Can specify as many intensities as number of target_indices;
        If fewer intensities are passed than target_indices, cycles through intensities
    origin : "corner", "mean" or "center"
        if "corner": set origin to upper left corner (default)
        if "mean": set origin to hypothetical image center
        if "center": set origin to real center (closest existing value to mean)

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for each target (key: "target_mask"),
        and additional keys containing stimulus parameters

    References
    ----------
    McCourt, M. E. (1982). A spatial frequency dependent grating-induction effect.
        Vision Research, 22, 119–134. https://doi.org/10.1016/0042-6989(82)90173-0
    """

    # Draw grating
    stim = square_wave_component(
        shape=shape,
        visual_size=visual_size,
        ppd=ppd,
        frequency=frequency,
        n_bars=n_bars,
        bar_width=bar_width,
        period=period,
        rotation=rotation,
        phase_shift=phase_shift,
        intensity_bars=intensity_bars,
        origin=origin,
        round_phase_width=True,
    )
    stim["img"] = gaussian_filter(stim["img"], target_blur)

    # Identify target region
    rectangle_size = (target_width, stim["visual_size"].width)

    target_mask = rectangle(
        rectangle_size=rectangle_size,
        ppd=stim["ppd"],
        visual_size=stim["visual_size"],
        intensity_background=0,
        intensity_rectangle=1,
    )

    # Superimpose
    stim["img"] = np.where(target_mask["shape_mask"], intensity_target, stim["img"])
    stim["target_mask"] = np.where(target_mask["shape_mask"], stim["grating_mask"], 0)
    return stim


if __name__ == "__main__":
    from stimuli.utils import plot_stimuli
    
    params = {
        "ppd": 40,
        "n_bars": 8,
        "bar_width": 1.0,
        }
    
    small_grating = {
        "ppd": 40,
        "bar_width": 1.0,
        "n_bars": 7,
        "intensity_bars": (0.2, 0.8),
        "target_indices": (0, 1, 3, 5, 7),
        }
    
    large_grating = {
        "ppd": 40,
        "bar_width": 1.0,
        "n_bars": 21,
        }

    stims = {
        "square_wave": square_wave(**params, target_indices=(4, 6)),
        "uniform": uniform(**params, visual_size=20, grating_size=5, target_indices=3),
        "grating": grating(large_grating_params=large_grating, small_grating_params=small_grating),
        "grating_masked": grating_masked(large_grating_params=large_grating,
                                         small_grating_params={**small_grating, "rotation": 90},
                                         mask_size=(5, 5, 2)),
        "counterphase_induction": counterphase_induction(**params, target_size=4, target_phase_shift=90),
        "induction": induction(**params, target_width=0.5),
        "induction_blur": induction_blur(**params, target_width=0.5, target_blur=5),
    }

    plot_stimuli(stims, mask=True, save=None)