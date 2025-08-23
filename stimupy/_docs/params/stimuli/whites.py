"""Parameter classes for stimuli.whites module."""

import param


class WhiteParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    frequency = param.Number(default=1.0, bounds=(0.1, 3), step=0.1, doc="Frequency in cpd")
    target_indices = param.Tuple(default=(3, 4), length=2, doc="Target bar indices")
    target_heights = param.Tuple(default=(2.0, 2.0), length=2, doc="Target heights")
    intensity_bars = param.Tuple(default=(0.0, 1.0), length=2, doc="Bar intensities (low, high)")
    intensity_target = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="Target intensity")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "frequency": self.frequency,
            "target_indices": self.target_indices,
            "target_heights": self.target_heights,
            "intensity_bars": self.intensity_bars,
            "intensity_target": self.intensity_target,
        }


class GeneralizedParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    frequency = param.Number(default=1, bounds=(0, 2), step=0.1, doc="Frequency in cpd")
    rotation = param.Number(default=0, bounds=(0, 360), step=1, doc="Rotation in degrees")
    intensity_bars_low = param.Number(default=0, bounds=(0, 1), step=0.01, doc="Low bar intensity")
    intensity_bars_high = param.Number(
        default=1, bounds=(0, 1), step=0.01, doc="High bar intensity"
    )
    target_indices = param.List(default=[1], doc="Target indices")
    intensity_target = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="Target intensity")
    target_center_offsets = param.Number(
        default=0, bounds=(-5, 5), step=0.1, doc="Target center offsets"
    )
    target_heights = param.Number(default=2.0, bounds=(0.5, 5), step=0.1, doc="Target heights")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "frequency": self.frequency,
            "rotation": self.rotation,
            "intensity_bars": (self.intensity_bars_low, self.intensity_bars_high),
            "target_indices": self.target_indices,
            "intensity_target": self.intensity_target,
            "target_center_offsets": self.target_center_offsets,
            "target_heights": self.target_heights,
        }


class WhiteTwoRowsParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    frequency = param.Number(default=1, bounds=(0, 2), step=0.1, doc="Frequency in cpd")
    rotation = param.Number(default=0, bounds=(0, 360), step=1, doc="Rotation in degrees")
    intensity_bars_low = param.Number(default=0, bounds=(0, 1), step=0.01, doc="Low bar intensity")
    intensity_bars_high = param.Number(
        default=1, bounds=(0, 1), step=0.01, doc="High bar intensity"
    )
    intensity_target = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="Target intensity")
    target_indices_top = param.List(default=[1], doc="Top target indices")
    target_indices_bottom = param.List(default=[1], doc="Bottom target indices")
    target_center_offset = param.Number(
        default=2.0, bounds=(0, 5), step=0.1, doc="Target center offset"
    )
    target_heights = param.Number(default=2.0, bounds=(0.5, 5), step=0.1, doc="Target heights")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "frequency": self.frequency,
            "rotation": self.rotation,
            "intensity_bars": (self.intensity_bars_low, self.intensity_bars_high),
            "intensity_target": self.intensity_target,
            "target_indices_top": self.target_indices_top,
            "target_indices_bottom": self.target_indices_bottom,
            "target_center_offset": self.target_center_offset,
            "target_heights": self.target_heights,
        }


class AngularParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    frequency = param.Number(default=8.0, bounds=(2, 16), step=0.5, doc="Frequency in cycles")
    rotation = param.Number(default=0, bounds=(0, 360), step=1, doc="Rotation in degrees")
    target_width = param.Number(default=0.5, bounds=(0.1, 5), step=0.1, doc="Target width")
    target_center = param.Number(default=1.0, bounds=(0, 1), step=0.01, doc="Target center")
    target_indices = param.Tuple(default=(2, 3), length=2, doc="Target segment indices")
    intensity_segments = param.Tuple(
        default=(0.0, 1.0), length=2, doc="Segment intensities (low, high)"
    )
    intensity_target = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="Target intensity")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "rotation": self.rotation,
            "frequency": self.frequency,
            "target_indices": self.target_indices,
            "target_width": self.target_width,
            "target_center": self.target_center,
            "intensity_segments": self.intensity_segments,
            "intensity_target": self.intensity_target,
        }


class RadialParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    frequency = param.Number(default=1.0, bounds=(0.1, 3), step=0.1, doc="Frequency in cpd")
    target_indices = param.Tuple(default=(2, 3), length=2, doc="Target ring indices")
    intensity_rings = param.Tuple(default=(0.0, 1.0), length=2, doc="Ring intensities (low, high)")
    intensity_target = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="Target intensity")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "frequency": self.frequency,
            "target_indices": self.target_indices,
            "intensity_rings": self.intensity_rings,
            "intensity_target": self.intensity_target,
        }


class AndersonParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    frequency = param.Number(default=1, bounds=(0, 2), step=0.1, doc="Frequency in cpd")
    intensity_bars_low = param.Number(default=0, bounds=(0, 1), step=0.01, doc="Low bar intensity")
    intensity_bars_high = param.Number(
        default=1, bounds=(0, 1), step=0.01, doc="High bar intensity"
    )
    intensity_target = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="Target intensity")
    target_indices_top = param.List(default=[1], doc="Top target indices")
    target_indices_bottom = param.List(default=[2], doc="Bottom target indices")
    target_center_offset = param.Number(
        default=2.0, bounds=(0, 5), step=0.1, doc="Target center offset"
    )
    target_height = param.Number(default=2.0, bounds=(1, 5), step=0.1, doc="Target height")
    intensity_stripes_low = param.Number(
        default=0, bounds=(0, 1), step=0.01, doc="Low stripe intensity"
    )
    intensity_stripes_high = param.Number(
        default=1, bounds=(0, 1), step=0.01, doc="High stripe intensity"
    )
    stripe_center_offset = param.Number(
        default=2, bounds=(-5, 5), step=0.1, doc="Stripe center offset"
    )
    stripe_height = param.Number(default=1.0, bounds=(0.5, 3), step=0.1, doc="Stripe height")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "frequency": self.frequency,
            "intensity_bars": (self.intensity_bars_low, self.intensity_bars_high),
            "intensity_target": self.intensity_target,
            "target_indices_top": self.target_indices_top,
            "target_indices_bottom": self.target_indices_bottom,
            "target_center_offset": self.target_center_offset,
            "target_height": self.target_height,
            "intensity_stripes": (self.intensity_stripes_low, self.intensity_stripes_high),
            "stripe_center_offset": self.stripe_center_offset,
            "stripe_height": self.stripe_height,
        }


class HoweParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    frequency = param.Number(default=1, bounds=(0, 2), step=0.1, doc="Frequency in cpd")
    intensity_bars_low = param.Number(default=0, bounds=(0, 1), step=0.01, doc="Low bar intensity")
    intensity_bars_high = param.Number(
        default=1, bounds=(0, 1), step=0.01, doc="High bar intensity"
    )
    intensity_target = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="Target intensity")
    target_indices_top = param.List(default=[1], doc="Top target indices")
    target_indices_bottom = param.List(default=[2], doc="Bottom target indices")
    target_center_offset = param.Number(
        default=2.0, bounds=(0, 5), step=0.1, doc="Target center offset"
    )
    target_height = param.Number(default=2.0, bounds=(1, 5), step=0.1, doc="Target height")
    intensity_stripes_low = param.Number(
        default=0, bounds=(0, 1), step=0.01, doc="Low stripe intensity"
    )
    intensity_stripes_high = param.Number(
        default=1, bounds=(0, 1), step=0.01, doc="High stripe intensity"
    )

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "frequency": self.frequency,
            "intensity_bars": (self.intensity_bars_low, self.intensity_bars_high),
            "intensity_target": self.intensity_target,
            "target_indices_top": self.target_indices_top,
            "target_indices_bottom": self.target_indices_bottom,
            "target_center_offset": self.target_center_offset,
            "target_height": self.target_height,
            "intensity_stripes": (self.intensity_stripes_low, self.intensity_stripes_high),
        }


class YazdanbakhshParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    frequency = param.Number(default=1, bounds=(0, 2), step=0.1, doc="Frequency in cpd")
    n_bars = param.Integer(default=10, bounds=(4, 20), doc="Number of bars")
    target_indices_top = param.List(default=[2], doc="Top target indices")
    target_indices_bottom = param.List(default=[-3], doc="Bottom target indices")
    target_center_offset = param.Number(
        default=2.0, bounds=(0, 5), step=0.1, doc="Target center offset"
    )
    target_heights = param.Number(default=2.0, bounds=(1, 5), step=0.1, doc="Target heights")
    gap_size = param.Number(default=0.5, bounds=(0, 2), step=0.1, doc="Gap size")
    intensity_bars_low = param.Number(default=0, bounds=(0, 1), step=0.01, doc="Low bar intensity")
    intensity_bars_high = param.Number(
        default=1, bounds=(0, 1), step=0.01, doc="High bar intensity"
    )
    intensity_target = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="Target intensity")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "frequency": self.frequency,
            "n_bars": self.n_bars,
            "target_indices_top": self.target_indices_top,
            "target_indices_bottom": self.target_indices_bottom,
            "target_center_offset": self.target_center_offset,
            "target_heights": self.target_heights,
            "gap_size": self.gap_size,
            "intensity_bars": (self.intensity_bars_low, self.intensity_bars_high),
            "intensity_target": self.intensity_target,
        }


class WeddingCakeParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    L_size_height = param.Number(default=4, bounds=(1, 8), step=0.1, doc="L height")
    L_size_width = param.Number(default=3, bounds=(1, 6), step=0.1, doc="L width")
    L_size_thickness = param.Number(default=1, bounds=(0.5, 3), step=0.1, doc="L thickness")
    target_height = param.Number(default=1.0, bounds=(0.5, 3), step=0.1, doc="Target height")
    target_indices1_y1 = param.Integer(default=2, bounds=(0, 5), doc="Target 1 Y1 index")
    target_indices1_x1 = param.Integer(default=2, bounds=(0, 5), doc="Target 1 X1 index")
    target_indices1_y2 = param.Integer(default=2, bounds=(0, 5), doc="Target 1 Y2 index")
    target_indices1_x2 = param.Integer(default=1, bounds=(0, 5), doc="Target 1 X2 index")
    target_indices2_y1 = param.Integer(default=2, bounds=(0, 5), doc="Target 2 Y1 index")
    target_indices2_x1 = param.Integer(default=-1, bounds=(-5, 5), doc="Target 2 X1 index")
    target_indices2_y2 = param.Integer(default=2, bounds=(0, 5), doc="Target 2 Y2 index")
    target_indices2_x2 = param.Integer(default=0, bounds=(-5, 5), doc="Target 2 X2 index")
    intensity_bars_low = param.Number(default=0, bounds=(0, 1), step=0.01, doc="Low bar intensity")
    intensity_bars_high = param.Number(
        default=1, bounds=(0, 1), step=0.01, doc="High bar intensity"
    )
    intensity_target = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="Target intensity")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "L_size": (self.L_size_height, self.L_size_width, self.L_size_thickness),
            "target_height": self.target_height,
            "target_indices1": (
                (self.target_indices1_y1, self.target_indices1_x1),
                (self.target_indices1_y2, self.target_indices1_x2),
            ),
            "target_indices2": (
                (self.target_indices2_y1, self.target_indices2_x1),
                (self.target_indices2_y2, self.target_indices2_x2),
            ),
            "intensity_bars": (self.intensity_bars_low, self.intensity_bars_high),
            "intensity_target": self.intensity_target,
        }


__all__ = [
    "WhiteParams",
    "GeneralizedParams",
    "WhiteTwoRowsParams",
    "AngularParams",
    "RadialParams",
    "AndersonParams",
    "HoweParams",
    "YazdanbakhshParams",
    "WeddingCakeParams",
]
