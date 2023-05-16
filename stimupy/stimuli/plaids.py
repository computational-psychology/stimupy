from stimupy.stimuli import gabors as gabors_stim
from stimupy.stimuli import waves

__all__ = [
    "gabors",
    "sine_waves",
    "square_waves",
]


def add_waves(wave_dict1, wave_dict2, weight1=1, weight2=1):
    """
    Create plaid-like stimulus by adding two waves

    Parameters
    ----------
    wave_dict1 : dict
        dictionary which contains the first wave-array (key: "img"), as well as
        keys "shape" and "ppd"
    wave_dict2 : dict
        dictionary which contains the second wave-array (key: "img"), as well as
        keys "shape" and "ppd"
    weight1 : float, optional
        Factor with which the first wave is multiplied. The default is 1.
    weight2 : float, optional
        Factor with which the second wave is multiplied. The default is 1.

    Returns
    -------
    wave_dict1 : dict
        dictionary with plaid-like stimulus and additional keys if specified.

    """
    if wave_dict1["shape"] != wave_dict2["shape"]:
        raise ValueError(
            f"Waves have different shapes; 1: {wave_dict1['shape']}, 2: {wave_dict2['shape']}"
        )
    if wave_dict1["ppd"] != wave_dict2["ppd"]:
        raise ValueError(
            "Waves have different ppds; 1: {wave_dict1['ppd']}, 2: {wave_dict2['ppd']}"
        )

    img = weight1 * wave_dict1["img"] + weight2 * wave_dict2["img"]
    img = img / (weight1 + weight2)

    # Update parameters
    wave_dict1["img"] = img
    try:
        wave_dict1["grating_mask2"] = wave_dict2["grating_mask"]
        wave_dict1["frequency2"] = wave_dict2["frequency"]
        wave_dict1["phase_width2"] = wave_dict2["phase_width"]
        wave_dict1["n_phases2"] = wave_dict2["n_phases"]
    except Exception:
        pass
    return wave_dict1


def gabors(
    gabor_parameters1,
    gabor_parameters2,
    weight1=1,
    weight2=1,
):
    """Draw plaid consisting of two gabors

    Parameters
    ----------
    gabor_parameters1 : dict
        kwargs to generate first Gabor
    gabor_parameters2 : dict
        kwargs to generate second Gabor
    weight1 : float
        weight of first Gabor (default: 1)
    weight2 : float
        weight of second Gabor (default: 1)

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for each phase (key: "grating_mask"),
        and additional keys containing stimulus parameters
    """

    # Create sine-wave gratings
    grating1 = gabors_stim.gabor(**gabor_parameters1)
    grating2 = gabors_stim.gabor(**gabor_parameters2)
    plaid = add_waves(grating1, grating2, weight1, weight2)

    out = {
        "img": plaid["img"],
        "grating_mask1": plaid["grating_mask"],
        "grating_mask2": plaid["grating_mask2"],
        "gabor_parameters1": gabor_parameters1,
        "gabor_parameters2": gabor_parameters2,
        "weight1": weight1,
        "weight2": weight2,
        "visual_size": plaid["visual_size"],
        "shape": plaid["shape"],
        "ppd": plaid["ppd"],
    }
    return out


def sine_waves(
    grating_parameters1,
    grating_parameters2,
    weight1=1,
    weight2=1,
):
    """Draw plaid consisting of two sine-wave gratings

    Parameters
    ----------
    grating_parameters1 : dict
        kwargs to generate first sine-wave grating
    grating_parameters2 : dict
        kwargs to generate second sine-wave grating
    weight1 : float
        weight of first grating (default: 1)
    weight2 : float
        weight of second grating (default: 1)

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for each phase (key: "grating_mask"),
        and additional keys containing stimulus parameters
    """

    # Create sine-wave gratings
    grating1 = waves.sine_linear(**grating_parameters1)
    grating2 = waves.sine_linear(**grating_parameters2)
    plaid = add_waves(grating1, grating2, weight1, weight2)

    out = {
        "img": plaid["img"],
        "grating_mask1": plaid["grating_mask"],
        "grating_mask2": plaid["grating_mask2"],
        "grating_parameters1": grating_parameters1,
        "grating_parameters2": grating_parameters2,
        "weight1": weight1,
        "weight2": weight2,
        "visual_size": plaid["visual_size"],
        "shape": plaid["shape"],
        "ppd": plaid["ppd"],
    }
    return out


def square_waves(
    grating_parameters1,
    grating_parameters2,
    weight1=1,
    weight2=1,
):
    """Draw plaid consisting of two square-wave gratings

    Parameters
    ----------
    grating_parameters1 : dict
        kwargs to generate first sine-wave grating
    grating_parameters2 : dict
        kwargs to generate second sine-wave grating
    weight1 : float
        weight of first grating (default: 1)
    weight2 : float
        weight of second grating (default: 1)

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for each phase (key: "grating_mask"),
        and additional keys containing stimulus parameters
    """

    # Create sine-wave gratings
    grating1 = waves.square_linear(**grating_parameters1)
    grating2 = waves.square_linear(**grating_parameters2)
    plaid = add_waves(grating1, grating2, weight1, weight2)

    out = {
        "img": plaid["img"],
        "grating_mask1": plaid["grating_mask"],
        "grating_mask2": plaid["grating_mask2"],
        "grating_parameters1": grating_parameters1,
        "grating_parameters2": grating_parameters2,
        "weight1": weight1,
        "weight2": weight2,
        "visual_size": plaid["visual_size"],
        "shape": plaid["shape"],
        "ppd": plaid["ppd"],
    }
    return out


def overview(**kwargs):
    """Generate example stimuli from this module

    Returns
    -------
    stims : dict
        dict with all stimuli containing individual stimulus dicts.
    """
    default_params = {
        "visual_size": 15,
        "ppd": 10,
        "origin": "center",
        "phase_shift": 30,
    }
    default_params.update(kwargs)

    grating1 = {
        **default_params,
        "bar_width": 1,
        "period": "ignore",
        "rotation": 0,
        "round_phase_width": False,
    }

    grating2 = {
        **default_params,
        "bar_width": 0.5,
        "period": "ignore",
        "rotation": 90,
        "round_phase_width": False,
    }

    # fmt: off
    stimuli = {
        "plaid_gabors": gabors({**grating1, "sigma": 3}, {**grating2, "sigma": 3}),
        "plaid_sine_waves": sine_waves(grating1, grating2),
        "plaid_square_waves": square_waves(grating1, grating2),
    }
    # fmt: on

    return stimuli


if __name__ == "__main__":
    from stimupy.utils import plot_stimuli

    stims = overview()
    plot_stimuli(stims, mask=False, save=None)
