import stimuli.illusions.angular as angular
import stimuli.illusions.benary_cross as benarys
import stimuli.illusions.checkerboards as checkerboards
import stimuli.illusions.circular as circular
import stimuli.illusions.cornsweet as cornsweet
import stimuli.illusions.cube as cube
import stimuli.illusions.dungeon as dungeon
import stimuli.illusions.grating as grating
import stimuli.illusions.hermann as hermann
import stimuli.illusions.mondrians as mondrians
import stimuli.illusions.sbc as sbc
import stimuli.illusions.todorovic as todorovic
import stimuli.illusions.wedding_cake as wedding_cake
import stimuli.illusions.whites as whites
from stimuli.illusions import bullseye as bullseye
from stimuli.illusions import frames as frames  # TODO: rename?
from stimuli.utils import plot_stimuli

p = {
    "visual_size": (10, 10),
    "ppd": 20,
}

p_mondrians = {
    "ppd": 10,
    "width": 2.0,
    "heights": 2.0,
    "depths": (0.0, 1.0, 0.0, -1.0),
    "target_indices": ((1, 1), (3, 1)),
    "intensities": (
        (0.4, 0.75, 0.4, 0.75),
        (0.75, 0.4, 0.75, 1.0),
        (0.4, 0.75, 0.4, 0.75),
        (0.0, 0.4, 0.0, 0.4),
    ),
}

# fmt: off
stims = {
    # Angular
    "Radial white": angular.radial_white(**p, n_segments=8),
    # Benary
    "Benary-general": benarys.benarys_cross_generalized(**p, target_size=1, cross_thickness=2, target_x=(3, 6, 3, 6), target_y=(4, 6, 6, 4)),
    "Benary-rectangles": benarys.benarys_cross_rectangles(**p, target_size=1, cross_thickness=2),
    "Benary-triangles": benarys.benarys_cross_triangles(**p, target_size=1, cross_thickness=2),
    "Todorovic' Benary - generalized": benarys.todorovic_benary_generalized(**p, L_width=2, target_size=1, target_x=(3, 6, 3, 6), target_y=(4, 6, 6, 4)),
    "Todorovic' Benary - rectangles": benarys.todorovic_benary_rectangles(**p, target_size=1, L_width=2),
    "Todorovic' Benary - triangles": benarys.todorovic_benary_triangles(**p, target_size=1, L_width=2),
    # Checkerboards
    "Checkerboard": checkerboards.checkerboard(**p, board_shape=8, targets=[(3, 2), (3, 5)]),
    "Contrast-contrast": checkerboards.contrast_contrast(**p, board_shape=8, target_shape=(4, 4)),
    # Circular
    "Circular White": circular.circular_white(**p, frequency=1.0),
    "Circular Bullseye": circular.circular_bullseye(**p, frequency=1.0),
    # Cornsweet
    "Cornsweet": cornsweet(**p, ramp_width=3),
    # Cube
    "Cube - variable cells": cube.cube_varying_cells(ppd=20, cell_heights=(1, 1.5, 1), cell_widths=(1.5, 2, 1.5), cell_spacing=0.5, targets=1),
    "Cube": cube.cube_illusion(**p, n_cells=5, targets=(1, 2), cell_thickness=1, cell_spacing=0.5),
    # Dungeon
    "Dungeon": dungeon.dungeon_illusion(**p, n_cells=5),
    # Frames
    "Frames": frames(**p, frequency=0.5, target_indices=3),
    "Bullseye": bullseye(**p, frequency=0.5),
    # Grating
    "Grating with targets": grating.square_wave(**p, frequency=0.5, target_indices=(3, 6)),
    "Grating uniform": grating.grating_uniform(**p, frequency=1, grating_size=3, target_indices=(3, 5)),
    "Grating grating": grating.grating_grating(ppd=20, large_grating_params={"visual_size": 10, "frequency": 1,}, small_grating_params={"visual_size": 3, "frequency": 1,}),
    # TODO: add other grating stims
    # Hermann
    "Hermann": hermann.hermann_grid(**p, element_size=(1.5, 1.5, 0.2)),
    # Mondrians
    "Mondrians": mondrians.corrugated_mondrians(**p_mondrians),
    # SBC
    "SBC - generalized": sbc.simultaneous_contrast_generalized(**p, target_size=3, target_position=(0, 2)),
    "SBC": sbc.simultaneous_contrast(**p, target_size=3),
    "SBC with dots": sbc.sbc_with_dots(ppd=20, n_dots=5, dot_radius=3, distance=0.5, target_shape=3),
    "Dotted SBC": sbc.dotted_sbc(ppd=20, n_dots=5, dot_radius=3, distance=0.5, target_shape=3),
    # Todorovic
    "Todorovic rectangle, general": todorovic.todorovic_rectangle_generalized(**p, target_size=4, target_position=3, covers_size=2, covers_x=(2, 6), covers_y=(2, 6)),
    "Todorovic rectangle": todorovic.todorovic_rectangle(**p, target_size=4, covers_size=2, covers_offset=2),
    "Todorovic cross, general": todorovic.todorovic_cross_generalized(**p, cross_size=4, cross_arm_ratios=1., cross_thickness=2, covers_size=2, covers_x=(2, 6), covers_y=(2, 6)),
    "Todorovic cross": todorovic.todorovic_cross(**p, cross_size=4, cross_thickness=2, covers_size=2),
    "Todorovic equal": todorovic.todorovic_equal(**p, cross_size=4, cross_thickness=2),
    # Wedding cake
    "Wedding cake": wedding_cake.wedding_cake_stimulus(**p, L_size=(3, 3, 1), target_height=1, target_indices1=((1, 1), (2, 1)),),
    # White
    "White flexible": whites.white_generalized(**p, grating_frequency=0.5, target_indices=(1, 3, 5), target_center_offsets=(-1, -3, -1), target_sizes=(2, 3, 2)),
    "White single row": whites.white(**p, grating_frequency=0.5, target_indices=(2, -3), target_size=2),
    "White two rows": whites.white_two_rows(**p, grating_frequency=0.5, target_indices_top=(2,4), target_indices_bottom=(-2, -4), target_size=1, target_center_offset=2),
    "Anderson White": whites.white_anderson(**p, grating_frequency=0.5, target_indices_top=3, target_indices_bottom=-2, target_center_offset=2, target_size=2, stripe_center_offset=1.5, stripe_size=2),
    "Yazdanbakhsh White": whites.white_yazdanbakhsh(**p, grating_frequency=0.5, target_indices_top=3, target_indices_bottom=-2, target_center_offset=2, target_size=2, gap_size=0.5),
    "Howe White": whites.white_howe(**p, grating_frequency=0.5, target_indices_top=3, target_indices_bottom=-2, target_center_offset=2, target_size=2),
}


if __name__ == "__main__":
    plot_stimuli(stims, mask=False, save=None)
