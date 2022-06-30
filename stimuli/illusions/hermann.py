import numpy as np
from stimuli.utils import degrees_to_pixels


def hermann_grid(
        ppd=10,
        grid_size=(10, 10),
        element_size=(1.5, 1.5, 0.2),
        vback=0.,
        vgrid=1.
        ):
    """
    Hermann grid

    Parameters
    ----------
    ppd : int
        pixels per degree (visual angle)
    grid_shape : (float, float)
        height and width of grid in degree visual angle
    element_size : (float, float, float)
        height, width and thickness of individual elements in degree visual angle
    vback : float
        value of background
    vgrid : float
        value of grid

    Returns
    -------
    A stimulus dictionary with the stimulus ['img'] and target mask ['mask']
    """

    grid_height, grid_width = degrees_to_pixels(grid_size, ppd)
    element_height, element_width, element_thick = degrees_to_pixels(element_size, ppd)

    img = np.ones([grid_height, grid_width], dtype=np.float32) * vback
    for i in range(element_thick):
        img[i::element_height, :] = vgrid
        img[:, i::element_width] = vgrid

    mask = None  # TODO add this
    return {"img": img, "mask": mask}


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    from stimuli.utils import plot_stim

    stim = hermann_grid()
    plot_stim(stim, stim_name="Hermann Grid")
    plt.show()
