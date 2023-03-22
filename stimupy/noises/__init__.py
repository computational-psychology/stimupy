from stimupy.noises.binaries import *
from stimupy.noises.narrowbands import *
from stimupy.noises.naturals import *
from stimupy.noises.utils import *
from stimupy.noises.whites import *


def overview(skip=False):
    """Generate example stimuli from this module

    Returns
    -------
    dict[str, dict]
        Dict mapping names to individual stimulus dicts
    """
    params = {
        "visual_size": 10,
        "ppd": 10,
        "pseudo_noise": True,
    }

    # fmt: off
    stimuli = {
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

    # stimuli = {}
    # for stimmodule_name in __all__:
    #     if stimmodule_name in ["overview", "plot_overview"]:
    #         pass

    #     print(f"Generating stimuli from {stimmodule_name}")
    #     # Get a reference to the actual module
    #     stimmodule = globals()[stimmodule_name]
    #     try:
    #         stims = stimmodule.overview()

    #         # Accumulate
    #         stimuli.update(stims)
    #     except NotImplementedError as e:
    #         if not skip:
    #             raise e
    #         # Skip stimuli that aren't implemented
    #         print("-- not implemented")
    #         pass

    return stimuli


def plot_overview(mask=False, save=None, extent_key="shape"):
    """Plot overview of examples in this module (and submodules)

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

    stims = overview(skip=True)
    plot_stimuli(stims, mask=mask, extent_key=extent_key, save=save)


if __name__ == "__main__":
    plot_overview()
