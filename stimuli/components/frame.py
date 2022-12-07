import itertools

import numpy as np

from stimuli.components.components import resolve_grating_params
from stimuli.utils import resolution

__all__ = [
    "frames",
]


def mask_frames(
    shape=None,
    visual_size=None,
    ppd=None,
    frequency=None,
    n_frames=None,
    frame_width=None,
    period="ignore",
):
    """Generate mask for alternating set of frames, a square grating (?)

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

    Returns
    ----------
    dict[str, Any]
        mask with integer index for each bar (key: "mask"),
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
    shape = resolution.validate_shape(params["length"] * 2)
    visual_size = resolution.validate_visual_size(params["visual_angle"] * 2)
    ppd = resolution.validate_ppd(params["ppd"])

    # Create image-base:
    x = np.linspace(-visual_size.width / 2, visual_size.width / 2, shape.width)
    y = np.linspace(-visual_size.height / 2, visual_size.height / 2, shape.height)
    xx, yy = np.meshgrid(x, y)
    mask = np.zeros(shape, dtype=int)

    # Determine frame edges
    frame_edges = [
        *itertools.accumulate(itertools.repeat(params["phase_width"], int(params["n_phases"])))
    ]
    if params["period"] == "ignore":
        frame_edges += [params["visual_angle"]]

    # Mask frames
    distances = np.maximum(np.abs(xx), np.abs(yy))
    for idx, edge in zip(reversed(range(len(frame_edges))), reversed(frame_edges)):
        mask[distances <= edge] = int(idx + 1)

    return {
        "mask": mask,
        "shape": shape,
        "visual_size": visual_size,
        "ppd": ppd,
        "frequency": params["frequency"],
        "frame_width": params["phase_width"],
        "n_frames": params["n_phases"],
        "period": params["period"],
    }


def frames(
    shape=None,
    visual_size=None,
    ppd=None,
    frequency=None,
    n_frames=None,
    frame_width=None,
    period="ignore",
    intensity_frames=(0.0, 1.0),
):
    """Draw set of square frames, at given spatial frequency

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
    intensity_bars : Sequence[float, ...]
        intensity value for each bar, by default [1.0, 0.0].
        Can specify as many intensities as n_bars;
        If fewer intensities are passed than n_bars, cycles through intensities

    Returns
    ----------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for each target (key: "mask"),
        and additional keys containing stimulus parameters
    """
    # Get frames mask
    stim = mask_frames(
        shape=shape,
        visual_size=visual_size,
        ppd=ppd,
        frequency=frequency,
        n_frames=n_frames,
        frame_width=frame_width,
        period=period,
    )
    mask = stim["mask"]

    # Draw frames
    img = np.zeros(mask.shape)
    ints = [*itertools.islice(itertools.cycle(intensity_frames), len(np.unique(mask)))]
    for frame_idx, intensity in zip(np.unique(mask), ints):
        img = np.where(mask == frame_idx, intensity, img)

    return {"img": img, **stim}
