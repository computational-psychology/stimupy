import json
import os.path
from itertools import product

import numpy as np
import pytest

import stimupy.papers.domijan2015
from stimupy.papers.domijan2015 import __all__ as stimlist
from stimupy.utils import export

data_dir = os.path.dirname(__file__)
jsonfile = os.path.join(data_dir, "domijan2015.json")
loaded = json.load(open(jsonfile))


@pytest.mark.parametrize("stim_name", stimlist)
def test_stim(stim_name):
    func = getattr(stimupy.papers.domijan2015, stim_name)
    stim = export.arrays_to_checksum(func(), keys=["img", "target_mask"])
    assert stim["img"] == loaded[stim_name]["img"], "imgs are different"
    assert stim["target_mask"] == loaded[stim_name]["mask"], "masks are different"


@pytest.mark.parametrize("stim_name, ppd", product(stimlist, (8, 10, 12, 14, 18, 20)))
def test_ppd(stim_name, ppd):
    func = getattr(stimupy.papers.domijan2015, stim_name)

    stim = func(ppd=ppd, shape=None)
    reshape = ppd / stimupy.papers.domijan2015.PPD
    target_shape = np.array(stim["original_shape"]) * reshape
    assert np.allclose(target_shape, stim["img"].shape, rtol=1, atol=(2 * (reshape % 1)))
