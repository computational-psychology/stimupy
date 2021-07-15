"""
This script creates example pngs for each illusion from /src/illusions/brightness_illusions2.py (see this script for
references).

Last update on 16.02.2021
@author: lynn & max
"""

import os
import matplotlib.pyplot as plt
from stimuli import illusions

result_folder = 'brightness_illusions/'
if not os.path.exists(result_folder):
    os.mkdir(result_folder)


# Dungeon Illusion
plt.imshow(illusions.dungeon_illusion())
plt.show()
plt.imshow(illusions.dungeon_illusion(7, 3))
plt.show()
plt.imshow(illusions.dungeon_illusion(15, 3))
plt.show()


# Cube Illusion
plt.imshow(illusions.cube_illusion(4, 1))
plt.show()
plt.imshow(illusions.cube_illusion(4, 2))
plt.show()
plt.imshow(illusions.cube_illusion(8, 3))
plt.show()


# Grating Illusion
plt.imshow(illusions.grating_illusion())
plt.show()
plt.imshow(illusions.grating_illusion(10, 2))
plt.show()


# Ring Pattern
plt.imshow(illusions.ring_pattern())
plt.show()
plt.imshow(illusions.ring_pattern(12, 5, 6))
plt.show()
