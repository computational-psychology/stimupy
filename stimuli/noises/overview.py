from stimuli.utils import plot_stimuli
from stimuli.noises.binaries import binary
from stimuli.noises.whites import white
import stimuli.noises.naturals as naturals
from stimuli.noises.narrowbands import narrowband


params = {
    "visual_size": 10,
    "ppd": 10,
    "rms_contrast": 0.5,
    "pseudo_noise": True,
    }

# fmt: off
stims = {
    # Binary
    "binary_noise": binary(visual_size=10, ppd=10, rms_contrast=0.5),
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


if __name__ == "__main__":
    plot_stimuli(stims, mask=True, save=None, vmin=-2, vmax=2)
