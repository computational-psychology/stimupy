import numpy as np

from .utils import degrees_to_pixels


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
