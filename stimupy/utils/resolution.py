import copy
import warnings
from collections import namedtuple

import numpy as np

__all__ = [
    "resolve",
    "resolve_1D",
    "resolve_dict",
    "visual_angle_from_length_ppd",
    "visual_angles_from_lengths_ppd",
    "visual_size_from_shape_ppd",
    "length_from_visual_angle_ppd",
    "lengths_from_visual_angles_ppd",
    "shape_from_visual_size_ppd",
    "ppd_from_shape_visual_size",
    "ppd_from_length_visual_angle",
    "compute_ppd",
    "validate_shape",
    "validate_ppd",
    "validate_visual_size",
    "valid_1D",
    "valid_resolution",
    "valid_dict",
]

Visual_size = namedtuple("Visual_size", "height width")
Shape = namedtuple("Shape", "height width")
Ppd = namedtuple("Ppd", "vertical horizontal")


class ResolutionError(ValueError):
    pass


class TooManyUnknownsError(ValueError):
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


def resolve_1D(length=None, visual_angle=None, ppd=None, round=True):
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
        raise TooManyUnknownsError(
            f"Too many unkowns to resolve resolution; {length},{visual_angle},{ppd}"
        )
    else:  # 1 unknown, so need to resolve
        # Which unknown?
        if length is None:
            if round:
                visual_angle_old = np.round(copy.deepcopy(visual_angle), 10)
                visual_angle = np.floor(np.round(visual_angle * ppd, 10)) / ppd
                if visual_angle_old != visual_angle:
                    warnings.warn(
                        f"Rounding visual angle because of ppd; {visual_angle_old} ->"
                        f" {visual_angle}"
                    )
            length = length_from_visual_angle_ppd(visual_angle=visual_angle, ppd=ppd, round=round)
        elif visual_angle is None:
            visual_angle = visual_angle_from_length_ppd(length=length, ppd=ppd)
        elif ppd is None:
            ppd = ppd_from_length_visual_angle(length=length, visual_angle=visual_angle)

    return length, visual_angle, ppd


def resolve_dict(dct):
    """Resolves the full resolution ("shape", "ppd", "visual_size"), for 2
    givens and 1 unknown in the input dictionary

    A resolution consists of a visual size in degrees, a shape in pixels,
    and specification of the number of pixels per degree.
    Since there is a strict geometric relation between these,
    shape = visual_size * ppd,
    if two are given, the third can be calculated using this function.

    This function resolves the resolution in both dimensions.

    Parameters
    ----------
    dct : dict
        dictionary with at least two out the three keys: "shape", "ppd", "visual_size"

    Returns
    -------
    Resolved dict

    See also
    ---------
    stimupy.utils.resolution
    """

    # Resolve
    ppd = dct["ppd"] if "ppd" in dct.keys() else None
    shape = dct["shape"] if "shape" in dct.keys() else None
    visual_size = dct["visual_size"] if "visual_size" in dct.keys() else None
    shape, visual_size, ppd = resolve(shape=shape, visual_size=visual_size, ppd=ppd)

    # Update dict
    dct["shape"] = shape
    dct["visual_size"] = visual_size
    dct["ppd"] = ppd
    return


def visual_size_to_axes(visual_size, shape, origin="mean"):
    """Generate axes from visual size, shape and origin

    Parameters
    ----------
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] in pixels
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] in degrees
    origin : "corner", "mean" or "center"
        if "corner": set origin to upper left corner
        if "mean": set origin to hypothetical image center (default)
        if "center": set origin to real center (closest existing value to mean)

    Returns
    -------
    (x, y):
        x and y axes, linearly spacing visual size in intervals defined by shape,
        and with the origin set in the right place.
    """

    # Validate params
    visual_size = validate_visual_size(visual_size=visual_size)
    shape = validate_shape(shape)

    # Set origin
    if origin == "corner":
        x = np.linspace(0, visual_size.width, shape.width)
        y = np.linspace(0, visual_size.height, shape.height)
    elif origin == "mean":
        vrange = (visual_size.height / 2, visual_size.width / 2)
        x = np.linspace(-vrange[1], vrange[1], shape.width)
        y = np.linspace(-vrange[0], vrange[0], shape.height)
    elif origin == "center":
        vrange = (visual_size.height / 2, visual_size.width / 2)
        x = np.linspace(-vrange[1], vrange[1], shape.width, endpoint=False)
        y = np.linspace(-vrange[0], vrange[0], shape.height, endpoint=False)
    else:
        raise ValueError('origin can only be be "corner", "mean" or "center"')

    return x, y


#############################
#    Resolve components     #
#############################
def visual_angle_from_length_ppd(length, ppd):
    """Calculate visual angle (degrees) from length (pixels) and pixels-per-degree

    Parameters
    ----------
    length : int or None
        length in pixels
    ppd : int or None
        pixels per degree

    Returns
    -------
    Length (pixels) translated to visual angle (degrees)
    """
    if length is not None and ppd is not None:
        visual_angle = length / ppd
    else:
        visual_angle = None
    return visual_angle


def visual_angles_from_lengths_ppd(lengths, ppd):
    """Calculate visual sizes (degrees) from given shapes (pixels) and pixels-per-degree

    Parameters
    ----------
    lengths : Sequence[int, int, ...] or None
        list of lengths
    ppd : int or None
        pixels per degree

    Returns
    -------
    List with lengths (pixels) translated to visual angles (degrees)
    """
    if isinstance(lengths, (int, float)):
        lengths = [
            lengths,
        ]

    if lengths is not None and ppd is not None:
        visual_angles = []
        for length in lengths:
            visual_angles.append(visual_angle_from_length_ppd(length, ppd))
    else:
        visual_angles = None

    if len(visual_angles) == 1:
        visual_angles = visual_angles[0]
    return visual_angles


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
    width = visual_angle_from_length_ppd(shape.width, ppd.horizontal)
    height = visual_angle_from_length_ppd(shape.height, ppd.vertical)

    # Construct Visual size NamedTuple:
    visual_size = Visual_size(width=width, height=height)

    return visual_size


def length_from_visual_angle_ppd(visual_angle, ppd, round=True):
    """Calculate length (pixels) from visual angle (degrees) and pixels-per-degree

    Parameters
    ----------
    visual_angle : float or None
        visual angle in degrees
    ppd : int or None
        pixels per degree
    round : bool
        if True, round output length to full pixels

    Returns
    -------
    visual angle (degrees) translated to length (pixels)
    """
    if visual_angle is not None and ppd is not None:
        fpix = np.round(visual_angle * ppd, 10)

        if round:
            pix = int(fpix)
            if fpix > 0 and fpix % pix:
                warnings.warn(f"Rounding shape; {visual_angle} * {ppd} = {fpix} -> {pix}")
        else:
            pix = float(fpix)
    else:
        pix = None
    return pix


def lengths_from_visual_angles_ppd(visual_angles, ppd, round=True):
    """Calculate lengths (pixels) from visual angles (degrees) and pixels-per-degree

    Parameters
    ----------
    visual_angles : Sequence[float, float, ...] or None
        list of visual angles
    ppd : int or None
        pixels per degree
    round : bool
        if True, round output length to full pixels

    Returns
    -------
    List with visual angles (degrees) translated to lengths (pixels)
    """
    if isinstance(visual_angles, (int, float, np.int64)):
        visual_angles = [
            visual_angles,
        ]
    if isinstance(ppd, (list, tuple)):
        raise ValueError("ppd should be a single number")

    if visual_angles is not None and ppd is not None:
        lengths = []
        for angle in visual_angles:
            lengths.append(length_from_visual_angle_ppd(angle, ppd, round=round))
    else:
        lengths = None

    if len(lengths) == 1:
        lengths = lengths[0]
    return lengths


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
    width = length_from_visual_angle_ppd(visual_size.width, ppd.horizontal)
    height = length_from_visual_angle_ppd(visual_size.height, ppd.vertical)

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
    horizontal = ppd_from_length_visual_angle(shape.width, visual_size.width)
    vertical = ppd_from_length_visual_angle(shape.height, visual_size.height)

    # Construct Ppd NamedTuple
    ppd = Ppd(horizontal=horizontal, vertical=vertical)

    return ppd


def ppd_from_length_visual_angle(length, visual_angle):
    """Calculate pixels-per-degree from length (pixels) and visual angle (degrees)

    Parameters
    ----------
    length : int or None
        length in pixels
    visual_angle : float or None
        visual angle in degrees

    Returns
    -------
    visual angle (degrees) translated to length (pixels)
    """
    if visual_angle is not None and length is not None:
        ppd = length / visual_angle
    else:
        ppd = None
    return ppd


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
            raise TypeError(f"shape must be of at least length 1: {shape}")
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
            raise TypeError(f"ppd must be of at least length 1: {ppd}")
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
            raise TypeError(f"visual_size must be of at least length 1: {visual_size}")
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
    if (width is not None and width < 0) or (height is not None and height < 0):
        raise ValueError(f"visual_size has to be nonnegative; {width, height}")

    # Initiate namedtuple:
    return Visual_size(height=height, width=width)


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
    calculated = length_from_visual_angle_ppd(visual_angle=visual_angle, ppd=ppd)
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


def valid_dict(dct):
    """Asserts that the combined specification of resolution in dict is geometrically valid.

    Asserts the combined specification of shape (in pixels), visual_size (deg) and ppd.
    If this makes sense, i.e. (roughly), int(visual_size * ppd) == shape,
    this function passes without output.
    If the specification does not make sense, raises a ResolutionError.

    Note that the resolution specification has to be fully resolved,
    i.e., none of the parameters can be/contain None

    Parameters
    ----------
    dct : dict
        dictionary with at least the keys "shape", "ppd", "visual_size"

    Raises
    ------
    ResolutionError
        if resolution specification is invalid,
        i.e. (roughly), if int(visual_size * ppd) != shape
    """
    ppd = dct["ppd"] if "ppd" in dct.keys() else None
    shape = dct["shape"] if "shape" in dct.keys() else None
    visual_size = dct["visual_size"] if "visual_size" in dct.keys() else None

    # Assert that resolution is valid
    valid_resolution(shape=shape, visual_size=visual_size, ppd=ppd)
