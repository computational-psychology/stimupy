"""Parameter classes for components.radials module."""

import param


class AnnulusParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    # Annulus parameters
    radius_outer = param.Number(default=3, bounds=(1, 5), step=0.1, doc="Outer radius in degrees")
    radius_inner = param.Number(default=1, bounds=(0, 3), step=0.1, doc="Inner radius in degrees")

    # Intensity parameters
    intensity_annulus = param.Number(
        default=1.0, bounds=(0, 1), step=0.01, doc="Annulus intensity"
    )
    intensity_background = param.Number(
        default=0.0, bounds=(0, 1), step=0.01, doc="Background intensity"
    )

    # Additional parameters
    origin = param.Selector(default="center", objects=["center", "mean", "corner"], doc="Origin")
    add_mask = param.Boolean(default=False, doc="Add mask to visualization")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "radii": (self.radius_inner, self.radius_outer),
            "intensity_ring": self.intensity_annulus,
            "intensity_background": self.intensity_background,
            "origin": self.origin,
        }


RingParams = AnnulusParams


class DiscParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    # Disc parameters
    radius = param.Number(default=2, bounds=(0, 4), step=0.1, doc="Radius in degrees")

    # Intensity parameters
    intensity_disc = param.Number(default=1.0, bounds=(0, 1), step=0.01, doc="Disc intensity")
    intensity_background = param.Number(
        default=0.0, bounds=(0, 1), step=0.01, doc="Background intensity"
    )

    # Additional parameters
    origin = param.Selector(default="center", objects=["center", "mean", "corner"], doc="Origin")
    add_mask = param.Boolean(default=False, doc="Add mask to visualization")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "radius": self.radius,
            "intensity_disc": self.intensity_disc,
            "intensity_background": self.intensity_background,
            "origin": self.origin,
        }


class RingsParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    # Rings parameters
    radius1 = param.Number(default=1, bounds=(0, 2), step=0.1, doc="Radius 1 in degrees")
    radius2 = param.Number(default=2, bounds=(1, 3), step=0.1, doc="Radius 2 in degrees")
    radius3 = param.Number(default=3, bounds=(2, 4), step=0.1, doc="Radius 3 in degrees")

    # Intensity parameters
    intensity1 = param.Number(default=0.8, bounds=(0, 1), step=0.01, doc="Ring 1 intensity")
    intensity2 = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="Ring 2 intensity")
    intensity3 = param.Number(default=0.3, bounds=(0, 1), step=0.01, doc="Ring 3 intensity")
    intensity_background = param.Number(
        default=0.0, bounds=(0, 1), step=0.01, doc="Background intensity"
    )

    # Additional parameters
    origin = param.Selector(default="center", objects=["center", "mean", "corner"], doc="Origin")
    add_mask = param.Boolean(default=False, doc="Add mask to visualization")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "radii": (self.radius1, self.radius2, self.radius3),
            "intensity_rings": (self.intensity1, self.intensity2, self.intensity3),
            "intensity_background": self.intensity_background,
            "origin": self.origin,
        }


__all__ = ["AnnulusParams", "DiscParams", "RingParams", "RingsParams"]
