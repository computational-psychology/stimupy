import json
import os.path

import pytest

import stimupy.papers.carney1999
from stimupy.papers.carney1999 import __all__ as stimlist
from stimupy.utils import export

data_dir = os.path.dirname(__file__)
jsonfile = os.path.join(data_dir, "carney1999.json")
loaded = json.load(open(jsonfile))


@pytest.mark.parametrize("stim_name", stimlist)
def test_stim(stim_name):
    func = getattr(stimupy.papers.carney1999, stim_name)
    stim = export.arrs_to_checksum(func(), keys=["img"])
    assert stim["img"] == loaded[stim_name]["img"], "imgs are different"
