from stimuli.utils import plot_stimuli
import stimuli.noises.white as white
import stimuli.noises.one_over_frequency as oof
import stimuli.noises.narrowband as narrowband


params = {
    "visual_size": 10,
    "ppd": 20,
    "rms_contrast": 0.5,
    "pseudo_noise": True,
    }

# fmt: off
stims = {
    # White
    "White noise": white(**params),
    # One over frequency
    "One over f": oof.one_over_f(**params, exponent=0.5),
    "Pink noise": oof.pink(**params),
    "Brown noise": oof.brown(**params),
    # Narrowband
    "Narrowband 3cpd": narrowband(**params, bandwidth=1, center_frequency=3.0),
    "Narrowband 9cpd": narrowband(**params, bandwidth=1, center_frequency=9.0),
}


if __name__ == "__main__":
    plot_stimuli(stims, mask=True, save=None, vmin=-2, vmax=2)
