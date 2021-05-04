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
def circular_white(n_parts, n_targets):
    # Inputs:
    #   - n_parts: number of black and white parts within circle (int)
    #   - n_targets: number of targets in the circle (int)
    #   - switch_polarity: inverse pixel values (bool)

    # Decide on resolution for the grid.
    # The lower the resolution, the worse the circles will look
    n_grid = 400
    n_numbers = n_grid*3

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
    grid = np.zeros([n_grid, n_grid*2]) + 0.5

    # Divide the circle in n_parts parts
    n_parts += 1
    r = np.linspace(0, 1, n_parts)

    # Specify the target locations:
    target_locations = np.arange(n_parts/2 - n_targets, n_parts/2 + n_targets, 2, int)
    if target_locations[0] % 2==0:
        target_locations -= 1

    for i in range(n_parts-1):
        r_chosen = np.linspace(r[i], r[i+1], n_numbers)
        for j in range(n_numbers):
            r_tiny = r_chosen[j]
            xxx = r_tiny*xx
            xxx = xxx - xxx.max() / 2 + n_grid/2
            yyy = r_tiny*yy
            yyy = yyy - yyy.max() / 2 + n_grid/2

            if i%2==0:
                grid[xxx.astype(int), yyy.astype(int)] = 1
            else:
                grid[xxx.astype(int), yyy.astype(int)] = 0

            if any(i==target_locations):
                grid[xxx.astype(int), yyy.astype(int)] = 0.5

    grid[:, n_grid:n_grid*2] = np.abs(grid[:, 0:n_grid]-1)
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
