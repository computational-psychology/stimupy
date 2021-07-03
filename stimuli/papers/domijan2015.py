import os
import sys

from stimuli import illusions

def dungeon():
    return illusions.dungeon.domijan2015()

def cube():
    return illusions.cube.domijan2015()

def grating():
    return illusions.grating.domijan2015()

def rings():
    return illusions.rings.domijan2015()

def bullseye():
    return illusions.bullseye.domijan2015()

def simultaneous_brightness_contrast():
    return illusions.sbc.domijan2015()

def white():
    return illusions.whites.domijan2015_white()

def benary():
    return illusions.benary_cross.domijan2015()

def todorovic():
    return illusions.todorovic.domijan2015()

def checkerboard_contrast_contrast():
    return illusions.checkerboard_contrast_contrast.domijan2015()

def checkerboard():
    return illusions.checkerboard_sbc.domijan2015()

def checkerboard_extended():
    return illusions.checkerboard_sbc.domijan2015_extended()
