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
