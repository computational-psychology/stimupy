import numpy as np


def checkerboard_contrast(n_checks=8, check_size=10, target1_coords=(3, 2), target2_coords=(5, 5), extend_targets=False,
                          padding=10, check1=0., check2=1., target=.5):
    """
    Checkerboard Contrast

    Parameters
    ----------
    n_checks: number of checks per board in each direction
    check_size: size of a check in px
    target1_coords: check-coordinates of target check 1
    target2_coords: check-coordinates of target check 2
    extend_targets: cross targets instead of single-check targets
    padding: around board in px
    check1: a check value
    check2: other check value
    target: target value

    Returns
    -------

    """
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
    img = np.pad(img, padding, constant_values=((check1 + check2) / 2), mode="constant")

    return img


def domijan2015():
    return checkerboard_contrast(n_checks=8, check_size=10, target1_coords=(3, 2), target2_coords=(5, 5), extend_targets=False, padding=10, check1=1., check2=9., target=5.)


def lynn_domijan2015():
    """
       there's one pixel translation between the stimuli package and utils generated inputs
       (see pixels [9,9] and [10,10] in reults from this and previous functions)
    """
    lum_white = 9.
    lum_black = 1.
    lum_gray = 5.

    input_image = lum_gray * np.ones([100, 100])
    input_image[9:89, 9:89] = lum_white

    for i in range(9, 80, 20):
        for j in range(9, 80, 20):
            input_image[i:i + 10, j:j + 10] = lum_black
            k, l = i + 10, j + 10
            input_image[k:k + 10, l:l + 10] = lum_black

    input_image[39:49, 29:39] = lum_gray
    input_image[59:69, 59:69] = lum_gray

    return input_image


