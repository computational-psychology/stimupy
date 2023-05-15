import numpy as np

from stimupy.components import draw_regions, mask_regions
from stimupy.components.radials import ring

__all__ = [
    "wedge",
    "segments",
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
    stim = mask_regions(
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
    angle=None,
    radius=None,
    rotation=0.0,
    inner_radius=0.0,
    intensity_wedge=1.0,
    intensity_background=0.0,
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
    angle : float
        angular-width (in degrees) of segment
    radius : float
        radius of disc, in degrees visual angle
    rotation : float, optional
        rotation (in degrees) from 3 o'clock, counterclockwise, by default 0.0
    inner_radius : float, optional
        inner radius (in degrees visual angle), to turn disc into a ring, by default 0
    intensity_wedge : float, optional
        intensity value of wedge, by default 1.0
    intensity_background : float, optional
        intensity value of background, by default 0.0
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
    if angle is None:
        raise ValueError("wedge() missing argument 'angle' which is not 'None'")
    if radius is None:
        raise ValueError("wedge() missing argument 'radius' which is not 'None'")

    # Convert to inner-, outer-angle
    angles = [0, angle]

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

    # Remove everything but wedge, and add additional args
    stim["img"] = np.where(mask["wedge_mask"], stim["img"], intensity_background)
    stim["wedge_mask"] = stim["ring_mask"] * mask["wedge_mask"]
    stim["wedge_mask"] = np.where(stim["wedge_mask"] != 0, 1, 0).astype(int)
    stim["angle"] = angle
    stim["radius"] = radius
    stim["inner_radius"] = inner_radius
    stim["intensity_wedge"] = intensity_wedge
    stim["intensity_background"] = intensity_background
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
        dict with the stimulus (key: "img"),
        mask with integer index for each segment (key: "wedge_mask"),
        and additional keys containing stimulus parameters
    """
    stim = mask_regions(
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


def segments(
    visual_size=None,
    ppd=None,
    shape=None,
    angles=None,
    rotation=0.0,
    intensity_background=0.5,
    intensity_segments=(0, 1),
    origin="mean",
):
    """Generate mask with integer indices for sequential angular segments

    Parameters
    ----------
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of image, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of image, in pixels
    angles : Sequence[Number] or None (default)
        upper-limit of each segment, in angular degrees 0-360
    rotation : float, optional
        rotation (in degrees) from 3 o'clock, counterclockwise, by default 0.0
    intensity_background : Number
        intensity value for background; default is 0.5.
    intensity_segments : Sequence[Number, ...]
        intensity value for each segment, from inside to out.
        If fewer intensities are passed than number of radii, cycles through intensity_segments
    origin : "corner", "mean" or "center"
        if "corner": set origin to upper left corner
        if "mean": set origin to hypothetical image center (default)angles
        if "center": set origin to real center (closest existing value to mean)

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for each segment (key: "wedge_mask"),
        and additional keys containing stimulus parameters
    """
    if angles is None:
        raise ValueError("segments() missing argument 'angles' which is not 'None'")
    if not isinstance(angles, (int, float)):
        if np.diff(angles).min() < 0:
            raise ValueError("angles need to monotonically increase")

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

    # Update args
    stim["angles"] = angles
    stim["intensity_background"] = intensity_background
    stim["intensity_segments"] = intensity_segments

    return stim


def overview(**kwargs):
    """Generate example stimuli from this module

    Returns
    -------
    stims : dict
        dict with all stimuli containing individual stimulus dicts.
    """
    default_params = {
        "visual_size": (10, 10),
        "ppd": 20,
    }
    default_params.update(kwargs)

    # fmt: off
    stimuli = {
        "angulars_wedge": wedge(**default_params, angle=30, radius=4),
        "angulars_segments": segments(**default_params, angles=(30, 120, 300)),
    }
    # fmt: on

    return stimuli


if __name__ == "__main__":
    from stimupy.utils import plot_stimuli

    stims = overview()
    plot_stimuli(stims, mask=False, save=None)
