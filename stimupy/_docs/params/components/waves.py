"""Parameter classes for components.waves module."""

import param


class BesselParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    # Wave parameters
    frequency = param.Number(default=1.0, bounds=(0.1, 3), step=0.1, doc="Frequency in cpd")
    order = param.Integer(default=0, bounds=(0, 5), doc="Bessel function order")

    # Intensity parameters
    intensity_min = param.Number(default=0.0, bounds=(0, 1), step=0.01, doc="Minimum intensity")
    intensity_max = param.Number(default=1.0, bounds=(0, 1), step=0.01, doc="Maximum intensity")

    # Additional parameters
    origin = param.Selector(default="center", objects=["center", "mean", "corner"], doc="Origin")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "frequency": self.frequency,
            "order": self.order,
            "intensities": (self.intensity_max, self.intensity_min),
            "origin": self.origin,
        }


class SineParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    # Wave parameters
    frequency = param.Number(default=1.0, bounds=(0.1, 3), step=0.1, doc="Frequency in cpd")
    phase_shift = param.Number(default=0, bounds=(0, 360), step=1, doc="Phase shift in degrees")
    rotation = param.Number(default=0, bounds=(0, 360), step=1, doc="Rotation in degrees")
    distance_metric = param.Selector(
        default="horizontal",
        objects=["horizontal", "vertical", "oblique", "radial", "angular", "rectilinear"],
        doc="Distance metric",
    )

    # Intensity parameters
    intensity_min = param.Number(default=0.0, bounds=(0, 1), step=0.01, doc="Minimum intensity")
    intensity_max = param.Number(default=1.0, bounds=(0, 1), step=0.01, doc="Maximum intensity")

    # Additional parameters
    origin = param.Selector(default="center", objects=["center", "mean", "corner"], doc="Origin")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "frequency": self.frequency,
            "phase_shift": self.phase_shift,
            "rotation": self.rotation,
            "distance_metric": self.distance_metric,
            "intensities": (self.intensity_min, self.intensity_max),
            "origin": self.origin,
        }


class SquareParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    # Wave parameters
    frequency = param.Number(default=1.0, bounds=(0.1, 3), step=0.1, doc="Frequency in cpd")
    phase_shift = param.Number(default=0, bounds=(0, 360), step=1, doc="Phase shift in degrees")
    rotation = param.Number(default=0, bounds=(0, 360), step=1, doc="Rotation in degrees")
    distance_metric = param.Selector(
        default="horizontal",
        objects=["horizontal", "vertical", "oblique", "radial", "angular", "rectilinear"],
        doc="Distance metric",
    )

    # Intensity parameters
    intensity_min = param.Number(default=0.0, bounds=(0, 1), step=0.01, doc="Minimum intensity")
    intensity_max = param.Number(default=1.0, bounds=(0, 1), step=0.01, doc="Maximum intensity")

    # Additional parameters
    origin = param.Selector(default="center", objects=["center", "mean", "corner"], doc="Origin")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "frequency": self.frequency,
            "phase_shift": self.phase_shift,
            "rotation": self.rotation,
            "distance_metric": self.distance_metric,
            "intensities": (self.intensity_min, self.intensity_max),
            "origin": self.origin,
        }


class StaircaseParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    # Wave parameters
    frequency = param.Number(default=1.0, bounds=(0.1, 3), step=0.1, doc="Frequency in cpd")
    phase_shift = param.Number(default=0, bounds=(0, 360), step=1, doc="Phase shift in degrees")
    rotation = param.Number(default=0, bounds=(0, 360), step=1, doc="Rotation in degrees")
    distance_metric = param.Selector(
        default="horizontal",
        objects=["horizontal", "vertical", "oblique", "radial", "angular", "rectilinear"],
        doc="Distance metric",
    )

    # Intensity parameters
    intensity_min = param.Number(default=0.0, bounds=(0, 1), step=0.01, doc="Minimum intensity")
    intensity_max = param.Number(default=1.0, bounds=(0, 1), step=0.01, doc="Maximum intensity")

    # Additional parameters
    origin = param.Selector(default="center", objects=["center", "mean", "corner"], doc="Origin")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "frequency": self.frequency,
            "phase_shift": self.phase_shift,
            "rotation": self.rotation,
            "distance_metric": self.distance_metric,
            "intensities": (self.intensity_min, self.intensity_max),
            "origin": self.origin,
        }


__all__ = ["BesselParams", "SineParams", "SquareParams", "StaircaseParams"]
