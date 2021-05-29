import numpy as np


def benarys_cross(input_size=100, cross_thickness=20, padding=10, back=1., cross=0., target=.5):
    """
    Benary's Cross Illusion (with square targets)

    Parameters
    ----------
    input_size: width and height of input in px
    cross_thickness: width of the cross bars in px
    padding: padding around cross in px
    back: background value
    cross: cross value
    target: target value

    Returns
    -------
    2D numpy array
    """
    img = np.ones((input_size, input_size)) * back

    cpos = (input_size - cross_thickness) // 2
    img[padding:-padding, cpos:-cpos] = cross
    img[cpos:-cpos, padding:-padding] = cross

    tsize = cross_thickness // 2
    tpos1y = cpos - tsize
    tpos1x = tpos1y
    tpos2y = cpos
    tpos2x = input_size - padding - tsize
    img[tpos1y:tpos1y + tsize, tpos1x:tpos1x + tsize] = target
    img[tpos2y:tpos2y + tsize, tpos2x:tpos2x + tsize] = target

    return img

def domijan2015():
    return benarys_cross(input_size=100, cross_thickness=20, padding=10, back=9., cross=1., target=5.)

def lynn_domijan2015():
    """
    there's one pixel translation between the stimuli package and utils generated inputs
    (see pixels [39,9] and [40,10] in reults from this and previous functions)
    """
    lum_white = 9.
    lum_black = 1.
    lum_gray = 5.

    input_image = lum_white * np.ones([100, 100])
    input_image[39:60, 9:90] = lum_black
    input_image[9:90, 39:60] = lum_black
    input_image[39:50, 79:90] = lum_gray
    input_image[28:39, 28:39] = lum_gray

    return input_image


