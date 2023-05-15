import copy
import itertools

import numpy as np
import scipy.special as sp

from stimupy.utils import resolution

__all__ = [
    "round_to_vals",
    "int_factorize",
    "get_function_argument_names",
    "apply_bessel",
    "resize_array",
    "resize_dict",
    "stack_dicts",
    "rotate_dict",
    "flip_dict",
    "roll_dict",
    "strip_dict",
    "permutate_params",
    "create_stimspace_stimuli",
]


def round_to_vals(arr, vals):
    """
    Round array to provided values (vals)

    Parameters
    ----------
    arr : np.ndarray
        Numpy array which values will be rounded
    vals : Sequence(float, ...)
        Values to which array will be rounded

    Returns
    -------
    out_arr : np.ndarray
        Rounded output array

    """
    n_val = len(vals)
    arr = np.repeat(np.expand_dims(arr, -1), n_val, axis=2)
    vals_arr = np.ones(arr.shape) * np.array(np.expand_dims(vals, [0, 1]))

    indices = np.argmin(np.abs(arr - vals_arr), axis=2)
    out_arr = np.copy(indices).astype(float)

    for i in range(n_val):
        out_arr[indices == i] = vals[i]
    return out_arr


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


def get_function_argument_names(func):
    """
    Get all argument names for a given function

    Parameters
    ----------
    func : function
        Get argument names from this function

    Returns
    -------
    names : tuple
        Tuple containing all argument names of given function
    """
    names = func.__code__.co_varnames[: func.__code__.co_argcount]
    return names


def apply_bessel(arr, order=0):
    """
    Bessel function of the first kind of real order and complex argument.

    Parameters
    ----------
    arr : np.ndarray
        Input array
    order : float
        Order of the bessel function. Default is 0.

    Returns
    -------
    out : np.ndarray
        Output array

    """
    out = sp.jv(order, arr)
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
    dict[str, Any]
        same as input dict but with larger key-arrays according to
        "(arr.shape[0] * factor[0], arr.shape[1] * factor[1])"
        and updated keys for "visual_size" and "shape"
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
                img = np.repeat(np.repeat(img, factor[0], axis=0), factor[1], axis=1)
                if key.endswith("mask"):
                    img = img.astype(int)
                new_dict[key] = img

    # Update visual_size and shape-keys
    dct["shape"] = resolution.validate_shape(img.shape)
    if "ppd" in dct.keys():
        dct["visual_size"] = resolution.visual_size_from_shape_ppd(img.shape, dct["ppd"])
    return new_dict


def stack_dicts(
    dct1, dct2, direction="horizontal", keys=("img", "*mask"), keep_mask_indices=False
):
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
    dict[str, Any]
        same as input dict1 but with stacked key-arrays and updated keys for
        "visual_size" and "shape"
    """

    # Create deepcopy to not override existing dict
    new_dict = copy.deepcopy(dct1)

    if isinstance(keys, str):
        keys = (keys,)

    # Find relevant keys
    keys1 = [
        dkey
        for key in keys
        for dkey in dct1.keys()
        if ((dkey == key) or ((dkey.endswith(key[1::])) and (key.startswith("*"))))
    ]
    keys2 = [
        dkey
        for key in keys
        for dkey in dct2.keys()
        if ((dkey == key) or ((dkey.endswith(key[1::])) and (key.startswith("*"))))
    ]

    if not keys1 == keys2:
        raise ValueError("The requested keys do not exist in both dicts")

    for key in dct1.keys():
        if key in keys1:
            img1 = dct1[key]
            img2 = dct2[key]
            if isinstance(img1, np.ndarray) and isinstance(img2, np.ndarray):
                if key.endswith("mask") and not keep_mask_indices:
                    img2 = np.where(img2 != 0, img2 + img1.max(), 0)

                if direction == "horizontal":
                    img = np.hstack([img1, img2])
                elif direction == "vertical":
                    img = np.vstack([img1, img2])
                else:
                    raise ValueError("direction must be horizontal or vertical")

                if key.endswith("mask"):
                    img = img.astype(int)
                new_dict[key] = img

    # Update visual_size and shape-keys
    new_dict["shape"] = resolution.validate_shape(img.shape)
    if "ppd" in new_dict.keys():
        new_dict["visual_size"] = resolution.visual_size_from_shape_ppd(img.shape, new_dict["ppd"])
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
    dict[str, Any]
        same as input dict but with rotated key-arrays and updated keys for
        "visual_size" and "shape"
    """

    # Create deepcopy to not override existing dict
    new_dict = copy.deepcopy(dct)

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
                if isinstance(nrots, (int, float)):
                    img = np.rot90(img, nrots)
                else:
                    raise ValueError("nrots must be a number")

                if key.endswith("mask"):
                    img = img.astype(int)
                new_dict[key] = img

    # Update visual_size and shape-keys
    new_dict["shape"] = resolution.validate_shape(img.shape)
    if "ppd" in new_dict.keys():
        new_dict["visual_size"] = resolution.visual_size_from_shape_ppd(img.shape, new_dict["ppd"])
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
    dict[str, Any]
        same as input dict but with flipped key-arrays
    """

    # Create deepcopy to not override existing dict
    new_dict = copy.deepcopy(dct)

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
    dict[str, Any]
        same as input dict but with rolled key-arrays
    """

    # Create deepcopy to not override existing dict
    new_dict = copy.deepcopy(dct)
    shift = np.array(shift).astype(int)

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
                img = np.roll(img, shift=shift, axis=axes)

                if key.endswith("mask"):
                    img = img.astype(int)
                new_dict[key] = img
    return new_dict


def strip_dict(
    dct,
    func,
):
    """
    Create a dictionary by stripping it from all keys that are not also
    an argument to the provided function

    Parameters
    ----------
    dct: dict
        dict which will be stripped
    func : function
        Get argument names from this function

    Returns
    -------
    dict[str, Any]
        same as input dict but stripped from all keys which are not also
        an argument to the provided function
    """

    # Get all argument names for given function
    names = get_function_argument_names(func)

    # Add keys from dct into new_dict if the key is also an argument name
    new_dict = dict()
    for name in names:
        if name in dct.keys():
            new_dict[name] = dct[name]
    return new_dict


def permutate_params(params):
    if not isinstance(params, dict):
        raise ValueError("params needs to be a dict with all stimulus parameters")

    keys, values = zip(*params.items())
    permutations_dicts = [dict(zip(keys, v)) for v in itertools.product(*values)]
    return permutations_dicts


def create_stimspace_stimuli(stimulus_function, permutations_dicts, title_params=None):
    if not callable(stimulus_function):
        raise ValueError("stimulus_function needs to be a function")
    if isinstance(title_params, str):
        title_params = [
            title_params,
        ]

    stimuli = {}
    for i, p in enumerate(permutations_dicts):
        if title_params is None:
            key = str(i)
        else:
            key = ""
            for tname in title_params:
                if isinstance(p[tname], (float, int)):
                    ptname = np.round(p[tname], 3)
                    key += f"{tname}={ptname} "
                else:
                    key += f"{tname}={p[tname]} "
        stimuli[key] = stimulus_function(
            **p,
        )
    return stimuli
