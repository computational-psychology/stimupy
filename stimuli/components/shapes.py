import numpy as np

from stimuli.components.angular import wedge
from stimuli.components.circular import annulus, disc, ring
from stimuli.utils import resolution

__all__ = [
    "rectangle",
    "triangle",
    "cross",
    "parallelogram",
    "wedge",
    "annulus",
    "disc",
    "ring",
]


def rectangle(
    shape=None,
    visual_size=None,
    ppd=None,
    rectangle_size=None,
    rectangle_position=None,
    intensity_rectangle=1.0,
    intensity_background=0.5,
):
    """Draw a rectangle

    Parameters
    ----------
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of image, in pixels
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of image, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    rectangle_size : Number, Sequence[Number, Number]
        size of the rectangle, in degrees visual angle
    rectangle_position : Number, Sequence[Number, Number], or None (default)
        position of the rectangle, in degrees visual angle.
        If None, rectangle will be placed in center of image.
    intensity_rectangle : float, optional
        intensity value for rectangle, by default 1.0
    intensity_background : float, optional
        intensity value of background, by default 0.5

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img"), mask (key: "mask")
        and additional keys containing stimulus parameters
    """

    # Resolve resolution
    shape, visual_size, ppd = resolution.resolve(shape=shape, visual_size=visual_size, ppd=ppd)
    rectangle_size = resolution.validate_visual_size(visual_size=rectangle_size)
    rect_shape = resolution.shape_from_visual_size_ppd(visual_size=rectangle_size, ppd=ppd)

    # Determine position
    if rectangle_position is None:
        # If not position is given, place centrally
        rect_posy = (visual_size.height / 2) - (rectangle_size.height / 2)
        rect_posx = (visual_size.width / 2) - (rectangle_size.width / 2)
        rectangle_position = (rect_posy, rect_posx)

    rectangle_position = resolution.validate_visual_size(rectangle_position)
    if (rectangle_position.height + rectangle_size.height > visual_size.height) or (
        rectangle_position.width + rectangle_size.width > visual_size.width
    ):
        raise ValueError("rectangle does not fully fit into stimulus")

    rect_pos = resolution.shape_from_visual_size_ppd(visual_size=rectangle_position, ppd=ppd)

    # Create mask
    mask = np.zeros(shape)
    mask[
        rect_pos.height : (rect_pos.height + rect_shape.height),
        rect_pos.width : (rect_pos.width + rect_shape.width),
    ] = True

    # Create image
    img = np.where(mask, intensity_rectangle, intensity_background)

    return {
        "img": img,
        "mask": mask.astype(int),
        "shape": shape,
        "visual_size": visual_size,
        "ppd": ppd,
        "rectangle_size": rectangle_size,
        "rectangle_position": rectangle_position,
        "intensity_background": intensity_background,
        "intensity_rectangle": intensity_rectangle,
    }


def triangle(
    visual_size=None,
    ppd=None,
    shape=None,
    intensity_triangle=0.5,
    intensity_background=0.0,
    include_corners=True,
):
    """Draw a triangle in the lower left corner

    Parameters
    ----------
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of image, in pixels
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of image, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    intensity_rectangle : float, optional
        intensity value for triangle, by default 1.0
    intensity_background : float, optional
        intensity value of background, by default 0.5
    include_corners : bool
        if True, image corners are part of the triangle (default)

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img"), mask (key: "mask")
        and additional keys containing stimulus parameters
    """

    # Resolve resolution
    shape, visual_size, ppd = resolution.resolve(shape=shape, visual_size=visual_size, ppd=ppd)
    height, width = shape.height, shape.width

    # Mask triangle
    mask = np.zeros(shape)
    line1 = np.linspace(0, height - 1, np.maximum(height, width) * 2).astype(int)
    line1 = np.linspace(line1, height - 1, np.maximum(height, width) * 2).astype(int)
    line2 = np.linspace(0, width - 1, np.maximum(height, width) * 2).astype(int)
    line2 = np.repeat(np.expand_dims(line2, -1), np.maximum(height, width) * 2, 1)
    mask[line1, line2] = 1
    
    if not include_corners:
        mask = np.abs(np.rot90(mask, 2) - 1)

    # Draw
    img = np.where(mask, intensity_triangle, intensity_background)

    return {
        "img": img,
        "mask": mask.astype(int),
        "shape": shape,
        "visual_size": visual_size,
        "ppd": ppd,
        "intensity_background": intensity_background,
        "intensity_triangle": intensity_triangle,
    }


def cross(
    shape=None,
    visual_size=None,
    ppd=None,
    cross_thickness=4.0,
    cross_arm_ratios=(1.0, 1.0),
    intensity_cross=1.0,
    intensity_background=0.5,
):
    """Draw a cross

    Parameters
    ----------
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of image, in pixels
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of image, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    cross_thickness : float
        thickness of the bars in degrees visual angle
    cross_arm_ratios : float or (float, float)
        ratio used to create arms (up-down, left-right)
    intensity_cross: float, optional
        intensity value for cross, by default 1.0
    intensity_background : float, optional
        intensity value of background, by default 0.5

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img"), mask (key: "mask")
        and additional keys containing stimulus parameters
    """

    # Resolve resolution
    shape, visual_size, ppd = resolution.resolve(shape=shape, visual_size=visual_size, ppd=ppd)
    cross_arm_ratios = resolution.validate_visual_size(cross_arm_ratios)

    if not isinstance(cross_thickness, (float, int)):
        raise ValueError("cross_thickness should be a single number")

    # Calculate cross arm lengths
    height, width = shape.height, shape.width
    thick = resolution.pix_from_visual_angle_ppd_1D(cross_thickness, ppd=ppd.horizontal)

    updown = int(height - thick)
    down = int(updown / (cross_arm_ratios[0] + 1))
    up = updown - down
    leftright = int(width - thick)
    right = int(leftright / (cross_arm_ratios[1] + 1))
    left = leftright - right
    cross_size = (up, down, left, right)

    if any(item < 1 for item in cross_size):
        raise ValueError("cross_arm_ratios too large or small")

    # Mask cross
    mask = np.zeros(shape).astype(int)
    x_edge_left, x_edge_right = left, -right
    y_edge_top, y_edge_bottom = up, -down
    mask[:, x_edge_left:x_edge_right] = 1
    mask[y_edge_top:y_edge_bottom, :] = 1

    # Draw
    img = np.where(mask, intensity_cross, intensity_background)

    return {
        "img": img,
        "mask": mask.astype(int),
        "shape": shape,
        "visual_size": visual_size,
        "ppd": ppd,
        "cross_arm_ratios": cross_arm_ratios,
        "cross_thickness": cross_thickness,
        "intensity_background": intensity_background,
        "intensity_cross": intensity_cross,
    }


def parallelogram(
    visual_size=None,
    ppd=None,
    shape=None,
    parallelogram_depth=None,
    orientation="horizontal",
    intensity_background=1.0,
    intensity_parallelogram=0.5,
):
    """Draw a parallelogram

    Parameters
    ----------
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of image, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of image, in pixels
    parallelogram_depth : float
        depth of parallelogram (if negative, skewed to the other side)
    orientation : "vertical" or "horizontal" (default)
        along which dimension the parallelogram is skewed
    intensity_background : float, optional
        intensity value of background, by default 1.0
    intensity_parallelogram : float, optional
        intensity value for parallelogram, by default 0.5

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img"), mask (key: "mask")
        and additional keys containing stimulus parameters
    """

    # Resolve resolutions
    shape, visual_size, ppd = resolution.resolve(shape=shape, visual_size=visual_size, ppd=ppd)

    # Parallelogram is drawn as rectnagular field, with two triangles cut out
    # if orientation == horizontal, triangles are cut out left and right
    # if orientation == vertical, triangles are cut out top and bottom

    triangle_size = (visual_size.height, abs(parallelogram_depth))

    # Create shapes to create parallelogram
    mask = np.ones(shape)
    if parallelogram_depth != 0.0:
        triangle1 = triangle(
            visual_size=triangle_size,
            ppd=ppd,
            intensity_background=1,
            intensity_triangle=0,
            include_corners=False
        )["img"]
        triangle1[-1, -1] = 0
        triangle2 = np.abs(triangle1-1)

        mask[0 : shape[0], 0 : triangle1.shape[1]] = np.logical_and(
            mask[0 : shape[0], 0 : triangle1.shape[1]], triangle1
        )
        mask[0 : shape[0], (mask.shape[1] - triangle2.shape[1]) :] = np.logical_and(
            mask[0 : shape[0], (mask.shape[1] - triangle2.shape[1]) :], triangle2
        )
        
        # Rotate
        if orientation == "vertical":
            mask = np.rot90(mask)
            mask = np.fliplr(mask)

        if parallelogram_depth < 0.0:
            mask = np.fliplr(mask)

    # Create image
    img = np.where(mask, intensity_parallelogram, intensity_background)

    return {
        "img": img,
        "mask": mask.astype(int),
        "shape": shape,
        "visual_size": visual_size,
        "ppd": ppd,
        "parallelogram_depth": parallelogram_depth,
        "orientation": orientation,
        "intensity_background": intensity_background,
        "intensity_parallelogram": intensity_parallelogram,
    }
