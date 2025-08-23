"""Parameter classes for stimuli.delboeufs module."""

import param


class DelboeufParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    outer_radius = param.Number(default=4, bounds=(0.5, 8), step=0.1, doc="")
    outer_line_width = param.Number(default=0, bounds=(0, 2), step=0.1, doc="")
    intensity_outer_line = param.Number(default=0.0, bounds=(0, 1), step=0.01, doc="")
    intensity_background = param.Number(default=1.0, bounds=(0, 1), step=0.01, doc="")
    target_radius = param.Number(default=2.5, bounds=(0, 5), step=0.1, doc="")
    intensity_target = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "outer_radius": self.outer_radius,
            "outer_line_width": self.outer_line_width,
            "intensity_outer_line": self.intensity_outer_line,
            "intensity_background": self.intensity_background,
            "target_radius": self.target_radius,
            "intensity_target": self.intensity_target,
        }


class TwoSidedParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=20, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    target_radius_left = param.Number(default=2.5, bounds=(0, 5), step=0.1, doc="")
    target_radius_right = param.Number(default=2.5, bounds=(0, 5), step=0.1, doc="")
    outer_radius_left = param.Number(default=4, bounds=(0.5, 8), step=0.1, doc="")
    outer_radius_right = param.Number(default=4, bounds=(0.5, 8), step=0.1, doc="")
    outer_line_width_left = param.Number(default=0, bounds=(0, 2), step=0.1, doc="")
    outer_line_width_right = param.Number(default=0, bounds=(0, 2), step=0.1, doc="")
    intensity_target = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="")
    intensity_outer_line = param.Number(default=0.0, bounds=(0, 1), step=0.01, doc="")
    intensity_background = param.Number(default=1.0, bounds=(0, 1), step=0.01, doc="")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "target_radius": (self.target_radius_left, self.target_radius_right),
            "outer_radius": (self.outer_radius_left, self.outer_radius_right),
            "outer_line_width": (self.outer_line_width_left, self.outer_line_width_right),
            "intensity_target": self.intensity_target,
            "intensity_outer_line": self.intensity_outer_line,
            "intensity_background": self.intensity_background,
        }


__all__ = ["DelboeufParams", "TwoSidedParams"]
