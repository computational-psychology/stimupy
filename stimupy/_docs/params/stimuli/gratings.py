"""Parameter classes for stimuli.gratings module."""

import param


class SquarewaveParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    frequency = param.Number(default=1.0, bounds=(0.1, 5), step=0.1, doc="Frequency in cpd")
    rotation = param.Number(default=0, bounds=(0, 360), step=1, doc="Rotation in degrees")
    phase_shift = param.Number(default=0, bounds=(0, 360), step=1, doc="Phase shift in degrees")
    intensity_min = param.Number(default=0.0, bounds=(0, 1), step=0.01, doc="Minimum intensity")
    intensity_max = param.Number(default=1.0, bounds=(0, 1), step=0.01, doc="Maximum intensity")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "frequency": self.frequency,
            "rotation": self.rotation,
            "phase_shift": self.phase_shift,
            "intensity_bars": (self.intensity_min, self.intensity_max),
        }


class SinewaveParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    frequency = param.Number(default=1.0, bounds=(0.1, 5), step=0.1, doc="Frequency in cpd")
    rotation = param.Number(default=0, bounds=(0, 360), step=1, doc="Rotation in degrees")
    phase_shift = param.Number(default=0, bounds=(0, 360), step=1, doc="Phase shift in degrees")
    intensity_min = param.Number(default=0.0, bounds=(0, 1), step=0.01, doc="Minimum intensity")
    intensity_max = param.Number(default=1.0, bounds=(0, 1), step=0.01, doc="Maximum intensity")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "frequency": self.frequency,
            "rotation": self.rotation,
            "phase_shift": self.phase_shift,
            "intensities": (self.intensity_min, self.intensity_max),
        }


__all__ = ["SquarewaveParams", "SinewaveParams"]
