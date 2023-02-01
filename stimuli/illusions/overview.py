import stimuli.illusions.angulars as angulars
import stimuli.illusions.benarys as benarys
import stimuli.illusions.checkerboards as checkerboards
import stimuli.illusions.circulars as circulars
from stimuli.illusions.cornsweets import cornsweet
import stimuli.illusions.cubes as cubes
from stimuli.illusions.delbouefs import delboeuf
from stimuli.illusions.dungeons import dungeon
import stimuli.illusions.gratings as gratings
from stimuli.illusions.hermanns import grid as hermann_grid
from stimuli.illusions.mondrians import corrugated_mondrians
from stimuli.illusions.mueller_lyers import mueller_lyer as mueller
from stimuli.illusions.ponzos import ponzo
import stimuli.illusions.sbcs as sbcs
import stimuli.illusions.todorovics as todorovics
from stimuli.illusions.wedding_cakes import wedding_cake
import stimuli.illusions.whites as whites
import stimuli.illusions.frames as frames
from stimuli.utils import plot_stimuli

p = {
    "visual_size": (10, 10),
    "ppd": 20,
}

p_mondrians = {
    "mondrian_depths": (0.0, 1.0, 0.0, -1.0),
    "target_indices": ((1, 1), (3, 1)),
    "mondrian_intensities": (
        (0.4, 0.75, 0.4, 0.75),
        (0.75, 0.4, 0.75, 1.0),
        (0.4, 0.75, 0.4, 0.75),
        (0.0, 0.4, 0.0, 0.4),
    ),
}


p_small_grating = {
    "ppd": 20,
    "frequency": 1,
    "intensity_bars": (1, 0),
    }

# fmt: off
stims = {
    # Angular
    "pinwheel": angulars.pinwheel(**p, n_segments=8),
    # Benary
    "benary_general": benarys.cross_generalized(**p, target_size=1, cross_thickness=2, target_x=(3, 6, 3, 6), target_y=(4, 6, 6, 4)),
    "benary_rectangles": benarys.cross_rectangles(**p, target_size=1, cross_thickness=2),
    "benary_triangles": benarys.cross_triangles(**p, target_size=1, cross_thickness=2),
    "todorovic_benary_general": benarys.todorovic_generalized(**p, L_width=2, target_size=1, target_x=(3, 6, 3, 6), target_y=(4, 6, 6, 4)),
    "todorovic_benary_rectangles": benarys.todorovic_rectangles(**p, target_size=1, L_width=2),
    "todorovic_benary_triangles": benarys.todorovic_triangles(**p, target_size=1, L_width=2),
    # Checkerboards
    "checkerboard": checkerboards.checkerboard(**p, board_shape=8, target_indices=[(3, 2), (3, 5)]),
    "contrast-contrast": checkerboards.contrast_contrast(**p, board_shape=8, target_shape=(4, 4)),
    # Circular
    "circular_rings": circulars.rings(**p, frequency=1.0),
    "circular_bullseye": circulars.bullseye(**p, frequency=1.0),
    # Cornsweet
    "cornsweet": cornsweet(**p, ramp_width=3),
    # Cube
    "cube_variable": cubes.varying_cells(ppd=20, cell_heights=(1, 1.5, 1), cell_widths=(1.5, 2, 1.5), cell_spacing=0.5, targets=1),
    "cube": cubes.cube(**p, n_cells=5, targets=(1, 2), cell_thickness=1, cell_spacing=0.5),
    # Delbouef
    "delbouef": delboeuf(**p, outer_radius=4, target_radius=3),
    # Dungeon
    "dungeon": dungeon(**p, n_cells=5),
    # Frames
    "frames": frames.rings(**p, frequency=0.5, target_indices=3),
    "frames_general": frames.rings_generalized(**p, frame_radii=(1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5), target_indices=3),
    "frames_bullseye": frames.bullseye(**p, frequency=0.5),
    "frames_bullseye_general": frames.bullseye_generalized(**p, frame_radii=(1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5)),
    # Grating
    "square_wave": gratings.square_wave(**p, frequency=0.5, target_indices=(3,)),
    "grating_uniform": gratings.uniform(**p, frequency=1, grating_size=3, target_indices=(3,)),
    "grating_grating1": gratings.grating(large_grating_params={**p, "frequency": 2, "rotation": 45},
                                         small_grating_params={**p_small_grating, "visual_size": 4, "target_indices": (1, 3, 5, 7),}),
    "grating_grating2": gratings.grating(large_grating_params={**p, "frequency": 1},
                                         small_grating_params={**p_small_grating, "visual_size": 4,"target_indices": (1, 3, 5, 7),}),
    "grating_grating3": gratings.grating(large_grating_params={**p, "frequency": 1, "intensity_bars": (0, 1),},
                                         small_grating_params={**p_small_grating, "visual_size": (4, 10), "target_indices": (9, 11, 13),}),
    "grating_grating_masked": gratings.grating_masked(large_grating_params={**p, "frequency": 1, "rotation": 90,},
                                                      small_grating_params={**p_small_grating, "visual_size": 4, "target_indices": (1, 3, 5, 7),},
                                                      mask_size=(2, 2, 1)),
    "counterphase_induction": gratings.counterphase_induction(**p, frequency=1, target_size=4, target_phase_shift=90,),
    "grating_induction": gratings.induction(**p, frequency=0.5, target_width=0.5),
    "grating_induction_blur": gratings.induction_blur(**p, frequency=0.5, target_width=0.5, target_blur=2),
    # Hermann´
    "hermann": hermann_grid(**p, element_size=(1.5, 1.5, 0.2)),
    # Mondrians
    "mondrians": corrugated_mondrians(**p, **p_mondrians),
    # Mueller-Lyer
    "mueller-lyer": mueller(**p, outer_lines_length=1.5, outer_lines_angle=45, target_length=6, line_width=0.1),
    # Ponzo
    "ponzo": ponzo(**p, outer_lines_length=8, outer_lines_width=0.1, target_lines_length=3, target_lines_width=0.1, target_distance=3),
    # SBC
    "sbc_generalized": sbcs.generalized(**p, target_size=3, target_position=(0, 2)),
    "sbc_basic": sbcs.basic(**p, target_size=3),
    "sbc_two_sided": sbcs.two_sided(**p, target_size=3),
    "sbc_with_dots": sbcs.with_dots(ppd=20, n_dots=5, dot_radius=3, distance=0.5, target_shape=3),
    "sbc_dotted": sbcs.dotted(ppd=20, n_dots=5, dot_radius=3, distance=0.5, target_shape=3),
    # Todorovic
    "todorovic_rectangle_general": todorovics.rectangle_generalized(**p, target_size=4, target_position=3, covers_size=2, covers_x=(2, 6), covers_y=(2, 6)),
    "todorovic_rectangle": todorovics.rectangle(**p, target_size=4, covers_size=2, covers_offset=2),
    "todorovic_cross_general": todorovics.cross_generalized(**p, cross_size=4, cross_arm_ratios=1., cross_thickness=2, covers_size=2, covers_x=(2, 6), covers_y=(2, 6)),
    "todorovic_cross": todorovics.cross(**p, cross_size=4, cross_thickness=2, covers_size=2),
    "todorovic_equal": todorovics.equal(**p, cross_size=4, cross_thickness=2),
    # Wedding cake
    "wedding_cake": wedding_cake(**p, L_size=(3, 3, 1), target_height=1, target_indices1=((1, 1), (2, 1)),),
    # White
    "white_general": whites.generalized(**p, frequency=0.5, target_indices=(1, 3, 5), target_center_offsets=(-1, -3, -1), target_heights=(2, 3, 2)),
    "white_basic": whites.white(**p, frequency=0.5, target_indices=(2, -3), target_height=2),
    "white_two-rows": whites.white_two_rows(**p, frequency=0.5, target_indices_top=(2,4), target_indices_bottom=(-2, -4), target_height=1, target_center_offset=2),
    "Anderson White": whites.anderson(**p, frequency=0.5, target_indices_top=3, target_indices_bottom=-2, target_center_offset=2, target_height=2, stripe_center_offset=1.5, stripe_height=2),
    "Yazdanbakhsh White": whites.yazdanbakhsh(**p, frequency=0.5, target_indices_top=3, target_indices_bottom=-2, target_center_offset=2, target_height=2, gap_size=0.5),
    "Howe White": whites.howe(**p, frequency=0.5, target_indices_top=3, target_indices_bottom=-2, target_center_offset=2, target_height=2),
}


if __name__ == "__main__":
    plot_stimuli(stims, mask=True, save=None)
