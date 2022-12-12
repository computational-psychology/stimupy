import numpy as np
from stimuli.utils import degrees_to_pixels


__all__ = [
    "hermann_grid",
]

def hermann_grid(
    visual_size=None,
    ppd=None,
    element_size=None,
    intensity_background=0.0,
    intensity_grid=1.0,
):
    """
    Hermann grid

    Parameters
    ----------
    visual_size : (float, float)
        The shape of the stimulus in degrees of visual angle. (y,x)
    ppd : int
        pixels per degree (visual angle)
    element_size : (float, float, float)
        height, width and thickness of individual elements in degree visual angle
    intensity_background : float
        value of background
    intensity_grid : float
        value of grid

    Returns
    -------
    A stimulus dictionary with the stimulus ['img'] and target mask ['mask']
    
    References
    ----------
    Hermann L (1870). Eine Erscheinung simultanen Contrastes". Pflügers Archiv
        fuer die gesamte Physiologie. 3: 13–15. https://doi.org/10.1007/BF01855743
    """
    if isinstance(visual_size, (float, int)):
        visual_size = (visual_size, visual_size)

    grid_height, grid_width = degrees_to_pixels(visual_size, ppd)
    element_height, element_width, element_thick = degrees_to_pixels(element_size, ppd)

    if element_height <= element_thick:
        raise ValueError("Element thickness larger than height")
    if element_width <= element_thick:
        raise ValueError("Element thickness larger than width")
    if element_thick <= 0:
        raise ValueError("Increase element thickness")

    img = np.ones([grid_height, grid_width], dtype=np.float32) * intensity_background
    for i in range(element_thick):
        img[i::element_height, :] = intensity_grid
        img[:, i::element_width] = intensity_grid

    params = {
        "shape": img.shape,
        "visual_size": np.array(img.shape) / ppd,
        "ppd": ppd,
        "element_size": element_size,
        "intensity_background": intensity_background,
        "intensity_grid": intensity_grid,
    }

    return {"img": img, "mask": None, **params}  # TODO: add mask


if __name__ == "__main__":
    from stimuli.utils import plot_stim

    stim = hermann_grid(visual_size=10, ppd=10, element_size=(1.5, 1.5, 0.2))
    plot_stim(stim, stim_name="Hermann Grid", mask=True, save=None)
