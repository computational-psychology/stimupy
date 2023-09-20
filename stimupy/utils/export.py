import copy
import json
import pickle
from hashlib import md5
from pathlib import Path

import numpy as np
from PIL import Image
from scipy.io import savemat

__all__ = [
    "array_to_checksum",
    "array_to_image",
    "array_to_npy",
    "array_to_mat",
    "array_to_pickle",
    "arrays_to_checksum",
    "to_json",
    "to_mat",
    "to_pickle",
]


def array_to_checksum(arr):
    """Hash (md5) array values, and return hex-checksum

    Parameters
    ----------
    arr : numpy.ndarray
        array to be hashed.

    Returns
    ----------
    str
        hex-string representation of hash (MD5) of given array
    """
    return md5(np.ascontiguousarray(arr.round(8))).hexdigest()


def array_to_image(arr, filename, format=None, norm=True):
    """Save a 2D numpy array as a grayscale image file.

    Parameters
    ----------
    arr : numpy.ndarray
        array to be exported. Values will be cropped to [0,255].
    filename : Path or str
        (full) path to the file to be created.
    norm : bool
        multiply array by 255, by default True
    """
    try:
        arr_to_write = np.ascontiguousarray(arr)
    except TypeError as e:
        raise e from ValueError("arr should be a numpy.ndarray(-like)")

    if norm:
        arr_to_write = arr_to_write * 255

    im = Image.fromarray(arr_to_write.astype("uint8"), mode="L")
    im.save(filename)


def array_to_npy(arr, filename):
    """Save a numpy array to npy-file.

    Parameters
    ----------
    arr : numpy.ndarray
        array to be exported.
    filename : Path or str
        (full) path to the file to be created.
    """
    try:
        arr_to_write = np.ascontiguousarray(arr)
    except TypeError as e:
        raise e from ValueError("arr should be a numpy.ndarray(-like)")

    filepath = Path(filename).resolve().with_suffix(".npy")

    np.save(filepath, arr_to_write)


def array_to_mat(arr, filename):
    """Save a numpy array to a mat-file.

    Parameters
    ----------
    arr : numpy.ndarray
        array to be exported.
    filename : Path or str
        (full) path to the file to be created.
    """
    try:
        arr_to_write = np.ascontiguousarray(arr)
    except TypeError as e:
        raise e from ValueError("arr should be a numpy.ndarray(-like)")

    filepath = Path(filename).resolve().with_suffix(".mat")

    savemat(filepath, {"arr": arr_to_write})


def array_to_pickle(arr, filename):
    """Save a numpy array to a pickle-file.

    Parameters
    ----------
    arr : numpy.ndarray
        array to be exported.
    filename : Path or str
        (full) path to the file to be created.
    """
    try:
        arr_to_write = np.ascontiguousarray(arr)
    except TypeError as e:
        raise e from ValueError("arr should be a numpy.ndarray(-like)")

    filepath = Path(filename).resolve().with_suffix(".pickle")

    with filepath.open("wb") as file:
        pickle.dump({"arr": arr_to_write}, file, protocol=pickle.HIGHEST_PROTOCOL)


def array_to_json(arr, filename):
    """Save a numpy array to a (pretty) JSON.

    Parameters
    ----------
    arr : numpy.ndarray
        array to be exported.
    filename : Path or str
        (full) path to the file to be created.
    """
    try:
        arr_to_write = np.ascontiguousarray(arr)
    except TypeError as e:
        raise e from ValueError("arr should be a numpy.ndarray(-like)")

    filepath = Path(filename).resolve().with_suffix(".json")

    with filepath.open("w", encoding="utf-8") as file:
        json.dump(arr_to_write.tolist(), file, ensure_ascii=False, indent=4)


def arrays_to_checksum(stim, keys=["img", "mask"]):
    """Hash (md5) values of arrays specified in keys, and save only the hex

    Parameters
    ----------
    stim : dict
        stimulus dictionary to export.
    keys : str of list of str
        keys of dict for which the hashing should be performed

    Returns
    ----------
    dict[str, Any]
        same as input dict but keys now only contain the hex
    """
    if isinstance(keys, str):
        keys = [
            keys,
        ]

    for key in keys:
        stim[key] = array_to_checksum(stim[key])

    return stim


def to_json(stim, filename):
    """Save stimulus-dict(s) as (pretty) JSON

    Parameters
    ----------
    stim : dict
        stimulus dictionary to export.
    filename : Path or str
        (full) path to the file to be created.

    """
    if not isinstance(stim, dict):
        raise ValueError("stim should be a dict")

    filepath = Path(filename).resolve().with_suffix(".json")

    stim2 = copy.deepcopy(stim)
    for key in stim2.keys():
        # np.ndarrays are not serializable; change to list
        if isinstance(stim2[key], np.ndarray):
            stim2[key] = stim2[key].tolist()

    with filepath.open("w", encoding="utf-8") as file:
        json.dump(stim2, file, ensure_ascii=False, indent=4)


def to_mat(stim, filename):
    """Save stimulus-dict(s) as mat-file

    Parameters
    ----------
    stim : dict
        stimulus dictionary to export.
    filename : Path or str
        (full) path to the file to be created.

    """
    if not isinstance(stim, dict):
        raise ValueError("stim should be a dict")

    filepath = Path(filename).resolve().with_suffix(".mat")

    savemat(filepath, stim)


def to_pickle(stim, filename):
    """Save stimulus-dict(s) as pickle-file

    Parameters
    ----------
    stim : dict
        stimulus dictionary to export.
    filename : Path or str
        (full) path to the file to be created.

    """
    if not isinstance(stim, dict):
        raise ValueError("stim should be a dict")

    filepath = Path(filename).resolve().with_suffix(".pickle")

    stim2 = copy.deepcopy(stim)
    for key in stim2.keys():
        # certain classes can cause problems for pickles; change to list
        if key in ["visual_size", "ppd", "shape"]:
            stim2[key] = list(stim2[key])

    with filepath.open("wb") as file:
        pickle.dump(stim2, file, protocol=pickle.HIGHEST_PROTOCOL)
