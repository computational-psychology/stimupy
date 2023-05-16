from stimupy.components import waves
from stimupy.components.gaussians import gaussian

__all__ = ["gabor"]


def gabor(
    visual_size=None,
    ppd=None,
    shape=None,
    frequency=None,
    n_bars=None,
    bar_width=None,
    period="ignore",
    rotation=0.0,
    phase_shift=0,
    intensity_bars=(0.0, 1.0),
    origin="center",
    round_phase_width=False,
    sigma=None,
):
    """Draw a Gabor: a sinewave grating in a Gaussian envelope

    Parameters
    ----------
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of image, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of image, in pixels
    frequency : Number, or None (default)
        spatial frequency of grating, in cycles per degree visual angle
    n_bars : Number, or None (default)
        number of bars in the grating
    bar_width : Number, or None (default)
        width of a single bar, in degrees visual angle
    sigma : float or (float, float)
        sigma of Gaussian in degree visual angle (y, x)
    period : "even", "odd", "either" or "ignore" (default)
        ensure whether the grating has "even" number of phases, "odd"
        number of phases, either or whether not to round the number of
        phases ("ignore")
    rotation : float, optional
        rotation (in degrees), counterclockwise, by default 0.0 (horizonal)
    phase_shift : float
        phase shift of grating in degrees
    intensity_bars : Sequence[float, ...]
        maximal intensity value for each bar, by default (0.0, 1.0).
    origin : "corner", "mean" or "center"
        if "corner": set origin to upper left corner
        if "mean": set origin to hypothetical image center (default)
        if "center": set origin to real center (closest existing value to mean)

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for each bar (key: "grating_mask"),
        and additional keys containing stimulus parameters
    """
    if sigma is None:
        raise ValueError("gabor() missing argument 'sigma' which is not 'None'")

    stim = waves.sine(
        visual_size=visual_size,
        ppd=ppd,
        shape=shape,
        frequency=frequency,
        n_phases=n_bars,
        phase_width=bar_width,
        period=period,
        rotation=rotation,
        phase_shift=phase_shift,
        intensities=intensity_bars,
        origin=origin,
        distance_metric="oblique",
        round_phase_width=round_phase_width,
    )

    gaussian_window = gaussian(
        visual_size=visual_size,
        ppd=ppd,
        sigma=sigma,
        origin=origin,
    )
    mean_int = (intensity_bars[0] + intensity_bars[1]) / 2
    stim["img"] = (stim["img"] - mean_int) * gaussian_window["img"] + mean_int
    del stim["intensities"]

    return {
        **stim,
        "sigma": sigma,
        "gaussian_mask": gaussian_window["gaussian_mask"],
        "intensity_bars": intensity_bars,
    }


def overview(**kwargs):
    """Generate example stimuli from this module

    Returns
    -------
    stims : dict
        dict with all stimuli containing individual stimulus dicts.
    """
    default_params = {
        "visual_size": 10,
        "ppd": 20,
        "rotation": 45,
    }
    default_params.update(kwargs)

    # fmt: off
    stimuli = {
        "gabor": gabor(**default_params, frequency=1, sigma=2, phase_shift=0, round_phase_width=False, origin="center"),
    }
    # fmt: on

    return stimuli


if __name__ == "__main__":
    from stimupy.utils import plot_stimuli

    stims = overview()
    plot_stimuli(stims, mask=False, save=None)
