import itertools

import numpy as np

from stimuli.components.components import image_base, resolve_grating_params
from stimuli.utils import resolution

__all__ = [
    "square_wave",
]


def mask_bars(
    shape=None,
    visual_size=None,
    ppd=None,
    frequency=None,
    n_bars=None,
    bar_width=None,
    period="ignore",
    orientation="horizontal",
):
    """Generate mask for square-wave grating, i.e., set of bars

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
    n_bars : int, or None (default)
        number of bars in the grating
    bar_width : Number, or None (default)
        width of a single bar, in degrees visual angle
    period : "full", "half", "ignore" (default)
        whether to ensure the grating only has "full" periods,
        half "periods", or no guarantees ("ignore")
    orientation : "vertical" or "horizontal" (default)
        orientation of the grating

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
        ppd = resolution.validate_ppd(ppd)
        shape = resolution.validate_shape(shape)
        visual_size = resolution.validate_visual_size(visual_size)

    # Orientation
    if orientation == "horizontal":
        length = shape.width
        visual_angle = visual_size.width
        ppd_1D = ppd.horizontal
    elif orientation == "vertical":
        length = shape.height
        visual_angle = visual_size.height
        ppd_1D = ppd.vertical

    # Resolve params
    params = resolve_grating_params(
        length=length,
        visual_angle=visual_angle,
        n_phases=n_bars,
        phase_width=bar_width,
        ppd=ppd_1D,
        frequency=frequency,
        period=period,
    )
    length = params["length"]
    ppd_1D = params["ppd"]
    visual_angle = params["visual_angle"]

    # Orientation switch
    if orientation == "horizontal":
        shape = (shape.height, length) if shape.height is not None else length
        visual_size = (
            (visual_size.height, visual_angle) if visual_size.height is not None else visual_angle
        )
        ppd = (ppd.vertical, ppd_1D) if ppd.vertical is not None else ppd_1D
    elif orientation == "vertical":
        shape = (length, shape.width) if shape.width is not None else length
        visual_size = (
            (visual_angle, visual_size.width) if visual_size.width is not None else visual_angle
        )
        ppd = (ppd_1D, ppd.horizontal) if ppd.horizontal is not None else ppd_1D
    shape = resolution.validate_shape(shape)
    visual_size = resolution.validate_visual_size(visual_size)
    ppd = resolution.validate_ppd(ppd)

    # Mask bars
    base = image_base(shape=shape, ppd=ppd, visual_size=visual_size)
    distances = base[orientation]
    distances -= distances.min()

    mask = np.zeros(shape, dtype=int)
    for idx, edge in zip(reversed(range(len(params["edges"]))), reversed(params["edges"])):
        mask[distances <= edge] = int(idx + 1)

    return {
        "mask": mask,
        "shape": shape,
        "visual_size": visual_size,
        "ppd": ppd,
        "frequency": params["frequency"],
        "bar_width": params["phase_width"],
        "n_bars": params["n_phases"],
        "period": params["period"],
        "orientation": orientation,
    }


def square_wave(
    shape=None,
    visual_size=None,
    ppd=None,
    frequency=None,
    n_bars=None,
    bar_width=None,
    period="ignore",
    orientation="horizontal",
    intensity_bars=(0.0, 1.0),
):
    """Draw square-wave grating (set of bars) of given spatial frequency

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
    n_bars : int, or None (default)
        number of bars in the grating
    bar_width : Number, or None (default)
        width of a single bar, in degrees visual angle
    period : "full", "half", "ignore" (default)
        whether to ensure the grating only has "full" periods,
        half "periods", or no guarantees ("ignore")
    orientation : "vertical" or "horizontal" (default)
        orientation of the grating
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

    # Get bars mask
    stim = mask_bars(
        shape=shape,
        visual_size=visual_size,
        ppd=ppd,
        frequency=frequency,
        n_bars=n_bars,
        bar_width=bar_width,
        orientation=orientation,
        period=period,
    )
    mask = stim["mask"]

    # Draw bars
    img = np.zeros(mask.shape)
    ints = [*itertools.islice(itertools.cycle(intensity_bars), len(np.unique(mask)))]
    for bar_idx, intensity in zip(np.unique(mask), ints):
        img = np.where(mask == bar_idx, intensity, img)

    return {"img": img, **stim}
