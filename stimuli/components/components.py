import numpy as np

from stimuli.utils import degrees_to_pixels, pad_to_shape


__all__ = [
    "rectangle",
    "triangle",
    "cross",
    "parallelogram",
    "transparency",
]


def rectangle(
    visual_size=(4.0, 4.0),
    ppd=10,
    rectangle_size=(2.0, 2.0),
    rectangle_position=None,
    intensity_background=0.0,
    intensity_rectangle=0.5,
):
    """
    Function to create a 2d rectangle

    Parameters
    ----------
    visual_size : float or (float, float)
        size of the image in degrees visual angle
    ppd : int
        pixels per degree (visual angle)
    rectangle_size : float (float, float)
        size of the rectangle / square in degrees visual angle
    rectangle_position : float or (float, float)
        coordinates of the rectangle / square in degrees visual angle
    intensity_background : float
        intensity value for background
    intensity_rectangle : float
        intensity value for rectangle

    Returns
    -------
    A stimulus dictionary with the stimulus ['img'] and target mask ['mask']
    """

    if isinstance(visual_size, (float, int)):
        visual_size = (visual_size, visual_size)
    if isinstance(rectangle_size, (float, int)):
        rectangle_size = (rectangle_size, rectangle_size)
    
    im_height, im_width = degrees_to_pixels(visual_size, ppd)
    rect_height, rect_width = degrees_to_pixels(rectangle_size, ppd)
    
    if rectangle_position is None:
        # If not position is given, place centrally
        rect_posy = int(im_height/2 - np.ceil(rect_height/2))
        rect_posx = int(im_width/2 - np.ceil(rect_width/2))
        rectangle_position = (rect_posy/ppd, rect_posx/ppd)

    if isinstance(rectangle_position, (float, int)):
        rectangle_position = (rectangle_position, rectangle_position)
    if ((rectangle_position[0] + rectangle_size[0] > visual_size[0]) or
        (rectangle_position[1] + rectangle_size[1] > visual_size[1])):
        raise ValueError("rectangle does not fully fit into stimulus")
    rect_posy, rect_posx = degrees_to_pixels(rectangle_position, ppd)

    # Create image and add rectangle
    img = np.ones((im_height, im_width)) * intensity_background
    img[rect_posy:rect_posy+rect_height,
        rect_posx:rect_posx+rect_width] = intensity_rectangle

    # Create mask
    mask = np.zeros(img.shape)
    mask[img == intensity_rectangle] = 1

    stim = {
        "img": img,
        "mask": mask.astype(int),
        "ppd": ppd,
        "visual_size": np.array(img.shape) / ppd,
        "shape": img.shape,
        "rectangle_size": rectangle_size,
        "rectangle_position": rectangle_position,
        "intensity_background": intensity_background,
        "intensity_rectangle": intensity_rectangle,
        }
    return stim


def triangle(
    visual_size=(2.0, 2.0),
    ppd=10,
    intensity_background=0.0,
    intensity_triangle=0.5):
    """
    Function to create a 2d triangle in the lower left diagonal

    Parameters
    ----------
    visual_size : float or (float, float)
        size of the image in degrees visual angle
    ppd : int
        pixels per degree (visual angle)
    intensity_background : float
        intensity value for background
    intensity_triangle : float
        intensity value for triangle

    Returns
    -------
    A stimulus dictionary with the stimulus ['img'] and target mask ['mask']
    """
    height, width = degrees_to_pixels(visual_size, ppd)
    img = np.ones([height, width]) * intensity_background
    line1 = np.linspace(0, height - 1, np.maximum(height, width) * 2).astype(int)
    line1 = np.linspace(line1, height - 1, np.maximum(height, width) * 2).astype(int)
    line2 = np.linspace(0, width - 1, np.maximum(height, width) * 2).astype(int)
    line2 = np.repeat(np.expand_dims(line2, -1), np.maximum(height, width) * 2, 1)
    img[line1, line2] = intensity_triangle
    
    mask = np.zeros(img.shape)
    mask[line1, line2] = 1
    
    stim = {
        "img": img,
        "mask": mask.astype(int),
        "ppd": ppd,
        "visual_size": np.array(img.shape) / ppd,
        "shape": img.shape,
        "intensity_background": intensity_background,
        "intensity_triangle": intensity_triangle,
        }
    return stim


def cross(
    visual_size=(20.0, 20.0),
    ppd=10,
    cross_arm_ratios=(1., 1.),
    cross_thickness=4.0,
    intensity_background=0.0,
    intensity_cross=1.0,
):
    """
    Function to create a 2d array with a cross

    Parameters
    ----------
    visual_size : float or (float, float)
        size of the image in degrees visual angle
    ppd : int
        pixels per degree (visual angle)
    cross_arm_ratios : float or (float, float)
        ratio used to create arms (up-down, left-right)
    cross_thickness : float
        thickness of the bars in degrees visual angle
    intensity_background : float
        intensity value for background
    intensity_cross : float
        intensity value for cross

    Returns
    -------
    A stimulus dictionary with the stimulus ['img'] and target mask ['mask']
    """
    if isinstance(visual_size, (float, int)):
        visual_size = (visual_size, visual_size)
    if isinstance(cross_arm_ratios, (float, int)):
        cross_arm_ratios = (cross_arm_ratios, cross_arm_ratios)
    if not isinstance(cross_thickness, (float, int)):
        raise ValueError("cross_thickness should be a single number")

    # Calculate cross arm lengths
    height, width = degrees_to_pixels(visual_size, ppd)
    thick = np.ceil(cross_thickness * ppd)
    
    updown = int(height - thick)
    down = int(updown / (cross_arm_ratios[0] + 1))
    up = updown - down
    leftright = int(width - thick)
    right = int(leftright / (cross_arm_ratios[1] + 1))
    left = leftright - right
    cross_size = (up, down, left, right)
    
    if any(item < 1 for item in cross_size):
        raise ValueError("cross_arm_ratios too large or small")

    # Create image and add cross
    img = np.ones((height, width)) * intensity_background
    x_edge_left, x_edge_right = left, -right
    y_edge_top, y_edge_bottom = up, -down
    img[:, x_edge_left:x_edge_right] = intensity_cross
    img[y_edge_top:y_edge_bottom, :] = intensity_cross
    
    # Create mask
    mask = np.copy(img)
    mask[img==intensity_background] = 0
    mask[img==intensity_cross] = 1
    
    stim = {
        "img": img,
        "mask": mask.astype(int),
        "ppd": ppd,
        "visual_size": np.array(img.shape) / ppd,
        "shape": img.shape,
        "cross_arm_ratios": cross_arm_ratios,
        "cross_thickness": cross_thickness,
        "intensity_background": intensity_background,
        "intensity_cross": intensity_cross,
        }
    return stim


def parallelogram(
    visual_size=(3., 4.),
    ppd=10,
    parallelogram_depth=1.,
    intensity_background=0.0,
    intensity_parallelogram=0.5,
):
    """
    Function to create a 2d array with a parallelogram

    Parameters
    ----------
    visual_size : float or (float, float)
        size of the image in degrees visual angle
    ppd : int
        pixels per degree (visual angle)
    parallelogram_depth : float
        depth of parallelogram (if negative, skewed to the other side)
    intensity_background : float
        intensity value for background
    intensity_parallelogram : float
        intensity value for cross

    Returns
    -------
    A stimulus dictionary with the stimulus ['img'] and target mask ['mask']
    """
    if isinstance(visual_size, (float, int)):
        visual_size = (visual_size, visual_size)

    height, width = degrees_to_pixels(visual_size, ppd)
    depth = degrees_to_pixels(abs(parallelogram_depth), ppd)

    # Create triangle to create parallelogram
    if depth == 0.:
        img = np.ones((height, width)) * intensity_parallelogram
    else:
        triangle1 = triangle(
            visual_size=(visual_size[0], abs(parallelogram_depth)),
            ppd=ppd,
            intensity_background=0.,
            intensity_triangle=-intensity_parallelogram + intensity_background,
            )["img"]

        triangle2 = triangle(
            visual_size=(visual_size[0], abs(parallelogram_depth)),
            ppd=ppd,
            intensity_background=-intensity_parallelogram + intensity_background,
            intensity_triangle=0.,
            )["img"]

        # Create image, add rectangle and subtract triangles
        img = np.ones((height, width)) * intensity_parallelogram
        img[0:height, 0:depth] += triangle1
        img[0:height, width-depth::] += triangle2

    if parallelogram_depth < 0.:
        img = np.fliplr(img)
    
    # Create mask
    mask = np.copy(img)
    mask[img==intensity_background] = 0
    mask[img==intensity_parallelogram] = 1
    
    stim = {
        "img": img,
        "mask": mask.astype(int),
        "ppd": ppd,
        "visual_size": np.array(img.shape) / ppd,
        "shape": img.shape,
        "parallelogram_depth": parallelogram_depth,
        "intensity_background": intensity_background,
        "intensity_parallelogram": intensity_parallelogram,
        }
    return stim


def transparency(img, mask, alpha=0.5, tau=0.2):
    """Applies a transparency layer to given image at specified (mask) location

    Parameters
    ----------
    img : numpy.ndarray
        2D image array that transparency should be applied to
    mask : numpy.ndarray
        2D binary array indicating which pixels to apply transparency to
    tau : Number
        tau of transparency (i.e. value of transparent medium), default 0.5
    alpha : Number
        alpha of transparency (i.e. how transparant the medium is), default 0.2

    Returns
    -------
    numpy.ndarray
        img, with the transparency applied to the masked region
    """
    return np.where(mask, alpha * img + (1 - alpha) * tau, img)


def smooth_window(shape, plateau, min_val, max_val, width):
    """
    Return an array that smoothly falls of from max_val to min_val. Plateau
    specifies the location of max_val, width defines the width of the gradient,
    i.e. the number of pixels to reach min_val.
    TODO: only really works for unslanted rectangles, otherwise the inside of
    the plateau is not filled in!

    Parameters
    ----------
    shape : tuple of two ints
            the shape of the output array, (y,x)
    plateau : tuple of two-tuples ((y1, x1), ...)
              the corner points of the plateau, i.e the region where the output
              should be max_val. If two points are given, they are interpreted
              as the upper left and lower right corner of the plateau.
    min_val : number
              the value of the output array at all locations further than width
              from the plateau
    max_val : number
              the value of the output array at the plateau
    width : int
            the distance it takes for the gradient funcion to change from max
            to min.

    Returns
    -------
    mask : 2D array
    """
    x = np.arange(shape[1])[np.newaxis, :]
    y = np.arange(shape[0])[:, np.newaxis]
    distance = np.ones(shape) * width
    if len(plateau) == 2:
        plateau_points = (
            plateau[0],
            (plateau[0][0], plateau[1][1]),
            plateau[1],
            (plateau[1][0], plateau[0][1]),
        )
        distance[plateau[0][0] : plateau[1][0], plateau[0][1] : plateau[1][1]] = 0
    else:
        plateau_points = plateau
    for i in range(len(plateau_points)):
        p1 = plateau_points[i]
        p2 = plateau_points[(i + 1) % len(plateau_points)]
        distance = np.fmin(distance, dist_to_segment(y, x, p1, p2))
    distance = distance / width * np.pi
    mask = (np.cos(distance) + 1) / 2
    mask = mask * (max_val - min_val) + min_val

    return mask


def dist_squared(y, x, p):
    return (y - p[0]) ** 2 + (x - p[1]) ** 2


def dist_to_segment(y, x, p1, p2):  # x3,y3 is the point
    """
    Compute the distance between a point, (y,x), and a line segment between p1
    and p2.
    """
    y = np.atleast_1d(y)
    x = np.atleast_1d(x)
    sl = dist_squared(p1[0], p1[1], p2)
    if sl == 0:
        return np.sqrt(dist_squared(y, x, p1))
    t = ((y - p1[0]) * (p2[0] - p1[0]) + (x - p1[1]) * (p2[1] - p1[1])) / sl
    dist = dist_squared(y, x, (p1[0] + t * (p2[0] - p1[0]), p1[1] + t * (p2[1] - p1[1])))
    dist[t > 1] = dist_squared(y, x, p2)[t > 1]
    dist[t < 0] = dist_squared(y, x, p1)[t < 0]
    return np.sqrt(dist)


def get_circle_indices(n_numbers, grid_shape):

    height, width = grid_shape

    x = np.linspace(0, 2 * np.pi, n_numbers)

    xx = np.cos(x)
    xx_min = np.abs(xx.min())
    xx += xx_min
    xx_max = xx.max()
    xx = xx / xx_max * (width - 1)

    yy = np.sin(x)
    yy_min = np.abs(yy.min())
    yy += yy_min
    yy_max = yy.max()
    yy = yy / yy_max * (height - 1)

    return (yy, xx)


def get_circle_mask(shape, center, radius):
    """
    Get a circle shaped mask

    Parameters
    -------
    shape: (height, width) of the mask in pixels
    center: (y_center, x_center) in pixels
    radius: radius of the circle in pixels

    Returns
    -------
    mask: 2D boolean numpy array
    """
    height, width = shape
    y_c, x_c = center

    xx, yy = np.mgrid[:height, :width]
    grid_radii = (xx - x_c) ** 2 + (yy - y_c) ** 2

    circle_mask = grid_radii < (radius**2)

    return circle_mask


def get_annulus_mask(shape, center, inner_radius, outer_radius):
    """
    Get an annulus shaped mask

    Parameters
    -------
    shape: (height, width) of the mask in pixels
    radius: radius of the circle in pixels
    center: width of the annulus in pixels

    Returns
    -------
    mask: 2D boolean numpy array
    """

    mask1 = get_circle_mask(shape, center, inner_radius)
    mask2 = get_circle_mask(shape, center, outer_radius)
    mask = np.logical_xor(mask1, mask2)

    return mask
