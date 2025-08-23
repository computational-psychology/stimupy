"""Parameter classes for stimuli.hermanns module."""

import param


class GridParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    # Element geometry parameters
    element_height = param.Number(default=1, bounds=(0.1, 2), step=0.1, doc="Element height")
    element_width = param.Number(default=1, bounds=(0.1, 2), step=0.1, doc="Element width")
    element_thickness = param.Number(
        default=0.1, bounds=(0.1, 1), step=0.1, doc="Element thickness"
    )

    # Intensity parameters
    intensity_grid = param.Number(default=1, bounds=(0, 1), step=0.01, doc="Grid intensity")
    intensity_background = param.Number(
        default=0, bounds=(0, 1), step=0.01, doc="Background intensity"
    )

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "element_size": (self.element_height, self.element_width, self.element_thickness),
            "intensity_background": self.intensity_background,
            "intensity_grid": self.intensity_grid,
        }


__all__ = ["GridParams"]
