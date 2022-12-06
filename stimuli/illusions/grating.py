import itertools

import numpy as np

from stimuli.components import rectangle
from stimuli.components import square_wave as square_wave_component
from stimuli.components import square_wave_grating
from stimuli.utils import degrees_to_pixels, pad_to_shape, pad_to_visual_size


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
    visual_size : float or (float, float)
        size of the image in degrees visual angle
    ppd : int
        pixels per degree (visual angle)
    n_bars : int
        the number of vertical bars
    bar_shape : (float, float)
        bar height and width in degrees visual angle
    intensity_bars : (float, float)
        intensity values for bars
    intensity_target : float
        value for target bar

    Returns
    -------
    A stimulus dictionary with the stimulus ['img'] and target mask ['mask']
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
    visual_size=(10., 10.),
    ppd=10,
    n_bars=8,
    bar_shape=(0.5, 4.0),
    intensity_bars=(0.0, 1.0),
    intensity_target=0.5,
):
    """
    Grating on a shifted grating

    Parameters
    ----------
    ppd : int
        pixels per degree (visual angle)
    n_bars : int
        the number of vertical bars
    bar_shape : (float, float)
        bar height and width in degrees visual angle
    im_size : (float, float)
        height and width of stimulus in visual angle
    intensity_bars : (float, float)
        intensity values for bars
    intensity_target : float
        value for target bar

    Returns
    -------
    A stimulus dictionary with the stimulus ['img'] and target mask ['mask']
    """

    stim = grating_grating(
        visual_size=visual_size,
        ppd=ppd,
        n_bars=n_bars,
        bar_shape=bar_shape,
        intensity_bars=intensity_bars,
        intensity_target=intensity_target,
        )
    img = stim["img"]
    mask = stim["mask"]

    bar_height, bar_width = degrees_to_pixels(bar_shape, ppd)
    xs = int((img.shape[1] - bar_width) / 2)
    img_col = np.ones([img.shape[0], bar_width]) * intensity_bars[0]
    img_col[bar_height::, :] = img[0 : img_col.shape[0] - bar_height, xs : xs + bar_width]
    img[:, xs : xs + bar_width] = img_col

    mask_col = np.zeros([mask.shape[0], bar_width])
    mask_col[bar_height::, :] = mask[0 : mask_col.shape[0] - bar_height, xs : xs + bar_width]
    mask[:, xs : xs + bar_width] = mask_col
    
    stim = {
        "img": img,
        "mask": mask.astype(int),
        "ppd": ppd,
        "visual_size": np.array(img.shape) / ppd,
        "shape": img.shape,
        "n_bars": n_bars,
        "bar_shape": bar_shape,
        "intensity_bars": intensity_bars,
        "intensity_target": intensity_target,
        }
    return stim


if __name__ == "__main__":
    import matplotlib.pyplot as plt

    from stimuli.utils import plot_stimuli

    ppd = 10
    bar_width = 1.0
    small_grating_params = {
        "n_bars": 8,
        "bar_width": bar_width,
    }
    large_grating_params = {
        "bar_width": bar_width,
        "visual_size": (32, 32),
    }

    stims = {
        "Grating illusion": square_wave(
            ppd=ppd, **small_grating_params, intensity_bars=(0.0, 1.0), target_indices=(2, 7)
        ),
        "Grating - uniform": grating_uniform(
            ppd=ppd, **small_grating_params, intensity_bars=(0.0, 1.0), image_size=(32, 32)
        ),
        "Grating - grating": grating_grating(
            ppd=ppd,
            small_grating_params={**small_grating_params, "intensity_bars": (0.0, 0.5)},
            large_grating_params=large_grating_params,
        ),
        # "Grating - grating shifted": grating_grating_shifted(),
    }

    plot_stimuli(stims, mask=False)
    plt.show()
