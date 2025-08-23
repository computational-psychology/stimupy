"""Parameter classes for stimuli.benarys module."""

import param


class CrossGeneralizedParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    cross_thickness = param.Number(default=2, bounds=(1, 10), step=0.1, doc="")
    target_height = param.Number(default=2, bounds=(1, 4), step=0.1, doc="")
    target_width = param.Number(default=2, bounds=(1, 4), step=0.1, doc="")
    target_type = param.Selector(default="r", objects=["r", "t"], doc="")
    intensity_target = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="")
    target_y = param.Number(default=2, bounds=(1, 4), step=0.1, doc="")
    target_x = param.Number(default=2, bounds=(1, 4), step=0.1, doc="")
    target_rotation = param.Number(default=0.0, bounds=(0, 360), step=1, doc="")
    intensity_background = param.Number(default=1.0, bounds=(0, 1), step=0.01, doc="")
    intensity_cross = param.Number(default=0.0, bounds=(0, 1), step=0.01, doc="")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "cross_thickness": self.cross_thickness,
            "target_size": (self.target_height, self.target_width),
            "target_type": self.target_type,
            "target_rotation": self.target_rotation,
            "target_x": self.target_x,
            "target_y": self.target_y,
            "intensity_background": self.intensity_background,
            "intensity_cross": self.intensity_cross,
            "intensity_target": self.intensity_target,
        }


class CrossRectanglesParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    cross_thickness = param.Number(default=2, bounds=(1, 10), step=0.1, doc="")
    target_height = param.Number(default=2, bounds=(1, 4), step=0.1, doc="")
    target_width = param.Number(default=2, bounds=(1, 4), step=0.1, doc="")
    intensity_target = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="")
    intensity_cross = param.Number(default=1.0, bounds=(0, 1), step=0.01, doc="")
    intensity_background = param.Number(default=0.0, bounds=(0, 1), step=0.01, doc="")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "cross_thickness": self.cross_thickness,
            "target_size": (self.target_height, self.target_width),
            "intensity_target": self.intensity_target,
            "intensity_cross": self.intensity_cross,
            "intensity_background": self.intensity_background,
        }


class CrossTrianglesParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    cross_thickness = param.Number(default=2, bounds=(1, 10), step=0.1, doc="")
    target_size = param.Number(default=2, bounds=(1, 4), step=0.1, doc="")
    intensity_target = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="")
    intensity_cross = param.Number(default=1.0, bounds=(0, 1), step=0.01, doc="")
    intensity_background = param.Number(default=0.0, bounds=(0, 1), step=0.01, doc="")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "cross_thickness": self.cross_thickness,
            "target_size": self.target_size,
            "intensity_target": self.intensity_target,
            "intensity_cross": self.intensity_cross,
            "intensity_background": self.intensity_background,
        }


class TodorovicGeneralizedParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    L_width = param.Number(default=2, bounds=(1, 10), step=0.1, doc="")
    target_size = param.Number(default=2, bounds=(1, 4), step=0.1, doc="")
    target_type = param.Selector(
        default="r", objects=["r", "t"], doc="(r)ectangle or (t)riangle targets"
    )
    target_rotation = param.Number(default=0, bounds=(0, 360), doc="Rotation angle in degrees")
    target_x = param.List(default=[1, 4], bounds=(-10, 10), doc="X position in degrees")
    target_y = param.List(default=[4, 1], bounds=(-10, 10), doc="Y position in degrees")
    intensity_target = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="")
    intensity_cross = param.Number(default=1.0, bounds=(0, 1), step=0.01, doc="")
    intensity_background = param.Number(default=0.0, bounds=(0, 1), step=0.01, doc="")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "L_width": self.L_width,
            "target_size": self.target_size,
            "target_type": self.target_type,
            "target_rotation": self.target_rotation,
            "target_x": self.target_x,
            "target_y": self.target_y,
            "intensity_target": self.intensity_target,
            "intensity_cross": self.intensity_cross,
            "intensity_background": self.intensity_background,
        }


class TodorovicRectanglesParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    L_width = param.Number(default=2, bounds=(1, 10), step=0.1, doc="")
    target_size = param.Number(default=2, bounds=(1, 4), step=0.1, doc="")
    intensity_target = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="")
    intensity_cross = param.Number(default=1.0, bounds=(0, 1), step=0.01, doc="")
    intensity_background = param.Number(default=0.0, bounds=(0, 1), step=0.01, doc="")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "L_width": self.L_width,
            "target_size": self.target_size,
            "intensity_target": self.intensity_target,
            "intensity_cross": self.intensity_cross,
            "intensity_background": self.intensity_background,
        }


class TodorovicTrianglesParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    L_width = param.Number(default=2, bounds=(1, 10), step=0.1, doc="")
    target_size = param.Number(default=2, bounds=(1, 4), step=0.1, doc="")
    intensity_target = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="")
    intensity_cross = param.Number(default=1.0, bounds=(0, 1), step=0.01, doc="")
    intensity_background = param.Number(default=0.0, bounds=(0, 1), step=0.01, doc="")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "L_width": self.L_width,
            "target_size": self.target_size,
            "intensity_target": self.intensity_target,
            "intensity_cross": self.intensity_cross,
            "intensity_background": self.intensity_background,
        }


__all__ = [
    "CrossGeneralizedParams",
    "CrossRectanglesParams",
    "CrossTrianglesParams",
    "TodorovicGeneralizedParams",
    "TodorovicRectanglesParams",
    "TodorovicTrianglesParams",
]
