import numpy as np
from stimuli.components import checkerboard as board
from stimuli.components import transparency
from stimuli.utils import resolution


__all__ = [
    "checkerboard",
    "contrast_contrast",
]

def mask_from_idx(checkerboard_stim, check_idc):
    """Create binary mask for specified check indidces

    Parameters
    ----------
    checkerboard_stim : dict
        stimulus dictionary of checkerboard,
    check_idc : Sequence[(Number, Number),...]
        target indices (row, column of checkerboard) of checks to create mask for

    Returns
    -------
    numpy.ndarray
        mask, as binary 2D numpy.ndarray with 1 for all pixels beloning to
        specified check(s), and 0 everywhere else

    Raises
    ------
    ValueError
        Check index is invalid given the board shape

    See also
    --------
    stimuli.components.checkerboard
    """
    board_shape = checkerboard_stim["board_shape"]

    check_size = checkerboard_stim["check_visual_size"]
    ppd = checkerboard_stim["ppd"]

    check_size_px = resolution.shape_from_visual_size_ppd(check_size, ppd)

    mask = np.zeros(checkerboard_stim["shape"])
    for coords in check_idc:
        if coords[0] < 0 or coords[0] > coords[0] or coords[1] < 0 or coords[1] > board_shape[1]:
            raise ValueError(f"Cannot provide mask for check {coords} outside board {board_shape}")
        ypos = int(coords[0] * check_size_px.height)
        xpos = int(coords[1] * check_size_px.width)
        mask[
            ypos : ypos + int(check_size_px.height),
            xpos : xpos + int(check_size_px.width),
        ] = 1

    return mask


def extend_target_idx(target_idx, offsets=[(-1, 0), (0, -1), (0, 0), (0, 1), (1, 0)]):
    """Extend target indices, to not just the specified check(s) but also surrounding

    Parameters
    ----------
    target_idx : (Number, Number)
        target indices (row, column of checkerboard)
    offsets : list, optional
        relative indices of neighboring checks to include in target,
        by default [(-1, 0), (0, -1), (0, 0), (0, 1), (1, 0)]

    Returns
    -------
    List[Tuple(Number, Number),...]
        List of all target indices
    """
    extended_idc = []
    for offset in offsets:
        new_idx = (target_idx[0] + offset[0], target_idx[1] + offset[1])
        extended_idc.append(new_idx)
    return extended_idc


def add_targets(checkerboard_stim, targets, extend_targets=False, intensity_target=0.5):
    """Add targets to a checkerboard stimulus

    Parameters
    ----------
    checkerboard_stim : dict
        stimulus dictionary of checkerboard,
        needs to contain at least "img" and "board_shape"
    targets : Sequence[(Number, Number),...]
        target indices (row, column of checkerboard)
    extend_targets : bool, optional
        if true, extends the targets by 1 check in all 4 directions, by default False
    intensity_target : float, optional
        intensity value of the target checks, by default 0.5

    Returns
    -------
    dict
        Stimulus dictionary that was passed in, with an updated "img",
        and "mask" : target region(s) mask, as 2D numpy.ndarray with integer values
        indicating target region

    See also
    --------
    stimuli.components.checkerboard
    """
    mask = np.zeros(checkerboard_stim["shape"])
    for i, target in enumerate(targets):
        if extend_targets:
            target_idc = extend_target_idx(target)
        else:
            target_idc = [target]
        for target_idx in target_idc:
            mask += mask_from_idx(checkerboard_stim, (target_idx,)) * (i + 1)
    img = np.where(mask, intensity_target, checkerboard_stim["img"])

    checkerboard_stim["img"] = img
    checkerboard_stim["mask"] = mask.astype(int)
    return checkerboard_stim


def checkerboard(
    shape=None,
    ppd=None,
    visual_size=None,
    board_shape=None,
    check_visual_size=None,
    targets=None,
    extend_targets=False,
    intensity_low=0.0,
    intensity_high=1.0,
    intensity_target=0.5,
):
    """Checkerboard assimilation effect

    High-contrast checkerboard, with intermediate targets embedded in it.
    Target brightness assimilates to direct surround, rather than contrast with it.

    These kinds of checkerboard displays are described by De Valois & De Valois (1988),
    and the brightness effect of it by Blakeslee & McCourt (2004).

    Parameters
    ----------
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] in pixels
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size of the total board [height, width] in degrees
    board_shape : Sequence[Number, Number], Number, or None (default)
        number of checks in [height, width] of checkerboard
    check_visual_size : Sequence[Number, Number], Number, or None (default)
        visual size of a single check [height, width] in degrees
    targets : Sequence[(Number, Number),...], optional
        target indices (row, column of checkerboard), by default None
    extend_targets : bool, optional
        if true, extends the targets by 1 check in all 4 directions, by default False
    intensity_low : float, optional
        intensity value of the dark checks (top left corner), by default 0.0
    intensity_high : float, optional
        intensity value of the light checks, by default 1.0
    intensity_target : float, optional
        intensity value of the target checks, by default 0.5

    Returns
    -------
    dict
        Stimulus dictionary, with all the (resolved) params and:
            'img' : stimulus image as 2D numpy.ndarray
            'mask' : target region(s) mask,
                     as 2D numpy.ndarray with integer values indicating target region

    See also
    --------
    stimuli.components.checkerboard

    References
    ----------
    Blakeslee, B., & McCourt, M. E. (2004). A unified theory of brightness contrast and
        assimilation incorporating oriented multiscale spatial filtering and contrast
        normalization. Vision Research, 44(21), 2483-2503. https://doi.org/10/fmcx5p
    De Valois, R. L., & De Valois, K. K. (1988). Spatial Vision. Oxford University Press.

    """

    # Set up basic checkerboard
    stim = board(
        ppd=ppd,
        shape=shape,
        visual_size=visual_size,
        board_shape=board_shape,
        check_visual_size=check_visual_size,
        intensity_low=intensity_low,
        intensity_high=intensity_high,
    )

    # Add targets
    if targets is not None:
        stim = add_targets(
            stim,
            targets=targets,
            extend_targets=extend_targets,
            intensity_target=intensity_target,
        )
    else:
        stim["mask"] = None
    return stim


def contrast_contrast(
    shape=None,
    ppd=None,
    visual_size=None,
    board_shape=None,
    check_visual_size=None,
    target_shape=(2, 3),
    intensity_low=0.0,
    intensity_high=1.0,
    tau=0.5,
    alpha=0.2,
):
    """Contrast-contrast effect on checkerboard with square transparency layer

    Checkerboard version of the contrast-contrast illusion (Chubb, Sperling, Solomon,
    1989), as used by Domijan (2015).

    Parameters
    ----------
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] in pixels
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size of the total board [height, width] in degrees
    board_shape : Sequence[Number, Number], Number, or None (default)
        number of checks in [height, width] of checkerboard
    check_visual_size : Sequence[Number, Number], Number, or None (default)
        visual size of a single check [height, width] in degrees
    targets_shape : (int, int)
        number of checks with transparency in y, x direction
    intensity_low : float, optional
        intensity value of the dark checks, by default 0.0
    intensity_high : float, optional
        intensity value of the light checks, by default 1.0
    tau : Number
        tau of transparency (i.e. value of transparent medium), default 0.5
    alpha : Number
        alpha of transparency (i.e. how transparant the medium is), default 0.2

    Returns
    -------
    dict
        Stimulus dictionary, with all  of the (resolved) params, and:
            "img" : stimulus image as 2D numpy.ndarray
            "mask" : target region(s) mask,
                     as 2D numpy.ndarray with integer values indicating target region


    References:
    -----------
    Chubb, C., Sperling, G., & Solomon, J. A. (1989). Texture interactions determine
        perceived contrast. Proc. Natl. Acad. Sci. USA, 5.
        https://doi.org/10.1073/pnas.86.23.9631
    Domijan, D. (2015). A Neurocomputational account of the role of contour facilitation
        in brightness perception. Frontiers in Human Neuroscience, 9(February), 1-16.
        https://doi.org/10/gh62x2

    """

    # Set up basic checkerboard
    stim = board(
        ppd=ppd,
        shape=shape,
        visual_size=visual_size,
        board_shape=board_shape,
        check_visual_size=check_visual_size,
        intensity_low=intensity_low,
        intensity_high=intensity_high,
    )
    img = stim["img"]

    # Determine target locations
    check_size_px = resolution.shape_from_visual_size_ppd(
        visual_size=stim["check_visual_size"], ppd=stim["ppd"]
    )
    target_idx = np.zeros(img.shape, dtype=bool)
    tposy = (img.shape[0] - target_shape[0] * check_size_px.height) // 2
    tposx = (img.shape[1] - target_shape[1] * check_size_px.width) // 2
    target_idx[
        tposy : tposy + target_shape[0] * check_size_px[0],
        tposx : tposx + target_shape[1] * check_size_px[1],
    ] = True

    # Construct mask for target region
    mask = np.zeros(img.shape)
    mask[target_idx] = 1

    # Apply transparency to target locations
    img = transparency(img, mask, alpha, tau)

    # Update stim dict
    stim["img"] = img
    stim["mask"] = mask.astype(int)
    stim["alpha"] = alpha
    stim["tau"] = tau

    return stim


if __name__ == "__main__":
    from stimuli.utils import plot_stimuli

    stims = {
        "Checkerboard (brightness)": checkerboard(
            ppd=32,
            board_shape=(8, 8),
            check_visual_size=(2, 2),
            targets=[(3, 2), (5, 5)],
        ),
        "Checkerboard contrast-contrast": contrast_contrast(
            ppd=32, board_shape=(8, 8), check_visual_size=(2, 2), target_shape=(4, 4)
        ),
    }
    plot_stimuli(stims, mask=True, save=None)
