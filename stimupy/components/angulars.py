import numpy as np

from stimupy.components import draw_regions, mask_elements, waves
from stimupy.components.radials import ring
from stimupy.utils import resolution

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
        distance_metric="angular",
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
    visual_size=None,
    ppd=None,
    shape=None,
    width=None,
    radius=None,
    rotation=0.0,
    inner_radius=0.0,
    intensity_wedge=1.0,
    intensity_background=0.5,
    origin="mean",
):
    """Draw a wedge, i.e., segment of a disc

    Parameters
    ----------
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of image, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of image, in pixels
    width : float
        angular-width (in degrees) of segment
    radius : float
        radius of disc, in degrees visual angle
    rotation : float, optional
        angle of rotation (in degrees) of segment,
        counterclockwise from 3 o'clock, by default 0.0
    inner_radius : float, optional
        inner radius (in degrees visual angle), to turn disc into a ring, by default 0
    intensity_wedge : float, optional
        intensity value of wedge, by default 1.0
    intensity_background : float, optional
        intensity value of background, by default 0.5
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
    if width is None:
        raise ValueError("wedge() missing argument 'width' which is not 'None'")
    if radius is None:
        raise ValueError("wedge() missing argument 'radius' which is not 'None'")

    # Convert to inner-, outer-angle
    angles = [0, width]

    # Draw disc
    stim = ring(
        visual_size=visual_size,
        ppd=ppd,
        shape=shape,
        radii=[inner_radius, radius],
        intensity_ring=intensity_wedge,
        intensity_background=intensity_background,
        origin=origin,
    )

    # Get mask for angles
    mask = mask_angle(
        rotation=rotation,
        angles=angles,
        visual_size=stim["visual_size"],
        ppd=stim["ppd"],
        shape=stim["shape"],
        origin=origin,
    )

    # Remove everything but wedge
    stim["img"] = np.where(mask["wedge_mask"], stim["img"], intensity_background)
    stim["wedge_mask"] = stim["ring_mask"] * mask["wedge_mask"]
    stim["wedge_mask"] = np.where(stim["wedge_mask"] != 0, 1, 0).astype(int)
    del stim["ring_mask"]
    return stim


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
        distance_metric="angular",
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
        stim["wedge_mask"],
        intensities=intensity_segments,
        intensity_background=intensity_background,
    )
    return stim


def grating(
    visual_size=None,
    ppd=None,
    shape=None,
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
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of image, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of image, in pixels
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
    lst = [visual_size, ppd, shape, frequency, n_segments, segment_width]
    if len([x for x in lst if x is not None]) < 3:
        raise ValueError(
            "'grating()' needs 3 non-None arguments for resolving from 'visual_size', "
            "'ppd', 'shape', 'frequency', 'n_segments', 'segment_width'"
        )

    # Resolve resolution
    shape, visual_size, ppd = resolution.resolve(shape=shape, visual_size=visual_size, ppd=ppd)

    if frequency is not None and frequency > 0.5:
        raise ValueError("'frequency' in angular grating must be smaller than 0.5")

    # Resolve grating
    params = waves.resolve_grating_params(
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
    visual_size=None,
    ppd=None,
    shape=None,
    radius=None,
    frequency=None,
    n_segments=None,
    segment_width=None,
    rotation=0.0,
    inner_radius=0.0,
    intensity_segments=(1.0, 0.0),
    intensity_background=0.5,
    origin="mean",
):
    """Pinwheel- / wheel-of-fortune-like angular grating on disc/ring

    Parameters
    ----------
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of image, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of image, in pixels
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
    lst = [visual_size, ppd, shape, frequency, n_segments, segment_width]
    if len([x for x in lst if x is not None]) < 3:
        raise ValueError(
            "'pinwheel()' needs 3 non-None arguments for resolving from 'visual_size', "
            "'ppd', 'shape', 'frequency', 'n_segments', 'segment_width'"
        )
    if radius is None:
        raise ValueError("pinwheel() missing argument 'radius' which is not 'None'")

    # Get disc
    disc = ring(
        radii=[inner_radius, radius],
        intensity_ring=1.0,
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
    stim["wedge_mask"] = np.where(disc["ring_mask"], stim["wedge_mask"], 0).astype(int)
    stim["radius"] = radius
    stim["intensity_background"] = intensity_background
    return stim
