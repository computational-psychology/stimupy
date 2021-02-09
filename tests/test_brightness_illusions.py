"""
This script creates example pngs for each illusion from /src/illusions/brightness_illusions.py (see this script for
references). They will be saved in the chosen result_folder (default: ./brightness_illusions/).

Last update on 09.02.2021
@author: lynn
"""

import os
import matplotlib.pyplot as plt
from stimuli import illusions

result_folder = 'brightness_illusions/'
if not os.path.exists(result_folder):
    os.mkdir(result_folder)


###################################
#     (Howe's) White illusion     #
###################################

# Classical White plots:
n_grid = 10
n_target = 1
width_target = 2

n = 1
m = 4
plt.figure(figsize=[25, 5])
plt.rcParams.update({'font.size': 12})
plt.subplot(n, m, 1)
plt.imshow(illusions.white_illusion(n_grid, n_target, width_target), cmap='gray')
plt.title('Classical White illusion 1')
plt.axis('off')

plt.subplot(n, m, 2)
plt.imshow(illusions.white_illusion(20, 1, 4), cmap='gray')
plt.title('Classical White illusion 2')
plt.axis('off')

plt.subplot(n, m, 3)
plt.imshow(illusions.white_illusion(20, 4, 8), cmap='gray')
plt.title('Classical White illusion 3')
plt.axis('off')

plt.subplot(n, m, 4)
plt.imshow(illusions.white_illusion(40, 14, 2), cmap='gray')
plt.title('Classical White illusion 4')
plt.axis('off')
plt.savefig(result_folder + '/white_classics.png')
plt.close()

# White variations plots:
n_grid = 20
n_target = 1
width_target = 4
invert = False
grid_lum = 1
switch_polarity = False
width_howe = 2
anderson_displacement = 2

n = 1
m = 5
plt.figure(figsize=[25, 5])
plt.rcParams.update({'font.size': 12})
plt.subplot(n, m, 1)
plt.imshow(illusions.white_illusion(n_grid, n_target, width_target), cmap='gray')
plt.title('Classical White illusion')
plt.axis('off')

plt.subplot(n, m, 2)
plt.imshow(illusions.white_illusion(n_grid, n_target, width_target, invert, grid_lum, switch_polarity, width_howe), cmap='gray')
plt.title('Howes White illusion 1')
plt.axis('off')

plt.subplot(n, m, 3)
plt.imshow(illusions.white_illusion(n_grid, n_target, width_target, invert, grid_lum, switch_polarity, 4), cmap='gray')
plt.title('Howes White illusion 2')
plt.axis('off')

plt.subplot(n, m, 4)
plt.imshow(illusions.white_illusion(n_grid, n_target, width_target, invert, grid_lum, switch_polarity, 8), cmap='gray')
plt.title('Howes White illusion 3')
plt.axis('off')

plt.subplot(n, m, 5)
plt.imshow(illusions.white_illusion(n_grid, n_target, width_target, invert, grid_lum, switch_polarity, 4, anderson_displacement), cmap='gray')
plt.title('Anderson White illusion')
plt.axis('off')
plt.savefig(result_folder + 'white_variations.png')
plt.close()


# Inverted White plots:
n_grid = 20
n_target = 3
width_target = 1
invert = True
grid_lum = 0.5
switch_polarity = False
# Adjustment to control the limits of the colormap (otherwise, the targets wouldnt be gray):
plot_adjustment_clim = 0.5

n = 2
m = 4
plt.figure(figsize=[25, 15])
plt.rcParams.update({'font.size': 12})
plt.subplot(n, m, 1)
plt.imshow(illusions.white_illusion(n_grid, n_target, width_target, invert, grid_lum, switch_polarity), cmap='gray')
plt.clim(0, 1+plot_adjustment_clim)
plt.title('Inverted White illusion 1')
plt.axis('off')

plt.subplot(n, m, 2)
plt.imshow(illusions.white_illusion(n_grid, n_target, width_target, invert, grid_lum, True), cmap='gray')
plt.clim(0-plot_adjustment_clim, 1)
plt.title('Inverted White illusion 2')
plt.axis('off')

plt.subplot(n, m, 3)
plt.imshow(illusions.white_illusion(20, n_target, 7, invert, grid_lum, switch_polarity), cmap='gray')
plt.clim(0, 1+plot_adjustment_clim)
plt.title('Inverted White illusion 3')
plt.axis('off')

plt.subplot(n, m, 4)
plt.imshow(illusions.white_illusion(20, n_target, 7, invert, grid_lum, True), cmap='gray')
plt.clim(0-plot_adjustment_clim, 1)
plt.title('Inverted White illusion 4')
plt.axis('off')

# Choose a different adjustment of the colormap for the following bars:
plot_adjustment_clim = 1

plt.subplot(n, m, 5)
plt.imshow(illusions.white_illusion(n_grid, n_target, width_target, invert, grid_lum, switch_polarity), cmap='gray')
plt.clim(0, 1+plot_adjustment_clim)
plt.title('Inverted White illusion 5')
plt.axis('off')

plt.subplot(n, m, 6)
plt.imshow(illusions.white_illusion(n_grid, n_target, width_target, invert, grid_lum, True), cmap='gray')
plt.clim(0-plot_adjustment_clim, 1)
plt.title('Inverted White illusion 6')
plt.axis('off')

plt.subplot(n, m, 7)
plt.imshow(illusions.white_illusion(20, n_target, 7, invert, grid_lum, switch_polarity), cmap='gray')
plt.clim(0, 1+plot_adjustment_clim)
plt.title('Inverted White illusion 7')
plt.axis('off')

plt.subplot(n, m, 8)
plt.imshow(illusions.white_illusion(20, n_target, 7, invert, grid_lum, True), cmap='gray')
plt.clim(0-plot_adjustment_clim, 1)
plt.title('Inverted White illusion 8')
plt.axis('off')
plt.savefig(result_folder + 'white_inverted.png')
plt.close()


###################################
#      Zig-zag White illusion     #
###################################

# n_grid needs to be an even number
n_grid = 12
# n_parts divided by an even number still needs to be an even number
n_parts = n_grid / 2
n_target = 2

n = 1
m = 4
plt.figure(figsize=[25, 5])
plt.rcParams.update({'font.size': 12})

plt.subplot(n, m, 1)
plt.imshow(illusions.zigzag_white(n_grid, n_parts, n_target), cmap='gray')
plt.title('Zig-zag White illusion 1')
plt.axis('off')

plt.subplot(n, m, 2)
plt.imshow(illusions.zigzag_white(16, 4, 4), cmap='gray')
plt.title('Zig-zag White illusion 2')
plt.axis('off')

plt.subplot(n, m, 3)
plt.imshow(illusions.zigzag_white(32, 4, 4), cmap='gray')
plt.title('Zig-zag White illusion 3')
plt.axis('off')

plt.subplot(n, m, 4)
plt.imshow(illusions.zigzag_white(48, 6, 12), cmap='gray')
plt.title('Zig-zag White illusion 4')
plt.axis('off')
plt.savefig(result_folder + 'zigzag_white.png')
plt.close()


###################################
#     Wheel of fortune White      #
###################################

# n_parts should be even numbered
n_parts = 14
target_width = 0.2

n = 1
m = 4
plt.figure(figsize=[25, 5])
plt.rcParams.update({'font.size': 12})

plt.subplot(n, m, 1)
plt.imshow(illusions.wheel_of_fortune_white(n_parts, target_width), cmap='gray')
plt.title('Wheel of fortune White illusion 1')
plt.axis('off')

plt.subplot(n, m, 2)
plt.imshow(illusions.wheel_of_fortune_white(n_parts, 0.6), cmap='gray')
plt.title('Wheel of fortune White illusion 2')
plt.axis('off')

plt.subplot(n, m, 3)
plt.imshow(illusions.wheel_of_fortune_white(34, 0.4), cmap='gray')
plt.title('Wheel of fortune White illusion 3')
plt.axis('off')

plt.subplot(n, m, 4)
plt.imshow(illusions.wheel_of_fortune_white(50, 0.4), cmap='gray')
plt.title('Wheel of fortune White illusion 4')
plt.axis('off')
plt.savefig(result_folder + 'wheel_of_fortune_white.png')
plt.close()


###################################
#     Circular White illusion     #
###################################

n_parts = 8
n_targets = 1

n = 2
m = 2
plt.figure(figsize=[25, 15])
plt.rcParams.update({'font.size': 12})

plt.subplot(n, m, 1)
plt.imshow(illusions.circular_white(n_parts, n_targets), cmap='gray')
plt.title('Circular White illusion 1')
plt.axis('off')

plt.subplot(n, m, 2)
plt.imshow(illusions.circular_white(16, 1), cmap='gray')
plt.title('Circular White illusion 2')
plt.axis('off')

plt.subplot(n, m, 3)
plt.imshow(illusions.circular_white(28, 1), cmap='gray')
plt.title('Circular White illusion 3')
plt.axis('off')

plt.subplot(n, m, 4)
plt.imshow(illusions.circular_white(28, 6), cmap='gray')
plt.title('Circular White illusion 4')
plt.axis('off')
plt.savefig(result_folder + 'circular_white.png')
plt.close()


###################################
#      Simultaneous contrast      #
###################################

# Classical simultaneous contrast plots:
n_grid = 20
size_target = 8

n = 2
m = 2
plt.figure(figsize=[25, 15])
plt.rcParams.update({'font.size': 12})

plt.subplot(n, m, 1)
plt.imshow(illusions.simultaneous_contrast(n_grid, size_target), cmap='gray')
plt.title('Simultaneous contrast illusion 1')
plt.axis('off')

plt.subplot(n, m, 2)
plt.imshow(illusions.simultaneous_contrast(n_grid, 6), cmap='gray')
plt.title('Simultaneous contrast illusion 2')
plt.axis('off')

plt.subplot(n, m, 3)
plt.imshow(illusions.simultaneous_contrast(n_grid, 4), cmap='gray')
plt.title('Simultaneous contrast illusion 3')
plt.axis('off')

plt.subplot(n, m, 4)
plt.imshow(illusions.simultaneous_contrast(n_grid, 2), cmap='gray')
plt.title('Simultaneous contrast illusion 4')
plt.axis('off')
plt.savefig(result_folder + 'simultaneous_contrast.png')
plt.close()

# Covered simultaneous contrast plots:
n_grid = 20
size_target = 10
add_squares = True
size_squares = 2

n = 2
m = 2
plt.figure(figsize=[25, 15])
plt.rcParams.update({'font.size': 12})

plt.subplot(n, m, 1)
plt.imshow(illusions.simultaneous_contrast(n_grid, size_target, add_squares, size_squares), cmap='gray')
plt.title('Covered simultaneous contrast illusion 1')
plt.axis('off')

plt.subplot(n, m, 2)
plt.imshow(illusions.simultaneous_contrast(30, 14, add_squares, 6), cmap='gray')
plt.title('Covered simultaneous contrast illusion 2')
plt.axis('off')

plt.subplot(n, m, 3)
plt.imshow(illusions.simultaneous_contrast(30, 14, add_squares, 5), cmap='gray')
plt.title('Covered simultaneous contrast illusion 3')
plt.axis('off')

plt.subplot(n, m, 4)
plt.imshow(illusions.simultaneous_contrast(30, 14, add_squares, size_squares), cmap='gray')
plt.title('Covered simultaneous contrast illusion 4')
plt.axis('off')
plt.savefig(result_folder + 'simultaneous_contrast_covered.png')
plt.close()


###################################
#         Extended White          #
###################################

n_grid = 30
size_target = 10
grid_lum = 1
shift = True

n = 2
m = 2
plt.figure(figsize=[25, 15])
plt.rcParams.update({'font.size': 12})

plt.subplot(n, m, 1)
plt.imshow(illusions.SC_white(n_grid, size_target, grid_lum), cmap='gray')
plt.clim(0, 1)
plt.title('Extended White illusion 1')
plt.axis('off')

plt.subplot(n, m, 2)
plt.imshow(illusions.SC_white(n_grid, size_target, 0), cmap='gray')
plt.title('Extended White illusion 2')
plt.axis('off')

plt.subplot(n, m, 3)
plt.imshow(illusions.extended_white(n_grid, size_target, False), cmap='gray')
plt.title('Extended White illusion 3')
plt.axis('off')

plt.subplot(n, m, 4)
plt.imshow(illusions.extended_white(n_grid, size_target, shift), cmap='gray')
plt.title('Extended White illusion 4')
plt.axis('off')
plt.savefig(result_folder + 'white_extended.png')
plt.close()


###################################
#        Grating induction        #
###################################

n_grid = 8
width_target = 0.5
blur = 6

n = 1
m = 4
plt.figure(figsize=[25, 5])
plt.rcParams.update({'font.size': 12})

plt.subplot(n, m, 1)
plt.imshow(illusions.grating_induction(n_grid, width_target, blur), cmap='gray')
plt.title('Grating induction 1')
plt.axis('off')

plt.subplot(n, m, 2)
plt.imshow(illusions.grating_induction(n_grid, width_target, 12), cmap='gray')
plt.title('Grating induction 2')
plt.axis('off')

plt.subplot(n, m, 3)
plt.imshow(illusions.grating_induction(22, 1.5, 14), cmap='gray')
plt.title('Grating induction 3')
plt.axis('off')

plt.subplot(n, m, 4)
plt.imshow(illusions.grating_induction(22, 0.5, 14), cmap='gray')
plt.title('Grating induction 4')
plt.axis('off')
plt.savefig(result_folder + 'grating_induction.png')
plt.close()


###################################
#     Checkered White illusion    #
###################################

n_grid = 5

n = 2
m = 2
plt.figure(figsize=[25, 15])
plt.rcParams.update({'font.size': 12})

plt.subplot(n, m, 1)
plt.imshow(illusions.checkered_white(n_grid), cmap='gray')
plt.title('Checkered White illusion 1')
plt.axis('off')

plt.subplot(n, m, 2)
plt.imshow(illusions.checkered_white(11), cmap='gray')
plt.title('Checkered White illusion 2')
plt.axis('off')

plt.subplot(n, m, 3)
plt.imshow(illusions.checkered_white(25), cmap='gray')
plt.title('Checkered White illusion 3')
plt.axis('off')

plt.subplot(n, m, 4)
plt.imshow(illusions.checkered_white(51), cmap='gray')
plt.title('Checkered White illusion 4')
plt.axis('off')
plt.savefig(result_folder + 'checkered_white.png')
plt.close()


###################################
#      Squared White illusion     #
###################################

# To ensure symmetry, n_grid and thickness should either both be even or both be odd
n_grid = 20
thickness = 2
target_ID = 0

n = 1
m = 2
plt.figure(figsize=[25, 5])
plt.rcParams.update({'font.size': 12})

plt.subplot(n, m, 1)
plt.imshow(illusions.squared_white(n_grid, thickness, target_ID), cmap='gray')
plt.title('Squared White illusion 1')
plt.axis('off')

plt.subplot(n, m, 2)
plt.imshow(illusions.squared_white(44, thickness, 2), cmap='gray')
plt.title('Squared White illusion 2')
plt.axis('off')
plt.savefig(result_folder + 'squared_white.png')
plt.close()


###################################
#      Dotted White illusion      #
###################################

# n_grid changes the resolution of the grid.
# The lower the resolution, the worse the dots will look
n_grid = 900
size_target = 300
n_dots = 9

n = 1
m = 2
plt.figure(figsize=[25, 5])
plt.rcParams.update({'font.size': 12})

plt.subplot(n, m, 1)
plt.imshow(illusions.dotted_white(n_grid, size_target, n_dots), cmap='gray')
plt.title('Dotted White illusion 1')
plt.axis('off')

plt.subplot(n, m, 2)
plt.imshow(illusions.dotted_white(n_grid, size_target, n_dots, True), cmap='gray')
plt.title('Dotted White illusion 2')
plt.axis('off')
plt.savefig(result_folder + 'dotted_white.png')
plt.close()
