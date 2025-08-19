import json
import os.path

import pytest

import stimupy.papers.betz2015
from stimupy.papers.betz2015 import __all__ as stimlist
from stimupy.utils import export

data_dir = os.path.dirname(__file__)
jsonfile = os.path.join(data_dir, "betz2015.json")
loaded = json.load(open(jsonfile))


@pytest.mark.parametrize("stim_name", stimlist)
def test_stim(stim_name):
    import numpy as np

    func = getattr(stimupy.papers.betz2015, stim_name)

    try:  # If function accepts RNG
        rng = np.random.RandomState(1234567890)  # Use legacy RandomState for reproducibility
        stim = func(rng=rng)

    except TypeError:
        # No RNG necessary
        stim = func()

    hashed_stim = export.arrays_to_checksum(stim, keys=["img", "target_mask"])
    assert hashed_stim["img"] == loaded[stim_name]["img"], "imgs are different"
    assert hashed_stim["target_mask"] == loaded[stim_name]["mask"], "masks are different"
