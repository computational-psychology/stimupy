import numpy as np
import pytest
from stimuli.utils import sizes


#############################
#    Validate visual size   #
#############################
@pytest.mark.parametrize(
    "visual_size, expected",
    [
        ((32, 32), (32, 32)),
        ((16, 32), (16, 32)),
        ((22.5, 48.1), (22.5, 48.1)),
        ((16), (16, 16)),
        ("32", (32, 32)),
        ((16, "32"), (16, 32)),
        (("16", "32"), (16, 32)),
        ((16.1, None), (16.1, None)),
        ((None, "32"), (None, 32)),
        ((None, None), (None, None)),
    ],
)
def test_validate_visual_size(visual_size, expected):
    out = sizes.validate_visual_size(visual_size)
    assert out.width == expected[0] and out.height == expected[1]


@pytest.mark.parametrize(
    "visual_size, exception",
    [
        ("bla", ValueError),
        ((32, 32, 32), TypeError),
        ({32, 32}, TypeError),
        ((-32, 16), ValueError),
        ((16, 0), ValueError),
    ],
)
def test_raises_visual_size(visual_size, exception):
    with pytest.raises(exception) as e_info:
        sizes.validate_visual_size(visual_size)


#############################
#       Validate shape      #
#############################
@pytest.mark.parametrize(
    "shape, expected",
    [
        ((32, 32), (32, 32)),
        ((16, 32), (16, 32)),
        ((22.5, 48.1), (22, 48)),
        ((16), (16, 16)),
        ("32", (32, 32)),
        ((16, "32"), (16, 32)),
        (("16", "32"), (16, 32)),
    ],
)
def test_validate_shape(shape, expected):
    out = sizes.validate_shape(shape)
    assert out.width == expected[0] and out.height == expected[1]


@pytest.mark.parametrize(
    "shape, exception",
    [
        ("bla", ValueError),
        ((32, 32, 32), TypeError),
        ({32, 32}, TypeError),
        ((-32, 16), ValueError),
        ((16, 0), ValueError),
    ],
)
def test_raises_shape(shape, exception):
    with pytest.raises(exception) as e_info:
        sizes.validate_shape(shape)


############################
#       Validate ppd       #
############################
@pytest.mark.parametrize(
    "ppd, expected",
    [
        ((32, 32), (32, 32)),
        ((16, 32), (16, 32)),
        ((22.5, 48.1), (22, 48)),
        ((16), (16, 16)),
        ("32", (32, 32)),
        ((16, "32"), (16, 32)),
        (("16", "32"), (16, 32)),
    ],
)
def test_validate_ppd(ppd, expected):
    out = sizes.validate_ppd(ppd)
    assert out.horizontal == expected[0] and out.vertical == expected[1]


@pytest.mark.parametrize(
    "ppd, exception",
    [
        ("bla", ValueError),
        ((32, 32, 32), TypeError),
        ({32, 32}, TypeError),
        ((-32, 16), ValueError),
        ((16, 0), ValueError),
    ],
)
def test_raises_ppd(ppd, exception):
    with pytest.raises(exception) as e_info:
        sizes.validate_ppd(ppd)
