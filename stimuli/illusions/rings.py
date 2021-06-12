import numpy as np
from stimuli import utils

def ring_pattern(n_rings=8, target_pos_l=4, target_pos_r=3, ring_width=5, padding=10, back=0., rings=1., target=.5, invert_rings=False, double=True, ):
    """
    Ring Pattern White's-like illusion

    Parameters
    ----------
    n_rings: the number of rings
    target_pos_l: the "index" of the target ring on the left half
    target_pos_r: the "index" of the targetring on the right half
    ring_width: width per ring in px
    padding: 4-valued tuple specifying padding (top, bottom, left, right) in px
    back: value for background
    rings: value for grid cells
    target: value for target
    invert_rings: inverts ordering of rings and background
    double: whether to return the full illusion with two grids side-by-side (inverting back and grid values)

    Returns
    -------
    2D numpy array
    """

    padding_top, padding_bottom, padding_left, padding_right = padding


    # calculate Minkowski-p=inf distances from centre
    x = np.arange(0, n_rings)
    x = np.hstack([np.flip(x), x])
    radii = np.maximum(np.abs(x[np.newaxis]), np.abs(x[:, np.newaxis]))

    # build array representing rings
    arr = np.ones((n_rings*2, n_rings*2)) * back
    arr[radii % 2 == (0 if invert_rings else 1)] = rings
    arr[radii == target_pos_l] = target

    # build image from array
    img = np.repeat(np.repeat(arr, ring_width, axis=0), ring_width, axis=1)
    img = np.pad(img, ((padding_top, padding_bottom), (padding_left, padding_right)), constant_values=back, mode="constant")

    y_c, x_c = img.shape
    y_c //=2
    x_c //=2

    row_c = img[y_c, :]
    img = np.insert(img, y_c, row_c, axis=0)

    col_c = img[:, x_c]
    img = np.insert(img, x_c, col_c, axis=1)



    # create right half of stimulus
    if double:
        img2 = ring_pattern(n_rings=n_rings, target_pos_l=target_pos_r, target_pos_r=0, ring_width=ring_width,
                            padding=padding, back=back, rings=rings, target=target, invert_rings=invert_rings, double=False)
        return np.hstack([img, img2])
    else:
        return img

def domijan2015():
    img = ring_pattern(n_rings=8, target_pos_l=4, target_pos_r=3, ring_width=5, padding=(9,10,9,10), back=1., rings=9., target=5., invert_rings=False, double=True)
    return img


