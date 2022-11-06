"""
Provides some functionality for creating and manipulating visual stimuli
represented as numpy arrays.
"""

import numpy as np


def degrees_to_pixels(degrees, ppd):
    """
    convert degrees of visual angle to pixels, given the number of pixels in
    1deg of visual angle.

    Parameters
    ----------
    degrees : number, tuple, list or a ndarray
              the degree values to be converted.
    ppd : number
          the number of pixels in the central 1 degree of visual angle.

    Returns
    -------
    pixels : number or ndarray
    """
    degrees = np.array(degrees)
    return (np.round(degrees * ppd)).astype(int)

    # This is the 'super correct' conversion, but it makes very little difference in practice
    # return (np.tan(np.radians(degrees / 2.)) / np.tan(np.radians(.5)) * ppd).astype(int)


def compute_ppd(screen_size, resolution, distance):
    """
    Compute the pixels per degree, i.e. the number of pixels in the central
    one degree of visual angle, in a presentation setup.

    Parameters
    ----------
    screen_size : scalar
                  the size of the presentation screen, in whatever unti you
                  prefer.
    resolution : scalar
                 the sceen resolution in the same direction that screen size
                 was measured in.
    distance : scalar
               the distance between the observer and the screen, in the same
               unit as screen_size.
    Returns
    -------
    ppd : number
          the number of pixels in one degree of visual angle.
    """

    ppmm = resolution / screen_size
    mmpd = 2 * np.tan(np.radians(0.5)) * distance
    return ppmm * mmpd


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


def adapt_mc(stimulus, mc=1.0, mean_lum=0.5):
    # Adapt Michelson contrast
    stimulus = (stimulus - stimulus.min()) / (stimulus.max() - stimulus.min())
    stimulus = (stimulus * mc * 2.0 * mean_lum) + (mean_lum - mc * mean_lum)
    return stimulus


def round_to_vals(input_arr, vals):
    n_val = len(vals)
    input_arr = np.repeat(np.expand_dims(input_arr, -1), n_val, axis=2)
    vals_arr = np.ones(input_arr.shape) * np.array(np.expand_dims(vals, [0, 1]))

    indices = np.argmin(np.abs(input_arr - vals_arr), axis=2)
    out_arr = np.copy(indices).astype(float)

    for i in range(n_val):
        out_arr[indices == i] = vals[i]
    return out_arr
