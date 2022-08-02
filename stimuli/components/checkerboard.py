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

    # Try to resolve resolution
    try:
        shape, visual_size, ppd = resolution.resolve(
            shape=shape, visual_size=visual_size, ppd=ppd
        )
    except ValueError:
        ppd = resolution.validate_ppd(ppd)
        shape = resolution.validate_shape(shape)
        visual_size = resolution.validate_visual_size(visual_size)

    check_visual_size = resolution.validate_visual_size(check_visual_size)
    board_shape = resolution.validate_shape(board_shape)

    # Resolve board_shape
    if board_shape.width is None:
        # Board shape is not specified, try to figure it out
        if check_visual_size.width is None:
            raise ValueError("Need to specify either board_shape or check_visual_size")
        elif visual_size.width is None:
            raise ValueError(
                "Cannot compute board_shape.width without check_visual_size.width or"
                " visual_size.width"
            )
        else:
            board_width = visual_size.width / check_visual_size.width
    else:
        board_width = board_shape.width
    if int(board_width) % board_width:
        warnings.warn(f"Rounding shape of board")
    board_width = int(board_width)
    if board_shape.height is None:
        # Board shape is not specified, try to figure it out
        if check_visual_size.height is None:
            raise ValueError("Need to specify either board_shape or check_visual_size")
        elif visual_size.height is None:
            raise ValueError(
                "Cannot compute board_shape.height without check_visual_size.height or"
                " visual_size.height"
            )
        else:
            board_height = visual_size.height / check_visual_size.height
    else:
        board_height = board_shape.height
    if int(board_height) % board_height:
        warnings.warn(f"Rounding shape of board")
    board_height = int(board_height)
    board_shape = resolution.Shape(height=board_height, width=board_width)
    assert board_shape is not None and all(board_shape)

    # Resolve visual_size
    if visual_size.width is None:
        if check_visual_size.width is not None:
            visual_width = check_visual_size.width * board_shape.width
        else:
            raise ValueError("Need to specify either check_visual_size, or visual_size")
    else:
        visual_width = visual_size.width
    if visual_size.height is None:
        if check_visual_size.height is not None:
            visual_height = check_visual_size.height * board_shape.height
        else:
            raise ValueError("Need to specify either check_visual_size, or visual_size")
    else:
        visual_height = visual_size.height
    visual_size = resolution.Visual_size(visual_height, visual_width)
    assert visual_size is not None and all(visual_size)

    # Resolve check_visual_size
    if check_visual_size.width is None:
        if visual_size.width is not None:
            check_width = visual_size.width / board_shape.width
    else:
        check_width = check_visual_size.width
    if check_visual_size.height is None:
        if visual_size.height is not None:
            check_height = visual_size.height / board_shape.height
    else:
        check_height = check_visual_size.height
    check_visual_size = resolution.Visual_size(height=check_height, width=check_width)

    # Check that board shape * check size == visual size
    # resolution.valid_resolution(shape=visual_size, visual_size=board_shape, ppd=check_visual_size)

    # Now resolve ppd
    shape, visual_size, ppd = resolution.resolve(
        shape=shape, visual_size=visual_size, ppd=ppd
    )
    if ppd is None or not all(ppd):
        raise ValueError("Could not resolve ppd")

    # Is check_shape possible?
    if (check_visual_size.height * ppd.vertical) % 1 or (
        check_visual_size.width * ppd.horizontal
    ) % 1:
        raise ValueError(
            f"Cannot produce checks of {check_visual_size} with resolution of {ppd}"
        )

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
