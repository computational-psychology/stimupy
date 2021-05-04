import numpy as np
from stimuli.illusions.rings import ring_pattern


def bullseye_illusion(n_rings=8, ring_width=5, padding=10, back=0., rings=1., target=.5):
    """
    Bullseye Illusion.
    Two ring patterns (see ring_pattern func), with target in centre and one ring pattern inverted.

    Parameters
    ----------
    n_rings: the number of rings
    ring_width: width per ring in px
    padding: padding around stimulus in px
    back: value for background
    rings: value for grid cells
    target: value for target

    Returns
    -------
    2D numpy array
    """
    img1 = ring_pattern(n_rings=n_rings, target_pos_l=0, ring_width=ring_width, padding=padding,
                        back=back, rings=rings, target=target, invert_rings=False, double=False)
    img2 = ring_pattern(n_rings=n_rings, target_pos_l=0, ring_width=ring_width, padding=padding,
                        back=back, rings=rings, target=target, invert_rings=True, double=False)
    return np.hstack([img1, img2])

def domijan2015():
    return bullseye_illusion(n_rings=8, ring_width=5, padding=10, back=1., rings=9., target=5.)

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
    input_image[24:75, 24:75] = lum_black
    input_image[29:70, 29:70] = lum_white
    input_image[34:65, 34:65] = lum_black
    input_image[39:60, 39:60] = lum_white
    input_image[44:55, 44:55] = lum_gray

    input_image[14:85, 114:185] = lum_white
    input_image[19:80, 119:180] = lum_black
    input_image[24:75, 124:175] = lum_white
    input_image[29:70, 129:170] = lum_black
    input_image[34:65, 134:165] = lum_white
    input_image[39:60, 139:160] = lum_black
    input_image[44:55, 144:155] = lum_gray

    return input_image



