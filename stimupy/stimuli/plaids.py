from stimupy.components import waves
from stimupy.components.gaussians import gaussian

__all__ = [
    "plaid",
]


def plaid(
    grating_parameters1,
    grating_parameters2,
    weight1=1,
    weight2=1,
    sigma=None,
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
    sigma : float or (float, float)
        sigma of Gaussian window in degree visual angle (y, x)

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for each phase (key: "grating_mask"),
        and additional keys containing stimulus parameters
    """
    if sigma is None:
        raise ValueError("plaid() missing argument 'sigma' which is not 'None'")

    # Create sine-wave gratings
    grating1 = waves.sine(**grating_parameters1)
    grating2 = waves.sine(**grating_parameters2)

    if grating1["shape"] != grating2["shape"]:
        raise ValueError("Gratings must have the same shape")
    if grating1["ppd"] != grating2["ppd"]:
        raise ValueError("Gratings must have same ppd")
    if grating1["origin"] != grating2["origin"]:
        raise ValueError("Grating origins must be the same")

    # Create Gaussian window
    window = gaussian(
        visual_size=grating1["visual_size"],
        ppd=grating1["ppd"],
        sigma=sigma,
        origin=grating1["origin"],
    )

    img = (weight1 * grating1["img"] + weight2 * grating2["img"]) * window["img"]
    img = img / (weight1 + weight2)

    # Update parameters
    grating1["img"] = img
    grating1["sigma"] = sigma
    grating1["grating_mask2"] = grating2["grating_mask"]
    grating1["frequency2"] = grating2["frequency"]
    grating1["phase_width2"] = grating2["phase_width"]
    grating1["n_phases2"] = grating2["n_phases"]
    grating1["gaussian_mask"] = window["gaussian_mask"]
    return grating1


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
        "distance_metric": "oblique",
    }
    default_params.update(kwargs)

    grating1 = {
        **default_params,
        "phase_width": 3.5,
        "period": "odd",
        "rotation": 0,
        "round_phase_width": False,
    }

    grating2 = {
        **default_params,
        "phase_width": 3.5,
        "period": "ignore",
        "rotation": 90,
        "round_phase_width": False,
    }

    # fmt: off
    stimuli = {
        "plaid": plaid(grating1, grating2, sigma=4.0),
    }
    # fmt: on

    return stimuli


if __name__ == "__main__":
    from stimupy.utils import plot_stimuli

    stims = overview()
    plot_stimuli(stims, mask=False, save=None)
