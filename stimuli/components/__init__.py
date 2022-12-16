import itertools
import warnings
from copy import deepcopy

import numpy as np

from stimuli.utils import int_factorize, resolution

from .components import *


def image_base(visual_size=None, shape=None, ppd=None, rotation=0.0, origin=None):
    """Create coordinate-arrays to serve as image base for drawing

    Parameters
    ----------
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of image, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of image, in pixels
    rotation : float, optional
        rotation (in degrees) counterclockwise from 3 o'clock, by default 0.0
    origin : Sequence[Number, Number], Number, or None (default)
        placement of origin [height,width from topleft] to calculate distances from.
        If None, set to center of visual_size

    Returns
    -------
    dict[str, Any]
        dict with keys:
        "visual_size", "ppd" : resolved from input arguments,
        "x", "y" : single axes
        "horiztonal", "vertical" : numpy.ndarray of shape, with distance from origin,
            in deg. visual angle, at each pixel
        "radial" : numpyn.ndarray of shape, with radius from origin,
            in deg. visual angle, at each pixel
        "angular" : numpy.ndarray of shape, with angle relative to 3 o'clock,
            in rad, at each pixel
        "cityblock" : numpy.ndarray of shape, with cityblock distance from origin,
            in deg. visual angle ,at each pixel
    """

    # Resolve resolution
    shape, visual_size, ppd = resolution.resolve(shape=shape, visual_size=visual_size, ppd=ppd)

    # Set origin
    if origin is None:
        origin = (visual_size.height / 2, visual_size.width / 2)
    origin = resolution.validate_visual_size(origin)

    # Image axes
    x = np.linspace(-origin.width, visual_size.width - origin.width, shape.width)
    y = np.linspace(-origin.height, visual_size.height - origin.width, shape.height)

    # Linear distance image bases
    xx, yy = np.meshgrid(x, y)

    # City-block distance (frames)
    cityblock = np.maximum(np.abs(xx), np.abs(yy))

    # Radial distance
    radial = np.sqrt(xx**2 + yy**2)

    # Angular distance
    angular = np.arctan2(xx, yy)
    angular -= np.deg2rad(rotation + 90)
    angular %= 2 * np.pi

    return {
        "visual_size": visual_size,
        "ppd": ppd,
        "shape": shape,
        "rotation": rotation,
        "x": x,
        "y": y,
        "horizontal": xx,
        "vertical": yy,
        "cityblock": cityblock,
        "radial": radial,
        "angular": angular,
    }


def mask_elements(
    orientation,
    edges,
    shape=None,
    visual_size=None,
    ppd=None,
    rotation=0.0,
    origin=None,
):
    """Generate mask with integer indices for consecutive elements

    Parameters
    ----------
    orientation : any of keys in stimuli.components.image_base()
        which dimension to mask over
    edges : Sequence[Number]
        upper-limit of each consecutive elements
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of image, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of image, in pixels
    rotation : float, optional
        angle of rotation (in degrees) of segments,
        counterclockwise away from 3 o'clock, by default 0.0
    origin : Sequence[Number, Number], Number, or None (default)
        placement of origin [height,width from topleft] to calculate distances from.
        If None, set to center of visual_size

    Returns
    ----------
    dict[str, Any]
        mask with integer index for each angular segment (key: "mask"),
        and additional keys containing stimulus parameters
    """

    # Set up coordinates
    base = image_base(
        shape=shape, visual_size=visual_size, ppd=ppd, rotation=rotation, origin=origin
    )
    distances = base[orientation]

    # Mark elements with integer idx-value
    mask = np.zeros(base["shape"], dtype=int)
    for idx, edge in zip(reversed(range(len(edges))), reversed(edges)):
        edge = np.round(edge, 10)
        mask[distances <= edge] = int(idx + 1)

    # Assemble output
    return {
        "mask": mask,
        "edges": edges,
        "orientation": orientation,
        "rotation": base["rotation"],
        "shape": base["shape"],
        "visual_size": base["visual_size"],
        "ppd": base["ppd"],
        "distances": distances,
    }


def resolve_grating_params(
    length=None,
    visual_angle=None,
    ppd=None,
    frequency=None,
    n_phases=None,
    phase_width=None,
    period="ignore",
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
    period : "full", "half", "ignore" (default)
        whether to ensure the grating only has "full" periods,
        half "periods", or no guarantees ("ignore")

    Returns
    -------
    dict[str, Any]
        dictionary with all six resolution & size parameters resolved.
    """

    if period not in ["ignore", "even", "odd", "either"]:
        raise TypeError(f"period not understood: {period}")

    # Try to resolve resolution
    try:
        length, visual_angle, ppd = resolution.resolve_1D(
            length=length, visual_angle=visual_angle, ppd=ppd
        )
    except ValueError:
        ppd = ppd
        length = length
        visual_angle = visual_angle

    old_frequency = deepcopy(frequency)
    old_n_phases = deepcopy(n_phases)
    old_phase_width = deepcopy(phase_width)

    # Try to resolve number and width(s) of phases:
    # Logic here is that phase_width expresses "degrees per phase",
    # which we can convert to "phases_per_degree"
    # phase_width = degrees_per_phase = 1 / phases_per_degree = 1 / (2*frequency)
    if phase_width is not None:
        # Make sure that phase width is realisable given ppd
        phase_width = np.round(phase_width * ppd) / ppd
        phases_pd = 1 / phase_width
        if frequency is not None and phases_pd != 2 * frequency:
            raise ValueError(f"phase_width {phase_width} and frequency {frequency} don't match")
    elif frequency is not None:
        # Make sure that frequency is realisable given ppd
        phases_pd = 2 * frequency
        phase_width = np.round(1 / phases_pd * ppd) / ppd
        phases_pd = 1 / phase_width
        frequency = phases_pd / 2
    else:  # both are None:
        phases_pd = None

    # Logic here is that phase_width expresses "degrees per phase",
    # which we can invert to phases_per_degree, analogous to ppd:
    # n_phases = phases_per_degree * n_degrees
    # is analogous to
    # pix = ppd * n_degrees
    # Thus we can resolve the number and spacing of phases also as a resolution
    try:
        n_phases, min_angle, phases_pd_calc = resolution.resolve_1D(
            length=n_phases,
            visual_angle=visual_angle,
            ppd=phases_pd,
            round=False,
        )
    except Exception as e:
        raise Exception("Could not resolve grating frequency, phase_width, n_phases") from e

    phase_width = 1 / phases_pd_calc
    phase_width = np.round(phase_width * ppd) / ppd
    phases_pd = 1 / phase_width
    frequency = phases_pd / 2
    
    n_phases, min_angle, phases_pd_calc = resolution.resolve_1D(
        length=None,
        visual_angle=visual_angle,
        ppd=phases_pd,
        round=False,
    )

    # Now resolve resolution
    visual_angle = min_angle if visual_angle is None else visual_angle
    length, visual_angle, ppd = resolution.resolve_1D(
        length=length, visual_angle=visual_angle, ppd=ppd
    )

    # Ensure full/half period?
    if period != "ignore":
        # Round n_phases
        if period == "even":  # n_phases has to be even
            n_phases = np.round(n_phases / 2) * 2
            phase_candidates = [n_phases, n_phases-2, n_phases+2, n_phases-4, n_phases+4, n_phases-6, n_phases+6]
            phase_candidates = [n_phases]
        elif period == "either":  # n_phases can be odd
            n_phases = np.round(n_phases)
            phase_candidates = [n_phases, n_phases-1, n_phases+1, n_phases-2, n_phases+2, n_phases-3, n_phases+3]
        elif period == "odd":  # n_phases can be odd
            n_phases = np.round(n_phases / 2) * 2 + 1
            phase_candidates = [n_phases, n_phases-2, n_phases+2, n_phases-4, n_phases+4, n_phases-6, n_phases+6]

        for pc in phase_candidates:
            # Recalculate phases_pd
            n_phases, min_angle, phases_pd = resolution.resolve_1D(
                length=pc,
                visual_angle=visual_angle,
                ppd=None,
                round=False,
            )
        
            # Convert to frequency
            phase_width = 1 / phases_pd
            frequency = phases_pd / 2
            
            if not (phase_width*ppd) % 1:
                break

        if (phase_width*ppd) % 1:
            raise resolution.ResolutionError(f"Cannot fit an {period} number of phases in {length} pix while "
                                              "considering other parameters. Change parameters or increase ppd.")
    
    if old_n_phases is not None:
        if (n_phases < (old_n_phases-1)) or (n_phases > (old_n_phases+1)):
            raise resolution.ResolutionError(f"Cannot fit {old_n_phases} phases in {length} pix."
                                             " Change parameters or increase ppd. Best possible at "
                                             f"given resolution: {n_phases} phases")

        if n_phases != old_n_phases:
            warnings.warn(
                f"Adjusted n_phases={old_n_phases}->{n_phases} because original"
                f"phase_width {old_phase_width} -> {phase_width} did not fit"
            )

    if (old_phase_width is not None and phase_width != old_phase_width):
        warnings.warn(f"Adjusted phase width because of poor resolution: {old_phase_width} -> {phase_width}")
    
    if (old_frequency is not None and frequency != old_frequency):
        warnings.warn(f"Adjusted frequency because of poor resolution: {old_frequency} -> {frequency}")

    # Check that frequency does not exceed Nyquist limit:
    if frequency > (ppd / 2):
        raise ValueError(
            f"Grating frequency ({frequency}) should not exceed Nyquist limit {ppd/2} (ppd/2)"
        )

    # Accumulate edges of phases
    edges = [*itertools.accumulate(itertools.repeat(phase_width, int(np.ceil(n_phases))))]
    if "period" == "ignore":
        edges += [visual_angle]

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


def draw_regions(mask, intensities, intensity_background=0.5):
    """Draw image with intensities for components in mask

    Parameters
    ----------
    mask : numpy.ndarray
        image-array with integer-indices for each region to draw
    intensities : Sequence[float, ...]
        intensity value for each masked region.
        Can specify as many intensities as number of masked regions;
        If fewer intensities are passed than masked regions, cycles through intensities
    intensity_background : float, optional
        intensity value of background, by default 0.5

    Returns
    -------
    numpy.ndarray
        image-array, same shape as mask, with intensity assigned to each masked region
    """

    # Create background
    img = np.ones(mask.shape) * intensity_background

    # Get mask indices
    mask_idcs = np.unique(mask[mask > 0])

    # Assign intensities to masked regions
    ints = [*itertools.islice(itertools.cycle(intensities), len(mask_idcs))]
    for frame_idx, intensity in zip(mask_idcs, ints):
        img = np.where(mask == frame_idx, intensity, img)

    return img


def round_n_phases(n_phases, length, period):
    # n_phases has to integer-divide length
    possible_phase_pix = np.array(list(int_factorize(length)))
    possible_n_phases = length / possible_phase_pix

    if period == "even":
        # only look at possible_n_phases that are even
        possible_n_phases = possible_n_phases[possible_n_phases % 2 == 0]
    elif period == "odd":
        # only look at possible_n_phases that are odd
        possible_n_phases = possible_n_phases[possible_n_phases % 2 != 0]

    closest = possible_n_phases[np.argmin(np.abs(possible_n_phases - n_phases))]

    return int(closest)
