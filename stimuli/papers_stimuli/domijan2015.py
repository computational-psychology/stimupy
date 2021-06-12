import os
import sys

stimuli_dir = os.path.abspath(__file__ + "../../../")
sys.path.append(stimuli_dir)
import illusions


def dungeon():
    # Done!
    return illusions.dungeon.domijan2015()

def cube():
    # Done!
    return illusions.cube.domijan2015()

def grating():
    # Done!
    return illusions.grating.domijan2015()

def ring():
    # Done!
    return illusions.ring.domijan2015()

def bullseye():
    # Done !
    return illusions.bullseye.domijan2015()

def simultaneous_brightness_contrast():
    # Done !
    return illusions.sbc.domijan2015()

def todorovic():
    return illusions.todorovic.domijan2015()

def checkerboard():
    # Done !
    return illusions.checkerboard_sbc.domijan2015()
