"""Parameter classes for stimuli.pinwheels module."""

import param


class PinwheelParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    n_segments = param.Integer(default=6, bounds=(2, 12), doc="Number of segments")
    rotation = param.Number(default=0, bounds=(0, 360), step=1, doc="Rotation in degrees")
    intensity1 = param.Number(default=0.0, bounds=(0, 1), step=0.01, doc="Intensity 1")
    intensity2 = param.Number(default=1.0, bounds=(0, 1), step=0.01, doc="Intensity 2")
    intensity_background = param.Number(
        default=0.5, bounds=(0, 1), step=0.01, doc="Background intensity"
    )
    target_idx = param.Integer(default=3, bounds=(0, 12), doc="Target index")
    target_width = param.Number(default=2.0, bounds=(0.1, 5), step=0.1, doc="Target width")
    target_center = param.Number(
        default=2.5, bounds=(0.5, 5), step=0.1, doc="Target center radius"
    )
    intensity_target = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="Target intensity")
    origin = param.Selector(
        default="mean", objects=["mean", "corner", "center"], doc="Origin position"
    )

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "n_segments": self.n_segments,
            "rotation": self.rotation,
            "intensity_segments": (self.intensity1, self.intensity2),
            "intensity_background": self.intensity_background,
            "target_indices": (self.target_idx,),
            "target_width": self.target_width,
            "target_center": self.target_center,
            "intensity_target": self.intensity_target,
            "origin": self.origin,
        }


__all__ = ["PinwheelParams"]
