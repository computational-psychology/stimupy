import json
from hashlib import md5

import numpy as np


def arrs_to_checksum(stim, keys=["img", "mask"]):
    # Hash (md5) values, and save only the hex
    for key in keys:
        stim[key] = md5(np.ascontiguousarray(stim[key])).hexdigest()

    return stim


def to_json(stim, filename):
    # stimulus-dict(s) as (pretty) JSON
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(stim, f, ensure_ascii=False, indent=4)
