"""Tests whether validation of resolution components works as expected

Seperately tests each of three components: visual size, shape, ppd.
For each component, the validation routine has two expected major behaviors:
- if input is valid, return canonical format (2-(named)tuple)
  - casts values to correct type (float or int)
  - expands 1D to 2D, i.e., if 1 value is provided, uses it for both dimensions
- if input is not valid, raise specific exceptions:
  - ValueError if input cannot be cast
  - ValueError if values are not in accepted ranges, i.e., not positive
  - TypeError if input is not a 1-Sequence or 2-Sequence

The tests do this through parameterization:
pytest runs each test for each of the specified parameter sets.

For the valid-input tests, each parameter set specifies the (valid) input,
and value (in canonical form) that should be returned.
If the actual returned value matches this expected return value, the test passes.

For the invalid-input tests, each parameter set specifies the (invalid) input,
and the Exception that should be raised.
If the function under testing raises this specified exception, the test passes.
"""

import pytest

from stimupy.utils import resolution


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
        (None, (None, None)),
    ],
)
def test_valid_visual_size(visual_size, expected):
    out = resolution.validate_visual_size(visual_size)
    assert out.width == expected[1] and out.height == expected[0]


@pytest.mark.parametrize(
    "visual_size, exception",
    [
        ((), TypeError),
        ("bla", ValueError),
        ((32, 32, 32), TypeError),
        ({32, 32}, TypeError),
        ((-32, 16), ValueError),
        ((16, -1), ValueError),
    ],
)
def test_invalid_visual_size(visual_size, exception):
    with pytest.raises(exception):
        resolution.validate_visual_size(visual_size)


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
        ((16.1, None), (16, None)),
        ((None, "32"), (None, 32)),
        ((None, None), (None, None)),
        (None, (None, None)),
    ],
)
def test_valid_shape(shape, expected):
    out = resolution.validate_shape(shape)
    assert out.width == expected[1] and out.height == expected[0]


@pytest.mark.parametrize(
    "shape, exception",
    [
        ((), TypeError),
        ("bla", ValueError),
        ((32, 32, 32), TypeError),
        ({32, 32}, TypeError),
        ((-32, 16), ValueError),
        ((16, 0), ValueError),
    ],
)
def test_invalid_shape(shape, exception):
    with pytest.raises(exception):
        resolution.validate_shape(shape)


############################
#       Validate ppd       #
############################
@pytest.mark.parametrize(
    "ppd, expected",
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
        (None, (None, None)),
    ],
)
def test_valid_ppd(ppd, expected):
    out = resolution.validate_ppd(ppd)
    assert out.horizontal == expected[1] and out.vertical == expected[0]


@pytest.mark.parametrize(
    "ppd, exception",
    [
        ((), TypeError),
        ("bla", ValueError),
        ((32, 32, 32), TypeError),
        ({32, 32}, TypeError),
        ((-32, 16), ValueError),
        ((16, 0), ValueError),
    ],
)
def test_invalid_ppd(ppd, exception):
    with pytest.raises(exception):
        resolution.validate_ppd(ppd)
