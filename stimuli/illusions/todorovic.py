import numpy as np


def todorovic_illusion(input_size=100, target_size=40, spacing=5, padding=15, back=0., grid=1., target=.5, double=True):
    """
    Todorovic's illusion

    Parameters
    ----------
    input_size: height of the input (and half of the width) in px
    target_size: height and width of the centred target cross in px
    spacing: spacing between grid cells (i.e target cross bar thickness) in px
    padding: padding around grid in px
    back: value for background
    grid: value for grid cells
    target: value for target
    double: whether to return the full illusion with two grids side-by-side (inverting back and grid values)

    Returns
    -------

    """
    img = np.ones((input_size, input_size)) * back

    # put target square on image
    tpos = (input_size-target_size)//2
    img[tpos:-tpos, tpos:-tpos] = target

    # put grid cells on image
    csize = (input_size - 2*padding - spacing)//2
    gpos1 = padding
    gpos2 = padding + csize + spacing
    img[gpos1:gpos1+csize, gpos1:gpos1+csize] = grid
    img[gpos1:gpos1+csize, gpos2:gpos2+csize] = grid
    img[gpos2:gpos2+csize, gpos1:gpos1+csize] = grid
    img[gpos2:gpos2+csize, gpos2:gpos2+csize] = grid

    # create right half of stimulus
    if double:
        img2 = todorovic_illusion(input_size=input_size, target_size=target_size, spacing=spacing, padding=padding,
                                  back=grid, grid=back, target=target, double=False)
        return np.hstack([img, img2])
    else:
        return img


def domijan2015():
    return todorovic_illusion(input_size=100, target_size=40, spacing=5, padding=15, back=1., grid=9., target=5., double=True)


def lynn_domijan2015():
    """
    sizes of the squares and distancing between them needs to be adjusted
    """
    lum_white = 9.
    lum_black = 1.
    lum_gray = 5.

    input_image = lum_white * np.ones([100, 200])
    input_image[:, 0:100] = lum_black
    input_image[29:70, 29:70] = lum_gray
    input_image[29:70, 129:170] = lum_gray

    input_image[14:45, 14:45] = lum_white
    input_image[14:45, 54:85] = lum_white
    input_image[54:85, 14:45] = lum_white
    input_image[54:85, 54:85] = lum_white

    input_image[14:45, 114:145] = lum_black
    input_image[14:45, 154:185] = lum_black
    input_image[54:85, 114:145] = lum_black
    input_image[54:85, 154:185] = lum_black

    return input_image



