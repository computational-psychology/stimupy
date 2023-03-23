import itertools
import warnings

import numpy as np

from stimupy.components import image_base
from stimupy.stimuli.gratings import squarewave
from stimupy.stimuli.pinwheels import pinwheel as radial
from stimupy.stimuli.waves import square_radial as circular
from stimupy.stimuli.wedding_cakes import wedding_cake
from stimupy.utils import resolution

__all__ = [
    "generalized",
    "white",
    "white_two_rows",
    "anderson",
    "howe",
    "yazdanbakhsh",
    "circular",
    "radial",
    "wedding_cake",
]


def generalized(
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
    target_indices=(),
    intensity_target=0.5,
    target_center_offsets=0,
    target_heights=None,
    origin="corner",
):
    """General function to create White's stimulus

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
    target_height : float, or Sequence[float, ...]
        center offset of targets in degrees visual angle (default: 0)
    target_height : float, or Sequence[float, ...]
        height of targets in degrees visual angle
    origin : "corner", "mean" or "center"
        if "corner": set origin to upper left corner (default)
        if "mean": set origin to hypothetical image center
        if "center": set origin to real center (closest existing value to mean)

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for each target (key: "mask"),
        and additional keys containing stimulus parameters

    References
    ----------
    White, M. (1979).
        A new effect of pattern on perceived lightness.
        Perception, 8(4), 413-416.
        https://doi.org/10.1068/p080413
    """
    if target_heights is None:
        raise ValueError("generalized() missing argument 'target_heights' which is not 'None'")

    # Spatial square-wave grating
    stim = squarewave(
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
    if isinstance(target_heights, (int, float)):
        target_heights = [
            target_heights,
        ]
    if isinstance(target_center_offsets, (int, float)):
        target_center_offsets = [
            target_center_offsets,
        ]
    intensity_target = itertools.cycle(intensity_target)
    target_heights = itertools.cycle(target_heights)
    target_center_offsets = itertools.cycle(target_center_offsets)

    # Resolve resolutions and get distances
    base = image_base(
        visual_size=visual_size,
        ppd=ppd,
        shape=shape,
        rotation=rotation,
        origin="center",
    )
    xx = base["horizontal"]
    yy = base["vertical"]
    theta = np.deg2rad(rotation)
    x = np.round(np.cos(theta) * yy - np.sin(theta) * xx, 8)

    target_zip = zip(target_indices, intensity_target, target_heights, target_center_offsets)

    # Place target(s)
    targets_mask = np.zeros_like(stim["grating_mask"])
    for target_idx, (bar_idx, intensity, height, offset) in enumerate(target_zip):
        mask1 = np.where(x >= offset + height / 2, 0, 1)
        mask2 = np.where(x < offset - height / 2, 0, 1)
        if bar_idx < 0:
            bar_idx = int(stim["n_bars"]) + bar_idx
        mask3 = np.where(stim["grating_mask"] == bar_idx + 1, target_idx + 1, 0)
        targets_mask += mask1 * mask2 * mask3
        stim["img"] = np.where(targets_mask == target_idx + 1, intensity, stim["img"])

    # Update and return stimulus
    stim["target_mask"] = targets_mask.astype(int)
    stim["target_indices"] = target_indices
    stim["intensity_target"] = intensity_target
    stim["target_heights"] = target_heights
    stim["target_center_offsets"] = target_center_offsets
    return stim


def white(
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
    target_height=None,
    origin="corner",
):
    """White's stimulus where all targets are vertically aligned at half the stimulus height

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
    target_height : float, or Sequence[float, ...]
        height of targets in degrees visual angle
    origin : "corner", "mean" or "center"
        if "corner": set origin to upper left corner (default)
        if "mean": set origin to hypothetical image center
        if "center": set origin to real center (closest existing value to mean)

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for each target (key: "mask"),
        and additional keys containing stimulus parameters

    References
    ----------
    White, M. (1979).
        A new effect of pattern on perceived lightness.
        Perception, 8(4), 413-416.
        https://doi.org/10.1068/p080413
    """

    stim = generalized(
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
        target_indices=target_indices,
        intensity_target=intensity_target,
        target_center_offsets=0,
        target_heights=target_height,
        origin=origin,
    )
    return stim


def white_two_rows(
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
    intensity_target=0.5,
    target_indices_top=None,
    target_indices_bottom=None,
    target_center_offset=None,
    target_height=None,
    origin="corner",
):
    """White's stimulus where targets are placed in two rows (top, bottom) that have the same
    distance from the center.

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
    intensity_target : float
        intensity value of target
    target_indices_top : int or tuple of ints
        bar indices where top target(s) will be placed. As many targets as ints.
    target_indices_bottom : int or tuple of ints
        bar indices where bottom target(s) will be placed. As many targets as ints.
    target_center_offset : float
        offset from target centers to image center in degree visual angle.
    target_height : float, or Sequence[float, ...]
        height of targets in degrees visual angle
    origin : "corner", "mean" or "center"
        if "corner": set origin to upper left corner (default)
        if "mean": set origin to hypothetical image center
        if "center": set origin to real center (closest existing value to mean)

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for each target (key: "mask"),
        and additional keys containing stimulus parameters

    References
    ----------
    White, M. (1979).
        A new effect of pattern on perceived lightness.
        Perception, 8(4), 413-416.
        https://doi.org/10.1068/p080413
    """
    if not isinstance(target_center_offset, (float, int)):
        raise ValueError("target_center_offset should be a single float / int")
    if isinstance(target_indices_top, (float, int)):
        target_indices_top = (target_indices_top,)
    if isinstance(target_indices_bottom, (float, int)):
        target_indices_bottom = (target_indices_bottom,)

    target_indices = target_indices_top + target_indices_bottom
    offsets_top = (-target_center_offset,) * len(target_indices_top)
    offsets_bottom = (target_center_offset,) * len(target_indices_bottom)
    target_center_offsets = offsets_top + offsets_bottom

    stim = generalized(
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
        target_indices=target_indices,
        intensity_target=intensity_target,
        target_center_offsets=target_center_offsets,
        target_heights=target_height,
        origin=origin,
    )
    return stim


def anderson(
    visual_size=None,
    ppd=None,
    shape=None,
    frequency=None,
    n_bars=None,
    bar_width=None,
    period="ignore",
    intensity_bars=(0.0, 1.0),
    intensity_target=0.5,
    target_indices_top=None,
    target_indices_bottom=None,
    target_center_offset=0,
    target_height=None,
    intensity_stripes=(1.0, 0.0),
    stripe_center_offset=0,
    stripe_height=None,
):
    """Anderson variation of White's stimulus

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
    intensity_bars : (float, float)
        intensity values of bars
    intensity_target : float
        intensity value of target
    target_indices_top : int or tuple of ints
        bar indices where top target(s) will be placed. As many targets as ints.
    target_indices_bottom : int or tuple of ints
        bar indices where bottom target(s) will be placed. As many targets as ints.
    target_center_offset : float
        offset from target centers to image center in degree visual angle.
    target_height : float, or Sequence[float, ...]
        height of targets in degrees visual angle
    intensity_stripes : (float, float)
        intensity values of horizontal stripes
    stripe_center_offset : float
        offset from stripe centers to image center in degree visual angle.
    stripe_height = float
        stripe height in degrees visual angle

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for each target (key: "mask"),
        and additional keys containing stimulus parameters

    References
    ----------
    Anderson, B. L. (2001).
        Contrasting theories of White's illusion.
        Perception, 30, 1499-1501.
    Blakeslee, B., Pasieka, W., & McCourt, M. E. (2005).
        Oriented multiscale spatial ﬁltering and contrast normalization:
        a parsimonious model of brightness induction in a continuum
        of stimuli including White, Howe and simultaneous brightness contrast.
        Vision Research, 45, 607-615.
    """
    if target_height is None:
        raise ValueError("anderson() missing argument 'target_height' which is not 'None'")
    if stripe_height is None:
        raise ValueError("anderson() missing argument 'stripe_height' which is not 'None'")

    stim = white_two_rows(
        visual_size=visual_size,
        ppd=ppd,
        shape=shape,
        frequency=frequency,
        n_bars=n_bars,
        bar_width=bar_width,
        period=period,
        rotation=0,
        phase_shift=0,
        intensity_bars=intensity_bars,
        intensity_target=intensity_target,
        target_indices_top=target_indices_top,
        target_indices_bottom=target_indices_bottom,
        target_center_offset=target_center_offset,
        target_height=target_height,
        origin="corner",
    )

    img = stim["img"]
    mask = stim["target_mask"]
    soffset = resolution.lengths_from_visual_angles_ppd(stripe_center_offset, np.unique(ppd)[0])
    sheight = resolution.lengths_from_visual_angles_ppd(stripe_height, np.unique(ppd)[0])
    cycle_width = (
        resolution.lengths_from_visual_angles_ppd(1.0 / (frequency * 2), np.unique(ppd)[0]) * 2
    )

    phase_width_px = cycle_width // 2
    height, width = img.shape
    nbars = width // phase_width_px
    ttop, tbot = np.array(target_indices_top), np.array(target_indices_bottom)
    ttop[ttop < 0] = nbars + ttop[ttop < 0]
    tbot[tbot < 0] = nbars + tbot[tbot < 0]

    if sheight / 2.0 > soffset:
        raise ValueError("Stripes overlap! Increase stripe offset or decrease stripe size.")
    if (target_height / 2 - target_center_offset + stripe_height / 2 - stripe_center_offset) > 0:
        raise ValueError(
            "Stripes overlap with targets! Increase stripe or target offsets or"
            "decrease stripe or target size"
        )
    if stripe_center_offset * ppd % 1 != 0:
        offsets_new = soffset / ppd
        warnings.warn(
            f"Stripe offsets rounded because of ppd; {stripe_center_offset} -> {offsets_new}"
        )

    # Add stripe at top
    ystart = height // 2 - soffset - sheight // 2
    img[ystart : ystart + sheight, 0 : phase_width_px * np.min(ttop)] = intensity_stripes[0]
    img[ystart : ystart + sheight, phase_width_px * (np.max(ttop) + 1) : :] = intensity_stripes[0]
    if (ystart < 0) or (ystart + sheight > height):
        raise ValueError("Anderson stripes do not fully fit into stimulus")

    # Add stripe at bottom
    ystart = height // 2 + soffset - sheight // 2
    img[ystart : ystart + sheight, 0 : phase_width_px * np.min(tbot)] = intensity_stripes[1]
    img[ystart : ystart + sheight, phase_width_px * (np.max(tbot) + 1) : :] = intensity_stripes[1]
    if (ystart < 0) or (ystart + sheight > height):
        raise ValueError("Anderson stripes do not fully fit into stimulus")

    stim["img"] = img
    stim["target_mask"] = mask
    stim["intensity_stripes"] = intensity_stripes
    stim["stripe_center_offset"] = stripe_center_offset
    stim["stripe_height"] = stripe_height
    return stim


def howe(
    visual_size=None,
    ppd=None,
    shape=None,
    frequency=None,
    n_bars=None,
    bar_width=None,
    period="ignore",
    intensity_bars=(0.0, 1.0),
    intensity_target=0.5,
    target_indices_top=None,
    target_indices_bottom=None,
    target_center_offset=0,
    target_height=None,
    intensity_stripes=(1.0, 0.0),
):
    """Howe variation of White's stimulus

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
    intensity_bars : (float, float)
        intensity values of bars
    intensity_target : float
        intensity value of target
    target_indices_top : int or tuple of ints
        bar indices where top target(s) will be placed. As many targets as ints.
    target_indices_bottom : int or tuple of ints
        bar indices where bottom target(s) will be placed. As many targets as ints.
    target_center_offset : float
        offset from target centers to image center in degree visual angle.
    target_height : float, or Sequence[float, ...]
        height of targets in degrees visual angle
    intensity_stripes : (float, float)
        intensity values of horizontal stripes

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for each target (key: "mask"),
        and additional keys containing stimulus parameters

    References
    ----------
    Blakeslee, B., Pasieka, W., & McCourt, M. E. (2005).
        Oriented multiscale spatial ﬁltering and contrast normalization:
        a parsimonious model of brightness induction in a continuum
        of stimuli including White, Howe and simultaneous brightness contrast.
        Vision Research, 45, 607-615.
    Howe, P. D. L. (2001).
        A comment on the Anderson (1997), the Todorovic (1997),
        and the Ross nd Pessoa (2000) explanations of White's eﬀect.
        Perception, 30, 1023-1026
    """
    return anderson(
        visual_size=visual_size,
        ppd=ppd,
        shape=shape,
        frequency=frequency,
        n_bars=n_bars,
        bar_width=bar_width,
        period=period,
        intensity_bars=intensity_bars,
        intensity_target=intensity_target,
        target_indices_top=target_indices_top,
        target_indices_bottom=target_indices_bottom,
        target_center_offset=target_center_offset,
        target_height=target_height,
        intensity_stripes=intensity_stripes,
        stripe_center_offset=target_center_offset,
        stripe_height=target_height,
    )


def yazdanbakhsh(
    visual_size=None,
    ppd=None,
    shape=None,
    frequency=None,
    n_bars=None,
    bar_width=None,
    period="ignore",
    intensity_bars=(0.0, 1.0),
    intensity_target=0.5,
    target_indices_top=None,
    target_indices_bottom=None,
    target_center_offset=0,
    target_height=None,
    intensity_stripes=(1.0, 0.0),
    gap_size=None,
):
    """Yazsdanbakhsh variation of White's stimulus

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
    intensity_bars : (float, float)
        intensity values of bars
    intensity_target : float
        intensity value of target
    target_indices_top : int or tuple of ints
        bar indices where top target(s) will be placed. As many targets as ints.
    target_indices_bottom : int or tuple of ints
        bar indices where bottom target(s) will be placed. As many targets as ints.
    target_center_offset : float
        offset from target centers to image center in degree visual angle.
    target_height : float, or Sequence[float, ...]
        height of targets in degrees visual angle
    intensity_stripes : (float, float)
        intensity values of horizontal stripes
    gap_size : float
        size of gap between target and grating bar

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for each target (key: "mask"),
        and additional keys containing stimulus parameters

    References
    ----------
    Yazdanbakhsh, A., Arabzadeh, E., Babadi, B., and Fazl, A. (2002).
        Munker-White-like illusions without T-junctions.
        Perception 31, 711-715. https://doi.org/10.1068/p3348
    """
    if target_height is None:
        raise ValueError("yazdanbakhsh() missing argument 'target_height' which is not 'None'")
    if gap_size is None:
        raise ValueError("yazdanbakhsh() missing argument 'gap_size' which is not 'None'")

    stim = white_two_rows(
        visual_size=visual_size,
        ppd=ppd,
        shape=shape,
        frequency=frequency,
        n_bars=n_bars,
        bar_width=bar_width,
        period=period,
        rotation=0,
        phase_shift=0,
        intensity_bars=intensity_bars,
        intensity_target=intensity_target,
        target_indices_top=target_indices_top,
        target_indices_bottom=target_indices_bottom,
        target_center_offset=target_center_offset,
        target_height=target_height,
        origin="corner",
    )

    img = stim["img"]
    mask = stim["target_mask"]
    gap_size_px = resolution.lengths_from_visual_angles_ppd(gap_size, np.unique(ppd)[0])
    target_offset_px = resolution.lengths_from_visual_angles_ppd(
        target_center_offset, np.unique(ppd)[0]
    )
    tsize_px = resolution.lengths_from_visual_angles_ppd(target_height, np.unique(ppd)[0])
    cycle_width_px = (
        resolution.lengths_from_visual_angles_ppd(1.0 / (stim["frequency"] * 2), np.unique(ppd)[0])
        * 2
    )
    phase_width_px = cycle_width_px // 2
    height, width = img.shape
    nbars = width // phase_width_px
    ttop, tbot = np.array(target_indices_top), np.array(target_indices_bottom)
    ttop[ttop < 0] = nbars + ttop[ttop < 0]
    tbot[tbot < 0] = nbars + tbot[tbot < 0]

    if isinstance(target_indices_top, (float, int)):
        ttop = (ttop,)
    if isinstance(target_indices_bottom, (float, int)):
        tbot = (tbot,)

    if any(t in ttop for t in tbot) and (target_offset_px - tsize_px // 2 - gap_size_px) < 0:
        raise ValueError("Stripes overlap! Replace or decrease targets or decrease stripe size.")

    # Add stripes at top
    ystart = height // 2 - target_offset_px - gap_size_px - tsize_px // 2
    ystart2 = height // 2 - target_offset_px + tsize_px // 2
    for t in ttop:
        img[
            ystart : ystart + gap_size_px, t * phase_width_px : (t + 1) * phase_width_px
        ] = intensity_stripes[0]
        img[
            ystart2 : ystart2 + gap_size_px, t * phase_width_px : (t + 1) * phase_width_px
        ] = intensity_stripes[0]

    # Add stripes at bottom
    ystart = height // 2 + target_offset_px - tsize_px // 2 - gap_size_px
    ystart2 = height // 2 + target_offset_px + tsize_px // 2
    for t in tbot:
        img[
            ystart : ystart + gap_size_px, t * phase_width_px : (t + 1) * phase_width_px
        ] = intensity_stripes[1]
        img[
            ystart2 : ystart2 + gap_size_px, t * phase_width_px : (t + 1) * phase_width_px
        ] = intensity_stripes[1]

    stim["img"] = img
    stim["target_mask"] = mask.astype(int)
    stim["intensity_stripes"] = intensity_stripes
    stim["gap_size"] = gap_size
    return stim


def overview(**kwargs):
    """Generate example stimuli from this module

    Returns
    -------
    stims : dict
        dict with all stimuli containing individual stimulus dicts.
    """
    default_params = {
        "visual_size": 10,
        "ppd": 30,
        "frequency": 0.5,
        "intensity_bars": (1, 0),
    }
    default_params.update(kwargs)

    # fmt: off
    stimuli = {
        "white": white(**default_params, target_indices=(2, -3), target_height=2),
        "white_general": generalized(
            **default_params, target_indices=(1, 3, 5), target_center_offsets=(-1, -3, -1), target_heights=(2, 3, 2)
        ),
        "white_two_rows": white_two_rows(
            **default_params,
            target_indices_top=(2, 4),
            target_indices_bottom=(-2, -4),
            target_height=1,
            target_center_offset=2,
        ),
        "white_anderson": anderson(
            **default_params,
            target_indices_top=3,
            target_indices_bottom=-2,
            target_center_offset=2,
            target_height=2,
            stripe_center_offset=1.5,
            stripe_height=2,
        ),
        "white_howe": howe(
            **default_params,
            target_indices_top=3,
            target_indices_bottom=-2,
            target_center_offset=2,
            target_height=2,
        ),
        "white_yazdanbakhsh": yazdanbakhsh(
            **default_params,
            target_indices_top=3,
            target_indices_bottom=-2,
            target_center_offset=2,
            target_height=2,
            gap_size=0.5,
        ),
    }
    # fmt: on

    return stimuli


if __name__ == "__main__":
    from stimupy.utils import plot_stimuli

    stims = overview()
    plot_stimuli(stims, mask=True, save=None)
