import warnings

import numpy as np

from stimupy.components.gratings import square_wave

__all__ = [
    "checkerboard",
]

# TODO: Fix bug that changing rotation, affect check size!


def checkerboard(
    visual_size=None,
    ppd=None,
    shape=None,
    frequency=None,
    board_shape=None,
    check_visual_size=None,
    period="ignore",
    rotation=0,
    intensity_checks=(1.0, 0.0),
    round_phase_width=True,
):
    """Draws a checkerboard with given specifications

    Parameters
    ----------
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size of the total board [height, width] in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] in pixels
    frequency : Sequence[Number, Number], Number, or None (default)
        frequency of checkerboard in [y, x] in cpd
    board_shape : Sequence[Number, Number], Number, or None (default)
        number of checks in [height, width] of checkerboard
    check_visual_size : Sequence[Number, Number], Number, or None (default)
        visual size of a single check [height, width] in degrees
    period : "even", "odd", "either" or "ignore" (default)
        ensure whether the grating has "even" number of phases, "odd"
        number of phases, either or whether not to round the number of
        phases ("ignore")
    rotation : Number
        rotation of grating in degrees (default: 0 = horizontal)
    intensity_checks : Sequence[float, float]
        intensity values of checks, by default (1.0, 0.0)

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for each check (key: "checker_mask"),
        and additional keys containing stimulus parameters
    """
    lst = [visual_size, ppd, shape, frequency, board_shape, check_visual_size]
    if len([x for x in lst if x is not None]) < 3:
        raise ValueError(
            "'checkerboard()' needs 3 non-None arguments for resolving from 'visual_size', "
            "'ppd', 'shape', 'frequency', 'board_shape', 'check_visual_size'"
        )

    if isinstance(frequency, (float, int)) or frequency is None:
        frequency = (frequency, frequency)
    if isinstance(board_shape, (float, int)) or board_shape is None:
        board_shape = (board_shape, board_shape)
    if isinstance(check_visual_size, (float, int)) or check_visual_size is None:
        check_visual_size = (check_visual_size, check_visual_size)

    create_twice = visual_size is None and shape is None

    # Create checkerboard by treating it as a plaid
    sw1 = square_wave(
        visual_size=visual_size,
        ppd=ppd,
        shape=shape,
        frequency=frequency[0],
        n_bars=board_shape[0],
        bar_width=check_visual_size[0],
        period=period,
        rotation=rotation,
        phase_shift=0,
        intensity_bars=intensity_checks,
        origin="corner",
        round_phase_width=round_phase_width,
    )

    sw2 = square_wave(
        visual_size=visual_size,
        ppd=ppd,
        shape=shape,
        frequency=frequency[1],
        n_bars=board_shape[1],
        bar_width=check_visual_size[1],
        period=period,
        rotation=rotation + 90,
        phase_shift=0,
        intensity_bars=intensity_checks,
        origin="corner",
        round_phase_width=round_phase_width,
    )

    # If neither a visual_size nor a shape was given, each square wave
    # grating is always a square. An easy solution is to just recreate
    # both gratings with the resolved parameters
    if create_twice:
        warnings.filterwarnings("ignore")
        sw1 = square_wave(
            visual_size=(sw1["visual_size"][0], sw2["visual_size"][1]),
            ppd=sw1["ppd"],
            shape=None,
            frequency=frequency[0],
            n_bars=board_shape[0],
            bar_width=check_visual_size[0],
            period=period,
            rotation=rotation,
            phase_shift=0,
            intensity_bars=intensity_checks,
            origin="corner",
            round_phase_width=round_phase_width,
        )

        sw2 = square_wave(
            visual_size=(sw1["visual_size"][0], sw2["visual_size"][1]),
            ppd=sw1["ppd"],
            shape=None,
            frequency=frequency[1],
            n_bars=board_shape[1],
            bar_width=check_visual_size[1],
            period=period,
            rotation=rotation + 90,
            phase_shift=0,
            intensity_bars=intensity_checks,
            origin="corner",
            round_phase_width=round_phase_width,
        )
        warnings.filterwarnings("default")

    # Add the two square-wave gratings into a checkerboard
    img = sw1["img"] + sw2["img"]
    img = np.where(
        img == intensity_checks[0] + intensity_checks[1], intensity_checks[1], intensity_checks[0]
    )

    # Create a mask with target indices for each check
    mask = sw1["grating_mask"] + sw2["grating_mask"] * sw1["grating_mask"].max() * 10
    unique_vals = np.unique(mask)
    for v in range(len(unique_vals)):
        mask[mask == unique_vals[v]] = v + 1

    stim = {
        "img": img,
        "checker_mask": mask.astype(int),
        "visual_size": sw1["visual_size"],
        "ppd": sw1["ppd"],
        "shape": sw1["shape"],
        "frequency": (sw2["frequency"], sw1["frequency"]),
        "board_shape": (sw2["n_bars"], sw1["n_bars"]),
        "check_visual_size": (sw2["bar_width"], sw1["bar_width"]),
        "period": period,
        "rotation": rotation,
        "intensity_checks": intensity_checks,
        "edges": (sw1["edges"], sw2["edges"]),
    }
    return stim
