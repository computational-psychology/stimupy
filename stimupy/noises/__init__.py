from .binaries import *
from .narrowbands import *
from .naturals import *
from .utils import *
from .whites import *


def create_overview():
    """
    Create dictionary with examples from all stimulus-noises

    Returns
    -------
    stims : dict
        dict with all stimuli containing individual stimulus dicts.
    """

    params = {
        "visual_size": 10,
        "ppd": 10,
        "pseudo_noise": True,
    }

    # fmt: off
    stims = {
        # Binary
        "binary_noise": binary(visual_size=10, ppd=10),
        # White
        "white_noise": white(**params),
        # One over frequency
        "one_over_f": one_over_f(**params, exponent=0.5),
        "pink_noise": pink(**params),
        "brown_noise": brown(**params),
        # Narrowband
        "narrowband_1cpd": narrowband(**params, bandwidth=1, center_frequency=1.0),
        "narrowband_3cpd": narrowband(**params, bandwidth=1, center_frequency=3.0),
    }
    # fmt: on

    return stims


def overview(mask=False, save=None, extent_key="shape"):
    """
    Plot overview with examples from all stimulus-noises 

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
