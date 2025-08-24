"""Parameter classes for stimuli.mueller_lyers module."""

import param


class MuellerLyerParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    outer_lines_length = param.Number(
        default=1, bounds=(0.1, 2), step=0.1, doc="Outer line length"
    )
    outer_lines_angle = param.Number(
        default=45, bounds=(-180, 180), step=1, doc="Outer line angle"
    )
    line_width = param.Number(default=0, bounds=(0, 0.5), step=0.01, doc="Line width")
    target_length = param.Number(default=2.5, bounds=(0, 5), step=0.1, doc="Target length")
    intensity_outer_lines = param.Number(
        default=1.0, bounds=(0, 1), step=0.01, doc="Outer lines intensity"
    )
    intensity_target = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="Target intensity")
    intensity_background = param.Number(
        default=0.0, bounds=(0, 1), step=0.01, doc="Background intensity"
    )

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "outer_lines_length": self.outer_lines_length,
            "outer_lines_angle": self.outer_lines_angle,
            "line_width": self.line_width,
            "target_length": self.target_length,
            "intensity_outer_lines": self.intensity_outer_lines,
            "intensity_target": self.intensity_target,
            "intensity_background": self.intensity_background,
        }


class TwoSidedParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    outer_lines_length = param.Number(
        default=1, bounds=(0.1, 2), step=0.1, doc="Outer line length"
    )
    outer_lines_angle = param.Number(
        default=45, bounds=(-180, 180), step=1, doc="Outer line angle"
    )
    line_width = param.Number(default=0, bounds=(0, 0.5), step=0.01, doc="Line width")
    target_length = param.Number(default=2.5, bounds=(0, 5), step=0.1, doc="Target length")
    intensity_outer_lines = param.Number(
        default=1.0, bounds=(0, 1), step=0.01, doc="Outer lines intensity"
    )
    intensity_target = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="Target intensity")
    intensity_background = param.Number(
        default=0.0, bounds=(0, 1), step=0.01, doc="Background intensity"
    )

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "outer_lines_length": self.outer_lines_length,
            "outer_lines_angle": self.outer_lines_angle,
            "line_width": self.line_width,
            "target_length": self.target_length,
            "intensity_outer_lines": self.intensity_outer_lines,
            "intensity_target": self.intensity_target,
            "intensity_background": self.intensity_background,
        }


__all__ = ["MuellerLyerParams", "TwoSidedParams"]
