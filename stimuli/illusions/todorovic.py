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


def domijan2015():
    return todorovic_illusion(
        target_shape=(4.1, 4.1),
        ppd=10,
        covers_shape=(3.1, 3.1),
        spacing=(1.5, 1.5, 1.5, 1.5),
        padding=(2.9, 3.0, 2.9, 3.0),
        grid=9.0,
        back=1.0,
        target=5.0,
    )


def RHS2007_todorovic_equal():
    total_height, total_width, ppd = (32,) * 3
    height, width = 12, 15
    target_height, target_width = 8, 8

    inner_padding_vertical, inner_padding_horizontal = (
        height - target_height
    ) / 2, (width - target_width) / 2
    inner_padding = (
        inner_padding_vertical,
        inner_padding_vertical,
        inner_padding_horizontal,
        inner_padding_horizontal,
    )

    covers_shape = (0.4 * 8,) * 2
    spacing = (0,) * 4

    back, grid, target = 1.0, 0.0, 0.5
    stim = todorovic_illusion(
        target_shape=(target_height, target_width),
        ppd=ppd,
        covers_shape=covers_shape,
        spacing=spacing,
        padding=inner_padding,
        back=back,
        grid=grid,
        target=target,
    )
    height_px, width_px = stim["img"].shape

    padding_vertical_top = degrees_to_pixels((total_height - height) / 2, ppd)
    padding_vertical_bottom = 1024 - padding_vertical_top - height_px
    padding_horizontal_left = degrees_to_pixels(
        (total_width - width * 2) / 2, ppd
    )
    padding_horizontal_right = 1024 - padding_horizontal_left - width_px

    img = np.pad(
        stim["img"],
        (
            (padding_vertical_top, padding_vertical_bottom),
            (padding_horizontal_left, padding_horizontal_right),
        ),
        "constant",
        constant_values=target,
    )
    mask = np.pad(
        stim["mask"],
        (
            (padding_vertical_top, padding_vertical_bottom),
            (padding_horizontal_left, padding_horizontal_right),
        ),
        "constant",
        constant_values=0,
    )

    return {"img": img, "mask": mask}


def RHS2007_todorovic_in_large():
    total_height, total_width, ppd = (32,) * 3
    height, width = 12, 15
    target_height, target_width = 5.3, 5.3

    inner_padding_vertical, inner_padding_horizontal = (
        height - target_height
    ) / 2, (width - target_width) / 2
    inner_padding = (
        inner_padding_vertical,
        inner_padding_vertical,
        inner_padding_horizontal,
        inner_padding_horizontal,
    )

    covers_shape = (0.4 * 8,) * 2
    spacing = ((8 - 5.3) / 2,) * 4

    back, grid, target = 1.0, 0.0, 0.5
    stim = todorovic_illusion(
        target_shape=(target_height, target_width),
        ppd=ppd,
        covers_shape=covers_shape,
        spacing=spacing,
        padding=inner_padding,
        back=back,
        grid=grid,
        target=target,
    )
    height_px, width_px = stim["img"].shape

    padding_vertical_top = degrees_to_pixels((total_height - height) / 2, ppd)
    padding_vertical_bottom = 1024 - padding_vertical_top - height_px
    padding_horizontal_left = degrees_to_pixels(
        (total_width - width * 2) / 2, ppd
    )
    padding_horizontal_right = 1024 - padding_horizontal_left - width_px

    img = np.pad(
        stim["img"],
        (
            (padding_vertical_top, padding_vertical_bottom),
            (padding_horizontal_left, padding_horizontal_right),
        ),
        "constant",
        constant_values=target,
    )
    mask = np.pad(
        stim["mask"],
        (
            (padding_vertical_top, padding_vertical_bottom),
            (padding_horizontal_left, padding_horizontal_right),
        ),
        "constant",
        constant_values=0,
    )

    return {"img": img, "mask": mask}


def RHS2007_todorovic_in_small():
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

    covers_shape = (0.4 * 8,) * 2
    spacing = ((8 - 3) / 2,) * 4

    back, grid, target = 1.0, 0.0, 0.5
    stim = todorovic_illusion(
        target_shape=(target_height, target_width),
        ppd=ppd,
        covers_shape=covers_shape,
        spacing=spacing,
        padding=inner_padding,
        back=back,
        grid=grid,
        target=target,
    )
    height_px, width_px = stim["img"].shape

    padding_vertical_top = degrees_to_pixels((total_height - height) / 2, ppd)
    padding_vertical_bottom = 1024 - padding_vertical_top - height_px
    padding_horizontal_left = degrees_to_pixels(
        (total_width - width * 2) / 2, ppd
    )
    padding_horizontal_right = 1024 - padding_horizontal_left - width_px

    stim["img"] = np.pad(
        stim["img"],
        (
            (padding_vertical_top, padding_vertical_bottom),
            (padding_horizontal_left, padding_horizontal_right),
        ),
        "constant",
        constant_values=target,
    )
    stim["mask"] = np.pad(
        stim["mask"],
        (
            (padding_vertical_top, padding_vertical_bottom),
            (padding_horizontal_left, padding_horizontal_right),
        ),
        "constant",
        constant_values=0,
    )

    return stim


if __name__ == "__main__":
    stim = todorovic_illusion()
    plot_stim(stim, mask=True)
