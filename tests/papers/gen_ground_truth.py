from os.path import abspath, dirname

from stimupy.papers import *
from stimupy.papers import __all__ as papers
from stimupy.utils import export

d = dirname(abspath(__file__))

# Generate the ground_truth dict for each paper; save as .JSON
for paper in papers:
    # Get a reference to the actual module, from the name-string
    paper_module = globals()[paper]

    # Generate all the stimulus-dicts (skip over NotImplemented)
    stims = paper_module.gen_all(skip=True)

    # Convert "img", "mask" to checksums
    for stim in stims.values():
        img = stim["img"]

        # If target_mask exists, use it.
        mask_keys = [key for key in stim.keys() if key.endswith("mask")]
        if "target_mask" in mask_keys:
            mask = stim["target_mask"]
        else:
            mask = stim[mask_keys[0]]

        stim.clear()
        stim["img"] = img
        stim["mask"] = mask
        export.arrays_to_checksum(stim, ["img", "mask"])

    # Save all as .JSON
    export.to_json(stims, f"{d}/{paper}.json")
