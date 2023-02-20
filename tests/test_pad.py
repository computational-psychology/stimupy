import numpy as np
import pytest

from stimupy.utils import pad, resolution


@pytest.mark.parametrize(
    "img_shape, padding, result",
    [
        ((128, 128), (64, 64), (256, 256)),
        ((100, 100), (64, 64), (228, 228)),
        ((128, 128), ((64, 64), (64, 64)), (256, 256)),
        ((128, 128), ((64, 64), (128, 128)), (256, 384)),
        ((128, 100), ((64, 64), (100, 128)), (256, 328)),
        ((128, 100), 64, (256, 228)),
    ],
)
def test_pad_by_shape(img_shape, padding, result):
    img = np.ones(img_shape)
    padded = pad.pad_by_shape(img, padding)
    assert padded.shape == result


@pytest.mark.parametrize(
    "img_shape, shape",
    [
        ((128, 128), (256, 256)),
        ((100, 100), (228, 228)),
        ((128, 128), (256, 256)),
        ((128, 128), (256, 384)),
        ((128, 100), (256, 328)),
        ((128, 100), (256, 228)),
    ],
)
def test_pad_to_shape(img_shape, shape):
    img = np.ones(img_shape)
    padded = pad.pad_to_shape(img, shape)
    assert padded.shape == shape


@pytest.mark.parametrize(
    "img_shape, padding, ppd, result_shape",
    [
        ((128, 128), (4.0, 4.0), (32, 32), (384, 384)),
        ((100, 100), (2.0, 2.0), (32, 32), (228, 228)),
        ((128, 128), ((2.0, 2.0), (2.0, 2.0)), 32, (256, 256)),
        ((128, 128), ((1.0, 1.0), (2.0, 2.0)), 64, (256, 384)),
        ((128, 100), ((6.4, 6.4), (10, 12.8)), 10, (256, 328)),
        ((128, 100), 8, 8, (256, 228)),
    ],
)
def test_pad_by_visual_size(img_shape, padding, ppd, result_shape):
    img = np.ones(img_shape)
    padded = pad.pad_by_visual_size(img, padding, ppd)
    assert padded.shape == result_shape


@pytest.mark.parametrize(
    "img_shape, visual_size, ppd",
    [
        ((256, 256), (32.0, 32.0), 32),
        ((100, 100), (32.0, 32.0), 32),
        ((256, 256), (32.0, 16.0), (16, 16)),
        ((256, 256), (32.0, 16.0), (16, 32)),
    ],
)
def test_pad_to_visual_size(img_shape, visual_size, ppd):
    img = np.ones(img_shape)
    padded = pad.pad_to_visual_size(img=img, visual_size=visual_size, ppd=ppd)
    result_shape = resolution.shape_from_visual_size_ppd(visual_size=visual_size, ppd=ppd)
    assert padded.shape == result_shape
