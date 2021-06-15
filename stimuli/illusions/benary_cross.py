import numpy as np


def benarys_cross(cross_size=(80,80,80,80), cross_thickness=20, padding=(10,10,10,10), target_size=10, back=1., cross=0., target=.5):
    """
    Benary's Cross Illusion (with square targets)

    Parameters
    ----------
    cross_size: size of the cross in px in form (top, bottom, left, right) specifying the length of each of the cross' bars
    cross_thickness: width of the cross bars in px
    padding: 4-valued tuple specifying padding (top, bottom, left, right) in px
    target_size: size of the side of target square in px
    back: background value
    cross: cross value
    target: target value

    Returns
    -------
    2D numpy array
    """

    padding_top, padding_bottom, padding_left, padding_right = padding
    cross_top, cross_bottom, cross_left, cross_right = cross_size
    width = cross_left + cross_thickness + cross_right
    height = cross_top+cross_thickness+cross_bottom

    img = np.ones((height, width)) * back

    x_edge_left, x_edge_right = cross_left, -cross_right
    y_edge_top, y_edge_bottom = cross_top, -cross_bottom
    img[:, x_edge_left:x_edge_right] = cross
    img[y_edge_top:y_edge_bottom, :] = cross


    tpos1y = y_edge_top - target_size
    tpos1x = x_edge_left - target_size
    tpos2y = y_edge_top
    tpos2x = -target_size
    img[tpos1y:tpos1y + target_size, tpos1x:tpos1x + target_size] = target
    img[tpos2y:tpos2y + target_size, tpos2x:] = target

    img = np.pad(img, ((padding_top, padding_bottom),(padding_left, padding_right)), 'constant', constant_values=back)

    return img

def domijan2015():
    return benarys_cross(cross_size=(30,30,30,30), cross_thickness=21, padding=(9,10,9,10),target_size=11,  back=9., cross=1., target=5.)

