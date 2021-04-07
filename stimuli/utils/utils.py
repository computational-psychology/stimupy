"""
Provides some functionality for creating and manipulating visual stimuli
represented as numpy arrays.
"""
import numpy as np
from PIL import Image


def write_array_to_image(filename, arr):
    """
    Save a 2D numpy array as a grayscale image file.

    Parameters
    ----------
    filename : str
        full path to the file to be creaated.
    arr : np.ndarray
        2D numpy array
        The data to be stored in the image. Values will be cropped to [0,255].
    """
    if Image:
        imsize = arr.shape
        im = Image.new('L', (imsize[1], imsize[0]))
        im.putdata(arr.flatten())
        im.save(filename)


def luminance2munsell(lum_values, reference_white):
    """
    Transform luminance values into Munsell values.
    The luminance values do not have to correspond to specific units, as long
    as they are in the same unit as the reference white, because Munsell values
    are a perceptually uniform scale of relative luminances.

    Parameters
    ----------
    lum_values : numpy-array
    reference_white : number

    Returns
    -------
    munsell_values : numpy-array

    Reference: H. Pauli, "Proposed extension of the CIE recommendation
    on 'Uniform color spaces, color difference equations, and metric color
    terms'," J. Opt. Soc. Am. 66, 866-867 (1976)
    """

    x = lum_values / float(reference_white)
    idx = x <= (6. / 29) ** 3
    y1 = 841. / 108 * x[idx] + 4. / 29
    y2 = x[~idx] ** (1. / 3)
    y = np.empty(x.shape)
    y[idx] = y1
    y[~idx] = y2
    return 11.6 * y - 1.6


def munsell2luminance(munsell_values, reference_white):
    """
    Transform Munsell values to luminance values.
    The luminance values will be in the same unit as the reference white, which
    can be arbitrary as long as the scale is linear.

    Parameters
    ----------
    munsell_values : numpy-array
    reference_white : number

    Returns
    -------
    lum_values : numpy-array

    Reference: H. Pauli, "Proposed extension of the CIE recommendation
    on 'Uniform color spaces, color difference equations, and metric color
    terms'," J. Opt. Soc. Am. 66, 866-867 (1976)
    """
    lum_values = (munsell_values + 1.6) / 11.6
    idx = lum_values <= 6. / 29
    lum_values[idx] = (lum_values[idx] - 4. / 29) / 841 * 108
    lum_values[~idx] **= 3
    return lum_values * reference_white


def degrees_to_pixels(degrees, ppd):
    """
    convert degrees of visual angle to pixels, given the number of pixels in
    1deg of visual angle.

    Parameters
    ----------
    degrees : number or ndarray
              the degree values to be converted.
    ppd : number
          the number of pixels in the central 1 degree of visual angle.

    Returns
    -------
    pixels : number or ndarray
    """
    return np.tan(np.radians(degrees / 2.)) / np.tan(np.radians(.5)) * ppd


def pixels_to_degrees(pixels, ppd):
    """
    convert pixels to degrees of visual angle, given the number of pixels in
    1deg of visual angle.

    Parameters
    ----------
    pixels : number or ndarray
              the pixel values to be converted.
    ppd : number
          the number of pixels in the central 1 degree of visual angle.

    Returns
    -------
    degres : number or ndarray
    """
    return 2 * np.degrees(np.arctan(pixels * np.tan(np.radians(.5)) / ppd))


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
    mmpd = 2 * np.tan(np.radians(.5)) * distance
    return ppmm * mmpd


def pad_array(arr, amount, pad_value=0):
    """
    Pad array with an arbitrary value. So far, only works for 2D arrays.

    Parameters
    ----------
    arr : numpy ndarray
          the array to be padded
    amount : number or numpy ndarray
             the amount of padding in each direction. Has to be of shape
             len(arr.shape) X 2. the n-th row specifies the amount of padding
             to be added to the n-th dimension of arr. The first value is the
             amount of padding added before, the second value after the array.
             If amount is a single number, it is used for padding in all
             directions.
    pad_value : number, optional
                the value to be padded. Default is 0.

    Returns
    -------
    output : numpy ndarray
             the padded array
    """
    # if amount is a single number, use it for padding in all directions
    if type(amount) is int or type(amount) is float:
        amount = np.array(((amount, amount), (amount, amount)))
    assert amount.amin() >= 0
    if len(arr.shape) != 2:
        raise NotImplementedError(
            "pad_array currently only works for 2D arrays")
    if amount.sum() == 0:
        return arr

    output_shape = [x + y.sum() for x, y in zip(arr.shape, amount)]
    output = np.ones(output_shape, dtype=arr.dtype) * pad_value
    output[amount[0][0]:output_shape[0] - amount[0][1],
           amount[1][0]:output_shape[1] - amount[1][1]] = arr
    return output


def center_array(arr, shape, pad_value=0):
    """Center an array on a larger one. Selects appropriate pad amounts in
    every direction.

    Parameters
    ----------
    arr : numpy ndarray
          the array to be padded
    shape : tuple of two ints
            the shape of the desired output array. Must be at least as large as
            the input, and even for even input shapes, and odd for odd input
            shapes.
    pad_value : number, optional
                the value to be padded. Default is 0.

    Returns
    -------
    output : numpy ndarray
             the padded array
    """
    if arr.shape == shape:
        return arr
    y_pad, x_pad = np.asarray(shape) - arr.shape
    assert (y_pad % 2 == 0) and (x_pad % 2 == 0)
    assert x_pad > 0 and y_pad > 0
    out = np.ones(shape, dtype=arr.dtype) * pad_value
    out[y_pad / 2: -y_pad / 2, x_pad / 2: -x_pad / 2] = arr
    return out


def resize_array(arr, factor):
    """
    Return a copy of an array, resized by the given factor. Every value is
    repeated factor[d] times along dimension d.

    Parameters
    ----------
    arr : 2D array
          the array to be resized
    factor : tupel of 2 ints
             the resize factor in the y and x dimensions

    Returns
    -------
    An array of shape (arr.shape[0] * factor[0], arr.shape[1] * factor[1])
    """
    return np.repeat(np.repeat(arr, factor[0], axis=0), factor[1], axis=1)


def smooth_window(shape, plateau, min_val, max_val, width):
    """
    Return an array that smoothly falls of from max_val to min_val. Plateau
    specifies the location of max_val, width defines the width of the gradient,
    i.e. the number of pixels to reach min_val.
    TODO: only really works for unslanted rectangles, otherwise the inside of
    the plateau is not filled in!

    Parameters
    ----------
    shape : tuple of two ints
            the shape of the output array, (y,x)
    plateau : tuple of two-tuples ((y1, x1), ...)
              the corner points of the plateau, i.e the region where the output
              should be max_val. If two points are given, they are interpreted
              as the upper left and lower right corner of the plateau.
    min_val : number
              the value of the output array at all locations further than width
              from the plateau
    max_val : number
              the value of the output array at the plateau
    width : int
            the distance it takes for the gradient funcion to change from max
            to min.

    Returns
    -------
    mask : 2D array
    """
    x = np.arange(shape[1])[np.newaxis, :]
    y = np.arange(shape[0])[:, np.newaxis]
    distance = np.ones(shape) * width
    if len(plateau) == 2:
        plateau_points = (plateau[0], (plateau[0][0], plateau[1][1]), plateau[1],
                          (plateau[1][0], plateau[0][1]))
        distance[plateau[0][0]: plateau[1][0], plateau[0][1]: plateau[1][1]] = 0
    else:
        plateau_points = plateau
    for i in range(len(plateau_points)):
        p1 = plateau_points[i]
        p2 = plateau_points[(i + 1) % len(plateau_points)]
        distance = np.fmin(distance, dist_to_segment(y, x, p1, p2))
    distance = distance / width * np.pi
    mask = (np.cos(distance) + 1) / 2
    mask = mask * (max_val - min_val) + min_val

    return mask


def dist_squared(y, x, p):
    return (y - p[0]) ** 2 + (x - p[1]) ** 2


def dist_to_segment(y, x, p1, p2):  # x3,y3 is the point
    """
    Compute the distance between a point, (y,x), and a line segment between p1
    and p2.
    """
    y = np.atleast_1d(y)
    x = np.atleast_1d(x)
    sl = dist_squared(p1[0], p1[1], p2)
    if sl == 0:
        return np.sqrt(dist_squared(y, x, p1))
    t = ((y - p1[0]) * (p2[0] - p1[0]) + (x - p1[1]) * (p2[1] - p1[1])) / sl
    dist = dist_squared(y, x, (p1[0] + t * (p2[0] - p1[0]), p1[1] + t * (p2[1] - p1[1])))
    dist[t > 1] = dist_squared(y, x, p2)[t > 1]
    dist[t < 0] = dist_squared(y, x, p1)[t < 0]
    return np.sqrt(dist)
