import numpy as np
from stimuli.utils import degrees_to_pixels, pad_img
from stimuli.Stimulus import Stimulus


def checkerboard_contrast_contrast_effect(ppd=10, n_checks=8, check_size=1.0, target_length=4, padding=(1.0,1.0,1.0,1.0), check1=0., check2=2.,
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

    check_size_px = degrees_to_pixels(check_size, ppd)

    arr1 = np.ndarray((n_checks, n_checks))
    for i, j in np.ndindex((n_checks, n_checks)):
        arr1[i, j] = check1 if i % 2 == j % 2 else check2

    mask_arr1 = np.zeros((n_checks, n_checks))


    idx = np.zeros((n_checks, n_checks), dtype=bool)
    tpos = (n_checks - target_length) // 2
    idx[tpos:tpos + target_length, tpos:tpos + target_length] = True
    arr1[idx] = alpha * arr1[idx] + (1 - alpha) * tau
    mask_arr1[idx] = True

    arr2 = arr1.copy()
    arr2[~idx] = tau

    mask_arr2 = mask_arr1.copy()

    img1 = np.repeat(np.repeat(arr1, check_size_px, axis=0), check_size_px, axis=1)
    img1 = pad_img(img1, padding, ppd, tau)
    img2 = np.repeat(np.repeat(arr2, check_size_px, axis=0), check_size_px, axis=1)
    img2 = pad_img(img2, padding, ppd, tau)

    mask1 = np.repeat(np.repeat(mask_arr1, check_size_px, axis=0), check_size_px, axis=1)
    mask1 = pad_img(mask1, padding, ppd, 0)
    mask2 = np.repeat(np.repeat(mask_arr2, check_size_px, axis=0), check_size_px, axis=1)
    mask2 = pad_img(mask2, padding, ppd, 0)

    img = np.hstack([img1, img2])
    mask =  np.hstack([mask1, mask2])
    stim = Stimulus()
    stim.img = img
    stim.target_mask = mask

    return stim



def domijan2015():
    return checkerboard_contrast_contrast_effect(n_checks=8, check_size=10, target_length=4, padding=(9,11,9,11), check1=1.,
                                                 check2=9., tau=5, alpha= .5)

if __name__ == '__main__':
    import matplotlib.pyplot as plt
    img, mask = checkerboard_contrast_contrast_effect()
    plt.imshow(img, cmap='gray')
    plt.show()