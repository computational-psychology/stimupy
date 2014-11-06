"""
Provides some functionality for creating and manipulating visual stimuli
represented as numpy arrays.
"""
import numpy as np
try:
    import Image
except ImportError:
    print "Could not import Image, utils.write_array_to_image will not work."
    Image = None

def write_array_to_image(filename, arr):
    """
    Save a 2D numpy array as a grayscale image file.

    Parameters
    ----------
    filename : str
               full path to the file to be creaated.
    arr : 2D numpy array
          The data to be stored in the image. Values will be cropped to
          [0,255].
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
    assert amount.min() >=0
    if len(arr.shape) != 2:
        raise NotImplementedError(
                        "pad_array currently only works for 2D arrays")
    if amount.sum() == 0:
        return arr

    output_shape = [x + y.sum() for x, y in zip(arr.shape, amount)]
    output = np.ones(output_shape, dtype = arr.dtype) * pad_value
    output[amount[0][0]:output_shape[0] - amount[0][1],
           amount[1][0]:output_shape[1] - amount[1][1]] = arr
    return output

def center_array(arr, shape, pad_value=0):
    if arr.shape == shape: return arr
    y_pad, x_pad = np.asarray(shape) - arr.shape
    assert (y_pad % 2 == 0) and (x_pad % 2 == 0)
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
    x_idx = np.arange(0, arr.shape[1], 1. / factor[1]).astype(int)
    y_idx = np.arange(0, arr.shape[0], 1. / factor[0]).astype(int)
    return arr[:, x_idx][y_idx, :]
