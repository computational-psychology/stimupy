"""Parameter classes for stimuli.plaids module."""

import param


class GaborsParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    sigma = param.Number(default=2, bounds=(0.1, 4), step=0.1, doc="Sigma")
    weight1 = param.Number(default=1, bounds=(0, 1), step=0.1, doc="Weight 1")
    weight2 = param.Number(default=1, bounds=(0, 1), step=0.1, doc="Weight 2")

    def get_stimulus_params(self):
        gabor_params1 = {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "sigma": self.sigma,
            "frequency": 1.0,
            "rotation": 0.0,
        }
        gabor_params2 = {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "sigma": self.sigma,
            "frequency": 1.0,
            "rotation": 45.0,
        }
        return {
            "gabor_parameters1": gabor_params1,
            "gabor_parameters2": gabor_params2,
            "weight1": self.weight1,
            "weight2": self.weight2,
        }


class SineWavesParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    weight1 = param.Number(default=1, bounds=(0, 1), step=0.1, doc="Weight 1")
    weight2 = param.Number(default=1, bounds=(0, 1), step=0.1, doc="Weight 2")

    def get_stimulus_params(self):
        grating_params1 = {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "frequency": 1.0,
            "rotation": 0.0,
        }
        grating_params2 = {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "frequency": 1.0,
            "rotation": 45.0,
        }
        return {
            "grating_parameters1": grating_params1,
            "grating_parameters2": grating_params2,
            "weight1": self.weight1,
            "weight2": self.weight2,
        }


class SquareWavesParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    weight1 = param.Number(default=1, bounds=(0, 1), step=0.1, doc="Weight 1")
    weight2 = param.Number(default=1, bounds=(0, 1), step=0.1, doc="Weight 2")

    def get_stimulus_params(self):
        grating_params1 = {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "frequency": 1.0,
            "rotation": 0.0,
        }
        grating_params2 = {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "frequency": 1.0,
            "rotation": 45.0,
        }
        return {
            "grating_parameters1": grating_params1,
            "grating_parameters2": grating_params2,
            "weight1": self.weight1,
            "weight2": self.weight2,
        }


__all__ = ["GaborsParams", "SineWavesParams", "SquareWavesParams"]
