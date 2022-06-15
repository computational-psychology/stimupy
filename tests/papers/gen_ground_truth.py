import json
from hashlib import sha1

import numpy as np


def ground_truth_RHS2007():
    import stimuli.papers.RHS2007
    from stimuli.papers.RHS2007 import __all__ as stimlist

    stims = {}
    for stimname in stimlist:
        print("Generating " + "RHS2007." + stimname)
        func = getattr(stimuli.papers.RHS2007, stimname)
        try:
            stim = func()
            stim["img"] = sha1(stim["img"]).hexdigest()
            stim["mask"] = sha1(stim["mask"]).hexdigest()
            stims[stimname] = stim
        except NotImplementedError:
            print("-- not implemented")

    with open("RHS2007.json", "w", encoding="utf-8") as f:
        json.dump(stims, f, ensure_ascii=False, indent=4)


def ground_truth_domijan2015():
    import stimuli.papers.domijan2015
    from stimuli.papers.domijan2015 import __all__ as stimlist

    stims = {}
    for stimname in stimlist:
        print("Generating " + "domijan2015." + stimname)
        func = getattr(stimuli.papers.domijan2015, stimname)
        try:
            stim = func()
            stim["img"] = sha1(stim["img"]).hexdigest()
            stim["mask"] = sha1(stim["mask"]).hexdigest()
            stims[stimname] = stim
        except NotImplementedError:
            print("-- not implemented")

    with open("domijan2015.json", "w", encoding="utf-8") as f:
        json.dump(stims, f, ensure_ascii=False, indent=4)


def ground_truth_murray2020():
    import stimuli.papers.murray2020
    from stimuli.papers.murray2020 import __all__ as stimlist

    stims = {}
    for stimname in stimlist:
        print("Generating " + "murray2020." + stimname)
        func = getattr(stimuli.papers.murray2020, stimname)
        try:
            stim = func()
            stim["img"] = sha1(np.ascontiguousarray(stim["img"])).hexdigest()
            stim["mask"] = sha1(np.ascontiguousarray(stim["mask"])).hexdigest()
            stims[stimname] = stim
        except NotImplementedError:
            print("-- not implemented")

    with open("murray2020.json", "w", encoding="utf-8") as f:
        json.dump(stims, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    ground_truth_domijan2015()
    ground_truth_murray2020()
    ground_truth_RHS2007()
