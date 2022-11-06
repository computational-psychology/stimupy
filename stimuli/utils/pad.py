import numpy as np

from . import resolution


def pad_by_visual_size(img, padding, ppd, pad_value=0.0):
    """Pad image by specified degrees of visual angle

    Can specify different amount (before, after) each axis.

    Parameters
    ----------
    img : numpy.ndarray
        image-array to be padded
    padding : float, or Sequence[float, float], or Sequence[Sequence[float, float], ...]
        amount of padding, in degrees visual angle, in each direction:
        ((before_1, after_1), … (before_N, after_N)) unique pad widths for each axis
        (float,) or float is a shortcut for before = after = pad width for all axes.
    ppd : Sequence[Number] or Sequence[Number, Number]
        pixels per degree
    pad_value : Numeric, optional
        value to pad with, by default 0.0

    Returns
    -------
    numpy.ndarray
        img padded by the specified amount(s)

    See also
    ---------
    stimuli.utils.resolution
    """

    # Broadcast to ((before_1, after_1),...(before_N, after_N))
    padding_degs = np.broadcast_to(padding, (img.ndim, 2))

    # ppd in canonical form
    ppd = resolution.validate_ppd(ppd)

    # Convert to shape in pixels
    padding_px = []
    for axis in padding_degs:
        shape = [
            resolution.pix_from_visual_angle_ppd_1D(i, ppd) if i > 0 else 0
            for i, ppd in zip(axis, ppd)
        ]
        padding_px.append(shape)

    # Pad by shape in pixels
    return pad_by_shape(img=img, padding=padding_px, pad_value=pad_value)


def pad_to_visual_size(img, visual_size, ppd, pad_value=0):
    """Pad image to specified visual size in degrees visual angle

    Parameters
    ----------
    img : numpy.ndarray
        image-array to be padded
    visual_size : Sequence[int, int, ...]
        desired visual size (in degrees visual angle) of img after padding
    ppd : Sequence[Number] or Sequence[Number, Number]
        pixels per degree
    pad_value : Numeric, optional
        value to pad with, by default 0.0

    Returns
    -------
    numpy.ndarray
        img padded by the specified amount(s)

    See also
    ---------
    stimuli.utils.resolution
    """

    # visual_size to shape
    shape = resolution.shape_from_visual_size_ppd(visual_size=visual_size, ppd=ppd)

    # pad
    return pad_to_shape(img=img, shape=shape, pad_value=pad_value)


def pad_by_shape(img, padding, pad_value=0):
    """Pad image by specified amount(s) of pixels

    Can specify different amount (before, after) each axis.

    Parameters
    ----------
    img : numpy.ndarray
        image-array to be padded
    padding : int, or Sequence[int, int], or Sequence[Sequence[int, int], ...]
        amount of padding, in pixels, in each direction:
        ((before_1, after_1), … (before_N, after_N)) unique pad widths for each axis
        (int,) or int is a shortcut for before = after = pad width for all axes.
    pad_val : float, optional
        value to pad with, by default 0.0

    Returns
    -------
    numpy.ndarray
        img padded by the specified amount(s)
    """

    # Ensure padding is in integers
    padding = np.array(padding, dtype=np.int32)

    return np.pad(img, padding, mode="constant", constant_values=pad_value)


def pad_to_shape(img, shape, pad_value=0):
    """Pad image to a resulting specified shape in pixels

    Parameters
    ----------
    img : numpy.ndarray
        image-array to be padded
    shape : Sequence[int, int, ...]
        desired shape of img after padding
    pad_value : float, optional
        value to pad with, by default 0.0

    Returns
    -------
    numpy.ndarray
        img padded to specified shape

    Raises
    ------
    ValueError
        if img.shape already exceeds shape
    """

    if np.any(img.shape > shape):
        raise ValueError("img is bigger than size after padding")

    padding_per_axis = np.array(shape) - np.array(img.shape)
    padding_before = padding_per_axis // 2
    padding_after = padding_per_axis - padding_before
    padding = np.stack([padding_before, padding_after]).T

    return pad_by_shape(
        img,
        padding=padding,
        pad_value=pad_value,
    )


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
