import numpy as np
from stimuli.utils import degrees_to_pixels, resolution


__all__ = [
    "hermann_grid",
]

def hermann_grid(
    visual_size=None,
    ppd=None,
    shape=None,
    element_size=None,
    intensity_background=0.0,
    intensity_grid=1.0,
):
    """
    Hermann grid

    Parameters
    ----------
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of grating, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of grating, in pixels
    element_size : (float, float, float)
        height, width and thickness of individual elements in degree visual angle
    intensity_background : float
        value of background
    intensity_grid : float
        value of grid

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        empty mask (key: "target_mask"),
        and additional keys containing stimulus parameters
    
    References
    ----------
    Hermann L (1870). Eine Erscheinung simultanen Contrastes". Pflügers Archiv
        fuer die gesamte Physiologie. 3: 13–15. https://doi.org/10.1007/BF01855743
    """
    # Resolve resolution
    shape, visual_size, ppd = resolution.resolve(shape=shape, visual_size=visual_size, ppd=ppd)    
    if len(np.unique(ppd)) > 1:
        raise ValueError("ppd should be equal in x and y direction")

    element_height, element_width, element_thick = degrees_to_pixels(element_size, np.unique(ppd))

    if element_height <= element_thick:
        raise ValueError("Element thickness larger than height")
    if element_width <= element_thick:
        raise ValueError("Element thickness larger than width")
    if element_thick <= 0:
        raise ValueError("Increase element thickness")

    img = np.ones(shape) * intensity_background
    for i in range(element_thick):
        img[i::element_height, :] = intensity_grid
        img[:, i::element_width] = intensity_grid

    stim = {
        "img": img,
        "target_mask": np.zeros(shape).astype(int),  # TODO: add mask
        "visual_size": visual_size,
        "ppd": ppd,
        "shape": shape,
        "element_size": element_size,
        "intensity_background": intensity_background,
        "intensity_grid": intensity_grid,
    }
    return stim


if __name__ == "__main__":
    from stimuli.utils import plot_stim

    stim = hermann_grid(visual_size=10, ppd=10, element_size=(1.5, 1.5, 0.2))
    plot_stim(stim, stim_name="Hermann Grid", mask=True, save=None)
