import json
from hashlib import md5

import numpy as np
from PIL import Image

__all__ = [
    "array_to_checksum",
    "array_to_image",
    "arrays_to_checksum",
    "to_json",
]


def array_to_checksum(arr):
    """
    Hash (md5) values, and save only the hex

    Parameters
    ----------
    arr : np.ndarray

    Returns
    ----------
    hex
    """
    return md5(np.ascontiguousarray(arr.round(8))).hexdigest()


def array_to_image(arr, filename):
    """
    Save a 2D numpy array as a grayscale image file.

    Parameters
    ----------
    arr : np.ndarray
        The data to be stored in the image. Values will be cropped to [0,255].
    filename : str
        full path to the file to be creaated.
    """
    if Image:
        imsize = arr.shape
        im = Image.new("L", (imsize[1], imsize[0]))
        im.putdata(arr.flatten())
        im.save(filename)


def arrays_to_checksum(stim, keys=["img", "mask"]):
    """
    Hash (md5) values of arrays specified in keys, and save only the hex

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
    """
    Stimulus-dict(s) as (pretty) JSON

    Parameters
    ----------
    stim : dict
        stimulus dictionary containing keys
    filename : str
        full path to the file to be creaated.

    """
    # stimulus-dict(s) as (pretty) JSON
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(stim, f, ensure_ascii=False, indent=4)
