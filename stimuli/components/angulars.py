import numpy as np

from stimuli.components import draw_regions, mask_elements, resolve_grating_params
from stimuli.components.circulars import ring
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
    origin="mean",
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
    origin : "corner", "mean" or "center"
        if "corner": set origin to upper left corner
        if "mean": set origin to hypothetical image center (default)
        if "center": set origin to real center (closest existing value to mean)

    Returns
    -------
    dict[str, Any]
        dict with boolean mask (key: bool_mask) for pixels falling in given angle,
        and additional params
    """
    stim = mask_elements(
        edges=np.deg2rad(angles),
        orientation="angular",
        rotation=rotation,
        shape=shape,
        visual_size=visual_size,
        ppd=ppd,
        origin=origin,
        )
    stim["wedge_mask"] = stim["mask"]
    del stim["mask"]
    return stim


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
    origin="mean",
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
    origin : "corner", "mean" or "center"
        if "corner": set origin to upper left corner
        if "mean": set origin to hypothetical image center (default)
        if "center": set origin to real center (closest existing value to mean)

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for each segment (key: "wedge_mask"),
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
        origin=origin,
    )
    visual_size = stim["visual_size"]
    shape = stim["shape"]
    ppd = stim["ppd"]

    # Get mask for angles
    mask = mask_angle(
        rotation=rotation,
        angles=angles,
        visual_size=visual_size,
        ppd=ppd,
        shape=shape,
        origin=origin,
    )

    # Remove everything but wedge
    stim["img"] = np.where(mask["wedge_mask"], stim["img"], intensity_background)
    return stim.update(mask)


def mask_segments(
    edges,
    rotation=0.0,
    visual_size=None,
    ppd=None,
    shape=None,
    origin="mean",
):
    """Generate mask with integer indices for consecutive angular segments

    Parameters
    ----------
    edges : Sequence[Number]
        upper-limit of each consecutive segment, in angular degrees 0-360
    rotation : float, optional
        angle of rotation (in degrees) of segments,
        counterclockwise away from 3 o'clock, by default 0.0
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of image, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of image, in pixels
    origin : "corner", "mean" or "center"
        if "corner": set origin to upper left corner
        if "mean": set origin to hypothetical image center (default)
        if "center": set origin to real center (closest existing value to mean)

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for each segment (key: "wedge_mask"),
        and additional keys containing stimulus parameters
    """
    stim = mask_elements(
        orientation="angular",
        edges=np.deg2rad(edges),
        rotation=rotation,
        shape=shape,
        visual_size=visual_size,
        ppd=ppd,
        origin=origin,
        )
    stim["wedge_mask"] = stim["mask"]
    del stim["mask"]
    return stim


def angular_segments(
    angles,
    intensity_segments,
    rotation=0.0,
    visual_size=None,
    ppd=None,
    shape=None,
    intensity_background=0.5,
    origin="mean",
):
    """Generate mask with integer indices for sequential angular segments

    Parameters
    ----------
    angles : Sequence[Number]
        upper-limit of each segment, in angular degrees 0-360
    intensities : Sequence[Number, ...]
        intensity value for each segment, from inside to out.
        If fewer intensities are passed than number of radii, cycles through intensities
    rotation : float, optional
        angle of rotation (in degrees) of segments,
        counterclockwise away from 3 o'clock, by default 0.0
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of image, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of image, in pixels
    origin : "corner", "mean" or "center"
        if "corner": set origin to upper left corner
        if "mean": set origin to hypothetical image center (default)
        if "center": set origin to real center (closest existing value to mean)

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for each segment (key: "wedge_mask"),
        and additional keys containing stimulus parameters
    """

    # Get mask
    stim = mask_segments(
        edges=angles,
        visual_size=visual_size,
        ppd=ppd,
        shape=shape,
        rotation=rotation,
        origin=origin,
    )

    # Draw image
    stim["img"] = draw_regions(
        stim["wedge_mask"], intensities=intensity_segments, intensity_background=intensity_background
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
    intensity_segments=(1.0, 0.0),
    origin="mean",
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
    intensity_segments : Sequence[Number, ...]
        intensity value for each segment, from inside to out, by default (1.0, 0.0).
        If fewer intensities are passed than number of radii, cycles through intensities
    origin : "corner", "mean" or "center"
        if "corner": set origin to upper left corner
        if "mean": set origin to hypothetical image center (default)
        if "center": set origin to real center (closest existing value to mean)

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for each segment (key: "wedge_mask"),
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
        round_phase_width=False,
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
        intensity_segments=intensity_segments,
        origin=origin,
    )

    # Assemble output
    return {
        **stim,
        "n_segments": params["n_phases"],
        "frequency": params["frequency"],
    }


def pinwheel(
    radius=None,
    frequency=None,
    n_segments=None,
    segment_width=None,
    rotation=0.0,
    inner_radius=0.0,
    intensity_segments=(1.0, 0.0),
    intensity_background=0.5,
    visual_size=None,
    ppd=None,
    shape=None,
    origin="mean",
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
    intensity_segments : Sequence[Number, ...]
        intensity value for each segment, from inside to out, by default (1.0, 0.0).
        If fewer intensities are passed than number of radii, cycles through intensities
    intensity_background : float (optional)
        intensity value of background, by default 0.5
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of image, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of image, in pixels
    origin : "corner", "mean" or "center"
        if "corner": set origin to upper left corner
        if "mean": set origin to hypothetical image center (default)
        if "center": set origin to real center (closest existing value to mean)

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for each segment (key: "wedge_mask"),
        and additional keys containing stimulus parameters
    """

    # Get disc
    disc = ring(
        radii=[inner_radius, radius],
        intensity_rings=1.0,
        intensity_background=0.0,
        visual_size=visual_size,
        ppd=ppd,
        shape=shape,
        origin=origin,
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
        intensity_segments=intensity_segments,
        visual_size=visual_size,
        shape=shape,
        ppd=ppd,
        origin=origin,
    )

    # Mask out everything but the disc
    stim["img"] = np.where(disc["ring_mask"], stim["img"], intensity_background)
    stim["radii"] = disc["edges"]
    stim["intensity_background"] = intensity_background
    return stim
