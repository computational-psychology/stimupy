import numpy as np
import pytest
from stimuli.utils import sizes


#############################
#   ppd from shape & size   #
#############################
@pytest.mark.parametrize(
    "shape, visual_size, expected_ppd",
    [
        ((1024, 1024), (32, 32), (32, 32)),
        ((1024, 1024), (16, 16), (64, 64)),
        ((512, 512), (32, 32), (16, 16)),
        (1024, (32, 32), (32, 32)),
        (
            [
                1024,
            ],
            (32, 32),
            (32, 32),
        ),
        ((1024, 1024), 32, (32, 32)),
        ([1024, 768], (32, 48), (32, 16)),
        ([None, None], (32, 24), (None, None)),
        ([512, None], (32, 24), (16, None)),
    ],
)
def test_ppd_from_shape_visual_size(shape, visual_size, expected_ppd):
    ppd = sizes.ppd_from_shape_visual_size(shape, visual_size)
    assert ppd.horizontal == expected_ppd[1] and ppd.vertical == expected_ppd[0]
