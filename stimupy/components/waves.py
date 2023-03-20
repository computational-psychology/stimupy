import itertools
import warnings
from copy import deepcopy

import numpy as np

from stimupy.components import image_base
from stimupy.utils import int_factorize, resolution
from stimupy.utils.contrast_conversions import adapt_intensity_range
from stimupy.utils.utils import round_to_vals


def resolve_grating_params(
    length=None,
    visual_angle=None,
    ppd=None,
    frequency=None,
    n_phases=None,
    phase_width=None,
    period="ignore",
    round_phase_width=True,
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
    length : Number, or None (default)
        lenght of grating, in pixels
    visual_angle :Number, or None (default)
        visual angle of grating, in degrees
    ppd : Number, or None (default)
        pixels per degree along the axis of grating
    frequency : Number, or None (default)
        frequency of grating, in cycles per degree
    n_phases : int, or None (default)
        number of phases (e.g., bars), i.e., half the number of full periods
    phase_width : Number, or None (default)
        extend of a single phase (e.g., bar), in degrees
    period : "even", "odd", "either", "ignore" (default)
        whether to ensure the grating has "even" number of phases,
        "odd" number of phases, or "either" even/odd,
        or no guarantees ("ignore")
    round_phase_width : bool,
        whether to round phase_width to an integer number of pixels, by default True


    Returns
    -------
    dict[str, Any]
        dictionary with all six resolution & size parameters resolved.
    """
    old_frequency = deepcopy(frequency)
    old_n_phases = deepcopy(n_phases)
    old_phase_width = deepcopy(phase_width)

    if period not in ["ignore", "even", "odd", "either"]:
        raise TypeError(f"period not understood: {period}")

    # Try to resolve resolution
    try:
        length, visual_angle, ppd = resolution.resolve_1D(
            length=length, visual_angle=visual_angle, ppd=ppd
        )
    except resolution.TooManyUnknownsError:
        ppd = ppd
        length = length
        visual_angle = visual_angle

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
        n_phases, min_angle, phases_pd = resolution.resolve_1D(
            length=n_phases,
            visual_angle=visual_angle,
            ppd=phases_pd,
            round=False,
        )
    except Exception as e:
        raise Exception("Could not resolve grating frequency, phase_width, n_phases") from e

    # Now resolve resolution
    visual_angle = min_angle if visual_angle is None else visual_angle
    length, visual_angle, ppd = resolution.resolve_1D(
        length=length, visual_angle=visual_angle, ppd=ppd
    )

    # Ensure n phases fit in length?
    if period != "ignore":
        n_phases = round_n_phases(n_phases=n_phases, length=length, period=period)

        # Calculate other params again:
        n_phases, min_angle, phases_pd = resolution.resolve_1D(
            length=n_phases,
            visual_angle=visual_angle,
            ppd=None,
            round=False,
        )

    # Ensure each phase consists of integer number of pixels?
    phase_width = 1 / phases_pd
    if round_phase_width:
        phase_width = np.round(phase_width * ppd) / ppd
        n_phases = length / np.round(phase_width * ppd)

    # Calculate frequency
    frequency = 1 / (2 * phase_width)

    # Check & warn if we changed some params
    if period == "ignore":
        if old_n_phases is not None and n_phases != old_n_phases:
            warnings.warn(
                f"Adjusted n_phases={old_n_phases} -> {n_phases} because of poor resolution"
            )

        if old_phase_width is not None and phase_width != old_phase_width:
            warnings.warn(
                f"Adjusted phase_width={old_phase_width} -> {phase_width} because of poor"
                " resolution"
            )

        if old_frequency is not None and frequency != old_frequency:
            warnings.warn(
                f"Adjusted frequency={old_frequency} -> {frequency} because of poor resolution"
            )
    else:
        if old_n_phases is not None and n_phases != old_n_phases:
            warnings.warn(
                f"Adjusted n_phases={old_n_phases} -> {n_phases} because of period={period}"
            )

        if old_phase_width is not None and phase_width != old_phase_width:
            warnings.warn(
                f"Adjusted phase_width={old_phase_width} -> {phase_width} because of"
                f" period={period}"
            )

        if old_frequency is not None and frequency != old_frequency:
            warnings.warn(
                f"Adjusted frequency={old_frequency} -> {frequency} because of period={period}"
            )

    # Check that frequency does not exceed Nyquist limit:
    if frequency > (ppd / 2):
        raise ValueError(
            f"Grating frequency ({frequency}) should not exceed Nyquist limit {ppd/2} (ppd/2)"
        )

    # Accumulate edges of phases (rounding to avoid accumulation of
    # floating point imprecisions)
    edges = [*itertools.accumulate(itertools.repeat(phase_width, int(np.ceil(n_phases))))]
    edges = np.round(np.array(edges), 8)
    edges = list(edges)

    return {
        "length": length,
        "visual_angle": visual_angle,
        "ppd": ppd,
        "frequency": frequency,
        "phase_width": phase_width,
        "n_phases": n_phases,
        "edges": edges,
        "period": period,
    }


def round_n_phases(n_phases, length, period="either"):
    """Round n_phases of grating to integer, even, or odd -- taking into account pixels

    Finds the nearest integer (optionally limited to even or odd) n_phases
    that length (in pixels) can be divided into.
    Note that this maybe be quite far away from the input.


    Parameters
    ----------
    n_phases : int
        number of phases (e.g., bars), i.e., half the number of full periods
    length : Number
        lenght of grating, in pixels
    period : "even", "odd", "either" (default)
        whether to ensure the grating has "even" number of phases,
        "odd" number of phases, or "either" even/odd

    Returns
    -------
    n_phases : int
        rounded n_phases
    """

    # n_phases has to integer-divide length
    possible_phase_pix = np.array(list(int_factorize(length)))
    possible_n_phases = length / possible_phase_pix

    if period == "even":
        # only look at possible_n_phases that are even
        possible_n_phases = possible_n_phases[possible_n_phases % 2 == 0]
    elif period == "odd":
        # only look at possible_n_phases that are odd
        possible_n_phases = possible_n_phases[possible_n_phases % 2 != 0]

    if len(possible_n_phases) == 0:
        raise ValueError(f"Cannot fit {period} number of phases into {length} px")

    closest = possible_n_phases[np.argmin(np.abs(possible_n_phases - n_phases))]

    return int(closest)


def sine(
    visual_size=None,
    ppd=None,
    shape=None,
    frequency=None,
    n_phases=None,
    phase_width=None,
    period="ignore",
    rotation=None,
    phase_shift=None,
    intensities=None,
    origin=None,
    base_type=None,
    round_phase_width=None,
):
    """Draw a sine-wave grating given a certain base_type

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
    n_phases : int, or None (default)
        number of phases in the grating
    phase_width : Number, or None (default)
        width of a single phase, in degrees visual angle
    period : "even", "odd", "either", "ignore" (default)
        ensure whether the grating has "even" number of phases, "odd"
        number of phases, either or whether not to round the number of
        phases ("ignore")
    rotation : float or None (default)
        rotation of grating in degrees
    phase_shift : float or None (default)
        phase shift of grating in degrees
    intensities : Sequence[float, float] or None (default)
        min and max intensity of sine-wave
    origin : "corner", "mean", "center" or None (default)
        if "corner": set origin to upper left corner
        if "mean": set origin to hypothetical image center
        if "center": set origin to real center (closest existing value to mean)
    base_type : str or None
        if "horizontal", use distance from origin in x-direction,
        if "vertical", use distance from origin in x-direction;
        if "rotated", use combined and rotated distance from origin in x-y;
        if "radial", use radial distance from origin,
        if "angular", use angular distance from origin,
        if "cityblock", use cityblock distance from origin
    round_phase_width : Bool or None (default)
        if True, round width of bars given resolution

    Returns
    ----------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for each bar (key: "grating_mask"),
        and additional keys containing stimulus parameters
    """
    if rotation is None:
        raise ValueError("waves.sine() missing argument 'rotation' which is not 'None'")
    if phase_shift is None:
        raise ValueError("waves.sine() missing argument 'phase_shift' which is not 'None'")
    if intensities is None:
        raise ValueError("waves.sine() missing argument 'intensities' which is not 'None'")
    if origin is None:
        raise ValueError("waves.sine() missing argument 'origin' which is not 'None'")
    if round_phase_width is None:
        raise ValueError("waves.sine() missing argument 'round_phase_width' which is not 'None'")
    if period is None:
        period = "ignore"

    base_types = ["horizontal", "vertical", "rotated", "radial", "angular", "cityblock"]
    if base_type not in base_types:
        raise ValueError(f"base_type needs to be one of {base_types}")

    lst = [visual_size, ppd, shape, frequency, n_phases, phase_width]
    if len([x for x in lst if x is not None]) < 3:
        raise ValueError(
            "'grating()' needs 3 non-None arguments for resolving from 'visual_size', "
            "'ppd', 'shape', 'frequency', 'n_phases', 'phase_width'"
        )

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

    if rotation % 90 != 0 and round_phase_width:
        round_phase_width = False
        warnings.warn("Rounding phase width is turned off for oblique gratings")

    if rotation % 90 != 0 and period != "ignore":
        period = "ignore"
        warnings.warn("Period ignored for oblique gratings")

    # Resolve params
    params = resolve_grating_params(
        length=length,
        visual_angle=visual_angle,
        n_phases=n_phases,
        phase_width=phase_width,
        ppd=ppd_1D,
        frequency=frequency,
        period=period,
        round_phase_width=round_phase_width,
    )
    length = params["length"]
    ppd_1D = params["ppd"]
    visual_angle = params["visual_angle"]
    frequency = params["frequency"]
    phase_width = params["phase_width"]
    n_phases = params["n_phases"]

    # Determine size/shape of whole image
    if None in shape:
        shape = [length * alpha[1], length * alpha[0]]
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
    base = image_base(
        shape=shape, visual_size=visual_size, ppd=ppd, rotation=rotation, origin=origin
    )
    distances = base[base_type]
    distances = np.round(distances, 6)

    # Shift distances minimally to ensure proper behavior
    if origin == "corner":
        distances = adapt_intensity_range(distances, 1e-03, distances.max() - 1e-03)
    else:
        distances = adapt_intensity_range(
            distances, distances.min() - 1e-05, distances.max() - 1e-05
        )

    # Draw image
    img = np.sin(frequency * 2 * np.pi * distances + np.deg2rad(phase_shift))
    img = adapt_intensity_range(img, intensities[0], intensities[1])

    # Create mask
    if origin == "corner" or base_type == "radial" or base_type == "cityblock":
        vals = np.arange(
            distances.min() + phase_width / 2, distances.max() + phase_width * 2, phase_width
        )

        if origin == "mean":
            vals -= distances.min()
    else:
        dmin = distances.min()
        dmax = distances.max() + phase_width * 2
        vals1 = np.arange(0 + phase_width / 2, dmax, phase_width)
        vals2 = -np.arange(-phase_width / 2, -dmin + phase_width, phase_width)
        vals = np.unique(np.append(vals2[::-1], vals1))

    phase_shift_ = (phase_shift % 360) / 180 * phase_width
    mask = round_to_vals(
        distances - distances.min(), np.round(vals - phase_shift_, 6) - distances.min()
    )

    for i, val in enumerate(np.unique(mask)):
        mask = np.where(mask == val, i + 1, mask)

    stim = {
        "img": img,
        "mask": mask.astype(int),
        "visual_size": visual_size,
        "ppd": ppd,
        "shape": shape,
        "frequency": frequency,
        "n_phases": n_phases,
        "phase_width": phase_width,
    }
    return stim


def square(
    visual_size=None,
    ppd=None,
    shape=None,
    frequency=None,
    n_phases=None,
    phase_width=None,
    period="ignore",
    rotation=None,
    phase_shift=None,
    intensities=None,
    origin=None,
    base_type=None,
    round_phase_width=None,
):
    """Draw a sine-wave grating given a certain base_type

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
    n_phases : int, or None (default)
        number of phases in the grating
    phase_width : Number, or None (default)
        width of a single phase, in degrees visual angle
    period : "even", "odd", "either", "ignore" (default)
        ensure whether the grating has "even" number of phases, "odd"
        number of phases, either or whether not to round the number of
        phases ("ignore")
    rotation : float or None (default)
        rotation of grating in degrees
    phase_shift : float or None (default)
        phase shift of grating in degrees
    intensities : Sequence[float, float] or None (default)
        min and max intensity of sine-wave
    origin : "corner", "mean", "center" or None (default)
        if "corner": set origin to upper left corner
        if "mean": set origin to hypothetical image center
        if "center": set origin to real center (closest existing value to mean)
    base_type : str or None
        if "horizontal", use distance from origin in x-direction,
        if "vertical", use distance from origin in x-direction;
        if "rotated", use combined and rotated distance from origin in x-y;
        if "radial", use radial distance from origin,
        if "angular", use angular distance from origin,
        if "cityblock", use cityblock distance from origin
    round_phase_width : Bool or None (default)
        if True, round width of bars given resolution

    Returns
    ----------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for each bar (key: "grating_mask"),
        and additional keys containing stimulus parameters
    """

    stim = sine(
        visual_size=visual_size,
        ppd=ppd,
        shape=shape,
        frequency=frequency,
        n_phases=n_phases,
        phase_width=phase_width,
        period=period,
        rotation=rotation,
        phase_shift=phase_shift,
        intensities=intensities,
        origin=origin,
        round_phase_width=round_phase_width,
        base_type=base_type,
    )

    # Round sine-wave to create square wave
    stim["img"] = round_to_vals(stim["img"], intensities)
    return stim
