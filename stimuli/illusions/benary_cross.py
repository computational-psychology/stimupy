import numpy as np
from stimuli.utils import degrees_to_pixels, pad_img, plot_stim


def benarys_cross(
    ppd=10,
    cross_size=(8, 8, 8, 8),
    cross_thickness=5,
    padding=(1, 1, 1, 1),
    target_size=2,
    back=1.0,
    cross=0.0,
    target=0.5,
):
    """
    Benary's Cross Illusion (with square targets)

    Parameters
    ----------
    ppd : int
        pixels per degree (visual angle)
    cross_size : (float, float, float, float)
        size of the cross in degrees visual angle in form (top, bottom, left, right) specifying the length of each of the cross' bars
    cross_thickness : float
        width of the cross bars in degrees visual angle
    padding : (float, float, float, float)
        4-valued tuple specifying padding (top, bottom, left, right) in degrees visual angle
    target_size : float
        size of the side of target square in degrees visual angle
    back : float
        background value
    cross : float
        cross value
    target : float
        target value

    Returns
    -------
    A stimulus object
    """

    (
        cross_top_px,
        cross_bottom_px,
        cross_left_px,
        cross_right_px,
    ) = degrees_to_pixels(cross_size, ppd)
    cross_thickness_px = degrees_to_pixels(cross_thickness, ppd)
    target_size_px = degrees_to_pixels(target_size, ppd)

    width = cross_left_px + cross_thickness_px + cross_right_px
    height = cross_top_px + cross_thickness_px + cross_bottom_px

    img = np.ones((height, width)) * back
    mask = np.zeros((height, width))

    x_edge_left, x_edge_right = cross_left_px, -cross_right_px
    y_edge_top, y_edge_bottom = cross_top_px, -cross_bottom_px
    img[:, x_edge_left:x_edge_right] = cross
    img[y_edge_top:y_edge_bottom, :] = cross

    tpos1y = y_edge_top - target_size_px
    tpos1x = x_edge_left - target_size_px
    tpos2y = y_edge_top
    tpos2x = -target_size_px
    img[
        tpos1y : tpos1y + target_size_px, tpos1x : tpos1x + target_size_px
    ] = target
    img[tpos2y : tpos2y + target_size_px, tpos2x:] = target

    mask[
        tpos1y : tpos1y + target_size_px, tpos1x : tpos1x + target_size_px
    ] = 1
    mask[tpos2y : tpos2y + target_size_px, tpos2x:] = 2

    img = pad_img(img, padding, ppd, back)
    mask = pad_img(mask, padding, ppd, 0)

    return {"img": img, "mask": mask}


if __name__ == "__main__":
    import matplotlib.pyplot as plt

    stim = benarys_cross()
    plot_stim(stim, mask=True)
