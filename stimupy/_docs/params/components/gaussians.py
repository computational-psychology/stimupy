"""Parameter classes for components.gaussians module."""

import param


class GaussianParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    # Gaussian parameters
    sigma1 = param.Number(default=1, bounds=(0, 3), step=0.1, doc="Sigma 1 in degrees")
    sigma2 = param.Number(default=1, bounds=(0, 3), step=0.1, doc="Sigma 2 in degrees")
    rotation = param.Integer(default=0, bounds=(0, 360), doc="Rotation in degrees")

    # Intensity parameters
    intensity_max = param.Number(default=1.0, bounds=(0, 1), step=0.01, doc="Maximum intensity")

    # Additional parameters
    origin = param.Selector(default="center", objects=["center", "mean", "corner"], doc="Origin")
    add_mask = param.Boolean(default=False, doc="Add mask to visualization")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "sigma": (self.sigma1, self.sigma2),
            "origin": self.origin,
            "rotation": self.rotation,
            "intensity_max": self.intensity_max,
        }


__all__ = ["GaussianParams"]
