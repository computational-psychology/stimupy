import numpy as np
from stimuli import utils

def dungeon_illusion(n_cells=5, target_radius=1, cell_size=10, padding=(10,10,10,10), back=0., grid=1., target=0.5, double=True):
    """
    Dungeon illusion (Bressan, 2001) with diamond target.

    Parameters
    ----------
    n_cells: the number of square cells (not counting background) per dimension
    target_radius: the "Manhattan radius" of the diamond target in # cells
    cell_size: size per cell in px
    padding: 4-valued tuple specifying padding (top, bottom, left, right) in px
    back: value for background
    grid: value for grid cells
    target: value for target
    double: whether to return the full illusion with two grids side-by-side (inverting back and grid values)
    shift: number of x,y pixels to shift all the squares by. Top left corner is 0,0

    Returns
    -------
    2D numpy array
    """

    padding_top, padding_bottom, padding_left, padding_right = padding

    # create 2D array of grid
    arr = np.ones((n_cells * 2 - 1, n_cells * 2 - 1)) * grid

    # compute Manhattan distances from image center (=radius) of each pixel
    x = np.arange(-n_cells+1, n_cells)
    radii = np.abs(x[np.newaxis]) + np.abs(x[:, np.newaxis])

    # add targets
    idx = radii <= (target_radius * 2)
    arr[idx] = target

    # compute and apply grid mask
    mask = [[(False if i % 2 == 0 and j % 2 == 0 else True) for i in range(n_cells * 2 - 1)] for j in
            range(n_cells * 2 - 1)]
    mask = np.array(mask)
    arr[mask] = back

    img = np.repeat(np.repeat(arr, cell_size, axis=0), cell_size, axis=1)
    img = np.pad(img, ((padding_top, padding_bottom), (padding_left, padding_right)), 'constant', constant_values=back)

    if double:
        img2 = dungeon_illusion(n_cells, target_radius, cell_size, padding=padding,  back=grid, grid=back, target=target, double=False)
        return np.hstack([img, img2])
    else:
        return img

def domijan2015():
    return dungeon_illusion(n_cells=5, target_radius=1,cell_size=10, padding=(9,11,9,11), back=1.0, grid=9.0, target=5.0, double=True)


