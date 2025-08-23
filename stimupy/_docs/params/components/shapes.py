"""Parameter classes for components.shapes module."""

import param


class AnnulusParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    # Shape parameters
    radius_outer = param.Number(default=3, bounds=(1, 5), step=0.1, doc="Outer radius in degrees")
    radius_inner = param.Number(default=1, bounds=(0, 3), step=0.1, doc="Inner radius in degrees")

    # Intensity parameters
    intensity_ring = param.Number(default=1.0, bounds=(0, 1), step=0.01, doc="Shape intensity")
    intensity_background = param.Number(
        default=0.0, bounds=(0, 1), step=0.01, doc="Background intensity"
    )

    # Additional parameters
    origin = param.Selector(default="center", objects=["center", "mean", "corner"], doc="Origin")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "radii": (self.radius_inner, self.radius_outer),
            "intensity_ring": self.intensity_ring,
            "intensity_background": self.intensity_background,
            "origin": self.origin,
        }


class CircleParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    # Shape parameters
    radius = param.Number(default=2, bounds=(0, 4), step=0.1, doc="Radius in degrees")

    # Intensity parameters
    intensity_circle = param.Number(default=1.0, bounds=(0, 1), step=0.01, doc="Shape intensity")
    intensity_background = param.Number(
        default=0.0, bounds=(0, 1), step=0.01, doc="Background intensity"
    )

    # Additional parameters
    origin = param.Selector(default="center", objects=["center", "mean", "corner"], doc="Origin")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "radius": self.radius,
            "intensity_circle": self.intensity_circle,
            "intensity_background": self.intensity_background,
            "origin": self.origin,
        }


class CrossParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    # Cross parameters
    cross_size_h = param.Number(default=4, bounds=(1, 6), step=0.1, doc="Horizontal cross size")
    cross_size_v = param.Number(default=4, bounds=(1, 6), step=0.1, doc="Vertical cross size")
    cross_thickness = param.Number(default=0.5, bounds=(0.1, 2), step=0.01, doc="Cross thickness")
    cross_arm_ratio = param.Number(
        default=0.2, bounds=(0.1, 0.5), step=0.01, doc="Cross arm ratio"
    )
    rotation = param.Integer(default=0, bounds=(0, 360), doc="Rotation in degrees")

    # Intensity parameters
    intensity_shape = param.Number(default=1.0, bounds=(0, 1), step=0.01, doc="Shape intensity")
    intensity_background = param.Number(
        default=0.0, bounds=(0, 1), step=0.01, doc="Background intensity"
    )

    # Additional parameters
    origin = param.Selector(default="center", objects=["center", "mean", "corner"], doc="Origin")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "cross_size": (self.cross_size_h, self.cross_size_v),
            "cross_thickness": self.cross_thickness,
            "cross_arm_ratios": (self.cross_arm_ratio, self.cross_arm_ratio),
            "rotation": self.rotation,
            "intensity_cross": self.intensity_shape,
            "intensity_background": self.intensity_background,
        }


class DiscParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    # Shape parameters
    radius = param.Number(default=2, bounds=(0, 4), step=0.1, doc="Radius in degrees")

    # Intensity parameters
    intensity_shape = param.Number(default=1.0, bounds=(0, 1), step=0.01, doc="Shape intensity")
    intensity_background = param.Number(
        default=0.0, bounds=(0, 1), step=0.01, doc="Background intensity"
    )

    # Additional parameters
    origin = param.Selector(default="center", objects=["center", "mean", "corner"], doc="Origin")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "radius": self.radius,
            "intensity_disc": self.intensity_shape,
            "intensity_background": self.intensity_background,
            "origin": self.origin,
        }


class EllipseParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    # Shape parameters
    radius1 = param.Number(default=3, bounds=(0, 5), step=0.1, doc="Radius 1 in degrees")
    radius2 = param.Number(default=2, bounds=(0, 5), step=0.1, doc="Radius 2 in degrees")
    rotation = param.Integer(default=0, bounds=(0, 360), doc="Rotation in degrees")

    # Intensity parameters
    intensity_ellipse = param.Number(default=1.0, bounds=(0, 1), step=0.01, doc="Shape intensity")
    intensity_background = param.Number(
        default=0.0, bounds=(0, 1), step=0.01, doc="Background intensity"
    )

    # Additional parameters
    origin = param.Selector(default="center", objects=["center", "mean", "corner"], doc="Origin")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "radius": (self.radius1, self.radius2),
            "rotation": self.rotation,
            "intensity_ellipse": self.intensity_ellipse,
            "intensity_background": self.intensity_background,
            "origin": self.origin,
        }


class ParallelogramParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    parallelogram_height = param.Integer(default=3, bounds=(1, 6), doc="")
    parallelogram_width = param.Integer(default=3, bounds=(1, 6), doc="")
    parallelogram_depth = param.Number(default=1.0, bounds=(-3.0, 3.0), step=0.1, doc="")
    rotation = param.Integer(default=0, bounds=(0, 360), doc="")
    intensity_parallelogram = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="")
    intensity_background = param.Number(default=0.0, bounds=(0, 1), step=0.01, doc="")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "parallelogram_size": (
                self.parallelogram_height,
                self.parallelogram_width,
                self.parallelogram_depth,
            ),
            "rotation": self.rotation,
            "intensity_parallelogram": self.intensity_parallelogram,
            "intensity_background": self.intensity_background,
        }


class RectangleParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    # Shape parameters
    rectangle_height = param.Number(default=3, bounds=(1, 5), step=0.1, doc="Rectangle height")
    rectangle_width = param.Number(default=4, bounds=(1, 6), step=0.1, doc="Rectangle width")
    rotation = param.Integer(default=0, bounds=(0, 360), doc="Rotation in degrees")

    # Intensity parameters
    intensity_shape = param.Number(default=1.0, bounds=(0, 1), step=0.01, doc="Shape intensity")
    intensity_background = param.Number(
        default=0.0, bounds=(0, 1), step=0.01, doc="Background intensity"
    )

    # Additional parameters
    origin = param.Selector(default="center", objects=["center", "mean", "corner"], doc="Origin")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "rectangle_size": (self.rectangle_height, self.rectangle_width),
            "rotation": self.rotation,
            "intensity_rectangle": self.intensity_shape,
            "intensity_background": self.intensity_background,
        }


class RingParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    # Shape parameters
    radius_outer = param.Number(default=3, bounds=(1, 5), step=0.1, doc="Outer radius in degrees")
    radius_inner = param.Number(default=1, bounds=(0, 3), step=0.1, doc="Inner radius in degrees")

    # Intensity parameters
    intensity_shape = param.Number(default=1.0, bounds=(0, 1), step=0.01, doc="Shape intensity")
    intensity_background = param.Number(
        default=0.0, bounds=(0, 1), step=0.01, doc="Background intensity"
    )

    # Additional parameters
    origin = param.Selector(default="center", objects=["center", "mean", "corner"], doc="Origin")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "radii": (self.radius_inner, self.radius_outer),
            "intensity_ring": self.intensity_shape,
            "intensity_background": self.intensity_background,
            "origin": self.origin,
        }


class TriangleParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    # Shape parameters
    triangle_size = param.Number(default=3, bounds=(1, 5), step=0.1, doc="Triangle size")
    rotation = param.Integer(default=0, bounds=(0, 360), doc="Rotation in degrees")

    # Intensity parameters
    intensity_shape = param.Number(default=1.0, bounds=(0, 1), step=0.01, doc="Shape intensity")
    intensity_background = param.Number(
        default=0.0, bounds=(0, 1), step=0.01, doc="Background intensity"
    )

    # Additional parameters
    origin = param.Selector(default="center", objects=["center", "mean", "corner"], doc="Origin")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "triangle_size": self.triangle_size,
            "rotation": self.rotation,
            "intensity_triangle": self.intensity_shape,
            "intensity_background": self.intensity_background,
        }


class WedgeParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    # Shape parameters
    angle = param.Integer(default=45, bounds=(1, 180), doc="Wedge angle in degrees")
    radius = param.Number(default=3, bounds=(1, 5), step=0.1, doc="Radius in degrees")
    rotation = param.Integer(default=0, bounds=(0, 360), doc="Rotation in degrees")

    # Intensity parameters
    intensity_wedge = param.Number(default=1.0, bounds=(0, 1), step=0.01, doc="Shape intensity")
    intensity_background = param.Number(
        default=0.0, bounds=(0, 1), step=0.01, doc="Background intensity"
    )

    # Additional parameters
    origin = param.Selector(default="center", objects=["center", "mean", "corner"], doc="Origin")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "angle": self.angle,
            "radius": self.radius,
            "rotation": self.rotation,
            "intensity_wedge": self.intensity_wedge,
            "intensity_background": self.intensity_background,
            "origin": self.origin,
        }


__all__ = [
    "CrossParams",
    "DiscParams",
    "EllipseParams",
    "ParallelogramParams",
    "RectangleParams",
    "RingParams",
    "TriangleParams",
    "CircleParams",
    "AnnulusParams",
    "WedgeParams",
]
