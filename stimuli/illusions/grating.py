import itertools

import numpy as np
from scipy.ndimage import gaussian_filter

from stimuli.components import rectangle
from stimuli.components import square_wave as square_wave_component
from stimuli.utils import pad_to_shape, pad_to_visual_size


def square_wave(
    shape=None,
    visual_size=None,
    ppd=None,
    frequency=None,
    n_bars=None,
    bar_width=None,
    orientation="horizontal",
    period="ignore",
    intensity_bars=(0.0, 1.0),
    target_indices=(),
    intensity_target=0.5,
):
    """Spatial square-wave grating (set of bars), with some bar(s) as target(s)

    Parameters
    ----------
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of grating, in pixels
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of grating, in degrees
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
    target_indices : int, or Sequence[int, ...]
        indices segments where targets will be placed
    intensity_target : float, or Sequence[float, ...], optional
        intensity value for each target, by default 0.5.
        Can specify as many intensities as number of target_indices;
        If fewer intensities are passed than target_indices, cycles through intensities

    Returns
    ----------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for each target (key: "mask"),
        and additional keys containing stimulus parameters
    """

    # Spatial square-wave grating
    stim = square_wave_component(
        shape=shape,
        visual_size=visual_size,
        ppd=ppd,
        frequency=frequency,
        n_bars=n_bars,
        bar_width=bar_width,
        orientation=orientation,
        period=period,
        intensity_bars=intensity_bars,
    )

    # Resolve target parameters
    if isinstance(target_indices, (int)):
        target_indices = [
            target_indices,
        ]
    if isinstance(intensity_target, (int, float)):
        intensity_target = [
            intensity_target,
        ]
    intensity_target = itertools.cycle(intensity_target)

    # Place target(s)
    targets_mask = np.zeros_like(stim["mask"])
    for target_idx, (bar_idx, intensity) in enumerate(zip(target_indices, intensity_target)):
        targets_mask = np.where(stim["mask"] == bar_idx, target_idx + 1, targets_mask)
        stim["img"] = np.where(targets_mask == target_idx + 1, intensity, stim["img"])

    # Update and return stimulus
    stim["bars_mask"] = stim["mask"]
    stim["mask"] = targets_mask

    return stim


def grating_uniform(
    shape=None,
    visual_size=None,
    ppd=None,
    frequency=None,
    n_bars=None,
    bar_width=None,
    orientation="horizontal",
    period="ignore",
    intensity_bars=(0.0, 1.0),
    target_indices=(),
    intensity_target=0.5,
    image_size=None,
    intensity_background=0.5,
):
    """Spatial square-wave grating (set of bars), on a background

    Parameters
    ----------
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of grating, in pixels
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of grating, in degrees
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
    target_indices : int, or Sequence[int, ...]
        indices segments where targets will be placed
    image_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of total image, in degrees
    intensity_background : float
        intensity value of background, by default 0.5.

    Returns
    ----------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for each bar (key: "mask"),
        and additional keys containing stimulus parameters
    """

    # Spatial square-wave grating
    stim = square_wave(
        shape=shape,
        visual_size=visual_size,
        ppd=ppd,
        frequency=frequency,
        n_bars=n_bars,
        bar_width=bar_width,
        orientation=orientation,
        period=period,
        intensity_bars=intensity_bars,
        target_indices=target_indices,
        intensity_target=intensity_target,
    )

    # Padding
    stim["img"] = pad_to_visual_size(
        img=stim["img"], visual_size=image_size, ppd=ppd, pad_value=intensity_background
    )
    stim["mask"] = pad_to_visual_size(
        img=stim["mask"], visual_size=image_size, ppd=ppd, pad_value=0
    )

    # Repack
    stim.update(
        intensity_background=intensity_background,
        grating_size=stim["visual_size"],
        grating_shape=stim["shape"],
        shape=stim["img"].shape,
        visual_size=image_size,
    )

    return stim


def grating_grating(
    small_grating_params,
    large_grating_params,
    ppd=None,
):
    """Grating on a grating

    Parameters
    ----------
    small_grating_params : dict
        kwargs to generate small grating
    large_grating_params : dict
        kwargs to generate larger grating
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]

    Returns
    ----------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for each bar (key: "mask"),
        and additional keys containing stimulus parameters
    """

    # Create gratings
    small_grating = square_wave(ppd=ppd, **small_grating_params)
    large_grating = square_wave(ppd=ppd, **large_grating_params)

    # Superimpose
    small_grating_mask = rectangle(
        rectangle_size=small_grating["visual_size"],
        ppd=ppd,
        visual_size=large_grating["visual_size"],
        intensity_background=0,
        intensity_rectangle=1,
        rectangle_position=(
            np.array(large_grating["visual_size"]) - np.array(small_grating["visual_size"])
        )
        / 2,
    )
    small_grating["img"] = pad_to_shape(small_grating["img"], shape=large_grating["img"].shape)
    small_grating["mask"] = pad_to_shape(small_grating["mask"], shape=large_grating["img"].shape)
    img = np.where(small_grating_mask["mask"], small_grating["img"], large_grating["img"])
    mask = np.where(small_grating_mask["mask"], small_grating["mask"], large_grating["img"])

    stim = {
        "img": img,
        "mask": mask.astype(int),
        "ppd": ppd,
    }
    return stim


def grating_grating_shifted(
    shifted_width,
    visual_size=None,
    shape=None,
    ppd=None,
    frequency=None,
    n_bars=None,
    bar_width=None,
    orientation="horizontal",
    period="ignore",
    intensity_bars=(0.0, 1.0),
    target_indices=(),
    intensity_target=0.5,
):
    """Spatial square-wave grating, with a central strip "shifted" (phase-offset)

    Parameters
    ----------
    shifted_width : float
        width of central strip to be shifted
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of the larger grating, in degrees
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of grating, in pixels
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
    target_indices : int, or Sequence[int, ...]
        indices segments where targets will be placed
    intensity_target : float, or Sequence[float, ...], optional
        intensity value for each target, by default 0.5.
        Can specify as many intensities as number of target_indices;
        If fewer intensities are passed than target_indices, cycles through intensities

    Returns
    ----------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for each target (key: "mask"),
        and additional keys containing stimulus parameters
    """

    # Resolve initial params
    large_params = {
        "shape": shape,
        "visual_size": visual_size,
        "frequency": frequency,
        "n_bars": n_bars,
        "bar_width": bar_width,
        "orientation": orientation,
        "period": period,
        "intensity_bars": reversed(intensity_bars),
    }
    large_grating = square_wave(ppd=ppd, **large_params)

    # Specify shifted section
    small_params = {
        "frequency": large_grating["frequency"],
        "bar_width": large_grating["bar_width"],
        "n_bars": large_grating["n_bars"],
        "orientation": orientation,
        "period": period,
        "intensity_bars": intensity_bars,
        "target_indices": target_indices,
        "intensity_target": intensity_target,
    }
    if orientation == "horizontal":
        small_params["visual_size"] = (shifted_width, large_grating["visual_size"].width)
    elif orientation == "vertical":
        small_params["visual_size"] = (large_grating["visual_size"].height, shifted_width)

    # Update larger grating params
    large_params.update(
        shape=large_grating["shape"],
        visual_size=large_grating["visual_size"],
        intensity_bars=reversed(intensity_bars),
    )

    # Generate
    stim = grating_grating(
        ppd=ppd, small_grating_params=small_params, large_grating_params=large_params
    )

    return stim


def grating_induction(
    visual_size=(10, 10),
    ppd=40,
    grating_frequency=0.5,
    target_height=0.5,
    blur=5,
    intensity_bars=(0.0, 1.0),
    intensity_target=0.5,
    period="ignore",
):
    """
    Grating induction illusions

    Parameters
    ----------
    visual_size : float or (float, float)
        size of the image in degrees visual angle
    ppd : int
        pixels per degree (visual angle)
    grating_frequency : float
        frequency of the grid in cycles per degree visual angle
    target_height : float
        height of the target in degrees visual angle
    blur : float
        amount of blur to apply
    intensity_bars : (float, float)
        intensity values of bars
    intensity_target : float
        intensity value of targets
    period : string in ['ignore', 'full', 'half']
        specifies if the period of the wave is considered for stimulus dimensions.
            'ignore' simply converts degrees to pixels
            'full' rounds down to guarantee a full period
            'half' adds a half period to the size 'full' would yield.
        Default is 'ignore'.

    Returns
    -------
    A stimulus dictionary with the stimulus ['img'] and target mask ['mask']
    """

    stim = square_wave(
        visual_size=visual_size,
        ppd=ppd,
        frequency=grating_frequency,
        intensity_bars=intensity_bars,
        period=period,
    )
    img = stim["img"]
    height, width = stim["shape"]
    theight = int(target_height * stim["ppd"].vertical)

    tstart = int(height) // 2 - theight // 2
    tend = tstart + theight

    low = np.minimum(intensity_bars[0], intensity_bars[1])
    high = np.maximum(intensity_bars[0], intensity_bars[1])
    mask = np.zeros((height, width))
    mask[tstart:tend, :] = (img[tstart:tend, :] - low) / (high - low) + 1

    img = gaussian_filter(img, blur)
    img[tstart:tend, :] = intensity_target

    params = {
        "shape": img.shape,
        "visual_size": np.array(img.shape) / ppd,
        "ppd": ppd,
        "grating_frequency": grating_frequency,
        "intensity_bars": intensity_bars,
        "intensity_target": intensity_target,
        "target_height": target_height,
        "blur": blur,
        "period": period,
    }

    return {"img": img, "mask": mask.astype(int), **params}


if __name__ == "__main__":
    import matplotlib.pyplot as plt

    from stimuli.utils import plot_stimuli

    ppd = 10
    bar_width = 1.0
    orientation = "vertical"
    small_grating_params = {
        "n_bars": 8,
        "bar_width": bar_width,
        "orientation": orientation,
    }
    large_grating_params = {
        "bar_width": bar_width,
        "visual_size": (32, 32),
        "orientation": orientation,
    }

    stims = {
        "Grating with targets": square_wave(
            ppd=ppd, **small_grating_params, intensity_bars=(0.0, 1.0), target_indices=(3, 6)
        ),
        "Grating on uniform background": grating_uniform(
            ppd=ppd,
            **small_grating_params,
            intensity_bars=(0.0, 1.0),
            image_size=(32, 32),
            target_indices=(3, 6),
        ),
        "Grating on grating": grating_grating(
            ppd=ppd,
            small_grating_params={
                **small_grating_params,
                "intensity_bars": (0.0, 0.5),
            },
            large_grating_params=large_grating_params,
        ),
        "Grating on grating, shifted": grating_grating_shifted(
            shifted_width=8.0,
            ppd=ppd,
            target_indices=(13, 18),
            **large_grating_params,
        ),
        "Grating induction": grating_induction(),
    }

    plot_stimuli(stims, mask=False)
    plt.show()
