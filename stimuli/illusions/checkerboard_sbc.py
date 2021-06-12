import numpy as np
from stimuli import utils

def checkerboard_contrast(n_checks=8, check_size=10, target1_coords=(3, 2), target2_coords=(5, 5), extend_targets=False,
                          padding=(10,10,10,10), check1=0., check2=1., target=.5):
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

    padding_top, padding_bottom, padding_left, padding_right = padding

    arr = np.ndarray((n_checks, n_checks))
    for i, j in np.ndindex((n_checks, n_checks)):
        arr[i, j] = check1 if i % 2 == j % 2 else check2

    arr[target1_coords] = target
    arr[target2_coords] = target
    if extend_targets:
        for idx in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            arr[target1_coords[0] + idx[0], target1_coords[1] + idx[1]] = target
            arr[target2_coords[0] + idx[0], target2_coords[1] + idx[1]] = target

    img = np.repeat(np.repeat(arr, check_size, axis=0), check_size, axis=1)
    img = np.pad(img, ((padding_top, padding_bottom), (padding_left, padding_right)), constant_values=((check1 + check2) / 2), mode="constant")

    return img


def domijan2015():
    return checkerboard_contrast(n_checks=8, check_size=10, target1_coords=(3, 2), target2_coords=(5, 5), extend_targets=False, padding=(9,11,9,11), check1=1., check2=9., target=5.)

