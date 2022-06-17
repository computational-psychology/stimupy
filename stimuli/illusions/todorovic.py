import numpy as np
from stimuli.utils import degrees_to_pixels, pad_img, plot_stim, pad_img_to_shape
from stimuli.components import rectangle, cross


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


def todorovic_in(
        im_size=(10., 10.),
        ppd=10,
        target_size=(4., 4.),
        target_pos=(3., 3.),
        covers_height=2.,
        covers_width=2.,
        covers_posx=(2., 6., 2., 6.),
        covers_posy=(2., 6., 6., 2.),
        vback=0.,
        vtarget=0.5,
        vcovers=1.,
        ):
    """
    Todorovic's illusion with rectangular target and rectangles added

    Parameters
    ----------
    im_size : (float, float)
        size of the stimulus in degrees of visual angle (height, width)
    ppd : int
        pixels per degree (visual angle)
    target_size : (float, float)
        size of the target in degrees of visual angle (height, width)
    target_pos : (float, float)
        coordinates where to place the target
    covers_height : float or tuple of floats
        height of covers; if single float, all covers have the same height
    covers_width : float or tuple of floats
        width of covers; if single float, all covers have the same width
    covers_posx : tuple of floats
        x coordinates of covers; as many covers as there are coordinates
    covers_posy : tuple of floats
        y coordinates of covers; as many covers as there are coordinates
    vback : float
        value for background
    vtarget : float
        value for target
    vcovers : float
        value for covers

    Returns
    -------
    A stimulus object
    """

    if isinstance(covers_height, (float, int)):
        covers_height = [covers_height]*len(covers_posx)
    if isinstance(covers_width, (float, int)):
        covers_width = [covers_width]*len(covers_posy)

    if any(len(lst) != len(covers_height) for lst in [covers_width, covers_posx, covers_posy]):
        raise Exception("covers_height, covers_width, covers_posx and covers_posy need the same length.")

    # Create image with square
    img = rectangle(ppd, im_size, target_size, target_pos, vback, vtarget)

    # Add covers
    covers_height = degrees_to_pixels(covers_height, ppd)
    covers_width = degrees_to_pixels(covers_width, ppd)
    covers_posx = degrees_to_pixels(covers_posx, ppd)
    covers_posy = degrees_to_pixels(covers_posy, ppd)

    for i in range(len(covers_height)):
        img[covers_posy[i]:covers_posy[i]+covers_height[i],
            covers_posx[i]:covers_posx[i]+covers_width[i]] = vcovers

    mask = np.copy(img)
    mask[mask == vback] = 0
    mask[mask == vcovers] = 0
    mask[mask == vtarget] = 1
    return {"img": img, "mask": mask}


def todorovic_out(
        im_size=(12., 12.),
        ppd=10,
        target_size=(4., 4., 4., 4.),
        target_thickness=2.,
        covers_height=2.,
        covers_width=2.,
        covers_posx=(3., 7., 3., 7.),
        covers_posy=(3., 7., 7., 3.),
        vback=0.,
        vtarget=0.5,
        vcovers=1.,
        ):

    if isinstance(covers_height, (float, int)):
        covers_height = [covers_height]*len(covers_posx)
    if isinstance(covers_width, (float, int)):
        covers_width = [covers_width]*len(covers_posy)

    if any(len(lst) != len(covers_height) for lst in [covers_width, covers_posx, covers_posy]):
        raise Exception("covers_height, covers_width, covers_posx and covers_posy need the same length.")

    img = cross(ppd, target_size, target_thickness, vback, vtarget)
    img = pad_img_to_shape(img, np.array(im_size)*ppd, val=vback)

    covers_height = degrees_to_pixels(covers_height, ppd)
    covers_width = degrees_to_pixels(covers_width, ppd)
    covers_posx = degrees_to_pixels(covers_posx, ppd)
    covers_posy = degrees_to_pixels(covers_posy, ppd)

    # Add covers
    for i in range(len(covers_height)):
        img[covers_posy[i]:covers_posy[i]+covers_height[i],
            covers_posx[i]:covers_posx[i]+covers_width[i]] = vcovers

    mask = np.copy(img)
    mask[mask == vback] = 0
    mask[mask == vcovers] = 0
    mask[mask == vtarget] = 1
    return {"img": img, "mask": mask}


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    plt.figure(1)
    stim = todorovic_in()
    plot_stim(stim, mask=True)

    plt.figure(2)
    stim = todorovic_out()
    plot_stim(stim, mask=True)
