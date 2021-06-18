import numpy as np
from scipy.ndimage.filters import gaussian_filter


###################################
#        Grating induction        #
###################################
def grating_illusion(n_grid, grating_shape, target_height, blur, padding=(10,10,10,10,)):
    # Inputs:
    #   - n_grid: number of black and white stripes (int, unit: pixels)
    #   - target_shape: (height, width) of the target in px
    #   - blur: amount of blur added (float)

    grating_height, grating_width = grating_shape

    # Create grid
    grid = np.zeros((1,n_grid), dtype=np.float32)
    grid[0, ::2] = 1
    grid[0, 1::2] = 0

    # Increase the resolution of the grid for blurring it later:
    grid = np.repeat(grid, grating_height, axis=0)
    grid = np.repeat(grid, grating_width, axis=1)
    grid = gaussian_filter(grid, blur)

    # Place target on blurred grid
    target_start_y = (grating_height-target_height)//2
    grid[target_start_y : target_start_y + target_height, :] = 0.5
    return grid

def RHS2007_grating_induction():
    n_grid = 8
    phase_width = 2
    res_factor = 20
    target_height, target_width = phase_width * res_factor * 6, phase_width * res_factor
    return grating_induction(n_grid=8, grating_shape=(target_height, target_width),
                                       target_height=phase_width * res_factor // 2, blur=5)
