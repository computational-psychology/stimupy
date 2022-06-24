import json
import os.path

import pytest
import stimuli.papers.RHS2007
from stimuli.papers.RHS2007 import __all__ as stimlist
from stimuli.utils import export

data_dir = os.path.dirname(__file__)
jsonfile = os.path.join(data_dir, "RHS2007.json")
loaded = json.load(open(jsonfile, "r"))


@pytest.mark.parametrize("stim_name", stimlist)
def test_stim(stim_name):
    func = getattr(stimuli.papers.RHS2007, stim_name)
    stim = export.arrs_to_checksum(func(), keys=["img", "mask"])
    assert stim["img"] == loaded[stim_name]["img"], "imgs are different"
    assert stim["mask"] == loaded[stim_name]["mask"], "masks are different"
