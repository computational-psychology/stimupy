import copy
import numpy as np

from .utils import resolution

__all__ = [
    "add_padding",
    "remove_padding",
    "pad_by_visual_size",
    "pad_to_visual_size",
    "pad_by_shape",
    "pad_to_shape",
    "pad_dict_by_visual_size",
    "pad_dict_to_visual_size",
    "pad_dict_by_shape",
    "pad_dict_to_shape",
]


def remove_padding(arr, c):
    """
    Remove padding by c

    Parameters
    ----------
    arr : numpy.ndarray
        input array
    c : int
        padding amount.

    Returns
    -------
    arr : numpy.ndarray
        reduced array

    """
    array_shape = arr.shape
    arr = arr[c : array_shape[0] - c, c : array_shape[1] - c]
    return arr


def add_padding(arr, c, val):
    """
    Remove padding by c

    Parameters
    ----------
    arr : numpy.ndarray
        input array
    c : int
        padding amount
    val : float
        background value

    Returns
    -------
    arr : numpy.ndarray
        padded array

    """
    h, w = arr.shape
    new_arr = np.ones([h + c * 2, w + c * 2]) * val
    new_arr[c : h + c, c : w + c] = arr
    return new_arr


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
    stimupy.utils.resolution
    """

    # Broadcast to ((before_1, after_1),...(before_N, after_N))
    padding_degs = np.broadcast_to(padding, (img.ndim, 2))

    # ppd in canonical form
    ppd = resolution.validate_ppd(ppd)

    # Convert to shape in pixels
    padding_px = []
    for axis in padding_degs:
        shape = [
            resolution.length_from_visual_angle_ppd(i, ppd) if i > 0 else 0
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
    stimupy.utils.resolution
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
    dict[str, Any]
        same as input dict but with larger key-arrays and updated keys for
        "visual_size" and "shape"
    """
    # Create deepcopy to not override existing dict
    new_dict = copy.deepcopy(dct)

    if isinstance(keys, str):
        keys = (keys,)

    # Find relevant keys
    keys = [
        dkey
        for key in keys
        for dkey in dct.keys()
        if ((dkey == key) or ((dkey.endswith(key[1::])) and (key.startswith("*"))))
    ]

    for key in dct.keys():
        if key in keys:
            img = dct[key]
            if isinstance(img, np.ndarray):
                # Add mask which indicates padded region
                new_dict["pad_mask"] = pad_by_visual_size(
                    np.zeros(img.shape), padding, ppd, 1
                ).astype(int)

                if key.endswith("mask"):
                    img = pad_by_visual_size(img, padding, ppd, 0)
                    img = img.astype(int)
                else:
                    img = pad_by_visual_size(img, padding, ppd, pad_value)
                new_dict[key] = img

    # Update visual_size and shape-keys
    new_dict["visual_size"] = resolution.visual_size_from_shape_ppd(img.shape, ppd)
    new_dict["shape"] = resolution.validate_shape(img.shape)
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
    dict[str, Any]
        same as input dict but with larger key-arrays and updated keys for
        "visual_size" and "shape"
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
    dict[str, Any]
        same as input dict but with larger key-arrays and updated keys for
        "visual_size" and "shape"
    """
    # Ensure padding is in integers
    padding = np.array(padding, dtype=np.int32)

    # Create deepcopy to not override existing dict
    new_dict = copy.deepcopy(dct)

    if isinstance(keys, str):
        keys = (keys,)

    # Find relevant keys
    keys = [
        dkey
        for key in keys
        for dkey in dct.keys()
        if ((dkey == key) or ((dkey.endswith(key[1::])) and (key.startswith("*"))))
    ]

    for key in dct.keys():
        if key in keys:
            img = dct[key]
            if isinstance(img, np.ndarray):
                # Add mask which indicates padded region
                new_dict["pad_mask"] = np.pad(
                    np.zeros(img.shape), padding, mode="constant", constant_values=1
                ).astype(int)

                if key.endswith("mask"):
                    img = np.pad(img, padding, mode="constant", constant_values=0)
                    img = img.astype(int)
                else:
                    img = np.pad(img, padding, mode="constant", constant_values=pad_value)
                new_dict[key] = img

    # Update visual_size and shape-keys
    new_dict["shape"] = resolution.validate_shape(img.shape)
    if "ppd" in dct.keys():
        new_dict["visual_size"] = resolution.visual_size_from_shape_ppd(img.shape, dct["ppd"])
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
    dict[str, Any]
        same as input dict but with larger key-arrays and updated keys for
        "visual_size" and "shape"

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
    keys = [
        dkey
        for key in keys
        for dkey in dct.keys()
        if ((dkey == key) or ((dkey.endswith(key[1::])) and (key.startswith("*"))))
    ]

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

                # Add mask which indicates padded region
                new_dict["pad_mask"] = pad_by_shape(
                    np.zeros(img.shape), padding=padding, pad_value=1
                ).astype(int)

                if key.endswith("mask"):
                    img = pad_by_shape(img, padding=padding, pad_value=0)
                    img = img.astype(int)
                else:
                    img = pad_by_shape(img, padding=padding, pad_value=pad_value)
                new_dict[key] = img

    # Update visual_size and shape-keys
    new_dict["shape"] = resolution.validate_shape(shape)
    if "ppd" in dct.keys():
        new_dict["visual_size"] = resolution.visual_size_from_shape_ppd(shape, dct["ppd"])
    return new_dict
