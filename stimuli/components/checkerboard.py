import warnings

import numpy as np
from stimuli.utils import resolution


def resolve_checkerboard_params(
    ppd=None,
    shape=None,
    visual_size=None,
    board_shape=None,
    check_visual_size=None,
):
    """Resolves (if possible) the various size parameters of the checkerboard

    Checkerboard component takes the regular resolution parameters(shape, ppd,
    visual_size). In addition, there has to be an additional specification of the size
    of the checkerboard. This can be done in two ways: either through a board_shape
    (height and width in integer number of checks), and/or by specifying the size the
    visual size (in degrees) of a single check.

    The total shape (in pixels) and visual size (in degrees) has to match the
    specification of the board shape (in checks) and check size (in degrees). Thus,
    not all 5 parameters have to be specified, as long as the both the resolution
    and the checkerboard size can be resolved.

    Note: all checks in a single board have the same size and shape.


    Parameters
    ----------
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] in pixels
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size of the total board [height, width] in degrees
    board_shape : Sequence[Number, Number], Number, or None (default)
        number of checks in [height, width] of checkerboard
    check_visual_size : Sequence[Number, Number], Number, or None (default)
        visual size of a single check [height, width] in degrees

    Returns
    -------
    dict
        dictionary with all five resolution & size parameters resolved.

    Raises
    ------
    ResolutionError
        if the total resolution (ppd, shape, visual_size) cannot be resolved
    ResolutionError
        if the board_shape and/or check_visual_size cannot be resolved
    ValueError
        if the (resolved) ppd does not allow for drawing (resolved) check_visual_size

    See also:
    ---------
    stimuli.components.checkerboard.checkerboard :
        to draw the actual checkerboard
    """

    # Try to resolve resolution
    try:
        shape, visual_size, ppd = resolution.resolve(shape=shape, visual_size=visual_size, ppd=ppd)
    except ValueError:
        ppd = resolution.validate_ppd(ppd)
        shape = resolution.validate_shape(shape)
        visual_size = resolution.validate_visual_size(visual_size)

    # Put intput check_visual_size and board_shape into canonical form
    check_visual_size = resolution.validate_visual_size(check_visual_size)
    board_shape = resolution.validate_shape(board_shape)

    # Try to resolve board dimensions
    # The logic here is that inverting check_visual_size, which expresses
    # degrees per check, gives "checks per degree", which functions analogous to ppd
    # Thus we can resolve the board dimensions also as a "resolution",
    # and then just invert the resolved "checks_per_degree" back to check_visual_size
    checks_per_degree = (
        1 / check_visual_size.height if check_visual_size.height is not None else None,
        1 / check_visual_size.width if check_visual_size.width is not None else None,
    )
    board_shape, visual_size, checks_per_degree = resolution.resolve(
        shape=board_shape,
        visual_size=visual_size,
        ppd=checks_per_degree,
    )
    check_visual_size = resolution.validate_visual_size(
        (1 / checks_per_degree.vertical, 1 / checks_per_degree.horizontal)
    )

    # Now resolve ppd
    shape, visual_size, ppd = resolution.resolve(shape=shape, visual_size=visual_size, ppd=ppd)

    # Is check_shape possible?
    if (check_visual_size.height * ppd.vertical) % 1 or (
        check_visual_size.width * ppd.horizontal
    ) % 1:
        raise ValueError(f"Cannot produce checks of {check_visual_size} with resolution of {ppd}")

    return {
        "shape": shape,
        "visual_size": visual_size,
        "ppd": ppd,
        "check_visual_size": check_visual_size,
        "board_shape": board_shape,
    }


def checkerboard(
    ppd=None,
    shape=None,
    visual_size=None,
    board_shape=None,
    check_visual_size=None,
    intensity_low=0.0,
    intensity_high=1.0,
):
    """Draws a checkerboard with given specifications

    Parameters
    ----------
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] in pixels
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size of the total board [height, width] in degrees
    board_shape : Sequence[Number, Number], Number, or None (default)
        number of checks in [height, width] of checkerboard
    check_visual_size : Sequence[Number, Number], Number, or None (default)
        visual size of a single check [height, width] in degrees
    intensity_low : float, optional
        intensity value of the dark checks, by default 0.0
    intensity_high : float, optional
        intensity value of the light checks, by default 1.0

    Returns
    -------
    np.ndarray
        image array (2D) containing exactly the checkerboard

    Raises
    ------
    ValueError
        if checkerboard does not fit into specified/resolved shape

    See also
    --------
    stimuli.components.checkerboard.resolve_checkerboard_params :
        how the size & resolution parameters can be resolved
    """

    params = resolve_checkerboard_params(
        ppd=ppd,
        shape=shape,
        visual_size=visual_size,
        board_shape=board_shape,
        check_visual_size=check_visual_size,
    )
    board_shape = params["board_shape"]
    check_visual_size = params["check_visual_size"]
    ppc = resolution.shape_from_visual_size_ppd(check_visual_size, params["ppd"])

    # Build board
    img = np.ndarray(board_shape)
    for i, j in np.ndindex(img.shape):
        img[i, j] = intensity_low if i % 2 == j % 2 else intensity_high

    # Resize by pix per check
    img = img.repeat(ppc.height, axis=0).repeat(ppc.width, axis=1)
    if shape is not None and shape != (None, None):
        if img.shape != shape:
            raise ValueError("Could not fit board in {shape}")

    # Collect stim + params
    stim = params
    stim["img"] = img
    stim["board_shape"] = board_shape

    return stim
