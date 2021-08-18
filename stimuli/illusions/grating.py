import numpy as np
from stimuli.utils import degrees_to_pixels, pad_img, plot_stim
from stimuli.Stimulus import Stimulus
from stimuli import illusions

def grating_illusion(ppd=10, n_bars=5, target_length=2, bar_width=1.0, bar_height=8.0, padding=(1.0,1.0,1.0,1.0), back=0., grid=1., target=0.5, double=True):
    """
    Grating illusion

    Parameters
    ----------
    ppd : int
        pixels per degree (visual angle)
    n_bars : int
        the number of vertical bars
    target_length : int
        #bars that make up the target
    bar_width : float
        width of bar in degrees visual angle
    bar_height : float
        height of bar in degrees visual angle
    padding : (float, float, float, float)
        4-valued tuple specifying padding (top, bottom, left, right) in degrees visual angle
    back : float
        value for background
    grid : float
        value for grid cells
    target : float
        value for target
    double : bool
        whether to return the full illusion with two grids side-by-side (inverting back and grid values)

    Returns
    -------
    A stimulus object
    """

    bar_height_px, bar_width_px = degrees_to_pixels(bar_height, ppd), degrees_to_pixels(bar_width, ppd)

    # create array of grating
    arr = np.ones(n_bars) * grid
    mask_arr = np.zeros(n_bars)

    target_offset = (n_bars-target_length)//2
    arr[target_offset:target_offset+target_length] = target
    for i, j in enumerate(range(target_offset,target_offset+target_length)):
        mask_arr[j] = i+1

    # final image array
    width_px = (n_bars*2-1)*bar_width_px
    height_px = bar_height_px
    img = np.ones((height_px, width_px)) * back
    mask = np.zeros((height_px, width_px))

    for i, val in np.ndenumerate(arr):
        target_val = val==target
        x = i[0]*2*bar_width_px
        img[:, x:x+bar_width_px] = val
        if target_val:
            mask[:, x:x+bar_width_px] = mask_arr[i]

    img = pad_img(img, padding, ppd, back)
    mask = pad_img(mask, padding, ppd, 0)


    if double:
        stim2 = grating_illusion(ppd=ppd, n_bars=n_bars, target_length=target_length, bar_width=bar_width, bar_height=bar_height,
                                padding=padding, back=grid, grid=back, target=target, double=False)
        img = np.hstack([img, stim2.img])
        mask = np.hstack([mask, stim2.target_mask])

    stim = Stimulus()
    stim.img = img
    stim.target_mask = mask

    return stim

def domijan2015():
    return illusions.grating_illusion(ppd=10, n_bars=5, target_length=1, bar_width=1.0, bar_height=8.1, padding=(.9,1.0,.9,1.1), back=1, grid=9, target=5, double=True)


if __name__ == '__main__':
    import matplotlib.pyplot as plt
    stim = grating_illusion()
    plot_stim(stim, mask=True)
