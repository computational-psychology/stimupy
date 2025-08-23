"""Parameter classes for stimuli.dungeons module."""

import param


class DungeonParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    # Grid geometry parameters
    n_cells1 = param.Integer(default=5, bounds=(2, 10), doc="Number of cells 1")
    n_cells2 = param.Integer(default=5, bounds=(2, 10), doc="Number of cells 2")

    # Intensity parameters
    intensity_grid = param.Number(default=1, bounds=(0, 1), step=0.01, doc="Grid intensity")
    intensity_background = param.Number(
        default=0.0, bounds=(0, 1), step=0.01, doc="Background intensity"
    )

    # Target parameters
    target_radius = param.Integer(default=1, bounds=(0, 3), doc="Target radius")
    intensity_target = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="Target intensity")

    # Additional parameters
    add_mask = param.Selector(default=None, objects=[None, "target_mask"], doc="Add mask")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "n_cells": (self.n_cells1, self.n_cells2),
            "intensity_grid": self.intensity_grid,
            "intensity_background": self.intensity_background,
            "target_radius": self.target_radius,
            "intensity_target": self.intensity_target,
        }


__all__ = ["DungeonParams"]
