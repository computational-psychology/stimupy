import warnings
from collections import namedtuple

Visual_size = namedtuple("Visual_size", "height width")
Shape = namedtuple("Shape", "height width")
Ppd = namedtuple("Ppd", "vertical horizontal")


class ResolutionError(ValueError):
    pass


def resolve(shape=None, visual_size=None, ppd=None):
    # TODO: make 2D
    n_unknowns = (
        (shape is None or shape == (None, None))
        + (visual_size is None or visual_size == (None, None))
        + (ppd is None or ppd == (None, None))
    )
    if n_unknowns > 1:
        raise ValueError(
            f"Too many unkowns to resolve resolution; {visual_size},{shape},{ppd}"
        )
    elif n_unknowns == 0:
        valid_resolution(shape=shape, visual_size=visual_size, ppd=ppd)
    else:  # 1 unknown
        if shape is None or shape == (None, None):
            shape = shape_from_visual_size_ppd(visual_size=visual_size, ppd=ppd)
        elif visual_size is None or visual_size == (None, None):
            visual_size = visual_size_from_shape_ppd(shape=shape, ppd=ppd)
        elif ppd is None or ppd == (None, None):
            ppd = ppd_from_shape_visual_size(shape=shape, visual_size=visual_size)

    shape = validate_shape(shape)
    ppd = validate_ppd(ppd)
    visual_size = validate_visual_size(visual_size)
    valid_resolution(shape=shape, visual_size=visual_size, ppd=ppd)

    return shape, visual_size, ppd


def valid_resolution(shape, visual_size, ppd):
    shape = validate_shape(shape)
    ppd = validate_ppd(ppd)
    visual_size = validate_visual_size(visual_size)

    # TODO: error is one input is None

    calculated = shape_from_visual_size_ppd(visual_size=visual_size, ppd=ppd)
    if calculated != shape:
        raise ResolutionError(f"Invalid resolution; {visual_size},{shape},{ppd}")


def visual_size_from_shape_ppd(shape, ppd):
    # Canonize inputs
    shape = validate_shape(shape)
    ppd = validate_ppd(ppd)

    # Define function for 1D case:
    def visual_angle_from_length_ppd_1D(length, ppd):
        if length is not None and ppd is not None:
            visual_angle = length / ppd
        else:
            visual_angle = None
        return visual_angle

    # Calculate width and height in pixels
    width = visual_angle_from_length_ppd_1D(shape.width, ppd.horizontal)
    height = visual_angle_from_length_ppd_1D(shape.height, ppd.vertical)

    # Construct Visual size NamedTuple:
    visual_size = Visual_size(width=width, height=height)

    return visual_size


def shape_from_visual_size_ppd(visual_size, ppd):
    # Canonize inputs
    visual_size = validate_visual_size(visual_size)
    ppd = validate_ppd(ppd)

    # Define function for 1D case:
    def pix_from_visual_angle_ppd_1D(visual_angle, ppd):
        if visual_angle is not None and ppd is not None:
            fpix = visual_angle * ppd
            pix = int(fpix)
            if fpix % pix:
                warnings.warn(
                    f"Rounding shape; {visual_angle} * {ppd} = {fpix} -> {pix}"
                )
        else:
            pix = None
        return pix

    # Calculate width and height in pixels
    width = pix_from_visual_angle_ppd_1D(visual_size.width, ppd.horizontal)
    height = pix_from_visual_angle_ppd_1D(visual_size.height, ppd.vertical)

    # Construct Shape NamedTuple:
    shape = Shape(width=width, height=height)

    return shape


def ppd_from_shape_visual_size(shape, visual_size):
    # Canonize inputs
    shape = validate_shape(shape)
    visual_size = validate_visual_size(visual_size)

    # Define function for 1D case:
    def ppd_from_length_visual_angle_1D(length, visual_angle):
        if visual_angle is not None and length is not None:
            ppd = length / visual_angle
        else:
            ppd = None
        return ppd

    # Calculate horizontal and vertical ppds
    horizontal = ppd_from_length_visual_angle_1D(shape.width, visual_size.width)
    vertical = ppd_from_length_visual_angle_1D(shape.height, visual_size.height)

    # Construct Ppd NamedTuple
    ppd = Ppd(horizontal=horizontal, vertical=vertical)

    return ppd


def validate_shape(shape):
    # Check if string:
    if isinstance(shape, str):
        shape = float(shape)

    # Check if sequence
    try:
        if len(shape) < 1:
            # Empty sequence
            raise ValueError(f"shape must be of at least length 1: {shape}")
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
        if len(ppd) < 1:
            # Empty sequence
            raise ValueError(f"ppd must be of at least length 1: {ppd}")
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
        if len(visual_size) < 1:
            # Empty sequence
            raise ValueError(f"visual_size must be of at least length 1: {visual_size}")
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
