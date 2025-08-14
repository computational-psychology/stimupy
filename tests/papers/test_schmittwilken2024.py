import json
import os.path

import pytest

import stimupy.papers.schmittwilken2024
from stimupy.papers.schmittwilken2024 import __all__ as stimlist
from stimupy.utils import export

data_dir = os.path.dirname(__file__)
jsonfile = os.path.join(data_dir, "schmittwilken2024.json")
loaded = json.load(open(jsonfile))


@pytest.mark.parametrize("stim_name", stimlist)
def test_stim(stim_name):
    func = getattr(stimupy.papers.schmittwilken2024, stim_name)
    stim = export.arrays_to_checksum(func(), keys=["img", "edge_mask"])
    assert stim["img"] == loaded[stim_name]["img"], "imgs are different"
    assert stim["edge_mask"] == loaded[stim_name]["mask"], "masks are different"
