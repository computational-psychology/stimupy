import json
import os.path

import pytest

import stimupy.papers.modelfest
from stimupy.papers.modelfest import __all__ as stimlist
from stimupy.utils import export

data_dir = os.path.dirname(__file__)
<<<<<<< HEAD:tests/papers/test_modelfest.py
jsonfile = os.path.join(data_dir, "modelfest.json")
loaded = json.load(open(jsonfile, "r"))
=======
jsonfile = os.path.join(data_dir, "carney1999.json")
loaded = json.load(open(jsonfile))
>>>>>>> a5203fe9c6aa03c15510f888960e120351f720f8:tests/papers/test_carney1999.py


@pytest.mark.parametrize("stim_name", stimlist)
def test_stim(stim_name):
    func = getattr(stimupy.papers.modelfest, stim_name)
    stim = export.arrs_to_checksum(func(), keys=["img"])
    assert stim["img"] == loaded[stim_name]["img"], "imgs are different"
