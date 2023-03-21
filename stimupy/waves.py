import itertools

import numpy as np

from stimupy.components import waves

__all__ = [
    "sine_linear",
    "square_linear",
    # "staircase_linear",
    # "sine_radial",
    # "square_radial",
    # "sine_cityblock",
    # "square_cityblock",
    # "sine_angular",
    # "square_angular",
]


def overview(**kwargs):
    """Generate example stimuli from this module

    Returns
    -------
    stims : dict
        dict with all stimuli containing individual stimulus dicts.
    """
    default_params = {"visual_size": 15, "ppd": 30}
    default_params.update(kwargs)

    grating_params = {
        "period": "odd",
        "phase_shift": 30,
        "origin": "center",
        "round_phase_width": False,
        "target_indices": (2, 5),
    }

    # fmt: off
    stimuli = {
        # "sine wave - horizontal": sine_linear(**default_params, **grating_params, bar_width=3.5, rotation=0),
        # "sine wave - vertical": sine_linear(**default_params, **grating_params, bar_width=3.5, rotation=90),
        # "sine wave - oblique": sine_linear(**default_params, **grating_params, bar_width=3.5, rotation=45),

        # "square wave - horizontal": square_linear(**default_params, **grating_params, bar_width=3.5, rotation=0),
        # "square wave - vertical": square_linear(**default_params, **grating_params, bar_width=3.5, rotation=90),
        # "square wave - oblique": square_linear(**default_params, **grating_params, bar_width=3.5, rotation=45),

        # "sine wave - radial": sine(**default_params, **grating_params, base_type="radial"),
        # "sine wave - angular": sine(**default_params, **grating_params, base_type="angular"),
        # "sine wave - cityblock": sine(**default_params, **grating_params, base_type="cityblock"),

        # "square wave - radial": square(**default_params, **grating_params, base_type="radial"),
        # "square wave - angular": square(**default_params, **grating_params, base_type="angular"),
        # "square wave - cityblock": square(**default_params, **grating_params, base_type="cityblock"),

    }
    # fmt: on

    return stimuli


if __name__ == "__main__":
    from stimupy.utils import plot_stimuli

    stims = overview()
    plot_stimuli(stims, mask=False, save=None)
