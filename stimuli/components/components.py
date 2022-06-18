import numpy as np
from stimuli.utils import degrees_to_pixels


def rectangle(ppd=10, im_size=(4., 4.), rect_size=(2., 2.), rect_pos=(1., 1.), vback=0., vrect=0.5):
    """
    Function to create a 2d array with a rectangle

    Parameters
    ----------
    ppd : int
        pixels per degree (visual angle)
    im_size : (float, float)
        size of the image in degrees visual angle
    square_size : (float, float)
        size of the square in degrees visual angle
    square_pos : (float, float)
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
    img[rect_posy:rect_posy+rect_height, rect_posx:rect_posx+rect_width] = target
    return img


def triangle(ppd=10, target_size=(2., 2.), vback=0., vtriangle=0.5):
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
    line1 = np.linspace(0, target_y_px-1, np.maximum(target_y_px, target_x_px)*2).astype(int)
    line1 = np.linspace(line1, target_y_px-1, np.maximum(target_y_px, target_x_px)*2).astype(int)
    line2 = np.linspace(0, target_x_px-1, np.maximum(target_y_px, target_x_px)*2).astype(int)
    line2 = np.repeat(np.expand_dims(line2, -1), np.maximum(target_y_px, target_x_px)*2, 1)
    img[line1, line2] = vtriangle
    return img


def cross(ppd=10, cross_size=(8., 8., 8., 8.), cross_thickness=4., vback=0., vcross=1.):
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
    (cross_top, cross_bottom, cross_left, cross_right) = degrees_to_pixels(cross_size, ppd)
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


def parallelogram(ppd=10, para_size=(2., 3., 1.), vback=0., vpara=0.5):
    para_height, para_width, para_depth = degrees_to_pixels(para_size, ppd)

    # Create triangle to create parallelogram
    tri1 = triangle(ppd, (para_size[0], para_size[2]), 0., -vpara+vback)
    tri2 = triangle(ppd, (para_size[0], para_size[2]), -vpara+vback, 0.)

    # Create image, add rectangle and subtract triangles
    img = np.ones((para_height, para_width+para_depth)) * vpara
    img[0:para_height, 0:para_depth] += tri1
    img[0:para_height, para_width::] += tri2
    return img
