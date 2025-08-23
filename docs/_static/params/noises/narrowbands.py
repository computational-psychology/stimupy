import param


class NarrowbandParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    center_frequency = param.Number(default=5.0, bounds=(0.1, 12), step=0.1, doc="")
    bandwidth = param.Number(default=1, bounds=(0.1, 2), step=0.1, doc="")
    intensity_min = param.Number(default=0.0, bounds=(0, 1), step=0.01, doc="")
    intensity_max = param.Number(default=1.0, bounds=(0, 1), step=0.01, doc="")
    pseudo_noise = param.Boolean(default=False, doc="")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "center_frequency": self.center_frequency,
            "bandwidth": self.bandwidth,
            "intensity_range": (self.intensity_min, self.intensity_max),
            "pseudo_noise": self.pseudo_noise,
        }


__all__ = ["NarrowbandParams"]
