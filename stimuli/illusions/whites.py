import numpy as np
import matplotlib.pyplot as plt
import math

from stimuli.utils import degrees_to_pixels, pad_img, get_annulus_mask
from stimuli.Stimulus import Stimulus
from stimuli.illusions.square_wave import square_wave


def white(
    shape=(10, 10),
    ppd=50,
    frequency=0.4,
    high=1.0,
    low=0.0,
    target=0.5,
    period="ignore",
    start="low",
    target_indices=(2, -3),
    target_height=None,
    targets_offset=0,
    orientation="horizontal",
    padding=(2, 2, 2, 2),
    padding_val=0.5,
):
    """
    Whites's illusion

    Parameters
    ----------
    shape : (float, float)
        The shape of the illustion in degrees of visual angle (height, width)
    ppd : int
        pixels per degree (visual angle)
    frequency : float
        frequency of the grid in cycles per degree visual angle
    high : float
        value of the bright stripes
    low : float
        value of the dark stripes
    target : float
        value for target
    period : string in ['ignore', 'full', 'half']
        see square_wave.py for details about this
    start : string in ['low','high']
        whether to start with a bright or a low stripes
    target_indices : (int, )
        indices of the stripes where the target(s) will be placed. There will be as many targets as indices specified.
    target_height : float
        height of the target in degrees visual angle. If it's None, the target will be 1/3 of the illusion height
    targets_offset : int
        Vertical offset of the target in pixels
    orientation : string in ['horizontal', 'vertical']
        orientation of the illusion
    padding : (float, float, float, float)
        4-valued tuple specifying padding (top, bottom, left, right) in degrees visual angle

    Returns
    -------
    A stimulus object
    """

    height_px, width_px = degrees_to_pixels(shape, ppd)

    if target_height is None:
        target_height_px = degrees_to_pixels(shape[1] / 3, ppd)
    else:
        target_height_px = degrees_to_pixels(target_height, ppd)

    img, pixels_per_cycle = square_wave(
        shape, ppd, frequency, high, low, period, start
    )
    mask = np.zeros((height_px, width_px))

    height, width = img.shape
    phase_width = pixels_per_cycle // 2
    y_start = height // 2 - target_height_px // 2 - targets_offset
    y_end = y_start + target_height_px

    for i, index in enumerate(target_indices):
        if index >= 0:
            x_start = (index-1) * phase_width
        else:
            # Calculate the number of phases based on resolution of grating:
            phases = int(2 * (int(shape[1] * ppd / phase_width) // 2))
            x_start = int((phases + index) * phase_width)
        x_end = x_start + phase_width
        img[y_start:y_end, x_start:x_end] = target
        mask[y_start:y_end, x_start:x_end] = i+1.

    if orientation == "vertical":
        img = np.rot90(img, 3)
        mask = np.rot90(mask, 3)

    img = pad_img(img, padding, ppd, padding_val)
    mask = pad_img(mask, padding, ppd, 0)

    return {"img": img, "mask": mask}


def circular_white(
    radius=5,
    ppd=50,
    frequency=1.0,
    high=1.0,
    low=0.0,
    target=0.5,
    target_indices=(2, 6),
    start="low",
    padding=(2, 2, 2, 2),
):
    """
    Circular Whites's illusion

    Parameters
    ----------
    radius : float
        radius of the circle in degrees visual angle
    ppd : int
        pixels per degree (visual angle)
    frequency : float
        frequency of the circles in cycles per degree visual angle
    high : float
        value of the bright stripes
    low : float
        value of the dark stripes
    target : float
        value for target
    target_indices : (int, )
        indices of the stripes where the target(s) will be placed. There will be as many targets as indices specified.
    start : string in ['low','high']
        whether to start with a bright or a low stripes
    padding : (float, float, float, float)
        4-valued tuple specifying padding (top, bottom, left, right) in degrees visual angle

    Returns
    ----------
    A stimulus object
    """

    height, width = (degrees_to_pixels(radius * 2, ppd),) * 2
    pixels_per_cycle = degrees_to_pixels(1.0 / (frequency * 2), ppd) * 2
    circle_width = pixels_per_cycle // 2
    n_cycles = (max(height, width)) // (circle_width * 2)

    st = low if start == "low" else high
    other = high if start == "low" else low
    img = np.ones((height, width)) * target
    mask = np.zeros((height, width))

    mask_counter = 1
    for i in range(0, n_cycles):
        radius = circle_width * i
        annulus_mask = get_annulus_mask(
            (height, width),
            (height // 2, width // 2),
            radius,
            radius + circle_width,
        )
        img[annulus_mask] = st if i % 2 == 0 else other
        if i in target_indices:
            img[annulus_mask] = target
            mask[annulus_mask] = mask_counter
            mask_counter += 1
        else:
            img[annulus_mask] = st if i % 2 == 0 else other

    img = pad_img(img, padding, ppd, target)
    mask = pad_img(mask, padding, ppd, 0)

    return {"img": img, "mask": mask}


def wheel_of_fortune_white(
    radius=10,
    ppd=50,
    n_cycles=5,
    target_width=0.7,
    target_indices=None,
    target_start=0.5,
    angle_shift=0,
    high=1.0,
    low=0.0,
    target=0.5,
    start="high",
    padding=(1, 1, 1, 1),
):
    # TODO: make this faster
    """
    Wheel of fortune Whites's illusion

    Parameters
    ----------
    radius : float
        radius of the circle in degrees visual angle
    ppd : int
        pixels per degree (visual angle)
    n_cycles : int
        number of full grid cycles in the circle
    target_width :  float in interval [0,1]
        width of the target, 1 means target goes from center all the way to the edge of the circle
    target_indices : (int, )
        indices of the stripes where the target(s) will be placed
    target_start : float in interval [0,1]
        specify where the target starts relative to the radius
    angle_shift : float
        rotate the circle for specified amount of radians
    high : float
        value of the bright stripes
    low : float
        value of the dark stripes
    target : float
        value for target
    start : string in ['low','high']
        whether to start with a bright or a low stripes
    padding : (float, float, float, float)
        4-valued tuple specifying padding (top, bottom, left, right) in degrees visual angle

    Returns
    ----------
    A stimulus object
    """

    n_parts = n_cycles * 2
    n_grid = degrees_to_pixels(radius, ppd) * 2
    n_numbers = n_grid * 2

    if target_indices is None:
        target_indices = (0, n_parts // 2)

    # Create a circle
    x = np.linspace(0, 2 * np.pi, int(n_numbers))

    xx = np.cos(x)
    xx_min = np.abs(xx.min())
    xx += xx_min
    xx_max = xx.max()
    xx = xx / xx_max * (n_grid - 1)

    yy = np.sin(x)
    yy_min = np.abs(yy.min())
    yy += yy_min
    yy_max = yy.max()
    yy = yy / yy_max * (n_grid - 1)

    img = np.zeros([n_grid, n_grid]) + 0.5
    mask = np.zeros([n_grid, n_grid])

    st = high if start == "high" else low
    other = low if start == "high" else high

    # Divide circle in n_parts parts:
    x = np.linspace(0 + angle_shift, 2 * np.pi + angle_shift, int(n_parts + 1))

    mask_counter = 1
    for i in range(len(x) - 1):
        xxx = np.linspace(x[i], x[i + 1], int(n_numbers))
        xxxx = np.cos(xxx)
        xxxx += xx_min
        xxxx = xxxx / xx_max * (n_grid - 1)

        yyyy = np.sin(xxx)
        yyyy += yy_min
        yyyy = yyyy / yy_max * (n_grid - 1)

        for j in range(int(n_numbers)):
            sep_x = np.linspace(n_grid / 2, xxxx[j], int(n_numbers))
            sep_y = np.linspace(n_grid / 2, yyyy[j], int(n_numbers))
            # Switch between bright and dark areas:
            if i % 2 == 0:
                img[sep_x.astype(int), sep_y.astype(int)] = st
            else:
                img[sep_x.astype(int), sep_y.astype(int)] = other

            if i in target_indices:
                # Place a single target inside the area
                img[
                    sep_x[
                        int(
                            n_numbers * (target_start - target_width / 2)
                        ) : int(n_numbers * (target_start + target_width / 2))
                    ].astype(int),
                    sep_y[
                        int(
                            n_numbers * (target_start - target_width / 2)
                        ) : int(n_numbers * (target_start + target_width / 2))
                    ].astype(int),
                ] = target

                mask[
                    sep_x[
                        int(
                            n_numbers * (target_start - target_width / 2)
                        ) : int(n_numbers * (target_start + target_width / 2))
                    ].astype(int),
                    sep_y[
                        int(
                            n_numbers * (target_start - target_width / 2)
                        ) : int(n_numbers * (target_start + target_width / 2))
                    ].astype(int),
                ] = mask_counter
        mask_counter += 1

    mask_vals = np.unique(mask)
    mask_vals = mask_vals[1:]
    for i, val in enumerate(mask_vals):
        mask[mask == val] = i + 1

    img = pad_img(img, padding, ppd, target)
    mask = pad_img(mask, padding, ppd, 0)

    return {"img": img, "mask": mask}


def white_anderson(
    shape=(5, 5),
    ppd=40,
    frequency=2,
    height_bars=1,
    height_horizontal_top=1,
    target_height=1,
    target_indices_top=(5,),
    target_offsets_top=(0.5,),
    target_indices_bottom=(12,),
    target_offsets_bottom=(-0.5,),
    high=1.0,
    low=0.0,
    target=0.5,
    top="low",
    padding=(1, 1, 1, 1),
):
    """
    Anderson's white illusion

    Parameters
    ----------
    shape : (float, float)
        The shape of the illustion in degrees of visual angle (height, width)
    ppd : int
        pixels per degree (visual angle)
    frequency : float
        frequency of the grid in cycles per degree visual angle
    height_bars : float
        height of the bars in degrees visual angle
    target_height : float
        height of the target in degrees visual angle. If it's None, the target will be 1/3 of the illusion height
    target_indices_top : (int, )
        indices of the stripes where the target(s) will be placed. If None, two targets are put on (0, n_parts // 2).
    target_offsets_top : (float, )
        vertical offsets of targets in the top
    target_indices_bottom : (int, )
        indices of the stripes where the target(s) will be placed. If None, two targets are put on (0, n_parts // 2).
    target_offsets_bottom : (float, )
        vertical offsets of targets in the bottom
    high : float
        value of the bright stripes
    low : float
        value of the dark stripes
    target : float
        value for target
    top : string in ['low', 'high']
        specify whether the top should be bright or dark
    padding : (float, float, float, float)
        4-valued tuple specifying padding (top, bottom, left, right) in degrees visual angle

    Returns
    -------
    A stimulus object
    """
    height, width = degrees_to_pixels(shape, ppd)
    pixels_per_cycle = degrees_to_pixels(1.0 / (frequency * 2), ppd) * 2
    height_bars, height_horizontal_top = degrees_to_pixels(
        height_bars, ppd
    ), degrees_to_pixels(height_horizontal_top, ppd)
    spacing_bottom = height - 3 * height_bars - height_horizontal_top

    top = low if top == "low" else high
    bottom = high if top == low else low

    img = np.ones((height, width)) * bottom
    mask = np.zeros((height, width))

    index = [
        i + j
        for i in range(pixels_per_cycle // 2)
        for j in range(0, width, pixels_per_cycle)
        if i + j < width
    ]

    img[: height_bars * 2 + height_horizontal_top, index] = top
    img[-height_bars:, index] = top
    img[height_bars : height_bars + height_horizontal_top, :] = top

    target_height = degrees_to_pixels(target_height, ppd)
    target_offsets_top = tuple(
        degrees_to_pixels(x, ppd) for x in target_offsets_top
    )
    target_offsets_bottom = tuple(
        degrees_to_pixels(x, ppd) for x in target_offsets_bottom
    )

    for i, ind in enumerate(target_indices_top):
        st = int(pixels_per_cycle / 2 * ind)
        end = int(st + pixels_per_cycle / 2)
        img[: height_bars * 2 + height_horizontal_top, st:end] = bottom
        offset = target_offsets_top[i]
        target_start = (
            height_bars + (height_horizontal_top - target_height) // 2 + offset
        )
        target_end = target_start + target_height
        img[target_start:target_end, st:end] = target
        mask[target_start:target_end, st:end] = i + 1

    for i, ind in enumerate(target_indices_bottom):
        st = int(pixels_per_cycle / 2 * ind)
        end = int(st + pixels_per_cycle / 2)
        img[height_bars + height_horizontal_top :, st:end] = top
        offset = target_offsets_bottom[i]
        target_start = -height_bars - spacing_bottom + offset
        target_end = target_start + target_height
        img[target_start:target_end, st:end] = target
        mask[target_start:target_end, st:end] = len(target_indices_top) + i + 1

    img = pad_img(img, padding, ppd, target)
    mask = pad_img(mask, padding, ppd, 0)

    return {"img": img, "mask": mask}


def RHS2007_WE_thick():
    total_height, total_width, ppd = (32.0,) * 3
    height, width = 12.0, 16.0
    n_cycles = 4.0
    frequency = n_cycles / width
    padding_horizontal = (total_width - width) / 2
    padding_vertical = (total_height - height) / 2
    padding = (
        padding_vertical,
        padding_vertical,
        padding_horizontal,
        padding_horizontal,
    )
    target_height = 4
    return white(
        shape=(height, width),
        ppd=ppd,
        frequency=frequency,
        start="low",
        target_indices=(3, 6),
        padding=padding,
        target_height=target_height,
    )


def RHS2007_WE_thin_wide():
    total_height, total_width, ppd = (32.0,) * 3
    height, width = 12.0, 16.0
    n_cycles = 8.0
    frequency = n_cycles / width
    padding_horizontal = (total_width - width) / 2.0
    padding_vertical = (total_height - height) / 2.0
    padding = (
        padding_vertical,
        padding_vertical,
        padding_horizontal,
        padding_horizontal,
    )
    target_height = 2
    return white(
        shape=(height, width),
        ppd=ppd,
        frequency=frequency,
        start="high",
        target_indices=(4, 13),
        padding=padding,
        target_height=target_height,
    )


def RHS2007_WE_dual():
    total_height, total_width, ppd = (32.0,) * 3
    height, width = 6.0, 8.0
    n_cycles = 4.0
    frequency = n_cycles / width

    padding_horizontal1, padding_vertical1 = (
        total_width / 2.0 - width
    ) / 2.0, (total_height - height) / 2.0
    padding1 = (
        padding_vertical1,
        padding_vertical1,
        padding_horizontal1,
        padding_horizontal1,
    )
    padding_horizontal2, padding_vertical2 = (
        total_width / 2.0 - height
    ) / 2.0, (total_height - width) / 2.0
    padding2 = (
        padding_vertical2,
        padding_vertical2,
        padding_horizontal2,
        padding_horizontal2,
    )

    target_height = 2.0
    stim1 = white(
        shape=(height, width),
        ppd=ppd,
        frequency=frequency,
        start="low",
        target_indices=(3, 6),
        padding=padding1,
        target_height=target_height,
    )
    stim2 = white(
        shape=(height, width),
        ppd=ppd,
        frequency=frequency,
        start="low",
        target_indices=(3, 6),
        padding=padding2,
        target_height=target_height,
        orientation="vertical",
    )

    img = np.hstack((stim1['img'], stim2['img']))
    mask = np.hstack((stim1['mask'], stim2['mask']))

    return {"img": img, "mask": mask}



def RHS2007_WE_anderson():
    total_height, total_width, ppd = (32,) * 3
    height, width = 16.0, 16.0
    n_cycles = 8.0
    frequency = n_cycles / width
    height_bars = height / 5
    height_horizontal = height_bars
    target_height = height_bars
    padding_horizontal = (total_width - width) / 2
    padding_vertical = (total_height - height) / 2
    padding = (
        padding_vertical,
        padding_vertical,
        padding_horizontal,
        padding_horizontal,
    )
    return white_anderson(
        shape=(height, width),
        ppd=ppd,
        frequency=frequency,
        target_height=target_height,
        target_indices_top=(5,),
        target_offsets_top=(target_height / 2,),
        target_indices_bottom=(10,),
        target_offsets_bottom=(-target_height / 2,),
        height_bars=height_bars,
        height_horizontal_top=height_horizontal,
        padding=padding,
    )


def RHS2007_WE_howe():
    total_height, total_width, ppd = (32.0,) * 3
    height, width = 16.0, 16.0
    n_cycles = 8.0
    frequency = n_cycles / width
    height_bars = height / 5.0
    height_horizontal = height_bars
    target_height = height_bars
    padding_horizontal = (total_width - width) / 2.0
    padding_vertical = (total_height - height) / 2.0
    padding = (
        padding_vertical,
        padding_vertical,
        padding_horizontal,
        padding_horizontal,
    )
    return white_anderson(
        shape=(height, width),
        ppd=ppd,
        frequency=frequency,
        target_height=target_height,
        target_indices_top=(5,),
        target_offsets_top=(0,),
        target_indices_bottom=(10,),
        target_offsets_bottom=(0,),
        height_bars=height_bars,
        height_horizontal_top=height_horizontal,
        padding=padding,
    )


def RHS2007_WE_radial_thick_small():
    total_height, total_width, ppd = (32.0,) * 3
    radius = 8.0
    padding = ((total_width - 2 * radius) / 2.0,) * 4
    n_cycles = 7.0
    return wheel_of_fortune_white(
        radius=radius,
        ppd=ppd,
        n_cycles=n_cycles,
        angle_shift=np.pi / n_cycles / 2.0,
        target_indices=(n_cycles - 1, 2 * n_cycles - 1),
        target_width=0.5,
        target_start=0.55,
        padding=padding,
    )


def RHS2007_WE_radial_thick():
    total_height, total_width, ppd = (32.0,) * 3
    radius = 12.0
    padding = ((total_width - 2 * radius) / 2.0,) * 4
    n_cycles = 9.0
    return wheel_of_fortune_white(
        radius=radius,
        ppd=ppd,
        n_cycles=n_cycles,
        angle_shift=np.pi / n_cycles / 2.0,
        target_indices=(n_cycles - 1, 2 * n_cycles - 1),
        target_width=0.3,
        target_start=0.5,
        padding=padding,
    )


def RHS2007_WE_radial_thin_small():
    total_height, total_width, ppd = (32.0,) * 3
    radius = 8.0
    padding = ((total_width - 2 * radius) / 2.0,) * 4
    n_cycles = 13.0
    return wheel_of_fortune_white(
        radius=radius,
        ppd=ppd,
        n_cycles=n_cycles,
        angle_shift=np.pi / n_cycles / 2,
        target_indices=(n_cycles - 1, 2 * n_cycles - 1),
        target_width=0.25,
        target_start=0.5,
        padding=padding,
    )


def RHS2007_WE_radial_thin():
    total_height, total_width, ppd = (32,) * 3
    radius = 12.0
    padding = ((total_width - 2 * radius) / 2,) * 4
    n_cycles = 21.0
    return wheel_of_fortune_white(
        radius=radius,
        ppd=ppd,
        n_cycles=n_cycles,
        angle_shift=np.pi / n_cycles / 2,
        target_indices=(n_cycles - 1, 2 * n_cycles - 1),
        target_width=0.15,
        target_start=0.55,
        padding=padding,
    )


def RHS2007_WE_circular1():
    total_height, total_width, ppd = (32,) * 3
    radius = 8.0
    n_cycles = 4.0
    frequency = n_cycles / radius
    padding_vertical = (total_height - 2 * radius) / 2
    padding = (padding_vertical, padding_vertical, 0, 0)
    stim1 = circular_white(
        radius=radius,
        ppd=ppd,
        frequency=frequency,
        target_indices=(4,),
        start="high",
        padding=padding,
    )
    stim2 = circular_white(
        radius=radius,
        ppd=ppd,
        frequency=frequency,
        target_indices=(4,),
        start="low",
        padding=padding,
    )
    stim2['mask'] *= 2

    img = np.hstack((stim1['img'], stim2['img']))
    mask = np.hstack((stim1['mask'], stim2['mask']))

    return {"img": img, "mask": mask}


def RHS2007_WE_circular05():
    total_height, total_width, ppd = (32,) * 3
    radius = 8
    n_cycles = 8
    frequency = n_cycles / radius
    padding_vertical = (total_height - 2 * radius) / 2
    padding = (padding_vertical, padding_vertical, 0, 0)
    stim1 = circular_white(
        radius=radius,
        ppd=ppd,
        frequency=frequency,
        target_indices=(10,),
        start="high",
        padding=padding,
    )
    stim2 = circular_white(
        radius=radius,
        ppd=ppd,
        frequency=frequency,
        target_indices=(10,),
        start="low",
        padding=padding,
    )
    stim2['mask'] *= 2

    img = np.hstack((stim1['img'], stim2['img']))
    mask = np.hstack((stim1['mask'], stim2['mask']))

    return {"img": img, "mask": mask}


def RHS2007_WE_circular025():
    total_height, total_width, ppd = (32.0,) * 3
    radius = 8.0
    n_cycles = 16.0
    frequency = n_cycles / radius
    padding_vertical = (total_height - 2 * radius) / 2.0
    padding = (padding_vertical, padding_vertical, 0, 0)
    stim1 = circular_white(
        radius=radius,
        ppd=ppd,
        frequency=frequency,
        target_indices=(22,),
        start="high",
        padding=padding,
    )
    stim2 = circular_white(
        radius=radius,
        ppd=ppd,
        frequency=frequency,
        target_indices=(22,),
        start="low",
        padding=padding,
    )
    stim2['mask'] *= 2

    img = np.hstack((stim1['img'], stim2['img']))
    mask = np.hstack((stim1['mask'], stim2['mask']))

    return {"img": img, "mask": mask}


def domijan2015_white():
    height, width, ppd = 8.1, 8.0, 10
    n_cycles = 4
    frequency = n_cycles / width
    return white(
        shape=(height, width),
        ppd=ppd,
        frequency=frequency,
        high=9.0,
        low=1.0,
        target=5.0,
        period="ignore",
        start="low",
        target_indices=(3, 6),
        target_height=2.1,
        targets_offset=0,
        orientation="horizontal",
        padding=(0.9, 1.0, 0.9, 1.1),
    )


if __name__ == "__main__":
    stim = white()
    plt.subplot(4, 2, 1)
    plt.imshow(stim['img'], cmap="gray")
    plt.subplot(4, 2, 2)
    plt.imshow(stim['mask'], cmap="gray")

    stim = circular_white()
    plt.subplot(4, 2, 3)
    plt.imshow(stim['img'], cmap='gray')
    plt.subplot(4, 2, 4)
    plt.imshow(stim['mask'], cmap='gray')

    stim = wheel_of_fortune_white()
    plt.subplot(4, 2, 5)
    plt.imshow(stim['img'], cmap='gray')
    plt.subplot(4, 2, 6)
    plt.imshow(stim['mask'], cmap='gray')

    stim = white_anderson()
    plt.subplot(4, 2, 7)
    plt.imshow(stim['img'], cmap='gray')
    plt.subplot(4, 2, 8)
    plt.imshow(stim['mask'], cmap='gray')

    plt.tight_layout()
    plt.show()
