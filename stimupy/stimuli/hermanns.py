import numpy as np

from stimupy.utils import resolution

__all__ = [
    "grid",
]


def grid(
    visual_size=None,
    ppd=None,
    shape=None,
    element_size=None,
    intensity_background=0.0,
    intensity_grid=1.0,
):
    """Hermann's (1870) grid

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
    Hermann L (1870).
        Eine Erscheinung simultanen Contrastes".
        Pflügers Archiv für die gesamte Physiologie. 3: 13-15.
        https://doi.org/10.1007/BF01855743
    """
    if element_size is None:
        raise ValueError("grid() missing argument 'element_size' which is not 'None'")

    # Resolve resolution
    shape, visual_size, ppd = resolution.resolve(shape=shape, visual_size=visual_size, ppd=ppd)
    if len(np.unique(ppd)) > 1:
        raise ValueError("ppd should be equal in x and y direction")

    eheight, ewidth, ethick = resolution.lengths_from_visual_angles_ppd(
        element_size, np.unique(ppd)
    )

    if eheight <= ethick:
        raise ValueError("Element thickness larger than height")
    if ewidth <= ethick:
        raise ValueError("Element thickness larger than width")
    if ethick <= 0:
        raise ValueError("Increase element thickness")

    img = np.ones(shape) * intensity_background
    for i in range(ethick):
        img[i::eheight, :] = intensity_grid
        img[:, i::ewidth] = intensity_grid

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


def overview(**kwargs):
    """Generate example stimuli from this module

    Returns
    -------
    stims : dict
        dict with all stimuli containing individual stimulus dicts.
    """
    default_params = {
        "visual_size": 10,
        "ppd": 30,
    }
    default_params.update(kwargs)

    # fmt: off
    stimuli = {
        "hermann_grid": grid(**default_params, element_size=(1.5, 1.5, 0.2))
    }
    # fmt: on

    return stimuli


if __name__ == "__main__":
    from stimupy.utils import plot_stimuli

    stims = overview()
    plot_stimuli(stims, mask=False, save=None)
