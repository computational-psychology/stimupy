import warnings
from collections import namedtuple

import numpy as np

Visual_size = namedtuple("Visual_size", "height width")
Shape = namedtuple("Shape", "height width")
Ppd = namedtuple("Ppd", "vertical horizontal")


class ResolutionError(ValueError):
    pass


def resolve(shape=None, visual_size=None, ppd=None):
    """Resolves the full resolution, for 2 givens and 1 unknown

    A resolution consists of a visual size in degrees, a shape in pixels,
    and specification of the number of pixels per degree.
    Since there is a strict geometric relation between these,
    shape = visual_size * ppd,
    if two are given, the third can be calculated using this function.

    This function resolves the resolution in both dimensions.


    Parameters
    ----------
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] in pixels
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]

    Returns
    -------
    Shape NamedTuple, with two attributes:
        .height: int, height in pixels
        .width: int, width in pixels
        See validate_shape
    Visual_size NamedTuple, with two attributes:
        .height: float, height in degrees visual angle
        .width: float, width in degrees visual angle
        See validate_visual_size
    ppd NamedTuple, with two attributes:
        .vertical: int, vertical pixels per degree (ppd)
        .horizontal: int, horizontal pixels per degree (ppd)
        see validate_ppd
    """

    # Canonize inputs
    ppd = validate_ppd(ppd)
    visual_size = validate_visual_size(visual_size)
    shape = validate_shape(shape)

    # Vertical
    height, visual_height, ppd_vertical = resolve_1D(
        length=shape.height, visual_angle=visual_size.height, ppd=ppd.vertical
    )

    # Horizontal
    width, visual_width, ppd_horizontal = resolve_1D(
        length=shape.width, visual_angle=visual_size.width, ppd=ppd.horizontal
    )

    # Check & canonize outputs
    shape = validate_shape((height, width))
    ppd = validate_ppd((ppd_vertical, ppd_horizontal))
    visual_size = validate_visual_size((visual_height, visual_width))

    # Assert that resolved resolution is valid
    valid_resolution(shape=shape, visual_size=visual_size, ppd=ppd)

    return shape, visual_size, ppd


def resolve_1D(length=None, visual_angle=None, ppd=None):
    """Resolves the full resolution, for 2 givens and 1 unknown

    A resolution consists of a visual size in degrees, a shape in pixels,
    and specification of the number of pixels per degree.
    Since there is a strict geometric relation between these,
    shape = visual_size * ppd,
    if two are given, the third can be calculated using this function.

    This function resolves the resolution in a single dimension.


    Parameters
    ----------
    length : Number, length in pixels, or None (default)
    visual_angle : Number, length in degrees, or None (default)
    ppd : Number, pixels per degree, or None (default)

    Returns
    -------
    length : int, length in pixels
    visual_angle : float, length in degrees
    ppd : float, pixels per degree
    """

    # How many unknowns passed in?
    n_unknowns = (length is None) + (visual_angle is None) + (ppd is None)

    # Triage based on number of unknowns
    if n_unknowns > 1:  # More than 1 unknown we cannot resolve
        raise ValueError(f"Too many unkowns to resolve resolution; {length},{visual_angle},{ppd}")
    else:  # 1 unknown, so need to resolve
        # Which unknown?
        if length is None:
            length = pix_from_visual_angle_ppd_1D(visual_angle=visual_angle, ppd=ppd)
        elif visual_angle is None:
            visual_angle = visual_angle_from_length_ppd_1D(length=length, ppd=ppd)
        elif ppd is None:
            ppd = ppd_from_length_visual_angle_1D(length=length, visual_angle=visual_angle)

    return length, visual_angle, ppd


def valid_1D(length, visual_angle, ppd):
    """Asserts that the combined specification of resolution is geometrically valid.

    Asserts the combined specification of shape (in pixels), visual_size (deg) and ppd.
    If this makes sense, i.e. (roughly), int(visual_size * ppd) == shape,
    this function passes without output.
    If the specification does not make sense, raises a ResolutionError.

    Note that the resolution specification has to be fully resolved,
    i.e., none of the parameters can be None

    Parameters
    ----------
    length : int, length in pixels
    visual_angle : float, size in degrees
    ppd : int, resolution in pixels-per-degree

    Raises
    ------
    ResolutionError
        if resolution specification is invalid,
        i.e. (roughly), if int(visual_angle * ppd) != length
    """

    # Check by calculating one component
    calculated = pix_from_visual_angle_ppd_1D(visual_angle=visual_angle, ppd=ppd)
    if calculated != length:
        raise ResolutionError(f"Invalid resolution; {visual_angle},{length},{ppd}")


def valid_resolution(shape, visual_size, ppd):
    """Asserts that the combined specification of resolution is geometrically valid.

    Asserts the combined specification of shape (in pixels), visual_size (deg) and ppd.
    If this makes sense, i.e. (roughly), int(visual_size * ppd) == shape,
    this function passes without output.
    If the specification does not make sense, raises a ResolutionError.

    Note that the resolution specification has to be fully resolved,
    i.e., none of the parameters can be/contain None

    Parameters
    ----------
    shape : 2-tuple (height, width), or something that can be cast (see validate_shape)
    visual_size : 2-tuple (height, width), or something that can be cast (see validate_visual_size)
    ppd : 2-tuple (vertical, horizontal), or something that can be cast (see validate_ppd)

    Raises
    ------
    ResolutionError
        if resolution specification is invalid,
        i.e. (roughly), if int(visual_size * ppd) != shape
    """

    # Canonize inputs
    shape = validate_shape(shape)
    ppd = validate_ppd(ppd)
    visual_size = validate_visual_size(visual_size)

    # Check by calculating one component
    calculated = shape_from_visual_size_ppd(visual_size=visual_size, ppd=ppd)
    if calculated != shape:
        raise ResolutionError(f"Invalid resolution; {visual_size},{shape},{ppd}")


#############################
#    Resolve components     #
#############################
def visual_angle_from_length_ppd_1D(length, ppd):
    if length is not None and ppd is not None:
        visual_angle = length / ppd
    else:
        visual_angle = None
    return visual_angle


def visual_size_from_shape_ppd(shape, ppd):
    """Calculate visual size (degrees) from given shape (pixels) and pixels-per-degree

    Parameters
    ----------
    shape : Sequence[int, int]; or int, or None
        each element has to be of type that can be cast to int, or None.
        See validate_shape
    ppd : Sequence[int, int]; or int, or None
        each element has to be of type that can be cast to int, or None.
        See validate_ppd

    Returns
    -------
    Visual_size NamedTuple, with two attributes:
        .height: float, height in degrees visual angle
        .width: float, width in degrees visual angle
        See validate_visual_size
    """

    # Canonize inputs
    shape = validate_shape(shape)
    ppd = validate_ppd(ppd)

    # Calculate width and height in pixels
    width = visual_angle_from_length_ppd_1D(shape.width, ppd.horizontal)
    height = visual_angle_from_length_ppd_1D(shape.height, ppd.vertical)

    # Construct Visual size NamedTuple:
    visual_size = Visual_size(width=width, height=height)

    return visual_size


def pix_from_visual_angle_ppd_1D(visual_angle, ppd):
    if visual_angle is not None and ppd is not None:
        fpix = visual_angle * ppd
        pix = int(fpix)
        if fpix % pix:
            warnings.warn(f"Rounding shape; {visual_angle} * {ppd} = {fpix} -> {pix}")
    else:
        pix = None
    return pix


def shape_from_visual_size_ppd(visual_size, ppd):
    """Calculate shape (pixels) from given visual size (degrees) and pixels-per-degree

    Parameters
    ----------
    visual_size : Sequence[Number, Number]; or Number; or None
        each element has to be of type that can be cast to float, or None.
    ppd : Sequence[int, int]; or int, or None
        each element has to be of type that can be cast to int, or None.
        See validate_ppd

    Returns
    -------
    Shape NamedTuple, with two attributes:
        .height: int, height in pixels
        .width: int, width in pixels
        See validate_shape
    """

    # Canonize inputs
    visual_size = validate_visual_size(visual_size)
    ppd = validate_ppd(ppd)

    # Calculate width and height in pixels
    width = pix_from_visual_angle_ppd_1D(visual_size.width, ppd.horizontal)
    height = pix_from_visual_angle_ppd_1D(visual_size.height, ppd.vertical)

    # Construct Shape NamedTuple:
    shape = Shape(width=width, height=height)

    return shape


def ppd_from_shape_visual_size(shape, visual_size):
    """Calculate resolution (ppd) from given shape (pixels) and visual size (degrees)

    Parameters
    ----------
    shape : Sequence[int, int]; or int, or None
        each element has to be of type that can be cast to int, or None.
        See validate_shape
    visual_size : Sequence[Number, Number]; or Number; or None
        each element has to be of type that can be cast to float, or None.
        See validate_visual_size

    Returns
    -------
    ppd NamedTuple, with two attributes:
        .vertical: int, vertical pixels per degree (ppd)
        .horizontal: int, horizontal pixels per degree (ppd)
        see validate_ppd
    """

    # Canonize inputs
    shape = validate_shape(shape)
    visual_size = validate_visual_size(visual_size)

    # Calculate horizontal and vertical ppds
    horizontal = ppd_from_length_visual_angle_1D(shape.width, visual_size.width)
    vertical = ppd_from_length_visual_angle_1D(shape.height, visual_size.height)

    # Construct Ppd NamedTuple
    ppd = Ppd(horizontal=horizontal, vertical=vertical)

    return ppd


def ppd_from_length_visual_angle_1D(length, visual_angle):
    if visual_angle is not None and length is not None:
        ppd = length / visual_angle
    else:
        ppd = None
    return ppd


#############################
#    Validate components    #
#############################
def validate_shape(shape):
    """Put specification of shape (in pixels) in canonical form, if possible

    Parameters
    ----------
    shape : Sequence of length 1 or 2; or None
        if 2 elements: interpret as (height, width)
        if 1 element: use as both height and width
        if None: return (None, None)
        each element has to be of type that can be cast to int, or None.

    Returns
    -------
    Shape NamedTuple, with two attributes:
        .height: int, height in pixels
        .width: int, width in pixels

    Raises
    ------
    ValueError
        if input does not have at least 1 element
    TypeError
        if input is not a Sequence(int, int) and cannot be cast to one
    ValueError
        if input has more than 2 elements
    """

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

    # Convert to int
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
    """Put specification of ppd in canonical form, if possible

    Parameters
    ----------
    ppd : Sequence of length 1 or 2; or None
        if 2 elements: interpret as (vertical, horizontal)
        if 1 element: use as both vertical and horizontal
        if None: return (None, None)
        each element has to be of type that can be cast to int, or None.

    Returns
    -------
    ppd NamedTuple, with two attributes:
        .vertical: int, vertical pixels per degree (ppd)
        .horizontal: int, horizontal pixels per degree (ppd)

    Raises
    ------
    ValueError
        if input does not have at least 1 element
    TypeError
        if input is not a Sequence(int, int) and cannot be cast to one
    ValueError
        if input has more than 2 elements
    """

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

    # Convert to float
    if horizontal is not None:
        horizontal = float(horizontal)
    if vertical is not None:
        vertical = float(vertical)

    # Check non-negative
    if (horizontal is not None and horizontal <= 0) or (vertical is not None and vertical <= 0):
        raise ValueError(f"ppd has to be positive; {horizontal, vertical}")

    # Initiate namedtuple:
    return Ppd(horizontal=horizontal, vertical=vertical)


def validate_visual_size(visual_size):
    """Put specification of visual size in canonical form, if possible

    Parameters
    ----------
    visual_size : Sequence of length 1 or 2; or None
        if 2 elements: interpret as (height, width)
        if 1 element: use as both height and width
        if None: return (None, None)
        each element has to be of type that can be cast to float, or None.

    Returns
    -------
    Visual_size NamedTuple, with two attributes:
        .height: float, height in degrees visual angle
        .width: float, width in degrees visual angle

    Raises
    ------
    ValueError
        if input does not have at least 1 element
    TypeError
        if input is not a Sequence(float, float) and cannot be cast to one
    ValueError
        if input has more than 2 elements
    """

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
        raise TypeError(f"visual_size must be of length 1 or 2, not greater: {visual_size}")

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


def degrees_to_pixels(degrees, ppd):
    """
    convert degrees of visual angle to pixels, given the number of pixels in
    1deg of visual angle.

    Parameters
    ----------
    degrees : number, tuple, list or a ndarray
              the degree values to be converted.
    ppd : number
          the number of pixels in the central 1 degree of visual angle.

    Returns
    -------
    pixels : number or ndarray
    """
    degrees = np.array(degrees)
    return (np.round(degrees * ppd)).astype(int)

    # This is the 'super correct' conversion, but it makes very little difference in practice
    # return (np.tan(np.radians(degrees / 2.)) / np.tan(np.radians(.5)) * ppd).astype(int)


def compute_ppd(screen_size, resolution, distance):
    """
    Compute the pixels per degree, i.e. the number of pixels in the central
    one degree of visual angle, in a presentation setup.

    Parameters
    ----------
    screen_size : scalar
                  the size of the presentation screen, in whatever unti you
                  prefer.
    resolution : scalar
                 the sceen resolution in the same direction that screen size
                 was measured in.
    distance : scalar
               the distance between the observer and the screen, in the same
               unit as screen_size.
    Returns
    -------
    ppd : number
          the number of pixels in one degree of visual angle.
    """

    ppmm = resolution / screen_size
    mmpd = 2 * np.tan(np.radians(0.5)) * distance
    return ppmm * mmpd
