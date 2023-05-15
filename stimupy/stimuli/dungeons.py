import numpy as np

from stimupy.utils import pad_to_shape, resolution

__all__ = [
    "dungeon",
]


def dungeon(
    visual_size=None,
    ppd=None,
    shape=None,
    cell_size=None,
    n_cells=None,
    target_radius=1,
    intensity_background=0.0,
    intensity_grid=1.0,
    intensity_target=0.5,
):
    """Dungeon stimulus (Bressan, 2001) with diamond target.

    Parameters
    ----------
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of grating, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of grating, in pixels
    cell_size : Sequence[Number, Number], Number, or None (default)
        size of individual cell (height, width)
    n_cells : Sequence[Number, Number], Number, or None (default)
        the number of square cells (not counting background) per dimension
    target_radius : int
        the "Manhattan radius" of the diamond target in # cells
    intensity_background : float
        intensity value for background
    intensity_grid : float
        intensity value for grid cells
    intensity_target : float
        intensity value for target

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for each target (key: "target_mask"),
        and additional keys containing stimulus parameters

    References
    ----------
    Bressan, P. (2001).
        Explaining lightness illusions.
        Perception, 30(9), 1031-1046.
        https://doi.org/10.1068/p3109
    Domijan, D. (2015).
        A neurocomputational account
        of the role of contour facilitation in brightness perception.
        Frontiers in Human Neuroscience, 9, 93.
        https://doi.org/10.3389/fnhum.2015.00093
    """

    if isinstance(visual_size, (float, int)) or (visual_size is None):
        visual_size = (visual_size, visual_size)
    if isinstance(cell_size, (float, int)) or (cell_size is None):
        cell_size = (cell_size, cell_size)
    if isinstance(n_cells, (float, int)) or (n_cells is None):
        n_cells = (n_cells, n_cells)

    params = resolve_dungeon_params(None, visual_size, ppd, n_cells, cell_size)
    n_cells = (int(params["n_cells"][0]), int(params["n_cells"][1]))

    height, width = params["shape"].height, params["shape"].width
    cheight = height / (n_cells[0] * 2 - 1)
    cwidth = width / (n_cells[1] * 2 - 1)

    # create 2D array of grid
    arr = np.ones((n_cells[0] * 2 - 1, n_cells[1] * 2 - 1)) * intensity_grid
    mask_arr = np.zeros((n_cells[0] * 2 - 1, n_cells[1] * 2 - 1))

    # compute Manhattan distances from image center (=radius) of each pixel
    y = np.arange(-n_cells[0] + 1, n_cells[0])
    x = np.arange(-n_cells[1] + 1, n_cells[1])
    radii = np.abs(x[np.newaxis]) + np.abs(y[:, np.newaxis])

    # add targets
    idx = radii <= (target_radius * 2)
    arr[idx] = intensity_target
    mask_arr[idx] = 1

    # compute and apply grid mask
    grid_mask = [
        [(False if i % 2 == 0 and j % 2 == 0 else True) for i in range(n_cells[1] * 2 - 1)]
        for j in range(n_cells[0] * 2 - 1)
    ]
    grid_mask = np.array(grid_mask)
    arr[grid_mask] = intensity_background
    mask_arr[grid_mask] = 0

    img = arr.repeat(cheight, axis=0).repeat(cwidth, axis=1)
    mask = mask_arr.repeat(cheight, axis=0).repeat(cwidth, axis=1)

    # Make sure that stimulus size is as requested
    if (img.shape[0] != height) or (img.shape[1] != width):
        img = pad_to_shape(img, (height, width), intensity_background)
        mask = pad_to_shape(mask, (height, width), 0)

    stim = {
        "img": img,
        "target_mask": mask.astype(int),
        "target_radius": target_radius,
        "intensity_background": intensity_background,
        "intensity_grid": intensity_grid,
        "intensity_target": intensity_target,
        **params,
    }
    return stim


def resolve_dungeon_params(
    shape=None,
    visual_size=None,
    ppd=None,
    n_cells=None,
    cell_size=None,
):
    # Try to resolve resolution
    try:
        shape, visual_size, ppd = resolution.resolve(shape=shape, visual_size=visual_size, ppd=ppd)
    except resolution.TooManyUnknownsError:
        ppd = resolution.validate_ppd(ppd)
        shape = resolution.validate_shape(shape)
        visual_size = resolution.validate_visual_size(visual_size)

    n_cells1, visual_angle1, cell_size1 = resolve_cells_1d(
        visual_size[0], n_cells[0] - 0.5, cell_size[0]
    )
    n_cells2, visual_angle2, cell_size2 = resolve_cells_1d(
        visual_size[1], n_cells[1] - 0.5, cell_size[1]
    )

    # Now resolve resolution
    shape, visual_size, ppd = resolution.resolve(
        shape=shape, visual_size=(visual_angle1 / 2, visual_angle2 / 2), ppd=ppd
    )

    return {
        "visual_size": visual_size,
        "ppd": ppd,
        "shape": shape,
        "n_cells": (n_cells1 + 0.5, n_cells2 + 0.5),
        "cell_size": (cell_size1 / 2, cell_size2 / 2),
    }


def resolve_cells_1d(
    visual_angle=None,
    n_cells=None,
    cell_size=None,
):
    # Try to resolve number and size of cells
    if cell_size is not None:
        cells_pd = 1 / cell_size / 2
    else:
        cells_pd = None

    try:
        n_cells, visual_angle, cells_pd = resolution.resolve_1D(
            length=n_cells, visual_angle=visual_angle, ppd=cells_pd
        )
        visual_angle = visual_angle * 2
        cell_size = 1 / cells_pd
    except Exception as e:
        raise Exception("Could not resolve n_cells, cell_size") from e

    return n_cells, visual_angle, cell_size


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
        "dungeon": dungeon(**default_params, n_cells=5)
    }
    # fmt: on

    return stimuli


if __name__ == "__main__":
    from stimupy.utils import plot_stimuli

    stims = overview()
    plot_stimuli(stims, mask=False, save=None)
