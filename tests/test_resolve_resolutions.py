import numpy as np
import pytest
from stimuli.utils import resolution


#############################
#   ppd from shape & size   #
#############################
@pytest.mark.parametrize(
    "shape, visual_size, ppd",
    [
        ((1024, 1024), (32, 32), (32, 32)),
        ((1024, 1024), (16, 16), (64, 64)),
        ((512, 512), (32, 32), (16, 16)),
        (1024, (32, 32), (32, 32)),
        ((1024, 1024), 32, (32, 32)),
        ([1024, 768], (32, 48), (32, 16)),
        ([None, None], (32, 24), (None, None)),
        ([512, None], (32, 24), (16, None)),
    ],
)
def test_ppd_from_shape_visual_size(shape, visual_size, ppd):
    out = resolution.ppd_from_shape_visual_size(shape, visual_size)
    assert out.horizontal == ppd[1] and out.vertical == ppd[0]


#############################
#   shape from size & ppd   #
#############################
@pytest.mark.parametrize(
    "shape, visual_size, ppd",
    [
        ((1024, 1024), (32, 32), (32, 32)),
        ((1024, 1024), (16, 16), (64, 64)),
        ((512, 512), (32, 32), (16, 16)),
        #    (1024, (32, 32), (32, 32)),
        ((1024, 1024), 32, (32, 32)),
        ([1024, 768], (32, 48), (32, 16)),
        ([None, None], (32, 24), (None, None)),
        ([512, None], (32, 24), (16, None)),
    ],
)
def test_shape_from_visual_size_ppd(visual_size, ppd, shape):
    out = resolution.shape_from_visual_size_ppd(visual_size, ppd)
    assert out.height == shape[0] and out.width == shape[1]


#############################
#   size from shape & ppd   #
#############################
@pytest.mark.parametrize(
    "shape, visual_size, ppd",
    [
        ((1024, 1024), (32, 32), (32, 32)),
        ((1024, 1024), (16, 16), (64, 64)),
        ((512, 512), (32, 32), (16, 16)),
        (1024, (32, 32), (32, 32)),
        ((1024, 1024), (32, 32), 32),
        ([1024, 768], (32, 48), (32, 16)),
        ([None, None], (None, None), (32, 24)),
        ([512, None], (32, None), (16, 24)),
    ],
)
def test_visual_size_from_shape_ppd(visual_size, ppd, shape):
    out = resolution.visual_size_from_shape_ppd(shape=shape, ppd=ppd)
    assert out.height == visual_size[0] and out.width == visual_size[1]
