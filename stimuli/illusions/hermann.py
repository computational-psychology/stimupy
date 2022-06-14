import numpy as np


###################################
#           Hermann Grid          #
###################################
def hermann_grid(n_grid=100, space=5):
    # TODO: the parameters aren't analogous to the other stimuli

    grid = np.zeros([n_grid, n_grid], dtype=np.float32)
    grid[::space, :] = 1
    grid[:, ::space] = 1

    img = grid
    mask = None  # TODO add this

    return {"img": img, "mask": mask}


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    from stimuli.utils import plot_stim

    stim = hermann_grid()
    plot_stim(stim, stim_name="Hermann Grid")
    plt.show()
