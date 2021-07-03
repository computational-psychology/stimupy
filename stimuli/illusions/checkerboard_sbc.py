import numpy as np
from stimuli.utils import degrees_to_pixels, pad_img
from stimuli.Stimulus import Stimulus

def checkerboard_contrast(ppd=10, n_checks=8, check_size=1.0, target1_coords=(3, 2), target2_coords=(5, 5), extend_targets=False,
                          padding=(1.0,1.0,1.0,1.0), check1=0., check2=1., target=.5):
    """
    Checkerboard Contrast

    Parameters
    ----------
    n_checks: number of checks per board in each direction
    check_size: size of a check in px
    target1_coords: check-coordinates of target check 1
    target2_coords: check-coordinates of target check 2
    extend_targets: cross targets instead of single-check targets
    padding: 4-valued tuple specifying padding (top, bottom, left, right) in px
    check1: a check value
    check2: other check value
    target: target value

    Returns
    -------

    """

    check_size_px = degrees_to_pixels(check_size, ppd)

    arr = np.ndarray((n_checks, n_checks))
    mask = np.zeros((n_checks, n_checks))

    for i, j in np.ndindex((n_checks, n_checks)):
        arr[i, j] = check1 if i % 2 == j % 2 else check2

    arr[target1_coords] = target
    arr[target2_coords] = target

    mask[target1_coords] = True
    mask[target2_coords] = True

    if extend_targets:
        for idx in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            arr[target1_coords[0] + idx[0], target1_coords[1] + idx[1]] = target
            arr[target2_coords[0] + idx[0], target2_coords[1] + idx[1]] = target

            mask[target1_coords[0] + idx[0], target1_coords[1] + idx[1]] = True
            mask[target2_coords[0] + idx[0], target2_coords[1] + idx[1]] = True

    img = np.repeat(np.repeat(arr, check_size_px, axis=0), check_size_px, axis=1)
    mask = np.repeat(np.repeat(mask, check_size_px, axis=0), check_size_px, axis=1)

    img = pad_img(img, padding, ppd, (check1+check2)/2)
    mask = pad_img(mask, padding, ppd, 0)

    stim = Stimulus()
    stim.img = img
    stim.target_mask = mask

    return stim


def domijan2015():
    return checkerboard_contrast(ppd=10, n_checks=8, check_size=1.0, target1_coords=(3, 2), target2_coords=(5, 5), extend_targets=False, padding=(.9,1.1,.9,1.1), check1=1., check2=9., target=5.)

def domijan2015_extended():
    return checkerboard_contrast(ppd=10, n_checks=8, check_size=1.0, target1_coords=(3, 2), target2_coords=(5, 5), extend_targets=True, padding=(.9,1.1,.9,1.1), check1=1., check2=9., target=5.)


if __name__ == '__main__':
    import matplotlib.pyplot as plt
    img, mask = checkerboard_contrast()
    plt.imshow(img, cmap='gray')
    plt.show()