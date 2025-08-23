"""Parameter classes for stimuli.wedding_cakes module."""

import param


class WeddingCakeParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    L_height = param.Number(default=2, bounds=(1, 5), step=0.1, doc="L height")
    L_width = param.Number(default=2, bounds=(1, 5), step=0.1, doc="L width")
    L_thickness = param.Number(default=0.5, bounds=(0.1, 2), step=0.1, doc="L thickness")
    target_height = param.Number(default=0.5, bounds=(0.1, 2), step=0.1, doc="Target height")
    intensity1 = param.Number(default=0.0, bounds=(0, 1), step=0.01, doc="Intensity 1")
    intensity2 = param.Number(default=1.0, bounds=(0, 1), step=0.01, doc="Intensity 2")
    intensity_target = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="Target intensity")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "L_size": (self.L_height, self.L_width, self.L_thickness),
            "target_height": self.target_height,
            "target_indices1": ((0, 0),),
            "target_indices2": ((0, 0),),
            "intensity_bars": (self.intensity1, self.intensity2),
            "intensity_target": self.intensity_target,
        }


__all__ = ["WeddingCakeParams"]
