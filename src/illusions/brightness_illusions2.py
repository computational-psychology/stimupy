"""
This script contains code for creating  brightness illusions used in Domijan (2015).
See /tests/test_brightness_illusions2.py for examples.

@author: lynn & max
"""

import numpy as np


def dungeon_illusion(n_cells=5, target_radius=1, cell_size=10, back=0., grid=1., target=0.5, double=True):
    """
    Dungeon illusion (Bressan, 2001) with diamond target.

    Parameters
    ----------
    n_cells: the number of square cells (not counting background) per dimension
    target_radius: the "Manhattan radius" of the diamond target in # cells
    cell_size: size per cell in px
    back: value for background
    grid: value for grid cells
    target: value for target
    double: whether to return the full illusion with two grids side-by-side (inverting back and grid values)

    Returns
    -------
    2D numpy array
    """
    # create 2D array of grid
    arr = np.ones((n_cells * 2 + 1, n_cells * 2 + 1)) * grid

    # compute Manhattan distances from image center (=radius) of each pixel
    x = np.arange(-n_cells, n_cells + 1)
    radii = np.abs(x[np.newaxis]) + np.abs(x[:, np.newaxis])

    # add targets
    idx = radii <= (target_radius * 2)
    arr[idx] = target

    # compute and apply grid mask
    mask = [[(False if i % 2 == 1 and j % 2 == 1 else True) for i in range(n_cells * 2 + 1)] for j in
            range(n_cells * 2 + 1)]
    mask = np.array(mask)
    arr[mask] = back

    img = np.repeat(np.repeat(arr, cell_size, axis=0), cell_size, axis=1)

    if double:
        img2 = dungeon_illusion(n_cells, target_radius, cell_size, back=grid, grid=back, target=target, double=False)
        return np.hstack([img, img2])
    else:
        return img


def cube_illusion(n_cells=4, target_length=1, cell_size=10, cell_spacing=3, padding=5, occlusion_overlap=4, back=0., grid=1., target=.5, double=True):
    """
    Cube illusion (Agostini & Galmonte, 2002)

    Parameters
    ----------
    n_cells: the number of square cells (not counting background) per dimension
    target_length: length in # cells per edge of the square
    cell_size: size per cell in px
    cell_spacing: distance between two cells in px
    padding: padding for entire grid
    occlusion_overlap: how my px the big central square overlaps on every grid cell
    back: value for background
    grid: value for grid cells
    target: value for target
    double: whether to return the full illusion with two grids side-by-side (inverting back and grid values)

    Returns
    -------
    2D numpy array
    """
    # array representing grid cells
    arr = np.ones((n_cells, n_cells)) * grid

    # add target pattern (floor and ceil leads to asymmetry in case of odd target size)
    target_offset = (n_cells-target_length)/2
    offs_c = int(np.ceil(target_offset))
    offs_f = int(np.floor(target_offset))
    arr[0,offs_c:offs_c+target_length] = target
    arr[-1,offs_f:offs_f+target_length] = target
    arr[offs_f:offs_f+target_length, 0] = target
    arr[offs_c:offs_c+target_length, -1] = target

    # final image array
    size = n_cells*cell_size + (n_cells-1)*cell_spacing + 2*padding
    img = np.ones((size, size)) * back

    for i, val in np.ndenumerate(arr):
        if i[0] in range(1, n_cells-1) and i[1] in range(1, n_cells-1):
            continue # skip centre cells for efficiency
        y = i[0]*(cell_size+cell_spacing) + padding
        x = i[1]*(cell_size+cell_spacing) + padding
        img[y:y+cell_size, x:x+cell_size] = val

    # add occlusion
    occ_inset = padding + cell_size - occlusion_overlap
    img[occ_inset:-occ_inset, occ_inset:-occ_inset] = back

    if double:
        img2 = cube_illusion(n_cells, target_length, cell_size, cell_spacing, padding, occlusion_overlap, back=grid, grid=back, target=target, double=False)
        return np.hstack([img, img2])
    else:
        return img


def grating_illusion(n_bars=5, target_length=1, bar_width=10, back=0., grid=1., target=0.5, double=True):
    """
    Grating illusion

    Parameters
    ----------
    n_bars: the number of vertical bars
    target_length: # bars that make up the target
    bar_width: width of bar in px (height is determined by making the image square)
    back: value for background
    grid: value for grid cells
    target: value for target
    double: whether to return the full illusion with two grids side-by-side (inverting back and grid values)

    Returns
    -------
    2D numpy array
    """
    # create array of grating
    arr = np.ones(n_bars) * grid
    target_offset = (n_bars-target_length)//2
    arr[target_offset:target_offset+target_length] = target

    # final image array
    size = n_bars*2*bar_width + bar_width
    img = np.ones((size, size)) * back

    for i, val in np.ndenumerate(arr):
        x = i[0]*2*bar_width + bar_width
        img[bar_width:-bar_width, x:x+bar_width] = val

    if double:
        img2 = grating_illusion(n_bars, target_length, bar_width, back=grid, grid=back, target=target, double=False)
        return np.hstack([img, img2])
    else:
        return img


def ring_pattern(n_rings=8, target_pos_l=4, target_pos_r=3, ring_width=5, padding=10, back=0., rings=1., target=.5, invert_rings=False, double=True):
    """
    Ring Pattern White's-like illusion

    Parameters
    ----------
    n_rings: the number of rings
    target_pos_l: the "index" of the target ring on the left half
    target_pos_r: the "index" of the targetring on the right half
    ring_width: width per ring in px
    padding: padding around stimulus in px
    back: value for background
    rings: value for grid cells
    target: value for target
    invert_rings: inverts ordering of rings and background
    double: whether to return the full illusion with two grids side-by-side (inverting back and grid values)

    Returns
    -------
    2D numpy array
    """
    # calculate Minkowski-p=inf distances from centre
    x = np.arange(0, n_rings)
    x = np.hstack([np.flip(x), x])
    radii = np.maximum(np.abs(x[np.newaxis]), np.abs(x[:, np.newaxis]))

    # build array representing rings
    arr = np.ones((n_rings*2, n_rings*2)) * back
    arr[radii%2==(0 if invert_rings else 1)] = rings
    arr[radii==target_pos_l] = target

    # build image from array
    img = np.repeat(np.repeat(arr, ring_width, axis=0), ring_width, axis=1)
    img = np.pad(img, padding, constant_values=back)

    # create right half of stimulus
    if double:
        img2 = ring_pattern(n_rings, target_pos_r, 0, ring_width, padding, back, rings, target, invert_rings, double=False)
        return np.hstack([img, img2])
    else:
        return img
