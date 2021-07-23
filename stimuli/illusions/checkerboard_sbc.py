import numpy as np
from stimuli.utils import degrees_to_pixels, pad_img, pad_img_to_shape, plot_stim
from stimuli.Stimulus import Stimulus
import matplotlib.pyplot as plt


def checkerboard_contrast(ppd=10, board_shape=(8,8), check_size=1.0, target1_coords=(3, 2), target2_coords=(5, 5), extend_targets=False,
                         check1=0., check2=1., target=.5):
    """
    Checkerboard Contrast

    Parameters
    ----------
    board shape: number of checks per board in y, x direction
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
    height_checks, width_checks = board_shape

    arr = np.ndarray((height_checks, width_checks))
    mask = np.zeros((height_checks, width_checks))

    for i, j in np.ndindex((height_checks, width_checks)):
        arr[i, j] = check1 if i % 2 == j % 2 else check2

    arr[target1_coords] = target
    arr[target2_coords] = target

    mask[target1_coords] = 1
    mask[target2_coords] = 2

    if extend_targets:
        for idx in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            arr[target1_coords[0] + idx[0], target1_coords[1] + idx[1]] = target
            arr[target2_coords[0] + idx[0], target2_coords[1] + idx[1]] = target

            mask[target1_coords[0] + idx[0], target1_coords[1] + idx[1]] = 1
            mask[target2_coords[0] + idx[0], target2_coords[1] + idx[1]] = 2

    img = np.repeat(np.repeat(arr, check_size_px, axis=0), check_size_px, axis=1)
    mask = np.repeat(np.repeat(mask, check_size_px, axis=0), check_size_px, axis=1)

    stim = Stimulus()
    stim.img = img
    stim.target_mask = mask

    return stim


def domijan2015():
    stim = checkerboard_contrast(ppd=10, board_shape=(8,8), check_size=1.0, target1_coords=(3, 2), target2_coords=(5, 5), extend_targets=False, check1=1., check2=9., target=5.)
    padding = (.9, 1.1, .9, 1.1)
    stim.img = pad_img(stim.img, padding, ppd=10, val=5.)
    stim.target_mask = pad_img(stim.target_mask, padding, ppd=10, val=0)
    return stim


def domijan2015_extended():
    stim = checkerboard_contrast(ppd=10, board_shape=(8,8), check_size=1.0, target1_coords=(3, 2), target2_coords=(5, 5), extend_targets=True, check1=1., check2=9., target=5.)
    padding = (.9, 1.1, .9, 1.1)
    stim.img = pad_img(stim.img, padding, ppd=10, val=5.)
    stim.target_mask = pad_img(stim.target_mask, padding, ppd=10, val=0)
    return stim


def RHS2007_Checkerboard016():
    total_height, total_width, ppd = (32,) * 3
    height_checks, width_checks = 40, 102
    check_height = 32/102
    board_shape = (height_checks, width_checks)

    check1, check2, target = 1, 0, .5
    target_height = height_checks // 2
    stim = checkerboard_contrast(ppd=ppd, board_shape=board_shape, check_size=check_height, target1_coords=(target_height, 16), target2_coords=(target_height, 85),
                                 extend_targets=False, check1=check1, check2=check2, target=target)

    stim.img = pad_img_to_shape(stim.img, (1024, 1024), val=target)
    stim.target_mask = pad_img_to_shape(stim.target_mask, (1024, 1024), val=0)

    return stim


def RHS2007_Checkerboard0938():
    total_height, total_width, ppd = (32,) * 3
    height_checks, width_checks = 7, 25
    check_height = 0.938
    board_shape = (height_checks, width_checks)

    check1, check2, target = 0, 1, .5
    target_height = height_checks // 2
    stim = checkerboard_contrast(ppd=ppd, board_shape=board_shape, check_size=check_height, target1_coords=(target_height, 6), target2_coords=(target_height, 17),
                                 extend_targets=False, check1=check1, check2=check2, target=target)
    stim.img = pad_img_to_shape(stim.img, (1024, 1024), val=target)
    stim.target_mask = pad_img_to_shape(stim.target_mask, (1024, 1024), val=0)

    return stim


def RHS2007_Checkerboard209():
    total_height, total_width, ppd = (32,) * 3
    height_checks, width_checks = 3, 10
    check_height = 2.09
    board_shape = (height_checks, width_checks)

    check1, check2, target = 0, 1, .5
    target_height = height_checks // 2
    stim = checkerboard_contrast(ppd=ppd, board_shape=board_shape, check_size=check_height, target1_coords=(target_height, 2), target2_coords=(target_height, 7),
                                 extend_targets=False, check1=check1, check2=check2, target=target)
    stim.img = pad_img_to_shape(stim.img, (1024, 1024), val=target)
    stim.target_mask = pad_img_to_shape(stim.target_mask, (1024, 1024), val=0)

    return stim


if __name__ == '__main__':
    img1 = RHS2007_Checkerboard016()
    img2 = RHS2007_Checkerboard0938()
    img3 = RHS2007_Checkerboard209()

    stim = checkerboard_contrast()
    plt.figure()
    plot_stim(stim, mask=True)
