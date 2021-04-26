import numpy as np


def simultaneous_brightness_contrast(input_size=100, target_size=20, left=1., right=0., target=.5):
    """
    Simultaneous brightness contrast

    Parameters
    ----------
    input_size: height of the input (and half of the width) in px
    target_size: height and width of the centred target square in px
    left: left background value
    right: right background value
    target: target value

    Returns
    -------
    2d numpy array
    """
    img1 = np.ones((input_size, input_size)) * left
    img2 = np.ones((input_size, input_size)) * right

    tpos = (input_size-target_size)//2
    img1[tpos:tpos+target_size, tpos:tpos+target_size] = target
    img2[tpos:tpos+target_size, tpos:tpos+target_size] = target

    return np.hstack([img1, img2])


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
