import math

import numpy as np
import stimuli

__all__ = [
    "WE_thick",
    "WE_thin_wide",
    "WE_dual",
    "WE_anderson",
    "WE_howe",
    "WE_zigzag",
    "WE_radial_thick_small",
    "WE_radial_thick",
    "WE_radial_thin_small",
    "WE_circular1",
    "WE_circular05",
    "WE_circular025",
    "grating_induction",
    "sbc_large",
    "sbc_small",
    "todorovic_equal",
    "todorovic_in_large",
    "todorovic_in_small",
    "todorovic_out",
    "checkerboard_016",
    "checkerboard_0938",
    "checkerboard209",
    "corrugated_mondrian",
    "benary_cross",
    "todorovic_benary1_2",
    "todorovic_benary3_4",
    "bullseye_thin",
    "bullseye_thick",
]


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
    raise NotImplementedError


def WE_radial_thick_small():
    return stimuli.illusions.whites.RHS2007_WE_radial_thick_small()


def WE_radial_thick():
    return stimuli.illusions.whites.RHS2007_WE_radial_thick()


def WE_radial_thin_small():
    return stimuli.illusions.whites.RHS2007_WE_radial_thin_small()


def WE_radial_thin():
    return stimuli.illusions.whites.RHS2007_WE_radial_thin()


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
    # TODO: not available atm
    raise NotImplementedError


def checkerboard_016():
    return stimuli.illusions.checkerboard_sbc.RHS2007_Checkerboard016()


def checkerboard_0938():
    return stimuli.illusions.checkerboard_sbc.RHS2007_Checkerboard0938()


def checkerboard209():
    return stimuli.illusions.checkerboard_sbc.RHS2007_Checkerboard209()


def corrugated_mondrian():
    # TODO: not available atm
    raise NotImplementedError


def benary_cross():
    # TODO: not available atm
    raise NotImplementedError


def todorovic_benary1_2():
    # TODO: not available atm
    raise NotImplementedError


def todorovic_benary3_4():
    # TODO: not available atm
    raise NotImplementedError


def bullseye_thin():
    # The parameters are mostly guessed
    return stimuli.illusions.bullseye.RHS2007_bullseye_thin()


def bullseye_thick():
    # The parameters are mostly guessed
    return stimuli.illusions.bullseye.RHS2007_bullseye_thick()


if __name__ == "__main__":
    import matplotlib.pyplot as plt

    stims = {}
    for stimname in __all__:
        print("Generating " + stimname)
        try:
            stims[stimname] = globals()[stimname]()
        except NotImplementedError:
            print("-- not implemented")

    # Plot each stimulus+mask
    n_stim = math.ceil(math.sqrt(len(stims)))
    plt.figure(figsize=(n_stim * 3, n_stim * 3))
    for i, (stim_name, stim) in enumerate(stims.items()):
        img, mask = stim["img"], stim["mask"]
        img = np.dstack([img, img, img])

        mask = np.insert(np.expand_dims(mask, 2), 1, 0, axis=2)
        mask = np.insert(mask, 2, 0, axis=2)
        final = mask + img
        final /= np.max(final)

        plt.subplot(n_stim, n_stim, i + 1)
        plt.title(stim_name)
        plt.imshow(final)

    plt.tight_layout()

    plt.show()
