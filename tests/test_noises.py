import numpy as np
import pytest

from stimupy.noises import binaries, narrowbands, naturals, whites


def get_noise_functions():
    return [
        binaries.binary,
        narrowbands.narrowband,
        naturals.one_over_f,
        naturals.pink,
        naturals.brown,
        whites.white,
    ]


@pytest.mark.parametrize("func", get_noise_functions())
def test_noise_reproducibility(func):
    # Create a fixed RNG
    seed = 12345
    rng1 = np.random.default_rng(seed)
    rng2 = np.random.default_rng(seed)

    # Minimal required arguments for each function
    kwargs = {
        "ppd": 32,
        "visual_size": 10,
    }
    # Some functions require extra args
    if func is narrowbands.narrowband:
        kwargs.update({"center_frequency": 2, "bandwidth": 1})
    if func is naturals.one_over_f:
        kwargs.update({"exponent": 1.0})

    # Call twice with two RNGs
    stim1 = func(rng=rng1, **kwargs)
    stim2 = func(rng=rng2, **kwargs)

    # Compare outputs
    np.testing.assert_allclose(stim1["img"], stim2["img"], atol=1e-12)
