import numpy as np
from stimuli.utils import degrees_to_pixels


__all__ = [
    "dungeon_illusion",
]

def dungeon_illusion(
    ppd=10,
    n_cells=5,
    target_radius=1,
    cell_size=1.0,
    intensity_background=0.0,
    intensity_grid=1.0,
    intensity_target=0.5,
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
    intensity_background : float
        intensity value for background
    intensity_grid : float
        intensity value for grid cells
    intensity_target : float
        intensity value for target

    Returns
    -------
    A stimulus dictionary with the stimulus ['img'] and target mask ['mask']
    """
    cell_size_px = degrees_to_pixels(cell_size, ppd)

    # create 2D array of grid
    arr = np.ones((n_cells * 2 - 1, n_cells * 2 - 1)) * intensity_grid
    mask_arr = np.zeros((n_cells * 2 - 1, n_cells * 2 - 1))

    # compute Manhattan distances from image center (=radius) of each pixel
    x = np.arange(-n_cells + 1, n_cells)
    radii = np.abs(x[np.newaxis]) + np.abs(x[:, np.newaxis])

    # add targets
    idx = radii <= (target_radius * 2)
    arr[idx] = intensity_target
    mask_arr[idx] = 1

    # compute and apply grid mask
    grid_mask = [
        [(False if i % 2 == 0 and j % 2 == 0 else True) for i in range(n_cells * 2 - 1)]
        for j in range(n_cells * 2 - 1)
    ]
    grid_mask = np.array(grid_mask)
    arr[grid_mask] = intensity_background
    mask_arr[grid_mask] = 0

    img = arr.repeat(cell_size_px, axis=0).repeat(cell_size_px, axis=1)
    mask = mask_arr.repeat(cell_size_px, axis=0).repeat(cell_size_px, axis=1)
    return {"img": img, "mask": mask}


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    from stimuli.utils import plot_stim

    stim = dungeon_illusion()
    plot_stim(stim, stim_name="Dungeon illusion")
    plt.show()
