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
    img = np.pad(img, padding, constant_values=back, mode="constant")

    # create right half of stimulus
    if double:
        img2 = ring_pattern(n_rings, target_pos_r, 0, ring_width, padding, back, rings, target, invert_rings, double=False)
        return np.hstack([img, img2])
    else:
        return img

def domijan2015():
    return ring_pattern(n_rings=8, target_pos_l=4, target_pos_r=3, ring_width=5, padding=10, back=1., rings=9., target=5., invert_rings=False, double=True)

def lynn_domijan2015():
    """
    there's one pixel translation between the stimuli package and utils generated inputs
    (see pixels [9,9] and [10,10] in reults from this and previous functions)
    """

    lum_white = 9.
    lum_black = 1.
    lum_gray = 5.

    input_image = lum_black * np.ones([100, 200])
    input_image[9:90, 9:90] = lum_white
    input_image[14:85, 14:85] = lum_black
    input_image[19:80, 19:80] = lum_white
    input_image[24:75, 24:75] = lum_gray
    input_image[29:70, 29:70] = lum_white
    input_image[34:65, 34:65] = lum_black
    input_image[39:60, 39:60] = lum_white
    input_image[44:55, 44:55] = lum_black

    input_image[9:90, 109:190] = lum_white
    input_image[14:85, 114:185] = lum_black
    input_image[19:80, 119:180] = lum_white
    input_image[24:75, 124:175] = lum_black
    input_image[29:70, 129:170] = lum_gray
    input_image[34:65, 134:165] = lum_black
    input_image[39:60, 139:160] = lum_white
    input_image[44:55, 144:155] = lum_black

    return input_image
