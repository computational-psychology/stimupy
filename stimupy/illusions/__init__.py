from . import (
    angulars,
    checkerboards,
    circulars,
    cornsweets,
    delboeufs,
    frames,
    gratings,
    hermanns,
    mueller_lyers,
    ponzos,
)


def create_overview():
    """
    Create dictionary with examples from all stimulus-illusions

    Returns
    -------
    stims : dict
        dict with all stimuli containing individual stimulus dicts.
    """

    p = {
        "visual_size": (10, 10),
        "ppd": 20,
    }

    p_small_grating = {
        "ppd": 20,
        "frequency": 1,
        "intensity_bars": (1, 0),
    }

    # fmt: off
    stims = {
        # Angular
        "pinwheel": angulars.pinwheel(**p, n_segments=8, target_width=1, target_indices=3),
        # Checkerboards
        "checkerboard": checkerboards.checkerboard(**p, board_shape=8, target_indices=[(3, 2), (3, 5)]),
        "contrast-contrast": checkerboards.contrast_contrast(**p, board_shape=8, target_shape=(4, 4)),
        # Circular
        "circular_rings": circulars.rings(**p, frequency=1.0),
        "circular_rings_two_sided": circulars.two_sided_rings(**p, frequency=1.0),
        "circular_bullseye": circulars.bullseye(**p, frequency=1.0),
        "circular_bullseye_two_sided": circulars.two_sided_bullseye(**p, frequency=1.0),
        # Cornsweet
        "cornsweet": cornsweets.cornsweet(**p, ramp_width=3),
        # Delbouef
        "delboeuf": delboeufs.delboeuf(**p, outer_radius=4, target_radius=1),
        "2sided_delboeuf": delboeufs.two_sided(**p, outer_radii=(2, 1.1), target_radius=1),
        # Frames
        "frames": frames.rings(**p, frequency=0.5, target_indices=3),
        "frames_general": frames.rings_generalized(**p, radii=(1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5), target_indices=3),
        "2sided_frames": frames.two_sided_rings(**p, frequency=1, target_indices=3),
        "frames_bullseye": frames.bullseye(**p, frequency=0.5),
        "frames_bullseye_general": frames.bullseye_generalized(**p, radii=(1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5)),
        "2sided_bullseye": frames.two_sided_bullseye(**p, frequency=1),
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
        "grating_induction_blur": gratings.induction_blur(**p, frequency=0.5, target_width=0.5, sigma=0.1),
        # Hermann´
        "hermann": hermanns.grid(**p, element_size=(1.5, 1.5, 0.2)),
        # Mueller-Lyer
        "mueller-lyer": mueller_lyers.mueller_lyer(**p, outer_lines_length=1.5, outer_lines_angle=45, target_length=6, line_width=0.1),
        "2sided_mueller-lyer": mueller_lyers.two_sided(**p, outer_lines_length=1.5, outer_lines_angle=45, target_length=2.5, line_width=0.1),
        # Ponzo
        "ponzo": ponzos.ponzo(**p, outer_lines_length=8, outer_lines_width=0.1, target_lines_length=3, target_lines_width=0.1, target_distance=3),
    }
    # fmt: on

    return stims


def overview(mask=False, save=None, extent_key="shape"):
    """
    Plot overview with examples from all stimulus-illusions

    Parameters
    ----------
    mask : bool or str, optional
        If True, plot mask on top of stimulus image (default: False).
        If string is provided, plot this key from stimulus dictionary as mask
    save : None or str, optional
        If None (default), do not save the plot.
        If string is provided, save plot under this name.
    extent_key : str, optional
        Key to extent which will be used for plotting.
        Default is "shape", using the image size in pixels as extent.

    """
    from stimupy.utils import plot_stimuli

    stims = create_overview()

    # Plotting
    plot_stimuli(stims, mask=mask, save=save, extent_key=extent_key)
