import json
from hashlib import md5

import numpy as np
from stimuli.papers import *
from stimuli.papers import __all__ as papers


def gen_ground_truth(paper):

    # Get a reference to the actual module, from the name-string
    paper_module = globals()[paper]

    # Extract the list of stimulus functions exported by that paper module
    stimlist = paper_module.__all__

    stims = {}  # save the stimulus-dicts in a larger dict, with name as key
    for stimname in stimlist:
        print(f"Generating {paper}.{stimname}")

        # Get a reference to the actual function
        func = getattr(paper_module, stimname)
        try:
            # Generate the stimulus-dict
            stim = func()

            # Hash (md5) "img" and "mask", and save only the hex
            stim["img"] = md5(np.ascontiguousarray(stim["img"])).hexdigest()
            stim["mask"] = md5(np.ascontiguousarray(stim["mask"])).hexdigest()

            # Accumulate
            stims[stimname] = stim
        except NotImplementedError:
            # Skip stimuli that aren't implemented
            print("-- not implemented")
            pass

    return stims


if __name__ == "__main__":
    from os.path import abspath, dirname

    d = dirname(abspath(__file__))

    # Generate the ground_truth dict for each paper; save as .JSON
    for paper in papers:
        stims = gen_ground_truth(paper)

        # Save the dictionary of stimulus-dicts as (pretty) JSON
        with open(f"{d}/{paper}.json", "w", encoding="utf-8") as f:
            json.dump(stims, f, ensure_ascii=False, indent=4)
