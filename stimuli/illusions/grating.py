import numpy as np


def grating_illusion(n_bars=5, target_length=1, bar_width=10, bar_height=80, padding=(10,10,10,10), back=0., grid=1., target=0.5, double=True):
    """
    Grating illusion

    Parameters
    ----------
    n_bars: the number of vertical bars
    target_length: # bars that make up the target
    bar_width: width of bar in px
    bar_height: height of bar in px
    padding: 4-valued tuple specifying padding (top, bottom, left, right) in px
    back: value for background
    grid: value for grid cells
    target: value for target
    double: whether to return the full illusion with two grids side-by-side (inverting back and grid values)

    Returns
    -------
    2D numpy array
    """

    padding_top, padding_bottom, padding_left, padding_right = padding

    # create array of grating
    arr = np.ones(n_bars) * grid
    target_offset = (n_bars-target_length)//2
    arr[target_offset:target_offset+target_length] = target

    # final image array
    width = (n_bars*2-1)*bar_width + padding_left + padding_right
    height = padding_top + bar_height + padding_bottom
    img = np.ones((height, width)) * back

    for i, val in np.ndenumerate(arr):
        x = padding_left + i[0]*2*bar_width
        img[padding_top:padding_top+bar_height, x:x+bar_width] = val

    if double:
        img2 = grating_illusion(n_bars=n_bars, target_length=target_length, bar_width=bar_width, bar_height=bar_height,
                                padding=padding, back=grid, grid=back, target=target, double=False)
        return np.hstack([img, img2])
    else:
        return img

def domijan2015():
    return grating_illusion(n_bars=5, target_length=1, bar_width=10, bar_height=81, padding=(9,10,9,11), back=1, grid=9, target=5, double=True)

