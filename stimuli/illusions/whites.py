"""
This script contains code for creating different brightness illusions.
See /tests/test_brightness_illusions.py for examples.


Illusions were inspired from:
1. White, 2010
The Early History of Whites Illusion

2. Robinson, Hammon, & de Sa, 2007
Explaining brightness illusions using spatial filtering and local response normalization

3. Blakeslee, Pasieka, & McCourt, 2005
Oriented multiscale spatial filtering and contrast normalization: a parsimonious
model of brightness induction in a continuum of stimuli including White, Howe
and simultaneous brightness contrast

Last update on 09.02.2021
@author: lynn
"""

import numpy as np
from stimuli.utils.utils import degrees_to_pixels
from stimuli.illusions.square_wave import square_wave


###################################
#     (Howe's) White illusion     #
###################################
def white_illusion(n_grid, n_targets, width_target, invert=False, grid_lum=1,
                   switch_polarity=False, width_howe=0, anderson_displacement=0):
    # TODO: n_grid seems to be number of cycles, not size of the grid in pixels
    # TODO: add possiblity of displacement of target in vertical/horizontal direction
    # TODO: add possibility of rotating the illusiong
    # Inputs:
    #   - n_grid: size of the grid (int, unit: pixels) -> this is wrong, it represents number of cycles
    #   - n_targets: number of targets that get placed on the black and white bars (int)
    #   - width_target: width of the targets (int, unit: pixels)
    #   - invert: if True, create inverted White illusion (bool)
    #   - grid_lum: luminance value for grid (float)
    #   - width_howe: width of uniform background behind the targets (int, unit: pixels)
    #   - anderson_displacement: displacement of the uniform background behind the
    #                            targets (int, unit: pixels)

    if invert:
        target_lum = 1
    else:
        target_lum = 0.5

    # Create the grid
    grid = np.zeros([n_grid, n_grid], dtype=np.float32)
    grid[::2, :] = grid_lum

    # Place the targets equally in the upper and lower half of the grid:
    start_dark = n_grid / 2 - n_targets*2
    start_bright = n_grid / 2 + 1

    # In case the target is bigger than half of the grid:
    # 1. Correction for dark target:
    if start_dark < 0:
        start_dark = 0
    # 2. Correction for bright target:
    diff = n_grid/2 - n_targets*2 -1
    if diff < 0:
        start_bright += diff

    # The same stimulus should always be on even parts of the grid:
    if start_bright % 2 != 0:
        start_bright += 1

    # Ensure that one target is on white and one target on black bars:
    if (start_dark+start_bright) % 2 == 0:
        start_dark += 1

    # Choose a width for the target:
    start_dark_width = int(n_grid / 2 + 1)
    start_bright_width = int(n_grid / 2 - width_target)

    # For Howe background:
    diff = (width_target - width_howe) / 2
    if diff < 0:
        start_dark_width -= diff/2
        start_bright_width += diff/2

    # For Anderson displacement:
    diff_dark = diff + anderson_displacement
    diff_bright = diff - anderson_displacement

    # Ensure that it looks symmetric:
    if (width_target - width_howe) % 2 == 0:
        start_bright_width -= 1
        # Place Howe background on grid:
        grid[:, int(start_dark_width+diff_dark):int(start_dark_width+diff_dark+width_howe)] = 1
        grid[:, int(start_bright_width+diff_bright):int(start_bright_width+diff_bright+width_howe)] = 0

        # Move Howe background:
        if anderson_displacement > 0:
            grid[int(start_dark):int(start_dark+n_targets*2):2, :] = 0
            grid[int(start_bright):int(start_bright+n_targets*2):2, :] = 1

        grid[int(start_dark):int(start_dark+n_targets*2):2, int(start_dark_width):int(start_dark_width+width_target)] = target_lum
        grid[int(start_bright):int(start_bright+n_targets*2):2, int(start_bright_width):int(start_bright_width+width_target)] = target_lum

    else:
        # Place Howe background on grid:
        grid[:, int(start_dark_width+diff_dark):int(start_dark_width+diff_dark+width_howe)] = 1
        grid[:, int(start_bright_width+diff_bright):int(start_bright_width+diff_bright+width_howe)] = 0

        # Move Howe background:
        if anderson_displacement > 0:
            grid[int(start_dark):int(start_dark+n_targets*2):2, :] = 0
            grid[int(start_bright):int(start_bright+n_targets*2):2, :] = 1

        grid[int(start_dark):int(start_dark+n_targets*2):2, int(start_dark_width):int(start_dark_width+width_target)] = target_lum
        grid[int(start_bright):int(start_bright+n_targets*2):2, int(start_bright_width-1):int(start_bright_width-1+width_target)] = target_lum

    if switch_polarity:
        grid = np.abs(grid-1)
    return grid


###################################
#      Zig-zag White illusion     #
###################################
def zigzag_white(n_grid, n_parts, n_target):
    # Inputs:
    #   - n_grid: size of the grid (int, unit: pixels); it should be even numbered
    #   - n_parts: number of grid parts in one dimension (int); n_parts divided
    #              by an even number still needs to be an even number
    #   - n_targets: number of targets that get placed on the black and white
    #                bars (int)

    # Create the grid
    grid = np.zeros([n_grid, n_grid], dtype=np.float32)
    # There should always be one pixel between the zigzag lines:
    distance = int(2)
    # Calculate length of the lines based on grid size and number of zigzag lines
    part_len = int(n_grid / n_parts)

    # Create the zigzag grid
    for h in range(0, int(n_parts), distance):
        for i in range(0, n_grid, distance):
            for j in range(part_len+1):
                idx1 = i + part_len*h
                idx2 = i + j
                if idx1 >= n_grid:
                    idx1 -= n_grid
                if idx2 >= n_grid:
                    idx2 -= n_grid

                grid[int(idx2), int(idx1)] = 1
                grid[int(idx1), int(idx2)] = 1

    # Depending on the number of targets, choose the starting point for
    # positioning the target in the grid
    start_targets = int(n_grid/2 - n_target/2*distance)
    end_targets = int(n_grid/2 + n_target/2*distance)
    # Ensure that one target is placed on black and one on white lines
    if n_target % 2 != 0:
        start_targets -= 1

    # Place the first type of target in the grid:
    for i in range(start_targets, end_targets, distance):
        for j in range(int(part_len/2), part_len):
            idx1 = i
            idx2 = i + j

            if idx1 >= n_grid:
                idx1 = []
            if idx2 >= n_grid:
                idx2 = []
            grid[int(idx2), int(idx1)] = 0.5

    # Place the second type of target in the grid:
    for i in range(start_targets, end_targets, distance):
        for j in range(int(part_len/2), part_len):
            idx1 = i + part_len -1
            idx2 = i + j - part_len -1

            if idx1 >= n_grid:
                idx1 = []
            if idx2 >= n_grid:
                idx2 = []
            grid[int(idx2), int(idx1)] = 0.5
    return grid


###################################
#     Wheel of fortune White      #
###################################
def wheel_of_fortune_white(n_parts, target_width):
    # Inputs:
    #   - n_parts: number of black and white parts within circle (int), it
    #              should be even numbered to avoid asymmetry
    #   - target_width: relative width of the targets between 0 and 1 (float)

    # Decide on resolution for the grid.
    # The lower the resolution, the worse the wheel of fortune will look
    n_grid = 1000
    n_numbers = n_grid / 2

    # Create a circle
    x = np.linspace(0, 2*np.pi, int(n_numbers))

    xx = np.cos(x)
    xx_min = np.abs(xx.min())
    xx += xx_min
    xx_max = xx.max()
    xx = xx / xx_max * (n_grid-1)

    yy = np.sin(x)
    yy_min = np.abs(yy.min())
    yy += yy_min
    yy_max = yy.max()
    yy = yy / yy_max * (n_grid-1)

    # Change the background to gray and place the circle on the grid:
    grid = np.zeros([n_grid, n_grid]) + 0.5
    grid[xx.astype(int), yy.astype(int)] = 1

    # Divide circle in n_parts parts:
    x = np.linspace(0, 2*np.pi, int(n_parts+1))

    for i in range(len(x)-1):
        xxx = np.linspace(x[i], x[i+1], int(n_numbers))
        xxxx = np.cos(xxx)
        xxxx += xx_min
        xxxx = xxxx / xx_max * (n_grid-1)

        yyyy = np.sin(xxx)
        yyyy += yy_min
        yyyy = yyyy / yy_max * (n_grid-1)

        for j in range(int(n_numbers)):
            sep_x = np.linspace(n_grid/2, xxxx[j], int(n_numbers))
            sep_y = np.linspace(n_grid/2, yyyy[j], int(n_numbers))
            # Switch between bright and dark areas:
            if i % 2 == 0:
                grid[sep_x.astype(int), sep_y.astype(int)] = 1
                if i == 0:
                    # Place a single target inside the area
                    grid[sep_x[int(n_numbers*(0.5-target_width/2)):int(n_numbers*(0.5+target_width/2))].astype(int),
                         sep_y[int(n_numbers*(0.5-target_width/2)):int(n_numbers*(0.5+target_width/2))].astype(int)] = 0.5
            else:
                grid[sep_x.astype(int), sep_y.astype(int)] = 0
                if i == n_parts/2 or i == n_parts/2+1:
                    # Place a single target inside the area
                    grid[sep_x[int(n_numbers*(0.5-target_width/2)):int(n_numbers*(0.5+target_width/2))].astype(int),
                         sep_y[int(n_numbers*(0.5-target_width/2)):int(n_numbers*(0.5+target_width/2))].astype(int)] = 0.5
    return grid


###################################
#     Circular White illusion     #
###################################
def circular_white(n_parts, target_locations, padding=(10,10,10,10,), high = 1., low = 0., target = .5, res = 400):
    # TODO: it's really slow

    # Inputs:
    #   - n_parts: number of black and white parts within circle (int)
    #   - n_targets: number of targets in the circle (int)
    #   - switch_polarity: inverse pixel values (bool)
    #   - index of the circle

    # Decide on resolution for the grid.
    # The lower the resolution, the worse the circles will look
    n_grid = res
    n_numbers = n_grid*3

    n_targets = len(target_locations)
    target_locations = np.array(target_locations)
    # Create a circle
    x = np.linspace(0, 2*np.pi, n_numbers)

    xx = np.cos(x)
    xx_min = np.abs(xx.min())
    xx += xx_min
    xx_max = xx.max()
    xx = xx / xx_max * (n_grid-1)

    yy = np.sin(x)
    yy_min = np.abs(yy.min())
    yy += yy_min
    yy_max = yy.max()
    yy = yy / yy_max * (n_grid-1)

    # Change the background to gray and place the circle on the grid:
    grid = np.ones([n_grid, n_grid*2]) * target

    # Divide the circle in n_parts parts
    n_parts += 1
    r = np.linspace(0, 1, n_parts)


    for i in range(n_parts-1):
        r_chosen = np.linspace(r[i], r[i+1], n_numbers)
        for j in range(n_numbers):
            r_tiny = r_chosen[j]
            xxx = r_tiny*xx
            xxx = xxx - xxx.max() / 2 + n_grid/2
            yyy = r_tiny*yy
            yyy = yyy - yyy.max() / 2 + n_grid/2

            if i%2==0:
                grid[xxx.astype(int), yyy.astype(int)] = high
            else:
                grid[xxx.astype(int), yyy.astype(int)] = low

            if any(i==target_locations):
                grid[xxx.astype(int), yyy.astype(int)] = target

    grid[:, n_grid:n_grid*2] = np.abs(grid[:, 0:n_grid]-1)

    padding_top, padding_bottom, padding_left, padding_right = padding
    padding_tuple = ((padding_top, padding_bottom), (padding_left, padding_right))
    grid = np.pad(grid, padding_tuple, "constant", constant_values=target)

    return grid


###################################
#         Extended White          #
###################################
def SC_white(n_grid, size_target, grid_lum=1):
    # Inputs:
    #   - n_grid: height of the grid (int, unit: pixels)
    #   - size_target: size of target in one dimension (int, unit: pixels)
    #   - grid_lum: highest luminance value in grid (float)

    # Create the background:
    grid = np.zeros([n_grid, n_grid*2], dtype=np.float32)
    grid[:, :] = grid_lum

    center = n_grid / 2
    # Ensure that the illusion looks symmetric:
    if size_target % 2 == 0:
        # Place targets on grid
        grid[int(center-size_target/2):int(center+size_target/2):2, int(center-size_target/2):int(center+size_target/2)] = 0.5
        grid[int(center-size_target/2+1):int(center+size_target/2):2, int(center-size_target/2):int(center+size_target/2)] = 1

    else:
        # Place targets on grid
        grid[int(center-size_target/2):int(center+1+size_target/2):2, int(center-size_target/2):int(center+1+size_target/2)] = 0.5
        grid[int(center-size_target/2):int(center+2+size_target/2):2, int(center-size_target/2):int(center+1+size_target/2)] = 1

    grid[:, n_grid:n_grid*2] = np.abs(grid[:, 0:n_grid]-1)
    return grid


def extended_white(n_grid, size_target, shift=False):
    # Inputs:
    #   - n_grid: height of the grid (int, unit: pixels)
    #   - size_target: size of target in one dimension (int, unit: pixels)
    #   - shift: shift whole grid around target by one (bool)

    # Create the background:
    grid = np.zeros([n_grid, n_grid*2], dtype=np.float32)
    grid[::2, :] = 1

    center = n_grid / 2
    # Ensure that the illusion looks symmetric:
    if size_target % 2 == 0:

        if shift:
            grid[:, int(center-size_target/2):int(center+size_target/2)] = 0
            grid[1::2, int(center-size_target/2):int(center+size_target/2)] = 1
            grid[int(center+1-size_target/2):int(center+1+size_target/2):2, int(center-size_target/2):int(center+size_target/2)] = 0.5
        else:
            # Place targets on grid
            grid[int(center-size_target/2):int(center+size_target/2):2, int(center-size_target/2):int(center+size_target/2)] = 0.5

    else:
        if shift:
            grid[:, int(center-size_target/2):int(center+1+size_target/2)] = 0
            grid[1::2, int(center-size_target/2):int(center+1+size_target/2)] = 1
            grid[int(center-size_target/2):int(center+1+size_target/2):2, int(center-size_target/2):int(center+1+size_target/2)] = 0.5
        else:
            # Place targets on grid
            grid[int(center+1-size_target/2):int(center+1+size_target/2):2, int(center-size_target/2):int(center+1+size_target/2)] = 0.5

    grid[:, n_grid:n_grid*2] = np.abs(grid[:, 0:n_grid]-1)
    return grid


###################################
#     Checkered White illusion    #
###################################
def checkered_white(n_grid):
    # Inputs:
    #   - n_grid: height of the grid (int, unit: pixels)

    # Create the checkerboard:
    grid = np.zeros([n_grid, n_grid*2], dtype=np.float32)
    grid[::2, ::2] = 1
    grid[1::2, 1::2] = 1

    if n_grid % 2 == 0:
        grid[int(n_grid/2), int(n_grid/2-1)] = 0.5
        grid[int(n_grid/2), int(n_grid/2+n_grid)] = 0.5
    else:
        grid[int(n_grid/2), int(n_grid/2)] = 0.5
        grid[int(n_grid/2), int(n_grid/2+n_grid)] = 0.5
    return grid


###################################
#      Squared White illusion     #
###################################
def squared_white(n_grid, thickness, target_ID=0):
    # Inputs:
    #   - n_grid: size of the grid (int, unit: pixels)
    #   - thickness: thickness of lines that comprise the squares (int, unit: pixels);
    #                if n_grid is even, thickness should also be even numbered
    #   - target_ID: index of target (int), default=0 for choosing the central square
    #   - switch_polarity: inverse pixel values (bool)

    grid = np.zeros([n_grid, n_grid*2], dtype=np.float32)
    grid[int(0):int(thickness), :] = 0.5
    grid[:, int(n_grid-thickness)::] = 0.5
    grid[int(n_grid-thickness)::, :] = 0.5
    grid[:, int(0):int(thickness)] = 0.5

    thickness_half = thickness / 2
    center = n_grid / 2

    for i in range(0, int(n_grid/2), thickness*2):
        if i == (target_ID*thickness*2):
            lum = 0.5
        else:
            lum = 1

        if thickness % 2==0:
            grid[int(center-i-thickness_half):int(center+i+thickness_half), int(center-i-thickness_half):int(center-i+thickness_half)] = lum
            grid[int(center-i-thickness_half):int(center+i+thickness_half), int(center+i-thickness_half):int(center+i+thickness_half)] = lum
            grid[int(center-i-thickness_half):int(center-i+thickness_half), int(center-i-thickness_half):int(center+i+thickness_half)] = lum
            grid[int(center+i-thickness_half):int(center+i+thickness_half), int(center-i-thickness_half):int(center+i+thickness_half)] = lum

        else:
            grid[int(center-i-thickness_half):int(center+i+thickness_half+1), int(center-i-thickness_half):int(center-i+thickness_half+1)] = lum
            grid[int(center-i-thickness_half):int(center+i+thickness_half+1), int(center+i-thickness_half):int(center+i+thickness_half+1)] = lum
            grid[int(center-i-thickness_half):int(center-i+thickness_half+1), int(center-i-thickness_half):int(center+i+thickness_half+1)] = lum
            grid[int(center+i-thickness_half):int(center+i+thickness_half+1), int(center-i-thickness_half):int(center+i+thickness_half+1)] = lum

    grid[:, int(n_grid):int(n_grid*2)] = np.abs(grid[:, int(0):int(n_grid)]-1)
    return grid


###################################
#      Dotted White illusion      #
###################################
def dotted_white(n_grid, size_target, n_dots, reverse_target=False):
    # Inputs:
    #   - n_grid: size/resolution of the grid (int, unit: pixels)
    #   - size_target: size of the central target squares (int, unit: pixels)
    #   - n_dots: number of dots per row (int)
    #   - switch_polarity: inverse pixel values (bool)
    #   - reverse_target: if True, the dots become the target

    # Decide on resolution for the grid.
    # The lower the resolution, the worse the dots will look
    n_numbers = n_grid*5
    size_dots = int(n_grid/n_dots)
    patch = np.zeros([size_dots, size_dots])

    # Create a circle
    x = np.linspace(0, 2*np.pi, n_numbers)

    xx = np.cos(x)
    xx_min = np.abs(xx.min())
    xx += xx_min
    xx_max = xx.max()

    yy = np.sin(x)
    yy_min = np.abs(yy.min())
    yy += yy_min
    yy_max = yy.max()

    # Place the circle on the dot and fill it by decreasing the radius of
    # the circle
    for i in range(int(size_dots/5), size_dots):
        xxx = xx / xx_max * (size_dots-i)
        xxx = xxx + size_dots/2 - xxx.max()/2
        yyy = yy / yy_max * (size_dots-i)
        yyy = yyy + size_dots/2 - yyy.max()/2
        patch[xxx.astype(int), yyy.astype(int)] = 1

    # Create the background:
    grid = np.zeros([n_grid, n_grid*2], dtype=np.float32)
    center = n_grid / 2

    # Place target on grid
    grid[int(center-size_target/2):int(center+size_target/2),
         int(center-size_target/2):int(center+size_target/2)] = 0.5

    # Either have a gray square behind the circles or gray circles:
    patch_tiled = np.tile(patch, (n_dots, n_dots))
    if reverse_target:
        patch_tiled = np.abs(patch_tiled-1)
    grid[:, int(0):int(n_grid)] += patch_tiled
    grid[grid > 1] = 1

    grid[:, int(n_grid):int(n_grid*2)] = np.abs(grid[:, int(0):int(n_grid)]-1)
    return grid



"""
The following illusions come from lightness module that has been integrated into illusions module
TODO: check for any redundancies between the the functions above and below
"""



def whites_illusion_bmcc(shape, ppd, contrast, frequency, mean_lum=.5,
                         patch_height=None, start='high', sep=1, padding=(3,3,3,3)):
    """
    Create a version of White's illusion on a square wave, in the style used by
    Blakeslee and McCourt (1999).

    Parameters
    ----------
    shape : tuple of 2 numbers
            The shape of the stimulus in degrees of visual angle. (y,x)
    ppd : number
          the number of pixels in one degree of visual angle
    contrast : float, in [0,1]
               the contrast of the grating, defined as
               (max_luminance - min_luminance) / mean_luminance
    frequency : number
                the spatial frequency of the wave in cycles per degree
    mean_lum : number
               the mean luminance of the grating, i.e. (max_lum + min_lum) / 2.
               The average luminance of the actual stimulus can differ slightly
               from this value if the stimulus is not an integer of cycles big.
    patch_height : number
                   the height of the gray patches, in degrees of visual ange
    start : string in ['high', 'low'] (optional)
            specifies if the wave starts with a high or low value. Default is
            'high'.
    sep : int (optional)
          the separation distance between the two test patches, measured in
          full grating cycles. Default is 1.
    padding: 4-valued tuple specifying padding (top, bottom, left, right) in degrees visual angle


    Returns
    -------
    stim : ndarray (2D)
        the stimulus

    References
    ----------
    Blakeslee B, McCourt ME (1999). A multiscale spatial filtering account of
    the White effect, simultaneous brightness contrast and grating induction.
    Vision research 39(26):4361-77.
    """
    padding_top, padding_bottom, padding_left, padding_right = tuple(int(degrees_to_pixels(x, ppd)) for x in padding)

    stim = square_wave(shape, ppd, contrast, frequency, mean_lum, 'full', start)
    half_cycle = int(degrees_to_pixels(1. / frequency / 2, ppd) + .5)
    if patch_height is None:
        patch_height = stim.shape[0] // 3
    else:
        patch_height = degrees_to_pixels(patch_height, ppd)
    y_pos = (stim.shape[0] - patch_height) // 2
    stim[y_pos: -y_pos,
         stim.shape[1] // 2 - (sep + 1) * half_cycle:
         stim.shape[1] // 2 - sep * half_cycle] = mean_lum
    stim[y_pos: -y_pos,
         stim.shape[1] // 2 + sep * half_cycle:
         stim.shape[1] // 2 + (sep + 1) * half_cycle] = mean_lum
    stim = np.pad(stim, ((padding_top, padding_bottom), (padding_left, padding_right)), 'constant', constant_values=mean_lum)

    return stim


def contours_white_bmmc(shape, ppd, contrast, frequency, mean_lum=.5,
                        patch_height=None, sep=1, orientation='vertical', contour_width=6):
    """
    Create stimuli with contours masking either the vertical or the horizontal
    borders of the test patches in White's illusion (Blakeslee, McCourt
    version).

    Parameters
    ----------
    shape : tuple of 2 numbers
            The shape of the stimulus in degrees of visual angle. (y,x)
    ppd : number
          the number of pixels in one degree of visual angle
    contrast : float, in [0,1]
               the contrast of dark vs bright contours, defined as
               (max_luminance - min_luminance) / (2 * mean_luminance)
    frequency : number
                the spatial frequency of the White's stimulus to be masked in
                cycles per degree
    mean_lum : number
               the background luminance of the masking stimuli.
    patch_height : number
                   the height of the gray patches to be masked, in degrees of
                   visual ange
    sep : int (optional)
          the separation distance between the two test patches, measured in
          full grating cycles. Default is 1.
    orientation : ['vertical', 'horizontal'] (optional)
                  the orientation of the border to be masked. Default is
                  'vertical'.
    contour_width : number
                     the width of the masking contour in pixels

    Returns
    -------
    masks : tuple of two 2D ndarrays
            the contour adaptation masks. masks[0] has dark contours, mask[1]
            has bright contours.
    """
    shape = degrees_to_pixels(np.array(shape), ppd).astype(int)
    pixels_per_cycle = int(degrees_to_pixels(1. / frequency / 2, ppd) + .5) * 2
    shape[1] = (shape[1] // pixels_per_cycle) * pixels_per_cycle
    # determine pixel width of individual grating bars (half cycle)
    hc = pixels_per_cycle // 2
    if patch_height is None:
        patch_height = shape[0] // 3
    else:
        patch_height = degrees_to_pixels(patch_height, ppd)
    y_pos = (shape[0] - patch_height) // 2
    x_pos = (shape[1] // 2 - (sep + 1) * hc,
             shape[1] // 2 + sep * hc)
    mask_dark = np.ones(shape) * mean_lum
    mask_bright = np.ones(shape) * mean_lum
    idx_mask = np.zeros(shape, dtype=bool)
    bright = mean_lum * (1 + contrast)
    dark = mean_lum * (1 - contrast)
    offset = contour_width // 2
    if orientation == 'vertical':
        idx_mask[y_pos: -y_pos,
                 x_pos[0] - offset: x_pos[0] + offset] = True
        idx_mask[y_pos: -y_pos,
                 x_pos[0] + hc - offset: x_pos[0] + hc + offset] = True
        idx_mask[y_pos: -y_pos,
                 x_pos[1] - offset: x_pos[1] + offset] = True
        idx_mask[y_pos: -y_pos,
                 x_pos[1] + hc - offset: x_pos[1] + hc + offset] = True
    elif orientation == 'horizontal':
        idx_mask[y_pos - offset: y_pos + offset,
                 x_pos[0]: x_pos[0] + hc] = True
        idx_mask[y_pos - offset: y_pos + offset,
                 x_pos[1]: x_pos[1] + hc] = True
        idx_mask[-y_pos - offset: -y_pos + offset,
                 x_pos[0]: x_pos[0] + hc] = True
        idx_mask[-y_pos - offset: -y_pos + offset,
                 x_pos[1]: x_pos[1] + hc] = True
    mask_dark[idx_mask] = dark
    mask_bright[idx_mask] = bright
    return mask_dark, mask_bright


def whites_illusion_gil(shape, ppd, contrast, frequency, mean_lum=.5,
                        start='low'):
    """
    Create a version of White's illusion on a square wave, in the style used by
    Gilchrist (2006, p. 281)

    Parameters
    ----------
    shape : tuple of 2 numbers
            The shape of the stimulus in degrees of visual angle. (y,x)
    ppd : number
          the number of pixels in one degree of visual angle
    contrast : float, in [0,1]
               the contrast of the grating, defined as
               (max_luminance - min_luminance) / mean_luminance
    frequency : number
                the spatial frequency of the wave in cycles per degree
    mean_lum : number
               the mean luminance of the grating, i.e. (max_lum + min_lum) / 2.
               The average luminance of the actual stimulus can differ slightly
               from this value if the stimulus is not an integer of cycles big.
    start : string in ['high', 'low'] (optional)
            specifies if the wave starts with a high or low value. Default is
            'high'.

    Returns
    -------
    stim : ndarray (2D)
           the stimulus

    References
    ----------
    Gilchrist A (2006). Seeing Black and White. New York, New York, USA: Oxford
    University Press.
    """
    stim = square_wave(shape, ppd, contrast, frequency, mean_lum, 'half',
                       start)
    half_cycle = int(degrees_to_pixels(1. / frequency / 2, ppd) + .5)
    on_dark_idx = [i for i in range(int(half_cycle * 2.5),
                                    int(stim.shape[1] - half_cycle * .5))
                   if stim[0, i] < mean_lum]
    on_light_idx = [i for i in range(int(half_cycle * 1.5),
                                     int(stim.shape[1] - half_cycle * 1.5))
                    if stim[0, i] > mean_lum]
    stim[stim.shape[0] // 5:
         stim.shape[0] // 5 * 2, on_light_idx] = mean_lum
    stim[stim.shape[0] // 5 * 3:
         stim.shape[0] // 5 * 4, on_dark_idx] = mean_lum

    # randomize border cutoff
    max_cut = stim.shape[0] / 10
    bg = stim[0, half_cycle]
    for start_idx in range(0 if start is 'low' else half_cycle,
                           stim.shape[1] - half_cycle, 2 * half_cycle):
        stim[0: np.random.randint(max_cut),
             start_idx: start_idx + half_cycle] = bg
        stim[stim.shape[0] - np.random.randint(max_cut):,
             start_idx: start_idx + half_cycle] = bg
    return stim



def default_white(n_cycles=5, grating_shape=(100,10), target_index=1, target_spacing=3, target_height=20, target_y_offset=0,
                padding=(10,10,10,10,), start="high", high=1, low=0, target=0.5):
    grating_height, grating_width = grating_shape
    height, width = grating_height, n_cycles*grating_width*2
    img = np.ones((height, width))*low

    target_start_y = int(height//2 - target_height//2 - target_y_offset)
    target_end_y = int(target_start_y + target_height)

    for i in range(n_cycles):
        img[:, 2*i*grating_width:(2*i+1)*grating_width] = high

        if 2*i == target_index or 2*i == target_index+target_spacing:
            img[target_start_y: target_end_y, 2*i*grating_width:(2*i+1)*grating_width] = target

        if (2*i+1) == target_index or (2*i+1) == target_index+target_spacing:
            img[target_start_y: target_end_y, (2*i+1)*grating_width:(2*i+2)*grating_width] = target

    if start == "low":
        high_mask, low_mask = img == high, img == low
        img[high_mask] = low
        img[low_mask] = high

    padding_top, padding_bottom, padding_left, padding_right = padding
    img = np.pad(img, ((padding_top, padding_bottom), (padding_left, padding_right)), 'constant', constant_values=target)

    return img


def domijan2015_white():
    return  default_white(n_cycles=4, grating_shape=(81, 10), target_index=2, target_spacing=3, start="low", target_height=21, padding=(9, 10, 9, 11), high=9, low=1, target=5)


def RHS2007_WE_thick():
    phase_width = 20
    height = phase_width * 6
    return default_white(n_cycles=4, grating_shape=(height, phase_width), target_index=2, target_spacing=3,
                                        target_height=phase_width*2, padding=(50,50,50,50,), start="low")
def RHS2007_WE_thin_wide():
    phase_width = 10
    height = phase_width * 12
    return default_white(n_cycles=8, grating_shape=(height, phase_width), target_index=3, target_spacing=9,
                                    target_height=phase_width*2, padding=(50, 50, 50, 50,), start="high")

def RHS2007_WE_circular1():
    return circular_white(8, (4,), padding=(200,200,0,0))

def RHS2007_WE_circular05():
    return circular_white(16, (10,), padding=(200, 200, 0, 0), res=1600)

def RHS2007_WE_circular025():
    return circular_white(32, (22,))
