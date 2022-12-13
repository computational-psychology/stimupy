import itertools

import numpy as np

from stimuli.components.circular import ring
from stimuli.components.components import (
    draw_regions,
    image_base,
    resolve_grating_params,
)
from stimuli.utils import resolution

__all__ = [
    "wedge",
    "grating",
    "pinwheel",
]


def mask_angle(
    angles,
    rotation=0.0,
    visual_size=None,
    ppd=None,
    shape=None,
):
    """Mask a contiguous set of angles in image

    Parameters
    ----------
    angles : Sequence[float, float]
        lower- and upper-limit of angles to mask, in degrees
    rotation : float, optional
        rotation (in degrees) from 3 o'clock, counterclockwise, by default 0.0
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of image, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of image, in pixels

    Returns
    -------
    dict[str, Any]
        dict with boolean mask (key: bool_mask) for pixels falling in given angle,
        and additional params
    """

    # Set up coordinates
    base = image_base(rotation=rotation, visual_size=visual_size, ppd=ppd, shape=shape)
    distances = base["angular"]

    # Create mask
    inner_angle, outer_angle = np.deg2rad(angles)
    mask = (distances > inner_angle) & (distances <= outer_angle)

    return {
        "mask": mask,
        "visual_size": base["visual_size"],
        "ppd": base["ppd"],
        "shape": base["shape"],
        "rotation": base["rotation"],
    }


def wedge(
    width,
    radius,
    rotation=0.0,
    inner_radius=0.0,
    intensity=1.0,
    intensity_background=0.5,
    visual_size=None,
    ppd=None,
    shape=None,
):
    """Draw a wedge, i.e., segment of a disc

    Parameters
    ----------
    width : float
        angular-width (in degrees) of segment
    radius : float
        radius of disc, in degrees visual angle
    rotation : float, optional
        angle of rotation (in degrees) of segment,
        counterclockwise from 3 o'clock, by default 0.0
    inner_radius : float, optional
        inner radius (in degrees visual angle), to turn disc into a ring, by default 0
    intensity : float, optional
        intensity value of wedge, by default 1.0
    intensity_background : float, optional
        intensity value of background, by default 0.5
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of image, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of image, in pixels

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img")
        and additional keys containing stimulus parameters
    """

    # Convert to inner-, outer-angle
    angles = [0, width]

    # Draw disc
    stim = ring(
        radii=[inner_radius, radius],
        intensity=intensity,
        intensity_background=intensity_background,
        visual_size=visual_size,
        ppd=ppd,
        shape=shape,
        # supersampling=supersampling,
    )
    visual_size = stim["visual_size"]
    shape = stim["shape"]
    ppd = stim["ppd"]

    # Get mask for angles
    bool_mask = mask_angle(
        rotation=rotation, angles=angles, visual_size=visual_size, ppd=ppd, shape=shape
    )

    # Remove everything but wedge
    stim["img"] = np.where(bool_mask["mask"], stim["img"], intensity_background)

    # Output
    stim.update(bool_mask)

    return stim


def mask_segments(
    edges,
    rotation=0.0,
    visual_size=None,
    ppd=None,
    shape=None,
):
    """Generate mask with integer indices for consecutive angular segments

    Parameters
    ----------
    edges : Sequence[Number]
        upper-limit of each consecutive segment, in angular degrees 0-360
    rotation : float, optional
        angle of rotation (in degrees) of segments,
        counterclockwise away from 3 o'clock, by default 0.0
    intensities : Sequence[Number, ...]
        intensity value for each segment, from inside to out, by default [1.0, 0.0]
        If fewer intensities are passed than number of radii, cycles through intensities
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of image, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of image, in pixels

    Returns
    ----------
    dict[str, Any]
        mask with integer index for each angular segment (key: "mask"),
        and additional keys containing stimulus parameters
    """

    # Try to resolve resolution
    shape, visual_size, ppd = resolution.resolve(shape=shape, visual_size=visual_size, ppd=ppd)

    # Set up coordinates
    base = image_base(shape=shape, ppd=ppd, visual_size=visual_size, rotation=rotation)
    distances = base["angular"]

    # Mask elements
    edges = np.deg2rad(edges)
    mask = np.zeros(shape, dtype=int)
    for idx, edge in zip(reversed(range(len(edges))), reversed(edges)):
        mask[distances <= edge] = int(idx + 1)

    return {
        "mask": mask,
        "edges": edges,
        "shape": shape,
        "visual_size": visual_size,
        "ppd": ppd,
        "orientation": "angular",
    }


def angular_segments(
    angles,
    rotation=0.0,
    intensity_segments=None,
    visual_size=None,
    ppd=None,
    shape=None,
    intensity_background=0.5,
):
    """Generate mask with integer indices for sequential angular segments

    Parameters
    ----------
    angles : Sequence[Number]
        upper-limit of each segment, in angular degrees 0-360
    rotation : float, optional
        angle of rotation (in degrees) of segments,
        counterclockwise away from 3 o'clock, by default 0.0
    intensities : Sequence[Number, ...]
        intensity value for each segment, from inside to out, by default [1.0, 0.0]
        If fewer intensities are passed than number of radii, cycles through intensities
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of image, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of image, in pixels

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img"), mask (key: "mask")
        and additional keys containing stimulus parameters
    """

    # Get mask
    stim = mask_segments(
        edges=angles, visual_size=visual_size, ppd=ppd, shape=shape, rotation=rotation
    )

    # Draw image
    stim["img"] = draw_regions(
        stim["mask"], intensities=intensity_segments, intensity_background=intensity_background
    )

    return stim


def grating(
    shape=None,
    visual_size=None,
    ppd=None,
    frequency=None,
    n_segments=None,
    segment_width=None,
    rotation=0.0,
    intensities_segments=[1.0, 0.0],
):
    """Draw an angular grating, i.e., set of segments

    Parameters
    ----------
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of image, in pixels
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of image, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    frequency : Number, or None (default)
        angular frequency of angular grating, in cycles per angular degree
    n_segments : int, or None (default)
        number of segments
    segment_width : Number, or None (default)
        angular width of a single segment, in degrees
    rotation : float, optional
        angle of rotation (in degrees) grating segments,
        counterclockwise away from 3 o'clock, by default 0.0
    intensities_segments : Sequence[Number, ...]
        intensity value for each segment, from inside to out, by default [1.0, 0.0]
        If fewer intensities are passed than number of radii, cycles through intensities

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for each segment (key: "mask"),
        and additional keys containing stimulus parameters
    """

    # Resolve resolution
    shape, visual_size, ppd = resolution.resolve(shape=shape, visual_size=visual_size, ppd=ppd)

    # Resolve grating
    params = resolve_grating_params(
        visual_angle=360,
        ppd=1,
        frequency=frequency,
        n_phases=n_segments,
        phase_width=segment_width,
        period="ignore",
    )

    # Determine angles
    angles = params["edges"]
    angles = sorted(np.unique(angles))

    # Draw stim
    stim = angular_segments(
        angles=angles,
        rotation=rotation,
        visual_size=visual_size,
        ppd=ppd,
        shape=shape,
        intensity_segments=intensities_segments,
    )

    # Assemble output
    return {
        **stim,
        "n_segments": params["n_phases"],
        "frequency": params["frequency"],
        "n_segments": params["n_phases"],
    }


def pinwheel(
    radius=None,
    frequency=None,
    n_segments=None,
    segment_width=None,
    rotation=0.0,
    inner_radius=0.0,
    intensities_segments=[1.0, 0.0],
    intensity_background=0.5,
    visual_size=None,
    ppd=None,
    shape=None,
):
    """Pinwheel- / wheel-of-fortune-like angular grating on disc/ring

    Parameters
    ----------
    radius : float
        radius of wheel, in degrees visual angle
    frequency : Number, or None (default)
        angular frequency of angular grating, in cycles per angular degree
    n_segments : int, or None (default)
        number of segments
    segment_width : Number, or None (default)
        angular width of a single segment, in degrees
    rotation : float, optional
        rotation (in degrees) of pinwheel segments away
        counterclockwise from 3 o'clock, by default 0.0
    inner_radius : float, optional
        inner radius (in degrees visual angle), to turn disc into a ring, by default 0.0
    intensities_segments : Sequence[Number, ...]
        intensity value for each segment, from inside to out, by default [1.0, 0.0]
        If fewer intensities are passed than number of radii, cycles through intensities
    intensity_background : float (optional)
        intensity value of background, by default 0.5
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of image, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of image, in pixels

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for each segment (key: "mask"),
        and additional keys containing stimulus parameters
    """

    # Get disc
    disc = ring(
        radii=[inner_radius, radius],
        intensity=1,
        intensity_background=0,
        visual_size=visual_size,
        ppd=ppd,
        shape=shape,
    )
    visual_size = disc["visual_size"]
    shape = disc["shape"]
    ppd = disc["ppd"]

    # Draw segments
    stim = grating(
        frequency=frequency,
        n_segments=n_segments,
        segment_width=segment_width,
        rotation=rotation,
        intensities_segments=intensities_segments,
        visual_size=visual_size,
        shape=shape,
        ppd=ppd,
    )

    # Mask out everywhere that the disc isn't
    stim["img"] = np.where(disc["img"], stim["img"], intensity_background)
    stim["mask"] = np.where(disc["img"], stim["mask"], 0)

    return {**stim, "radii": disc["radii"], "intensity_background": intensity_background}
