from . import angulars


def create_overview():
    """
    Create dictionary with examples from all stimulus-illusions

    Returns
    -------
    stims : dict
        dict with all stimuli containing individual stimulus dicts.
    """

    p = {
        "visual_size": (10, 10),
        "ppd": 20,
    }

    p_small_grating = {
        "ppd": 20,
        "frequency": 1,
        "intensity_bars": (1, 0),
    }

    # fmt: off
    stims = {
        # Angular
        "pinwheel": angulars.pinwheel(**p, n_segments=8, target_width=1, target_indices=3),
    }
    # fmt: on

    return stims


def overview(mask=False, save=None, extent_key="shape"):
    """
    Plot overview with examples from all stimulus-illusions

    Parameters
    ----------
    mask : bool or str, optional
        If True, plot mask on top of stimulus image (default: False).
        If string is provided, plot this key from stimulus dictionary as mask
    save : None or str, optional
        If None (default), do not save the plot.
        If string is provided, save plot under this name.
    extent_key : str, optional
        Key to extent which will be used for plotting.
        Default is "shape", using the image size in pixels as extent.

    """
    from stimupy.utils import plot_stimuli

    stims = create_overview()

    # Plotting
    plot_stimuli(stims, mask=mask, save=save, extent_key=extent_key)
