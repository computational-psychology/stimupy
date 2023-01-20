import numpy as np
import copy

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


# %%
#################################
#         Dictionaries          #
#################################
def pad_dict_by_visual_size(dct, padding, ppd, pad_value=0.0, keys=("img", "*mask")):
    """Pad images in dictionary by specified degrees of visual angle

    Can specify different amount (before, after) each axis.

    Parameters
    ----------
    dct : dict
        dict containing image-arrays to be padded
    padding : float, or Sequence[float, float], or Sequence[Sequence[float, float], ...]
        amount of padding, in degrees visual angle, in each direction:
        ((before_1, after_1), … (before_N, after_N)) unique pad widths for each axis
        (float,) or float is a shortcut for before = after = pad width for all axes.
    ppd : Sequence[Number] or Sequence[Number, Number]
        pixels per degree
    pad_value : Numeric, optional
        value to pad with, by default 0.0
    keys : Sequence[String, String] or String
        keys in dict for images to be padded

    Returns
    -------
    dict with padded images by the specified amount(s)

    See also
    ---------
    stimuli.utils.resolution
    """
    # Create deepcopy to not override existing dict
    new_dict = copy.deepcopy(dct)
    
    if isinstance(keys, str):
        keys = (keys,)

    # Find relevant keys
    keys = [dkey for key in keys for dkey in dct.keys() if ((dkey == key) or
                                                            ((dkey.endswith(key[1::])) and
                                                              (key.startswith("*")))
                                                             )]
    
    for key in dct.keys():
            if key in keys:
                img = dct[key]
                if isinstance(img, np.ndarray):
                    if key.endswith("mask"):
                        img = pad_by_visual_size(img, padding, ppd, 0)
                        img = img.astype(int)
                    else:
                        img = pad_by_visual_size(img, padding, ppd, pad_value)
                    new_dict[key] = img
    return new_dict


def pad_dict_to_visual_size(dct, visual_size, ppd, pad_value=0, keys=("img", "*mask")):
    """Pad images in dictionary to specified visual size in degrees visual angle

    Parameters
    ----------
    dct : dict
        dict containing image-arrays to be padded
    visual_size : Sequence[int, int, ...]
        desired visual size (in degrees visual angle) of img after padding
    ppd : Sequence[Number] or Sequence[Number, Number]
        pixels per degree
    pad_value : Numeric, optional
        value to pad with, by default 0.0
    keys : Sequence[String, String] or String
        keys in dict for images to be padded

    Returns
    -------
    dict with padded images by the specified amount(s)

    See also
    ---------
    stimuli.utils.resolution
    """

    # visual_size to shape
    shape = resolution.shape_from_visual_size_ppd(visual_size=visual_size, ppd=ppd)

    # pad
    return pad_dict_to_shape(dct=dct, shape=shape, pad_value=pad_value, keys=keys)


def pad_dict_by_shape(dct, padding, pad_value=0, keys=("img", "*mask")):
    """Pad images in dictionary by specified amount(s) of pixels

    Can specify different amount (before, after) each axis.

    Parameters
    ----------
    dct : dict
        dict containing image-arrays to be padded
    padding : int, or Sequence[int, int], or Sequence[Sequence[int, int], ...]
        amount of padding, in pixels, in each direction:
        ((before_1, after_1), … (before_N, after_N)) unique pad widths for each axis
        (int,) or int is a shortcut for before = after = pad width for all axes.
    pad_val : float, optional
        value to pad with, by default 0.0
    keys : Sequence[String, String] or String
        keys in dict for images to be padded

    Returns
    -------
    dict with padded images by the specified amount(s)
    """
    # Ensure padding is in integers
    padding = np.array(padding, dtype=np.int32)
    
    # Create deepcopy to not override existing dict
    new_dict = copy.deepcopy(dct)
    
    if isinstance(keys, str):
        keys = (keys,)

    # Find relevant keys
    keys = [dkey for key in keys for dkey in dct.keys() if ((dkey == key) or
                                                            ((dkey.endswith(key[1::])) and
                                                              (key.startswith("*")))
                                                             )]
    
    for key in dct.keys():
            if key in keys:
                img = dct[key]
                if isinstance(img, np.ndarray):
                    if key.endswith("mask"):
                        img = np.pad(img, padding, mode="constant", constant_values=0)
                        img = img.astype(int)
                    else:
                        img = np.pad(img, padding, mode="constant", constant_values=pad_value)
                    new_dict[key] = img
    return new_dict


def pad_dict_to_shape(dct, shape, pad_value=0, keys=("img", "*mask")):
    """Pad images in dicationary to a resulting specified shape in pixels

    Parameters
    ----------
    dct : dict
        dict containing image-arrays to be padded
    shape : Sequence[int, int, ...]
        desired shape of img after padding
    pad_value : float, optional
        value to pad with, by default 0.0
    keys : Sequence[String, String] or String
        keys in dict for images to be padded

    Returns
    -------
    dict with padded images by the specified amount(s)

    Raises
    ------
    ValueError
        if img.shape already exceeds shape
    """
    # Create deepcopy to not override existing dict
    new_dict = copy.deepcopy(dct)
    
    if isinstance(keys, str):
        keys = (keys,)

    # Find relevant keys
    keys = [dkey for key in keys for dkey in dct.keys() if ((dkey == key) or
                                                            ((dkey.endswith(key[1::])) and
                                                              (key.startswith("*")))
                                                             )]
    
    for key in dct.keys():
            if key in keys:
                img = dct[key]
                if isinstance(img, np.ndarray):
                    if np.any(img.shape > shape):
                        raise ValueError("img is bigger than size after padding")
    
                    padding_per_axis = np.array(shape) - np.array(img.shape)
                    padding_before = padding_per_axis // 2
                    padding_after = padding_per_axis - padding_before
                    padding = np.stack([padding_before, padding_after]).T
    
                    if key.endswith("mask"):
                        img = pad_by_shape(img, padding=padding, pad_value=0)
                        img = img.astype(int)
                    else:
                        img = pad_by_shape(img, padding=padding, pad_value=pad_value)
                    new_dict[key] = img
    return new_dict


def resize_dict(dct, factor, keys=("img", "*mask")):
    """
    Return a copy of an array, resized by the given factor. Every value is
    repeated factor[d] times along dimension d.

    Parameters
    ----------
    dct : dict
        dict containing arrays to be resized
    factor : tupel of 2 ints
        the resize factor in the y and x dimensions
    keys : Sequence[String, String] or String
        keys in dict for images to be padded

    Returns
    -------
    dict with arrays of shape (arr.shape[0] * factor[0], arr.shape[1] * factor[1])
    """
    # Create deepcopy to not override existing dict
    new_dict = copy.deepcopy(dct)
    
    if isinstance(keys, str):
        keys = (keys,)

    # Find relevant keys
    keys = [dkey for key in keys for dkey in dct.keys() if ((dkey == key) or
                                                            ((dkey.endswith(key[1::])) and
                                                              (key.startswith("*")))
                                                             )]
    
    for key in dct.keys():
            if key in keys:
                img = dct[key]
                if isinstance(img, np.ndarray):
                    img = np.repeat(np.repeat(img, factor[0], axis=0), factor[1], axis=1)
                    if key.endswith("mask"):
                        img = img.astype(int)
                    new_dict[key] = img
    return new_dict


def stack_dicts(dct1, dct2, direction="horizontal", keys=("img", "*mask"), keep_mask_indices=False):
    """
    Return a dict with resized key-arrays by the given factor. Every value is
    repeated factor[d] times along dimension d.

    Parameters
    ----------
    dct1: dict
        dict containing arrays to be stacked
    dct2: dict
        dict containing arrays to be stacked
    direction : str
        stack horizontal(ly) or vertical(ly) (default: horizontal)
    keys : Sequence[String, String] or String
        keys in dict for images to be padded

    Returns
    -------
    dict with keys with stacked arrays
    """
    
    # Create deepcopy to not override existing dict
    new_dict = copy.deepcopy(dct1)
    
    if isinstance(keys, str):
        keys = (keys,)

    # Find relevant keys
    keys1 = [dkey for key in keys for dkey in dct1.keys() if ((dkey == key) or
                                                              ((dkey.endswith(key[1::])) and
                                                               (key.startswith("*")))
                                                              )]
    keys2 = [dkey for key in keys for dkey in dct2.keys() if ((dkey == key) or
                                                              ((dkey.endswith(key[1::])) and
                                                               (key.startswith("*")))
                                                              )]

    if not keys1 == keys2:
        raise ValueError("The requested keys do not exist in both dicts")
    
    for key in dct1.keys():
            if key in keys1:
                img1 = dct1[key]
                img2 = dct2[key]
                if isinstance(img1, np.ndarray) and isinstance(img2, np.ndarray):
                    if key.endswith("mask") and not keep_mask_indices:
                        img2 = np.where(img2 != 0, img2+img1.max(), 0)

                    if direction == "horizontal":
                        img = np.hstack([img1, img2])
                    elif direction == "vertical":
                        img = np.vstack([img1, img2])
                    else:
                        raise ValueError("direction must be horizontal or vertical")

                    if key.endswith("mask"):
                        img = img.astype(int)
                    new_dict[key] = img
    return new_dict


def rotate_dict(dct, nrots=1, keys=("img", "*mask")):
    """
    Return a dict with key-arrays rotated by nrots*90 degrees.

    Parameters
    ----------
    dct: dict
        dict containing arrays to be stacked
    nrot : int
        number of rotations by 90 degrees
    keys : Sequence[String, String] or String
        keys in dict for images to be padded

    Returns
    -------
    dict with keys with rotated arrays
    """
    
    # Create deepcopy to not override existing dict
    new_dict = copy.deepcopy(dct)

    # Find relevant keys
    keys = [dkey for key in keys for dkey in dct.keys() if ((dkey == key) or
                                                            ((dkey.endswith(key[1::])) and
                                                              (key.startswith("*")))
                                                             )]
    
    for key in dct.keys():
            if key in keys:
                img = dct[key]
                if isinstance(img, np.ndarray):
                    if isinstance(nrots, (int, float)):
                        img = np.rot90(img, nrots)
                    else:
                        raise ValueError("nrots must be a number")

                    if key.endswith("mask"):
                        img = img.astype(int)
                    new_dict[key] = img
    return new_dict


def flip_dict(dct, direction="lr", keys=("img", "*mask")):
    """
    Return a dict with key-arrays rotated by nrots*90 degrees.

    Parameters
    ----------
    dct: dict
        dict containing arrays to be stacked
    direction : str
        "lr" for left-right, "ud" for up-down flipping
    keys : Sequence[String, String] or String
        keys in dict for images to be padded

    Returns
    -------
    dict with keys with rotated arrays
    """
    
    # Create deepcopy to not override existing dict
    new_dict = copy.deepcopy(dct)

    # Find relevant keys
    keys = [dkey for key in keys for dkey in dct.keys() if ((dkey == key) or
                                                            ((dkey.endswith(key[1::])) and
                                                              (key.startswith("*")))
                                                             )]
    
    for key in dct.keys():
            if key in keys:
                img = dct[key]
                if isinstance(img, np.ndarray):
                    if direction == "lr":
                        img = np.fliplr(img)
                    elif direction == "ud":
                        img = np.flipud(img)
                    else:
                        raise ValueError("direction must be lr or ud")

                    if key.endswith("mask"):
                        img = img.astype(int)
                    new_dict[key] = img
    return new_dict


def roll_dict(dct, shift, axes, keys=("img", "*mask")):
    """
    Return a dict with key-arrays rolled by shift in axes.

    Parameters
    ----------
    dct: dict
        dict containing arrays to be stacked
    shift : int
        number of pixels by which to shift
    axes : Number or Sequence[Number, ...]
        axes in which to shift
    keys : Sequence[String, String] or String
        keys in dict for images to be padded

    Returns
    -------
    dict with keys with rolled arrays
    """
    
    # Create deepcopy to not override existing dict
    new_dict = copy.deepcopy(dct)
    shift = np.array(shift).astype(int)

    # Find relevant keys
    keys = [dkey for key in keys for dkey in dct.keys() if ((dkey == key) or
                                                            ((dkey.endswith(key[1::])) and
                                                              (key.startswith("*")))
                                                             )]
    
    for key in dct.keys():
            if key in keys:
                img = dct[key]
                if isinstance(img, np.ndarray):
                    img = np.roll(img, shift=shift, axis=axes)

                    if key.endswith("mask"):
                        img = img.astype(int)
                    new_dict[key] = img
    return new_dict
