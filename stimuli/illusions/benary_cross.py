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
