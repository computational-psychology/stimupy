import itertools

import numpy as np

from stimuli.components.circular import ring
from stimuli.utils import resolution


def img_angles(visual_size=None, ppd=None, shape=None):
    """Matrix of angle (relative to center) for each pixel

    Parameters
    ----------
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of image, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of image, in pixels

    Returns
    -------
    numpy.ndarray
        array of shape, with the angle (in rad) relative to center point, for each pixel
    """

    # Resolve resolution
    shape, visual_size, ppd = resolution.resolve(shape, visual_size, ppd)

    # Image coordinates
    x = np.linspace(-visual_size.width / 2.0, visual_size.width / 2.0, shape.width)
    y = np.linspace(-visual_size.height / 2.0, visual_size.height / 2.0, shape.height)
    yy, xx = np.meshgrid(y, x)

    # Rotate image coordinates
    img_angles = -np.arctan2(xx, yy)
    img_angles %= 2 * np.pi

    return img_angles


def mask_angle(
    angles,
    visual_size=None,
    ppd=None,
    shape=None,
):
    """Mask a contiguous set of angles in image

    Parameters
    ----------
    angles : Sequence[float, float]
        lower- and upper-limit of angles to mask, in degrees
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of image, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of image, in pixels

    Returns
    -------
    dict[str, Any]
        dict with boolean mask (key: bool_mask) for pixels falling in given angle,
        and additional params
    """

    image_angles = img_angles(visual_size=visual_size, ppd=ppd, shape=shape)

    # Create mask
    inner_angle, outer_angle = np.deg2rad(angles)
    bool_mask = (image_angles > inner_angle) & (image_angles <= outer_angle)

    return {"mask": bool_mask, "visual_size": visual_size, "ppd": ppd}


def wedge(
    angle,
    radius,
    rotation=0.0,
    inner_radius=0.0,
    intensity=1.0,
    intensity_background=0.5,
    visual_size=None,
    ppd=None,
    supersampling=1,
    shape=None,
):
    """Draw a wedge, i.e., segment of a disc

    Parameters
    ----------
    angle : float
        angular-width (in degrees) of segment
    radius : float
        radius of disc, in degrees visual angle
    rotation : float, optional
        angle of rotation (in degrees) of segment,
        counterclockwise from 3 o'clock, by default 0.0
    inner_radius : float, optional
        inner radius (in degrees visual angle), to turn disc into a ring, by default 0
    intensity : float, optional
        intensity value of wedge, by default 1.0
    intensity_background : float, optional
        intensity value of background, by default 0.5
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of image, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    supersampling : int (optional)
        supersampling-factor used for anti-aliasing, by default 5.
        Warning: produces smoother circles but might introduce gradients that affect vision!
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of image, in pixels

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img")
        and additional keys containing stimulus parameters
    """

    # Convert to inner-, outer-angle
    angles = (rotation, angle + rotation)

    # Draw disc
    stim = ring(
        radii=[inner_radius, radius],
        intensity=intensity,
        intensity_background=intensity_background,
        visual_size=visual_size,
        ppd=ppd,
        shape=shape,
        supersampling=supersampling,
    )
    visual_size = stim["visual_size"]
    shape = stim["shape"]
    ppd = stim["ppd"]

    # Get mask for angles
    bool_mask = mask_angle(angles=angles, visual_size=visual_size, ppd=ppd, shape=shape)

    # Remove everything but wedge
    stim["img"] = np.where(bool_mask["mask"], stim["img"], intensity_background)

    # Output
    stim.update(bool_mask)

    return stim


def segment_masks(
    angles,
    visual_size=None,
    ppd=None,
    shape=None,
):
    """Generate mask with integer indices for angular segments

    Parameters
    ----------
    angles : Sequence[Number]
        lower- and upper-limit (in angular degrees 0-360) of each segment
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of image, in pixels
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of image, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]

    Returns
    -------
    dict[str, Any]
        dict with the mask (key: "mask")
        and additional keys containing stimulus parameters
    """

    # Resolve resolution
    shape, visual_size, ppd = resolution.resolve(shape, visual_size, ppd)

    # Convert to segment angles
    angles = np.array(angles) % 360

    # Accumulate mask
    mask = np.zeros(shape, dtype=int)
    for idx, angle in enumerate(angles[:-1]):
        bool_mask = mask_angle(
            angles=[angle, angles[idx + 1]], visual_size=visual_size, shape=shape, ppd=ppd
        )
        mask += bool_mask["mask"] * (idx + 1)

    return {"mask": mask, "visual_size": visual_size, "ppd": ppd}


def resolve_angular_params(
    shape=None,
    visual_size=None,
    ppd=None,
    frequency=None,
    n_segments=None,
    segment_width=None,
):
    """Resolve (if possible) spatial parameters for angular grating, i.e., set of segments

    Angular grating (circle segments) component takes the regular resolution parameters
    (shape, ppd, visual_size). In addition, there has to be an additional specification
    of the number of segments, and their width. This can be done in two ways:
    a segment_width (in degrees) and n_segments, and/or by specifying the spatial frequency
    of a angular grating (in cycles per degree)

    The total shape (in pixels) and visual size (in degrees) has to match the
    specification of the segments and their widths.
    Thus, not all 6 parameters have to be specified, as long as the both the resolution
    and the distribution of segments can be resolved.

    Note: all segments in a grating have the same width

    Parameters
    ----------
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of image, in pixels
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of image, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    frequency : Number, or None (default)
        spatial frequency of angular grating, in cycles per degree
    n_segments : int, or None (default)
        number of segments
    segment_width : Number, or None (default)
        width of a single segment, in degrees

    Returns
    -------
    dict[str, Any]
        dictionary with all six resolution & size parameters resolved.
    """

    # Resolve resolution
    resolution.resolve(shape=shape, visual_size=visual_size, ppd=ppd)

    # Try to resolve number and width(s) of segments
    # segment_width = degrees_per_segment = 1 / segments_per_degree = 1 / (2*frequency)
    if segment_width is not None:
        segment_per_degree = 1 / segment_width
        if frequency is not None and segment_per_degree != 2 * frequency:
            raise ValueError(
                f"segment_width {segment_width} and frequency {frequency} don't match"
            )
    elif frequency is not None:
        segment_per_degree = 2 * frequency
    else:  # both are None:
        segment_per_degree = None

    # Logic here is that segment_width expresses "degrees per segment",
    # which we can invert to segments_per_degree, analogous to ppd:
    # n_segments = segments_per_degree * n_degrees
    # is analogous to
    # pix = ppd * n_degrees
    # Thus we can resolve the number and spacing of segments also as a resolution
    try:
        n_segments, _, segment_per_degree = resolution.resolve_1D(
            length=n_segments, visual_angle=360, ppd=segment_per_degree
        )
        segment_width = 1 / segment_per_degree
        frequency = segment_per_degree / 2
    except Exception as e:
        raise Exception("Could not resolve grating frequency, segment_width, n_segments") from e

    # Determine angles
    angular_widths = itertools.repeat(segment_width, n_segments)
    angles = [0] + [*itertools.accumulate(angular_widths)]

    return {
        "shape": shape,
        "visual_size": visual_size,
        "ppd": ppd,
        "frequency": frequency,
        "segment_width": segment_width,
        "n_segments": n_segments,
        "angles": angles,
    }