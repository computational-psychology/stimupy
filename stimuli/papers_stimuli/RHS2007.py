import os
import sys

stimuli_dir = os.path.abspath(__file__ + "../../../")
sys.path.append(stimuli_dir)
import illusions
import lightness

def WE_thick():
    # TODO: patch_height doesn't work
    # TODO: see if something needs to be changed for the contrast
    shape = (12, 16)
    return lightness.whites_illusion_bmcc(shape=(12, 16), ppd=5, contrast=0.5, frequency=4/shape[0], start="low")


def WE_thin_wide():
    # TODO: change the positions of the targets
    shape = (12, 16)
    return lightness.whites_illusion_bmcc(shape=(12, 16), ppd=5, contrast=0.5, frequency=8/shape[0], start="low")


def WE_dual():
    #TODO: not available atm
    pass

def WE_anderson():
    #TODO: not available atm
    pass

def WE_howe():
    #TODO: not available atm
    pass

def WE_zigzag():
    # TODO: rotate the illusion
    # TODO: not totally sure what n_parts does exactly
    # TODO: change size in degrees visual angle
    return illusions.whites.zigzag_white(20, 10, 4)

def WE_radial_thick_small():
    #TODO: not available atm
    pass

def WE_radial_thick():
    #TODO: not available atm
    pass

def WE_radial_thin_small():
    #TODO: not available atm
    pass

def WE_radial_thin():
    #TODO: not available atm
    pass

def WE_circular1():
    # TODO: change the location of the target inside the circle
    # TODO: set fixed total size in degrees visual angle
    return illusions.whites.circular_white(8, 1)

def WE_circular05():
    # TODO: change the location of the target inside the circle
    # TODO: set fixed total size in degrees visual angle
    return illusions.circular_white(16, 2)

def WE_circular025():
    # TODO: change the location of the target inside the circle
    # TODO: set fixed total size in degrees visual angle
    return illusions.circular_white(32, 2)

def grating_induction():
    # TODO: choose shape in degrees visual angle (and don't make it square automagically)
    # TODO: specify target width in degrees visual angle
    # TODO: figure out exact blur value
    return illusions.grating_induction(n_grid=8, width_target=0.4, blur=5)

def sbc_large():
    # TODO: choose shape in degrees visual angle
    return illusions.sbc.simultaneous_brightness_contrast(input_size=100, target_size=25 )

def sbc_small():
    # TODO: choose shape in degrees visual angle
    return illusions.sbc.simultaneous_brightness_contrast(input_size=96, target_size=8 )

def todorovic_equal():
    # TODO: figure out correct value for padding/spacing/input_size
    # TODO: specify background shape in deg visual angle
    return illusions.todorovic.todorovic_illusion(input_size=100, target_size=76, spacing=16, padding=12, back=1.0, grid=0, target=0.5 )

def todorovic_in_large():
    # TODO: figure out correct value for padding/spacing/input_size
    # TODO: specify background shape in deg visual angle
    return illusions.todorovic.todorovic_illusion(input_size=100, target_size=44, spacing=10, padding=15, back=1.0, grid=0, target=0.5)

def todorovic_in_small():
    return illusions.todorovic.todorovic_illusion(input_size=100, target_size=25, spacing=10, padding=20, back=1.0, grid=0, target=0.5)

def todorovic_out():
    #TODO: not available atm
    pass

def checkerboard_016():
    #TODO: not available atm
    pass

def checkerboard_094():
    #TODO: not available atm
    pass

def checkerboard21():
    #TODO: not available atm
    pass

def corrugated_mondrian():
    #TODO: not available atm
    pass

def benary_cross():
    #TODO: not available atm
    pass

def todorovic_benary1_2():
    #TODO: not available atm
    pass

def todorovic_benary3_4():
    #TODO: not available atm
    pass

def bullseye_thin():
    # TODO: figure out the correct parameters
    return illusions.bullseye.bullseye_illusion(n_rings=8, ring_width=1, padding=1, back=0., rings=1., target=.5)

def bullseye_thick():
    # TODO: figure out the correct parameters
    return illusions.bullseye.bullseye_illusion(n_rings=8, ring_width=1, padding=1, back=0., rings=1., target=.5)
