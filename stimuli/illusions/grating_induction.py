import numpy as np
from scipy.ndimage.filters import gaussian_filter


###################################
#        Grating induction        #
###################################
def grating_induction(n_grid, width_target, blur):
    # Inputs:
    #   - n_grid: number of black and white stripes (int, unit: pixels)
    #   - width_target: width of the target (float, unit: pixels)
    #   - blur: amount of blur added (float)

    # Create grid
    grid = np.zeros([n_grid, n_grid], dtype=np.float32)
    grid[:, ::2] = 1
    grid[:, 1::2] = 0

    # Increase the resolution of the grid for blurring it later:
    res_factor = 50
    grid = np.repeat(grid, res_factor, axis=0)
    grid = np.repeat(grid, res_factor, axis=1)
    grid = gaussian_filter(grid, blur)

    # Place target on blurred grid
    n_grid = n_grid*res_factor
    width_target = int(width_target*res_factor)
    if width_target % 2 == 0:
        grid[int(n_grid/2-width_target/2):int(n_grid/2+width_target/2), :] = 0.5
    else:
        grid[int(n_grid/2-width_target/2-1):int(n_grid/2+width_target/2), :] = 0.5
    return grid
