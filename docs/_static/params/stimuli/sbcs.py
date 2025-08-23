"""Parameter classes for stimuli.sbcs module."""

import param


class BasicParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    target_height = param.Number(default=3.0, bounds=(1, 6), step=0.1, doc="Target height")
    target_width = param.Number(default=3.0, bounds=(1, 6), step=0.1, doc="Target width")
    intensity_background = param.Number(
        default=0.0, bounds=(0, 1), step=0.01, doc="Background intensity"
    )
    intensity_target = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="Target intensity")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "target_size": (self.target_height, self.target_width),
            "intensity_background": self.intensity_background,
            "intensity_target": self.intensity_target,
        }


class GeneralizedParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    target_height = param.Number(default=3.0, bounds=(1, 6), step=0.1, doc="Target height")
    target_width = param.Number(default=3.0, bounds=(1, 6), step=0.1, doc="Target width")
    target_x = param.Number(default=3.0, bounds=(0, 10), step=0.1, doc="Target X position")
    target_y = param.Number(default=3.0, bounds=(0, 10), step=0.1, doc="Target Y position")
    rotation = param.Number(default=0.0, bounds=(0, 360), step=1, doc="Rotation in degrees")
    intensity_background = param.Number(
        default=0.0, bounds=(0, 1), step=0.01, doc="Background intensity"
    )
    intensity_target = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="Target intensity")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "target_size": (self.target_height, self.target_width),
            "target_position": (self.target_y, self.target_x),
            "rotation": self.rotation,
            "intensity_background": self.intensity_background,
            "intensity_target": self.intensity_target,
        }


class SquareParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    target_radius = param.Number(default=1.0, bounds=(0.1, 3), step=0.1, doc="Target radius")
    surround_radius = param.Number(default=2.0, bounds=(1, 4), step=0.1, doc="Surround radius")
    rotation = param.Number(default=0.0, bounds=(0, 360), step=1, doc="Rotation in degrees")
    intensity_surround = param.Number(
        default=1.0, bounds=(0, 1), step=0.01, doc="Surround intensity"
    )
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
            "target_radius": self.target_radius,
            "surround_radius": self.surround_radius,
            "rotation": self.rotation,
            "intensity_surround": self.intensity_surround,
            "intensity_background": self.intensity_background,
            "intensity_target": self.intensity_target,
            "origin": self.origin,
        }


class CircularParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    target_radius = param.Number(default=1.0, bounds=(0.1, 3), step=0.1, doc="Target radius")
    surround_radius = param.Number(default=2.0, bounds=(1, 4), step=0.1, doc="Surround radius")
    intensity_surround = param.Number(
        default=1.0, bounds=(0, 1), step=0.01, doc="Surround intensity"
    )
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
            "target_radius": self.target_radius,
            "surround_radius": self.surround_radius,
            "intensity_surround": self.intensity_surround,
            "intensity_background": self.intensity_background,
            "intensity_target": self.intensity_target,
            "origin": self.origin,
        }


class BasicTwoSidedParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    target_height = param.Number(default=3.0, bounds=(1, 6), step=0.1, doc="Target height")
    target_width = param.Number(default=3.0, bounds=(1, 6), step=0.1, doc="Target width")
    intensity_target_left = param.Number(
        default=0.5, bounds=(0, 1), step=0.01, doc="Left target intensity"
    )
    intensity_target_right = param.Number(
        default=0.5, bounds=(0, 1), step=0.01, doc="Right target intensity"
    )
    intensity_background_left = param.Number(
        default=0.0, bounds=(0, 1), step=0.01, doc="Left background intensity"
    )
    intensity_background_right = param.Number(
        default=1.0, bounds=(0, 1), step=0.01, doc="Right background intensity"
    )

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "target_size": (self.target_height, self.target_width),
            "intensity_target": (self.intensity_target_left, self.intensity_target_right),
            "intensity_background": (
                self.intensity_background_left,
                self.intensity_background_right,
            ),
        }


class SquareTwoSidedParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    target_radius_left = param.Number(
        default=1.0, bounds=(0.1, 3), step=0.1, doc="Left target radius"
    )
    target_radius_right = param.Number(
        default=1.0, bounds=(0.1, 3), step=0.1, doc="Right target radius"
    )
    surround_radius_left = param.Number(
        default=2.0, bounds=(1, 4), step=0.1, doc="Left surround radius"
    )
    surround_radius_right = param.Number(
        default=2.0, bounds=(1, 4), step=0.1, doc="Right surround radius"
    )
    rotation_left = param.Number(
        default=0.0, bounds=(0, 360), step=1, doc="Left rotation in degrees"
    )
    rotation_right = param.Number(
        default=0.0, bounds=(0, 360), step=1, doc="Right rotation in degrees"
    )
    intensity_target_left = param.Number(
        default=0.5, bounds=(0, 1), step=0.01, doc="Left target intensity"
    )
    intensity_target_right = param.Number(
        default=0.5, bounds=(0, 1), step=0.01, doc="Right target intensity"
    )
    intensity_surround_left = param.Number(
        default=0.0, bounds=(0, 1), step=0.01, doc="Left surround intensity"
    )
    intensity_surround_right = param.Number(
        default=1.0, bounds=(0, 1), step=0.01, doc="Right surround intensity"
    )
    intensity_background = param.Number(
        default=0.5, bounds=(0, 1), step=0.01, doc="Background intensity"
    )

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "target_radius": (self.target_radius_left, self.target_radius_right),
            "surround_radius": (self.surround_radius_left, self.surround_radius_right),
            "rotation": (self.rotation_left, self.rotation_right),
            "intensity_target": (self.intensity_target_left, self.intensity_target_right),
            "intensity_surround": (self.intensity_surround_left, self.intensity_surround_right),
            "intensity_background": self.intensity_background,
        }


class CircularTwoSidedParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    target_radius_left = param.Number(
        default=1.0, bounds=(0.1, 3), step=0.1, doc="Left target radius"
    )
    target_radius_right = param.Number(
        default=1.0, bounds=(0.1, 3), step=0.1, doc="Right target radius"
    )
    surround_radius_left = param.Number(
        default=2.0, bounds=(1, 4), step=0.1, doc="Left surround radius"
    )
    surround_radius_right = param.Number(
        default=2.0, bounds=(1, 4), step=0.1, doc="Right surround radius"
    )
    intensity_target_left = param.Number(
        default=0.5, bounds=(0, 1), step=0.01, doc="Left target intensity"
    )
    intensity_target_right = param.Number(
        default=0.5, bounds=(0, 1), step=0.01, doc="Right target intensity"
    )
    intensity_surround_left = param.Number(
        default=0.0, bounds=(0, 1), step=0.01, doc="Left surround intensity"
    )
    intensity_surround_right = param.Number(
        default=1.0, bounds=(0, 1), step=0.01, doc="Right surround intensity"
    )
    intensity_background = param.Number(
        default=0.5, bounds=(0, 1), step=0.01, doc="Background intensity"
    )

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "target_radius": (self.target_radius_left, self.target_radius_right),
            "surround_radius": (self.surround_radius_left, self.surround_radius_right),
            "intensity_target": (self.intensity_target_left, self.intensity_target_right),
            "intensity_surround": (self.intensity_surround_left, self.intensity_surround_right),
            "intensity_background": self.intensity_background,
        }


class WithDotsParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    n_dots = param.Tuple(default=(5, 5), doc="Number of dots (vertical, horizontal)")
    dot_radius = param.Number(default=0.2, bounds=(0.05, 0.5), step=0.01, doc="Dot radius")
    distance = param.Number(
        default=0.05, bounds=(0.01, 0.2), step=0.01, doc="Distance between dots"
    )
    target_shape = param.Tuple(default=(3, 3), doc="Target shape in dots")
    intensity_background = param.Number(
        default=0.0, bounds=(0, 1), step=0.01, doc="Background intensity"
    )
    intensity_dots = param.Number(default=1.0, bounds=(0, 1), step=0.01, doc="Dot intensity")
    intensity_target = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="Target intensity")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "n_dots": self.n_dots,
            "dot_radius": self.dot_radius,
            "distance": self.distance,
            "target_shape": self.target_shape,
            "intensity_background": self.intensity_background,
            "intensity_dots": self.intensity_dots,
            "intensity_target": self.intensity_target,
        }


class DottedParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    n_dots = param.Tuple(default=(5, 5), doc="Number of dots (vertical, horizontal)")
    dot_radius = param.Number(default=0.2, bounds=(0.05, 0.5), step=0.01, doc="Dot radius")
    distance = param.Number(
        default=0.05, bounds=(0.01, 0.2), step=0.01, doc="Distance between dots"
    )
    target_shape = param.Tuple(default=(3, 3), doc="Target shape in dots")
    intensity_background = param.Number(
        default=0.0, bounds=(0, 1), step=0.01, doc="Background intensity"
    )
    intensity_dots = param.Number(default=1.0, bounds=(0, 1), step=0.01, doc="Dot intensity")
    intensity_target = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="Target intensity")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "n_dots": self.n_dots,
            "dot_radius": self.dot_radius,
            "distance": self.distance,
            "target_shape": self.target_shape,
            "intensity_background": self.intensity_background,
            "intensity_dots": self.intensity_dots,
            "intensity_target": self.intensity_target,
        }


__all__ = [
    "BasicParams",
    "GeneralizedParams",
    "SquareParams",
    "CircularParams",
    "BasicTwoSidedParams",
    "SquareTwoSidedParams",
    "CircularTwoSidedParams",
    "WithDotsParams",
    "DottedParams",
]
