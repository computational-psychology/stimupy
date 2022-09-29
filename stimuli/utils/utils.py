"""
Provides some functionality for creating and manipulating visual stimuli
represented as numpy arrays.
"""
import matplotlib.pyplot as plt
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
        im = Image.new("L", (imsize[1], imsize[0]))
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
    idx = x <= (6.0 / 29) ** 3
    y1 = 841.0 / 108 * x[idx] + 4.0 / 29
    y2 = x[~idx] ** (1.0 / 3)
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
    idx = lum_values <= 6.0 / 29
    lum_values[idx] = (lum_values[idx] - 4.0 / 29) / 841 * 108
    lum_values[~idx] **= 3
    return lum_values * reference_white


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


def pixels_to_degrees(pixels, ppd):
    """
    convert pixels to degrees of visual angle, given the number of pixels in
    1deg of visual angle.

    Parameters
    ----------
    pixels : number, tuple, list or a ndarray
              the pixel values to be converted.
    ppd : number
          the number of pixels in the central 1 degree of visual angle.

    Returns
    -------
    degres : number or ndarray
    """
    pixels = np.array(pixels)
    return pixels / ppd
    # This is the 'super correct' conversion, but it makes very little difference in practice
    # return 2 * np.degrees(np.arctan(pixels * np.tan(np.radians(.5)) / ppd))


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
        raise NotImplementedError("pad_array currently only works for 2D arrays")
    if amount.sum() == 0:
        return arr

    output_shape = [x + y.sum() for x, y in zip(arr.shape, amount)]
    output = np.ones(output_shape, dtype=arr.dtype) * pad_value
    output[
        amount[0][0] : output_shape[0] - amount[0][1],
        amount[1][0] : output_shape[1] - amount[1][1],
    ] = arr
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
    out[y_pad / 2 : -y_pad / 2, x_pad / 2 : -x_pad / 2] = arr
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
        plateau_points = (
            plateau[0],
            (plateau[0][0], plateau[1][1]),
            plateau[1],
            (plateau[1][0], plateau[0][1]),
        )
        distance[plateau[0][0] : plateau[1][0], plateau[0][1] : plateau[1][1]] = 0
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
    dist = dist_squared(
        y, x, (p1[0] + t * (p2[0] - p1[0]), p1[1] + t * (p2[1] - p1[1]))
    )
    dist[t > 1] = dist_squared(y, x, p2)[t > 1]
    dist[t < 0] = dist_squared(y, x, p1)[t < 0]
    return np.sqrt(dist)


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


def get_circle_indices(n_numbers, grid_shape):

    height, width = grid_shape

    x = np.linspace(0, 2 * np.pi, n_numbers)

    xx = np.cos(x)
    xx_min = np.abs(xx.min())
    xx += xx_min
    xx_max = xx.max()
    xx = xx / xx_max * (width - 1)

    yy = np.sin(x)
    yy_min = np.abs(yy.min())
    yy += yy_min
    yy_max = yy.max()
    yy = yy / yy_max * (height - 1)

    return (yy, xx)


def get_circle_mask(shape, center, radius):
    """
    Get a circle shaped mask

    Parameters
    -------
    shape: (height, width) of the mask in pixels
    center: (y_center, x_center) in pixels
    radius: radius of the circle in pixels

    Returns
    -------
    mask: 2D boolean numpy array
    """
    height, width = shape
    y_c, x_c = center

    xx, yy = np.mgrid[:height, :width]
    grid_radii = (xx - x_c) ** 2 + (yy - y_c) ** 2

    circle_mask = grid_radii < (radius**2)

    return circle_mask


def get_annulus_mask(shape, center, inner_radius, outer_radius):
    """
    Get an annulus shaped mask

    Parameters
    -------
    shape: (height, width) of the mask in pixels
    radius: radius of the circle in pixels
    center: width of the annulus in pixels

    Returns
    -------
    mask: 2D boolean numpy array
    """

    mask1 = get_circle_mask(shape, center, inner_radius)
    mask2 = get_circle_mask(shape, center, outer_radius)
    mask = np.logical_xor(mask1, mask2)

    return mask


def pad_img(img, padding, ppd, val):
    """
    padding: degrees visual angle (top, bottom, left, right)
    """
    padding_px = np.array(degrees_to_pixels(padding, ppd), dtype=np.int32)
    padding_top, padding_bottom, padding_left, padding_right = padding_px
    return np.pad(
        img,
        (
            (int(padding_top), int(padding_bottom)),
            (int(padding_left), int(padding_right)),
        ),
        "constant",
        constant_values=((val, val), (val, val)),
    )


def pad_img_to_shape(img, shape, val=0):
    """
    shape: shape of the resulting image in pixels (height, width)
    """
    height_px, width_px = shape
    height_img_px, width_img_px = img.shape
    if height_img_px > height_px or width_img_px > width_px:
        raise ValueError("the image is bigger than the size after padding")

    padding_vertical_top = int((height_px - height_img_px) // 2)
    padding_vertical_bottom = int(height_px - height_img_px - padding_vertical_top)

    padding_horizontal_left = int((width_px - width_img_px) // 2)
    padding_horizontal_right = int(width_px - width_img_px - padding_horizontal_left)

    return np.pad(
        img,
        (
            (padding_vertical_top, padding_vertical_bottom),
            (padding_horizontal_left, padding_horizontal_right),
        ),
        "constant",
        constant_values=val,
    )


def compare_plots(plots):
    M = len(plots)
    for i, (plot_name, plot) in enumerate(plots.items()):
        plt.subplot(1, M, i + 1)
        plt.title(plot_name)
        plt.imshow(plot, cmap="gray")
    plt.show()


def plot_stim(stim, mask=False, stim_name="stim", ax=None):
    if ax is None:
        ax = plt.gca()

    if not mask:
        ax.imshow(stim["img"], cmap="gray")
    else:
        img, mask = stim["img"], stim["mask"]
        img = np.dstack([img, img, img])

        mask = np.insert(np.expand_dims(mask, 2), 1, 0, axis=2)
        mask = np.insert(mask, 2, 0, axis=2)
        final = mask + img
        final /= np.max(final)
        ax.imshow(final)

    ax.set_title(label=stim_name)
    return ax


def plot_stimuli(stims, mask=False):
    import math

    # Plot each stimulus+mask
    n_stim = math.ceil(math.sqrt(len(stims)))
    F = plt.figure(figsize=(n_stim * 3, n_stim * 3))
    for i, (stim_name, stim) in enumerate(stims.items()):
        ax = F.add_subplot(n_stim, n_stim, i + 1)
        plot_stim(stim, mask, stim_name=stim_name, ax=ax)

    plt.tight_layout()
    plt.show()


###################################
#          Lynns utils            #
###################################
def randomize_sign(array):
    """Helper function that randomizes the sign of values in an array.

    Parameters
    ----------
    array
        N-dimensional array

    Returns
    -------
    array
        Same array with randomized signs

    """
    sign = np.random.rand(*array.shape) - 0.5
    sign[sign <= 0.0] = -1.0
    sign[sign > 0.0] = 1.0
    array = array * sign
    return array


# Calculate peak frequency and boundaries for bandwidth
def filter_statistics(f, gauss):
    nX = len(f)
    f_test = f[int(nX / 2.0) : :]
    gauss_test = gauss[int(nX / 2.0) : :, int(nX / 2.0)]

    # Calculate peak freq of 1d gaussian filter:
    max_index = np.where(gauss_test == np.max(gauss_test))
    max_index = max_index[0][0]
    fpeak = f_test[max_index]

    # Calculate lower and upper boundary for FWHM
    idx_low = np.abs(gauss_test[0:max_index] - np.max(gauss_test) / 2.0).argmin()
    idx_high = np.abs(gauss_test[max_index::] - np.max(gauss_test) / 2.0).argmin()
    flow = f_test[idx_low]
    fhigh = f_test[max_index + idx_high]
    return fpeak, flow, fhigh


def bandpass_filter(fx, fy, fcenter, sigma):
    """Function to create a bandpass filter

    Parameters
    ----------
    fx
        Array with frequencies in x-direction.
    fy
        Array with frequencies in y-direction.
    fcenter
        Center frequency of the bandpass filter
    sigma
        Sigma that defines the spread of the Gaussian in deg.

    Returns
    -------
    dog
        2D Difference-of-Gaussian filter in frequency domain.

    """
    # Calculate the distance of each 2d spatial frequency from requested center frequency
    distance = np.abs(fcenter - np.sqrt(fx**2.0 + fy**2.0))

    # Create bandpass filter:
    gauss = (
        1.0
        / (np.sqrt(2.0 * np.pi) * sigma)
        * np.exp(-(distance**2.0) / (2.0 * sigma**2.0))
    )
    gauss = gauss / gauss.max()
    return gauss


# Create oriented Gaussian filter:
def oriented_filter(fx, fy, sigma, orientation):
    # convert orientation parameter to radians
    theta = np.deg2rad(orientation)

    # determine a, b, c coefficients
    a = np.cos(theta) ** 2 / (2 * sigma**2)
    b = -(np.sin(2 * theta) / (4 * sigma**2))
    c = np.sin(theta) ** 2 / (2 * sigma**2)

    # create Gaussian
    ofilter = np.exp(-(a * fx**2 + 2 * b * fx * fy + c * fy**2))
    return ofilter


# Apply Gaussian envelope to a stimulus
def apply_gaussian_env(stimulus, sigma):
    # Inputs:
    #    stimulus: Input stimulus, numpy array
    #    sigma: Sigma of Gaussian in px
    #    norm: Bool, if True normalize output array between 0 and 1
    # Output:
    # 2d numpy array with stimulus multiplied with Gaussian envelope

    # Create a meshgrid:
    size = stimulus.shape[0]
    xx, yy = np.mgrid[:size, :size] - size / 2.0

    # Create a Gaussian envelope:
    gauss = (
        1.0
        / (np.sqrt(2.0 * np.pi) * sigma)
        * np.exp(-(xx**2.0 + yy**2.0) / (2.0 * sigma**2.0))
    )
    gauss = gauss / gauss.max()
    stimulus = stimulus * gauss
    return stimulus


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
