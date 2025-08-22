"""Parameter classes for stimuli.whites module."""

import param


class WhiteParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    frequency = param.Number(default=1.0, bounds=(0.1, 3), step=0.1, doc="Frequency in cpd")
    target_indices = param.Tuple(default=(3, 4), length=2, doc="Target bar indices")
    target_heights = param.Tuple(default=(2.0, 2.0), length=2, doc="Target heights")
    intensity_bars = param.Tuple(default=(0.0, 1.0), length=2, doc="Bar intensities (low, high)")
    intensity_target = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="Target intensity")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "frequency": self.frequency,
            "target_indices": self.target_indices,
            "target_heights": self.target_heights,
            "intensity_bars": self.intensity_bars,
            "intensity_target": self.intensity_target,
        }


class AngularParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    frequency = param.Number(default=8.0, bounds=(2, 16), step=0.5, doc="Frequency in cycles")
    rotation = param.Number(default=0, bounds=(0, 360), step=1, doc="Rotation in degrees")
    target_width = param.Number(default=0.5, bounds=(0.1, 5), step=0.1, doc="Target width")
    target_center = param.Number(default=1.0, bounds=(0, 1), step=0.01, doc="Target center")
    target_indices = param.Tuple(default=(2, 3), length=2, doc="Target segment indices")
    intensity_segments = param.Tuple(
        default=(0.0, 1.0), length=2, doc="Segment intensities (low, high)"
    )
    intensity_target = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="Target intensity")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "rotation": self.rotation,
            "frequency": self.frequency,
            "target_indices": self.target_indices,
            "target_width": self.target_width,
            "target_center": self.target_center,
            "intensity_segments": self.intensity_segments,
            "intensity_target": self.intensity_target,
        }


class RadialParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    frequency = param.Number(default=1.0, bounds=(0.1, 3), step=0.1, doc="Frequency in cpd")
    target_indices = param.Tuple(default=(2, 3), length=2, doc="Target ring indices")
    intensity_rings = param.Tuple(default=(0.0, 1.0), length=2, doc="Ring intensities (low, high)")
    intensity_target = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="Target intensity")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "frequency": self.frequency,
            "target_indices": self.target_indices,
            "intensity_rings": self.intensity_rings,
            "intensity_target": self.intensity_target,
        }


__all__ = ["WhiteParams", "AngularParams", "RadialParams"]
