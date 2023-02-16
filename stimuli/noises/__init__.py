from .whites import white as white
from .binaries import binary as binary
from .naturals import *
from .narrowbands import narrowband as narrowband
from .utils import *


def create_overview(mask=False, save=None):
    from stimuli.utils import plot_stimuli
    import stimuli.noises.naturals as naturals

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
    
    # Plotting
    plot_stimuli(stims, mask=mask, save=save)