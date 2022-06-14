import math

import numpy as np
import stimuli
from stimuli.utils import degrees_to_pixels, pad_img_to_shape

__all__ = [
    "WE_thick",
    "WE_thin_wide",
    "WE_dual",
    "WE_anderson",
    "WE_howe",
    "WE_zigzag",
    "WE_radial_thick_small",
    "WE_radial_thick",
    "WE_radial_thin_small",
    "WE_circular1",
    "WE_circular05",
    "WE_circular025",
    "grating_induction",
    "sbc_large",
    "sbc_small",
    "todorovic_equal",
    "todorovic_in_large",
    "todorovic_in_small",
    "todorovic_out",
    "checkerboard_016",
    "checkerboard_0938",
    "checkerboard209",
    "corrugated_mondrian",
    "benary_cross",
    "todorovic_benary1_2",
    "todorovic_benary3_4",
    "bullseye_thin",
    "bullseye_thick",
]


def WE_thick():
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
    return stimuli.illusions.whites.white(
        shape=(height, width),
        ppd=ppd,
        frequency=frequency,
        start="low",
        target_indices=(3, 6),
        padding=padding,
        target_height=target_height + (1 / ppd),
        targets_offset=1,
    )


def WE_thin_wide():
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
    return stimuli.illusions.whites.white(
        shape=(height, width),
        ppd=ppd,
        frequency=frequency,
        start="high",
        target_indices=(4, 13),
        padding=padding,
        target_height=target_height,
    )


def WE_dual():
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
    stim1 = stimuli.illusions.whites.white(
        shape=(height, width),
        ppd=ppd,
        frequency=frequency,
        start="low",
        target_indices=(3, 6),
        padding=padding1,
        target_height=target_height,
    )
    stim2 = stimuli.illusions.whites.white(
        shape=(height, width),
        ppd=ppd,
        frequency=frequency,
        start="low",
        target_indices=(3, 6),
        padding=padding2,
        target_height=target_height,
        orientation="vertical",
    )

    img = np.hstack((stim1["img"], stim2["img"]))
    mask = np.hstack((stim1["mask"], stim2["mask"]))

    return {"img": img, "mask": mask}


def WE_anderson():
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
    return stimuli.illusions.whites.white_anderson(
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


def WE_howe():
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
    return stimuli.illusions.whites.white_anderson(
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


def WE_zigzag():
    # TODO: not available atm
    raise NotImplementedError


def WE_radial_thick_small():
    total_height, total_width, ppd = (32.0,) * 3
    radius = 8.0
    padding = ((total_width - 2 * radius) / 2.0,) * 4
    n_cycles = 7.0
    return stimuli.illusions.whites.wheel_of_fortune_white(
        radius=radius,
        ppd=ppd,
        n_cycles=n_cycles,
        angle_shift=np.pi / n_cycles / 2.0,
        target_indices=(n_cycles - 1, 2 * n_cycles - 1),
        target_width=0.5,
        target_start=0.55,
        padding=padding,
    )


def WE_radial_thick():
    total_height, total_width, ppd = (32.0,) * 3
    radius = 12.0
    padding = ((total_width - 2 * radius) / 2.0,) * 4
    n_cycles = 9.0
    return stimuli.illusions.whites.wheel_of_fortune_white(
        radius=radius,
        ppd=ppd,
        n_cycles=n_cycles,
        angle_shift=np.pi / n_cycles / 2.0,
        target_indices=(n_cycles - 1, 2 * n_cycles - 1),
        target_width=0.3,
        target_start=0.5,
        padding=padding,
    )


def WE_radial_thin_small():
    total_height, total_width, ppd = (32.0,) * 3
    radius = 8.0
    padding = ((total_width - 2 * radius) / 2.0,) * 4
    n_cycles = 13.0
    return stimuli.illusions.whites.wheel_of_fortune_white(
        radius=radius,
        ppd=ppd,
        n_cycles=n_cycles,
        angle_shift=np.pi / n_cycles / 2,
        target_indices=(n_cycles - 1, 2 * n_cycles - 1),
        target_width=0.25,
        target_start=0.5,
        padding=padding,
    )


def WE_radial_thin():
    total_height, total_width, ppd = (32,) * 3
    radius = 12.0
    padding = ((total_width - 2 * radius) / 2,) * 4
    n_cycles = 21.0
    return stimuli.illusions.whites.wheel_of_fortune_white(
        radius=radius,
        ppd=ppd,
        n_cycles=n_cycles,
        angle_shift=np.pi / n_cycles / 2,
        target_indices=(n_cycles - 1, 2 * n_cycles - 1),
        target_width=0.15,
        target_start=0.55,
        padding=padding,
    )


def WE_circular1():
    total_height, total_width, ppd = (32,) * 3
    radius = 8.0
    n_cycles = 4.0
    frequency = n_cycles / radius
    padding_vertical = (total_height - 2 * radius) / 2
    padding = (padding_vertical, padding_vertical, 0, 0)
    stim1 = stimuli.illusions.whites.circular_white(
        radius=radius,
        ppd=ppd,
        frequency=frequency,
        target_indices=(4,),
        start="high",
        padding=padding,
    )
    stim2 = stimuli.illusions.whites.circular_white(
        radius=radius,
        ppd=ppd,
        frequency=frequency,
        target_indices=(4,),
        start="low",
        padding=padding,
    )
    stim2["mask"] *= 2

    img = np.hstack((stim1["img"], stim2["img"]))
    mask = np.hstack((stim1["mask"], stim2["mask"]))

    return {"img": img, "mask": mask}


def WE_circular05():
    total_height, total_width, ppd = (32,) * 3
    radius = 8
    n_cycles = 8
    frequency = n_cycles / radius
    padding_vertical = (total_height - 2 * radius) / 2
    padding = (padding_vertical, padding_vertical, 0, 0)
    stim1 = stimuli.illusions.whites.circular_white(
        radius=radius,
        ppd=ppd,
        frequency=frequency,
        target_indices=(10,),
        start="high",
        padding=padding,
    )
    stim2 = stimuli.illusions.whites.circular_white(
        radius=radius,
        ppd=ppd,
        frequency=frequency,
        target_indices=(10,),
        start="low",
        padding=padding,
    )
    stim2["mask"] *= 2

    img = np.hstack((stim1["img"], stim2["img"]))
    mask = np.hstack((stim1["mask"], stim2["mask"]))

    return {"img": img, "mask": mask}


def WE_circular025():
    total_height, total_width, ppd = (32.0,) * 3
    radius = 8.0
    n_cycles = 16.0
    frequency = n_cycles / radius
    padding_vertical = (total_height - 2 * radius) / 2.0
    padding = (padding_vertical, padding_vertical, 0, 0)
    stim1 = stimuli.illusions.whites.circular_white(
        radius=radius,
        ppd=ppd,
        frequency=frequency,
        target_indices=(22,),
        start="high",
        padding=padding,
    )
    stim2 = stimuli.illusions.whites.circular_white(
        radius=radius,
        ppd=ppd,
        frequency=frequency,
        target_indices=(22,),
        start="low",
        padding=padding,
    )
    stim2["mask"] *= 2

    img = np.hstack((stim1["img"], stim2["img"]))
    mask = np.hstack((stim1["mask"], stim2["mask"]))

    return {"img": img, "mask": mask}


def grating_induction():
    total_height, total_width, ppd = (32.0,) * 3
    n_cycles = 4.0
    height, width = 12.0, 16.0
    frequency = n_cycles / width
    padding_horizontal = (total_width - width) / 2
    padding_vertical = (total_height - height) / 2
    padding = (
        padding_vertical,
        padding_vertical,
        padding_horizontal,
        padding_horizontal,
    )
    return stimuli.illusions.grating_induction.grating_illusion(
        shape=(height, width),
        ppd=ppd,
        frequency=frequency,
        target_height=1,
        blur=10,
        start="high",
        padding=padding,
    )


def sbc_large():
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

    return stimuli.illusions.sbc.simultaneous_brightness_contrast(
        target_shape=(target_height, target_width),
        ppd=ppd,
        inner_padding=inner_padding,
        padding=padding,
    )


def sbc_small():
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

    return stimuli.illusions.sbc.simultaneous_brightness_contrast(
        target_shape=(target_height, target_width),
        ppd=ppd,
        inner_padding=inner_padding,
        padding=padding,
    )


def todorovic_equal():
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
    stim = stimuli.illusions.todorovic.todorovic_illusion(
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


def todorovic_in_large():
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
    stim = stimuli.illusions.todorovic.todorovic_illusion(
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


def todorovic_in_small():
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
    stim = stimuli.illusions.todorovic.todorovic_illusion(
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


def todorovic_out():
    # TODO: not available atm
    raise NotImplementedError


def checkerboard_016():
    total_height, total_width, ppd = (32,) * 3
    height_checks, width_checks = 40, 102
    check_height = 32.0 / 102.0
    board_shape = (height_checks, width_checks)

    check1, check2, target = 1, 0, 0.5
    target_height = height_checks // 2
    stim = stimuli.illusions.checkerboard_sbc.checkerboard_contrast(
        ppd=ppd,
        board_shape=board_shape,
        check_size=check_height,
        targets_coords=((target_height, 16), (target_height, 85)),
        extend_targets=False,
        check1=check1,
        check2=check2,
        target=target,
    )

    img = pad_img_to_shape(stim["img"], (1024, 1024), val=target)
    mask = pad_img_to_shape(stim["mask"], (1024, 1024), val=0)

    return {"img": img, "mask": mask}


def checkerboard_0938():
    total_height, total_width, ppd = (32,) * 3
    height_checks, width_checks = 7, 25
    check_height = 0.938
    board_shape = (height_checks, width_checks)

    check1, check2, target = 0, 1, 0.5
    target_height = height_checks // 2
    stim = stimuli.illusions.checkerboard_sbc.checkerboard_contrast(
        ppd=ppd,
        board_shape=board_shape,
        check_size=check_height,
        targets_coords=((target_height, 6), (target_height, 17)),
        extend_targets=False,
        check1=check1,
        check2=check2,
        target=target,
    )
    img = pad_img_to_shape(stim["img"], (1024, 1024), val=target)
    mask = pad_img_to_shape(stim["mask"], (1024, 1024), val=0)

    return {"img": img, "mask": mask}


def checkerboard209():
    total_height, total_width, ppd = (32,) * 3
    height_checks, width_checks = 3, 10
    check_height = 2.09
    board_shape = (height_checks, width_checks)

    check1, check2, target = 0, 1, 0.5
    target_height = height_checks // 2
    stim = stimuli.illusions.checkerboard_sbc.checkerboard_contrast(
        ppd=ppd,
        board_shape=board_shape,
        check_size=check_height,
        targets_coords=((target_height, 2), (target_height, 7)),
        extend_targets=False,
        check1=check1,
        check2=check2,
        target=target,
    )
    img = pad_img_to_shape(stim["img"], (1024, 1024), val=target)
    mask = pad_img_to_shape(stim["mask"], (1024, 1024), val=0)

    return {"img": img, "mask": mask}


def corrugated_mondrian():
    # TODO: not available atm
    raise NotImplementedError


def benary_cross():
    # TODO: not available atm
    raise NotImplementedError


def todorovic_benary1_2():
    # TODO: not available atm
    raise NotImplementedError


def todorovic_benary3_4():
    # TODO: not available atm
    raise NotImplementedError


def bullseye_thin():
    # The parameters are mostly guessed
    return stimuli.illusions.bullseye.bullseye_illusion(
        n_rings=8,
        ring_width=1,
        padding=(100, 100, 100, 100),
        back=1.0,
        rings=9.0,
        target=5.0,
    )


def bullseye_thick():
    # The parameters are mostly guessed
    return stimuli.illusions.bullseye.bullseye_illusion(
        n_rings=8,
        ring_width=1,
        padding=(50, 50, 50, 50),
        back=1.0,
        rings=9.0,
        target=5.0,
    )


if __name__ == "__main__":
    import matplotlib.pyplot as plt

    stims = {}
    for stimname in __all__:
        print("Generating " + stimname)
        try:
            stims[stimname] = globals()[stimname]()
        except NotImplementedError:
            print("-- not implemented")

    # Plot each stimulus+mask
    n_stim = math.ceil(math.sqrt(len(stims)))
    plt.figure(figsize=(n_stim * 3, n_stim * 3))
    for i, (stim_name, stim) in enumerate(stims.items()):
        img, mask = stim["img"], stim["mask"]
        img = np.dstack([img, img, img])

        mask = np.insert(np.expand_dims(mask, 2), 1, 0, axis=2)
        mask = np.insert(mask, 2, 0, axis=2)
        final = mask + img
        final /= np.max(final)

        plt.subplot(n_stim, n_stim, i + 1)
        plt.title(stim_name)
        plt.imshow(final)

    plt.tight_layout()

    plt.show()
