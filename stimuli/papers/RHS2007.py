import numpy as np

from stimuli import illusions

def WE_thick():
    return stimuli.illusions.whites.RHS2007_WE_thick()

def WE_thin_wide():
    return stimuli.illusions.whites.RHS2007_WE_thin_wide()

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
    # TODO: not available atm
    img = illusions.whites.zigzag_white(40, 4, 4)
    return img

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
    return illusions.whites.RHS2007_WE_circular1()

def WE_circular05():
    return illusions.whites.RHS2007_WE_circular05()

def WE_circular025():
    return illusions.whites.RHS2007_WE_circular025()

def grating_induction():
    return illusions.grating_induction.RHS2007_grating_induction()

def sbc_large():
    return illusions.sbc.RHS2007_sbc_large()

def sbc_small():
   return illusions.sbc.RHS2007_sbc_small()

def todorovic_equal():
    return illusions.todorovic.RHS2007_todorovic_equal()

def todorovic_in_large():
    return illusions.todorovic.RHS2007_todorovic_in_large()

def todorovic_in_small():
    return illusions.todorovic.RHS2007_todorovic_in_small()

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
    # The parameters are mostly guessed
    return illusions.bullseye.RHS2007_bullseye_thin()

def bullseye_thick():
    # The parameters are mostly guessed
    return illusions.bullseye.RHS2007_bullseye_thick()
