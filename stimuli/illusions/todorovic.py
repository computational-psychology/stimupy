import matplotlib.pyplot as plt
import numpy as np
import math

from stimuli.utils import degrees_to_pixels, pad_img, plot_stim
from stimuli.Stimulus import Stimulus


def todorovic_illusion(target_shape=(4,4), ppd=10, covers_shape=(2.5, 2.5), spacing=(1.5,1.5,1.5,1.5), inner_padding=(3,3,3,3), padding=(2,2,2,2), back=0., grid=1., target=.5, double=True):
    """
    Todorovic's illusion

    Parameters
    ----------
    target_padding: tuple specifying distance  of the target edge from (top, bottom, left,right) edge of the stimulus
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
    target_height, target_width = target_shape
    target_height_px, target_width_px = degrees_to_pixels(target_shape, ppd)

    img = np.ones((target_height_px, target_width_px)) * target
    img = pad_img(img, inner_padding, ppd, back)

    mask = np.ones((target_height_px, target_width_px))
    mask = pad_img(mask, inner_padding, ppd, 0)

    inner_padding_px = degrees_to_pixels(inner_padding, ppd)
    inner_padding_top_px, inner_padding_bottom_px, inner_padding_left_px, inner_padding_right_px = inner_padding_px

    width_px = inner_padding_left_px + target_width_px + inner_padding_right_px
    height_px = inner_padding_top_px + target_height_px + inner_padding_bottom_px

    cover_height_px, cover_width_px = degrees_to_pixels(covers_shape, ppd)
    spacing_px = degrees_to_pixels(spacing, ppd)
    spacing_top_px, spacing_bottom_px, spacing_left_px, spacing_right_px = spacing_px

    target_top_left_x = (width_px-target_width_px)//2
    target_top_left_y = (height_px-target_height_px)//2

    # top left square
    cover_start_x = target_top_left_x - spacing_top_px
    cover_start_y = target_top_left_y - spacing_left_px
    img[cover_start_y:cover_start_y+cover_height_px, cover_start_x:cover_start_x+cover_width_px] = grid
    mask[cover_start_y:cover_start_y+cover_height_px, cover_start_x:cover_start_x+cover_width_px] = 0

    # top right square
    cover_end_x = target_top_left_x + target_width_px + spacing_top_px
    cover_start_y = target_top_left_y - spacing_right_px
    img[cover_start_y:cover_start_y+cover_height_px, cover_end_x-cover_width_px:cover_end_x] = grid
    mask[cover_start_y:cover_start_y+cover_height_px, cover_end_x-cover_width_px:cover_end_x] = 0

    # bottom left square
    cover_start_x = target_top_left_x - spacing_bottom_px
    cover_end_y = target_top_left_y + target_height_px + spacing_left_px
    img[cover_end_y-cover_height_px:cover_end_y, cover_start_x:cover_start_x + cover_width_px] = grid
    mask[cover_end_y-cover_height_px:cover_end_y, cover_start_x:cover_start_x + cover_width_px] = 0

    # bottom right square
    cover_end_x = target_top_left_x + target_width_px + spacing_bottom_px
    cover_end_y = target_top_left_y + target_height_px + spacing_right_px
    img[cover_end_y-cover_height_px:cover_end_y, cover_end_x-cover_width_px:cover_end_x] = grid
    mask[cover_end_y-cover_height_px:cover_end_y, cover_end_x-cover_width_px:cover_end_x] = 0

    # create right half of stimulus
    if double:
        stim2 = todorovic_illusion(target_shape=target_shape, ppd=ppd, covers_shape=covers_shape, spacing=spacing,
                                  padding=(0,0,0,0), inner_padding=inner_padding, back=grid, grid=back, target=target, double=False)
        img = np.hstack([img, stim2.img])
        mask = np.hstack([mask, stim2.target_mask])

    img = pad_img(img, padding, ppd, target)
    mask = pad_img(mask, padding, ppd, 0)

    stim = Stimulus()
    stim.img = img
    stim.target_mask = mask

    return stim

def domijan2015():
    return todorovic_illusion(target_shape=(4.1, 4.1), ppd=10, covers_shape=(3.1, 3.1), spacing=(1.5, 1.5, 1.5, 1.5), inner_padding=(2.9,3.0, 2.9,3.0 ),
                              padding=(0,0,0,0), grid=9., back=1., target=5.)

def RHS2007_todorovic_equal():
    total_height, total_width, ppd = (32,)*3
    height, width = 12, 15
    target_height, target_width = 8, 8

    inner_padding_vertical, inner_padding_horizontal = (height - target_height) / 2, (width - target_width) / 2
    inner_padding = (inner_padding_vertical, inner_padding_vertical, inner_padding_horizontal, inner_padding_horizontal)

    padding_vertical, padding_horizontal = (total_height - height) / 2, (total_width - 2 * width) / 2
    padding = (padding_vertical, padding_vertical, padding_horizontal, padding_horizontal)

    covers_shape = (0.4 * 8,) * 2
    spacing = (0,) * 4
    return todorovic_illusion(target_shape=(target_height, target_width), ppd=ppd, covers_shape=covers_shape, spacing=spacing,
                                                          inner_padding=inner_padding, padding=padding, back=1., grid=0.)

def RHS2007_todorovic_in_large():
    total_height, total_width, ppd = (32,)*3
    height, width = 12, 15
    target_height, target_width = 5.3, 5.3

    inner_padding_vertical, inner_padding_horizontal = (height - target_height) / 2, (width - target_width) / 2
    inner_padding = (inner_padding_vertical, inner_padding_vertical, inner_padding_horizontal, inner_padding_horizontal)

    padding_vertical, padding_horizontal = (total_height - height) / 2, (total_width - 2 * width) / 2
    padding = (padding_vertical, padding_vertical, padding_horizontal, padding_horizontal)

    covers_shape = (0.4 * 8,) * 2
    spacing = ((8 - 5.3) / 2,) * 4

    return todorovic_illusion(target_shape=(target_height, target_width), ppd=ppd, covers_shape=covers_shape, spacing=spacing,
                              inner_padding=inner_padding, padding=padding, back=1., grid=0.)


def RHS2007_todorovic_in_small():
    total_height, total_width, ppd = (32,)*3
    height, width = 12, 15
    target_height, target_width = 3,3

    inner_padding_vertical, inner_padding_horizontal = (height - target_height) / 2, (width - target_width) / 2
    inner_padding = (inner_padding_vertical, inner_padding_vertical, inner_padding_horizontal, inner_padding_horizontal)

    padding_vertical, padding_horizontal = (total_height - height) / 2, (total_width - 2 * width) / 2
    padding = (padding_vertical, padding_vertical, padding_horizontal, padding_horizontal)

    covers_shape = (0.4 * 8,) * 2
    spacing = ((8 - 3) / 2,) * 4
    return todorovic_illusion(target_shape=(target_height, target_width), ppd=ppd, covers_shape=covers_shape, spacing=spacing,
                              inner_padding=inner_padding, padding=padding, back=1., grid=0.)


if __name__ == '__main__':
    import matplotlib.pyplot as plt
    stim = todorovic_illusion()
    plot_stim(stim, mask=True)


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
