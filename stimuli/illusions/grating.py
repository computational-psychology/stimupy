import numpy as np


def grating_illusion(n_bars=5, target_length=1, bar_width=10, back=0., grid=1., target=0.5, double=True):
    """
    Grating illusion

    Parameters
    ----------
    n_bars: the number of vertical bars
    target_length: # bars that make up the target
    bar_width: width of bar in px (height is determined by making the image square)
    back: value for background
    grid: value for grid cells
    target: value for target
    double: whether to return the full illusion with two grids side-by-side (inverting back and grid values)

    Returns
    -------
    2D numpy array
    """
    # create array of grating
    arr = np.ones(n_bars) * grid
    target_offset = (n_bars-target_length)//2
    arr[target_offset:target_offset+target_length] = target

    # final image array
    size = n_bars*2*bar_width + bar_width
    img = np.ones((size, size)) * back

    for i, val in np.ndenumerate(arr):
        x = i[0]*2*bar_width + bar_width
        img[bar_width:-bar_width, x:x+bar_width] = val

    if double:
        img2 = grating_illusion(n_bars, target_length, bar_width, back=grid, grid=back, target=target, double=False)
        return np.hstack([img, img2])
    else:
        return img