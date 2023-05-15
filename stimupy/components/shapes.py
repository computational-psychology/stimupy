import numpy as np

from stimupy.components import image_base
from stimupy.components.angulars import wedge
from stimupy.components.radials import annulus, disc, ring
from stimupy.utils import resolution

__all__ = [
    "rectangle",
    "triangle",
    "cross",
    "parallelogram",
    "ellipse",
    "circle",
    "wedge",
    "annulus",
    "disc",
    "ring",
]


def rectangle(
    visual_size=None,
    ppd=None,
    shape=None,
    rectangle_size=None,
    rectangle_position=None,
    intensity_rectangle=1.0,
    intensity_background=0.0,
    rotation=0.0,
):
    """Draw a rectangle

    Parameters
    ----------
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of image, in degrees visual angle
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of image, in pixels
    rectangle_size : Number, Sequence[Number, Number]
        rectangle size [height, width], in degrees visual angle
    rectangle_position : Number, Sequence[Number, Number], or None (default)
        position of the rectangle, in degrees visual angle.
        If None, rectangle will be placed in center of image.
    intensity_rectangle : float, optional
        intensity value for rectangle, by default 1.0
    intensity_background : float, optional
        intensity value of background, by default 0.0
    rotation : float, optional
        rotation (in degrees), counterclockwise, by default 0.0 (horizonal)

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for the shape (key: "rectangle_mask"),
        and additional keys containing stimulus parameters
    """
    if rectangle_size is None:
        raise ValueError("rectangle() missing argument 'rectangle_size' which is not 'None'")

    # Resolve resolutions and get distances
    base = image_base(
        visual_size=visual_size,
        ppd=ppd,
        shape=shape,
        rotation=rotation,
        origin="center",
    )
    xx = base["horizontal"]
    yy = base["vertical"]
    theta = np.deg2rad(rotation)
    rectangle_size = resolution.validate_visual_size(visual_size=rectangle_size)

    # Determine center position
    rect_posy = (base["visual_size"].height / 2) - (rectangle_size.height / 2)
    rect_posx = (base["visual_size"].width / 2) - (rectangle_size.width / 2)
    center_pos = (rect_posy, rect_posx)

    if rectangle_position is None:
        # If no position is given, place rectangle centrally
        rectangle_position = center_pos

    # Positions should always be positive
    rectangle_position = np.array(rectangle_position).clip(min=0)
    center_pos = np.array(center_pos).clip(min=0)

    # Determine shift
    rect_pos = resolution.shape_from_visual_size_ppd(rectangle_position, base["ppd"])
    center_pos = resolution.shape_from_visual_size_ppd(center_pos, base["ppd"])
    rect_shift = (np.array(rect_pos) - np.array(center_pos)).astype(int)

    # Rotate coordinate systems
    x = np.round(np.cos(theta) * xx - np.sin(theta) * yy, 8)
    y = np.round(np.sin(theta) * xx + np.cos(theta) * yy, 8)

    # Rounding for more robust behavior:
    x = np.round(x * (base["ppd"][0] * 2)) / (base["ppd"][0] * 2)
    y = np.round(y * (base["ppd"][0] * 2)) / (base["ppd"][0] * 2)

    # Draw rectangle
    img1 = np.where(x < rectangle_size.width / 2, 1, 0)
    img2 = np.where(x >= -rectangle_size.width / 2, 1, 0)
    img3 = np.where(y < rectangle_size.height / 2, 1, 0)
    img4 = np.where(y >= -rectangle_size.height / 2, 1, 0)
    img = img1 * img2 * img3 * img4

    # Shift rectangle
    img = np.roll(img, (rect_shift[0], rect_shift[1]), axis=(0, 1))

    # Does the rectangle fit?
    x1 = rectangle_size[1] / 2 * np.cos(theta)
    x2 = rectangle_size[1] / 2 * np.sin(theta)
    y1 = rectangle_size[0] / 2 * np.cos(theta)
    y2 = rectangle_size[0] / 2 * np.sin(theta)
    cy = x2 + y1 + np.abs(rect_shift[0] / base["ppd"][0])
    cy = np.floor(cy * base["ppd"][0]) / base["ppd"][0]
    cx = x1 + y2 + np.abs(rect_shift[1] / base["ppd"][1])
    cx = np.floor(cx * base["ppd"][1]) / base["ppd"][1]

    if (cy > base["visual_size"][0] / 2) or (cx > base["visual_size"][1] / 2):
        raise ValueError("stimulus does not fully fit into requested size")

    return {
        "img": img * (intensity_rectangle - intensity_background) + intensity_background,
        "rectangle_mask": img.astype(int),
        "visual_size": base["visual_size"],
        "ppd": base["ppd"],
        "shape": base["shape"],
        "rectangle_size": rectangle_size,
        "rectangle_position": rectangle_position,
        "intensity_background": intensity_background,
        "intensity_rectangle": intensity_rectangle,
        "rotation": rotation,
    }


def triangle(
    visual_size=None,
    ppd=None,
    shape=None,
    triangle_size=None,
    intensity_triangle=1.0,
    intensity_background=0.0,
    include_corners=True,
    rotation=0.0,
):
    """Draw a triangle

    Parameters
    ----------
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of image, in degrees visual angle
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of image, in pixels
    triangle_size : Number, Sequence[Number, Number]
        triangle size [height width], in degrees visual angle
    intensity_triangle : float, optional
        intensity value for triangle, by default 1.0
    intensity_background : float, optional
        intensity value of background, by default 0.0
    rotation : float, optional
        rotation (in degrees), counterclockwise, by default 0.0

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for the shape (key: "triangle_mask"),
        and additional keys containing stimulus parameters
    """
    if triangle_size is None:
        raise ValueError("triangle() missing argument 'triangle_size' which is not 'None'")

    # Resolve resolutions and get distances
    base = image_base(
        visual_size=visual_size,
        ppd=ppd,
        shape=shape,
        rotation=rotation,
        origin="center",
    )
    xx = base["horizontal"]
    yy = base["vertical"]
    triangle_size = resolution.validate_visual_size(visual_size=triangle_size)

    angle_diagonal = np.arctan(triangle_size[1] / triangle_size[0])
    angle_diagonal = np.rad2deg(angle_diagonal)
    theta = np.deg2rad(rotation + angle_diagonal)
    x = np.round(np.cos(theta) * xx - np.sin(theta) * yy, 8)

    # Split image in two parts following the diagonal
    if include_corners:
        img = np.where(x <= 0, 1, 0)
    else:
        fac = base["ppd"][0] / 2
        x = np.round(x * fac) / fac
        img = np.where(x < 0, 1, 0)

    # Create rectangular mask
    rect = rectangle(
        visual_size=visual_size,
        ppd=ppd,
        shape=shape,
        rectangle_size=triangle_size,
        rotation=rotation,
    )
    img = img * rect["rectangle_mask"]

    return {
        "img": img * (intensity_triangle - intensity_background) + intensity_background,
        "triangle_mask": img.astype(int),
        "visual_size": base["visual_size"],
        "ppd": base["ppd"],
        "shape": base["shape"],
        "triangle_size": triangle_size,
        "intensity_background": intensity_background,
        "intensity_triangle": intensity_triangle,
        "rotation": rotation,
        "include_corners": include_corners,
    }


def cross(
    visual_size=None,
    ppd=None,
    shape=None,
    cross_size=None,
    cross_thickness=None,
    cross_arm_ratios=(1.0, 1.0),
    intensity_cross=1.0,
    intensity_background=0.0,
    rotation=0.0,
):
    """Draw a cross

    Parameters
    ----------
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of image, in degrees visual angle
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of image, in pixels
    cross_size : Number, Sequence[Number, Number]
        cross size [height, width], in degrees visual angle
    cross_thickness : Number, Sequence[Number, Number]
        thickness of cross in degrees visual angle
    cross_arm_ratios : float or (float, float)
        ratio used to create arms (up-down, left-right)
    intensity_cross: float, optional
        intensity value for cross, by default 1.0
    intensity_background : float, optional
        intensity value of background, by default 0.0
    rotation : float, optional
        rotation (in degrees), counterclockwise, by default 0.0

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for the shape (key: "cross_mask"),
        and additional keys containing stimulus parameters
    """
    if cross_size is None:
        raise ValueError("cross() missing argument 'cross_size' which is not 'None'")
    if cross_thickness is None:
        raise ValueError("cross() missing argument 'cross_thickness' which is not 'None'")

    # Resolve resolution
    shape, visual_size, ppd = resolution.resolve(shape=shape, visual_size=visual_size, ppd=ppd)
    cross_size = resolution.validate_visual_size(cross_size)
    cross_thickness = resolution.validate_visual_size(cross_thickness)

    if isinstance(cross_arm_ratios, (float, int)):
        cross_arm_ratios = (cross_arm_ratios, cross_arm_ratios)

    # Determine coordinate center
    cy = visual_size.height / 2
    cx = visual_size.width / 2
    theta = np.deg2rad(rotation)

    # Calculate cross placement based on ratios of cross legs
    updown = cross_size.height - cross_thickness[0]
    down = updown / (cross_arm_ratios[0] + 1)
    up = updown - down
    leftright = cross_size.width - cross_thickness[1]
    right = leftright / (cross_arm_ratios[1] + 1)
    left = leftright - right

    posy1 = cy - cross_size[0] / 2 + (down - up) * np.cos(theta) / 2
    posx1 = cx - cross_thickness[0] / 2 + (down - up) * np.sin(theta) / 2

    posy2 = cy - cross_thickness[1] / 2 + (right - left) * np.sin(-theta) / 2
    posx2 = cx - cross_size[1] / 2 + (right - left) * np.cos(-theta) / 2

    # Create cross as two rectangles
    rect1 = rectangle(
        visual_size=visual_size,
        ppd=ppd,
        rectangle_size=(cross_size[0], cross_thickness[0]),
        rectangle_position=(posy1, posx1),
        rotation=rotation,
    )

    rect2 = rectangle(
        visual_size=visual_size,
        ppd=ppd,
        rectangle_size=(cross_thickness[1], cross_size[1]),
        rectangle_position=(posy2, posx2),
        rotation=rotation,
    )

    img = rect1["img"] + rect2["img"]
    img[img > 1] = 1

    return {
        "img": img * (intensity_cross - intensity_background) + intensity_background,
        "cross_mask": img.astype(int),
        "shape": shape,
        "visual_size": visual_size,
        "ppd": ppd,
        "cross_size": cross_size,
        "cross_arm_ratios": cross_arm_ratios,
        "cross_thickness": cross_thickness,
        "intensity_background": intensity_background,
        "intensity_cross": intensity_cross,
        "rotation": rotation,
    }


def parallelogram(
    visual_size=None,
    ppd=None,
    shape=None,
    parallelogram_size=None,
    intensity_parallelogram=1.0,
    intensity_background=0.0,
    rotation=0.0,
):
    """Draw a parallelogram

    Parameters
    ----------
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of image, in degrees visual angle
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of image, in pixels
    parallelogram_size : [Number, Number, Number], [Number, Number], Number or None (default)
        parallelogram size [height, width, depth], in degrees visual angle
    intensity_parallelogram : float, optional
        intensity value for parallelogram, by default 1.0
    intensity_background : float, optional
        intensity value of background, by default 0.0
    rotation : float, optional
        rotation (in degrees), counterclockwise, by default 0.0

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for the shape (key: "parallelogram_mask"),
        and additional keys containing stimulus parameters
    """
    if parallelogram_size is None:
        raise ValueError(
            "parallelogram() missing argument 'parallelogram_size' which is not 'None'"
        )
    if isinstance(parallelogram_size, (float, int)):
        parallelogram_size = (parallelogram_size, parallelogram_size, 0)
    if len(parallelogram_size) == 2:
        parallelogram_size = tuple(
            list(parallelogram_size)
            + [
                0,
            ]
        )

    # Resolve resolutions and get distances
    base = image_base(
        visual_size=visual_size,
        ppd=ppd,
        shape=shape,
        rotation=rotation,
        origin="center",
    )
    xx = base["horizontal"]
    yy = base["vertical"]

    # Create rectangule
    rectangle_size = (parallelogram_size[0], parallelogram_size[1] + np.abs(parallelogram_size[2]))
    rect = rectangle(
        visual_size=visual_size,
        ppd=ppd,
        shape=shape,
        rectangle_size=rectangle_size,
        rotation=rotation,
    )
    img = rect["img"]

    if parallelogram_size[2] != 0:
        if parallelogram_size[2] > 0:
            triangle_size = (parallelogram_size[0], np.abs(parallelogram_size[2]))
            rot1 = rotation
        else:
            triangle_size = (np.abs(parallelogram_size[2]), parallelogram_size[0])
            rot1 = rotation - 90

        angle_diagonal = np.arctan(triangle_size[1] / triangle_size[0])
        angle_diagonal = np.rad2deg(angle_diagonal)
        theta = np.deg2rad(rot1 + angle_diagonal)
        x = np.round(np.cos(theta) * xx - np.sin(theta) * yy, 8)

        # Shift diagonals so that resulting triangles cover corners of rectangle
        theta = np.deg2rad(rotation)
        pwidth = parallelogram_size[1] / 2 * base["ppd"][0]
        shift1 = int(np.round(pwidth) * np.sin(theta))
        shift2 = int(np.floor(pwidth) * np.cos(theta))

        # Split image in two parts following the diagonal
        tri1 = np.where(np.roll(x, (shift1, -shift2), axis=(0, 1)) < 0, 0, 1)
        tri1 = np.where(x < 0, tri1, 0)
        tri2 = np.where(np.roll(x, (-shift1, shift2), axis=(0, 1)) > 0, 0, 1)
        tri2 = np.where(x >= 0, tri2, 0)

        # Combine everything
        img = tri1 * img + tri2 * img

    return {
        "img": img * (intensity_parallelogram - intensity_background) + intensity_background,
        "parallelogram_mask": img.astype(int),
        "shape": base["shape"],
        "visual_size": base["visual_size"],
        "ppd": base["ppd"],
        "parallelogram_size": parallelogram_size,
        "intensity_background": intensity_background,
        "intensity_parallelogram": intensity_parallelogram,
        "rotation": rotation,
    }


def ellipse(
    visual_size=None,
    ppd=None,
    shape=None,
    radius=None,
    intensity_ellipse=1.0,
    intensity_background=0.0,
    rotation=0.0,
    origin="mean",
    restrict_size=True,
):
    """Draw an ellipse

    Parameters
    ----------
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of image, in degrees visual angle
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of image, in pixels
    radius : Sequence[Number, Number], Number or None (default)
        ellipse radius [ry, rx] in degrees visual angle
    intensity_ellipse : float, optional
        intensity value for ellipse, by default 1.0
    intensity_background : float, optional
        intensity value of background, by default 0.0
    rotation : float, optional
        rotation (in degrees), counterclockwise, by default 0.0
    origin : "corner", "mean" or "center"
        if "corner": set origin to upper left corner
        if "mean": set origin to hypothetical image center (default)
        if "center": set origin to real center (closest existing value to mean)
    restrict_size : Bool
        if False, allow ellipse to reach beyond image size (default: True)

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for the shape (key: "ellipse_mask"),
        and additional keys containing stimulus parameters
    """
    if radius is None:
        raise ValueError("ellipse() missing argument 'radius' which is not 'None'")

    # Resolve resolutions and get distances
    radius = resolution.validate_visual_size(visual_size=radius)
    base = image_base(
        visual_size=visual_size,
        ppd=ppd,
        shape=shape,
        rotation=rotation,
        origin=origin,
    )

    xx = base["horizontal"]
    yy = base["vertical"]

    # Rotate coordinate systems
    theta = np.deg2rad(rotation)
    x = np.round(np.cos(theta) * yy - np.sin(theta) * xx, 8)
    y = np.round(np.sin(theta) * yy + np.cos(theta) * xx, 8)

    # Draw ellipse
    arr = np.sqrt(x**2 + (y * radius[0] / radius[1]) ** 2)
    img = np.where(arr <= radius[0], 1, 0)

    # Does ellipse fit?
    x1 = radius[1] * np.cos(theta)
    x2 = radius[1] * np.sin(theta)
    y1 = radius[0] * np.cos(theta)
    y2 = radius[0] * np.sin(theta)
    cy = np.floor((x2 + y1) * base["ppd"][0]) / base["ppd"][0]
    cx = np.floor((x1 + y2) * base["ppd"][1]) / base["ppd"][1]

    if restrict_size and ((cy > base["visual_size"][0] / 2) or (cx > base["visual_size"][1] / 2)):
        raise ValueError("stimulus does not fully fit into requested size")

    return {
        "img": img * (intensity_ellipse - intensity_background) + intensity_background,
        "ellipse_mask": img.astype(int),
        "shape": base["shape"],
        "visual_size": base["visual_size"],
        "ppd": base["ppd"],
        "radius": radius,
        "intensity_background": intensity_background,
        "intensity_ellipse": intensity_ellipse,
        "rotation": rotation,
    }


def circle(
    visual_size=None,
    ppd=None,
    shape=None,
    radius=None,
    intensity_circle=1.0,
    intensity_background=0.0,
    origin="mean",
    restrict_size=True,
):
    """Draw an ellipse

    Parameters
    ----------
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of image, in degrees visual angle
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of image, in pixels
    radius : Number or None (default)
        circle radius in degrees visual angle
    intensity_circle : float, optional
        intensity value for circle, by default 1.0
    intensity_background : float, optional
        intensity value of background, by default 0.0
    origin : "corner", "mean" or "center"
        if "corner": set origin to upper left corner
        if "mean": set origin to hypothetical image center (default)
        if "center": set origin to real center (closest existing value to mean)
    restrict_size : Bool
        if False, allow circle to reach beyond image size (default: True)

    Returns
    ----------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for the shape (key: "circle_mask"),
        and additional keys containing stimulus parameters
    """
    if radius is None:
        raise ValueError("circle() missing argument 'radius' which is not 'None'")
    if not isinstance(radius, (int, float)):
        raise ValueError("radius should be a single number")

    stim = ellipse(
        visual_size=visual_size,
        ppd=ppd,
        shape=shape,
        radius=radius,
        intensity_ellipse=intensity_circle,
        intensity_background=intensity_background,
        rotation=0.0,
        origin=origin,
        restrict_size=restrict_size,
    )
    stim["circle_mask"] = stim["ellipse_mask"]
    stim["intensity_circle"] = intensity_circle
    stim.pop("ellipse_mask", "intensity_ellipse")
    return stim


def overview(**kwargs):
    """Generate example stimuli from this module

    Returns
    -------
    stims : dict
        dict with all stimuli containing individual stimulus dicts.
    """
    default_params = {
        "visual_size": (10, 10),
        "ppd": 20,
    }
    default_params.update(kwargs)

    # fmt: off
    stimuli = {
        "shapes_rectangle": rectangle(**default_params, rectangle_size=(4, 2.5)),
        "shapes_triangle": triangle(**default_params, triangle_size=(4, 2.5)),
        "shapes_cross": cross(**default_params, cross_size=(4, 2.5), cross_thickness=1, cross_arm_ratios=(1, 1)),
        "shapes_parallelogram": parallelogram(**default_params, parallelogram_size=(5.2, 3.1, 0.9)),
        "shapes_ellipse": ellipse(**default_params, radius=(4, 3)),
        "shapes_circle": circle(**default_params, radius=3),
        "shapes_disc": disc(**default_params, radius=3),
        "shapes_ring": ring(**default_params, radii=(1, 2)),
        "shapes_annulus": annulus(**default_params, radii=(1, 2)),
        "shapes_wedge": wedge(**default_params, angle=30, radius=4),}
    # fmt: on

    return stimuli


if __name__ == "__main__":
    from stimupy.utils import plot_stimuli

    stims = overview()
    plot_stimuli(stims, mask=False, save=None)
