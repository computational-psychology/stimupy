"""
Provides some functionality for creating and manipulating visual stimuli
represented as numpy arrays.
"""

import warnings
import numpy as np


def shift_pixels(img, shift):
    """
    Shift image by specified number of pixels. The pixels pushed on the edge will reappear on the other side (wrap around)

    Parameters
    ----------
    img : 2D array representing the image to be shifted
    shift: (x,y) tuple specifying the number of pixels to shift. Positive x specifies shift in the right direction
        and positive y shift downwards

    Returns
    -------
    img : shifted image
    """
    return np.roll(img, shift, (1, 0))


def round_to_vals(input_arr, vals):
    n_val = len(vals)
    input_arr = np.repeat(np.expand_dims(input_arr, -1), n_val, axis=2)
    vals_arr = np.ones(input_arr.shape) * np.array(np.expand_dims(vals, [0, 1]))

    indices = np.argmin(np.abs(input_arr - vals_arr), axis=2)
    out_arr = np.copy(indices).astype(float)

    for i in range(n_val):
        out_arr[indices == i] = vals[i]
    return out_arr


def to_img(array, save):
    from PIL import Image

    if array.min() < 0:
        array = array - array.min()
    if array.max() > 1:
        array = array / array.max()
    array = (array * 255).astype(np.uint8)

    im = Image.fromarray(array)

    try:
        im.save(save)
    except ValueError:
        warnings.warn("No file extension provided, saving as png")
        im.save(save + ".png", "PNG")


def int_factorize(n):
    """All integer factors of integer n

    All integer factors, i.e., all integers that n is integer-divisible by.
    Also not a very efficient algorithm (brute force trial division),
    so should only be used as a helpter function.

    Parameters
    ----------
    n : int
        number to factorize

    Returns
    -------
    set
        set of all integer factors of n
    """

    factors = {1}  # set, guarantees unique factors
    for i in range(2, int(np.sqrt(n)) + 1):
        if n % i == 0:
            # N is divisible by i...
            factors.add(i)
            # ...thus also divisible by n/i
            factors.add(n // i)

    return factors
