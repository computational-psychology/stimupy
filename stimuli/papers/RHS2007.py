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

VISEXTENT = (32.0, 32.0)
PPD = 32


def WE_thick(ppd=PPD):
    height, width = 12.0, 16.0
    n_cycles = 4.0
    frequency = n_cycles / width
    target_height = 4 + (1 / ppd)
    stim = stimuli.illusions.whites.white(
        shape=(height, width),
        ppd=ppd,
        frequency=frequency,
        start="low",
        target_indices=(3, 6),
        target_height=target_height,
        targets_offset=1,
    )
    shape = degrees_to_pixels(VISEXTENT, ppd)
    stim["img"] = pad_img_to_shape(stim["img"], shape, val=0.5)
    stim["mask"] = pad_img_to_shape(stim["mask"], shape, val=0)
    return stim


def WE_thin_wide(ppd=PPD):
    height, width = 12.0, 16.0
    n_cycles = 8.0
    frequency = n_cycles / width
    target_height = 2
    stim = stimuli.illusions.whites.white(
        shape=(height, width),
        ppd=ppd,
        frequency=frequency,
        start="high",
        target_indices=(4, 13),
        target_height=target_height,
    )

    shape = degrees_to_pixels(VISEXTENT, ppd)
    stim["img"] = pad_img_to_shape(stim["img"], shape, val=0.5)
    stim["mask"] = pad_img_to_shape(stim["mask"], shape, val=0)
    return stim


def WE_dual(ppd=PPD):
    height, width = 6.0, 8.0
    n_cycles = 4.0
    frequency = n_cycles / width
    target_height = 2.0

    stim1 = stimuli.illusions.whites.white(
        shape=(height, width),
        ppd=ppd,
        frequency=frequency,
        start="low",
        target_indices=(3, 6),
        target_height=target_height,
    )

    shape = degrees_to_pixels(VISEXTENT, ppd)
    stim1["img"] = pad_img_to_shape(stim1["img"], shape / (1, 2), val=0.5)
    stim1["mask"] = pad_img_to_shape(stim1["mask"], shape / (1, 2), val=0)

    stim2 = stimuli.illusions.whites.white(
        shape=(height, width),
        ppd=ppd,
        frequency=frequency,
        start="low",
        target_indices=(3, 6),
        target_height=target_height,
        orientation="vertical",
    )

    stim2["img"] = pad_img_to_shape(stim2["img"], shape / (1, 2), val=0.5)
    stim2["mask"] = pad_img_to_shape(stim2["mask"], shape / (1, 2), val=0)

    stim = {
        "img": np.hstack((stim1["img"], stim2["img"])),
        "mask": np.hstack((stim1["mask"], stim2["mask"])),
    }

    return stim


def WE_anderson(ppd=PPD):
    height, width = 16.0, 16.0
    n_cycles = 8.0
    frequency = n_cycles / width
    height_bars = height / 5
    height_horizontal = height_bars
    target_height = height_bars

    stim = stimuli.illusions.whites.white_anderson(
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
    )
    shape = degrees_to_pixels(VISEXTENT, ppd)
    stim["img"] = pad_img_to_shape(stim["img"], shape, val=0.5)
    stim["mask"] = pad_img_to_shape(stim["mask"], shape, val=0)
    return stim


def WE_howe(ppd=PPD):
    height, width = 16.0, 16.0
    n_cycles = 8.0
    frequency = n_cycles / width
    height_bars = height / 5.0
    height_horizontal = height_bars
    target_height = height_bars
    stim = stimuli.illusions.whites.white_anderson(
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
    )
    shape = degrees_to_pixels(VISEXTENT, ppd)
    stim["img"] = pad_img_to_shape(stim["img"], shape, val=0.5)
    stim["mask"] = pad_img_to_shape(stim["mask"], shape, val=0)
    return stim


def WE_zigzag():
    # TODO: not available atm
    raise NotImplementedError


def WE_radial_thick_small(ppd=PPD):
    radius = 8.0
    n_cycles = 7.0
    stim = stimuli.illusions.whites.wheel_of_fortune_white(
        radius=radius,
        ppd=ppd,
        n_cycles=n_cycles,
        angle_shift=np.pi / n_cycles / 2.0,
        target_indices=(n_cycles - 1, 2 * n_cycles - 1),
        target_width=0.5,
        target_start=0.55,
    )
    shape = degrees_to_pixels(VISEXTENT, ppd)
    stim["img"] = pad_img_to_shape(stim["img"], shape, val=0.5)
    stim["mask"] = pad_img_to_shape(stim["mask"], shape, val=0)
    return stim


def WE_radial_thick(ppd=PPD):
    radius = 12.0
    n_cycles = 9.0
    stim = stimuli.illusions.whites.wheel_of_fortune_white(
        radius=radius,
        ppd=ppd,
        n_cycles=n_cycles,
        angle_shift=np.pi / n_cycles / 2.0,
        target_indices=(n_cycles - 1, 2 * n_cycles - 1),
        target_width=0.3,
        target_start=0.5,
    )
    shape = degrees_to_pixels(VISEXTENT, ppd)
    stim["img"] = pad_img_to_shape(stim["img"], shape, val=0.5)
    stim["mask"] = pad_img_to_shape(stim["mask"], shape, val=0)
    return stim


def WE_radial_thin_small(ppd=PPD):
    radius = 8.0
    n_cycles = 13.0
    stim = stimuli.illusions.whites.wheel_of_fortune_white(
        radius=radius,
        ppd=ppd,
        n_cycles=n_cycles,
        angle_shift=np.pi / n_cycles / 2,
        target_indices=(n_cycles - 1, 2 * n_cycles - 1),
        target_width=0.25,
        target_start=0.5,
    )
    shape = degrees_to_pixels(VISEXTENT, ppd)
    stim["img"] = pad_img_to_shape(stim["img"], shape, val=0.5)
    stim["mask"] = pad_img_to_shape(stim["mask"], shape, val=0)
    return stim


def WE_radial_thin(ppd=PPD):
    radius = 12.0
    n_cycles = 21.0
    stim = stimuli.illusions.whites.wheel_of_fortune_white(
        radius=radius,
        ppd=ppd,
        n_cycles=n_cycles,
        angle_shift=np.pi / n_cycles / 2,
        target_indices=(n_cycles - 1, 2 * n_cycles - 1),
        target_width=0.15,
        target_start=0.55,
    )
    shape = degrees_to_pixels(VISEXTENT, ppd)
    stim["img"] = pad_img_to_shape(stim["img"], shape, val=0.5)
    stim["mask"] = pad_img_to_shape(stim["mask"], shape, val=0)
    return stim


def WE_circular1(ppd=PPD):
    radius = 8.0
    n_cycles = 4.0
    frequency = n_cycles / radius
    stim1 = stimuli.illusions.whites.circular_white(
        radius=radius,
        ppd=ppd,
        frequency=frequency,
        target_indices=(4,),
        start="high",
    )

    stim2 = stimuli.illusions.whites.circular_white(
        radius=radius,
        ppd=ppd,
        frequency=frequency,
        target_indices=(4,),
        start="low",
    )
    stim2["mask"] *= 2

    stim = {
        "img": np.hstack((stim1["img"], stim2["img"])),
        "mask": np.hstack((stim1["mask"], stim2["mask"])),
    }

    shape = degrees_to_pixels(VISEXTENT, ppd)
    stim["img"] = pad_img_to_shape(stim["img"], shape, val=0.5)
    stim["mask"] = pad_img_to_shape(stim["mask"], shape, val=0)

    return stim


def WE_circular05(ppd=PPD):
    radius = 8
    n_cycles = 8
    frequency = n_cycles / radius
    stim1 = stimuli.illusions.whites.circular_white(
        radius=radius,
        ppd=ppd,
        frequency=frequency,
        target_indices=(10,),
        start="high",
    )
    stim2 = stimuli.illusions.whites.circular_white(
        radius=radius,
        ppd=ppd,
        frequency=frequency,
        target_indices=(10,),
        start="low",
    )
    stim2["mask"] *= 2

    stim = {
        "img": np.hstack((stim1["img"], stim2["img"])),
        "mask": np.hstack((stim1["mask"], stim2["mask"])),
    }

    shape = degrees_to_pixels(VISEXTENT, ppd)
    stim["img"] = pad_img_to_shape(stim["img"], shape, val=0.5)
    stim["mask"] = pad_img_to_shape(stim["mask"], shape, val=0)

    return stim


def WE_circular025(ppd=PPD):
    radius = 8.0
    n_cycles = 16.0
    frequency = n_cycles / radius
    stim1 = stimuli.illusions.whites.circular_white(
        radius=radius,
        ppd=ppd,
        frequency=frequency,
        target_indices=(22,),
        start="high",
    )
    stim2 = stimuli.illusions.whites.circular_white(
        radius=radius,
        ppd=ppd,
        frequency=frequency,
        target_indices=(22,),
        start="low",
    )
    stim2["mask"] *= 2

    stim = {
        "img": np.hstack((stim1["img"], stim2["img"])),
        "mask": np.hstack((stim1["mask"], stim2["mask"])),
    }

    shape = degrees_to_pixels(VISEXTENT, ppd)
    stim["img"] = pad_img_to_shape(stim["img"], shape, val=0.5)
    stim["mask"] = pad_img_to_shape(stim["mask"], shape, val=0)

    return stim


def grating_induction(ppd=PPD):
    n_cycles = 4.0
    height, width = 12.0, 16.0
    frequency = n_cycles / width
    stim = stimuli.illusions.grating_induction.grating_illusion(
        shape=(height, width),
        ppd=ppd,
        frequency=frequency,
        target_height=1,
        blur=10,
        start="high",
    )

    shape = degrees_to_pixels(VISEXTENT, ppd)
    stim["img"] = pad_img_to_shape(stim["img"], shape, val=0.5)
    stim["mask"] = pad_img_to_shape(stim["mask"], shape, val=0)

    return stim


def sbc_large(ppd=PPD):
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

    stim = stimuli.illusions.sbc.simultaneous_brightness_contrast(
        target_shape=(target_height, target_width),
        ppd=ppd,
        inner_padding=inner_padding,
    )
    shape = degrees_to_pixels(VISEXTENT, ppd)
    stim["img"] = pad_img_to_shape(stim["img"], shape, val=0.5)
    stim["mask"] = pad_img_to_shape(stim["mask"], shape, val=0)

    return stim


def sbc_small(ppd=PPD):
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

    stim = stimuli.illusions.sbc.simultaneous_brightness_contrast(
        target_shape=(target_height, target_width),
        ppd=ppd,
        inner_padding=inner_padding,
    )
    shape = degrees_to_pixels(VISEXTENT, ppd)
    stim["img"] = pad_img_to_shape(stim["img"], shape, val=0.5)
    stim["mask"] = pad_img_to_shape(stim["mask"], shape, val=0)

    return stim


def todorovic_equal(ppd=PPD):
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

    shape = degrees_to_pixels(VISEXTENT, ppd)
    stim["img"] = pad_img_to_shape(stim["img"], shape, val=0.5)
    stim["mask"] = pad_img_to_shape(stim["mask"], shape, val=0)

    return stim


def todorovic_in_large(ppd=PPD):
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

    shape = degrees_to_pixels(VISEXTENT, ppd)
    stim["img"] = pad_img_to_shape(stim["img"], shape, val=0.5)
    stim["mask"] = pad_img_to_shape(stim["mask"], shape, val=0)

    return stim


def todorovic_in_small(ppd=PPD):
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

    shape = degrees_to_pixels(VISEXTENT, ppd)
    stim["img"] = pad_img_to_shape(stim["img"], shape, val=0.5)
    stim["mask"] = pad_img_to_shape(stim["mask"], shape, val=0)

    return stim


def todorovic_out():
    # TODO: not available atm
    raise NotImplementedError


def checkerboard_016(ppd=PPD):
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

    shape = degrees_to_pixels(VISEXTENT, ppd)
    stim["img"] = pad_img_to_shape(stim["img"], shape, val=0.5)
    stim["mask"] = pad_img_to_shape(stim["mask"], shape, val=0)

    return stim


def checkerboard_0938(ppd=PPD):
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

    shape = degrees_to_pixels(VISEXTENT, ppd)
    stim["img"] = pad_img_to_shape(stim["img"], shape, val=0.5)
    stim["mask"] = pad_img_to_shape(stim["mask"], shape, val=0)

    return stim


def checkerboard209(ppd=PPD):
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

    shape = degrees_to_pixels(VISEXTENT, ppd)
    stim["img"] = pad_img_to_shape(stim["img"], shape, val=0.5)
    stim["mask"] = pad_img_to_shape(stim["mask"], shape, val=0)

    return stim


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


def bullseye_thin(ppd=PPD):
    # The parameters are mostly guessed
    stim = stimuli.illusions.bullseye.bullseye_illusion(
        n_rings=8,
        ring_width=1,
        back=1.0,
        rings=9.0,
        target=5.0,
    )
    shape = degrees_to_pixels(VISEXTENT, ppd)
    stim["img"] = pad_img_to_shape(stim["img"], shape, val=0.5)
    stim["mask"] = pad_img_to_shape(stim["mask"], shape, val=0)

    return stim


def bullseye_thick(ppd=PPD):
    # The parameters are mostly guessed
    stim = stimuli.illusions.bullseye.bullseye_illusion(
        n_rings=8,
        ring_width=1,
        back=1.0,
        rings=9.0,
        target=5.0,
    )

    shape = degrees_to_pixels(VISEXTENT, ppd)
    stim["img"] = pad_img_to_shape(stim["img"], shape, val=0.5)
    stim["mask"] = pad_img_to_shape(stim["mask"], shape, val=0)

    return stim


if __name__ == "__main__":
    from stimuli.utils import plot_stimuli

    stims = {}
    for stimname in __all__:
        print("Generating " + stimname)
        try:
            stims[stimname] = globals()[stimname]()
        except NotImplementedError:
            print("-- not implemented")

    plot_stimuli(stims, mask=False)
