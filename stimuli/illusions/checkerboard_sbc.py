import numpy as np
import stimuli.illusions
from stimuli.utils import degrees_to_pixels, pad_img, plot_stim
from stimuli.Stimulus import Stimulus

def checkerboard_contrast(ppd=10, board_shape=(8,8), check_size=1.0, target1_coords=(3, 2), target2_coords=(5, 5), extend_targets=False,
                          padding=(1.0,1.0,1.0,1.0), check1=0., check2=1., target=.5):
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

    img = pad_img(img, padding, ppd, (check1+check2)/2)
    mask = pad_img(mask, padding, ppd, 0)

    stim = Stimulus()
    stim.img = img
    stim.target_mask = mask

    return stim


def domijan2015():
    return checkerboard_contrast(ppd=10, board_shape=(8,8), check_size=1.0, target1_coords=(3, 2), target2_coords=(5, 5), extend_targets=False, padding=(.9,1.1,.9,1.1), check1=1., check2=9., target=5.)

def domijan2015_extended():
    return checkerboard_contrast(ppd=10, board_shape=(8,8), check_size=1.0, target1_coords=(3, 2), target2_coords=(5, 5), extend_targets=True, padding=(.9,1.1,.9,1.1), check1=1., check2=9., target=5.)

def RHS2007_Checkerboard016():
    total_height, total_width, ppd = (32,) * 3
    height_checks, width_checks = 40, 102
    check_height, check_width = 32/102, 32/102
    board_shape = (height_checks, width_checks)
    height, width = check_height*height_checks, check_width*width_checks
    padding_horizontal = (total_width - width) / 2
    padding_vertical = (total_height - height) / 2
    padding = (padding_vertical, padding_vertical, padding_horizontal, padding_horizontal)
    img = stimuli.illusions.checkerboard_contrast(ppd=ppd, board_shape=board_shape, check_size=check_height, target1_coords=(20, 17), target2_coords=(20, 86),
                                                  extend_targets=False, padding=padding, check1=0, check2=1, target=.5)
    return img



def RHS2007_Checkerboard0938():
    total_height, total_width, ppd = (32,) * 3
    height_checks, width_checks = 7, 25
    check_height, check_width = 0.938, 0.938
    board_shape = (height_checks, width_checks)
    height, width = check_height*height_checks, check_width*width_checks
    padding_horizontal = (total_width - width) / 2
    padding_vertical = (total_height - height) / 2
    padding = (padding_vertical, padding_vertical, padding_horizontal, padding_horizontal)
    target_height = height_checks //2
    img = stimuli.illusions.checkerboard_contrast(ppd=ppd, board_shape=board_shape, check_size=check_height, target1_coords=(target_height, 6), target2_coords=(target_height, 17),
                                                  extend_targets=False, padding=padding, check1=0, check2=1, target=.5)
    return img



def RHS2007_Checkerboard209():
    total_height, total_width, ppd = (32,) * 3
    height_checks, width_checks = 3, 10
    check_height, check_width = 2.09, 2.09
    board_shape = (height_checks, width_checks)
    height, width = check_height*height_checks, check_width*width_checks
    padding_horizontal = (total_width - width) / 2
    padding_vertical = (total_height - height) / 2
    padding = (padding_vertical, padding_vertical, padding_horizontal, padding_horizontal)
    target_height = height_checks //2
    img = stimuli.illusions.checkerboard_contrast(ppd=ppd, board_shape=board_shape, check_size=check_height, target1_coords=(target_height, 2), target2_coords=(target_height, 7),
                                                  extend_targets=False, padding=padding, check1=0, check2=1, target=.5)
    return img



if __name__ == '__main__':
    import matplotlib.pyplot as plt
    stim = checkerboard_contrast()
    plt.figure()
    plot_stim(stim, mask=True)