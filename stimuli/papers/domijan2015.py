from stimuli import illusions

__all__ = [
    "dungeon",
    "cube",
    "grating",
    "rings",
    "bullseye",
    "simultaneous_brightness_contrast",
    "white",
    "benary",
    "todorovic",
    "checkerboard_contrast_contrast",
    "checkerboard",
    "checkerboard_extended",
]


def dungeon():
    # mask done
    return illusions.dungeon.domijan2015()


def cube():
    # mask done
    return illusions.cube.domijan2015()


def grating():
    # mask done
    return illusions.grating.domijan2015()


def rings():
    # mask done
    return illusions.rings.domijan2015()


def bullseye():
    # TODO: add mask
    return illusions.bullseye.domijan2015()


def simultaneous_brightness_contrast():
    # mask done
    return illusions.sbc.domijan2015()


def white():
    return illusions.whites.domijan2015_white()


def benary():
    # mask done
    return illusions.benary_cross.domijan2015()


def todorovic():
    # mask done
    return illusions.todorovic.domijan2015()


def checkerboard_contrast_contrast():
    # TODO: add mask
    return illusions.checkerboard_contrast_contrast.domijan2015()


def checkerboard():
    # mask done
    return illusions.checkerboard_sbc.domijan2015()


def checkerboard_extended():
    # mask done
    return illusions.checkerboard_sbc.domijan2015_extended()


if __name__ == "__main__":
    import math

    import matplotlib.pyplot as plt
    import numpy as np

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
