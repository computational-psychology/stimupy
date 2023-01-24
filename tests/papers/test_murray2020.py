import json
import os.path

import pytest
import stimuli.papers.murray2020
from stimuli.papers.murray2020 import __all__ as stimlist
from stimuli.utils import export

data_dir = os.path.dirname(__file__)
jsonfile = os.path.join(data_dir, "murray2020.json")
loaded = json.load(open(jsonfile, "r"))


@pytest.mark.parametrize("stim_name", stimlist)
def test_checksum(stim_name):
    func = getattr(stimuli.papers.murray2020, stim_name)
    stim = export.arrs_to_checksum(func(), keys=["img", "target_mask"])
    assert stim["img"] == loaded[stim_name]["img"], "imgs are different"
    assert stim["target_mask"] == loaded[stim_name]["mask"], "masks are different"


@pytest.mark.parametrize("stim_name", stimlist)
def test_normalization(stim_name):
    func = getattr(stimuli.papers.murray2020, stim_name)
    stim = func()
    assert stim["img"].min() == 0, "img minimum is not 0"
    assert stim["img"].max() == 1, "img max is not 1"
    assert "original_range" in stim, "No original_range in output stimulus-dict"
