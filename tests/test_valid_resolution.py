"""Tests whether validation of resolution specification works as expected

Tests the combined specification of shape (in pixels), visual_size (deg) and ppd.
If this makes sense, i.e. roughly, int(visual_size * ppd) == shape,
function should pass without output.
If it does not make sense, function should raise a ResolutionError.

The tests do this through parameterization:
pytest runs each test for each of the specified parameter sets.

For the valid-input tests, each parameter set specifies the (valid) input,
and value (in canonical form) that should be returned.
If the actual returned value matches this expected return value, the test passes.

For the invalid-input tests, each parameter set specifies the (invalid) input,
and the function should raise a ResolutionError for each of these.
"""
import pytest

from stimupy.utils import resolution


@pytest.mark.parametrize(
    "shape, visual_size, ppd",
    (
        ((1024, 1024), (32, 32), (32, 32)),
        ((1024, 1024), (32, 16), (32, 64)),
        ((512, 1024), (16, 64), (32, 16)),
        ((500, 400), (20, 40), (25, 10)),
        (1024, (32, 32), (32, 32)),
        ((1024, 1024), 32, (32, 32)),
        ((1024, 1024), (32, 32), 32),
    ),
)
def test_valid_resolution(shape, visual_size, ppd):
    resolution.valid_resolution(shape=shape, visual_size=visual_size, ppd=ppd)


@pytest.mark.parametrize(
    "shape, visual_size, ppd",
    (
        ((1024, 1024), (32, 32), (16, 16)),
        ((1024, 1024), (32, 16), (32, 32)),
        ((512, 1024), (32, 32), (32, 32)),
        ((500, 400), (20, 20), (25, 10)),
        (1024, (32, 16), (32, 32)),
        ((1024, 512), 32, (32, 30)),
        ((1024, 512), (32, 32), 32),
        ((1024, None), (32, 32), (32, 32)),
        ((1024, 1024), (32, None), (32, 32)),
        ((1024, 1024), (32, 32), (None, 32)),
        ((1024, None), (32, 32), (32, 32)),
        ((1024, 1024), (32, None), (32, 32)),
        (None, (32, 32), (32, 32)),
        ((1024, 1024), None, (32, 32)),
        ((1024, 1024), (32, 32), None),
    ),
)
def test_invalid_resolution(shape, visual_size, ppd):
    with pytest.raises(resolution.ResolutionError):
        resolution.valid_resolution(shape=shape, visual_size=visual_size, ppd=ppd)
