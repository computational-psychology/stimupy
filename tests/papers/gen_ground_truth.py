from os.path import abspath, dirname

from stimupy.papers import *  # noqa: F403
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
        elif mask_keys:
            mask = stim[mask_keys[0]]
        else:
            mask = None

        stim.clear()
        stim["img"] = img
        keys = ["img"]
        if mask is not None:
            stim["mask"] = mask
            keys += ["mask"]
        export.arrays_to_checksum(stim, keys)

    # Save all as .JSON
    export.to_json(stims, f"{d}/{paper}.json")