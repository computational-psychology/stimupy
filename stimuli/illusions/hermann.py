import numpy as np
from stimuli.utils import plot_stim
from stimuli.Stimulus import Stimulus
from stimuli.utils import  plot_stim

###################################
#           Hermann Grid          #
###################################
def hermann_grid(n_grid=100, space=5):
    #TODO: the parameters aren't analogous to the other stimuli

    grid = np.zeros([n_grid, n_grid], dtype=np.float32)
    grid[::space, :] = 1
    grid[:, ::space] = 1

    stim = Stimulus()
    stim.img = grid
    stim.target_mask = None
    return stim


if __name__ == '__main__':
    import matplotlib.pyplot as plt
    stim = hermann_grid()
    plot_stim(stim)