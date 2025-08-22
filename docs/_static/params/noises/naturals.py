from pathlib import __all__
import param


class OneOverFParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    exponent = param.Number(default=1.0, bounds=(0.0, 5), step=0.1, doc="")
    intensity_min = param.Number(default=0.0, bounds=(0, 1), step=0.01, doc="")
    intensity_max = param.Number(default=1.0, bounds=(0, 1), step=0.01, doc="")
    pseudo_noise = param.Boolean(default=False, doc="")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "exponent": self.exponent,
            "intensity_range": (self.intensity_min, self.intensity_max),
            "pseudo_noise": self.pseudo_noise,
        }


class BrownParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    intensity_min = param.Number(default=0.0, bounds=(0, 1), step=0.01, doc="")
    intensity_max = param.Number(default=1.0, bounds=(0, 1), step=0.01, doc="")
    pseudo_noise = param.Boolean(default=False, doc="")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "intensity_range": (self.intensity_min, self.intensity_max),
            "pseudo_noise": self.pseudo_noise,
        }


class PinkParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    intensity_min = param.Number(default=0.0, bounds=(0, 1), step=0.01, doc="")
    intensity_max = param.Number(default=1.0, bounds=(0, 1), step=0.01, doc="")
    pseudo_noise = param.Boolean(default=False, doc="")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "intensity_range": (self.intensity_min, self.intensity_max),
            "pseudo_noise": self.pseudo_noise,
        }


__all__ = ["OneOverFParams", "BrownParams", "PinkParams"]
