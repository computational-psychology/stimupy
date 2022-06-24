import numpy as np
from stimuli.utils import degrees_to_pixels


def dungeon_illusion(
    ppd=10,
    n_cells=5,
    target_radius=1,
    cell_size=1.0,
    back=0.0,
    grid=1.0,
    target=0.5,
):
    """
    Dungeon illusion (Bressan, 2001) with diamond target.

    Parameters
    ----------
    ppd : int
        pixels per degree (visual angle)
    n_cells : int
        the number of square cells (not counting background) per dimension
    target_radius : int
        the "Manhattan radius" of the diamond target in # cells
    cell_size : float
        size per cell in degrees visual angle
    back : float
        value for background
    grid : float
        value for grid cells
    target : float
        value for target

    Returns
    -------
    A stimulus object
    """
    cell_size_px = degrees_to_pixels(cell_size, ppd)

    # create 2D array of grid
    arr = np.ones((n_cells * 2 - 1, n_cells * 2 - 1)) * grid
    mask_arr = np.zeros((n_cells * 2 - 1, n_cells * 2 - 1))

    # compute Manhattan distances from image center (=radius) of each pixel
    x = np.arange(-n_cells + 1, n_cells)
    radii = np.abs(x[np.newaxis]) + np.abs(x[:, np.newaxis])

    # add targets
    idx = radii <= (target_radius * 2)
    arr[idx] = target
    mask_arr[idx] = 1

    # compute and apply grid mask
    grid_mask = [
        [
            (False if i % 2 == 0 and j % 2 == 0 else True)
            for i in range(n_cells * 2 - 1)
        ]
        for j in range(n_cells * 2 - 1)
    ]
    grid_mask = np.array(grid_mask)
    arr[grid_mask] = back
    mask_arr[grid_mask] = 0

    # This is used to number each target square individually instead of giving them all an index of 1
    # ind1, ind2 = np.nonzero(mask_arr)
    # for i in range(len(ind1)):
    #     mask_arr[ind1[i], ind2[i]] = i+1

    img = np.repeat(np.repeat(arr, cell_size_px, axis=0), cell_size_px, axis=1)

    mask = np.repeat(
        np.repeat(mask_arr, cell_size_px, axis=0), cell_size_px, axis=1
    )

    return {"img": img, "mask": mask}


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    from stimuli.utils import plot_stim

    stim = dungeon_illusion()
    plot_stim(stim, stim_name="Dungeon illusion")
    plt.show()
