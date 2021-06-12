import numpy as np
import math

def todorovic_illusion(target_padding=(60,60,60,60), covers_size=(30,30), spacing=5, padding=(15,15,15,15), back=0., grid=1., target=.5, double=True):
    """
    Todorovic's illusion

    Parameters
    ----------
    target_padding: tuple specifying distance  of the target edge from (top, bottom, left,right) edge of the image
    squares_size: tuple specifying (height, width) of the four squares covering the target in px
    spacing: spacing between grid cells (i.e target cross bar thickness) in px
    padding: 4-valued tuple specifying padding (top, bottom, left, right) in px
    back: value for background
    grid: value for grid cells
    target: value for target
    double: whether to return the full illusion with two grids side-by-side (inverting back and grid values)

    Returns
    -------

    """

    padding_top, padding_bottom, padding_left, padding_right = padding
    covers_height, covers_width = covers_size
    target_top, target_bottom, target_left, target_right = target_padding

    width = padding_left + covers_width*2 + spacing + padding_right
    height = padding_top + covers_height*2 + spacing + padding_bottom

    img = np.ones((height, width)) * back

    # put target square on image

    img[target_top:-target_bottom, target_left:-target_right] = target


    img[padding_top:padding_top+covers_height, padding_left:padding_left+covers_width] = grid # top left
    img[padding_top:padding_top+covers_height, padding_left+covers_width+spacing:-padding_right] = grid # top right
    img[padding_top+covers_height+spacing:-padding_bottom, padding_left:padding_left+covers_width] = grid # bottom left
    img[padding_top+covers_height+spacing:-padding_bottom, padding_left+covers_width+spacing:-padding_right] = grid # bottom right


    # create right half of stimulus
    if double:
        img2 = todorovic_illusion(target_padding=target_padding, covers_size=covers_size, spacing=spacing, padding=padding,
                                  back=grid, grid=back, target=target, double=False)
        return np.hstack([img, img2])
    else:
        return img


def domijan2015():
    return todorovic_illusion(target_padding=(29,30,29,30), covers_size=(31,31), spacing=9, padding=(14,15,14,15), back=1., grid=9., target=5., double=True)







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

