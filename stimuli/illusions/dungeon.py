import numpy as np

def dungeon_illusion(n_cells=5, target_radius=1, cell_size=10, back=0., grid=1., target=0.5, double=True):
    """
    Dungeon illusion (Bressan, 2001) with diamond target.

    Parameters
    ----------
    n_cells: the number of square cells (not counting background) per dimension
    target_radius: the "Manhattan radius" of the diamond target in # cells
    cell_size: size per cell in px
    back: value for background
    grid: value for grid cells
    target: value for target
    double: whether to return the full illusion with two grids side-by-side (inverting back and grid values)

    Returns
    -------
    2D numpy array
    """
    # create 2D array of grid
    arr = np.ones((n_cells * 2 + 1, n_cells * 2 + 1)) * grid

    # compute Manhattan distances from image center (=radius) of each pixel
    x = np.arange(-n_cells, n_cells + 1)
    radii = np.abs(x[np.newaxis]) + np.abs(x[:, np.newaxis])

    # add targets
    idx = radii <= (target_radius * 2)
    arr[idx] = target

    # compute and apply grid mask
    mask = [[(False if i % 2 == 1 and j % 2 == 1 else True) for i in range(n_cells * 2 + 1)] for j in
            range(n_cells * 2 + 1)]
    mask = np.array(mask)
    arr[mask] = back

    img = np.repeat(np.repeat(arr, cell_size, axis=0), cell_size, axis=1)

    if double:
        img2 = dungeon_illusion(n_cells, target_radius, cell_size, back=grid, grid=back, target=target, double=False)
        return np.hstack([img, img2])
    else:
        return img