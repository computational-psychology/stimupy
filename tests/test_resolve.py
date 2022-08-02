import pytest
from stimuli.utils import resolution


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
def test_pass_valid_resolution(shape, visual_size, ppd):
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
    ),
)
def test_raises_valid_resolution(shape, visual_size, ppd):
    with pytest.raises(ValueError) as e_info:
        resolution.valid_resolution(shape=shape, visual_size=visual_size, ppd=ppd)


def test_resolve():
    pass
