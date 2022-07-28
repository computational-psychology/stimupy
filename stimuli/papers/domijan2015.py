import numpy as np
from stimuli import illusions
from stimuli.utils import pad_img

__all__ = [
    "dungeon",
    "cube",
    "grating",
    "rings",
    "bullseye",
    "simultaneous_brightness_contrast",
    "white",
    "benary",
    "todorovic",
    "checkerboard_contrast_contrast",
    "checkerboard",
    "checkerboard_extended",
    "white_anderson",
    "white_howe",
    "white_yazdanbakhsh",
]

PPD = 1             # default: 1
HEIGHT_DEG = None   # default: None
PAD = True


def gen_all(ppd=PPD, skip=False):
    stims = {}  # save the stimulus-dicts in a larger dict, with name as key
    for stim_name in __all__:
        print(f"Generating domijan2015.{stim_name}")

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


def check_requirements(original_size_px, height_px, height_deg, ppd):
    if height_px is None and (height_deg is None or ppd is None):
        raise ValueError('You need to define two out of ppd, height_px and height_deg')
    if height_deg is None and (height_px is None or ppd is None):
        raise ValueError('You need to define two out of ppd, height_px and height_deg')

    if height_px is not None and ppd is not None:
        conversion_fac = height_px / original_size_px / ppd

    if height_deg is not None and ppd is not None:
        conversion_fac = height_deg / original_size_px

    if height_px is not None and height_deg is not None and ppd is not None:
        ppd_calc = int(np.round(height_px / height_deg))
        assert ppd_calc == ppd
        conversion_fac = height_px / original_size_px / ppd

    if height_px is not None and height_deg is not None and ppd is None:
        ppd = int(np.round(height_px / height_deg))
        conversion_fac = height_px / original_size_px / ppd
    return height_px, height_deg, ppd, conversion_fac


def dungeon(height_px=110, ppd=PPD, height_deg=HEIGHT_DEG):
    height_px, height_deg, ppd, conversion_fac = check_requirements(110, height_px, height_deg, ppd)

    n_cells = 5
    target_radius = 1.
    cell_size = 10. * conversion_fac
    v1, v2, v3 = 0., 0.5, 1.

    stim1 = illusions.dungeon.dungeon_illusion(
        ppd=ppd,
        n_cells=n_cells,
        target_radius=target_radius,
        cell_size=cell_size,
        vback=v1,
        vgrid=v3,
        vtarget=v2,
    )

    stim2 = illusions.dungeon.dungeon_illusion(
        ppd=ppd,
        n_cells=n_cells,
        target_radius=target_radius,
        cell_size=cell_size,
        vback=v3,
        vgrid=v1,
        vtarget=v2,
    )

    padding = np.array((9., 11., 9., 11.)) * conversion_fac
    stim1["img"] = pad_img(stim1["img"], padding, ppd, v1)
    stim1["mask"] = pad_img(stim1["mask"], padding, ppd, 0)
    stim2["img"] = pad_img(stim2["img"], padding, ppd, v3)
    stim2["mask"] = pad_img(stim2["mask"], padding, ppd, 0)

    img = np.hstack([stim1["img"], stim2["img"]])
    mask = np.hstack([stim1["mask"], stim2["mask"] * 2])
    return {"img": img, "mask": mask, "original_range": (1, 9)}


def cube(height_px=100, ppd=PPD, height_deg=HEIGHT_DEG):
    height_px, height_deg, ppd, conversion_fac = check_requirements(100, height_px, height_deg, ppd)

    v1, v2, v3 = 0., 0.5, 1.
    occlusion = np.array((7,)*4) * conversion_fac
    stim1 = illusions.cube.cube_illusion(
        ppd=ppd,
        n_cells=4,
        target_length=2,
        cell_long=15.*conversion_fac,
        cell_short=11.*conversion_fac,
        corner_cell_width=18.*conversion_fac,
        corner_cell_height=18.*conversion_fac,
        cell_spacing=5.*conversion_fac,
        occlusion_overlap=occlusion,
        vback=v1,
        vgrid=v3,
        vtarget=v2,
    )
    stim2 = illusions.cube.cube_illusion(
        ppd=ppd,
        n_cells=4,
        target_length=2,
        cell_long=15.*conversion_fac,
        cell_short=11.*conversion_fac,
        corner_cell_width=18.*conversion_fac,
        corner_cell_height=18.*conversion_fac,
        cell_spacing=5.*conversion_fac,
        occlusion_overlap=occlusion,
        vback=v3,
        vgrid=v1,
        vtarget=v2,
    )

    # Padding
    padding = np.array((9., 10., 9., 10.)) * conversion_fac
    img1 = pad_img(stim1["img"], padding, ppd, v1)
    mask1 = pad_img(stim1["mask"], padding, ppd, 0)
    img2 = pad_img(stim2["img"], padding, ppd, v3)
    mask2 = pad_img(stim2["mask"], padding, ppd, 0)

    # Increase target index of right stimulus half
    mask2 = mask2 + 1
    mask2[mask2 == 1] = 0

    # Stacking
    img_stacked = np.hstack([img1, img2])
    mask_stacked = np.hstack([mask1, mask2])
    return {"img": img_stacked, "mask": mask_stacked, "original_range": (1, 9)}


def grating(height_px=100, ppd=PPD, height_deg=HEIGHT_DEG):
    height_px, height_deg, ppd, conversion_fac = check_requirements(100, height_px, height_deg, ppd)

    v1, v2, v3 = 0., 0.5, 1.
    bar_shape = np.array((81, 10)) * conversion_fac
    stim1 = illusions.grating.grating_illusion(
        ppd=ppd,
        n_bars=9,
        target_indices=(4,),
        bar_shape=bar_shape,
        vbar1=v3,
        vbar2=v1,
        vtarget=v2,
    )
    stim2 = illusions.grating.grating_illusion(
        ppd=ppd,
        n_bars=9,
        target_indices=(4,),
        bar_shape=bar_shape,
        vbar1=v1,
        vbar2=v3,
        vtarget=v2,
    )

    # Padding
    padding = np.array((9., 10., 9., 11.)) * conversion_fac
    img1 = pad_img(stim1["img"], padding, ppd, v1)
    mask1 = pad_img(stim1["mask"], padding, ppd, 0)
    img2 = pad_img(stim2["img"], padding, ppd, v3)
    mask2 = pad_img(stim2["mask"], padding, ppd, 0)

    # Increase target index of right stimulus half
    mask2 = mask2 + 1
    mask2[mask2 == 1] = 0

    # Stacking
    img_stacked = np.hstack([img1, img2])
    mask_stacked = np.hstack([mask1, mask2])
    return {"img": img_stacked, "mask": mask_stacked, "original_range": (1, 9)}


def rings(height_px=100, ppd=PPD, height_deg=HEIGHT_DEG):
    height_px, height_deg, ppd, conversion_fac = check_requirements(100, height_px, height_deg, ppd)

    v1, v2, v3 = 0., 0.5, 1.
    stim1 = illusions.rings.ring_stimulus(
        ppd=ppd,
        n_rings=8,
        target_idx=4,
        ring_width=5.*conversion_fac,
        vring1=v1,
        vring2=v3,
        vtarget=v2,
    )
    stim2 = illusions.rings.ring_stimulus(
        ppd=ppd,
        n_rings=8,
        target_idx=3,
        ring_width=5.*conversion_fac,
        vring1=v1,
        vring2=v3,
        vtarget=v2,
    )

    # Padding
    padding = np.array((9., 10., 9., 10.)) * conversion_fac
    img1 = pad_img(stim1["img"], padding, ppd, v1)
    mask1 = pad_img(stim1["mask"], padding, ppd, 0)
    img2 = pad_img(stim2["img"], padding, ppd, v1)
    mask2 = pad_img(stim2["mask"], padding, ppd, 0)

    # Increase target index of right stimulus half
    mask2 = mask2 + 1
    mask2[mask2 == 1] = 0

    # Stacking
    img_stacked = np.hstack([img1, img2])
    mask_stacked = np.hstack([mask1, mask2])
    return {"img": img_stacked, "mask": mask_stacked, "original_range": (1, 9)}


def bullseye(height_px=100, ppd=PPD, height_deg=HEIGHT_DEG):
    height_px, height_deg, ppd, conversion_fac = check_requirements(100, height_px, height_deg, ppd)

    v1, v2, v3 = 0., 0.5, 1.
    stim1 = illusions.bullseye.bullseye_stimulus(
        ppd=ppd,
        n_rings=8,
        ring_width=5.*conversion_fac,
        vring1=v1,
        vring2=v3,
        vtarget=v2,
    )
    stim2 = illusions.bullseye.bullseye_stimulus(
        ppd=ppd,
        n_rings=8,
        ring_width=5.*conversion_fac,
        vring1=v3,
        vring2=v1,
        vtarget=v2,
    )

    # Padding
    padding = np.array((9., 10., 9., 10.)) * conversion_fac
    img1 = pad_img(stim1["img"], padding, ppd, v1)
    mask1 = pad_img(stim1["mask"], padding, ppd, 0)
    img2 = pad_img(stim2["img"], padding, ppd, v1)
    mask2 = pad_img(stim2["mask"], padding, ppd, 0)

    # Increase target index of right stimulus half
    mask2 = mask2 + 1
    mask2[mask2 == 1] = 0

    # Stacking
    img_stacked = np.hstack([img1, img2])
    mask_stacked = np.hstack([mask1, mask2])
    return {"img": img_stacked, "mask": mask_stacked, "original_range": (1, 9)}


def simultaneous_brightness_contrast(height_px=100, ppd=PPD, height_deg=HEIGHT_DEG):
    height_px, height_deg, ppd, conversion_fac = check_requirements(100, height_px, height_deg, ppd)
    im_size = np.array((100, 100)) * conversion_fac
    target_size = np.array((21, 21)) * conversion_fac
    target_pos = np.array((39, 39)) * conversion_fac

    stim1 = illusions.sbc.simultaneous_contrast(
        ppd=ppd,
        im_size=im_size,
        target_size=target_size,
        target_pos=target_pos,
        vback=1.,
        vtarget=0.5,
    )
    stim2 = illusions.sbc.simultaneous_contrast(
        ppd=ppd,
        im_size=im_size,
        target_size=target_size,
        target_pos=target_pos,
        vback=0.,
        vtarget=0.5,
    )

    # Increase target index of right stimulus half
    mask2 = stim2["mask"] + 1
    mask2[mask2 == 1] = 0

    # Stacking
    img_stacked = np.hstack([stim1["img"], stim2["img"]])
    mask_stacked = np.hstack([stim1["mask"], mask2])
    return {"img": img_stacked, "mask": mask_stacked, "original_range": (1, 9)}


def white(height_px=80, ppd=PPD, height_deg=HEIGHT_DEG, pad=PAD):
    height_px, height_deg, ppd, conversion_fac = check_requirements(80, height_px, height_deg, ppd)

    height = 80 * conversion_fac
    width = 80 * conversion_fac
    n_cycles = 4
    frequency = n_cycles / width
    stim = illusions.whites.white(
        shape=(height, width),
        ppd=ppd,
        frequency=frequency,
        high=1.,
        low=0.,
        target=0.5,
        period="ignore",
        start="low",
        target_indices=(3, 6),
        target_height=21*conversion_fac,
        targets_offset=0,
        orientation="horizontal",
    )

    if pad:
        padding = np.array((9., 11., 9., 11.)) * conversion_fac
        stim["img"] = pad_img(stim["img"], padding, ppd, val=0.5)
        stim["mask"] = pad_img(stim["mask"], padding, ppd, val=0)
    stim["original_range"] = (1, 9)
    return stim


def benary(height_px=100, ppd=PPD, height_deg=HEIGHT_DEG):
    height_px, height_deg, ppd, conversion_fac = check_requirements(100, height_px, height_deg, ppd)
    cross_size = np.array((30,)*4) * conversion_fac
    target_size = np.array((11.1, 11.1)) * conversion_fac  # TODO: fix rounding problem for different ppds
    target_posx = np.array((19, 70)) * conversion_fac
    target_posy = np.array((19, 30)) * conversion_fac

    stim = illusions.benary_cross.benarys_cross(
        ppd=ppd,
        cross_size=cross_size,
        cross_thickness=21*conversion_fac,
        target_type=("r", "r"),
        target_ori=(0.0, 0.0),
        target_size=target_size,
        target_posx=target_posx,
        target_posy=target_posy,
        vback=1.,
        vcross=0.,
        vtarget=0.5,
    )

    padding = np.array((9., 10., 9., 10.)) * conversion_fac
    stim["img"] = pad_img(stim["img"], padding, ppd, val=1.)
    stim["mask"] = pad_img(stim["mask"], padding, ppd, val=0)
    stim["original_range"] = (1, 9)
    return stim


def todorovic(height_px=100, ppd=PPD, height_deg=HEIGHT_DEG):
    height_px, height_deg, ppd, conversion_fac = check_requirements(100, height_px, height_deg, ppd)
    im_size = np.array((100, 100)) * conversion_fac
    target_size = np.array((41, 41)) * conversion_fac
    target_pos = np.array((29, 29)) * conversion_fac
    covers_posx = np.array((14, 54, 14, 54)) * conversion_fac
    covers_posy = np.array((14, 54, 54, 14)) * conversion_fac

    stim1 = illusions.todorovic.todorovic_in(
        im_size=im_size,
        ppd=ppd,
        target_size=target_size,
        target_pos=target_pos,
        covers_height=31*conversion_fac,
        covers_width=31*conversion_fac,
        covers_posx=covers_posx,
        covers_posy=covers_posy,
        vback=0.,
        vtarget=0.5,
        vcovers=1.,
    )
    stim2 = illusions.todorovic.todorovic_in(
        im_size=im_size,
        ppd=ppd,
        target_size=target_size,
        target_pos=target_pos,
        covers_height=31*conversion_fac,
        covers_width=31*conversion_fac,
        covers_posx=covers_posx,
        covers_posy=covers_posy,
        vback=1.,
        vtarget=0.5,
        vcovers=0.,
    )

    # Increase target index of right stimulus half
    mask2 = stim2["mask"] + 1
    mask2[mask2 == 1] = 0

    # Stacking
    img_stacked = np.hstack([stim1["img"], stim2["img"]])
    mask_stacked = np.hstack([stim1["mask"], mask2])
    return {"img": img_stacked, "mask": mask_stacked, "original_range": (1, 9)}


def checkerboard_contrast_contrast(height_px=80, ppd=PPD, height_deg=HEIGHT_DEG, pad=PAD):
    height_px, height_deg, ppd, conversion_fac = check_requirements(80, height_px, height_deg, ppd)

    stim1 = illusions.checkerboards.contrast_contrast(
        ppd=ppd,
        board_shape=(8, 8),
        check_size=10*conversion_fac,
        target_shape=(4, 4),
        vcheck1=0.,
        vcheck2=1.,
        tau=0.5,
        alpha=0.5,
    )

    stim2 = illusions.checkerboards.contrast_contrast(
        ppd=ppd,
        board_shape=(4, 4),
        check_size=10*conversion_fac,
        target_shape=(4, 4),
        vcheck1=0.,
        vcheck2=1.,
        tau=0.5,
        alpha=0.5,
    )

    # Increase target index of right stimulus half
    img2, mask2 = stim2["img"], stim2["mask"] + 1
    mask2[mask2 == 1] = 0

    # Padding
    padding = np.array((20., 20., 20., 20.)) * conversion_fac
    if PAD:
        padding1 = np.array((9., 11., 9., 11.)) * conversion_fac
        padding = np.array(padding1) + padding
        stim1['img'] = pad_img(stim1['img'], padding1, ppd=ppd, val=0.5)
        stim1['mask'] = pad_img(stim1['mask'], padding1, ppd=ppd, val=0)
    img2 = pad_img(img2, padding, ppd=ppd, val=0.5)
    mask2 = pad_img(mask2, padding, ppd=ppd, val=0)

    # Stacking
    img = np.hstack([stim1['img'], img2])
    mask = np.hstack([stim1['mask'], mask2])
    return {"img": img, "mask": mask, "original_range": (1, 9)}


def checkerboard(height_px=80, ppd=PPD, height_deg=HEIGHT_DEG, pad=PAD):
    height_px, height_deg, ppd, conversion_fac = check_requirements(80, height_px, height_deg, ppd)

    stim = illusions.checkerboards.contrast(
        ppd=ppd,
        board_shape=(8, 8),
        check_size=10*conversion_fac,
        target_indices=((3, 2), (5, 5)),
        extend_targets=False,
        vcheck1=0.,
        vcheck2=1.,
        vtarget=0.5,
    )

    if pad:
        padding = np.array((9., 11., 9., 11.)) * conversion_fac
        stim["img"] = pad_img(stim["img"], padding, ppd=ppd, val=0.5)
        stim["mask"] = pad_img(stim["mask"], padding, ppd=ppd, val=0)
    stim["original_range"] = (1, 9)
    return stim


def checkerboard_extended(height_px=80, ppd=PPD, height_deg=HEIGHT_DEG, pad=PAD):
    height_px, height_deg, ppd, conversion_fac = check_requirements(80, height_px, height_deg, ppd)

    stim = illusions.checkerboards.contrast(
        ppd=ppd,
        board_shape=(8, 8),
        check_size=10*conversion_fac,
        target_indices=((3, 2), (5, 5)),
        extend_targets=True,
        vcheck1=0.,
        vcheck2=1.,
        vtarget=0.5,
    )

    if pad:
        padding = np.array((9., 11., 9., 11.)) * conversion_fac
        stim["img"] = pad_img(stim["img"], padding, ppd=ppd, val=0.5)
        stim["mask"] = pad_img(stim["mask"], padding, ppd=ppd, val=0)
    stim["original_range"] = (1, 9)
    return stim


def white_yazdanbakhsh(height_px=80, ppd=PPD, height_deg=HEIGHT_DEG, pad=PAD):
    height_px, height_deg, ppd, conversion_fac = check_requirements(80, height_px, height_deg, ppd)

    height = 80 * conversion_fac
    width = 80 * conversion_fac
    n_cycles = 4
    frequency = n_cycles / width

    stim = illusions.whites.white_yazdanbakhsh(
        shape=(height, width),
        ppd=ppd,
        frequency=frequency,
        stripe_height=height / 10,
        target_height=height / 4,
        target_indices_top=(2,),
        target_ypos_top=(height / 2.7,),
        target_indices_bottom=(5,),
        target_ypos_bottom=(height / 2.7,),
        vbars=(0., 1.),
        vtarget=0.5,
        vtopstripe=1.,
        vbotstripe=0.,
    )

    if pad:
        padding = np.array((9., 11., 9., 11.)) * conversion_fac
        stim["img"] = pad_img(stim["img"], padding, ppd=ppd, val=0.5)
        stim["mask"] = pad_img(stim["mask"], padding, ppd=ppd, val=0)
    stim["original_range"] = (1, 9)
    return stim


def white_anderson(height_px=80, ppd=PPD, height_deg=HEIGHT_DEG, pad=PAD):
    height_px, height_deg, ppd, conversion_fac = check_requirements(80, height_px, height_deg, ppd)

    height = 100 * conversion_fac
    width = 100 * conversion_fac
    n_cycles = 5
    frequency = n_cycles / width

    stim = illusions.whites.white_anderson(
        shape=(height, width),
        ppd=ppd,
        frequency=frequency,
        stripe_height=height / 5,
        stripe_ypos=(height / 5, 3 * height / 5),
        target_height=height / 5,
        target_indices_top=(2,),
        target_offsets_top=(height / 10,),
        target_indices_bottom=(7,),
        target_offsets_bottom=(-height / 10,),
        vbars=(1., 0.),
        vtarget=0.5,
        vtopstripe=0.,
        vbotstripe=1.,
    )

    if pad:
        padding = np.array((9., 11., 9., 11.)) * conversion_fac
        stim["img"] = pad_img(stim["img"], padding, ppd=ppd, val=0.5)
        stim["mask"] = pad_img(stim["mask"], padding, ppd=ppd, val=0)
    stim["original_range"] = (1, 9)
    return stim


def white_howe(height_px=80, ppd=PPD, height_deg=HEIGHT_DEG, pad=PAD):
    height_px, height_deg, ppd, conversion_fac = check_requirements(80, height_px, height_deg, ppd)

    height = 100 * conversion_fac
    width = 100 * conversion_fac
    n_cycles = 5
    frequency = n_cycles / width

    stim = illusions.whites.white_howe(
        shape=(height, width),
        ppd=ppd,
        frequency=frequency,
        stripe_height=height / 5,
        stripe_ypos=(height / 5, 3 * height / 5),
        target_height=height / 5,
        target_indices_top=(2,),
        target_indices_bottom=(7,),
        vbars=(1., 0.),
        vtarget=0.5,
        vtopstripe=0.,
        vbotstripe=1.,
    )

    if pad:
        padding = np.array((9., 11., 9., 11.)) * conversion_fac
        stim["img"] = pad_img(stim["img"], padding, ppd=ppd, val=0.5)
        stim["mask"] = pad_img(stim["mask"], padding, ppd=ppd, val=0)
    stim["original_range"] = (1, 9)
    return stim


if __name__ == "__main__":
    from stimuli.utils import plot_stimuli

    stims = gen_all(skip=True)
    plot_stimuli(stims, mask=False)
