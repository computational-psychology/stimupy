import numpy as np

from stimupy.utils import degrees_to_pixels, resolution

__all__ = [
    "varying_cells",
    "cube",
]


def varying_cells(
    ppd,
    cell_heights,
    cell_widths,
    cell_spacing,
    targets=None,
    intensity_background=0.0,
    intensity_grid=1.0,
    intensity_target=0.5,
):
    """
    Cube stimulus (Agostini & Galmonte, 2002) with flexible cell sizes.

    Parameters
    ----------
    ppd : int
        pixels per degree (visual angle)
    cell_heights : Sequence or float
        Heights of individual cell elements in degrees. Will be used on each side.
    cell_widths : Sequence or float
        Widths of individual cell elements in degrees. Will be used on each side.
    cell_spacing : Sequence or float
        distance between individual cells iin degrees. Will be used on each side.
    targets : Sequence
        Target indices. Will be used on each side
    intensity_background : float
        intensity value for background
    intensity_grid : float
        intensity value for grid cells
    intensity_target : float
        intensity value for target

    Returns
    ----------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for each target (key: "target_mask"),
        and additional keys containing stimulus parameters

    References
    ----------
    Agostini, T., and Galmonte, A. (2002). Perceptual organization overcomes the
        effects of local surround in determining simultaneous lightness contrast.
        Psychol. Sci. 13, 89–93. https://doi.org/10.1111/1467-9280.00417
    Domijan, D. (2015). A neurocomputational account of the role of contour
        facilitation in brightness perception. Frontiers in Human Neuroscience,
        9, 93. https://doi.org/10.3389/fnhum.2015.00093
    """

    if isinstance(cell_heights, (float, int)):
        cell_heights = (cell_heights,)
    if isinstance(cell_widths, (float, int)):
        cell_widths = (cell_widths,)
    if isinstance(cell_spacing, (float, int)):
        cell_spacing = (cell_spacing,)
    if targets is None:
        targets = ()
    if isinstance(targets, (float, int)):
        targets = (targets,)

    n_cells = np.maximum(len(cell_heights), len(cell_widths))
    n_cells = np.maximum(n_cells, len(cell_spacing) + 1)

    if len(cell_heights) == 1:
        cell_heights = cell_heights * n_cells
    if len(cell_widths) == 1:
        cell_widths = cell_widths * n_cells
    if len(cell_spacing) == 1:
        cell_spacing = cell_spacing * n_cells
    cell_spacing = list(cell_spacing)
    cell_spacing[n_cells - 1] = 0

    cheights = degrees_to_pixels(cell_heights, ppd)
    cwidths = degrees_to_pixels(cell_widths, ppd)
    cspaces = degrees_to_pixels(cell_spacing, ppd)
    height = sum(cwidths) + sum(cspaces)
    width = height

    # Initiate image
    img = np.ones([height, width]) * intensity_background
    mask = np.zeros([height, width])

    # Add cells: top and bottom
    xs = 0
    for i in range(n_cells):
        if i in targets:
            fill_img = intensity_target
            fill_mask = 1
        else:
            fill_img = intensity_grid
            fill_mask = 0
        img[0 : cheights[i], xs : xs + cwidths[i]] = fill_img
        img[height - cheights[i] : :, xs : xs + cwidths[i]] = fill_img
        mask[0 : cheights[i], xs : xs + cwidths[i]] = fill_mask
        mask[height - cheights[i] : :, xs : xs + cwidths[i]] = fill_mask
        xs += cwidths[i] + cspaces[i]

    # Add cells: left and right
    xs = 0
    for i in range(n_cells):
        if i in targets:
            fill_img = intensity_target
            fill_mask = 1
        else:
            fill_img = intensity_grid
            fill_mask = 0
        img[xs : xs + cwidths[i], 0 : cheights[i]] = fill_img
        img[xs : xs + cwidths[i], width - cheights[i] : :] = fill_img
        mask[xs : xs + cwidths[i], 0 : cheights[i]] = fill_mask
        mask[xs : xs + cwidths[i], width - cheights[i] : :] = fill_mask
        xs += cwidths[i] + cspaces[i]

    stim = {
        "img": img,
        "target_mask": mask.astype(int),
        "shape": img.shape,
        "visual_size": np.array(img.shape) / ppd,
        "ppd": ppd,
        "targets": targets,
        "cell_heights": cell_heights,
        "cell_widths": cell_widths,
        "cell_spacing": cell_spacing,
        "intensity_background": intensity_background,
        "intensity_grid": intensity_grid,
        "intensity_target": intensity_target,
    }
    return stim


def cube(
    visual_size=None,
    ppd=None,
    shape=None,
    n_cells=None,
    targets=None,
    cell_thickness=None,
    cell_spacing=None,
    intensity_background=0.0,
    intensity_grid=1.0,
    intensity_target=0.5,
):

    """
    Cube illusion (Agostini & Galmonte, 2002)

    Parameters
    ----------
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of image, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of image, in pixels
    n_cells : int
        the number of square cells (not counting background) per dimension
    targets : Sequence
        Target indices. Will be used on each side
    cell_thickness : float
        Thickness of each cell in degree of visual angle
    cell_spacing : float or (float, float)
        distance between two cells in degrees visual angle
    intensity_background : float
        intensity value for background
    intensity_grid : float
        intensity value for grid cells
    intensity_target : float
        intensity value for target

    Returns
    ----------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for each target (key: "target_mask"),
        and additional keys containing stimulus parameters

    References
    ----------
    Agostini, T., and Galmonte, A. (2002). Perceptual organization overcomes the
        effects of local surround in determining simultaneous lightness contrast.
        Psychol. Sci. 13, 89–93. https://doi.org/10.1111/1467-9280.00417
    Domijan, D. (2015). A neurocomputational account of the role of contour
        facilitation in brightness perception. Frontiers in Human Neuroscience,
        9, 93. https://doi.org/10.3389/fnhum.2015.00093
    """

    # Resolve resolution
    shape, visual_size, ppd = resolution.resolve(shape=shape, visual_size=visual_size, ppd=ppd)
    if len(np.unique(ppd)) > 1:
        raise ValueError("ppd should be equal in x- and y-direction")
    if n_cells is None:
        raise ValueError("cube() missing argument 'n_cells' which is not 'None'")
    if cell_thickness is None:
        raise ValueError("cube() missing argument 'cell_thickness' which is not 'None'")
    if cell_spacing is None:
        raise ValueError("cube() missing argument 'cell_spacing' which is not 'None'")

    if isinstance(cell_spacing, (float, int)):
        cell_spacing = (cell_spacing, cell_spacing)
    if isinstance(n_cells, (float, int)):
        n_cells = (n_cells, n_cells)
    if targets is None:
        targets = ()

    height, width = shape
    cell_space = degrees_to_pixels(cell_spacing, np.unique(ppd)[0])
    cell_thick = degrees_to_pixels(cell_thickness, np.unique(ppd)[0])

    # Initiate image
    img = np.ones([height, width]) * intensity_background
    mask = np.zeros([height, width])

    # Calculate cell widths and heights
    cell_height = int((height - cell_space[0] * (n_cells[0] - 1)) / n_cells[0])
    cell_width = int((width - cell_space[1] * (n_cells[1] - 1)) / n_cells[1])

    if (cell_thick > cell_height) or (cell_thick > cell_width):
        raise ValueError("cell_thickness is too large")

    # Calculate cell placements:
    xs = np.arange(0, width - 1, cell_width + cell_space[1])
    rxs = xs[::-1]
    ys = np.arange(0, height - 1, cell_height + cell_space[0])
    rys = ys[::-1]

    # Add cells: top and bottom
    for i in range(n_cells[1]):
        if i in targets:
            fill_img = intensity_target
            fill_mask = 1
        else:
            fill_img = intensity_grid
            fill_mask = 0
        img[0:cell_thick, xs[i] : xs[i] + cell_width] = fill_img
        img[height - cell_thick : :, rxs[i] : rxs[i] + cell_width] = fill_img
        mask[0:cell_thick, xs[i] : xs[i] + cell_width] = fill_mask
        mask[height - cell_thick : :, rxs[i] : rxs[i] + cell_width] = fill_mask

    # Add cells: left and right
    for i in range(n_cells[0]):
        if i in targets:
            fill_img = intensity_target
            fill_mask = 1
        else:
            fill_img = intensity_grid
            fill_mask = 0
        img[rys[i] : rys[i] + cell_height, 0:cell_thick] = fill_img
        img[ys[i] : ys[i] + cell_height, height - cell_thick : :] = fill_img
        mask[rys[i] : rys[i] + cell_height, 0:cell_thick] = fill_mask
        mask[ys[i] : ys[i] + cell_height, height - cell_thick : :] = fill_mask

    stim = {
        "img": img,
        "target_mask": mask.astype(int),
        "shape": shape,
        "visual_size": visual_size,
        "ppd": ppd,
        "targets": targets,
        "n_cells": n_cells,
        "cell_thickness": cell_thickness,
        "cell_spacing": cell_spacing,
        "intensity_background": intensity_background,
        "intensity_grid": intensity_grid,
        "intensity_target": intensity_target,
    }
    return stim


if __name__ == "__main__":
    from stimupy.utils import plot_stimuli

    p1 = {
        "ppd": 10,
        "cell_heights": (1, 2, 1),
        "cell_widths": (1.5, 2, 1.5),
        "cell_spacing": 0.5,
        "targets": 1,
    }

    p2 = {
        "visual_size": 10,
        "ppd": 10,
        "n_cells": 5,
        "targets": (1, 2),
        "cell_thickness": 1,
        "cell_spacing": 0.5,
    }

    stims = {
        "varying cells": varying_cells(**p1),
        "cube": cube(**p2),
    }
    plot_stimuli(stims, mask=True, save=None)
