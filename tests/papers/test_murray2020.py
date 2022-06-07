import os.path
import pickle

import numpy as np
import pytest
import stimuli.papers.murray2020
from stimuli.papers.murray2020 import __all__ as stimlist

data_dir = os.path.dirname(__file__)
picklefile = os.path.join(data_dir, "murray2020.pickle")
loaded = pickle.load(open(picklefile, "rb"))


@pytest.mark.parametrize("stim", stimlist)
def test_stim(stim):
    func = getattr(stimuli.papers.murray2020, stim)
    assert np.all(func()["img"] == loaded[stim]["img"]), "imgs are different"
    assert np.all(
        func()["mask"] == loaded[stim]["mask"]
    ), "masks are different"
