"""Parameter classes for stimuli.cornsweets module."""

import param


class CornsweetParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    # Cornsweet geometry parameters
    ramp_width = param.Number(default=2, bounds=(0, 5), step=0.1, doc="Ramp width in degrees")
    exponent = param.Number(default=2.75, bounds=(0.5, 5), step=0.05, doc="Exponent")
    rotation = param.Integer(default=0, bounds=(0, 360), doc="Rotation in degrees")

    # Intensity parameters
    intensity1 = param.Number(default=1, bounds=(0, 1), step=0.01, doc="Intensity 1")
    intensity2 = param.Number(default=0.0, bounds=(0, 1), step=0.01, doc="Intensity 2")
    intensity_plateau = param.Number(
        default=0.5, bounds=(0, 1), step=0.01, doc="Plateau intensity"
    )

    # Additional parameters
    add_mask = param.Selector(
        default=None, objects=[None, "target_mask", "edge_mask"], doc="Add mask"
    )

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "rotation": self.rotation,
            "intensity_edges": (self.intensity1, self.intensity2),
            "intensity_plateau": self.intensity_plateau,
            "ramp_width": self.ramp_width,
            "exponent": self.exponent,
        }


__all__ = ["CornsweetParams"]
