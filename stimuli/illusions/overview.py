import matplotlib.pyplot as plt
import math

from stimuli import illusions, papers


stimuli = {
    "benary cross": illusions.benarys_cross(),
    "checkerboard contrast\ncontrast effect": illusions.checkerboard_contrast_contrast_effect(),
    "checkerboard sbc": illusions.checkerboard_contrast(),
    "checkerboard extended": illusions.checkerboard_contrast(extend_targets=True),
    "cornsweet": illusions.cornsweet(),
    "cube": illusions.cube_illusion(),
    "disc and ring": illusions.disc_and_ring(),
    "duneon": illusions.dungeon_illusion(),
    "grating": illusions.grating_illusion(),
    "grating induction": illusions.grating_induction.grating_illusion(),
    "hermann": illusions.hermann_grid(),
    "rings": illusions.ring_pattern(),
    "bullseye": illusions.bullseye_illusion(),
    "sbc sbc": illusions.simultaneous_brightness_contrast(),
    "todorovic in": papers.RHS2007.todorovic_in_large(),
    "todorovic equal": papers.RHS2007.todorovic_equal(),
    "white_illusion": illusions.white(),
    "circular white": illusions.circular_white(),
    "wheel of fortune_white": illusions.wheel_of_fortune_white(),
    "white anderson": illusions.white_anderson(),
    "white howe": illusions.white_anderson(target_offsets_top=(0,), target_offsets_bottom=(0,)),
}


M = len(stimuli)
a = int(math.ceil(math.sqrt(M)))

plt.figure(figsize=(20, 20))

for i, (name, stim) in enumerate(stimuli.items()):
    plt.subplot(a, a, i + 1)
    plt.subplots_adjust(wspace=0.3, hspace=0.2)
    plt.xticks([])
    plt.yticks([])
    plt.title(name, fontsize=25)
    plt.imshow(stim["img"], cmap="gray")

plt.tight_layout()
plt.show()
