"""Parameter classes for stimuli.edges module."""

import param


class StepParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    rotation = param.Number(default=0.0, bounds=(0, 360), step=1, doc="Rotation in degrees")
    intensity1 = param.Number(default=0.0, bounds=(0, 1), step=0.01, doc="Intensity 1")
    intensity2 = param.Number(default=1.0, bounds=(0, 1), step=0.01, doc="Intensity 2")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "rotation": self.rotation,
            "intensity_edges": (self.intensity1, self.intensity2),
        }


class GaussianParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    sigma = param.Number(default=2.0, bounds=(0.1, 4), step=0.1, doc="Sigma")
    rotation = param.Number(default=0.0, bounds=(0, 360), step=1, doc="Rotation in degrees")
    intensity1 = param.Number(default=0.0, bounds=(0, 1), step=0.01, doc="Intensity 1")
    intensity2 = param.Number(default=1.0, bounds=(0, 1), step=0.01, doc="Intensity 2")
    intensity_background = param.Number(
        default=0.5, bounds=(0, 1), step=0.01, doc="Background intensity"
    )

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "sigma": self.sigma,
            "rotation": self.rotation,
            "intensity_edges": (self.intensity1, self.intensity2),
            "intensity_background": self.intensity_background,
        }


class CornsweetParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    ramp_width = param.Number(default=2.0, bounds=(0.1, 5), step=0.1, doc="Ramp width")
    rotation = param.Number(default=0.0, bounds=(0, 360), step=1, doc="Rotation in degrees")
    intensity1 = param.Number(default=0.0, bounds=(0, 1), step=0.01, doc="Intensity 1")
    intensity2 = param.Number(default=1.0, bounds=(0, 1), step=0.01, doc="Intensity 2")
    intensity_plateau = param.Number(
        default=0.5, bounds=(0, 1), step=0.01, doc="Plateau intensity"
    )
    exponent = param.Number(default=2.75, bounds=(1, 5), step=0.1, doc="Exponent")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "ramp_width": self.ramp_width,
            "rotation": self.rotation,
            "intensity_edges": (self.intensity1, self.intensity2),
            "intensity_plateau": self.intensity_plateau,
            "exponent": self.exponent,
        }


__all__ = ["StepParams", "GaussianParams", "CornsweetParams"]
