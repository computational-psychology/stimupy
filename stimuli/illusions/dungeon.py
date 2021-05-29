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

def domijan2015():
    return dungeon_illusion(n_cells=5, target_radius=1,cell_size=10, back=1.0, grid=9.0, target=5.0, double=True)

def lynn_domijan2015():
    """
    there's one pixel translation between the stimuli package and utils generated inputs
    (see pixels [9,9] and [10,10] in reults from this and previous functions)
    """
    lum_white = 9.
    lum_black = 1.
    lum_gray = 5.
    input_image = lum_black * np.ones([110, 220])
    input_image[:, 110:220] = lum_white

    for i in range(9, 90, 20):
        for j in range(9, 90, 20):
            input_image[i:i + 10, j:j + 10] = lum_white
        for j in range(119, 210, 20):
            input_image[i:i + 10, j:j + 10] = lum_black

    input_image[49:59, 29:39] = lum_gray
    input_image[49:59, 49:59] = lum_gray
    input_image[49:59, 69:79] = lum_gray
    input_image[49:59, 139:149] = lum_gray
    input_image[49:59, 159:169] = lum_gray
    input_image[49:59, 179:189] = lum_gray

    input_image[29:39, 49:59] = lum_gray
    input_image[69:79, 49:59] = lum_gray
    input_image[29:39, 159:169] = lum_gray
    input_image[69:79, 159:169] = lum_gray

    return input_image
