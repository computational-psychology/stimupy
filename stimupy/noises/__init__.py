from .binaries import binary as binary
from .narrowbands import narrowband as narrowband
from .naturals import *
from .utils import *
from .whites import white as white


def create_overview():
    import stimupy.noises.naturals as naturals

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
        "one_over_f": naturals.one_over_f(**params, exponent=0.5),
        "pink_noise": naturals.pink(**params),
        "brown_noise": naturals.brown(**params),
        # Narrowband
        "narrowband_1cpd": narrowband(**params, bandwidth=1, center_frequency=1.0),
        "narrowband_3cpd": narrowband(**params, bandwidth=1, center_frequency=3.0),
    }
    # fmt: on

    return stims


def overview(mask=False, save=None):
    from stimupy.utils import plot_stimuli

    stims = create_overview()

    # Plotting
    plot_stimuli(stims, mask=mask, save=save)
