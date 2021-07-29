import matplotlib.pyplot as plt
import math

from stimuli import illusions



stimuli = {
    "benary cross": illusions.benarys_cross,
    "bullseye": illusions.bullseye_illusion,
    "checkerboard contrast\ncontrast effect": illusions.checkerboard_contrast_contrast_effect,
    "checkerboard_sbc": illusions.checkerboard_contrast,
    "cornsweet": illusions.cornsweet,
    "cube": illusions.cube_illusion,
    "disc and ring": illusions.disc_and_ring,
    "duneon": illusions.dungeon_illusion,
    "grating": illusions.grating_illusion,
    "grating induction": illusions.grating_illusion,
    "hermann": illusions.hermann_grid,
    "rings": illusions.ring_pattern,
    "sbc sbc": illusions.simultaneous_brightness_contrast,
    "todorovic": illusions.todorovic_illusion,
    "white_illusion": illusions.white,
    "circular_white": illusions.circular_white,
    "wheel_of_fortune_white": illusions.wheel_of_fortune_white,
    "white_anderson": illusions.white_anderson
}



M = len(stimuli)
a = int(math.ceil(math.sqrt(M)))

plt.figure(figsize=(20, 20))

for i, (name, stim_func) in enumerate(stimuli.items()):
    stim = stim_func()
    plt.subplot(a, a, i+1)
    plt.subplots_adjust(wspace=0.3, hspace=0.2)
    plt.xticks([])
    plt.yticks([])
    plt.title(name, fontsize=25)
    plt.imshow(stim.img, cmap='gray')


plt.show()