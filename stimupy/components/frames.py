import numpy as np

from stimupy.components import draw_regions, mask_elements

__all__ = [
    "frames",
]


def mask_frames(
    edges,
    shape=None,
    visual_size=None,
    ppd=None,
    origin="mean",
):
    """Generate mask with integer indices for sequential square frames

    Parameters
    ----------
    edges : Sequence[Number, ...]
        upper-limit of each frame, in degrees visual angle
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
        mask with integer index for each frame (key: "frame_mask"),
        and additional keys containing stimulus parameters
    """
    stim = mask_elements(
        distance_metric="rectilinear",
        edges=edges,
        rotation=0.0,
        shape=shape,
        visual_size=visual_size,
        ppd=ppd,
        origin=origin,
    )
    stim["frame_mask"] = stim["mask"]
    del stim["mask"]
    return stim


def frames(
    visual_size=None,
    ppd=None,
    shape=None,
    radii=None,
    intensity_frames=(1.0, 0.0),
    intensity_background=0.5,
    origin="mean",
):
    """Draw sequential set of square frames with specified radii

    Parameters
    ----------
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of image, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of image, in pixels
    radii : Sequence[Number]
        radii of each frame, in degrees visual angle
    intensity_frames : Sequence[float, ...]
        intensity value for each frame, by default (1.0, 0.0).
        Can specify as many intensities as number of frame_widths;
        If fewer intensities are passed than frame_widhts, cycles through intensities
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
        mask with integer index for each frame (key: "frame_mask"),
        and additional keys containing stimulus parameters
    """
    if radii is None:
        raise ValueError("frames() missing argument 'radii' which is not 'None'")

    if np.diff(radii).min() < 0:
        raise ValueError("radii need to monotonically increase")

    # Get frames mask
    stim = mask_frames(
        edges=radii,
        shape=shape,
        visual_size=visual_size,
        ppd=ppd,
        origin=origin,
    )

    # Draw image
    stim["img"] = draw_regions(
        stim["frame_mask"], intensities=intensity_frames, intensity_background=intensity_background
    )
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
        "ppd": 30,
    }
    default_params.update(kwargs)

    # fmt: off
    stimuli = {
        "frames_frames": frames(**default_params, radii=(1, 2, 3)),
    }
    # fmt: on

    return stimuli


if __name__ == "__main__":
    from stimupy.utils import plot_stimuli

    stims = overview()
    plot_stimuli(stims, mask=True, save=None)
