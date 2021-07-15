import numpy as np
import math

import stimuli



def WE_thick():
    return stimuli.illusions.whites.RHS2007_WE_thick()

def WE_thin_wide():
    return stimuli.illusions.whites.RHS2007_WE_thin_wide()


def WE_dual():
    return stimuli.illusions.whites.RHS2007_WE_dual()


def WE_anderson():
    return stimuli.illusions.whites.RHS2007_WE_anderson()


def WE_howe():
    return stimuli.illusions.whites.RHS2007_WE_howe()

def WE_zigzag():
    # TODO: not available atm
    pass


def WE_radial_thick_small():
    return stimuli.illusions.whites.RHS2007_WE_radial_thick_small()

def WE_radial_thick():
    return stimuli.illusions.whites.RHS2007_WE_radial_thick()


def WE_radial_thin_small():
    return stimuli.illusions.whites.RHS2007_WE_radial_thin_small()


def WE_radial_thin():
    return stimuli.illusions.whites.RHS2007_WE_radial_thin_small()


def WE_circular1():
    return stimuli.illusions.whites.RHS2007_WE_circular1()


def WE_circular05():
    return stimuli.illusions.whites.RHS2007_WE_circular05()


def WE_circular025():
    return stimuli.illusions.whites.RHS2007_WE_circular025()


def grating_induction():
    return stimuli.illusions.grating_induction.RHS2007_grating_induction()


def sbc_large():
    return stimuli.illusions.sbc.RHS2007_sbc_large()

def sbc_small():
    return stimuli.illusions.sbc.RHS2007_sbc_small()


def todorovic_equal():
    return stimuli.illusions.todorovic.RHS2007_todorovic_equal()

def todorovic_in_large():
    return stimuli.illusions.todorovic.RHS2007_todorovic_in_large()

def todorovic_in_small():
    return stimuli.illusions.todorovic.RHS2007_todorovic_in_small()


def todorovic_out():
    #TODO: not available atm
    pass

def checkerboard_016():
    return stimuli.illusions.checkerboard_sbc.RHS2007_Checkerboard016()

def checkerboard_094():
    return stimuli.illusions.checkerboard_sbc.RHS2007_Checkerboard0938()

def checkerboard21():
    return stimuli.illusions.checkerboard_sbc.RHS2007_Checkerboard209()


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
    return stimuli.illusions.bullseye.RHS2007_bullseye_thin()

def bullseye_thick():
    # The parameters are mostly guessed
    return stimuli.illusions.bullseye.RHS2007_bullseye_thick()

if __name__ == "__main__":
    import matplotlib.pyplot as plt
    plot_all = True
    if plot_all:
        stims = {
            "WE_thick": WE_thick,
            "WE_thin_wide": WE_thin_wide,
            "WE_dual": WE_dual,
            "WE_anderson": WE_anderson,
            "WE_howe": WE_howe,
            "WE_radial_thick_small": WE_radial_thick_small,
            "WE_radial_thick": WE_radial_thick,
            "WE_radial_thin_small": WE_radial_thin_small,
            "WE_radial_thin": WE_radial_thin,
            "WE_circular1": WE_circular1,
            "WE_circular05": WE_circular05,
            "WE_circular025": WE_circular025,
            "grating_induction": grating_induction,
            "sbc_large": sbc_large,
            "sbc_small": sbc_small,
            "todorovic_equal": todorovic_equal,
            "todorovic_in_large": todorovic_in_large,
            "todorovic_in_small": todorovic_in_small
        }

        M = len(stims)
        plt.figure(figsize=(8, M*3))
        for i, (stim_name, stim) in enumerate(stims.items()):
            print("Generating", stim_name+"")
            st = stim()
            plt.subplot(M, 2, 2 * i + 1)
            plt.title(stim_name + " - img")
            plt.imshow(st.img, cmap='gray')

            if st.target_mask is not None:
                plt.subplot(M, 2, 2 * i + 2)
                plt.colorbar()
                plt.title(stim_name + " - mask")
                plt.imshow(st.target_mask, cmap='gray')

        plt.tight_layout()

    else:
        plt.imshow(img, cmap='gray')
    plt.show()
