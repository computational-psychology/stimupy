import numpy as np
import stimuli
from stimuli.utils import degrees_to_pixels, pad_img, plot_stim
from stimuli.Stimulus import Stimulus


def simultaneous_brightness_contrast(ppd=10, target_shape=(5,5), padding=(2,2,2,2), inner_padding=(3,3,3,3), left=1., right=0., target=.5):
    """
    Simultaneous brightness contrast

    Parameters
    ----------
    shape: shape of the stimulus in degrees visual angle (height,width)
    target_shape: target shape in degrees visual angle (height, width)
    padding: 4-valued tuple specifying padding (top, bottom, left, right) in degrees visual angle
    left: left background value
    right: right background value
    target: target value

    Returns
    -------
    2d numpy array
    """

    target_height, target_width = target_shape

    target_height_px, target_width_px = stimuli.utils.degrees_to_pixels(target_shape, ppd)

    img = np.ones((target_height_px, target_width_px)) * target
    mask = np.ones((target_height_px, target_width_px))

    img1 = pad_img(img, inner_padding, ppd, left)
    img2 = pad_img(img, inner_padding, ppd, right)
    img = np.hstack((img1, img2))

    mask1 = pad_img(mask, inner_padding, ppd, 0)
    mask2 = pad_img(mask, inner_padding, ppd, 0)
    mask = np.hstack((mask1, mask2*2))

    img = pad_img(img, padding, ppd, target)
    mask = pad_img(mask, padding, ppd, 0)

    stim = Stimulus()
    stim.img = img
    stim.target_mask = mask

    return stim


def domijan2015():
    return simultaneous_brightness_contrast(ppd=10, target_shape=(2.1,2.1), inner_padding=(3.9,4.0,3.9,4.0), padding=(0,0,0,0), left=9., right=1., target=5.)

def RHS2007_sbc_large():
    total_height, total_width, ppd = (32,)*3
    height, width = 12, 15
    target_height, target_width = 3,3

    inner_padding_vertical, inner_padding_horizontal = (height-target_height)/2, (width-target_width)/2
    inner_padding = (inner_padding_vertical, inner_padding_vertical, inner_padding_horizontal, inner_padding_horizontal)

    padding_vertical, padding_horizontal = (total_height - height)/2, (total_width - 2 * width)/2
    padding = (padding_vertical, padding_vertical, padding_horizontal, padding_horizontal)

    return stimuli.illusions.sbc.simultaneous_brightness_contrast(target_shape=(target_height, target_width), ppd=ppd, inner_padding=inner_padding, padding=padding)


def RHS2007_sbc_small():
    total_height, total_width, ppd = (32,)*3
    height, width = 12, 15
    target_height, target_width = 1,1

    inner_padding_vertical, inner_padding_horizontal = (height - target_height) / 2, (width - target_width) / 2
    inner_padding = (inner_padding_vertical, inner_padding_vertical, inner_padding_horizontal, inner_padding_horizontal)

    padding_vertical, padding_horizontal = (total_height - height) / 2, (total_width - 2 * width) / 2
    padding = (padding_vertical, padding_vertical, padding_horizontal, padding_horizontal)

    return stimuli.illusions.sbc.simultaneous_brightness_contrast(target_shape=(target_height, target_width), ppd=ppd, inner_padding=inner_padding, padding=padding)



if __name__ == '__main__':
    import matplotlib.pyplot as plt
    stim = simultaneous_brightness_contrast()
    plot_stim(stim, mask=True)


###################################
#      Simultaneous contrast      #
###################################
def simultaneous_contrast(n_grid, size_target, add_squares=False, size_squares=2,
                          seperate=False):
    # Inputs:
    #   - n_grid: height of the grid (int, unit: pixels)
    #   - size_target: size of target in one dimension (int, unit: pixels)
    #   - add_squares: if True, cover targets (partially) with squares (bool)
    #   - size_squares: size of the squares in one dimension (int, unit:pixels)
    #   - seperate: seperate the left and right half of the illusion by a gray
    #               area (bool)

    # Create the background:
    grid = np.zeros([n_grid, n_grid*2], dtype=np.float32)
    grid[:, n_grid:n_grid*2] = 1
    if seperate:
        # Optional: seperate black and white halfs by a gray area
        grid[:, n_grid-1:n_grid+1] = 0.5

    center = n_grid / 2
    # Ensure that the illusion looks symmetric:
    if size_target % 2 == 0:
        # Place targets on grid
        grid[int(center-size_target/2):int(center+size_target/2), int(center-size_target/2):int(center+size_target/2)] = 0.5
        grid[int(center-size_target/2):int(center+size_target/2), int(center+n_grid-size_target/2):int(center+n_grid+size_target/2)] = 0.5

        # Add covering squares:
        if add_squares:
            # Set a constant difference between the covering squares.
            # If you want them to be closer relative to the rest of the grid, increase
            # the grid size (n_grid)
            dist = 1
            grid[int(center-size_squares-dist):int(center-dist), int(center-size_squares-dist):int(center-dist)] = 1
            grid[int(center+dist):int(center+dist+size_squares), int(center+dist):int(center+dist+size_squares)] = 1
            grid[int(center-size_squares-dist):int(center-dist), int(center+dist):int(center+dist+size_squares)] = 1
            grid[int(center+dist):int(center+dist+size_squares), int(center-size_squares-dist):int(center-dist)] = 1
            grid[int(center-size_squares-dist):int(center-dist), int(center+n_grid-size_squares-dist):int(center+n_grid-dist)] = 0
            grid[int(center+dist):int(center+dist+size_squares), int(center+n_grid+dist):int(center+n_grid+dist+size_squares)] = 0
            grid[int(center-size_squares-dist):int(center-dist), int(center+n_grid+dist):int(center+n_grid+dist+size_squares)] = 0
            grid[int(center+dist):int(center+dist+size_squares), int(center+n_grid-size_squares-dist):int(center+n_grid-dist)] = 0

            # If the target is much bigger than the covering squares, "cut" the
            # overlap, so the target looks like a cross
            if size_target > (size_squares*2 + dist):
                grid[int(0):int(center-size_squares-dist), int(0):int(center-dist)] = 0
                grid[int(0):int(center-size_squares-dist), int(center+dist):int(n_grid)] = 0
                grid[int(center+size_squares+dist)::, int(0):int(center-dist)] = 0
                grid[int(center+size_squares+dist)::, int(center+dist):int(n_grid)] = 0
                grid[int(0):int(center-dist), int(0):int(center-dist-size_squares)] = 0
                grid[int(0):int(center-dist), int(center+dist+size_squares):int(n_grid)] = 0
                grid[int(center+dist)::, int(0):int(center-dist-size_squares)] = 0
                grid[int(center+dist)::, int(center+dist+size_squares):int(n_grid)] = 0

                grid[int(0):int(center-size_squares-dist), int(n_grid):int(center+n_grid-dist)] = 1
                grid[int(0):int(center-size_squares-dist), int(center+n_grid+dist)::] = 1
                grid[int(center+size_squares+dist)::, int(n_grid):int(center+n_grid-dist)] = 1
                grid[int(center+size_squares+dist)::, int(center+n_grid+dist)::] = 1
                grid[int(0):int(center-dist), int(n_grid):int(center+n_grid+-dist-size_squares)] = 1
                grid[int(0):int(center-dist), int(center+n_grid+dist+size_squares)::] = 1
                grid[int(center+dist)::, int(n_grid):int(center+n_grid-dist-size_squares)] = 1
                grid[int(center+dist)::, int(center+n_grid+dist+size_squares)::] = 1

        else:
            grid[int(center-size_target/2):int(center+size_target/2), int(center-size_target/2):int(center+size_target/2)] = 0.5
            grid[int(center-size_target/2):int(center+size_target/2), int(center+n_grid-size_target/2):int(center+n_grid+size_target/2)] = 0.5

    else:
        # Place targets on grid
        grid[int(center-size_target/2):int(center+1+size_target/2), int(center-size_target/2):int(center+1+size_target/2)] = 0.5
        grid[int(center-size_target/2):int(center+1+size_target/2), int(center+n_grid-size_target/2):int(center+1+n_grid+size_target/2)] = 0.5
        if add_squares:
            # Set a constant difference between the covering squares.
            # If you want them to be closer relative to the rest of the grid, increase
            # the grid size (n_grid)
            dist = 2
            dist = dist/2
            grid[int(center+1-size_squares-dist):int(center+1-dist), int(center+1-size_squares-dist):int(center+1-dist)] = 1
            grid[int(center+dist):int(center+dist+size_squares), int(center+dist):int(center+dist+size_squares)] = 1
            grid[int(center+1-size_squares-dist):int(center+1-dist), int(center+dist):int(center+dist+size_squares)] = 1
            grid[int(center+dist):int(center+dist+size_squares), int(center+1-size_squares-dist):int(center+1-dist)] = 1
            grid[int(center+1-size_squares-dist):int(center+1-dist), int(center+1+n_grid-size_squares-dist):int(center+1+n_grid-dist)] = 0
            grid[int(center+dist):int(center+dist+size_squares), int(center+n_grid+dist):int(center+n_grid+dist+size_squares)] = 0
            grid[int(center+1-size_squares-dist):int(center+1-dist), int(center+n_grid+dist):int(center+n_grid+dist+size_squares)] = 0
            grid[int(center+dist):int(center+dist+size_squares), int(center+1+n_grid-size_squares-dist):int(center+1+n_grid-dist)] = 0

            # If the target is much bigger than the covering squares, "cut" the
            # overlap, so the target looks like a cross
            if size_target > (size_squares*2 + dist):
                grid[int(0):int(center-size_squares-dist+1), int(0):int(center-dist+1)] = 0
                grid[int(0):int(center-size_squares-dist+1), int(center+dist):int(n_grid)] = 0
                grid[int(center+size_squares+dist)::, int(0):int(center-dist+1)] = 0
                grid[int(center+size_squares+dist)::, int(center+dist):int(n_grid)] = 0
                grid[int(0):int(center-dist+1), int(0):int(center-dist-size_squares+1)] = 0
                grid[int(0):int(center-dist+1), int(center+dist+size_squares):int(n_grid)] = 0
                grid[int(center+dist)::, int(0):int(center-dist-size_squares+1)] = 0
                grid[int(center+dist)::, int(center+dist+size_squares):int(n_grid)] = 0

                grid[int(0):int(center-size_squares-dist+1), int(n_grid):int(center+n_grid-dist+1)] = 1
                grid[int(0):int(center-size_squares-dist+1), int(center+n_grid+dist)::] = 1
                grid[int(center+size_squares+dist)::, int(n_grid):int(center+n_grid-dist+1)] = 1
                grid[int(center+size_squares+dist)::, int(center+n_grid+dist)::] = 1
                grid[int(0):int(center-dist+1), int(n_grid):int(center+n_grid+-dist-size_squares+1)] = 1
                grid[int(0):int(center-dist+1), int(center+n_grid+dist+size_squares)::] = 1
                grid[int(center+dist)::, int(n_grid):int(center+n_grid-dist-size_squares+1)] = 1
                grid[int(center+dist)::, int(center+n_grid+dist+size_squares)::] = 1
    return grid

