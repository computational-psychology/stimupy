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


# This function comes from the lightness module that has been integrated inside the illusions dir.
# TODO: Compare this function with the one above and merge into one
def todorovic_lightness(coc, vert_rep, horz_rep):

    """
    Create a checkerboard illusion by appropriately aligning COC stimuli, in
    the way demonstrated by Todorovic (1987).

    Parameters
    ----------
    coc : ndarray
          The base Craig-O'Brien-Cornsweet stimulus, created with cornsweet().
          It should have a small ramp-width compared to its size, moderate
          contrast, and be square.
    horz_rep : int
               number of horizontal repetitions of the cornsweet stimulus.
    vert_rep : int
               number of vertical repetitions.

    Returns
    -------
    stim: ndarray (2D)

    References
    ----------
    Todorovic, D. (1987). The Craik-O'Brien-Cornsweet effect: new
    varieties and their theoretical implications. Perception & psychophysics,
    42(6), 545-60, Plate 4.
    """

    stim = np.tile(np.hstack((coc, np.fliplr(coc))), (1, horz_rep / 2))
    if horz_rep % 2 != 0:
        stim = np.hstack((stim, stim[:, 0:coc.shape[1]]))
    stim = np.tile(np.vstack((stim, np.roll(stim, coc.shape[1], 1))),
                   (vert_rep / 2, 1))
    if vert_rep % 2 != 0:
        stim = np.vstack((stim, stim[0:coc.shape[0], :]))
    return stim
