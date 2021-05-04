import os
import sys

stimuli_dir = os.path.abspath(__file__ + "../../../")
sys.path.append(stimuli_dir)
import illusions


def dungeon():
    return illusions.dungeon.domijan()

def cube():
    return illusions.cube.domijan()

def grating():
    return illusions.grating.domijan()

def ring():
    return illusions.ring.domijan()

def bullseye():
    return illusions.bullseye.domijan()

def simultaneous_brightness_contrast():
    return illusions.sbc.domijan()

def todorovic():
    return illusions.todorovic.domijan()

def checkerboard():
    return illusions.checkerboard_sbc.domijan()
