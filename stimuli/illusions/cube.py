import numpy as np
from stimuli.utils import degrees_to_pixels
# from stimuli.illusions.checkerboards import checkerboard


__all__ = [
    "cube_varying_cells",
    "cube_illusion",
]


def cube_varying_cells(
    ppd=None,
    cell_heights=None,
    cell_widths=None,
    cell_spacing=None,
    targets=None,
    intensity_background=0.0,
    intensity_grid=1.0,
    intensity_target=0.5,
):
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
    n_cells = np.maximum(n_cells, len(cell_spacing)+1)
    
    if len(cell_heights) == 1:
        cell_heights = cell_heights * n_cells
    if len(cell_widths) == 1:
        cell_widths = cell_widths * n_cells
    if len(cell_spacing) == 1:
        cell_spacing = cell_spacing * n_cells
    cell_spacing = list(cell_spacing)
    cell_spacing[n_cells-1] = 0

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
        img[0:cheights[i], xs:xs+cwidths[i]] = fill_img
        img[height-cheights[i]::, xs:xs+cwidths[i]] = fill_img
        mask[0:cheights[i], xs:xs+cwidths[i]] = fill_mask
        mask[height-cheights[i]::, xs:xs+cwidths[i]] = fill_mask
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
        img[xs:xs+cwidths[i], 0:cheights[i]] = fill_img
        img[xs:xs+cwidths[i], width-cheights[i]::] = fill_img
        mask[xs:xs+cwidths[i], 0:cheights[i]] = fill_mask
        mask[xs:xs+cwidths[i], width-cheights[i]::] = fill_mask
        xs += cwidths[i] + cspaces[i]

    stim = {
        "img": img,
        "mask": mask.astype(int),
        }
    return stim


def cube_illusion(
    visual_size=None,
    ppd=None,
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
    visual_size :
        blub
    ppd : int
        pixels per degree (visual angle)
    n_cells : int
        the number of square cells (not counting background) per dimension
    cell_thickness : 
        blub
    cell_spacing : float or (float, float)
        distance between two cells in degrees visual angle
    intensity_background : float
        intensity value for background
    intensity_grid : float
        intensity value for grid cells
    intensity_target : float
        intensity value for target

    Returns
    -------
    A stimulus dictionary with the stimulus ['img'] and target mask ['mask']
    """
    if isinstance(visual_size, (float, int)):
        visual_size = (visual_size, visual_size)
    if isinstance(cell_spacing, (float, int)):
        cell_spacing = (cell_spacing, cell_spacing)
    if isinstance(n_cells, (float, int)):
        n_cells = (n_cells, n_cells)
    if targets is None:
        targets = ()

    height, width = degrees_to_pixels(visual_size, ppd)
    cell_space = degrees_to_pixels(cell_spacing, ppd)
    cell_thick = degrees_to_pixels(cell_thickness, ppd)

    # Initiate image
    img = np.ones([height, width]) * intensity_background
    mask = np.zeros([height, width])

    # Calculate cell widths and heights
    cell_height = int((height - cell_space[0]*(n_cells[0]-1)) / n_cells[0])
    cell_width = int((width - cell_space[1]*(n_cells[1]-1)) / n_cells[1])
    
    if (cell_thick > cell_height) or (cell_thick > cell_width):
        raise ValueError("cell_thickness is too large")

    # Calculate cell placements:
    xs = np.arange(0, width-1, cell_width+cell_space[1])
    rxs = xs[::-1]
    ys = np.arange(0, height-1, cell_height+cell_space[0])
    rys = ys[::-1]
    
    # Add cells: top and bottom
    for i in range(n_cells[1]):
        if i in targets:
            fill_img = intensity_target
            fill_mask = 1
        else:
            fill_img = intensity_grid
            fill_mask = 0
        img[0:cell_thick, xs[i]:xs[i]+cell_width] = fill_img
        img[height-cell_thick::, rxs[i]:rxs[i]+cell_width] = fill_img
        mask[0:cell_thick, xs[i]:xs[i]+cell_width] = fill_mask
        mask[height-cell_thick::, rxs[i]:rxs[i]+cell_width] = fill_mask

    # Add cells: left and right
    for i in range(n_cells[0]):
        if i in targets:
            fill_img = intensity_target
            fill_mask = 1
        else:
            fill_img = intensity_grid
            fill_mask = 0
        img[rys[i]:rys[i]+cell_height, 0:cell_thick] = fill_img
        img[ys[i]:ys[i]+cell_height, height-cell_thick::] = fill_img
        mask[rys[i]:rys[i]+cell_height, 0:cell_thick] = fill_mask
        mask[ys[i]:ys[i]+cell_height, height-cell_thick::] = fill_mask

    stim = {
        "img": img,
        "mask": mask.astype(int),
        }
    return stim



if __name__ == "__main__":
    from stimuli.utils import plot_stimuli
    
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
        "Cube - varying cells": cube_varying_cells(**p1),
        "Cube": cube_illusion(**p2),
        }
    plot_stimuli(stims, mask=True, save=None)
