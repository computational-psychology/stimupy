import numpy as np
from stimuli.utils import degrees_to_pixels, pad_img, plot_stim
from stimuli.Stimulus import Stimulus


def cube_illusion(ppd=10, n_cells=5, target_length=2, cell_long=1.5, cell_short=1.0, corner_cell_width=1.8, corner_cell_height=1.8,
                  cell_spacing=.5, padding=(1.0,1.0,1.0,1.0), occlusion_overlap=(.7,.7,.7,.7), back=0., grid=1., target=.5, double=True):


    """
    Cube illusion (Agostini & Galmonte, 2002)

    Parameters
    ----------
    n_cells: the number of square cells (not counting background) per dimension
    target_length: length in # cells per edge of the square
    cell_long: long side of a cell in px
    cell_short: short side of a cell in px
    cell_spacing: distance between two cells in px
    padding: 4-valued tuple specifying padding (top, bottom, left, right) in px
    occlusion_overlap: 4-valued tuple specifying how many px the big central square overlaps the cells on (top, bottom, left, right
    back: value for background
    grid: value for grid cells
    target: value for target
    double: whether to return the full illusion with two grids side-by-side (inverting back and grid values)

    Returns
    -------
    2D numpy array
    """
    cell_long_px, cell_short_px = degrees_to_pixels(cell_long, ppd), degrees_to_pixels(cell_short, ppd)
    corner_cell_width_px, corner_cell_height_px = degrees_to_pixels(corner_cell_width, ppd), degrees_to_pixels(corner_cell_height, ppd)
    cell_spacing_px = degrees_to_pixels(cell_spacing, ppd)
    # array representing grid cells
    arr = np.ones((n_cells, n_cells)) * grid

    # add target pattern (floor and ceil leads to asymmetry in case of odd target size)
    target_offset = (n_cells-target_length)/2
    offs_c = int(np.ceil(target_offset))
    offs_f = int(np.floor(target_offset))
    arr[0, offs_c:offs_c+target_length] = target
    arr[-1, offs_f:offs_f+target_length] = target
    arr[offs_f:offs_f+target_length, 0] = target
    arr[offs_c:offs_c+target_length, -1] = target
    

    # final image array
    width_px = (n_cells-2)*cell_long_px + 2*corner_cell_width_px + (n_cells-1)*cell_spacing_px
    height_px = (n_cells-2)*cell_long_px + 2*corner_cell_height_px + (n_cells-1)*cell_spacing_px

    img = np.ones((height_px, width_px)) * back
    mask = np.zeros((height_px, width_px))
    mask_counter = 0

    for i, val in np.ndenumerate(arr):
        target_cell = val==target
        if target_cell:
            mask_counter += 1
        if i[0] in range(1, n_cells-1) and i[1] in range(1, n_cells-1):
            continue  # skip centre cells for efficiency
        elif i == (0,0):  # top left corner cell
            img[:corner_cell_height_px, :corner_cell_width_px] = val
            if target_cell:
                mask[:corner_cell_height_px, :corner_cell_width_px] = mask_counter

        elif i == (0, n_cells-1): # top right corner cell
            img[:corner_cell_height_px, -corner_cell_width_px:] = val
            if target_cell:
                mask[:corner_cell_height_px, -corner_cell_width_px:] = mask_counter

        elif i == (n_cells-1, 0): # bottom left corner cell
            img[-corner_cell_height_px:, :corner_cell_width_px] = val
            if target_cell:
                mask[-corner_cell_height_px:, :corner_cell_width_px] = mask_counter

        elif i == (n_cells - 1, n_cells-1):  # bottom right corner cell
            img[-corner_cell_height_px:, -corner_cell_width_px:] = val
            if target_cell:
                mask[-corner_cell_height_px:, -corner_cell_width_px:] = mask_counter

        else:
            if i[0] == 0 or i[0] == n_cells -1: # top/bottom side
                x = corner_cell_width_px + cell_spacing_px + (i[1] - 1) * (cell_long_px + cell_spacing_px)
                if i[0] == 0: # top side
                    img[:cell_short_px, x:x + cell_long_px] = val
                    if target_cell:
                        mask[:cell_short_px, x:x + cell_long_px] = mask_counter
                else: # bottom side
                    img[-cell_short_px:, x:x + cell_long_px] = val
                    if target_cell:
                        mask[-cell_short_px:, x:x + cell_long_px] = mask_counter

            else: # left/right side
                y = corner_cell_width_px + cell_spacing_px + (i[0] - 1) * (cell_long_px + cell_spacing_px)

                if i[1] == 0: # left side
                    img[y:y + cell_long_px, :cell_short_px] = val
                    if target_cell:
                        mask[y:y + cell_long_px, :cell_short_px] = mask_counter

                else: # right side
                    img[y:y + cell_long_px, -cell_short_px:] = val
                    if target_cell:
                        mask[y:y + cell_long_px, -cell_short_px:] = mask_counter



    # add occlusion
    occlusion_overlap_px = degrees_to_pixels(occlusion_overlap, ppd)
    occlusion_top, occlusion_bottom, occlusion_left, occlusion_right = occlusion_overlap_px

    occ_inset_x_left = corner_cell_width_px - occlusion_left
    occ_inset_x_right = width_px - corner_cell_width_px + occlusion_right

    occ_inset_y_top = corner_cell_height_px - occlusion_top
    occ_inset_y_bottom = height_px - corner_cell_height_px + occlusion_bottom

    img[occ_inset_y_top:occ_inset_y_bottom, occ_inset_x_left:occ_inset_x_right] = back
    mask[occ_inset_y_top:occ_inset_y_bottom, occ_inset_x_left:occ_inset_x_right] = False

    img = pad_img(img, padding, ppd, back)
    mask = pad_img(mask, padding, ppd, 0)

    if double:
        stim2 = cube_illusion(ppd=ppd, n_cells=n_cells, target_length=target_length, cell_long=cell_long, cell_short=cell_short, corner_cell_width=corner_cell_width, corner_cell_height=corner_cell_height,
                             cell_spacing=cell_spacing, padding=padding, occlusion_overlap=occlusion_overlap, back=grid, grid=back, target=target, double=False)
        img = np.hstack([img, stim2.img])
        mask = np.hstack([mask, stim2.target_mask])

    stim = Stimulus()
    stim.img = img
    stim.target_mask = mask

    return stim


def domijan2015():
    return cube_illusion(ppd=10, n_cells=4, target_length=1, cell_long=1.5, cell_short=1.1, corner_cell_width=1.8, corner_cell_height=1.8, cell_spacing=.5, padding=(.9,1.0,.9,1.0),
                         occlusion_overlap=(.7,.7,.7,.7), back=1., grid=9., target=5., double=True)

if __name__ == '__main__':
    import matplotlib.pyplot as plt
    stim = cube_illusion()
    plot_stim(stim, mask=True)