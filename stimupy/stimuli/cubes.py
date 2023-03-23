import numpy as np

from stimupy.utils import resolution

__all__ = [
    "varying_cells",
    "cube",
]


def varying_cells(
    ppd=None,
    cell_lengths=None,
    cell_thickness=None,
    cell_spacing=None,
    target_indices=None,
    intensity_background=0.0,
    intensity_cells=1.0,
    intensity_target=0.5,
):
    """
    Cube stimulus (Agostini & Galmonte, 2002) with flexible cell lengths.

    Parameters
    ----------
    ppd : Number or None (default)
        pixels per degree (visual angle)
    cell_lengths : Sequence[Number, ...], Number of None (default)
        lengths of individual cells in degrees
    cell_thickness : Number or None (default)
        thickness of each cell in degrees
    cell_spacing : Number or None (default)
        spacing between cells in degrees
    target_indices : Sequence or None
        target indices; will be used on each side
    intensity_background : float
        intensity value for background
    intensity_cells : float
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
    Agostini, T., and Galmonte, A. (2002).
        Perceptual organization overcomes the effects of local surround
        in determining simultaneous lightness contrast.
        Psychol. Sci. 13, 89-93.
        https://doi.org/10.1111/1467-9280.00417
    Domijan, D. (2015).
        A neurocomputational account
        of the role of contour facilitation in brightness perception.
        Frontiers in Human Neuroscience, 9, 93.
        https://doi.org/10.3389/fnhum.2015.00093
    """
    if not isinstance(ppd, (float, int)):
        ppd = np.unique(ppd)
        if len(ppd) != 1:
            raise ValueError("ppd has to be the same in x and y direction")
        else:
            ppd = ppd[0]

    if isinstance(cell_lengths, (float, int)):
        cell_lengths = (cell_lengths,)
    if target_indices is None:
        target_indices = ()
    if isinstance(target_indices, (float, int)):
        target_indices = (target_indices,)

    n_cells = len(cell_lengths)

    clengths = resolution.lengths_from_visual_angles_ppd(cell_lengths, ppd)
    cthick = resolution.lengths_from_visual_angles_ppd(cell_thickness, ppd)
    cspace = resolution.lengths_from_visual_angles_ppd(cell_spacing, ppd)
    height = (
        np.maximum(clengths[0], cthick)
        + np.maximum(clengths[-1], cthick)
        + sum(clengths[1 : n_cells - 1])
        + cspace * (n_cells - 1)
    )
    width = height

    # Initiate image
    cell_mask = np.zeros([height, width])
    target_mask = np.zeros([height, width])

    xs = 0
    counter = 1
    for i in range(n_cells):
        if i in target_indices:
            fill_mask = 1
        else:
            fill_mask = 0

        # Add cells top
        cell_mask[0:cthick, xs : xs + clengths[i]] = counter
        target_mask[0:cthick, xs : xs + clengths[i]] += fill_mask

        # Add cells bottom
        cell_mask[height - cthick : :, width - xs - clengths[i] : width - xs] = counter + 1
        target_mask[height - cthick : :, width - xs - clengths[i] : width - xs] += fill_mask

        # Add cells left
        cell_mask[height - xs - clengths[i] : height - xs, 0:cthick] = counter + 2
        target_mask[height - xs - clengths[i] : height - xs, 0:cthick] += fill_mask

        # Add cells right
        cell_mask[xs : xs + clengths[i], width - cthick : :] = counter + 3
        target_mask[xs : xs + clengths[i], width - cthick : :] += fill_mask

        if i == 0:
            xs += np.maximum(clengths[i], cthick) + cspace
        elif i == n_cells - 2:
            xs += np.maximum(clengths[-2], cthick) + cspace
        else:
            xs += clengths[i] + cspace
        counter += 4

    unique_vals = np.unique(cell_mask)
    for v in range(len(unique_vals) - 1):
        cell_mask[cell_mask == unique_vals[v + 1]] = v + 1

    img = np.where(cell_mask != 0, intensity_cells, intensity_background)
    img = np.where(target_mask != 0, intensity_target, img)
    target_mask = np.where(target_mask >= 1, 1, 0)

    stim = {
        "img": img,
        "cell_mask": cell_mask.astype(int),
        "target_mask": target_mask.astype(int),
        "shape": img.shape,
        "visual_size": np.array(img.shape) / ppd,
        "ppd": ppd,
        "target_indices": target_indices,
        "cell_lengths": cell_lengths,
        "cell_thickness": cell_thickness,
        "cell_spacing": cell_spacing,
        "intensity_background": intensity_background,
        "intensity_cells": intensity_cells,
        "intensity_target": intensity_target,
    }
    return stim


def cube(
    visual_size=None,
    ppd=None,
    shape=None,
    n_cells=None,
    target_indices=None,
    cell_thickness=None,
    cell_spacing=None,
    intensity_background=0.0,
    intensity_cells=1.0,
    intensity_target=0.5,
):
    """Cube illusion (Agostini & Galmonte, 2002)

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
    target_indices : Sequence
        Target indices. Will be used on each side
    cell_thickness : Number or None (default)
        thickness of each cell in degrees
    cell_spacing : Sequence[Number, Number], Number or None (default)
        spacing between cells in degrees (height, width)
    intensity_background : float
        intensity value for background
    intensity_cells : float
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
    Agostini, T., and Galmonte, A. (2002).
        Perceptual organization overcomes the effects of local surround
        in determining simultaneous lightness contrast.
        Psychol. Sci. 13, 89-93.
        https://doi.org/10.1111/1467-9280.00417
    Domijan, D. (2015).
        A neurocomputational account
        of the role of contour facilitation in brightness perception.
        Frontiers in Human Neuroscience, 9, 93.
        https://doi.org/10.3389/fnhum.2015.00093
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
    if target_indices is None:
        target_indices = ()
    if isinstance(target_indices, (float, int)):
        target_indices = (target_indices,)

    height, width = shape
    cell_space = resolution.lengths_from_visual_angles_ppd(cell_spacing, np.unique(ppd))
    cell_thick = resolution.lengths_from_visual_angles_ppd(cell_thickness, np.unique(ppd))

    # Initiate image
    cell_mask = np.zeros([height, width])
    target_mask = np.zeros([height, width])

    # Calculate cell widths and heights
    cell_height = int((height - cell_space[0] * (n_cells[0] - 1)) / n_cells[0])
    cell_width = int((width - cell_space[1] * (n_cells[1] - 1)) / n_cells[1])

    if (cell_thick > cell_height) or (cell_thick > cell_width):
        raise ValueError("cannot fit all cells into image")

    # Calculate cell placements:
    xs = np.arange(0, width - 1, cell_width + cell_space[1])
    rxs = xs[::-1]
    ys = np.arange(0, height - 1, cell_height + cell_space[0])
    rys = ys[::-1]

    # Add cells: top and bottom
    counter = 1
    for i in range(n_cells[1]):
        if i in target_indices:
            fill_mask = 1
        else:
            fill_mask = 0

        cell_mask[0:cell_thick, xs[i] : xs[i] + cell_width] = counter
        cell_mask[height - cell_thick : :, rxs[i] : rxs[i] + cell_width] = counter + 1
        target_mask[0:cell_thick, xs[i] : xs[i] + cell_width] += fill_mask
        target_mask[height - cell_thick : :, rxs[i] : rxs[i] + cell_width] += fill_mask
        counter += 2

    # Add cells: left and right
    for i in range(n_cells[0]):
        if i in target_indices:
            fill_mask = 1
        else:
            fill_mask = 0

        cell_mask[rys[i] : rys[i] + cell_height, 0:cell_thick] = counter
        cell_mask[ys[i] : ys[i] + cell_height, height - cell_thick : :] = counter + 1
        target_mask[rys[i] : rys[i] + cell_height, 0:cell_thick] += fill_mask
        target_mask[ys[i] : ys[i] + cell_height, height - cell_thick : :] += fill_mask
        counter += 2

    unique_vals = np.unique(cell_mask)
    for v in range(len(unique_vals) - 1):
        cell_mask[cell_mask == unique_vals[v + 1]] = v + 1

    img = np.where(cell_mask != 0, intensity_cells, intensity_background)
    img = np.where(target_mask != 0, intensity_target, img)
    target_mask = np.where(target_mask >= 1, 1, 0)

    stim = {
        "img": img,
        "cell_mask": cell_mask.astype(int),
        "target_mask": target_mask.astype(int),
        "shape": shape,
        "visual_size": visual_size,
        "ppd": ppd,
        "target_indices": target_indices,
        "n_cells": n_cells,
        "cell_thickness": cell_thickness,
        "cell_spacing": cell_spacing,
        "intensity_background": intensity_background,
        "intensity_cells": intensity_cells,
        "intensity_target": intensity_target,
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
        "ppd": 30,
        "cell_thickness": 1,
        "cell_spacing": 0.5,
    }
    default_params.update(kwargs)

    # fmt: off
    stimuli = {
        "cubes_regular": cube(**default_params, visual_size=10, n_cells=5, target_indices=(1,2)),
        "cubes_variable": varying_cells(**default_params, cell_lengths=(2,4,2), target_indices=1),
    }
    # fmt: on

    return stimuli


if __name__ == "__main__":
    from stimupy.utils import plot_stimuli

    stims = overview()
    plot_stimuli(stims, mask=False, save=None)
