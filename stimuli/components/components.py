import numpy as np

from stimuli.utils import degrees_to_pixels, resize_array


def rectangle(
    ppd=10,
    im_size=(4.0, 4.0),
    rect_size=(2.0, 2.0),
    rect_pos=(1.0, 1.0),
    intensity_background=0.0,
    intensity_rectangle=0.5,
):
    """
    Function to create a 2d array with a rectangle

    Parameters
    ----------
    ppd : int
        pixels per degree (visual angle)
    im_size : float or (float, float)
        size of the image in degrees visual angle
    rect_size : float (float, float)
        size of the square in degrees visual angle
    rect_pos : float or (float, float)
        coordinates of the square in degrees visual angle
    intensity_background : float
        intensity value for background
    intensity_rectangle : float
        intensity value for rectangle

    Returns
    -------
    A 2d-array with a rectangle
    """
    if isinstance(im_size, (float, int)):
        im_size = (im_size, im_size)
    if isinstance(rect_size, (float, int)):
        rect_size = (rect_size, rect_size)
    if isinstance(rect_pos, (float, int)):
        rect_pos = (rect_pos, rect_pos)
    if rect_pos[0] + rect_size[0] > im_size[0] or rect_pos[1] + rect_size[1] > im_size[1]:
        raise ValueError("rectangle does not fully fit into stimulus")

    im_height, im_width = degrees_to_pixels(im_size, ppd)
    rect_height, rect_width = degrees_to_pixels(rect_size, ppd)
    rect_posy, rect_posx = degrees_to_pixels(rect_pos, ppd)

    # Create image and add square
    img = np.ones((im_height, im_width)) * intensity_background
    target = np.ones((rect_height, rect_width)) * intensity_rectangle
    img[rect_posy : rect_posy + rect_height, rect_posx : rect_posx + rect_width] = target
    return img


def triangle(ppd=10, target_size=(2.0, 2.0), intensity_background=0.0, intensity_triangle=0.5):
    """
    Function to create a 2d array with a triangle in the lower left diagonal

    Parameters
    ----------
    ppd : int
        pixels per degree (visual angle)
    target_size : (float, float)
        size of the target in degrees visual angle
    intensity_background : float
        intensity value for background
    intensity_triangle : float
        intensity value for triangle

    Returns
    -------
    A 2d-array with a triangle
    """
    target_y_px, target_x_px = degrees_to_pixels(target_size, ppd)
    img = np.ones([target_y_px, target_x_px]) * intensity_background
    line1 = np.linspace(0, target_y_px - 1, np.maximum(target_y_px, target_x_px) * 2).astype(int)
    line1 = np.linspace(line1, target_y_px - 1, np.maximum(target_y_px, target_x_px) * 2).astype(
        int
    )
    line2 = np.linspace(0, target_x_px - 1, np.maximum(target_y_px, target_x_px) * 2).astype(int)
    line2 = np.repeat(np.expand_dims(line2, -1), np.maximum(target_y_px, target_x_px) * 2, 1)
    img[line1, line2] = intensity_triangle
    return img


def cross(
    ppd=10,
    cross_size=(8.0, 8.0, 8.0, 8.0),
    cross_thickness=4.0,
    intensity_background=0.0,
    intensity_cross=1.0,
):
    """
    Function to create a 2d array with a cross

    Parameters
    ----------
    ppd : int
        pixels per degree (visual angle)
    cross_size : (float, float, float, float)
        size of the cross' arms in degrees visual angle in form (top, bottom, left, right)
    cross_thickness : float
        width of the cross bars in degrees visual angle
    intensity_background : float
        intensity value for background
    intensity_cross : float
        intensity value for cross

    Returns
    -------
    A 2d-array with a cross
    """
    if isinstance(cross_size, (float, int)):
        cross_size = (cross_size, cross_size, cross_size, cross_size)
    if len(cross_size) == 2:
        cross_size = (cross_size[0], cross_size[0], cross_size[1], cross_size[1])
    if len(cross_size) != 4:
        raise ValueError("cross_size should be a single number, or a tuple of two or four")
    if not isinstance(cross_thickness, (float, int)):
        raise ValueError("cross_thickness should be a single number")

    (cross_top, cross_bottom, cross_left, cross_right) = degrees_to_pixels(cross_size, ppd)
    cross_thickness = degrees_to_pixels(cross_thickness, ppd)
    width = cross_left + cross_thickness + cross_right
    height = cross_top + cross_thickness + cross_bottom

    # Create image and add cross
    img = np.ones((height, width)) * intensity_background
    x_edge_left, x_edge_right = cross_left, -cross_right
    y_edge_top, y_edge_bottom = cross_top, -cross_bottom
    img[:, x_edge_left:x_edge_right] = intensity_cross
    img[y_edge_top:y_edge_bottom, :] = intensity_cross
    return img


def parallelogram(ppd=10, para_size=(2.0, 3.0, -1.0), intensity_background=0.0, vpara=0.5):
    para_height, para_width, para_depth = degrees_to_pixels(para_size, ppd)
    para_depth = np.abs(para_depth)

    # Create triangle to create parallelogram
    if para_depth == 0.0:
        img = np.ones((para_height, para_width)) * vpara
    else:
        tri1 = triangle(
            ppd, (para_size[0], np.abs(para_size[2])), 0.0, -vpara + intensity_background
        )
        tri2 = triangle(
            ppd, (para_size[0], np.abs(para_size[2])), -vpara + intensity_background, 0.0
        )

        # Create image, add rectangle and subtract triangles
        img = np.ones((para_height, para_width + para_depth)) * vpara
        img[0:para_height, 0:para_depth] += tri1
        img[0:para_height, para_width::] += tri2

    if para_size[2] < 0.0:
        img = np.fliplr(img)
    return img


def square_wave(
    shape=(10, 10),
    ppd=10,
    frequency=1,
    intensity_bars=(0.0, 1.0),
    period="ignore",
):
    """
    Create a horizontal square wave of given spatial frequency.

    Parameters
    ----------
    shape : (float, float)
        The shape of the stimulus in degrees of visual angle. (y,x)
    ppd : int
        pixels per degree (visual angle)
    intensity_bars : (float, float)
        intensity values for bars
    frequency : float
        the spatial frequency of the wave in cycles per degree
    period : string in ['ignore', 'full', 'half']
        specifies if the period of the wave is considered for stimulus dimensions.
            'ignore' simply converts degrees to pixels
            'full' rounds down to guarantee a full period
            'half' adds a half period to the size 'full' would yield.
        Default is 'ignore'.

    Returns
    -------
    A 2d-array with a square-wave grating
    """

    if period not in ["ignore", "full", "half"]:
        raise TypeError("period not understood: %s" % period)
    if frequency > ppd / 2:
        raise ValueError("The frequency is limited to ppd/2.")

    height, width = degrees_to_pixels(shape, ppd)
    pixels_per_cycle = degrees_to_pixels(1.0 / (frequency * 2), ppd) * 2
    frequency_used = 1.0 / pixels_per_cycle * ppd
    if degrees_to_pixels(1.0 / frequency, ppd) % 2 != 0:
        print(
            "Warning: Square-wave frequency changed from %f to %f ensure an even-numbered cycle"
            " width!" % (frequency, frequency_used)
        )

    if period == "full":
        width = (width // pixels_per_cycle) * pixels_per_cycle
    elif period == "half":
        width = (width // pixels_per_cycle) * pixels_per_cycle + pixels_per_cycle / 2
    width = int(width)

    stim = np.ones((height, width)) * intensity_bars[1]

    index = [
        i + j
        for i in range(pixels_per_cycle // 2)
        for j in range(0, width, pixels_per_cycle)
        if i + j < width
    ]
    stim[:, index] = intensity_bars[0]
    return stim


def disc_and_rings(
    ppd=20,
    radii=(3, 6, 9),
    intensity_background=0.0,
    intensity_discs=(1.0, 0.0, 1.0),
    ssf=5,
):
    """
    Create a central disc with rings

    Parameters
    ----------
    ppd : int
        pixels per degree (visual angle)
    radii : tuple of floats
        radii of disc in degree visual angle
    intensity_background : float
        intensity value for background
    intensity_discs : tuple of floats
        intensity values for discs
    ssf : int (optional)
          the supersampling-factor used for anti-aliasing. Default is 5.

    Returns
    -------
    A 2d-array with a disc
    """
    radii_px = degrees_to_pixels(radii, ppd) * ssf

    # create stimulus at 5 times size to allow for supersampling antialiasing
    img = np.ones([radii_px.max() * 2, radii_px.max() * 2]) * intensity_background

    # compute distance from center of array for every point, cap at 1.0
    x = np.linspace(-img.shape[1] / 2.0, img.shape[1] / 2.0, img.shape[1])
    y = np.linspace(-img.shape[0] / 2.0, img.shape[0] / 2.0, img.shape[0])
    dist = np.sqrt(x[np.newaxis, :] ** 2 + y[:, np.newaxis] ** 2)

    radii_px = radii_px[::-1]
    intensity_discs = intensity_discs[::-1]
    for radius, value in zip(radii_px, intensity_discs):
        img[dist < radius] = value

    # downsample the stimulus by local averaging along rows and columns
    sampler = resize_array(np.eye(img.shape[0] // ssf), (1, ssf))
    img = np.dot(sampler, np.dot(img, sampler.T)) / ssf**2
    return img


def disc(
    ppd=20,
    radius=3,
    intensity_background=0.0,
    intensity_disc=1.0,
    ssf=5,
):
    """
    Create a central disc

    Parameters
    ----------
    ppd : int
        pixels per degree (visual angle)
    radius : float
        radius of disc in degree visual angle
    intensity_background : float
        intensity value for background
    intensity_disc : float
        intensity value for disc
    ssf : int (optional)
          the supersampling-factor used for anti-aliasing. Default is 5.

    Returns
    -------
    A 2d-array with a disc
    """
    radius = [radius]
    intensity_disc = [intensity_disc]

    if len(radius) > 1:
        raise ValueError("Too many radii passed")
    if len(intensity_disc) > 1:
        raise ValueError("Too many values for discs passed")

    img = disc_and_rings(ppd, radius, intensity_background, intensity_disc, ssf)
    return img


def square_wave_grating(
    ppd=10,
    n_bars=8,
    bar_shape=(8.0, 1.0),
    intensity_min=0.0,
    intensity_max=1.0,
):
    """
    Square-wave grating

    Parameters
    ----------
    ppd : int
        pixels per degree (visual angle)
    n_bars : int
        the number of vertical bars
    bar_shape : (float, float)
        bar height and width in degrees visual angle
    intensity_min : float
        intensity value for first bar
    intensity_max : float
        intensity value for second bar

    Returns
    -------
    A 2d-array with a square-wave grating
    """

    bar_height_px, bar_width_px = degrees_to_pixels(bar_shape, ppd)
    img = np.ones([1, n_bars]) * intensity_max
    img[:, ::2] = intensity_min
    img = img.repeat(bar_width_px, axis=1).repeat(bar_height_px, axis=0)
    return img


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
