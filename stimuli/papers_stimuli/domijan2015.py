import os
import sys

from stimuli import illusions

def benary():
    return illusions.benary_cross.domijan2015()

def todorovic():
    return illusions.todorovic.domijan2015()

def checkerboard():
    return illusions.checkerboard_sbc.domijan2015()

def simultaneous_brightness_contrast():
    return illusions.sbc.domijan2015()

def dungeon():
    return illusions.dungeon.domijan2015()

def cube():
    return illusions.cube.domijan2015()

def grating():
    return illusions.grating.domijan2015()

def ring():
    return illusions.ring.domijan2015()

def bullseye():
    return illusions.bullseye.domijan2015()

def white():
    return illusions.whites.domijan2015_white()