import itertools

import numpy as np

from stimupy.components import combine_masks, draw_regions
from stimupy.components.shapes import rectangle
from stimupy.stimuli.gratings import squarewave
from stimupy.stimuli.pinwheels import pinwheel as angular
from stimupy.stimuli.waves import square_radial as radial
from stimupy.stimuli.wedding_cakes import wedding_cake

__all__ = [
    "generalized",
    "white",
    "white_two_rows",
    "anderson",
    "howe",
    "yazdanbakhsh",
    "angular",
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
    rotation=0.0,
    intensity_bars=(0.0, 1.0),
    target_indices=(),
    intensity_target=0.5,
    target_center_offsets=0,
    target_heights=None,
    origin="corner",
    round_phase_width=True,
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
    rotation : float, optional
        rotation (in degrees), counterclockwise, by default 0.0 (horizonal)
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
    target_center_offsets : float, or Sequence[float, ...]
        center offset of targets in degrees visual angle (default: 0)
    target_heights : float, or Sequence[float, ...]
        height of targets in degrees visual angle
    origin : "corner", "mean" or "center"
        if "corner": set origin to upper left corner (default)
        if "mean": set origin to hypothetical image center
        if "center": set origin to real center (closest existing value to mean)
    round_phase_width : Bool
        if True (default), round phase width of grating

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

    # Spatial square-wave grating
    stim = squarewave(
        visual_size=visual_size,
        ppd=ppd,
        shape=shape,
        frequency=frequency,
        n_bars=n_bars,
        bar_width=bar_width,
        rotation=rotation,
        phase_shift=0,
        period=period,
        intensity_bars=intensity_bars,
        origin=origin,
        round_phase_width=round_phase_width,
    )

    # Resolve target parameters
    if isinstance(target_indices, (int)):
        target_indices = (target_indices,)
    if isinstance(intensity_target, (int, float)):
        intensity_target = (intensity_target,)
    if isinstance(target_heights, (int, float)):
        target_heights = (target_heights,)
    if isinstance(target_center_offsets, (int, float)):
        target_center_offsets = (target_center_offsets,)

    if len(target_indices) != 0 and target_heights is None:
        raise ValueError("generalized() missing argument 'target_heights' which is not 'None'")
    if len(target_indices) == 0 and target_heights is None:
        target_heights = (0,)

    intensity_target = tuple(
        itertools.islice(itertools.cycle(intensity_target), len(target_indices))
    )
    target_heights = tuple(itertools.islice(itertools.cycle(target_heights), len(target_indices)))
    target_center_offsets = tuple(
        itertools.islice(itertools.cycle(target_center_offsets), len(target_indices))
    )

    # Place target(s)
    stim_center = stim["visual_size"].height / 2
    target_zip = zip(target_indices, intensity_target, target_heights, target_center_offsets)
    targets_mask = np.zeros_like(stim["grating_mask"])
    for target_idx, (bar_idx, intensity, height, offset) in enumerate(target_zip):
        # Draw a stripe of target_height x stim_width, at center + offset
        rect = rectangle(
            visual_size=stim["visual_size"],
            ppd=stim["ppd"],
            shape=stim["shape"],
            rectangle_size=(height, stim["visual_size"].width),
            rectangle_position=(stim_center + offset - (height / 2), 0),
            intensity_rectangle=intensity,
        )

        # Find where strip intersects with the target bar
        if bar_idx < 0:
            bar_idx = int(stim["n_bars"]) + bar_idx
        mask = (stim["grating_mask"] == bar_idx + 1) & rect["rectangle_mask"]
        targets_mask = np.where(mask, target_idx + 1, targets_mask)

        # Draw target
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
    rotation=0.0,
    intensity_bars=(1.0, 0.0),
    target_indices=(),
    intensity_target=0.5,
    target_heights=None,
    origin="corner",
    round_phase_width=True,
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
    target_heights : float, or Sequence[float, ...]
        height of targets in degrees visual angle
    origin : "corner", "mean" or "center"
        if "corner": set origin to upper left corner (default)
        if "mean": set origin to hypothetical image center
        if "center": set origin to real center (closest existing value to mean)
    round_phase_width : Bool
        if True (default), round phase width of grating

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
        intensity_bars=intensity_bars,
        target_indices=target_indices,
        intensity_target=intensity_target,
        target_center_offsets=0,
        target_heights=target_heights,
        origin=origin,
        round_phase_width=round_phase_width,
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
    rotation=0.0,
    intensity_bars=(1.0, 0.0),
    intensity_target=0.5,
    target_indices_top=(),
    target_indices_bottom=(),
    target_center_offset=None,
    target_heights=None,
    origin="corner",
    round_phase_width=True,
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
    rotation : float, optional
        rotation (in degrees), counterclockwise, by default 0.0 (horizonal)
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
    target_heights : float, or Sequence[float, ...]
        height of targets in degrees visual angle
    origin : "corner", "mean" or "center"
        if "corner": set origin to upper left corner (default)
        if "mean": set origin to hypothetical image center
        if "center": set origin to real center (closest existing value to mean)
    round_phase_width : Bool
        if True (default), round phase width of grating

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
        intensity_bars=intensity_bars,
        target_indices=target_indices,
        intensity_target=intensity_target,
        target_center_offsets=target_center_offsets,
        target_heights=target_heights,
        origin=origin,
        round_phase_width=round_phase_width,
    )

    stim["target_indices_top"] = target_indices_top
    stim["target_indices_bottom"] = target_indices_bottom
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
    round_phase_width=True,
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
    round_phase_width : Bool
        if True (default), round phase width of grating

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
    if isinstance(stripe_height, (int, float)):
        stripe_height = (stripe_height, stripe_height)

    # Generate White's stimulus with two rows of targets
    stim = white_two_rows(
        visual_size=visual_size,
        ppd=ppd,
        shape=shape,
        frequency=frequency,
        n_bars=n_bars,
        bar_width=bar_width,
        period=period,
        rotation=0.0,
        intensity_bars=intensity_bars,
        intensity_target=intensity_target,
        target_indices_top=target_indices_top,
        target_indices_bottom=target_indices_bottom,
        target_center_offset=target_center_offset,
        target_heights=target_height,
        origin="corner",
        round_phase_width=round_phase_width,
    )

    # Masks for stripes (as rectangles)
    stim_center = stim["visual_size"].height / 2
    stripe_top = rectangle(
        visual_size=stim["visual_size"],
        ppd=stim["ppd"],
        shape=stim["shape"],
        rectangle_size=(stripe_height[0], stim["visual_size"].width),
        rectangle_position=(stim_center - stripe_center_offset - (stripe_height[0] / 2), 0),
    )
    for bar_idx in stim["target_indices_top"]:
        if bar_idx < 0:
            bar_idx = int(stim["n_bars"]) + bar_idx
        stripe_top["rectangle_mask"] = np.where(
            stim["grating_mask"] == bar_idx + 1, 0, stripe_top["rectangle_mask"]
        )

    stripe_bottom = rectangle(
        visual_size=stim["visual_size"],
        ppd=stim["ppd"],
        shape=stim["shape"],
        rectangle_size=(stripe_height[1], stim["visual_size"].width),
        rectangle_position=(stim_center + stripe_center_offset - (stripe_height[1] / 2), 0),
    )
    for bar_idx in stim["target_indices_bottom"]:
        if bar_idx < 0:
            bar_idx = int(stim["n_bars"]) + bar_idx
        stripe_bottom["rectangle_mask"] = np.where(
            stim["grating_mask"] == bar_idx + 1, 0, stripe_bottom["rectangle_mask"]
        )

    try:
        stripes_mask = combine_masks(stripe_top["rectangle_mask"], stripe_bottom["rectangle_mask"])
    except ValueError:
        raise ValueError("Stripes overlap. Increase stripe offset or decrease stripe size.")

    # Combine images
    stripes_img = draw_regions(stripes_mask, intensities=intensity_stripes)
    img = np.where(stripes_mask, stripes_img, stim["img"])
    img = np.where(stim["target_mask"], stim["img"], img)
    stim["img"] = img

    # Output
    stim["stripe_center_offset"] = stripe_center_offset
    stim["stripe_height"] = stripe_height
    stim["stripes_mask"] = stripes_mask
    stim["intensity_stripes"] = intensity_stripes

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
    round_phase_width=True,
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
    round_phase_width : Bool
        if True (default), round phase width of grating

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
        round_phase_width=round_phase_width,
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
    target_heights=None,
    # intensity_stripes=(1.0, 0.0),
    gap_size=None,
    round_phase_width=True,
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
    target_heights : float, or Sequence[float, ...]
        height of targets in degrees visual angle
    gap_size : float
        size of gap between target and grating bar
    round_phase_width : Bool
        if True (default), round phase width of grating

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
    if target_heights is None:
        raise ValueError("yazdanbakhsh() missing argument 'target_heights' which is not 'None'")
    if gap_size is None:
        raise ValueError("yazdanbakhsh() missing argument 'gap_size' which is not 'None'")

    # Generate White's stimulus with two rows of targets
    stim = white_two_rows(
        visual_size=visual_size,
        ppd=ppd,
        shape=shape,
        frequency=frequency,
        n_bars=n_bars,
        bar_width=bar_width,
        period=period,
        rotation=0.0,
        intensity_bars=intensity_bars,
        intensity_target=intensity_target,
        target_indices_top=target_indices_top,
        target_indices_bottom=target_indices_bottom,
        target_center_offset=target_center_offset,
        target_heights=target_heights,
        origin="corner",
        round_phase_width=round_phase_width,
    )

    # Masks for top gaps
    stim_center = stim["visual_size"].height / 2
    gap_top_masks = []
    for t_idx, bar_idx in enumerate(stim["target_indices_top"]):
        height = stim["target_heights"][t_idx]

        # Mask for rectangle
        rect = rectangle(
            visual_size=stim["visual_size"],
            ppd=stim["ppd"],
            shape=stim["shape"],
            rectangle_size=(height + 2 * gap_size, stim["visual_size"].width),
            rectangle_position=(stim_center - target_center_offset - (height / 2) - gap_size, 0),
        )

        # Reduce to just this bar: intersection between rect mask and bar mask
        if bar_idx < 0:
            bar_idx = int(stim["n_bars"]) + bar_idx
        stim["gap_mask"] = (stim["grating_mask"] == bar_idx + 1) & rect["rectangle_mask"]

        # Remove everywhere it intersects with target mask
        stim["gap_mask"] = np.where(stim["target_mask"] == t_idx + 1, 0, stim["gap_mask"])
        gap_top_masks.append(stim["gap_mask"])

    # Masks for bottom gaps
    gap_bottom_masks = []
    for idx, bar_idx in enumerate(stim["target_indices_bottom"]):
        t_idx = idx + len(stim["target_indices_top"])
        height = stim["target_heights"][t_idx]

        # Mask for rectangle
        rect = rectangle(
            visual_size=stim["visual_size"],
            ppd=stim["ppd"],
            shape=stim["shape"],
            rectangle_size=(height + 2 * gap_size, stim["visual_size"].width),
            rectangle_position=(stim_center + target_center_offset - (height / 2) - gap_size, 0),
        )

        # Reduce to just this bar: intersection between rect mask and bar mask
        if bar_idx < 0:
            bar_idx = int(stim["n_bars"]) + bar_idx
        stim["gap_mask"] = (stim["grating_mask"] == bar_idx + 1) & rect["rectangle_mask"]

        # Remove everywhere it intersects with target mask
        stim["gap_mask"] = np.where(stim["target_mask"] == t_idx + 1, 0, stim["gap_mask"])
        gap_bottom_masks.append(stim["gap_mask"])

    stim["gap_mask"] = combine_masks(*gap_top_masks, *gap_bottom_masks)

    # Create stim without targets
    stim_wo = white_two_rows(
        visual_size=visual_size,
        ppd=ppd,
        shape=shape,
        frequency=frequency,
        n_bars=n_bars,
        bar_width=bar_width,
        period=period,
        rotation=0.0,
        intensity_bars=(intensity_bars[1], intensity_bars[0]),
        intensity_target=intensity_target,
        target_center_offset=target_center_offset,
        target_heights=target_heights,
        origin="corner",
        round_phase_width=round_phase_width,
    )

    # Remove information at gaps:
    stim["img"] = np.where(stim["gap_mask"], stim_wo["img"], stim["img"])

    # Output
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
    }
    default_params.update(kwargs)

    # fmt: off
    stimuli = {
        "white": white(**default_params, target_indices=(2, -3), target_heights=2, frequency=0.5,),
        "white_general": generalized(
            **default_params,
            target_indices=(1, 3, 5),
            target_center_offsets=(-1, -3, -1),
            target_heights=(2, 3, 2),
            frequency=0.5,),
        "white_two_rows": white_two_rows(
            **default_params,
            target_indices_top=(2, 4),
            target_indices_bottom=(-2, -4),
            target_heights=1,
            target_center_offset=2,
            frequency=0.5,),
        "white_anderson": anderson(
            **default_params,
            target_indices_top=3,
            target_indices_bottom=-4,
            target_center_offset=2,
            target_height=2,
            stripe_center_offset=1.5,
            stripe_height=2,
            frequency=0.5,),
        "white_howe": howe(
            **default_params,
            target_indices_top=3,
            target_indices_bottom=-4,
            target_center_offset=2,
            target_height=2,
            frequency=0.5,),
        "white_yazdanbakhsh": yazdanbakhsh(
            **default_params,
            target_indices_top=2,
            target_indices_bottom=-3,
            target_center_offset=2,
            target_heights=2,
            gap_size=0.5,
            frequency=0.5,),
        "white_angular": angular(
            **default_params,
            n_segments=10,
            target_indices=(1, 6),
            target_width=1,),
        "white_radial": radial(
            **default_params,
            frequency=0.5,
            target_indices=(1, 4),
            clip=True),
        "white_wedding_cake": wedding_cake(
            **default_params,
            L_size=(4, 2.5, 0.5),
            target_height=2,
            target_indices1=((1, 4), (1, 3)),
            target_indices2=((1, 0), (1, 1)),)
    }
    # fmt: on

    return stimuli


if __name__ == "__main__":
    from stimupy.utils import plot_stimuli

    stims = overview()
    plot_stimuli(stims, mask=False, save=None)
