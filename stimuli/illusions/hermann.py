import numpy as np


###################################
#           Hermann Grid          #
###################################
def hermann_grid(n_grid=1000, space=100):
    #TODO: the parameters aren't analogous to the other stimuli
    #TODO: figure out the default parameters that results in something that makes sense

    grid = np.zeros([n_grid, n_grid], dtype=np.float32)
    grid[::space, :] = 1
    grid[:, ::space] = 1
    return grid


if __name__ == '__main__':
    import matplotlib.pyplot as plt
    plt.imshow(hermann_grid(), cmap='gray')
    plt.show()