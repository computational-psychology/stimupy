import numpy as np
from stimuli import illusions
from stimuli.utils import degrees_to_pixels, pad_img, pad_img_to_shape

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
    "todorovic_benary1_2_3_4",
    "bullseye_thin",
    "bullseye_thick",
]

VISEXTENT = (32.0, 32.0)
PPD = 32


def gen_all(ppd=PPD, skip=False):
    stims = {}  # save the stimulus-dicts in a larger dict, with name as key
    for stim_name in __all__:
        print(f"Generating RHS2007.{stim_name}")

        # Get a reference to the actual function
        func = globals()[stim_name]
        try:
            stim = func()

            # Accumulate
            stims[stim_name] = stim
        except NotImplementedError as e:
            if not skip:
                raise e
            # Skip stimuli that aren't implemented
            print("-- not implemented")
            pass

    return stims


def WE_thick(ppd=PPD):
    height, width = 12.0, 16.0
    n_cycles = 4.0
    frequency = n_cycles / width
    target_height = 4 + (1 / ppd)
    stim = illusions.whites.white(
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
    stim = illusions.whites.white(
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

    stim1 = illusions.whites.white(
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

    stim2 = illusions.whites.white(
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

    stim = illusions.whites.white_anderson(
        shape=(height, width),
        ppd=ppd,
        frequency=frequency,
        stripe_height=height / 5,
        stripe_ypos=(height / 5, 3 * height / 5),
        target_height=height / 5,
        target_indices_top=(5,),
        target_offsets_top=(height / 10,),
        target_indices_bottom=(10,),
        target_offsets_bottom=(-height / 10,),
        vbars=(0.0, 1.0),
        vtarget=0.5,
        vtopstripe=0.0,
        vbotstripe=1.0,
    )
    shape = degrees_to_pixels(VISEXTENT, ppd)
    stim["img"] = pad_img_to_shape(stim["img"], shape, val=0.5)
    stim["mask"] = pad_img_to_shape(stim["mask"], shape, val=0)
    return stim


def WE_howe(ppd=PPD):
    height, width = 16.0, 16.0
    n_cycles = 8.0
    frequency = n_cycles / width

    stim = illusions.whites.white_howe(
        shape=(height, width),
        ppd=ppd,
        frequency=frequency,
        stripe_height=height / 5,
        stripe_ypos=(height / 5, 3 * height / 5),
        target_height=height / 5,
        target_indices_top=(5,),
        target_indices_bottom=(10,),
        vbars=(0.0, 1.0),
        vtarget=0.5,
        vtopstripe=0.0,
        vbotstripe=1.0,
    )
    shape = degrees_to_pixels(VISEXTENT, ppd)
    stim["img"] = pad_img_to_shape(stim["img"], shape, val=0.5)
    stim["mask"] = pad_img_to_shape(stim["mask"], shape, val=0)
    return stim


def WE_zigzag(ppd=PPD):
    i1, i2 = -1, 0
    stim = illusions.whites.white_zigzag(
        ppd=PPD,
        L_size=(5.0, 6.3, 1.0),
        L_distance=1.0,
        L_repeats=(3.5, 3.6),
        target_height=3.0,
        target_idx_v1=((i1, -1), (i1, -0), (i1, 1), (i1, 2)),
        target_idx_v2=((i2, -1), (i2, -0), (i2, 1), (i2, -2)),
        v1=0.0,
        v2=1.0,
        vtarget=0.5,
    )
    shape = degrees_to_pixels(VISEXTENT, ppd)
    stim["img"] = pad_img_to_shape(stim["img"], shape, val=0.5)
    stim["mask"] = pad_img_to_shape(stim["mask"], shape, val=0)
    return stim


def WE_radial_thick_small(ppd=PPD):
    radius = 8.0
    n_cycles = 7.0
    stim = illusions.whites.wheel_of_fortune_white(
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
    stim = illusions.whites.wheel_of_fortune_white(
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
    stim = illusions.whites.wheel_of_fortune_white(
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
    stim = illusions.whites.wheel_of_fortune_white(
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
    stim1 = illusions.whites.circular_white(
        radius=radius,
        ppd=ppd,
        frequency=frequency,
        target_indices=(4,),
        start="high",
    )

    stim2 = illusions.whites.circular_white(
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
    stim1 = illusions.whites.circular_white(
        radius=radius,
        ppd=ppd,
        frequency=frequency,
        target_indices=(10,),
        start="high",
    )
    stim2 = illusions.whites.circular_white(
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
    stim1 = illusions.whites.circular_white(
        radius=radius,
        ppd=ppd,
        frequency=frequency,
        target_indices=(22,),
        start="high",
    )
    stim2 = illusions.whites.circular_white(
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
    stim = illusions.grating_induction.grating_illusion(
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
    im_size = (13.0, 15.5)
    tsize = 3.0
    target_pos = (
        im_size[0] / 2.0 - tsize / 2.0,
        im_size[1] / 2.0 - tsize / 2.0,
    )
    stim1 = illusions.sbc.simultaneous_contrast(
        ppd=ppd,
        im_size=im_size,
        target_size=(tsize, tsize),
        target_pos=target_pos,
        vback=0.0,
        vtarget=0.5,
    )
    stim2 = illusions.sbc.simultaneous_contrast(
        ppd=ppd,
        im_size=im_size,
        target_size=(tsize, tsize),
        target_pos=target_pos,
        vback=1.0,
        vtarget=0.5,
    )

    # Increase target index of right stimulus half
    mask2 = stim2["mask"] + 1
    mask2[mask2 == 1] = 0

    # Stacking
    img = np.hstack([stim1["img"], stim2["img"]])
    mask = np.hstack([stim1["mask"], mask2])

    shape = degrees_to_pixels(VISEXTENT, ppd)
    img = pad_img_to_shape(img, shape, val=0.5)
    mask = pad_img_to_shape(mask, shape, val=0)
    return {"img": img, "mask": mask}


def sbc_small(ppd=PPD):
    im_size = (13.0, 15.5)
    tsize = 1.0
    target_pos = (
        im_size[0] / 2.0 - tsize / 2.0,
        im_size[1] / 2.0 - tsize / 2.0,
    )
    stim1 = illusions.sbc.simultaneous_contrast(
        ppd=ppd,
        im_size=im_size,
        target_size=(tsize, tsize),
        target_pos=target_pos,
        vback=0.0,
        vtarget=0.5,
    )
    stim2 = illusions.sbc.simultaneous_contrast(
        ppd=ppd,
        im_size=im_size,
        target_size=(tsize, tsize),
        target_pos=target_pos,
        vback=1.0,
        vtarget=0.5,
    )

    # Increase target index of right stimulus half
    mask2 = stim2["mask"] + 1
    mask2[mask2 == 1] = 0

    # Stacking
    img = np.hstack([stim1["img"], stim2["img"]])
    mask = np.hstack([stim1["mask"], mask2])

    shape = degrees_to_pixels(VISEXTENT, ppd)
    img = pad_img_to_shape(img, shape, val=0.5)
    mask = pad_img_to_shape(mask, shape, val=0)
    return {"img": img, "mask": mask}


def todorovic_equal(ppd=PPD):
    im_size = (13.0, 15.5)
    csize = 3.2
    tthick = csize / 2.0
    posx1 = im_size[1] / 2.0 - csize - tthick / 2.0
    posx2 = im_size[1] / 2.0 + tthick / 2.0 - 1 / ppd
    posy1 = im_size[0] / 2.0 - csize - tthick / 2.0
    posy2 = im_size[0] / 2.0 + tthick / 2.0 - 1 / ppd

    stim1 = illusions.todorovic.todorovic_out(
        im_size=im_size,
        ppd=ppd,
        target_size=(csize,) * 4,
        target_thickness=tthick,
        covers_height=csize,
        covers_width=csize,
        covers_posx=(posx1, posx2, posx1, posx2),
        covers_posy=(posy1, posy2, posy2, posy1),
        vback=1.0,
        vtarget=0.5,
        vcovers=0.0,
    )
    stim2 = illusions.todorovic.todorovic_out(
        im_size=im_size,
        ppd=ppd,
        target_size=(csize,) * 4,
        target_thickness=tthick,
        covers_height=csize,
        covers_width=csize,
        covers_posx=(posx1, posx2, posx1, posx2),
        covers_posy=(posy1, posy2, posy2, posy1),
        vback=0.0,
        vtarget=0.5,
        vcovers=1.0,
    )

    # Increase target index of right stimulus half
    mask2 = stim2["mask"] + 1
    mask2[mask2 == 1] = 0

    # Stacking
    img = np.hstack([stim1["img"], stim2["img"]])
    mask = np.hstack([stim1["mask"], mask2])

    shape = degrees_to_pixels(VISEXTENT, ppd)
    img = pad_img_to_shape(img, shape, val=0.5)
    mask = pad_img_to_shape(mask, shape, val=0)
    return {"img": img, "mask": mask}


def todorovic_in_large(ppd=PPD):
    im_size = (13.0, 15.5)
    tsize = 5.3
    tpos = np.array(im_size) / 2.0 - tsize / 2.0
    csize = 3.2
    posx1 = im_size[1] / 2.0 - csize - csize / 4.0
    posx2 = im_size[1] / 2.0 + csize / 4.0 - 1 / ppd
    posy1 = im_size[0] / 2.0 - csize - csize / 4.0
    posy2 = im_size[0] / 2.0 + csize / 4.0 - 1 / ppd

    stim1 = illusions.todorovic.todorovic_in(
        im_size=im_size,
        ppd=ppd,
        target_size=(tsize, tsize),
        target_pos=tpos,
        covers_height=csize,
        covers_width=csize,
        covers_posx=(posx1, posx2, posx1, posx2),
        covers_posy=(posy1, posy2, posy2, posy1),
        vback=1.0,
        vtarget=0.5,
        vcovers=0.0,
    )
    stim2 = illusions.todorovic.todorovic_in(
        im_size=im_size,
        ppd=ppd,
        target_size=(tsize, tsize),
        target_pos=tpos,
        covers_height=csize,
        covers_width=csize,
        covers_posx=(posx1, posx2, posx1, posx2),
        covers_posy=(posy1, posy2, posy2, posy1),
        vback=0.0,
        vtarget=0.5,
        vcovers=1.0,
    )

    # Increase target index of right stimulus half
    mask2 = stim2["mask"] + 1
    mask2[mask2 == 1] = 0

    # Stacking
    img = np.hstack([stim1["img"], stim2["img"]])
    mask = np.hstack([stim1["mask"], mask2])

    shape = degrees_to_pixels(VISEXTENT, ppd)
    img = pad_img_to_shape(img, shape, val=0.5)
    mask = pad_img_to_shape(mask, shape, val=0)
    return {"img": img, "mask": mask}


def todorovic_in_small(ppd=PPD):
    im_size = (13.0, 15.5)
    tsize = 3.0
    tpos = np.array(im_size) / 2.0 - tsize / 2.0
    csize = 3.2
    posx1 = im_size[1] / 2.0 - csize - csize / 4.0
    posx2 = im_size[1] / 2.0 + csize / 4.0 - 1 / ppd
    posy1 = im_size[0] / 2.0 - csize - csize / 4.0
    posy2 = im_size[0] / 2.0 + csize / 4.0 - 1 / ppd

    stim1 = illusions.todorovic.todorovic_in(
        im_size=im_size,
        ppd=ppd,
        target_size=(tsize, tsize),
        target_pos=tpos,
        covers_height=csize,
        covers_width=csize,
        covers_posx=(posx1, posx2, posx1, posx2),
        covers_posy=(posy1, posy2, posy2, posy1),
        vback=1.0,
        vtarget=0.5,
        vcovers=0.0,
    )
    stim2 = illusions.todorovic.todorovic_in(
        im_size=im_size,
        ppd=ppd,
        target_size=(tsize, tsize),
        target_pos=tpos,
        covers_height=csize,
        covers_width=csize,
        covers_posx=(posx1, posx2, posx1, posx2),
        covers_posy=(posy1, posy2, posy2, posy1),
        vback=0.0,
        vtarget=0.5,
        vcovers=1.0,
    )

    # Increase target index of right stimulus half
    mask2 = stim2["mask"] + 1
    mask2[mask2 == 1] = 0

    # Stacking
    img = np.hstack([stim1["img"], stim2["img"]])
    mask = np.hstack([stim1["mask"], mask2])

    shape = degrees_to_pixels(VISEXTENT, ppd)
    img = pad_img_to_shape(img, shape, val=0.5)
    mask = pad_img_to_shape(mask, shape, val=0)
    return {"img": img, "mask": mask}


def todorovic_out(ppd=PPD):
    im_size = (13.0, 15.5)
    csize = 3.2
    tthick = csize / 2.0
    posx1 = im_size[1] / 2.0 - csize - tthick / 2.0
    posx2 = im_size[1] / 2.0 + tthick / 2.0 - 1 / ppd
    posy1 = im_size[0] / 2.0 - csize - tthick / 2.0
    posy2 = im_size[0] / 2.0 + tthick / 2.0 - 1 / ppd

    stim1 = illusions.todorovic.todorovic_out(
        im_size=im_size,
        ppd=ppd,
        target_size=(3.7,) * 4,
        target_thickness=tthick,
        covers_height=csize,
        covers_width=csize,
        covers_posx=(posx1, posx2, posx1, posx2),
        covers_posy=(posy1, posy2, posy2, posy1),
        vback=1.0,
        vtarget=0.5,
        vcovers=0.0,
    )
    stim2 = illusions.todorovic.todorovic_out(
        im_size=im_size,
        ppd=ppd,
        target_size=(3.7,) * 4,
        target_thickness=tthick,
        covers_height=csize,
        covers_width=csize,
        covers_posx=(posx1, posx2, posx1, posx2),
        covers_posy=(posy1, posy2, posy2, posy1),
        vback=0.0,
        vtarget=0.5,
        vcovers=1.0,
    )

    # Increase target index of right stimulus half
    mask2 = stim2["mask"] + 1
    mask2[mask2 == 1] = 0

    # Stacking
    img = np.hstack([stim1["img"], stim2["img"]])
    mask = np.hstack([stim1["mask"], mask2])

    shape = degrees_to_pixels(VISEXTENT, ppd)
    img = pad_img_to_shape(img, shape, val=0.5)
    mask = pad_img_to_shape(mask, shape, val=0)
    return {"img": img, "mask": mask}


def checkerboard_016(ppd=PPD):
    height_checks, width_checks = 40, 102
    check_height = 32.0 / 102.0
    board_shape = (height_checks, width_checks)

    check1, check2, target = 1, 0, 0.5
    target_height = height_checks // 2
    stim = illusions.checkerboard_sbc.checkerboard_contrast(
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
    stim = illusions.checkerboard_sbc.checkerboard_contrast(
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
    stim = illusions.checkerboard_sbc.checkerboard_contrast(
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


def corrugated_mondrian(ppd=PPD):
    depths = (0.0, -1.0, 0.0, 1.0, 0.0)
    v1, v2, v3, v4 = 0.0, 0.4, 0.75, 1.0
    values = (
        (v3, v2, v3, v2, v3),
        (v4, v3, v2, v3, v4),
        (v3, v2, v3, v2, v3),
        (v2, v1, v2, v1, v2),
        (v3, v2, v3, v2, v3),
    )
    target_idx = ((1, 2), (3, 2))

    stim = illusions.mondrians.corrugated_mondrians(
        ppd=PPD,
        widths=2.0,
        heights=2.0,
        depths=depths,
        target_idx=target_idx,
        values=values,
        vback=0.5,
    )

    shape = degrees_to_pixels(VISEXTENT, ppd)
    stim["img"] = pad_img_to_shape(stim["img"], shape, val=0.5)
    stim["mask"] = pad_img_to_shape(stim["mask"], shape, val=0)
    return stim


def benary_cross(ppd=PPD):
    vback = 1.0
    vtarget = 0.5
    padding = (0.0, 0.0, 4.0, 4.0)
    stim = illusions.benary_cross.benarys_cross(
        ppd=PPD,
        cross_size=(4.5, 4.5, 9.5, 9.5),
        cross_thickness=4.0,
        target_type=("t", "t"),
        target_ori=(45.0, 0.0),
        target_size=(2.5, 2.5),
        target_posx=(9.5 - np.sqrt(11.25), 13.5),
        target_posy=(4.5, 2.0),
        vback=vback,
        vcross=0.0,
        vtarget=vtarget,
    )

    shape = degrees_to_pixels(VISEXTENT, ppd)
    img = pad_img(stim["img"], padding, ppd, val=vback)
    img = pad_img_to_shape(img, shape, vtarget)
    mask = pad_img(stim["mask"], padding, ppd, val=0)
    mask = pad_img_to_shape(mask, shape, 0)
    return {"img": img, "mask": mask}


def todorovic_benary1_2(ppd=PPD):
    vback = 1.0
    vtarget = 0.5
    stim = illusions.benary_cross.todorovic_benary(
        ppd=PPD,
        L_size=(6.5, 6.5, 2.5, 28.5),
        target_size=(2.5, 2.5),
        target_type=("t", "t"),
        target_ori=(0.0, 180.0),
        target_posx=(2.5, 26.0),
        target_posy=(4.0, 6.5),
        vback=vback,
        vcross=0.0,
        vtarget=vtarget,
    )

    shape = degrees_to_pixels(VISEXTENT, ppd)
    img = pad_img_to_shape(stim["img"], shape, vtarget)
    mask = pad_img_to_shape(stim["mask"], shape, 0)
    return {"img": img, "mask": mask}


def todorovic_benary3_4(ppd=PPD):
    vback = 1.0
    vtarget = 0.5
    stim = illusions.benary_cross.todorovic_benary(
        ppd=PPD,
        L_size=(6.5, 6.5, 2.5, 28.5),
        target_size=(2.5, 2.5),
        target_type=("t", "t"),
        target_ori=(45.0, 225.0),
        target_posx=(9.5, 18.0),
        target_posy=(6.5, 6.5 - np.sqrt(11.25) / 2.0),
        vback=vback,
        vcross=0.0,
        vtarget=vtarget,
    )

    shape = degrees_to_pixels(VISEXTENT, ppd)
    img = pad_img_to_shape(stim["img"], shape, vtarget)
    mask = pad_img_to_shape(stim["mask"], shape, 0)
    return {"img": img, "mask": mask}


def todorovic_benary1_2_3_4(ppd=PPD):
    vback = 1.0
    vtarget = 0.5
    stim = illusions.benary_cross.todorovic_benary(
        ppd=PPD,
        L_size=(6.5, 6.5, 2.5, 28.5),
        target_size=(2.5, 2.5),
        target_type=("t", "t", "t", "t"),
        target_ori=(0.0, 45.0, 225.0, 180.0),
        target_posx=(2.5, 9.5, 18.0, 26.0),
        target_posy=(4.0, 6.5, 6.5 - np.sqrt(11.25) / 2.0, 6.5),
        vback=vback,
        vcross=0.0,
        vtarget=vtarget,
    )

    shape = degrees_to_pixels(VISEXTENT, ppd)
    img = pad_img_to_shape(stim["img"], shape, vtarget)
    mask = pad_img_to_shape(stim["mask"], shape, 0)
    return {"img": img, "mask": mask}


def bullseye_thin(ppd=PPD):
    v1, v2, v3 = 1.0, 0.5, 0.0
    shape_ind = degrees_to_pixels(np.array(VISEXTENT) / 2.0, ppd)
    shape_all = degrees_to_pixels(VISEXTENT, ppd)
    stim1 = illusions.bullseye.bullseye_stimulus(
        ppd=ppd,
        n_rings=8,
        ring_width=0.1,
        vring1=v1,
        vring2=v3,
        vtarget=v2,
    )
    stim2 = illusions.bullseye.bullseye_stimulus(
        ppd=ppd,
        n_rings=8,
        ring_width=0.1,
        vring1=v3,
        vring2=v1,
        vtarget=v2,
    )

    # Individual padding
    img1 = pad_img_to_shape(stim1["img"], shape_ind, v2)
    mask1 = pad_img_to_shape(stim1["mask"], shape_ind, 0)
    img2 = pad_img_to_shape(stim2["img"], shape_ind, v2)
    mask2 = pad_img_to_shape(stim2["mask"], shape_ind, 0)

    # Increase target index of right stimulus half
    mask2 = mask2 + 1
    mask2[mask2 == 1] = 0

    # Stacking
    img = np.hstack([img1, img2])
    mask = np.hstack([mask1, mask2])

    # Full padding
    img = pad_img_to_shape(img, shape_all, v2)
    mask = pad_img_to_shape(mask, shape_all, 0)
    return {"img": img, "mask": mask}


def bullseye_thick(ppd=PPD):
    v1, v2, v3 = 1.0, 0.5, 0.0
    shape_ind = degrees_to_pixels(np.array(VISEXTENT) / 2.0, ppd)
    shape_all = degrees_to_pixels(VISEXTENT, ppd)
    stim1 = illusions.bullseye.bullseye_stimulus(
        ppd=ppd,
        n_rings=6,
        ring_width=0.2,
        vring1=v1,
        vring2=v3,
        vtarget=v2,
    )
    stim2 = illusions.bullseye.bullseye_stimulus(
        ppd=ppd,
        n_rings=6,
        ring_width=0.2,
        vring1=v3,
        vring2=v1,
        vtarget=v2,
    )

    # Individual padding
    img1 = pad_img_to_shape(stim1["img"], shape_ind, v2)
    mask1 = pad_img_to_shape(stim1["mask"], shape_ind, 0)
    img2 = pad_img_to_shape(stim2["img"], shape_ind, v2)
    mask2 = pad_img_to_shape(stim2["mask"], shape_ind, 0)

    # Increase target index of right stimulus half
    mask2 = mask2 + 1
    mask2[mask2 == 1] = 0

    # Stacking
    img = np.hstack([img1, img2])
    mask = np.hstack([mask1, mask2])

    # Full padding
    img = pad_img_to_shape(img, shape_all, v2)
    mask = pad_img_to_shape(mask, shape_all, 0)
    return {"img": img, "mask": mask}


if __name__ == "__main__":
    from stimuli.utils import plot_stimuli

    stims = gen_all(skip=True)

    plot_stimuli(stims, mask=False)
