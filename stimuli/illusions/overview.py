import matplotlib.pyplot as plt
import math

import benary_cross
import bullseye
import checkerboard_contrast_contrast
import checkerboard_sbc
import cornsweet
import cube
import disc_and_ring
import dungeon
import grating
import grating_induction
import hermann
import rings
import sbc
import square_wave
import todorovic
import whites

"""
illusions = {
    "benary cross": benary_cross.benarys_cross(),
    "bullseye": bullseye.bullseye_illusion(),
    "checkerboard contrast\ncontrast effect": checkerboard_contrast_contrast.checkerboard_contrast_contrast_effect(),
    "checkerboard_sbc": checkerboard_sbc.checkerboard_contrast(),
    "cornsweet": cornsweet.cornsweet(101,5, 0.5),
    "cube": cube.cube_illusion(),
    "disc and ring": disc_and_ring.disc_and_ring((16,16), (6,3,2), (0.9, 0.4, 0.7)),
    "duneon": dungeon.dungeon_illusion(),
    "grating": grating.grating_illusion(),
    "grating induction": grating_induction.grating_induction(100, 20, 0.2),
    "hermann": hermann.hermann_grid(10, 2),
    "rings": rings.ring_pattern(),
    "sbc sbc": sbc.simultaneous_brightness_contrast(),
    "sbc simultaneous\ncontrast": sbc.simultaneous_contrast(100, 20),
    "square wave": square_wave.square_wave((16,16), 5, 0.5, 0.5),
    "todorovic": todorovic.todorovic_illusion(),
    "todorovic_lightness": todorovic.todorovic_lightness()

}
"""


white_illusions = {
    "white_illusion": whites.white_illusion(10, 3, 5),
    "zigzag_white": whites.zigzag_white(10, 4, 2),
    "wheel_of_fortune_white": whites.wheel_of_fortune_white(2, 10),
    "circular_white": whites.circular_white(4, 3),
    "SC_white": whites.SC_white(100, 20),
    "extended_white": whites.extended_white(100, 20),
    "checkered_white": whites.checkered_white(100),
    "squared_white": whites.squared_white(100, 10),
    "dotted_white": whites.dotted_white(100, 20, 5),
    "whites_illusion_bmcc": whites.whites_illusion_bmcc(100, 20, 5, 2),
    "contours_white_bmmc": whites.contours_white_bmmc(100, 20, 5, 1),
    "whites_illusion_gil": whites.whites_illusion_gil(100, 20, 5, 1)
}


M = len(illusions)
N = len(white_illusions)
a = int(math.ceil(math.sqrt(M+N)))

plt.figure(figsize=(20, 20))

for i, (name, img) in enumerate(white_illusions.items()):
    plt.subplot(a, a, M+i+1)
    plt.subplots_adjust(wspace=0.3, hspace=0.2)
    plt.xticks([])
    plt.yticks([])
    plt.title(name, fontsize=25)
    plt.imshow(img, cmap='gray')
"""
for i, (name, img) in enumerate(illusions.items()):
    plt.subplot(a, a, i+1)
    plt.subplots_adjust(wspace=0.3, hspace=0.2)
    plt.xticks([])
    plt.yticks([])
    plt.title(name, fontsize=25)
    plt.imshow(img, cmap='gray')"""


plt.show()