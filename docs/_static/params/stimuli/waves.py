"""Parameter classes for stimuli.waves module."""

import param


class SineLinearParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    frequency = param.Number(default=1.0, bounds=(0.1, 3), step=0.1, doc="Frequency in cpd")
    rotation = param.Number(default=0, bounds=(0, 360), step=1, doc="Rotation in degrees")
    phase_shift = param.Number(default=0, bounds=(0, 360), step=1, doc="Phase shift in degrees")
    intensity_min = param.Number(default=0.0, bounds=(0, 1), step=0.01, doc="Minimum intensity")
    intensity_max = param.Number(default=1.0, bounds=(0, 1), step=0.01, doc="Maximum intensity")
    origin = param.Selector(default="center", objects=["center", "mean", "corner"], doc="Origin")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "frequency": self.frequency,
            "rotation": self.rotation,
            "phase_shift": self.phase_shift,
            "intensities": (self.intensity_min, self.intensity_max),
            "origin": self.origin,
        }


class SquareLinearParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    frequency = param.Number(default=1.0, bounds=(0.1, 3), step=0.1, doc="Frequency in cpd")
    rotation = param.Number(default=0, bounds=(0, 360), step=1, doc="Rotation in degrees")
    phase_shift = param.Number(default=0, bounds=(0, 360), step=1, doc="Phase shift in degrees")
    intensity_min = param.Number(default=0.0, bounds=(0, 1), step=0.01, doc="Minimum intensity")
    intensity_max = param.Number(default=1.0, bounds=(0, 1), step=0.01, doc="Maximum intensity")
    origin = param.Selector(default="center", objects=["center", "mean", "corner"], doc="Origin")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "frequency": self.frequency,
            "rotation": self.rotation,
            "phase_shift": self.phase_shift,
            "intensity_bars": (self.intensity_min, self.intensity_max),
            "origin": self.origin,
        }


class StaircaseLinearParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    frequency = param.Number(default=1.0, bounds=(0.1, 3), step=0.1, doc="Frequency in cpd")
    rotation = param.Number(default=0, bounds=(0, 360), step=1, doc="Rotation in degrees")
    phase_shift = param.Number(default=0, bounds=(0, 360), step=1, doc="Phase shift in degrees")
    intensity_min = param.Number(default=0.0, bounds=(0, 1), step=0.01, doc="Minimum intensity")
    intensity_max = param.Number(default=1.0, bounds=(0, 1), step=0.01, doc="Maximum intensity")
    origin = param.Selector(default="center", objects=["center", "mean", "corner"], doc="Origin")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "frequency": self.frequency,
            "rotation": self.rotation,
            "phase_shift": self.phase_shift,
            "intensity_bars": (self.intensity_min, self.intensity_max),
            "origin": self.origin,
        }


class SineRadialParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    frequency = param.Number(default=1.0, bounds=(0.1, 3), step=0.1, doc="Frequency in cpd")
    phase_shift = param.Number(default=0, bounds=(0, 360), step=1, doc="Phase shift in degrees")
    intensity_min = param.Number(default=0.0, bounds=(0, 1), step=0.01, doc="Minimum intensity")
    intensity_max = param.Number(default=1.0, bounds=(0, 1), step=0.01, doc="Maximum intensity")
    origin = param.Selector(default="center", objects=["center", "mean", "corner"], doc="Origin")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "frequency": self.frequency,
            "phase_shift": self.phase_shift,
            "intensities": (self.intensity_min, self.intensity_max),
            "origin": self.origin,
        }


class SquareRadialParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    frequency = param.Number(default=1.0, bounds=(0.1, 3), step=0.1, doc="Frequency in cpd")
    phase_shift = param.Number(default=0, bounds=(0, 360), step=1, doc="Phase shift in degrees")
    intensity_min = param.Number(default=0.0, bounds=(0, 1), step=0.01, doc="Minimum intensity")
    intensity_max = param.Number(default=1.0, bounds=(0, 1), step=0.01, doc="Maximum intensity")
    origin = param.Selector(default="center", objects=["center", "mean", "corner"], doc="Origin")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "frequency": self.frequency,
            "phase_shift": self.phase_shift,
            "intensity_rings": (self.intensity_min, self.intensity_max),
            "origin": self.origin,
        }


class StaircaseRadialParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    frequency = param.Number(default=1.0, bounds=(0.1, 3), step=0.1, doc="Frequency in cpd")
    phase_shift = param.Number(default=0, bounds=(0, 360), step=1, doc="Phase shift in degrees")
    intensity_min = param.Number(default=0.0, bounds=(0, 1), step=0.01, doc="Minimum intensity")
    intensity_max = param.Number(default=1.0, bounds=(0, 1), step=0.01, doc="Maximum intensity")
    origin = param.Selector(default="center", objects=["center", "mean", "corner"], doc="Origin")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "frequency": self.frequency,
            "phase_shift": self.phase_shift,
            "intensity_rings": (self.intensity_min, self.intensity_max),
            "origin": self.origin,
        }


class SineAngularParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    frequency = param.Number(default=8.0, bounds=(1, 16), step=0.5, doc="Frequency in cycles")
    phase_shift = param.Number(default=0, bounds=(0, 360), step=1, doc="Phase shift in degrees")
    intensity_min = param.Number(default=0.0, bounds=(0, 1), step=0.01, doc="Minimum intensity")
    intensity_max = param.Number(default=1.0, bounds=(0, 1), step=0.01, doc="Maximum intensity")
    origin = param.Selector(default="center", objects=["center", "mean", "corner"], doc="Origin")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "frequency": self.frequency,
            "phase_shift": self.phase_shift,
            "intensities": (self.intensity_min, self.intensity_max),
            "origin": self.origin,
        }


class SquareAngularParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    frequency = param.Number(default=8.0, bounds=(1, 16), step=0.5, doc="Frequency in cycles")
    phase_shift = param.Number(default=0, bounds=(0, 360), step=1, doc="Phase shift in degrees")
    intensity_min = param.Number(default=0.0, bounds=(0, 1), step=0.01, doc="Minimum intensity")
    intensity_max = param.Number(default=1.0, bounds=(0, 1), step=0.01, doc="Maximum intensity")
    origin = param.Selector(default="center", objects=["center", "mean", "corner"], doc="Origin")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "frequency": self.frequency,
            "phase_shift": self.phase_shift,
            "intensity_segments": (self.intensity_min, self.intensity_max),
            "origin": self.origin,
        }


class StaircaseAngularParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    frequency = param.Number(default=8.0, bounds=(1, 16), step=0.5, doc="Frequency in cycles")
    phase_shift = param.Number(default=0, bounds=(0, 360), step=1, doc="Phase shift in degrees")
    intensity_min = param.Number(default=0.0, bounds=(0, 1), step=0.01, doc="Minimum intensity")
    intensity_max = param.Number(default=1.0, bounds=(0, 1), step=0.01, doc="Maximum intensity")
    origin = param.Selector(default="center", objects=["center", "mean", "corner"], doc="Origin")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "frequency": self.frequency,
            "phase_shift": self.phase_shift,
            "intensity_segments": (self.intensity_min, self.intensity_max),
            "origin": self.origin,
        }


class SineRectilinearParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    frequency = param.Number(default=8.0, bounds=(1, 16), step=0.5, doc="Frequency in cycles")
    phase_shift = param.Number(default=0, bounds=(0, 360), step=1, doc="Phase shift in degrees")
    intensity_min = param.Number(default=0.0, bounds=(0, 1), step=0.01, doc="Minimum intensity")
    intensity_max = param.Number(default=1.0, bounds=(0, 1), step=0.01, doc="Maximum intensity")
    origin = param.Selector(default="center", objects=["center", "mean", "corner"], doc="Origin")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "frequency": self.frequency,
            "phase_shift": self.phase_shift,
            "intensities": (self.intensity_min, self.intensity_max),
            "origin": self.origin,
        }


class SquareRectilinearParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    frequency = param.Number(default=8.0, bounds=(1, 16), step=0.5, doc="Frequency in cycles")
    phase_shift = param.Number(default=0, bounds=(0, 360), step=1, doc="Phase shift in degrees")
    intensity_min = param.Number(default=0.0, bounds=(0, 1), step=0.01, doc="Minimum intensity")
    intensity_max = param.Number(default=1.0, bounds=(0, 1), step=0.01, doc="Maximum intensity")
    origin = param.Selector(default="center", objects=["center", "mean", "corner"], doc="Origin")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "frequency": self.frequency,
            "phase_shift": self.phase_shift,
            "intensity_frames": (self.intensity_min, self.intensity_max),
            "origin": self.origin,
        }


class StaircaseRectilinearParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    frequency = param.Number(default=8.0, bounds=(1, 16), step=0.5, doc="Frequency in cycles")
    phase_shift = param.Number(default=0, bounds=(0, 360), step=1, doc="Phase shift in degrees")
    intensity_min = param.Number(default=0.0, bounds=(0, 1), step=0.01, doc="Minimum intensity")
    intensity_max = param.Number(default=1.0, bounds=(0, 1), step=0.01, doc="Maximum intensity")
    origin = param.Selector(default="center", objects=["center", "mean", "corner"], doc="Origin")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "frequency": self.frequency,
            "phase_shift": self.phase_shift,
            "intensity_frames": (self.intensity_min, self.intensity_max),
            "origin": self.origin,
        }


__all__ = [
    "SineLinearParams",
    "SquareLinearParams",
    "StaircaseLinearParams",
    "SineRadialParams",
    "SquareRadialParams",
    "StaircaseRadialParams",
    "SineAngularParams",
    "SquareAngularParams",
    "StaircaseAngularParams",
    "SineRectilinearParams",
    "SquareRectilinearParams",
    "StaircaseRectilinearParams",
]
