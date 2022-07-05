import numpy as np
from stimuli.utils import degrees_to_pixels, pad_img_to_shape
from stimuli.components import square_wave_grating


def grating_illusion(
    ppd=10,
    n_bars=8,
    target_indices=(2, 4),
    bar_shape=(8, 1.),
    vbar1=0.0,
    vbar2=1.0,
    vtarget=0.5
):
    """
    Grating illusion

    Parameters
    ----------
    ppd : int
        pixels per degree (visual angle)
    n_bars : int
        the number of vertical bars
    target_indices : tuple
        tuple with bar target indices from left to right
    bar_shape : (float, float)
        bar height and width in degrees visual angle
    vbar1 : float
        value for bar 1
    vbar2 : float
        value for bar 2
    vtarget : float
        value for target

    Returns
    -------
    A stimulus dictionary with the stimulus ['img'] and target mask ['mask']
    """

    bar_width_px = degrees_to_pixels(bar_shape[1], ppd)
    img = square_wave_grating(ppd, n_bars, bar_shape, vbar1, vbar2)
    mask = np.zeros(img.shape)

    if isinstance(target_indices, (float, int)):
        target_indices = (target_indices,)

    for i, idx in enumerate(target_indices):
        img[:, idx*bar_width_px:(idx+1)*bar_width_px] = vtarget
        mask[:, idx*bar_width_px:(idx+1)*bar_width_px] = i + 1
    return {"img": img, "mask": mask}


def grating_uniform(
        ppd=10,
        n_bars=8,
        bar_shape=(0.5, 4.),
        im_size=(10., 10.),
        vback=0.,
        vbar=1.,
        vtarget=0.5,
        ):
    """
    Grating on a uniform background

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
    vback : float
        value for background
    vbar : float
        value for bar
    vtarget : float
        value for other bar which indicates target

    Returns
    -------
    A stimulus dictionary with the stimulus ['img'] and target mask ['mask']
    """

    # Create and rotate square-wave grating
    bar_shape = (bar_shape[1], bar_shape[0])
    img = square_wave_grating(ppd, n_bars, bar_shape, vbar, vtarget)
    img = np.rot90(img)
    mask = np.zeros(img.shape)
    mask[img == vtarget] = 1

    # Padding
    im_size_px = degrees_to_pixels(im_size, ppd)
    img = pad_img_to_shape(img, im_size_px, vback)
    mask = pad_img_to_shape(mask, im_size_px, 0)
    return {"img": img, "mask": mask}


def grating_grating(
        ppd=10,
        n_bars=8,
        bar_shape=(0.5, 4.),
        im_size=(10.3, 10.3),
        vbar1=0.,
        vbar2=1.,
        vtarget=0.5,
        ):
    """
    Grating on a grating

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
    vbar1 : float
        value for bar1
    vbar2 : float
        value for bar2
    vtarget : float
        value for target bar

    Returns
    -------
    A stimulus dictionary with the stimulus ['img'] and target mask ['mask']
    """

    # Create and rotate square-wave grating
    bar_shape = (bar_shape[1], bar_shape[0])
    img_small = square_wave_grating(ppd, n_bars, bar_shape, vbar1, vtarget)
    img_small = np.rot90(img_small)
    mask_small = np.zeros(img_small.shape)
    mask_small[img_small == vtarget] = 1

    nbars = int(np.ceil(im_size[0] / bar_shape[1]))
    barshape = (im_size[1], bar_shape[1])
    img_large = square_wave_grating(ppd, nbars, barshape, vbar1, vbar2)
    img_large = np.rot90(img_large)

    # Reduce size to desired size
    im_size_px = degrees_to_pixels(im_size, ppd)
    img_large = img_large[0:im_size_px[0], 0:im_size_px[1]]

    # Incorporate small grating in large grating
    nbars = nbars + (nbars % 2)
    bar_height_px = degrees_to_pixels(bar_shape[1], ppd)
    ys = int((nbars*bar_height_px - img_small.shape[0]) / 2)
    xs = (im_size_px[1] - img_small.shape[1]) // 2
    img_large[ys:ys+img_small.shape[0], xs:xs+img_small.shape[1]] = img_small

    mask_large = np.zeros(img_large.shape)
    mask_large[ys:ys+img_small.shape[0], xs:xs+img_small.shape[1]] = mask_small
    return {"img": img_large, "mask": mask_large}


def grating_grating_shifted(
        ppd=10,
        n_bars=8,
        bar_shape=(0.5, 4.),
        im_size=(10., 10.),
        vbar1=0.,
        vbar2=1.,
        vtarget=0.5,
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
    vbar1 : float
        value for bar1
    vbar2 : float
        value for bar2
    vtarget : float
        value for target bar

    Returns
    -------
    A stimulus dictionary with the stimulus ['img'] and target mask ['mask']
    """

    stim = grating_grating(ppd, n_bars, bar_shape, im_size, vbar1, vbar2, vtarget)
    img = stim['img']
    mask = stim['mask']

    bar_height, bar_width = degrees_to_pixels(bar_shape, ppd)
    xs = int((img.shape[1] - bar_width) / 2)
    img_col = np.ones([img.shape[0], bar_width]) * vbar1
    img_col[bar_height::, :] = img[0:img_col.shape[0]-bar_height, xs:xs+bar_width]
    img[:, xs:xs+bar_width] = img_col

    mask_col = np.zeros([mask.shape[0], bar_width])
    mask_col[bar_height::, :] = mask[0:mask_col.shape[0]-bar_height, xs:xs+bar_width]
    mask[:, xs:xs+bar_width] = mask_col
    return {"img": img, "mask": mask}


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    from stimuli.utils import plot_stimuli

    stims = {
        "Grating illusion": grating_illusion(),
        "Grating - uniform": grating_uniform(),
        "Grating - grating": grating_grating(),
        "Grating - grating shifted": grating_grating_shifted(),
    }

    plot_stimuli(stims, mask=True)
    plt.show()
