import json
import os.path
from hashlib import md5

import numpy as np
import pytest
import stimuli.papers.murray2020
from stimuli.papers.murray2020 import __all__ as stimlist

data_dir = os.path.dirname(__file__)
jsonfile = os.path.join(data_dir, "murray2020.json")
loaded = json.load(open(jsonfile, "r"))


@pytest.mark.parametrize("stim", stimlist)
def test_stim(stim):
    func = getattr(stimuli.papers.murray2020, stim)
    assert (
        md5(np.ascontiguousarray(func()["img"])).hexdigest()
        == loaded[stim]["img"]
    ), "imgs are different"
    assert (
        md5(np.ascontiguousarray(func()["mask"])).hexdigest()
        == loaded[stim]["mask"]
    ), "masks are different"
