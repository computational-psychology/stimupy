import numpy as np
from stimuli.utils import plot_stimuli
import stimuli.components.angulars as angulars
import stimuli.components.checkerboards as checkerboards
import stimuli.components.circulars as circulars
import stimuli.components.edges as edges
import stimuli.components.frames as frames
import stimuli.components.gaussians as gaussians
import stimuli.components.gratings as gratings
import stimuli.components.lines as lines
import stimuli.components.mondrians as mondrians
import stimuli.components.shapes as shapes


p = {
    "visual_size": 10,
    "ppd": 20,
    }

p_mondrians = {
    "mondrian_positions": ((0,0), (0,5), (1,3), (4,6), (6,1)),
    "mondrian_sizes": 3,
    "mondrian_intensities": np.random.rand(5),
    }

# fmt: off
stims = {
    # angulars
    "wedge": angulars.wedge(**p, width=30, radius=3),
    "angular_grating": angulars.grating(**p, n_segments=8),
    "pinwheel": angulars.pinwheel(**p, n_segments=8, radius=3),
    # checkerboards
    "checkerboard_v1": checkerboards.checkerboard(**p, board_shape=(10, 10)),
    "checkerboard_v2": checkerboards.checkerboard(**p, board_shape=(10, 10), rotation=45),
    "checkerboard_v3": checkerboards.checkerboard(**p, frequency=1),
    "checkerboard_v4": checkerboards.checkerboard(**p, frequency=1, rotation=45),
    # circulars
    "disc_and_rings": circulars.disc_and_rings(**p, radii=[1, 2, 3]),
    "disc": circulars.disc(**p, radius=3),
    "ring": circulars.ring(**p, radii=(1, 3)),
    "anngulus (=ring)": circulars.annulus(**p, radii=(1, 3)),
    "circular_grating": circulars.grating(**p, frequency=1),
    "circular_grating_v2": circulars.grating(**p, n_rings=8),
    "bessel": circulars.bessel(**p, frequency=1),
    # edges
    "step_edge": edges.step_edge(**p),
    "gassian_edge": edges.gaussian_edge(**p, sigma=1.5),
    "cornsweet_edge": edges.cornsweet_edge(**p, ramp_width=3),
    # frames
    "frames": frames.frames(**p, frame_radii=(1, 2, 3)),
    "frames_grating": frames.grating(**p, n_frames=8),
    # gaussians
    "gaussian": gaussians.gaussian(**p, sigma=(1, 2)),
    # gratings
    "square_wave": gratings.square_wave(**p, frequency=1),
    "square_wave2": gratings.square_wave(**p, frequency=1, rotation=45),
    "sine_wave": gratings.sine_wave(**p, frequency=1),
    "gabor": gratings.gabor(**p, frequency=1, sigma=2),
    "staircase": gratings.staircase(**p, n_bars=8),
    "plaid": gratings.plaid(grating_parameters1={**p, "frequency": 1},
                            grating_parameters2={**p, "frequency": 1, "rotation": 90},
                            sigma=2),
    # lines
    "line": lines.line(**p, line_length=3),
    "dipole": lines.dipole(**p, line_length=3, line_gap=0.5),
    "line_circle": lines.circle(**p, radius=3),
    # mondrians
    "mondrians": mondrians.mondrians(**p, **p_mondrians),
    # shapes
    "rectangle": shapes.rectangle(**p, rectangle_size=3),
    "triangle": shapes.triangle(**p, triangle_size=3),
    "cross": shapes.cross(**p, cross_size=3, cross_thickness=0.5),
    "parallelogram": shapes.parallelogram(**p, parallelogram_size=(3, 3, 1)),
    "ellipse": shapes.ellipse(**p, radius=(2, 3)),
    "shape_wedge": shapes.wedge(**p, width=30, radius=3),
    "shape_annulus": shapes.annulus(**p, radii=(1, 3)),
    "shape_ring": shapes.ring(**p, radii=(1, 3)),
    "shape_disc": shapes.disc(**p, radius=3),
}


if __name__ == "__main__":
    plot_stimuli(stims, mask=False, save=None)
