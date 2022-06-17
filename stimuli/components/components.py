import numpy as np
from stimuli.utils import degrees_to_pixels


def triangle(ppd=10., target_size=(2., 2.), vback=0., vtriangle=0.5):
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
    img = np.zeros([target_y_px, target_x_px])
    line1 = np.linspace(0, target_y_px-1, np.maximum(target_y_px, target_x_px)*2).astype(int)
    line1 = np.linspace(line1, target_y_px-1, np.maximum(target_y_px, target_x_px)*2).astype(int)
    line2 = np.linspace(0, target_x_px-1, np.maximum(target_y_px, target_x_px)*2).astype(int)
    line2 = np.repeat(np.expand_dims(line2, -1), np.maximum(target_y_px, target_x_px)*2, 1)
    img[line1, line2] = vtriangle
    return img


def cross(ppd=10., cross_size=(8., 8., 8., 8.), cross_thickness=4., vback=0., vcross=1.):
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
