"""Parameter classes for components.lines module."""

import param


class CircleParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    radius = param.Number(default=3, bounds=(0, 6), step=0.01, doc="")
    line_width = param.Number(default=0, bounds=(0, 3), step=0.01, doc="")
    intensity_line = param.Number(default=1.0, bounds=(0, 1), step=0.01, doc="")
    intensity_background = param.Number(default=0.0, bounds=(0, 1), step=0.01, doc="")
    mask = param.Boolean(default=False, doc="")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "radius": self.radius,
            "line_width": self.line_width,
            "intensity_line": self.intensity_line,
            "intensity_background": self.intensity_background,
        }


class DipoleParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    length = param.Number(default=5, bounds=(0, 8), step=0.01, doc="")
    theta = param.Number(default=0, bounds=(0, 360), step=0.01, doc="")
    line_width = param.Number(default=0, bounds=(0, 3), step=0.01, doc="")
    line_gap = param.Number(default=1.0, bounds=(0, 5), step=0.01, doc="Gap between lines")
    intensity_line = param.Number(default=1.0, bounds=(0, 1), step=0.01, doc="")
    intensity_background = param.Number(default=0.0, bounds=(0, 1), step=0.01, doc="")
    mask = param.Boolean(default=False, doc="")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "line_length": self.length,  # Fixed: dipole expects line_length, not length
            "rotation": self.theta,  # Fixed: dipole expects rotation, not theta
            "line_width": self.line_width,
            "line_gap": self.line_gap,  # Added missing parameter
            "intensity_lines": (
                self.intensity_background,
                self.intensity_line,
            ),  # Fixed: dipole expects intensity_lines tuple
        }


class EllipseParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    radius1 = param.Number(default=3, bounds=(0, 6), step=0.01, doc="")
    radius2 = param.Number(default=2, bounds=(0, 6), step=0.01, doc="")
    rotation = param.Number(default=0, bounds=(0, 360), step=0.01, doc="")
    line_width = param.Number(default=0, bounds=(0, 3), step=0.01, doc="")
    intensity_line = param.Number(default=1.0, bounds=(0, 1), step=0.01, doc="")
    intensity_background = param.Number(default=0.0, bounds=(0, 1), step=0.01, doc="")
    mask = param.Boolean(default=False, doc="")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "radius": (self.radius1, self.radius2),
            "line_width": self.line_width,
            "intensity_line": self.intensity_line,
            "intensity_background": self.intensity_background,
        }


class LineParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    length = param.Number(default=5, bounds=(0, 8), step=0.01, doc="")
    theta = param.Number(default=0, bounds=(0, 360), step=0.01, doc="")
    line_width = param.Number(default=0, bounds=(0, 3), step=0.01, doc="")
    intensity_line = param.Number(default=1.0, bounds=(0, 1), step=0.01, doc="")
    intensity_background = param.Number(default=0.0, bounds=(0, 1), step=0.01, doc="")
    mask = param.Boolean(default=False, doc="")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "line_length": self.length,
            "rotation": self.theta,
            "line_width": self.line_width,
            "intensity_line": self.intensity_line,
            "intensity_background": self.intensity_background,
        }


__all__ = ["CircleParams", "DipoleParams", "EllipseParams", "LineParams"]
