import numpy as np
from stimuli.utils import degrees_to_pixels, resize_array


def rectangle(
    ppd=10,
    im_size=(4.0, 4.0),
    rect_size=(2.0, 2.0),
    rect_pos=(1.0, 1.0),
    vback=0.0,
    vrect=0.5,
):
    """
    Function to create a 2d array with a rectangle

    Parameters
    ----------
    ppd : int
        pixels per degree (visual angle)
    im_size : (float, float)
        size of the image in degrees visual angle
    rect_size : (float, float)
        size of the square in degrees visual angle
    rect_pos : (float, float)
        coordinates of the square in degrees visual angle
    vback : float
        background value
    vrect : float
        rectangle value

    Returns
    -------
    A 2d-array with a rectangle
    """
    im_height, im_width = degrees_to_pixels(im_size, ppd)
    rect_height, rect_width = degrees_to_pixels(rect_size, ppd)
    rect_posy, rect_posx = degrees_to_pixels(rect_pos, ppd)

    # Create image and add square
    img = np.ones((im_height, im_width)) * vback
    target = np.ones((rect_height, rect_width)) * vrect
    img[
        rect_posy : rect_posy + rect_height, rect_posx : rect_posx + rect_width
    ] = target
    return img


def triangle(ppd=10, target_size=(2.0, 2.0), vback=0.0, vtriangle=0.5):
    """
    Function to create a 2d array with a triangle in the lower left diagonal

    Parameters
    ----------
    ppd : int
        pixels per degree (visual angle)
    target_size : (float, float)
        size of the target in degrees visual angle
    vback : float
        background value
    vtriangle : float
        triangle value

    Returns
    -------
    A 2d-array with a triangle
    """
    target_y_px, target_x_px = degrees_to_pixels(target_size, ppd)
    img = np.ones([target_y_px, target_x_px]) * vback
    line1 = np.linspace(
        0, target_y_px - 1, np.maximum(target_y_px, target_x_px) * 2
    ).astype(int)
    line1 = np.linspace(
        line1, target_y_px - 1, np.maximum(target_y_px, target_x_px) * 2
    ).astype(int)
    line2 = np.linspace(
        0, target_x_px - 1, np.maximum(target_y_px, target_x_px) * 2
    ).astype(int)
    line2 = np.repeat(
        np.expand_dims(line2, -1), np.maximum(target_y_px, target_x_px) * 2, 1
    )
    img[line1, line2] = vtriangle
    return img


def cross(
    ppd=10,
    cross_size=(8.0, 8.0, 8.0, 8.0),
    cross_thickness=4.0,
    vback=0.0,
    vcross=1.0,
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
    vback : float
        background value
    vcross : float
        cross value

    Returns
    -------
    A 2d-array with a cross
    """
    (cross_top, cross_bottom, cross_left, cross_right) = degrees_to_pixels(
        cross_size, ppd
    )
    cross_thickness = degrees_to_pixels(cross_thickness, ppd)
    width = cross_left + cross_thickness + cross_right
    height = cross_top + cross_thickness + cross_bottom

    # Create image and add cross
    img = np.ones((height, width)) * vback
    x_edge_left, x_edge_right = cross_left, -cross_right
    y_edge_top, y_edge_bottom = cross_top, -cross_bottom
    img[:, x_edge_left:x_edge_right] = vcross
    img[y_edge_top:y_edge_bottom, :] = vcross
    return img


def parallelogram(ppd=10, para_size=(2.0, 3.0, -1.0), vback=0.0, vpara=0.5):
    para_height, para_width, para_depth = degrees_to_pixels(para_size, ppd)
    para_depth = np.abs(para_depth)

    # Create triangle to create parallelogram
    if para_depth == 0.0:
        img = np.ones((para_height, para_width)) * vpara
    else:
        tri1 = triangle(
            ppd, (para_size[0], np.abs(para_size[2])), 0.0, -vpara + vback
        )
        tri2 = triangle(
            ppd, (para_size[0], np.abs(para_size[2])), -vpara + vback, 0.0
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
    high=1.0,
    low=0.0,
    period="ignore",
    start="high",
):
    """
    Create a horizontal square wave of given spatial frequency.

    Parameters
    ----------
    shape : (float, float)
        The shape of the stimulus in degrees of visual angle. (y,x)
    ppd : int
        pixels per degree (visual angle)
    high : float
        value of the bright pixels
    low : float
        value of the dark pixels
    frequency : float
        the spatial frequency of the wave in cycles per degree
    period : string in ['ignore', 'full', 'half']
        specifies if the period of the wave is taken into account when determining exact stimulus dimensions.
            'ignore' simply converts degrees to pixels
            'full' rounds down to guarantee a full period
            'half' adds a half period to the size 'full' would yield.
        Default is 'ignore'.
    start : string in ['high', 'low']
        specifies if the wave starts with a high or low value. Default is 'high'.

    Returns
    -------
    (2D ndarray, pixels_per_cycle)
    """

    if period not in ["ignore", "full", "half"]:
        raise TypeError("size not understood: %s" % period)
    if start not in ["high", "low"]:
        raise TypeError("start value not understood: %s" % start)
    if frequency > ppd / 2:
        raise ValueError("The frequency is limited to 1/2 cycle per pixel.")

    height, width = degrees_to_pixels(shape, ppd)
    pixels_per_cycle = degrees_to_pixels(1.0 / (frequency * 2.0), ppd) * 2

    if period == "full":
        width = (width // pixels_per_cycle) * pixels_per_cycle
    elif period == "half":
        width = (
            height // pixels_per_cycle
        ) * pixels_per_cycle + pixels_per_cycle / 2

    stim = np.ones((height, width)) * (low if start == "high" else high)

    index = [
        i + j
        for i in range(pixels_per_cycle // 2)
        for j in range(0, width, pixels_per_cycle)
        if i + j < width
    ]
    stim[:, index] = low if start == "low" else high
    return (stim, pixels_per_cycle)


def checkerboard(
        ppd=10,
        board_shape=(8, 8),
        check_size=1.0,
        vcheck1=0.0,
        vcheck2=1.0,
        ):

    check_size_px = degrees_to_pixels(check_size, ppd)
    nchecks_height, nchecks_width = board_shape

    img = np.ndarray((nchecks_height, nchecks_width))

    for i, j in np.ndindex((nchecks_height, nchecks_width)):
        img[i, j] = vcheck1 if i % 2 == j % 2 else vcheck2

    img = img.repeat(check_size_px, axis=0).repeat(check_size_px, axis=1)
    return img


def disc(
        ppd=20,
        radius=3,
        vback=0.,
        vdisc=1.,
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
    vback : float
        value of background
    vdisc : float
        value of disc
    ssf : int (optional)
          the supersampling-factor used for anti-aliasing. Default is 5.

    Returns
    -------
    A 2d-array with a disc
    """
    radius_px = degrees_to_pixels(radius, ppd) * ssf

    # create stimulus at 5 times size to allow for supersampling antialiasing
    img = np.ones([radius_px*2, radius_px*2]) * vback

    # compute distance from center of array for every point, cap at 1.0
    x = np.linspace(-img.shape[1] / 2.0, img.shape[1] / 2.0, img.shape[1])
    y = np.linspace(-img.shape[0] / 2.0, img.shape[0] / 2.0, img.shape[0])
    dist = np.sqrt(x[np.newaxis, :] ** 2 + y[:, np.newaxis] ** 2)
    img[dist < radius_px] = vdisc

    # downsample the stimulus by local averaging along rows and columns
    sampler = resize_array(np.eye(img.shape[0] // ssf), (1, ssf))
    img = np.dot(sampler, np.dot(img, sampler.T)) / ssf**2
    return img
