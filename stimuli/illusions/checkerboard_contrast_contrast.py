import numpy as np


def checkerboard_contrast_contrast_effect(n_checks=8, check_size=10, target_length=4, padding=(10,10,10,10), check1=0., check2=2.,
                                          tau=.5, alpha=.5):
    """
    Contrast-contrast effect on checkerboard with square transparency layer.

    Parameters
    ----------
    n_checks: number of checks per board in each direction
    check_size: size of a check in px
    target_length: size of the target in # checks
    padding: 4-valued tuple specifying padding (top, bottom, left, right) in px
    check1: a check value
    check2: other check value
    tau: tau of transparency
    alpha: alpha of transparency

    Returns
    -------
    2D numpy array
    """

    padding_top, padding_bottom, padding_left, padding_right = padding
    padding_tuple = ((padding_top, padding_bottom), (padding_left, padding_right))

    arr1 = np.ndarray((n_checks, n_checks))
    for i, j in np.ndindex((n_checks, n_checks)):
        arr1[i, j] = check1 if i % 2 == j % 2 else check2

    idx = np.zeros((n_checks, n_checks), dtype=bool)
    tpos = (n_checks - target_length) // 2
    idx[tpos:tpos + target_length, tpos:tpos + target_length] = True
    arr1[idx] = alpha * arr1[idx] + (1 - alpha) * tau

    arr2 = arr1.copy()
    arr2[~idx] = tau

    img1 = np.repeat(np.repeat(arr1, check_size, axis=0), check_size, axis=1)
    img1 = np.pad(img1, padding_tuple, constant_values=tau, mode="constant")
    img2 = np.repeat(np.repeat(arr2, check_size, axis=0), check_size, axis=1)
    img2 = np.pad(img2, padding_tuple, constant_values=tau, mode="constant")

    return np.hstack([img1, img2])



def domijan2015():
    return checkerboard_contrast_contrast_effect(n_checks=8, check_size=10, target_length=4, padding=(9,11,9,11), check1=1.,
                                                 check2=9., tau=5, alpha= .5)
