from collections import namedtuple

Visual_size = namedtuple("Visual_size", "height width")
Shape = namedtuple("Shape", "height width")
Ppd = namedtuple("Ppd", "vertical horizontal")


def visual_size_from_shape_ppd(shape, ppd):
    shape = validate_shape(shape)
    ppd = validate_ppd(ppd)

    # Calculate width and height in pixels
    if shape.width is not None and ppd.horizontal is not None:
        width = shape.width / ppd.horizontal
    else:
        width = None

    if shape.height is not None and ppd.vertical is not None:
        height = shape.height / ppd.vertical
    else:
        height = None

    # Construct shape:
    visual_size = Visual_size(width=width, height=height)

    return visual_size


def shape_from_visual_size_ppd(visual_size, ppd):
    visual_size = validate_visual_size(visual_size)
    ppd = validate_ppd(ppd)

    # Calculate width and height in pixels
    if visual_size.width is not None and ppd.horizontal is not None:
        width = visual_size.width * ppd.horizontal
        # TODO: warning rounding?
    else:
        width = None

    if visual_size.height is not None and ppd.vertical is not None:
        height = visual_size.height * ppd.vertical
        # TODO: warning rounding?
    else:
        height = None

    # Construct shape:
    shape = Shape(width=width, height=height)

    return shape


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
    width = shape[1]
    height = shape[0]

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
    return Shape(height=height, width=width)


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
    horizontal = ppd[1]
    vertical = ppd[0]

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
    return Ppd(horizontal=horizontal, vertical=vertical)


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
    width = visual_size[1]
    height = visual_size[0]

    # Convert to float
    if width is not None:
        width = float(width)
    if height is not None:
        height = float(height)

    # Check non-negative
    if (width is not None and width <= 0) or (height is not None and height <= 0):
        raise ValueError(f"visual_size has to be positive; {width, height}")

    # Initiate namedtuple:
    return Visual_size(height=height, width=width)
