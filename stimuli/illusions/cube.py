import numpy as np


def cube_illusion(n_cells=4, target_length=1, cell_long=15, cell_short=10, corner_cell_width=15, corner_cell_height=10, cell_spacing=3, padding=(5,5,5,5), occlusion_overlap=(4,4,4,4), back=0., grid=1., target=.5, double=True):
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
    # array representing grid cells
    arr = np.ones((n_cells, n_cells)) * grid

    padding_top, padding_bottom, padding_left, padding_right = padding

    # add target pattern (floor and ceil leads to asymmetry in case of odd target size)
    target_offset = (n_cells-target_length)/2
    offs_c = int(np.ceil(target_offset))
    offs_f = int(np.floor(target_offset))
    arr[0, offs_c:offs_c+target_length] = target
    arr[-1, offs_f:offs_f+target_length] = target
    arr[offs_f:offs_f+target_length, 0] = target
    arr[offs_c:offs_c+target_length, -1] = target

    # final image array
    width = (n_cells-2)*cell_long + 2*corner_cell_width + (n_cells-1)*cell_spacing + padding_left + padding_right
    height = (n_cells-2)*cell_long + 2*corner_cell_height + (n_cells-1)*cell_spacing + padding_top + padding_bottom

    img = np.ones((height, width)) * back

    for i, val in np.ndenumerate(arr):
        if i[0] in range(1, n_cells-1) and i[1] in range(1, n_cells-1):
            continue  # skip centre cells for efficiency
        elif i == (0,0):  # top left corner cell
            x, y = padding_left, padding_top
            img[y:y+corner_cell_height, x:x+corner_cell_width] = val
        elif i == (0, n_cells-1): # top right corner cell
            x = padding_left + corner_cell_width + cell_spacing + (n_cells-2)*(cell_long + cell_spacing)
            y = padding_top
            img[y:y+corner_cell_height, x:x+corner_cell_width] = val
        elif i == (n_cells-1, 0): # bottom left corner cell
            x = padding_left
            y = padding_top + corner_cell_height + cell_spacing + (n_cells-2)*(cell_long + cell_spacing)
            img[y:y+corner_cell_height, x:x+corner_cell_width] = val
        elif i == (n_cells - 1, n_cells-1):  # bottom right corner cell
            x = padding_left + corner_cell_width + cell_spacing + (n_cells - 2)*(cell_long + cell_spacing)
            y = padding_top + corner_cell_height + cell_spacing + (n_cells - 2)*(cell_long + cell_spacing)
            img[y:y + corner_cell_height, x:x + corner_cell_width] = val
        else:
            if i[0] == 0 or i[0] == n_cells -1: # top/bottom side
                x = padding_left + corner_cell_width + cell_spacing + (i[1] - 1) * (cell_long + cell_spacing)
                if i[0] == 0: # top side
                    y = padding_top
                else: # bottom side
                    y = - padding_bottom - cell_short

                img[y:y + cell_short, x:x + cell_long] = val

            else: # left/right side
                y = padding_top + corner_cell_width + cell_spacing + (i[0] - 1) * (cell_long + cell_spacing)

                if i[1] == 0: # left side
                    x = padding_left

                else: # right side
                    x = -padding_right - cell_short

                img[y:y + cell_long, x:x + cell_short] = val


    # add occlusion
    occlusion_top, occlusion_bottom, occlusion_left, occlusion_right = occlusion_overlap

    occ_inset_x_left = padding_left + corner_cell_width - occlusion_left
    occ_inset_x_right = width - padding_right - corner_cell_width + occlusion_right

    occ_inset_y_top = padding_top + corner_cell_height - occlusion_top
    occ_inset_y_bottom = height - padding_bottom - corner_cell_height + occlusion_bottom

    img[occ_inset_y_top:occ_inset_y_bottom, occ_inset_x_left:occ_inset_x_right] = back

    if double:
        img2 = cube_illusion(n_cells=n_cells, target_length=target_length, cell_long=cell_long, cell_short=cell_short, corner_cell_width=corner_cell_width, corner_cell_height=corner_cell_height,
                             cell_spacing=cell_spacing, padding=padding, occlusion_overlap=occlusion_overlap, back=grid, grid=back, target=target, double=False)
        return np.hstack([img, img2])
    else:
        return img


def domijan2015():
    return cube_illusion(n_cells=4, target_length=1, cell_long=15, cell_short=11, corner_cell_width=18, corner_cell_height=18, cell_spacing=5, padding=(9,10,9,10),
                         occlusion_overlap=(7,7,7,7), back=1., grid=9., target=5., double=True)
