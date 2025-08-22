"""Parameter classes for stimuli.todorovics module."""

import param


class CrossGeneralizedParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    cross_size_height = param.Number(default=4, bounds=(2, 8), step=0.1, doc="Cross height")
    cross_size_width = param.Number(default=4, bounds=(2, 8), step=0.1, doc="Cross width")
    cross_thickness = param.Number(default=0.5, bounds=(0.1, 2), step=0.1, doc="Cross thickness")
    covers_height = param.Number(default=2, bounds=(0, 4), step=0.1, doc="Covers height")
    covers_width = param.Number(default=2, bounds=(0, 4), step=0.1, doc="Covers width")
    cover_x1 = param.Number(default=2, bounds=(0, 8), step=0.1, doc="Cover 1 X position")
    cover_y1 = param.Number(default=4, bounds=(0, 8), step=0.1, doc="Cover 1 Y position")
    cover_x2 = param.Number(default=6, bounds=(0, 8), step=0.1, doc="Cover 2 X position")
    cover_y2 = param.Number(default=4, bounds=(0, 8), step=0.1, doc="Cover 2 Y position")
    intensity_background = param.Number(
        default=0.0, bounds=(0, 1), step=0.01, doc="Background intensity"
    )
    intensity_target = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="Target intensity")
    intensity_covers = param.Number(default=1.0, bounds=(0, 1), step=0.01, doc="Covers intensity")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "cross_size": (self.cross_size_height, self.cross_size_width),
            "cross_thickness": self.cross_thickness,
            "covers_size": (self.covers_height, self.covers_width),
            "covers_x": (self.cover_x1, self.cover_x2),
            "covers_y": (self.cover_y1, self.cover_y2),
            "intensity_background": self.intensity_background,
            "intensity_target": self.intensity_target,
            "intensity_covers": self.intensity_covers,
        }


class EqualParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    cross_size = param.Number(
        default=4.0, bounds=(2, 8), step=0.1, doc="Cross size", allow_None=True
    )
    cross_thickness = param.Number(
        default=1.0, bounds=(0.5, 3), step=0.1, doc="Cross thickness", allow_None=True
    )
    cover_size = param.Number(
        default=1.5, bounds=(0.1, 2), step=0.1, doc="Cover size", allow_None=True
    )
    intensity_background = param.Number(
        default=0.0, bounds=(0, 1), step=0.01, doc="Background intensity"
    )
    intensity_target = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="Target intensity")
    intensity_covers = param.Number(default=1.0, bounds=(0, 1), step=0.01, doc="Covers intensity")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "cross_size": self.cross_size,
            "cross_thickness": self.cross_thickness,
            "cover_size": self.cover_size,
            "intensity_background": self.intensity_background,
            "intensity_target": self.intensity_target,
            "intensity_covers": self.intensity_covers,
        }


class RectangleGeneralizedParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    target_height = param.Number(default=2, bounds=(0, 4), step=0.1, doc="Target height")
    target_width = param.Number(default=2, bounds=(0, 4), step=0.1, doc="Target width")
    intensity_target = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="Target intensity")
    target_x = param.Number(default=4, bounds=(0, 8), step=0.1, doc="Target X position")
    target_y = param.Number(default=4, bounds=(0, 8), step=0.1, doc="Target Y position")
    covers_height = param.Number(default=2, bounds=(0, 4), step=0.1, doc="Covers height")
    covers_width = param.Number(default=2, bounds=(0, 4), step=0.1, doc="Covers width")
    cover_x1 = param.Number(default=2, bounds=(0, 8), step=0.1, doc="Cover 1 X position")
    cover_y1 = param.Number(default=4, bounds=(0, 8), step=0.1, doc="Cover 1 Y position")
    cover_x2 = param.Number(default=6, bounds=(0, 8), step=0.1, doc="Cover 2 X position")
    cover_y2 = param.Number(default=4, bounds=(0, 8), step=0.1, doc="Cover 2 Y position")
    intensity_background = param.Number(
        default=0.0, bounds=(0, 1), step=0.01, doc="Background intensity"
    )
    intensity_covers = param.Number(default=1.0, bounds=(0, 1), step=0.01, doc="Covers intensity")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "target_size": (self.target_height, self.target_width),
            "target_position": (self.target_y, self.target_x),
            "covers_size": (self.covers_height, self.covers_width),
            "covers_x": (self.cover_x1, self.cover_x2),
            "covers_y": (self.cover_y1, self.cover_y2),
            "intensity_background": self.intensity_background,
            "intensity_target": self.intensity_target,
            "intensity_covers": self.intensity_covers,
        }


__all__ = ["CrossGeneralizedParams", "EqualParams", "RectangleGeneralizedParams"]
