import itertools

import numpy as np

from stimuli.components import square_wave as square_wave_component
from stimuli.components import square_wave_grating
from stimuli.utils import degrees_to_pixels, pad_to_visual_size


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
    target_indices=(2, 4),
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
    target_indices=(2, 4),
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
    visual_size=(10.3, 10.3),
    ppd=10,
    n_bars=8,
    bar_shape=(0.5, 4.0),
    intensity_bars=(0.0, 1.0),
    intensity_target=0.5,
):
    """
    Grating on a grating

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

    # Create and rotate square-wave grating
    bar_shape = (bar_shape[1], bar_shape[0])
    img_small = square_wave_grating(
        ppd=ppd,
        n_bars=n_bars,
        bar_shape=bar_shape,
        intensity_bars=(intensity_bars[0], intensity_target),
        )["img"]
    img_small = np.rot90(img_small)
    mask_small = np.zeros(img_small.shape)
    mask_small[img_small == intensity_target] = 1

    nbars = int(np.ceil(visual_size[0] / bar_shape[1]))
    barshape = (visual_size[1], bar_shape[1])
    img_large = square_wave_grating(
        ppd=ppd,
        n_bars=nbars,
        bar_shape=barshape,
        intensity_bars=(intensity_bars[0], intensity_bars[1]),
        )["img"]
    img_large = np.rot90(img_large)

    # Reduce size to desired size
    im_size_px = degrees_to_pixels(visual_size, ppd)
    img_large = img_large[0 : im_size_px[0], 0 : im_size_px[1]]

    # Incorporate small grating in large grating
    nbars = nbars + (nbars % 2)
    bar_height_px = degrees_to_pixels(bar_shape[1], ppd)
    ys = int((nbars * bar_height_px - img_small.shape[0]) / 2)
    xs = (im_size_px[1] - img_small.shape[1]) // 2
    img_large[ys : ys + img_small.shape[0], xs : xs + img_small.shape[1]] = img_small

    mask_large = np.zeros(img_large.shape)
    mask_large[ys : ys + img_small.shape[0], xs : xs + img_small.shape[1]] = mask_small
    
    stim = {
        "img": img_large,
        "mask": mask_large.astype(int),
        "ppd": ppd,
        "visual_size": np.array(img_large.shape) / ppd,
        "shape": img_large.shape,
        "n_bars": n_bars,
        "bar_shape": bar_shape,
        "intensity_bars": intensity_bars,
        "intensity_target": intensity_target,
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

    stims = {
        "Grating illusion": square_wave(
            ppd=10,
            n_bars=8,
            bar_width=1.0,
            target_indices=(2, 7),
        ),
        "Grating - uniform": grating_uniform(),
        "Grating - grating": grating_grating(),
        "Grating - grating shifted": grating_grating_shifted(),
    }

    plot_stimuli(stims, mask=False)
    plt.show()
