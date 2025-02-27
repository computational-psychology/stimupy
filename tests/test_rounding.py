import numpy as np
import pytest

from stimupy.utils import round_to_vals

rng = np.random.default_rng()


@pytest.mark.parametrize("size", [10, 100, 1000, 10000])
@pytest.mark.parametrize("n_vals", [5, 50, 500])
def test_rounding(size, n_vals):
    arr = rng.uniform(0, 1000, (size, size))
    vals = rng.integers(0, 1000, n_vals)
    rounded_arr = round_to_vals(arr, vals)
    assert np.all(np.isin(rounded_arr, vals))
