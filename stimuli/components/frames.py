import numpy as np

from stimuli.components import draw_regions, mask_elements, resolve_grating_params
from stimuli.utils import resolution

__all__ = [
    "frames",
    "square_wave",
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
    ----------
    dict[str, Any]
        mask with integer index for each frame (key: "frame_mask"),
        and additional keys containing stimulus parameters
    """
    stim = mask_elements(
        orientation="cityblock",
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
    frame_radii,
    shape=None,
    visual_size=None,
    ppd=None,
    intensity_frames=(1.0, 0.0),
    intensity_background=0.5,
    origin="mean",
):
    """Draw sequential set of square frames with specified radii

    Parameters
    ----------
    frame_radii : Sequence[Number]
        radii of each frame, in degrees visual angle
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of image, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of image, in pixels
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
    ----------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for each frame (key: "frame_mask"),
        and additional keys containing stimulus parameters
    """

    # Get frames mask
    stim = mask_frames(
        edges=frame_radii,
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


def square_wave(
    shape=None,
    visual_size=None,
    ppd=None,
    frequency=None,
    n_frames=None,
    frame_width=None,
    period="ignore",
    intensity_frames=(1.0, 0.0),
    intensity_background=0.5,
    origin="mean",
):
    """Draw set of equal-width square frames, at given spatial frequency

    Parameters
    ----------
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of image, in pixels
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of image, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    frequency : Number, or None (default)
        spatial frequency of grating, in cycles per degree visual angle
    n_frames : int, or None (default)
        number of frames in the grating
    frame_width : Number, or None (default)
        width of a single frame, in degrees visual angle
    period : "full", "half", "ignore" (default)
        whether to ensure the grating only has "full" periods,
        half "periods", or no guarantees ("ignore")
    intensity_frames : Sequence[float, ...]
        intensity value for each frame, by default (1.0, 0.0).
        Can specify as many intensities as number of frame_widths;
        If fewer intensities are passed than frame_widhts, cycles through intensities
    intensity_background : float (optional)
        intensity value of background, by default 0.5
    origin : "corner", "mean" or "center"
        if "corner": set origin to upper left corner
        if "mean": set origin to hypothetical image center (default)
        if "center": set origin to real center (closest existing value to mean)

    Returns
    ----------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for each frame (key: "frame_mask"),
        and additional keys containing stimulus parameters
    """

    # Try to resolve resolution
    try:
        shape, visual_size, ppd = resolution.resolve(shape=shape, visual_size=visual_size, ppd=ppd)
    except ValueError:
        ppd = resolution.validate_ppd(ppd) if ppd is not None else None
        shape = resolution.validate_shape(shape) if shape is not None else None
        visual_size = (
            resolution.validate_visual_size(visual_size) if visual_size is not None else None
        )

    # Resolve params
    length = np.array(shape).min() / 2 if shape is not None else None
    ppd_1D = np.array(ppd).min() if ppd is not None else None
    visual_angle = np.array(visual_size).min() / 2 if visual_size is not None else None
    params = resolve_grating_params(
        length=length,
        visual_angle=visual_angle,
        n_phases=n_frames,
        phase_width=frame_width,
        ppd=ppd_1D,
        frequency=frequency,
        period=period,
    )
    shape, visual_size, ppd = resolution.resolve(
        shape=params["length"] * 2, visual_size=params["visual_angle"] * 2, ppd=params["ppd"]
    )

    # Draw
    stim = frames(
        frame_radii=params["edges"],
        shape=shape,
        visual_size=visual_size,
        ppd=ppd,
        intensity_frames=intensity_frames,
        intensity_background=intensity_background,
        origin=origin,
    )

    return {
        **stim,
        "frequency": params["frequency"],
        "n_frames": params["n_phases"],
        "frame_width": params["phase_width"],
        "period": params["period"],
        "orientation": "cityblock",
    }