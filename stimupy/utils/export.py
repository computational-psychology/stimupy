import copy
import json
import pickle
from hashlib import md5

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
    """Hash (md5) values, and save only the hex

    Parameters
    ----------
    arr : np.ndarray
        Array to be hashed.

    Returns
    ----------
    hex
    """
    return md5(np.ascontiguousarray(arr.round(8))).hexdigest()


def array_to_image(arr, filename, norm=True):
    """Save a 2D numpy array as a grayscale image file.

    Parameters
    ----------
    arr : np.ndarray
        Array to be saved. Values will be cropped to [0,255].
    filename : str
        full path to the file to be created.
    norm : bool
        if True (default), multiply array by 255
    """
    if filename[-4:] != ".png" and filename[-4:] != ".jpg":
        filename += ".png"

    if isinstance(arr, (np.ndarray, list)):
        arr = np.array(arr)

        if norm:
            arr = arr * 255

        if Image:
            imsize = arr.shape
            im = Image.new("L", (imsize[1], imsize[0]))
            im.putdata(arr.flatten())
            im.save(filename)
    else:
        raise ValueError("arr should be a np.ndarray")


def array_to_npy(arr, filename):
    """Save a numpy array to npy-file.

    Parameters
    ----------
    arr : np.ndarray
        Array to be saved.
    filename : str
        full path to the file to be creaated.
    """
    if isinstance(arr, (np.ndarray, list)):
        np.save(filename, arr)
    else:
        raise ValueError("arr should be a np.ndarray")


def array_to_mat(arr, filename):
    """Save a numpy array to a mat-file.

    Parameters
    ----------
    arr : np.ndarray
        Array to be saved.
    filename : str
        full path to the file to be creaated.
    """
    if filename[-4:] != ".mat":
        filename += ".mat"

    if isinstance(arr, (np.ndarray, list)):
        savemat(filename, {"arr": arr})
    else:
        raise ValueError("arr should be a np.ndarray")


def array_to_pickle(arr, filename):
    """Save a numpy array to a pickle-file.

    Parameters
    ----------
    arr : np.ndarray
        Array to be saved.
    filename : str
        full path to the file to be creaated.
    """
    if filename[-7:] != ".pickle":
        filename += ".pickle"

    if isinstance(arr, (np.ndarray, list)):
        with open(filename, "wb") as handle:
            pickle.dump({"arr": arr}, handle, protocol=pickle.HIGHEST_PROTOCOL)
    else:
        raise ValueError("arr should be a np.ndarray")


def array_to_json(arr, filename):
    """Save a numpy array to a (pretty) JSON.

    Parameters
    ----------
    arr : np.ndarray
        Array to be saved.
    filename : str
        full path to the file to be creaated.
    """
    if filename[-5:] != ".json":
        filename += ".json"

    if isinstance(arr, np.ndarray):
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(arr.tolist(), f, ensure_ascii=False, indent=4)
    elif isinstance(arr, list):
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(arr, f, ensure_ascii=False, indent=4)
    else:
        raise ValueError("arr should be a np.ndarray")


def arrays_to_checksum(stim, keys=["img", "mask"]):
    """Hash (md5) values of arrays specified in keys, and save only the hex

    Parameters
    ----------
    stim : dict
        stimulus dictionary containing keys
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
        stimulus dictionary containing keys
    filename : str
        full path to the file to be creaated.

    """
    if filename[-5:] != ".json":
        filename += ".json"

    # stimulus-dict(s) as (pretty) JSON
    if isinstance(stim, dict):
        stim2 = copy.deepcopy(stim)

        for key in stim2.keys():
            # np.ndarrays are not serializable; change to list
            if isinstance(stim2[key], np.ndarray):
                stim2[key] = stim2[key].tolist()

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(stim2, f, ensure_ascii=False, indent=4)
    else:
        raise ValueError("stim should be a dict")


def to_mat(stim, filename):
    """Save stimulus-dict(s) as mat-file

    Parameters
    ----------
    stim : dict
        stimulus dictionary containing keys
    filename : str
        full path to the file to be creaated.

    """
    if filename[-4:] != ".mat":
        filename += ".mat"

    if isinstance(stim, dict):
        savemat(filename, stim)
    else:
        raise ValueError("stim should be a dict")


def to_pickle(stim, filename):
    """Save stimulus-dict(s) as pickle-file

    Parameters
    ----------
    stim : dict
        stimulus dictionary containing keys
    filename : str
        full path to the file to be creaated.

    """
    if filename[-7:] != ".pickle":
        filename += ".pickle"

    if isinstance(stim, dict):
        stim2 = copy.deepcopy(stim)

        for key in stim2.keys():
            # certain classes can cause problems for pickles; change to list
            if key in ["visual_size", "ppd", "shape"]:
                stim2[key] = list(stim2[key])

        with open(filename, "wb") as handle:
            pickle.dump(stim2, handle, protocol=pickle.HIGHEST_PROTOCOL)
    else:
        raise ValueError("stim should be a dict")
