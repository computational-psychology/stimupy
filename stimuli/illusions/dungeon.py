import numpy as np
from stimuli.utils import degrees_to_pixels, pad_img


def dungeon_illusion(ppd=10, n_cells=5, target_radius=1, cell_size=1.0, padding=(1.0,1.0,1.0,1.0), back=0., grid=1., target=0.5, double=True):
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
    cell_size_px = degrees_to_pixels(cell_size, ppd)

    # create 2D array of grid
    arr = np.ones((n_cells * 2 - 1, n_cells * 2 - 1)) * grid
    mask_arr = np.zeros((n_cells * 2 - 1, n_cells * 2 - 1))

    # compute Manhattan distances from image center (=radius) of each pixel
    x = np.arange(-n_cells+1, n_cells)
    radii = np.abs(x[np.newaxis]) + np.abs(x[:, np.newaxis])

    # add targets
    idx = radii <= (target_radius * 2)
    arr[idx] = target
    mask_arr[idx] = True

    # compute and apply grid mask
    grid_mask = [[(False if i % 2 == 0 and j % 2 == 0 else True) for i in range(n_cells * 2 - 1)] for j in
            range(n_cells * 2 - 1)]
    grid_mask = np.array(grid_mask)
    arr[grid_mask] = back
    mask_arr[grid_mask] = False

    img = np.repeat(np.repeat(arr, cell_size_px, axis=0), cell_size_px, axis=1)
    img = pad_img(img, padding, ppd, back)

    mask = np.repeat(np.repeat(mask_arr, cell_size_px, axis=0), cell_size_px, axis=1)
    mask = pad_img(mask, padding, ppd, False)

    if double:
        img2, mask2 = dungeon_illusion(ppd=ppd, n_cells=n_cells, target_radius=target_radius, cell_size=cell_size, padding=padding,  back=grid, grid=back, target=target, double=False)
        return (np.hstack([img, img2]), np.hstack([mask, mask2]))
    else:
        return (img, mask)

def domijan2015():
    return dungeon_illusion(ppd=10, n_cells=5, target_radius=1,cell_size=1.0, padding=(.9,1.1,.9,1.1), back=1.0, grid=9.0, target=5.0, double=True)


if __name__ == '__main__':
    import matplotlib.pyplot as plt
    img, mask = dungeon_illusion()
    plt.imshow(img, cmap='gray')
    plt.show()
