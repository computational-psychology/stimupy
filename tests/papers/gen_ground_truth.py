from os.path import abspath, dirname

from stimuli.papers import *
from stimuli.papers import __all__ as papers
from stimuli.utils import export

d = dirname(abspath(__file__))

# Generate the ground_truth dict for each paper; save as .JSON
for paper in papers:
    # Get a reference to the actual module, from the name-string
    paper_module = globals()[paper]

    # Generate all the stimulus-dicts (skip over NotImplemented)
    stims = paper_module.gen_all(skip=True)

    # Convert "img", "mask" to checksums
    for stim in stims.values():
        export.arrs_to_checksum(stim, ["img", "mask"])

    # Save all as .JSON
    export.to_json(stims, f"{d}/{paper}.json")
