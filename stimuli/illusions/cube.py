import numpy as np

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