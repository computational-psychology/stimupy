"""Parameter classes for stimuli.bullseyes module."""

import param


class CircularParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    frequency = param.Number(default=1.0, bounds=(0.1, 2), step=0.1, doc="Frequency in cpd")
    phase_shift = param.Number(default=0, bounds=(0, 360), step=1, doc="Phase shift in degrees")
    intensity1 = param.Number(default=0.0, bounds=(0, 1), step=0.01, doc="Intensity 1")
    intensity2 = param.Number(default=1.0, bounds=(0, 1), step=0.01, doc="Intensity 2")
    intensity_background = param.Number(
        default=0.5, bounds=(0, 1), step=0.01, doc="Background intensity"
    )
    intensity_target = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="Target intensity")
    origin = param.Selector(
        default="mean", objects=["mean", "corner", "center"], doc="Origin position"
    )

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "frequency": self.frequency,
            "phase_shift": self.phase_shift,
            "intensity_rings": (self.intensity1, self.intensity2),
            "intensity_background": self.intensity_background,
            "intensity_target": self.intensity_target,
            "origin": self.origin,
        }


class CircularGeneralizedParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    radius1 = param.Number(default=1.0, bounds=(0.1, 5), step=0.1, doc="Radius 1")
    radius2 = param.Number(default=2.0, bounds=(0.1, 5), step=0.1, doc="Radius 2")
    radius3 = param.Number(default=3.0, bounds=(0.1, 5), step=0.1, doc="Radius 3")
    intensity1 = param.Number(default=1.0, bounds=(0, 1), step=0.01, doc="Intensity 1")
    intensity2 = param.Number(default=0.3, bounds=(0, 1), step=0.01, doc="Intensity 2")
    intensity3 = param.Number(default=0.8, bounds=(0, 1), step=0.01, doc="Intensity 3")
    intensity_background = param.Number(
        default=0.0, bounds=(0, 1), step=0.01, doc="Background intensity"
    )
    target_idx = param.Integer(default=1, bounds=(1, 4), doc="Target index")
    intensity_target = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="Target intensity")
    origin = param.Selector(
        default="center", objects=["mean", "corner", "center"], doc="Origin position"
    )

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "radii": (self.radius1, self.radius2, self.radius3),
            "intensity_rings": (self.intensity1, self.intensity2, self.intensity3),
            "intensity_background": self.intensity_background,
            "intensity_target": self.intensity_target,
            "origin": self.origin,
        }


class CircularTwoSidedParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    frequency = param.Number(default=1.0, bounds=(0.1, 2), step=0.1, doc="Frequency in cpd")
    phase_shift = param.Number(default=0, bounds=(0, 360), step=1, doc="Phase shift in degrees")
    intensity1 = param.Number(default=1.0, bounds=(0, 1), step=0.01, doc="Intensity 1")
    intensity2 = param.Number(default=0.0, bounds=(0, 1), step=0.01, doc="Intensity 2")
    intensity_background = param.Number(
        default=0.5, bounds=(0, 1), step=0.01, doc="Background intensity"
    )
    target_idx = param.Integer(default=2, bounds=(0, 10), doc="Target index")
    intensity_target_left = param.Number(
        default=0.5, bounds=(0, 1), step=0.01, doc="Left target intensity"
    )
    intensity_target_right = param.Number(
        default=0.5, bounds=(0, 1), step=0.01, doc="Right target intensity"
    )
    origin = param.Selector(
        default="mean", objects=["mean", "corner", "center"], doc="Origin position"
    )

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "frequency": self.frequency,
            "phase_shift": self.phase_shift,
            "intensity_rings": (
                (self.intensity1, self.intensity2),
                (self.intensity2, self.intensity1),
            ),
            "intensity_background": self.intensity_background,
            "intensity_target": (self.intensity_target_left, self.intensity_target_right),
            "origin": self.origin,
        }


class RectangularParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    frequency = param.Number(default=1.0, bounds=(0.1, 2), step=0.1, doc="Frequency in cpd")
    phase_shift = param.Number(default=0, bounds=(0, 360), step=1, doc="Phase shift in degrees")
    intensity1 = param.Number(default=1.0, bounds=(0, 1), step=0.01, doc="Intensity 1")
    intensity2 = param.Number(default=0.0, bounds=(0, 1), step=0.01, doc="Intensity 2")
    intensity_background = param.Number(
        default=0.5, bounds=(0, 1), step=0.01, doc="Background intensity"
    )
    intensity_target = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="Target intensity")
    origin = param.Selector(
        default="center", objects=["mean", "corner", "center"], doc="Origin position"
    )

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "frequency": self.frequency,
            "phase_shift": self.phase_shift,
            "intensity_frames": (self.intensity1, self.intensity2),
            "intensity_background": self.intensity_background,
            "intensity_target": self.intensity_target,
            "origin": self.origin,
        }


class RectangularGeneralizedParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    radius1 = param.Number(default=1.0, bounds=(0.1, 5), step=0.1, doc="Radius 1")
    radius2 = param.Number(default=2.0, bounds=(0.1, 5), step=0.1, doc="Radius 2")
    radius3 = param.Number(default=3.0, bounds=(0.1, 5), step=0.1, doc="Radius 3")
    intensity1 = param.Number(default=1.0, bounds=(0, 1), step=0.01, doc="Intensity 1")
    intensity2 = param.Number(default=0.3, bounds=(0, 1), step=0.01, doc="Intensity 2")
    intensity3 = param.Number(default=0.8, bounds=(0, 1), step=0.01, doc="Intensity 3")
    intensity_background = param.Number(
        default=0.0, bounds=(0, 1), step=0.01, doc="Background intensity"
    )
    target_idx = param.Integer(default=1, bounds=(1, 4), doc="Target index")
    intensity_target = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="Target intensity")
    origin = param.Selector(
        default="center", objects=["mean", "corner", "center"], doc="Origin position"
    )
    rotation = param.Number(default=0.0, bounds=(0, 360), step=1, doc="Rotation in degrees")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "radii": (self.radius1, self.radius2, self.radius3),
            "intensity_frames": (self.intensity1, self.intensity2, self.intensity3),
            "intensity_background": self.intensity_background,
            "intensity_target": self.intensity_target,
            "origin": self.origin,
            "rotation": self.rotation,
        }


class RectangularTwoSidedParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=20, bounds=(1, 40), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    frequency = param.Number(default=1.0, bounds=(0.1, 2), step=0.1, doc="Frequency in cpd")
    phase_shift = param.Number(default=0, bounds=(0, 360), step=1, doc="Phase shift in degrees")
    intensity1 = param.Number(default=1.0, bounds=(0, 1), step=0.01, doc="Intensity 1")
    intensity2 = param.Number(default=0.0, bounds=(0, 1), step=0.01, doc="Intensity 2")
    intensity_background = param.Number(
        default=0.5, bounds=(0, 1), step=0.01, doc="Background intensity"
    )
    target_idx = param.Integer(default=1, bounds=(0, 10), doc="Target index")
    intensity_target_left = param.Number(
        default=0.5, bounds=(0, 1), step=0.01, doc="Left target intensity"
    )
    intensity_target_right = param.Number(
        default=0.5, bounds=(0, 1), step=0.01, doc="Right target intensity"
    )

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "frequency": self.frequency,
            "phase_shift": self.phase_shift,
            "intensity_frames": (
                (self.intensity1, self.intensity2),
                (self.intensity2, self.intensity1),
            ),
            "intensity_background": self.intensity_background,
            "intensity_target": (self.intensity_target_left, self.intensity_target_right),
        }


__all__ = [
    "CircularParams",
    "CircularGeneralizedParams",
    "CircularTwoSidedParams",
    "RectangularParams",
    "RectangularGeneralizedParams",
    "RectangularTwoSidedParams",
]
