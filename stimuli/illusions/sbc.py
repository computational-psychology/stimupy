import numpy as np
import stimuli
from stimuli.utils import pad_img, plot_stim


def simultaneous_brightness_contrast(
    ppd=10,
    target_shape=(5, 5),
    padding=(2, 2, 2, 2),
    inner_padding=(3, 3, 3, 3),
    left=1.0,
    right=0.0,
    target=0.5,
):
    """
    Simultaneous brightness contrast

    Parameters
    ----------
    ppd : int
        pixels per degree (visual angle)
    target shape : (float, float)
        target shape in degrees visual angle (height, width)
    padding : (float, float, float, float)
        4-valued tuple specifying outer padding (top, bottom, left, right) in degrees visual angle
    inner_padding:
        4-valued tuple specifying inner padding (top, bottom, left, right) in degrees visual angle
    left : float
        left background value
    right : float
        right background value
    target : float
        target value

    Returns
    -------
    A stimulus object
    """

    target_height, target_width = target_shape

    target_height_px, target_width_px = stimuli.utils.degrees_to_pixels(
        target_shape, ppd
    )

    img = np.ones((target_height_px, target_width_px)) * target
    mask = np.ones((target_height_px, target_width_px))

    img1 = pad_img(img, inner_padding, ppd, left)
    img2 = pad_img(img, inner_padding, ppd, right)
    img = np.hstack((img1, img2))

    mask1 = pad_img(mask, inner_padding, ppd, 0)
    mask2 = pad_img(mask, inner_padding, ppd, 0)
    mask = np.hstack((mask1, mask2 * 2))

    img = pad_img(img, padding, ppd, target)
    mask = pad_img(mask, padding, ppd, 0)

    return {"img": img, "mask": mask}


def RHS2007_sbc_large():
    total_height, total_width, ppd = (32,) * 3
    height, width = 12, 15
    target_height, target_width = 3, 3

    inner_padding_vertical, inner_padding_horizontal = (
        height - target_height
    ) / 2, (width - target_width) / 2
    inner_padding = (
        inner_padding_vertical,
        inner_padding_vertical,
        inner_padding_horizontal,
        inner_padding_horizontal,
    )

    padding_vertical, padding_horizontal = (total_height - height) / 2, (
        total_width - 2 * width
    ) / 2
    padding = (
        padding_vertical,
        padding_vertical,
        padding_horizontal,
        padding_horizontal,
    )

    return simultaneous_brightness_contrast(
        target_shape=(target_height, target_width),
        ppd=ppd,
        inner_padding=inner_padding,
        padding=padding,
    )


def RHS2007_sbc_small():
    total_height, total_width, ppd = (32,) * 3
    height, width = 12, 15
    target_height, target_width = 1, 1

    inner_padding_vertical, inner_padding_horizontal = (
        height - target_height
    ) / 2, (width - target_width) / 2
    inner_padding = (
        inner_padding_vertical,
        inner_padding_vertical,
        inner_padding_horizontal,
        inner_padding_horizontal,
    )

    padding_vertical, padding_horizontal = (total_height - height) / 2, (
        total_width - 2 * width
    ) / 2
    padding = (
        padding_vertical,
        padding_vertical,
        padding_horizontal,
        padding_horizontal,
    )

    return simultaneous_brightness_contrast(
        target_shape=(target_height, target_width),
        ppd=ppd,
        inner_padding=inner_padding,
        padding=padding,
    )


if __name__ == "__main__":
    import matplotlib.pyplot as plt

    stim = simultaneous_brightness_contrast()
    plot_stim(stim, mask=True)
