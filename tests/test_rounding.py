import numpy as np
import pytest

from stimupy.utils import round_to_vals

rng = np.random.default_rng()


@pytest.mark.parametrize("size", [10, 100, 1000, 10000])
@pytest.mark.parametrize("n_vals", [5, 50, 500])
@pytest.mark.parametrize("mode", ["nearest", "floor", "ceil"])
def test_rounding(size, n_vals, mode):
    vals = rng.integers(0, 1000, n_vals)
    arr = rng.uniform(vals.min(), vals.max(), (size, size))
    rounded_arr = round_to_vals(arr, vals, mode)

    assert np.all(np.isin(rounded_arr, vals))
    if mode == "floor":
        assert np.all(rounded_arr <= arr)
    elif mode == "ceil":
        assert np.all(rounded_arr >= arr)


def test_raises_oob():
    with pytest.raises(ValueError):
        round_to_vals([0], [1, 2], "floor")

    with pytest.raises(ValueError):
        round_to_vals([3], [1, 2], "ceil")
