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
    "WE_radial_thin",
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


def gen_all(ppd=PPD, pad=True, skip=False):
    stims = {}  # save the stimulus-dicts in a larger dict, with name as key
    for stim_name in __all__:
        print(f"Generating RHS2007.{stim_name}")

        # Get a reference to the actual function
        func = globals()[stim_name]
        try:
            stim = func(ppd=ppd, pad=pad)

            # Accumulate
            stims[stim_name] = stim
        except NotImplementedError as e:
            if not skip:
                raise e
            # Skip stimuli that aren't implemented
            print("-- not implemented")
            pass

    return stims


def WE_thick(ppd=PPD, pad=True):
    height, width = 12.0, 16.0
    n_cycles = 4.0
    stim = illusions.whites.white(
        shape=(height, width),
        ppd=ppd,
        grating_frequency=n_cycles/width,
        vbars=(0., 1.),
        target_indices=(2, 5),
        target_size=4,
        period="ignore",
    )

    if pad:
        shape = degrees_to_pixels(VISEXTENT, ppd)
        stim["img"] = pad_img_to_shape(stim["img"], shape, val=0.5)
        stim["mask"] = pad_img_to_shape(stim["mask"], shape, val=0)

    return stim


def WE_thin_wide(ppd=PPD, pad=True):
    height, width = 12.0, 16.0
    n_cycles = 8.0
    stim = illusions.whites.white(
        shape=(height, width),
        ppd=ppd,
        grating_frequency=n_cycles/width,
        vbars=(1., 0.),
        target_indices=(3, 12),
        target_size=2,
        period="ignore",
    )

    if pad:
        shape = degrees_to_pixels(VISEXTENT, ppd)
        stim["img"] = pad_img_to_shape(stim["img"], shape, val=0.5)
        stim["mask"] = pad_img_to_shape(stim["mask"], shape, val=0)

    return stim


def WE_dual(ppd=PPD, pad=True):
    height, width = 6.0, 8.0
    n_cycles = 4.0

    stim1 = illusions.whites.white(
        shape=(height, width),
        ppd=ppd,
        grating_frequency=n_cycles/width,
        vbars=(0., 1.),
        target_indices=(2, 5),
        target_size=2,
        period="ignore",
    )

    stim2 = illusions.whites.white(
        shape=(height, width),
        ppd=ppd,
        grating_frequency=n_cycles/width,
        vbars=(0., 1.),
        target_indices=(2, 5),
        target_size=2,
        period="ignore",
    )
    stim2['img'] = np.rot90(stim2['img'], 3)
    stim2['mask'] = np.rot90(stim2['mask'], 3)

    if pad:
        shape = degrees_to_pixels(VISEXTENT, ppd) / (1, 2)
    else:
        shape = np.max([stim1["img"].shape, stim2["img"].shape], axis=1)
    stim1["img"] = pad_img_to_shape(stim1["img"], shape, val=0.5)
    stim1["mask"] = pad_img_to_shape(stim1["mask"], shape, val=0)
    stim2["img"] = pad_img_to_shape(stim2["img"], shape, val=0.5)
    stim2["mask"] = pad_img_to_shape(stim2["mask"], shape, val=0)

    stim = {
        "img": np.hstack((stim1["img"], stim2["img"])),
        "mask": np.hstack((stim1["mask"], stim2["mask"])),
    }

    return stim


def WE_anderson(ppd=PPD, pad=True):
    height, width = 16.0, 16.0
    n_cycles = 8.0
    stim = illusions.whites.white_anderson(
        shape=(height, width),
        ppd=ppd,
        grating_frequency=n_cycles/width,
        vbars=(0., 1.),
        vtarget=0.5,
        target_indices_top=(5,),
        target_indices_bottom=(10,),
        target_center_offset=height/10,
        target_size=height/5,
        vstripes=(0., 1.),
        stripe_center_offset=height/5,
        stripe_size=height/5,
        period="ignore",
    )

    if pad:
        shape = degrees_to_pixels(VISEXTENT, ppd)
        stim["img"] = pad_img_to_shape(stim["img"], shape, val=0.5)
        stim["mask"] = pad_img_to_shape(stim["mask"], shape, val=0)

    return stim


def WE_howe(ppd=PPD, pad=True):
    height, width = 16.0, 16.0
    n_cycles = 8.0
    stim = illusions.whites.white_howe(
        shape=(height, width),
        ppd=ppd,
        grating_frequency=n_cycles/width,
        vbars=(0., 1.),
        vtarget=0.5,
        target_indices_top=(5,),
        target_indices_bottom=(10,),
        target_center_offset=height/5,
        target_size=height/5,
        vstripes=(0., 1.),
        period="ignore",
    )

    if pad:
        shape = degrees_to_pixels(VISEXTENT, ppd)
        stim["img"] = pad_img_to_shape(stim["img"], shape, val=0.5)
        stim["mask"] = pad_img_to_shape(stim["mask"], shape, val=0)

    return stim


def WE_zigzag(ppd=PPD, pad=True):
    i1, i2 = -1, 0
    stim = illusions.wedding_cake.wedding_cake_stimulus(
        ppd=PPD,
        L_size=(4.0, 5, 1.0),
        L_repeats=(3.5, 3.4),
        target_height=2.0,
        target_idx_v1=((i1, -1), (i1, -0), (i1, 1), (i1, 2)),
        target_idx_v2=((i2, -1), (i2, -0), (i2, 1), (i2, -2)),
        v1=0.0,
        v2=1.0,
        vtarget=0.5,
    )

    if pad:
        shape = degrees_to_pixels(VISEXTENT, ppd)
        stim["img"] = pad_img_to_shape(stim["img"], shape, val=0.5)
        stim["mask"] = pad_img_to_shape(stim["mask"], shape, val=0)

    return stim


def WE_radial_thick_small(ppd=PPD, pad=True):
    n_cycles = 7
    stim = illusions.circular.radial_white(
        shape=(16, 16),
        ppd=ppd,
        n_segments=n_cycles*2,
        rotate=np.pi/n_cycles/2,
        target_indices=(0, n_cycles),
        target_width=4.,
        target_center=4.5,
        vslices=(1., 0.),
        vbackground=0.5,
        vtarget=0.5,
    )

    if pad:
        shape = degrees_to_pixels(VISEXTENT, ppd)
        stim["img"] = pad_img_to_shape(stim["img"], shape, val=0.5)
        stim["mask"] = pad_img_to_shape(stim["mask"], shape, val=0)

    return stim


def WE_radial_thick(ppd=PPD, pad=True):
    n_cycles = 9
    stim = illusions.circular.radial_white(
        shape=(24, 24),
        ppd=ppd,
        n_segments=n_cycles*2,
        rotate=np.pi/n_cycles/2,
        target_indices=(0, n_cycles),
        target_width=4.,
        target_center=6.,
        vslices=(1., 0.),
        vbackground=0.5,
        vtarget=0.5,
    )

    if pad:
        shape = degrees_to_pixels(VISEXTENT, ppd)
        stim["img"] = pad_img_to_shape(stim["img"], shape, val=0.5)
        stim["mask"] = pad_img_to_shape(stim["mask"], shape, val=0)

    return stim


def WE_radial_thin_small(ppd=PPD, pad=True):
    n_cycles = 13
    stim = illusions.circular.radial_white(
        shape=(16, 16),
        ppd=ppd,
        n_segments=n_cycles*2,
        rotate=np.pi/n_cycles/2,
        target_indices=(0, n_cycles),
        target_width=2.,
        target_center=4.,
        vslices=(1., 0.),
        vbackground=0.5,
        vtarget=0.5,
    )

    if pad:
        shape = degrees_to_pixels(VISEXTENT, ppd)
        stim["img"] = pad_img_to_shape(stim["img"], shape, val=0.5)
        stim["mask"] = pad_img_to_shape(stim["mask"], shape, val=0)

    return stim


def WE_radial_thin(ppd=PPD, pad=True):
    n_cycles = 21
    stim = illusions.circular.radial_white(
        shape=(24, 24),
        ppd=ppd,
        n_segments=n_cycles*2,
        rotate=np.pi/n_cycles/2,
        target_indices=(0, n_cycles),
        target_width=2.,
        target_center=6.,
        vslices=(1., 0.),
        vbackground=0.5,
        vtarget=0.5,
    )

    if pad:
        shape = degrees_to_pixels(VISEXTENT, ppd)
        stim["img"] = pad_img_to_shape(stim["img"], shape, val=0.5)
        stim["mask"] = pad_img_to_shape(stim["mask"], shape, val=0)

    return stim


def WE_circular1(ppd=PPD, pad=True):
    height, width = 16., 16.
    stim1 = illusions.circular.circular_white(
        shape=(height, width),
        ppd=ppd,
        frequency=8/height,
        vdiscs=(1., 0.),
        vtarget=0.5,
        vbackground=0.5,
        target_indices=4,
    )

    stim2 = illusions.circular.circular_white(
        shape=(height, width),
        ppd=ppd,
        frequency=8/height,
        vdiscs=(0., 1.),
        vtarget=0.5,
        vbackground=0.5,
        target_indices=4,
    )
    stim2["mask"] *= 2

    stim = {
        "img": np.hstack((stim1["img"], stim2["img"])),
        "mask": np.hstack((stim1["mask"], stim2["mask"])),
    }

    if pad:
        shape = degrees_to_pixels(VISEXTENT, ppd)
        stim["img"] = pad_img_to_shape(stim["img"], shape, val=0.5)
        stim["mask"] = pad_img_to_shape(stim["mask"], shape, val=0)
    return stim


def WE_circular05(ppd=PPD, pad=True):
    height, width = 16., 16.
    stim1 = illusions.circular.circular_white(
        shape=(height, width),
        ppd=ppd,
        frequency=16/height,
        vdiscs=(1., 0.),
        vtarget=0.5,
        vbackground=0.5,
        target_indices=10,
    )

    stim2 = illusions.circular.circular_white(
        shape=(height, width),
        ppd=ppd,
        frequency=16/height,
        vdiscs=(0., 1.),
        vtarget=0.5,
        vbackground=0.5,
        target_indices=(10,),
    )
    stim2["mask"] *= 2

    stim = {
        "img": np.hstack((stim1["img"], stim2["img"])),
        "mask": np.hstack((stim1["mask"], stim2["mask"])),
    }

    if pad:
        shape = degrees_to_pixels(VISEXTENT, ppd)
        stim["img"] = pad_img_to_shape(stim["img"], shape, val=0.5)
        stim["mask"] = pad_img_to_shape(stim["mask"], shape, val=0)
    return stim


def WE_circular025(ppd=PPD, pad=True):
    height, width = 16., 16.
    stim1 = illusions.circular.circular_white(
        shape=(height, width),
        ppd=ppd,
        frequency=32/height,
        vdiscs=(1., 0.),
        vtarget=0.5,
        vbackground=0.5,
        target_indices=(22,),
    )

    stim2 = illusions.circular.circular_white(
        shape=(height, width),
        ppd=ppd,
        frequency=32/height,
        vdiscs=(0., 1.),
        vtarget=0.5,
        vbackground=0.5,
        target_indices=(22,),
    )
    stim2["mask"] *= 2

    stim = {
        "img": np.hstack((stim1["img"], stim2["img"])),
        "mask": np.hstack((stim1["mask"], stim2["mask"])),
    }

    if pad:
        shape = degrees_to_pixels(VISEXTENT, ppd)
        stim["img"] = pad_img_to_shape(stim["img"], shape, val=0.5)
        stim["mask"] = pad_img_to_shape(stim["mask"], shape, val=0)
    return stim


def grating_induction(ppd=PPD, pad=True):
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

    if pad:
        shape = degrees_to_pixels(VISEXTENT, ppd)
        stim["img"] = pad_img_to_shape(stim["img"], shape, val=0.5)
        stim["mask"] = pad_img_to_shape(stim["mask"], shape, val=0)

    return stim


def sbc_large(ppd=PPD, pad=True):
    im_size = (13.0, 15.5)
    stim1 = illusions.sbc.simultaneous_contrast(
        shape=im_size,
        ppd=ppd,
        target_size=3.,
        vback=0.0,
        vtarget=0.5,
    )
    stim2 = illusions.sbc.simultaneous_contrast(
        shape=im_size,
        ppd=ppd,
        target_size=3.,
        vback=1.0,
        vtarget=0.5,
    )

    # Increase target index of right stimulus half
    mask2 = stim2["mask"] + 1
    mask2[mask2 == 1] = 0

    # Stacking
    img = np.hstack([stim1["img"], stim2["img"]])
    mask = np.hstack([stim1["mask"], mask2])

    if pad:
        shape = degrees_to_pixels(VISEXTENT, ppd)
        img = pad_img_to_shape(img, shape, val=0.5)
        mask = pad_img_to_shape(mask, shape, val=0)

    return {"img": img, "mask": mask}


def sbc_small(ppd=PPD, pad=True):
    im_size = (13.0, 15.5)
    stim1 = illusions.sbc.simultaneous_contrast(
        shape=im_size,
        ppd=ppd,
        target_size=1.,
        vback=0.0,
        vtarget=0.5,
    )
    stim2 = illusions.sbc.simultaneous_contrast(
        shape=im_size,
        ppd=ppd,
        target_size=1.,
        vback=1.0,
        vtarget=0.5,
    )

    # Increase target index of right stimulus half
    mask2 = stim2["mask"] + 1
    mask2[mask2 == 1] = 0

    # Stacking
    img = np.hstack([stim1["img"], stim2["img"]])
    mask = np.hstack([stim1["mask"], mask2])

    if pad:
        shape = degrees_to_pixels(VISEXTENT, ppd)
        img = pad_img_to_shape(img, shape, val=0.5)
        mask = pad_img_to_shape(mask, shape, val=0)

    return {"img": img, "mask": mask}


def todorovic_equal(ppd=PPD, pad=True):
    stim1 = illusions.todorovic.todorovic_cross(
        shape=(13.0, 15.5),
        ppd=ppd,
        target_arms_size=3.2,
        target_thickness=1.6,
        covers_size=3.2,
        vback=1.0,
        vtarget=0.5,
        vcovers=0.0,
    )
    stim2 = illusions.todorovic.todorovic_cross(
        shape=(13.0, 15.5),
        ppd=ppd,
        target_arms_size=3.2,
        target_thickness=1.6,
        covers_size=3.2,
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

    if pad:
        shape = degrees_to_pixels(VISEXTENT, ppd)
        img = pad_img_to_shape(img, shape, val=0.5)
        mask = pad_img_to_shape(mask, shape, val=0)

    return {"img": img, "mask": mask}


def todorovic_in_large(ppd=PPD, pad=True):
    stim1 = illusions.todorovic.todorovic_rectangle(
        shape=(13.0, 15.5),
        ppd=ppd,
        target_size=5.3,
        covers_size=3.2,
        covers_offset=2.4,
        vback=1.0,
        vtarget=0.5,
        vcovers=0.0,
    )
    stim2 = illusions.todorovic.todorovic_rectangle(
        shape=(13.0, 15.5),
        ppd=ppd,
        target_size=5.3,
        covers_size=3.2,
        covers_offset=2.4,
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

    if pad:
        shape = degrees_to_pixels(VISEXTENT, ppd)
        img = pad_img_to_shape(img, shape, val=0.5)
        mask = pad_img_to_shape(mask, shape, val=0)

    return {"img": img, "mask": mask}


def todorovic_in_small(ppd=PPD, pad=True):
    stim1 = illusions.todorovic.todorovic_cross(
        shape=(13.0, 15.5),
        ppd=ppd,
        target_arms_size=0.7,
        target_thickness=1.7,
        covers_size=3.2,
        vback=1.0,
        vtarget=0.5,
        vcovers=0.0,
    )
    stim2 = illusions.todorovic.todorovic_cross(
        shape=(13.0, 15.5),
        ppd=ppd,
        target_arms_size=0.7,
        target_thickness=1.7,
        covers_size=3.2,
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

    if pad:
        shape = degrees_to_pixels(VISEXTENT, ppd)
        img = pad_img_to_shape(img, shape, val=0.5)
        mask = pad_img_to_shape(mask, shape, val=0)
    return {"img": img, "mask": mask}


def todorovic_out(ppd=PPD, pad=True):
    stim1 = illusions.todorovic.todorovic_cross(
        shape=(13.0, 15.5),
        ppd=ppd,
        target_arms_size=3.7,
        target_thickness=1.6,
        covers_size=3.2,
        vback=1.0,
        vtarget=0.5,
        vcovers=0.0,
    )
    stim2 = illusions.todorovic.todorovic_cross(
        shape=(13.0, 15.5),
        ppd=ppd,
        target_arms_size=3.7,
        target_thickness=1.6,
        covers_size=3.2,
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

    if pad:
        shape = degrees_to_pixels(VISEXTENT, ppd)
        img = pad_img_to_shape(img, shape, val=0.5)
        mask = pad_img_to_shape(mask, shape, val=0)

    return {"img": img, "mask": mask}


def checkerboard_016(ppd=PPD, pad=True):
    nchecks_height, nchecks_width = 40, 102
    check_height = 0.156
    board_shape = (nchecks_height, nchecks_width)

    vcheck1, vcheck2, vtarget = 1, 0, 0.5
    target_posy = nchecks_height // 2
    stim = illusions.checkerboards.contrast(
        ppd=ppd,
        board_shape=board_shape,
        check_size=check_height,
        target_indices=((target_posy, 16), (target_posy, 85)),
        extend_targets=False,
        vcheck1=vcheck1,
        vcheck2=vcheck2,
        vtarget=vtarget,
    )

    if pad:
        shape = degrees_to_pixels(VISEXTENT, ppd)
        stim["img"] = pad_img_to_shape(stim["img"], shape, val=0.5)
        stim["mask"] = pad_img_to_shape(stim["mask"], shape, val=0)

    return stim


def checkerboard_0938(ppd=PPD, pad=True):
    nchecks_height, nchecks_width = 7, 25
    check_height = 0.938
    board_shape = (nchecks_height, nchecks_width)

    vcheck1, vcheck2, vtarget = 0, 1, 0.5
    target_posy = nchecks_height // 2
    stim = illusions.checkerboards.contrast(
        ppd=ppd,
        board_shape=board_shape,
        check_size=check_height,
        target_indices=((target_posy, 6), (target_posy, 17)),
        extend_targets=False,
        vcheck1=vcheck1,
        vcheck2=vcheck2,
        vtarget=vtarget,
    )

    if pad:
        shape = degrees_to_pixels(VISEXTENT, ppd)
        stim["img"] = pad_img_to_shape(stim["img"], shape, val=0.5)
        stim["mask"] = pad_img_to_shape(stim["mask"], shape, val=0)

    return stim


def checkerboard209(ppd=PPD, pad=True):
    nchecks_height, nchecks_width = 3, 10
    check_height = 2.09
    board_shape = (nchecks_height, nchecks_width)

    vcheck1, vcheck2, vtarget = 0, 1, 0.5
    target_posy = nchecks_height // 2
    stim = illusions.checkerboards.contrast(
        ppd=ppd,
        board_shape=board_shape,
        check_size=check_height,
        target_indices=((target_posy, 2), (target_posy, 7)),
        extend_targets=False,
        vcheck1=vcheck1,
        vcheck2=vcheck2,
        vtarget=vtarget,
    )

    if pad:
        shape = degrees_to_pixels(VISEXTENT, ppd)
        stim["img"] = pad_img_to_shape(stim["img"], shape, val=0.5)
        stim["mask"] = pad_img_to_shape(stim["mask"], shape, val=0)

    return stim


def corrugated_mondrian(ppd=PPD, pad=True):
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

    if pad:
        shape = degrees_to_pixels(VISEXTENT, ppd)
        stim["img"] = pad_img_to_shape(stim["img"], shape, val=0.5)
        stim["mask"] = pad_img_to_shape(stim["mask"], shape, val=0)

    return stim


def benary_cross2(ppd=PPD, pad=True):
    vback = 1.0
    vtarget = 0.5
    padding = (0.0, 0.0, 4.0, 4.0)
    stim = illusions.benary_cross.benarys_cross_generalized(
        shape=(13, 23),
        ppd=PPD,
        cross_thickness=4.0,
        target_type=("t", "t"),
        target_ori=(45.0, 0.0),
        target_size=(2.5, 2.5),
        target_posx=(9.5 - np.sqrt(12.5)+2/ppd, 13.5),
        target_posy=(4.5, 2.0),
        vback=vback,
        vcross=0.0,
        vtarget=vtarget,
    )

    if pad:
        shape = degrees_to_pixels(VISEXTENT, ppd)
        stim["img"] = pad_img(stim["img"], padding, ppd, val=vback)
        stim["img"] = pad_img_to_shape(stim["img"], shape, vtarget)
        stim["mask"] = pad_img(stim["mask"], padding, ppd, val=0)
        stim["mask"] = pad_img_to_shape(stim["mask"], shape, 0)

    return stim


def benary_cross(ppd=PPD, pad=True):
    vback = 1.0
    vtarget = 0.5
    padding = (0.0, 0.0, 4.0, 4.0)
    stim = illusions.benary_cross.benarys_cross_triangles(
        shape=(13, 23),
        ppd=PPD,
        cross_thickness=4.0,
        target_size=2.5,
        vback=vback,
        vcross=0.0,
        vtarget=vtarget,
    )
    stim['img'] = np.fliplr(stim['img'])
    stim['mask'] = np.fliplr(stim['mask'])
    stim['mask'][stim['mask'] != 0] = np.abs(stim['mask'][stim['mask'] != 0] - 3)

    if pad:
        shape = degrees_to_pixels(VISEXTENT, ppd)
        stim["img"] = pad_img(stim["img"], padding, ppd, val=vback)
        stim["img"] = pad_img_to_shape(stim["img"], shape, vtarget)
        stim["mask"] = pad_img(stim["mask"], padding, ppd, val=0)
        stim["mask"] = pad_img_to_shape(stim["mask"], shape, 0)

    return stim


def todorovic_benary1_2(ppd=PPD, pad=True):
    vback = 1.0
    vtarget = 0.5
    stim = illusions.benary_cross.todorovic_benary_generalized(
        shape=(13., 31.),
        ppd=PPD,
        L_width=2.5,
        target_size=(2.5, 2.5),
        target_type=("t", "t"),
        target_ori=(0.0, 180.0),
        target_posx=(2.5, 26.0),
        target_posy=(4.0, 6.5),
        vback=vback,
        vcross=0.0,
        vtarget=vtarget,
    )

    if pad:
        shape = degrees_to_pixels(VISEXTENT, ppd)
        stim["img"] = pad_img_to_shape(stim["img"], shape, vtarget)
        stim["mask"] = pad_img_to_shape(stim["mask"], shape, 0)

    return stim


def todorovic_benary3_4(ppd=PPD, pad=True):
    vback = 1.0
    vtarget = 0.5
    stim = illusions.benary_cross.todorovic_benary_generalized(
        shape=(13., 31.),
        ppd=PPD,
        L_width=2.5,
        target_size=(2.5, 2.5),
        target_type=("t", "t"),
        target_ori=(45.0, 225.0),
        target_posx=(9.5, 18.0),
        target_posy=(6.5, 6.5 - np.sqrt(12.5)/2.+1/ppd),
        vback=vback,
        vcross=0.0,
        vtarget=vtarget,
    )

    if pad:
        shape = degrees_to_pixels(VISEXTENT, ppd)
        stim["img"] = pad_img_to_shape(stim["img"], shape, vtarget)
        stim["mask"] = pad_img_to_shape(stim["mask"], shape, 0)

    return stim


def todorovic_benary1_2_3_4(ppd=PPD, pad=True):
    vback = 1.0
    vtarget = 0.5
    stim = illusions.benary_cross.todorovic_benary_generalized(
        shape=(13., 31.),
        ppd=PPD,
        L_width=2.5,
        target_size=(2.5, 2.5),
        target_type=("t", "t", "t", "t"),
        target_ori=(0.0, 45.0, 225.0, 180.0),
        target_posx=(2.5, 9.5, 18.0, 26.0),
        target_posy=(4.0, 6.5, 6.5 - np.sqrt(12.5)/2.+1/ppd, 6.5),
        vback=vback,
        vcross=0.0,
        vtarget=vtarget,
    )

    if pad:
        shape = degrees_to_pixels(VISEXTENT, ppd)
        stim["img"] = pad_img_to_shape(stim["img"], shape, vtarget)
        stim["mask"] = pad_img_to_shape(stim["mask"], shape, 0)

    return stim


def bullseye_thin(ppd=PPD, pad=True):
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
    if pad:
        stim1["img"] = pad_img_to_shape(stim1["img"], shape_ind, v2)
        stim1["mask"] = pad_img_to_shape(stim1["mask"], shape_ind, 0)
        stim2["img"] = pad_img_to_shape(stim2["img"], shape_ind, v2)
        stim2["mask"] = pad_img_to_shape(stim2["mask"], shape_ind, 0)

    # Increase target index of right stimulus half
    stim2["mask"] = stim2["mask"] + 1
    stim2["mask"][stim2["mask"] == 1] = 0

    # Stacking
    img = np.hstack([stim1["img"], stim2["img"]])
    mask = np.hstack([stim1["mask"], stim2["mask"]])

    # Full padding
    if pad:
        img = pad_img_to_shape(img, shape_all, v2)
        mask = pad_img_to_shape(mask, shape_all, 0)

    return {"img": img, "mask": mask}


def bullseye_thick(ppd=PPD, pad=True):
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
    if pad:
        stim1["img"] = pad_img_to_shape(stim1["img"], shape_ind, v2)
        stim1["mask"] = pad_img_to_shape(stim1["mask"], shape_ind, 0)
        stim2["img"] = pad_img_to_shape(stim2["img"], shape_ind, v2)
        stim2["mask"] = pad_img_to_shape(stim2["mask"], shape_ind, 0)

    # Increase target index of right stimulus half
    stim2["mask"] = stim2["mask"] + 1
    stim2["mask"][stim2["mask"] == 1] = 0

    # Stacking
    img = np.hstack([stim1["img"], stim2["img"]])
    mask = np.hstack([stim1["mask"], stim2["mask"]])

    # Full padding
    if pad:
        img = pad_img_to_shape(img, shape_all, v2)
        mask = pad_img_to_shape(mask, shape_all, 0)

    return {"img": img, "mask": mask}


if __name__ == "__main__":
    from stimuli.utils import plot_stimuli

    stims = gen_all(pad=True, skip=True)
    plot_stimuli(stims, mask=False)
