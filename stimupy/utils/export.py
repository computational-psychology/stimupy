import json
from hashlib import md5

import numpy as np
from PIL import Image


def arrs_to_checksum(stim, keys=["img", "mask"]):
    # Hash (md5) values, and save only the hex
    for key in keys:
        stim[key] = md5(np.ascontiguousarray(stim[key])).hexdigest()

    return stim


def to_json(stim, filename):
    # stimulus-dict(s) as (pretty) JSON
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(stim, f, ensure_ascii=False, indent=4)


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
