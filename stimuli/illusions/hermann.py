import numpy as np

###################################
#           Hermann Grid          #
###################################
def hermann_grid(n_grid, space):
    grid = np.zeros([n_grid, n_grid], dtype=np.float32)
    grid[::space, :] = 1
    grid[:, ::space] = 1
    return grid