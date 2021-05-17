import os
import sys

stimuli_dir = os.path.abspath(__file__ + "../../../")
sys.path.append(stimuli_dir)
import illusions


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

def simultaneous_brightness_contrast():
    return illusions.sbc.domijan2015()

def todorovic():
    return illusions.todorovic.domijan2015()

def checkerboard():
    return illusions.checkerboard_sbc.domijan2015()
