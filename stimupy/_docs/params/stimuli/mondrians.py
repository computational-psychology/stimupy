"""Parameter classes for stimuli.mondrians module."""

import param


class MondrianParams(param.Parameterized):
    # Image size parameters
    height = param.Number(default=10, bounds=(1, 20), doc="Height of image in degrees")
    width = param.Number(default=10, bounds=(1, 20), doc="Width of image in degrees")
    ppd = param.Number(default=32, bounds=(1, 60), doc="Pixels per degree")

    # Mondrian positions (y, x coordinates)
    pos1_y = param.Number(default=0, bounds=(0, 10), doc="Y position of mondrian 1")
    pos1_x = param.Number(default=0, bounds=(0, 10), doc="X position of mondrian 1")
    pos2_y = param.Number(default=8, bounds=(0, 10), doc="Y position of mondrian 2")
    pos2_x = param.Number(default=4, bounds=(0, 10), doc="X position of mondrian 2")
    pos3_y = param.Number(default=1, bounds=(0, 10), doc="Y position of mondrian 3")
    pos3_x = param.Number(default=6, bounds=(0, 10), doc="X position of mondrian 3")

    # Mondrian sizes (height, width, depth)
    size1_h = param.Number(default=3, bounds=(0.5, 8), doc="Height of mondrian 1")
    size1_w = param.Number(default=4, bounds=(0.5, 8), doc="Width of mondrian 1")
    size1_d = param.Number(default=1, bounds=(-2, 2), doc="Depth of mondrian 1")
    size2_h = param.Number(default=2, bounds=(0.5, 8), doc="Height of mondrian 2")
    size2_w = param.Number(default=2, bounds=(0.5, 8), doc="Width of mondrian 2")
    size2_d = param.Number(default=0, bounds=(-2, 2), doc="Depth of mondrian 2")
    size3_h = param.Number(default=5, bounds=(0.5, 8), doc="Height of mondrian 3")
    size3_w = param.Number(default=4, bounds=(0.5, 8), doc="Width of mondrian 3")
    size3_d = param.Number(default=-1, bounds=(-2, 2), doc="Depth of mondrian 3")

    # Intensities
    intensity1 = param.Number(default=0.2, bounds=(0, 1), doc="Intensity of mondrian 1")
    intensity2 = param.Number(default=0.6, bounds=(0, 1), doc="Intensity of mondrian 2")
    intensity3 = param.Number(default=0.9, bounds=(0, 1), doc="Intensity of mondrian 3")
    intensity_background = param.Number(default=0.5, bounds=(0, 1), doc="Background intensity")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "positions": (
                (self.pos1_y, self.pos1_x),
                (self.pos2_y, self.pos2_x),
                (self.pos3_y, self.pos3_x),
            ),
            "sizes": (
                (self.size1_h, self.size1_w, self.size1_d),
                (self.size2_h, self.size2_w, self.size2_d),
                (self.size3_h, self.size3_w, self.size3_d),
            ),
            "intensities": (self.intensity1, self.intensity2, self.intensity3),
            "intensity_background": self.intensity_background,
        }


class CorrugatedMondrianParams(param.Parameterized):
    # Image size parameters
    height = param.Number(default=10, bounds=(1, 20), doc="Height of image in degrees")
    width = param.Number(default=10, bounds=(1, 20), doc="Width of image in degrees")
    ppd = param.Number(default=32, bounds=(1, 60), doc="Pixels per degree")

    # Grid parameters
    nrows = param.Integer(default=4, bounds=(1, 8), doc="Number of rows", allow_None=True)
    ncols = param.Integer(default=4, bounds=(1, 8), doc="Number of columns", allow_None=True)

    # Depth parameters
    depth1 = param.Number(default=1, bounds=(-2, 2), doc="Depth of row 1")
    depth2 = param.Number(default=0, bounds=(-2, 2), doc="Depth of row 2")
    depth3 = param.Number(default=-1, bounds=(-2, 2), doc="Depth of row 3")
    depth4 = param.Number(default=0, bounds=(-2, 2), doc="Depth of row 4")

    # Target parameters
    target_idx1 = param.Integer(default=1, bounds=(0, 3), doc="Target row index 1")
    target_idx2 = param.Integer(default=1, bounds=(0, 3), doc="Target column index 1")
    target_idx3 = param.Integer(default=3, bounds=(0, 3), doc="Target row index 2")
    target_idx4 = param.Integer(default=1, bounds=(0, 3), doc="Target column index 2")
    intensity_target = param.Number(
        default=0.5, bounds=(0, 1), doc="Target intensity", allow_None=True
    )

    # Background intensity
    intensity_background = param.Number(default=0.5, bounds=(0, 1), doc="Background intensity")

    def get_stimulus_params(self):
        import numpy as np

        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "nrows": self.nrows,
            "ncols": self.ncols,
            "depths": (self.depth1, self.depth2, self.depth3, self.depth4),
            "intensities": np.random.rand(4, 4),
            "target_indices": (
                (self.target_idx1, self.target_idx2),
                (self.target_idx3, self.target_idx4),
            ),
            "intensity_background": self.intensity_background,
            "intensity_target": self.intensity_target,
        }


__all__ = ["MondrianParams", "CorrugatedMondrianParams"]
