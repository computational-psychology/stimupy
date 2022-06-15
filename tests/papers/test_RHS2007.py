import json
import os.path
from hashlib import sha1

import pytest
import stimuli.papers.RHS2007
from stimuli.papers.RHS2007 import __all__ as stimlist

data_dir = os.path.dirname(__file__)
jsonfile = os.path.join(data_dir, "RHS2007.json")
loaded = json.load(open(jsonfile, "r"))


@pytest.mark.parametrize("stim", stimlist)
def test_stim(stim):
    func = getattr(stimuli.papers.RHS2007, stim)
    assert (
        sha1(func()["img"]).hexdigest() == loaded[stim]["img"]
    ), "imgs are different"
    assert (
        sha1(func()["mask"]).hexdigest() == loaded[stim]["mask"]
    ), "masks are different"
