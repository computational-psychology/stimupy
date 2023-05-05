import json
import os.path

import pytest

import stimupy.papers.RHS2007
from stimupy.papers.RHS2007 import __all__ as stimlist
from stimupy.utils import export

data_dir = os.path.dirname(__file__)
jsonfile = os.path.join(data_dir, "RHS2007.json")
loaded = json.load(open(jsonfile))


@pytest.mark.parametrize("stim_name", stimlist)
def test_stim(stim_name):
    func = getattr(stimupy.papers.RHS2007, stim_name)
    stim = export.arrays_to_checksum(func(), keys=["img", "target_mask"])
    assert stim["img"] == loaded[stim_name]["img"], "imgs are different"
    assert stim["target_mask"] == loaded[stim_name]["mask"], "masks are different"
