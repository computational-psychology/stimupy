import numpy as np
from stimuli.utils import degrees_to_pixels, pad_img, plot_stim


def todorovic_illusion(
    target_shape=(4, 4),
    ppd=10,
    covers_shape=(2.5, 2.5),
    spacing=(1.5, 1.5, 1.5, 1.5),
    padding=(2, 2, 2, 2),
    back=0.0,
    grid=1.0,
    target=0.5,
    double=True,
):
    """
    Todorovic's illusion

    Parameters
    ----------
    target_shape : (float, float)
        The shape of the target in degrees of visual angle (height, width)
    ppd : int
        pixels per degree (visual angle)
    covers_shape : (float, float)
        The shape of the covers in degrees of visual angle (height, width)
    spacing : (float, float, float, float)
        Spacing between the covers in the form of (top, bottom, left, right).
    padding : (float, float, float, float)
        4-valued tuple specifying padding (top, bottom, left, right) in degrees visual angle
    back : float
        value for background
    grid : float
        value for grid cells
    target : float
        value for target
    double: bool
        whether to return the full illusion with two grids side-by-side

    Returns
    -------
    A stimulus object
    """

    target_height, target_width = target_shape
    target_height_px, target_width_px = degrees_to_pixels(target_shape, ppd)

    img = np.ones((target_height_px, target_width_px)) * target
    img = pad_img(img, padding, ppd, back)

    mask = np.ones((target_height_px, target_width_px))
    mask = pad_img(mask, padding, ppd, 0)

    padding_px = degrees_to_pixels(padding, ppd)
    (
        padding_top_px,
        padding_bottom_px,
        padding_left_px,
        padding_right_px,
    ) = padding_px

    width_px = padding_left_px + target_width_px + padding_right_px
    height_px = padding_top_px + target_height_px + padding_bottom_px

    cover_height_px, cover_width_px = degrees_to_pixels(covers_shape, ppd)
    spacing_px = degrees_to_pixels(spacing, ppd)
    (
        spacing_top_px,
        spacing_bottom_px,
        spacing_left_px,
        spacing_right_px,
    ) = spacing_px

    target_top_left_x = (width_px - target_width_px) // 2
    target_top_left_y = (height_px - target_height_px) // 2

    # top left square
    cover_start_x = target_top_left_x - spacing_top_px
    cover_start_y = target_top_left_y - spacing_left_px
    img[
        cover_start_y : cover_start_y + cover_height_px,
        cover_start_x : cover_start_x + cover_width_px,
    ] = grid
    mask[
        cover_start_y : cover_start_y + cover_height_px,
        cover_start_x : cover_start_x + cover_width_px,
    ] = 0

    # top right square
    cover_end_x = target_top_left_x + target_width_px + spacing_top_px
    cover_start_y = target_top_left_y - spacing_right_px
    img[
        cover_start_y : cover_start_y + cover_height_px,
        cover_end_x - cover_width_px : cover_end_x,
    ] = grid
    mask[
        cover_start_y : cover_start_y + cover_height_px,
        cover_end_x - cover_width_px : cover_end_x,
    ] = 0

    # bottom left square
    cover_start_x = target_top_left_x - spacing_bottom_px
    cover_end_y = target_top_left_y + target_height_px + spacing_left_px
    img[
        cover_end_y - cover_height_px : cover_end_y,
        cover_start_x : cover_start_x + cover_width_px,
    ] = grid
    mask[
        cover_end_y - cover_height_px : cover_end_y,
        cover_start_x : cover_start_x + cover_width_px,
    ] = 0

    # bottom right square
    cover_end_x = target_top_left_x + target_width_px + spacing_bottom_px
    cover_end_y = target_top_left_y + target_height_px + spacing_right_px
    img[
        cover_end_y - cover_height_px : cover_end_y,
        cover_end_x - cover_width_px : cover_end_x,
    ] = grid
    mask[
        cover_end_y - cover_height_px : cover_end_y,
        cover_end_x - cover_width_px : cover_end_x,
    ] = 0

    # create right half of stimulus
    if double:
        stim2 = todorovic_illusion(
            target_shape=target_shape,
            ppd=ppd,
            covers_shape=covers_shape,
            spacing=spacing,
            padding=padding,
            back=grid,
            grid=back,
            target=target,
            double=False,
        )
        img = np.hstack([img, stim2["img"]])
        mask = np.hstack([mask, stim2["mask"] * 2])

    # img = pad_img(img, padding, ppd, target)
    # mask = pad_img(mask, padding, ppd, 0)

    return {"img": img, "mask": mask}


if __name__ == "__main__":
    stim = todorovic_illusion()
    plot_stim(stim, mask=True)
