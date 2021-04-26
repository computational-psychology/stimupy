import numpy as np


def ring_pattern(n_rings=8, target_pos_l=4, target_pos_r=3, ring_width=5, padding=10, back=0., rings=1., target=.5, invert_rings=False, double=True):
    """
    Ring Pattern White's-like illusion

    Parameters
    ----------
    n_rings: the number of rings
    target_pos_l: the "index" of the target ring on the left half
    target_pos_r: the "index" of the targetring on the right half
    ring_width: width per ring in px
    padding: padding around stimulus in px
    back: value for background
    rings: value for grid cells
    target: value for target
    invert_rings: inverts ordering of rings and background
    double: whether to return the full illusion with two grids side-by-side (inverting back and grid values)

    Returns
    -------
    2D numpy array
    """
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
    img = np.pad(img, padding, constant_values=back)

    # create right half of stimulus
    if double:
        img2 = ring_pattern(n_rings, target_pos_r, 0, ring_width, padding, back, rings, target, invert_rings, double=False)
        return np.hstack([img, img2])
    else:
        return img
