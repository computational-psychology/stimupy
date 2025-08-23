"""Parameter classes for stimuli.ponzos module."""

import param


class PonzoParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    outer_lines_length = param.Number(
        default=4, bounds=(0.5, 8), step=0.1, doc="Outer lines length"
    )
    outer_lines_width = param.Number(default=0, bounds=(0, 2), step=0.01, doc="Outer lines width")
    outer_lines_angle = param.Number(default=15, bounds=(-30, 30), step=1, doc="Outer lines angle")
    target_lines_length = param.Number(
        default=2, bounds=(0.5, 4), step=0.1, doc="Target lines length"
    )
    target_lines_width = param.Number(
        default=0, bounds=(0, 2), step=0.01, doc="Target lines width"
    )
    target_distance = param.Number(default=2, bounds=(0.5, 4), step=0.1, doc="Target distance")
    intensity_outer_lines = param.Number(
        default=1.0, bounds=(0, 1), step=0.01, doc="Outer lines intensity"
    )
    intensity_target_lines = param.Number(
        default=0.5, bounds=(0, 1), step=0.01, doc="Target lines intensity"
    )
    intensity_background = param.Number(
        default=0.0, bounds=(0, 1), step=0.01, doc="Background intensity"
    )

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "outer_lines_length": self.outer_lines_length,
            "outer_lines_width": self.outer_lines_width,
            "outer_lines_angle": self.outer_lines_angle,
            "target_lines_length": self.target_lines_length,
            "target_lines_width": self.target_lines_width,
            "target_distance": self.target_distance,
            "intensity_outer_lines": self.intensity_outer_lines,
            "intensity_target_lines": self.intensity_target_lines,
            "intensity_background": self.intensity_background,
        }


__all__ = ["PonzoParams"]
