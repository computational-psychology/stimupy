import math
from stimuli import illusions
import numpy as np

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
    #TODO: add mask
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
    #TODO: add mask
    return illusions.checkerboard_contrast_contrast.domijan2015()

def checkerboard():
    # mask done
    return illusions.checkerboard_sbc.domijan2015()

def checkerboard_extended():
    # mask done
    return illusions.checkerboard_sbc.domijan2015_extended()



if __name__ == "__main__":
    import matplotlib.pyplot as plt
    plot_all = True
    if plot_all:
        stims = {
            "dungeon": dungeon,
            "cube": cube,
            "grating": grating,
            "rings": rings,
            "bullseye": bullseye,
            "simultaneous_brightness_contrast": simultaneous_brightness_contrast,
            "white": white,
            "benary": benary,
            "todorovic": todorovic,
            "checkerboard_contrast_contrast": checkerboard_contrast_contrast,
            "checkerboard": checkerboard,
            "checkerboard_extended": checkerboard_extended,
        }

        a = math.ceil(math.sqrt(len(stims)))
        plt.figure(figsize=(a * 3, a * 3))
        for i, (stim_name, stim) in enumerate(stims.items()):
            print("Generating", stim_name + "")
            st = stim()
            img, mask = st["img"], st["mask"]
            img = np.dstack([img, img, img])

            mask = np.insert(np.expand_dims(mask, 2), 1, 0, axis=2)
            mask = np.insert(mask, 2, 0, axis=2)
            final = mask + img
            final /= np.max(final)

            plt.subplot(a, a, i + 1)
            plt.title(stim_name + " - img")
            plt.imshow(final)

        plt.tight_layout()

    else:
        plt.imshow(img, cmap='gray')

    plt.savefig("overview_domijan2015.png")
    plt.show()