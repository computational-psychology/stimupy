from collections import namedtuple

Visual_size = namedtuple("Visual_size", "width height")
Shape = namedtuple("Shape", "width height")
Ppd = namedtuple("Ppd", "horizontal vertical")


def ppd_from_shape_visual_size(shape, visual_size):
    shape = validate_shape(shape)
    visual_size = validate_visual_size(visual_size)

    # Calculate horizontal and vertical ppds
    if visual_size.width is not None and shape.width is not None:
        horizontal = shape.width / visual_size.width
    else:
        horizontal = None

    if visual_size.height is not None and shape.height is not None:
        vertical = shape.height / visual_size.height
    else:
        vertical = None

    # Construct ppd namedtuple
    ppd = Ppd(horizontal=horizontal, vertical=vertical)

    return ppd


def validate_shape(shape):
    # Check if string:
    if isinstance(shape, str):
        shape = float(shape)

    # Check if sequence
    try:
        len(shape)
    except TypeError:  # not a sequence; make it one
        shape = (shape, shape)

    # Check if length == 2
    if len(shape) == 1:
        # If Sequence of len()=1 is passed in, use as both height and width
        shape = (shape[0], shape[0])
    elif len(shape) > 2:
        # If Sequence of len()>2 is passed in: error
        raise TypeError(f"shape must be of length 1 or 2, not greater: {shape}")

    # Unpack
    width = shape[0]
    height = shape[1]

    # TODO: check if whole integer?

    # Convert to float
    if width is not None:
        width = int(width)
    if height is not None:
        height = int(height)

    # Check non-negative
    if (width is not None and width <= 0) or (height is not None and height <= 0):
        raise ValueError(f"shape has to be positive; {width, height}")

    # Initiate namedtuple:
    return Shape(width, height)


def validate_ppd(ppd):
    # Check if string:
    if isinstance(ppd, str):
        ppd = float(ppd)

    # Check if sequence
    try:
        len(ppd)
    except TypeError:  # not a sequence; make it one
        ppd = (ppd, ppd)

    # Check if length == 2
    if len(ppd) == 1:
        # If Sequence of len()=1 is passed in, use as both height and width
        ppd = (ppd[0], ppd[0])
    elif len(ppd) > 2:
        # If Sequence of len()>2 is passed in: error
        raise TypeError(f"ppd must be of length 1 or 2, not greater: {ppd}")

    # Unpack
    horizontal = ppd[0]
    vertical = ppd[1]

    # TODO: check if whole integer?

    # Convert to float
    if horizontal is not None:
        horizontal = int(horizontal)
    if vertical is not None:
        vertical = int(vertical)

    # Check non-negative
    if (horizontal is not None and horizontal <= 0) or (
        vertical is not None and vertical <= 0
    ):
        raise ValueError(f"ppd has to be positive; {horizontal, vertical}")

    # Initiate namedtuple:
    return Ppd(horizontal, vertical)


def validate_visual_size(visual_size):
    # Check if string:
    if isinstance(visual_size, str):
        visual_size = float(visual_size)

    # Check if sequence
    try:
        len(visual_size)
    except TypeError:  # not a sequence; make it one
        visual_size = (visual_size, visual_size)

    # Check if length == 2
    if len(visual_size) == 1:
        # If Sequence of len()=1 is passed in, use as both height and width
        visual_size = (visual_size[0], visual_size[0])
    elif len(visual_size) > 2:
        # If Sequence of len()>2 is passed in: error
        raise TypeError(
            f"visual_size must be of length 1 or 2, not greater: {visual_size}"
        )

    # Unpack
    width = visual_size[0]
    height = visual_size[1]

    # Convert to float
    if width is not None:
        width = float(width)
    if height is not None:
        height = float(height)

    # Check non-negative
    if (width is not None and width <= 0) or (height is not None and height <= 0):
        raise ValueError(f"visual_size has to be positive; {width, height}")

    # Initiate namedtuple:
    return Visual_size(width, height)
