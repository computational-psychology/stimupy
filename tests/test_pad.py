import numpy as np
import pytest

from stimuli.utils import pad


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
