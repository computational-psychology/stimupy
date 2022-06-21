import json
import os.path
from hashlib import md5

import pytest
import stimuli.papers.domijan2015
from stimuli.papers.domijan2015 import __all__ as stimlist

data_dir = os.path.dirname(__file__)
jsonfile = os.path.join(data_dir, "domijan2015.json")
loaded = json.load(open(jsonfile, "r"))


@pytest.mark.parametrize("stim", stimlist)
def test_stim(stim):
    func = getattr(stimuli.papers.domijan2015, stim)
    assert (
        md5(func()["img"]).hexdigest() == loaded[stim]["img"]
    ), "imgs are different"
    assert (
        md5(func()["mask"]).hexdigest() == loaded[stim]["mask"]
    ), "masks are different"
