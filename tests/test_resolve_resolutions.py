"""Tests whether resolving of resolution/components works as expected

Seperately tests each of three components: visual size, shape, ppd.
For each component, the resolver routine has 1 expected behavior:
from the two givens, calculate the third unknown component.
As long as the two givens are valid (see valid_*),
the output will be the third component in canonical form.

Also tests the overall resolving: given three inputs with one None, resolve the unknown.
This function has two expected behaviors:
- if the resolution can be resolved, i.e., there is just 1 unknown per dimension,
returns all three components in canonical form
- if the resolution cannot be resolved, i.e., there is more than 1 unknown in a dimension,
raises a ValueError.

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


#############################
#    resolve resolution     #
#############################
@pytest.mark.parametrize(
    "shape, visual_size, ppd",
    [
        ((1024, 1024), (32, 32), (32, 32)),  # Already resolved
        (None, (32, 32), (32, 32)),  # One unknown
        ((1024, 1024), None, (32, 32)),  # One unknown
        ((1024, 1024), (32, 32), None),  # One unknown
        ((None, 1024), (32, None), (32, 32)),  # One unknown in each dimension
        ((None, 1024), (32, 32), (32, None)),  # One unknown in each dimension
        ((1024, None), (32, 32), (None, 32)),  # One unknown in each dimension
        (1024, 32, None),
    ],
)
def test_resolve_resolution(shape, visual_size, ppd):
    shape, visual_size, ppd = resolution.resolve(shape=shape, visual_size=visual_size, ppd=ppd)
    resolution.valid_resolution(shape=shape, visual_size=visual_size, ppd=ppd)


@pytest.mark.parametrize(
    "shape, visual_size, ppd",
    [
        (None, None, (32, 32)),  # Two unkowns
        ((1024, 1024), None, None),  # Two unkowns
        (None, (32, 32), None),  # Two unkowns
        ((1024, None), (32, None), (32, 32)),  # Two unkowns in one dimension
        ((1024, 1024), (32, None), (32, None)),  # Two unkowns in one dimension
        ((1024, None), (32, 32), (32, None)),  # Two unkowns in one dimension
    ],
)
def test_too_many_unknowns(shape, visual_size, ppd):
    with pytest.raises(ValueError):
        resolution.resolve(shape=shape, visual_size=visual_size, ppd=ppd)
