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
    arr[0, offs_c:offs_c+target_length] = target
    arr[-1, offs_f:offs_f+target_length] = target
    arr[offs_f:offs_f+target_length, 0] = target
    arr[offs_c:offs_c+target_length, -1] = target

    # final image array
    size = n_cells*cell_size + (n_cells-1)*cell_spacing + 2*padding
    img = np.ones((size, size)) * back

    for i, val in np.ndenumerate(arr):
        if i[0] in range(1, n_cells-1) and i[1] in range(1, n_cells-1):
            continue  # skip centre cells for efficiency
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


def bullseye_illusion(n_rings=8, ring_width=5, padding=10, back=0., rings=1., target=.5):
    """
    Bullseye Illusion.
    Two ring patterns (see ring_pattern func), with target in centre and one ring pattern inverted.

    Parameters
    ----------
    n_rings: the number of rings
    ring_width: width per ring in px
    padding: padding around stimulus in px
    back: value for background
    rings: value for grid cells
    target: value for target

    Returns
    -------
    2D numpy array
    """
    img1 = ring_pattern(n_rings=n_rings, target_pos_l=0, ring_width=ring_width, padding=padding,
                        back=back, rings=rings, target=target, invert_rings=False, double=False)
    img2 = ring_pattern(n_rings=n_rings, target_pos_l=0, ring_width=ring_width, padding=padding,
                        back=back, rings=rings, target=target, invert_rings=True, double=False)
    return np.hstack([img1, img2])


def simultaneous_brightness_contrast(input_size=100, target_size=20, left=1., right=0., target=.5):
    """
    Simultaneous brightness contrast

    Parameters
    ----------
    input_size: height of the input (and half of the width) in px
    target_size: height and width of the centred target square in px
    left: left background value
    right: right background value
    target: target value

    Returns
    -------
    2d numpy array
    """
    img1 = np.ones((input_size, input_size)) * left
    img2 = np.ones((input_size, input_size)) * right

    tpos = (input_size-target_size)//2
    img1[tpos:tpos+target_size, tpos:tpos+target_size] = target
    img2[tpos:tpos+target_size, tpos:tpos+target_size] = target

    return np.hstack([img1, img2])


def benarys_cross(input_size=100, cross_thickness=20, padding=10, back=1., cross=0., target=.5):
    """
    Benary's Cross Illusion (with square targets)

    Parameters
    ----------
    input_size: width and height of input in px
    cross_thickness: width of the cross bars in px
    padding: padding around cross in px
    back: background value
    cross: cross value
    target: target value

    Returns
    -------
    2D numpy array
    """
    img = np.ones((input_size, input_size)) * back

    cpos = (input_size - cross_thickness) // 2
    img[padding:-padding, cpos:-cpos] = cross
    img[cpos:-cpos, padding:-padding] = cross

    tsize = cross_thickness // 2
    tpos1y = cpos - tsize
    tpos1x = tpos1y
    tpos2y = cpos
    tpos2x = input_size - padding - tsize
    img[tpos1y:tpos1y + tsize, tpos1x:tpos1x + tsize] = target
    img[tpos2y:tpos2y + tsize, tpos2x:tpos2x + tsize] = target

    return img


def todorovic_illusion(input_size=100, target_size=40, spacing=5, padding=15, back=0., grid=1., target=.5, double=True):
    """
    Todorovic's illusion

    Parameters
    ----------
    input_size: height of the input (and half of the width) in px
    target_size: height and width of the centred target cross in px
    spacing: spacing between grid cells (i.e target cross bar thickness) in px
    padding: padding around grid in px
    back: value for background
    grid: value for grid cells
    target: value for target
    double: whether to return the full illusion with two grids side-by-side (inverting back and grid values)

    Returns
    -------

    """
    img = np.ones((input_size, input_size)) * back

    # put target square on image
    tpos = (input_size-target_size)//2
    img[tpos:-tpos, tpos:-tpos] = target

    # put grid cells on image
    csize = (input_size - 2*padding - spacing)//2
    gpos1 = padding
    gpos2 = padding + csize + spacing
    img[gpos1:gpos1+csize, gpos1:gpos1+csize] = grid
    img[gpos1:gpos1+csize, gpos2:gpos2+csize] = grid
    img[gpos2:gpos2+csize, gpos1:gpos1+csize] = grid
    img[gpos2:gpos2+csize, gpos2:gpos2+csize] = grid

    # create right half of stimulus
    if double:
        img2 = todorovic_illusion(input_size=input_size, target_size=target_size, spacing=spacing, padding=padding,
                                  back=grid, grid=back, target=target, double=False)
        return np.hstack([img, img2])
    else:
        return img


def checkerboard_contrast_contrast_effect(n_checks=8, check_size=10, target_length=4, padding=10, check1=0., check2=1.,
                                          tau=.5, alpha=.5):
    """
    Contrast-contrast effect on checkerboard with square transparency layer.

    Parameters
    ----------
    n_checks: number of checks per board in each direction
    check_size: size of a check in px
    target_length: size of the target in # checks
    padding: around board in px
    check1: a check value
    check2: other check value
    tau: tau of transparency
    alpha: alpha of transparency

    Returns
    -------
    2D numpy array
    """
    arr1 = np.ndarray((n_checks, n_checks))
    for i, j in np.ndindex((n_checks, n_checks)):
        arr1[i, j] = check1 if i % 2 == j % 2 else check2

    idx = np.zeros((n_checks, n_checks), dtype=bool)
    tpos = (n_checks - target_length) // 2
    idx[tpos:tpos + target_length, tpos:tpos + target_length] = True
    arr1[idx] = alpha * arr1[idx] + (1 - alpha) * tau

    arr2 = arr1.copy()
    arr2[~idx] = tau

    img1 = np.repeat(np.repeat(arr1, check_size, axis=0), check_size, axis=1)
    img1 = np.pad(img1, padding, constant_values=tau)
    img2 = np.repeat(np.repeat(arr2, check_size, axis=0), check_size, axis=1)
    img2 = np.pad(img2, padding, constant_values=tau)

    return np.hstack([img1, img2])


def checkerboard_contrast(n_checks=8, check_size=10, target1_coords=(3, 2), target2_coords=(5, 5), extend_targets=False,
                          padding=10, check1=0., check2=1., target=.5):
    """
    Checkerboard Contrast

    Parameters
    ----------
    n_checks: number of checks per board in each direction
    check_size: size of a check in px
    target1_coords: check-coordinates of target check 1
    target2_coords: check-coordinates of target check 2
    extend_targets: cross targets instead of single-check targets
    padding: around board in px
    check1: a check value
    check2: other check value
    target: target value

    Returns
    -------

    """
    arr = np.ndarray((n_checks, n_checks))
    for i, j in np.ndindex((n_checks, n_checks)):
        arr[i, j] = check1 if i % 2 == j % 2 else check2

    arr[target1_coords] = target
    arr[target2_coords] = target
    if extend_targets:
        for idx in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            arr[target1_coords[0] + idx[0], target1_coords[1] + idx[1]] = target
            arr[target2_coords[0] + idx[0], target2_coords[1] + idx[1]] = target

    img = np.repeat(np.repeat(arr, check_size, axis=0), check_size, axis=1)
    img = np.pad(img, padding, constant_values=((check1 + check2) / 2))

    return img
