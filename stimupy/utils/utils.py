import collections
import copy
import functools
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
    "make_two_sided",
    "permutate_params",
    "create_stimspace_stimuli",
]


def _count_none_args(*args):
    """Counts the number of None values in the provided arguments

    Parameters
    ----------
    *args : dict
        variable number of arguments to check for None values

    Returns
    -------
    int :
        number of None values in the arguments.

    Examples
    --------
    >>> check_multiple_none(None, 1, None, 2, 3)
    2
    >>> check_multiple_none(1, 2, 3)
    0
    """
    return args.count(None)


def _repeat_numeric_arg(arg, n=2):
    """If provided argument is single number, repeat n times

    Checks if the argument is a single number (int, float).
    If so, returns a list containing the number repeated the specified number of times.
    For other datatypes, returns the argument itself.

    Parameters
    ----------
    arg : Any
        Input argument to check
    count : int, optional
        Number of times to repeat the argument, by default 2.

    Returns
    -------
    list or any:
        List with the number repeated 'count' times if the argument is a number,
        or the original arg if non-numeric.

    Examples
    --------
    >>> check_and_repeat(5, n=3)
    [5, 5, 5]
    >>> check_and_repeat("Hello")
    'Hello'
    """
    # Check if the argument is a single number (int or float)
    if isinstance(arg, (int, float)):
        return [arg] * n  # Repeat the number 'count' times in a list
    else:
        return arg


def round_to_vals(arr, vals, mode="nearest"):
    """Round each element of array to closest match in provided values

    For each element in the input `arr`, find the closest value from the provided `vals`
    and replace the element with this closest value.
    If the element is equidistant to two values, the smaller
    value is chosen.

    Parameters
    ----------
    arr : np.ndarray
        array to be rounded
    vals : Sequence(float, ...)
        values to which array will be rounded
    mode : ["nearest", "floor", "ceil"], optional
        rounding mode. Default is "nearest".

    Returns
    -------
    out_arr : np.ndarray
        Rounded output array

    Raises
    ------
    ValueError
        If `mode` is not one of ["nearest", "floor", "ceil"].
        If `arr` contains values outside the bounds of
        `vals` when `mode` is "floor" or "ceil".

    Examples
    --------
    >>> arr = np.array([1.1, 2.2, 3.3, 4.4, 5.5])
    >>> vals = [1, 3, 5]
    >>> round_to_vals(arr, vals)
    array([1., 3., 3., 5., 5.])

    """
    # Ensure the 1D array contains only unique values
    arr_1d = np.sort(np.unique(vals))
    arr = np.array(arr)

    # Ensure arr fall within bounds of mode:
    if mode == "floor" and arr.min() < arr_1d.min():
        raise ValueError(
            f"Array values must be within bounds of vals : {arr.min()} < {arr_1d.min()}"
        )
    if mode == "ceil" and arr.min() > arr_1d.max():
        raise ValueError(
            f"Array values must be within bounds of vals: {arr.min()} > {arr_1d.max()}"
        )

    # Find the nearest values from vals, for each element in arr
    if mode == "floor":
        idxs = np.searchsorted(arr_1d, arr, side="left") - 1
    elif mode == "ceil":
        idxs = np.searchsorted(arr_1d, arr, side="right")
    elif mode == "nearest":
        # Find indexes where previous index is closer
        idxs = np.searchsorted(arr_1d, arr, side="left")
        prev_idx_is_less = (idxs == len(arr_1d)) | (
            np.fabs(arr - arr_1d[np.maximum(idxs - 1, 0)])
            < np.fabs(arr - arr_1d[np.minimum(idxs, len(arr_1d) - 1)])
        )
        idxs[prev_idx_is_less] -= 1
    else:
        raise ValueError(f"Invalid mode: {mode}")

    # Replace each element in arr with the nearest value from vals
    rounded_arr = arr_1d[idxs]

    return rounded_arr


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
    factor : tuple of 2 ints
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
    factor : tuple of 2 ints
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


def make_two_sided(func, two_sided_params):
    """Create two-sided version of a stimulus function

    Where (some) parameters can be specified separately for each side.
    These parameters should then be specified as a 2-Sequence (2-ple, list of len=2),
    where entry [0] is the parameter value for left side, and [1] for right side.
    This means that if the kwarg takes a Sequence itself, e.g., `intensities`,
    then the two-sided specification must be, e.g.,
    ((int_left_0, int_left_1), (int_right_0, int_right_1))

    Will be left- and right-sided.


    Parameters
    ----------
    func : function
        stimulus function to double
    two_sided_params : Sequence[str]
        names of parameters (kwargs) of func
        that can be specified separately for each side of the display.

    Returns
    -------
    function
        two-sided version of stimulus function
    """

    @functools.wraps(func)
    def two_sided_func(**kwargs):
        shape = kwargs.pop("shape", None)
        visual_size = kwargs.pop("visual_size", None)
        ppd = kwargs.pop("ppd", None)

        # Resolve resolution
        try:
            shape, visual_size, ppd = resolution.resolve(
                shape=shape, visual_size=visual_size, ppd=ppd
            )
        except resolution.TooManyUnknownsError:
            shape = resolution.validate_shape(shape)
            visual_size = resolution.validate_visual_size(visual_size)
            ppd = resolution.validate_ppd(ppd)
        if visual_size.width is not None:
            _visual_size = (visual_size.height, visual_size.width / 2)
        else:
            _visual_size = None
        if shape.width is not None:
            _shape = (shape.height, shape.width / 2)
        else:
            _shape = None

        # Left side
        left_side_params = {}
        for key, value in kwargs.items():
            if key in two_sided_params and isinstance(value, collections.abc.Sequence):
                left_side_params[key] = value[0]
            else:
                left_side_params[key] = value

        left = func(
            visual_size=_visual_size,
            ppd=ppd,
            shape=_shape,
            **left_side_params,
        )

        # Right side
        right_side_params = {}
        for key, value in kwargs.items():
            if key in two_sided_params and isinstance(value, collections.abc.Sequence):
                right_side_params[key] = value[1]
            else:
                right_side_params[key] = value

        right = func(
            visual_size=_visual_size,
            ppd=ppd,
            shape=_shape,
            **right_side_params,
        )

        stim = stack_dicts(left, right, direction="horizontal")
        stim["shape"] = left["shape"].height, left["shape"].width + right["shape"].width
        stim["visual_size"] = (
            left["visual_size"].height,
            left["visual_size"].width + right["visual_size"].width,
        )
        for key in two_sided_params:
            if key in kwargs:
                stim[key] = kwargs[key]
            else:
                stim[key] = (left[key], right[key])
        return stim

    return two_sided_func


def permutate_params(params):
    """Generate all possible parameter combinations for a stimulus function.

    Takes a dictionary of stimulus parameters, where each parameter value is
    provided as a sequence (e.g., list, tuple). Returns a list of dictionaries,
    each representing one unique combination of parameter values. This is
    useful for systematically exploring a stimulus parameter space
    (e.g., in 1D, 2D, or higher dimensions).

    Parameters
    ----------
    params : dict
        Dictionary mapping parameter names (str) to sequences of possible values.
        Each sequence will be iterated over to form combinations.  
        Example::
            {
                "frequency": [1, 2, 4],
                "sigma": [0.05, 0.1]
            }

    Returns
    -------
    list of dict
        A list where each element is a dictionary mapping parameter names to
        specific values, corresponding to one combination from the Cartesian
        product of all provided sequences.  
        Example output::
            [
                {"frequency": 1, "sigma": 0.05},
                {"frequency": 1, "sigma": 0.1},
                {"frequency": 2, "sigma": 0.05},
                ...
            ]

    Raises
    ------
    ValueError
        If `params` is not a dictionary.
    """
    if not isinstance(params, dict):
        raise ValueError("params needs to be a dict with all stimulus parameters")

    keys, values = zip(*params.items())
    permutations_dicts = [dict(zip(keys, v)) for v in itertools.product(*values)]
    return permutations_dicts


def create_stimspace_stimuli(stimulus_function, permutations_dicts, title_params=None):
    """Generate stimuli for all parameter combinations in a stimspace.

    Given a callable `stimulus_function` and a list of parameter combinations
    (as produced by [`utils.permutate_params`](utils.permutate_params)),
    this function generates and returns all corresponding stimulus images.
    Optionally, specific parameters can be included in the stimulus names
    for easier identification in plots or debugging.

    Parameters
    ----------
    stimulus_function : callable
        A stimulus-generating function that accepts keyword arguments matching
        the keys in `permutations_dicts`.

    permutations_dicts : list of dict
        A list of parameter dictionaries, each representing one combination of
        stimulus parameters to be passed to `stimulus_function`.
        Typically obtained from [`utils.permutate_params`](utils.permutate_params).

    title_params : str or list of str, optional
        Name(s) of parameters to display in the dictionary keys for the output.
        - If a string, it is interpreted as a single parameter name.
        - If a list, multiple parameter values will be included in the name.
        - If `None` (default), keys will be simple integer indices.

    Returns
    -------
    dict
        Dictionary mapping descriptive keys to the generated stimulus outputs.
        Keys are either:
        - String representations of selected `title_params` and their values.
        - Sequential integer strings if `title_params` is `None`.

    Raises
    ------
    ValueError
        If `stimulus_function` is not callable.

    Examples
    --------
    >>> from stimupy.stimuli.gabors import gabor
    >>> from stimupy.utils import permutate_params, create_stimspace_stimuli
    >>> params = {
    ...     "visual_size": [1.],
    ...     "ppd": [50],
    ...     "sigma": [0.1, 0.2],
    ...     "frequency": [2, 4]
    ... }
    >>> permuted = permutate_params(params)
    >>> stimspace = create_stimspace_stimuli(
    ...     stimulus_function=gabor,
    ...     permutations_dicts=permuted,
    ...     title_params=["sigma", "frequency"]
    ... )
    >>> list(stimspace.keys())
    ['sigma=0.1 frequency=2 ', 'sigma=0.1 frequency=4 ', 
     'sigma=0.2 frequency=2 ', 'sigma=0.2 frequency=4 ']
    """
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
