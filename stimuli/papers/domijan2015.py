import numpy as np
from stimuli import illusions
from stimuli.utils import pad_img
from stimuli.utils.resolution import resolve

## TODO: Add warning when stimulus shape or visual_size is different from what requested!
## TODO: Should shape / visual_size include padding or not?

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

PPD = 10    # default: 10
PAD = True  # default: True
SHAPES = {
    "dungeon": (110, 220),
    "cube": (100, 200),
    "grating": (100, 220),
    "rings": (100, 200),
    "bullseye": (100, 200),
    "simultaneous_brightness_contrast": (100, 200),
    "white": (80, 80),
    "benary": (100, 100),
    "todorovic": (100, 200),
    "checkerboard_contrast_contrast": (80, 160),
    "checkerboard": (80, 80),
    "checkerboard_extended": (80, 80),
    "white_anderson": (100, 100),
    "white_howe": (100, 100),
    "white_yazdanbakhsh": (80, 80),
    }
v1, v2, v3 = 0., 0.5, 1.


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


def resolve_input(inpt):
    if isinstance(inpt, (float, int)):
        inpt = (inpt, None)
    if inpt is None:
        inpt = (None, None)
    if len(inpt) > 2:
        raise ValueError("argument has too many dimensions")
    return inpt


def get_conversion_1d(original_shape, shape, visual_size, ppd):
    if shape is None and (visual_size is None or ppd is None):
        raise ValueError('You need to define two out of ppd, shape and visual_size')
    if visual_size is None and (shape is None or ppd is None):
        raise ValueError('You need to define two out of ppd, shape and visual_size')

    if shape is not None and ppd is not None:
        conversion_fac = shape / original_shape * PPD / ppd

    if visual_size is not None and ppd is not None:
        conversion_fac = visual_size / original_shape * PPD

    if shape is not None and visual_size is not None and ppd is not None:
        ppd_calc = int(np.round(shape / visual_size))
        assert ppd_calc == ppd
        conversion_fac = shape / original_shape * PPD / ppd

    if shape is not None and visual_size is not None and ppd is None:
        ppd = int(np.round(shape / visual_size))
        conversion_fac = shape / original_shape * PPD / ppd
    return conversion_fac / PPD


def get_conversion_2d(original_shape, shape, visual_size, ppd):
    try:
        c1 = get_conversion_1d(original_shape[0], shape[0], visual_size[0], ppd)
    except Exception:
        c1 = None

    try:
        c2 = get_conversion_1d(original_shape[1], shape[1], visual_size[1], ppd)
    except Exception:
        c2 = c1

    if c1 is None:
        c1 = c2
    if c1 != c2:
        raise ValueError("Requested shape/visual_size is impossible given the stimulus defaults. "
                         "Consider setting either the height or width to None")
    return c1


def dungeon(shape=SHAPES["dungeon"], ppd=PPD, visual_size=None):
    shape = resolve_input(shape)
    visual_size = resolve_input(visual_size)
    c = get_conversion_2d(SHAPES["dungeon"], shape, visual_size, ppd)
    shape, visual_size, ppd = resolve(None, np.array(SHAPES["dungeon"]) * c, ppd)
    ppd = ppd[0]

    params = {
        "ppd": ppd,
        "n_cells": 5,
        "target_radius": 1,
        "cell_size": 10. * c,
        }

    stim1 = illusions.dungeon.dungeon_illusion(
        **params,
        vback=v1,
        vgrid=v3,
        vtarget=v2,
    )

    stim2 = illusions.dungeon.dungeon_illusion(
        **params,
        vback=v3,
        vgrid=v1,
        vtarget=v2,
    )

    padding = np.array((9., 11., 9., 11.)) * c
    stim1["img"] = pad_img(stim1["img"], padding, ppd, v1)
    stim1["mask"] = pad_img(stim1["mask"], padding, ppd, 0)
    stim2["img"] = pad_img(stim2["img"], padding, ppd, v3)
    stim2["mask"] = pad_img(stim2["mask"], padding, ppd, 0)

    # Stacking
    img = np.hstack([stim1["img"], stim2["img"]])
    mask = np.hstack([stim1["mask"], stim2["mask"] * 2])

    params.update(original_shape=SHAPES["dungeon"],
                  original_ppd=PPD,
                  original_visual_size=np.array(SHAPES["dungeon"])/PPD,
                  original_range=(1, 9),
                  intensity_range=(v1, v3),
                  visual_size=np.array(img.shape)/ppd,
                  shape=img.shape,
                  )
    return {"img": img, "mask": mask, **params}


def cube(shape=SHAPES["cube"], ppd=PPD, visual_size=None):
    shape = resolve_input(shape)
    visual_size = resolve_input(visual_size)
    c = get_conversion_2d(SHAPES["cube"], shape, visual_size, ppd)
    shape, visual_size, ppd = resolve(None, np.array(SHAPES["cube"]) * c, ppd)
    ppd = ppd[0]

    params = {
        "ppd": ppd,
        "n_cells": 4,
        "target_length": 2,
        "cell_long": 15. * c,
        "cell_short": 11. * c,
        "corner_cell_width": 18. * c,
        "corner_cell_height": 18. * c,
        "cell_spacing": 5. * c,
        "occlusion_overlap": np.array((7,)*4) * c,
        }

    stim1 = illusions.cube.cube_illusion(
        **params,
        vback=v1,
        vgrid=v3,
        vtarget=v2,
    )
    stim2 = illusions.cube.cube_illusion(
        **params,
        vback=v3,
        vgrid=v1,
        vtarget=v2,
    )

    # Padding
    padding = np.array((9., 10., 9., 10.)) * c
    img1 = pad_img(stim1["img"], padding, ppd, v1)
    mask1 = pad_img(stim1["mask"], padding, ppd, 0)
    img2 = pad_img(stim2["img"], padding, ppd, v3)
    mask2 = pad_img(stim2["mask"], padding, ppd, 0)

    # Increase target index of right stimulus half
    mask2 = mask2 + 1
    mask2[mask2 == 1] = 0

    # Stacking
    img = np.hstack([img1, img2])
    mask = np.hstack([mask1, mask2])

    params.update(original_shape=SHAPES["cube"],
                  original_ppd=PPD,
                  original_visual_size=np.array(SHAPES["cube"])/PPD,
                  original_range=(1, 9),
                  intensity_range=(v1, v3),
                  visual_size=np.array(img.shape)/ppd,
                  shape=img.shape,
                  )
    return {"img": img, "mask": mask, **params}


def grating(shape=SHAPES["grating"], ppd=PPD, visual_size=None):
    shape = resolve_input(shape)
    visual_size = resolve_input(visual_size)
    c = get_conversion_2d(SHAPES["grating"], shape, visual_size, ppd)
    shape, visual_size, ppd = resolve(None, np.array(SHAPES["grating"]) * c, ppd)
    ppd = ppd[0]

    params = {
        "ppd": ppd,
        "n_bars": 9,
        "target_indices": (4,),
        "bar_shape": (81*c, 10*c),
        }

    stim1 = illusions.grating.grating_illusion(
        **params,
        vbar1=v3,
        vbar2=v1,
        vtarget=v2,
    )
    stim2 = illusions.grating.grating_illusion(
        **params,
        vbar1=v1,
        vbar2=v3,
        vtarget=v2,
    )

    # Padding
    padding = np.array((9., 10., 9., 11.)) * c
    img1 = pad_img(stim1["img"], padding, ppd, v1)
    mask1 = pad_img(stim1["mask"], padding, ppd, 0)
    img2 = pad_img(stim2["img"], padding, ppd, v3)
    mask2 = pad_img(stim2["mask"], padding, ppd, 0)

    # Increase target index of right stimulus half
    mask2 = mask2 + 1
    mask2[mask2 == 1] = 0

    # Stacking
    img = np.hstack([img1, img2])
    mask = np.hstack([mask1, mask2])

    params.update(original_shape=SHAPES["grating"],
                  original_ppd=PPD,
                  original_visual_size=np.array(SHAPES["grating"])/PPD,
                  original_range=(1, 9),
                  intensity_range=(v1, v3),
                  visual_size=np.array(img.shape)/ppd,
                  shape=img.shape,
                  )
    return {"img": img, "mask": mask, **params}


def rings(shape=SHAPES["rings"], ppd=PPD, visual_size=None):
    shape = resolve_input(shape)
    visual_size = resolve_input(visual_size)
    c = get_conversion_2d(SHAPES["rings"], shape, visual_size, ppd)
    shape, visual_size, ppd = resolve(None, np.array(SHAPES["rings"]) * c, ppd)
    ppd = ppd[0]

    params = {
        "ppd": ppd,
        "n_rings": 8,
        "ring_width": 5. * c,
        }

    stim1 = illusions.rings.ring_stimulus(
        **params,
        target_idx=4,
        vring1=v1,
        vring2=v3,
        vtarget=v2,
    )
    stim2 = illusions.rings.ring_stimulus(
        **params,
        target_idx=3,
        vring1=v1,
        vring2=v3,
        vtarget=v2,
    )

    # Padding
    padding = np.array((9., 10., 9., 10.)) * c
    img1 = pad_img(stim1["img"], padding, ppd, v1)
    mask1 = pad_img(stim1["mask"], padding, ppd, 0)
    img2 = pad_img(stim2["img"], padding, ppd, v1)
    mask2 = pad_img(stim2["mask"], padding, ppd, 0)

    # Increase target index of right stimulus half
    mask2 = mask2 + 1
    mask2[mask2 == 1] = 0

    # Stacking
    img = np.hstack([img1, img2])
    mask = np.hstack([mask1, mask2])

    params.update(original_shape=SHAPES["rings"],
                  original_ppd=PPD,
                  original_visual_size=np.array(SHAPES["rings"])/PPD,
                  original_range=(1, 9),
                  intensity_range=(v1, v3),
                  visual_size=np.array(img.shape)/ppd,
                  shape=img.shape,
                  target_idx_left=4,
                  target_idx_right=3,
                  )
    return {"img": img, "mask": mask, **params}


def bullseye(shape=SHAPES["bullseye"], ppd=PPD, visual_size=None):
    shape = resolve_input(shape)
    visual_size = resolve_input(visual_size)
    c = get_conversion_2d(SHAPES["bullseye"], shape, visual_size, ppd)
    shape, visual_size, ppd = resolve(None, np.array(SHAPES["bullseye"]) * c, ppd)
    ppd = ppd[0]

    params = {
        "ppd": ppd,
        "n_rings": 8,
        "ring_width": 5. * c,
        }

    stim1 = illusions.bullseye.bullseye_stimulus(
        **params,
        vring1=v1,
        vring2=v3,
        vtarget=v2,
    )
    stim2 = illusions.bullseye.bullseye_stimulus(
        **params,
        vring1=v3,
        vring2=v1,
        vtarget=v2,
    )

    # Padding
    padding = np.array((9., 10., 9., 10.)) * c
    img1 = pad_img(stim1["img"], padding, ppd, v1)
    mask1 = pad_img(stim1["mask"], padding, ppd, 0)
    img2 = pad_img(stim2["img"], padding, ppd, v1)
    mask2 = pad_img(stim2["mask"], padding, ppd, 0)

    # Increase target index of right stimulus half
    mask2 = mask2 + 1
    mask2[mask2 == 1] = 0

    # Stacking
    img = np.hstack([img1, img2])
    mask = np.hstack([mask1, mask2])

    params.update(original_shape=SHAPES["bullseye"],
                  original_ppd=PPD,
                  original_visual_size=np.array(SHAPES["bullseye"])/PPD,
                  original_range=(1, 9),
                  intensity_range=(v1, v3),
                  visual_size=np.array(img.shape)/ppd,
                  shape=img.shape,
                  )
    return {"img": img, "mask": mask, **params}


def simultaneous_brightness_contrast(shape=SHAPES["simultaneous_brightness_contrast"],
                                     ppd=PPD,
                                     visual_size=None):
    shape = resolve_input(shape)
    visual_size = resolve_input(visual_size)
    c = get_conversion_2d(SHAPES["simultaneous_brightness_contrast"], shape, visual_size, ppd)
    shape, visual_size, ppd = resolve(None,
                                      np.array(SHAPES["simultaneous_brightness_contrast"]) * c,
                                      ppd)
    ppd = ppd[0]

    params = {
        "shape": visual_size[0],
        "ppd": ppd,
        "target_size": (21*c, 21*c),
        "target_pos": (39*c, 39*c),
        }

    stim1 = illusions.sbc.simultaneous_contrast_generalized(
        **params,
        vback=v3,
        vtarget=v2,
    )
    stim2 = illusions.sbc.simultaneous_contrast_generalized(
        **params,
        vback=v1,
        vtarget=v2,
    )

    # Increase target index of right stimulus half
    mask2 = stim2["mask"] + 1
    mask2[mask2 == 1] = 0

    # Stacking
    img = np.hstack([stim1["img"], stim2["img"]])
    mask = np.hstack([stim1["mask"], mask2])

    params.update(original_shape=SHAPES["simultaneous_brightness_contrast"],
                  original_ppd=PPD,
                  original_visual_size=np.array(SHAPES["simultaneous_brightness_contrast"])/PPD,
                  original_range=(1, 9),
                  intensity_range=(v1, v3),
                  visual_size=np.array(img.shape)/ppd,
                  shape=img.shape,
                  )
    return {"img": img, "mask": mask, **params}


def white(shape=SHAPES["white"], ppd=PPD, visual_size=None, pad=PAD):
    shape = resolve_input(shape)
    visual_size = resolve_input(visual_size)
    c = get_conversion_2d(SHAPES["white"], shape, visual_size, ppd)
    shape, visual_size, ppd = resolve(None, np.array(SHAPES["white"]) * c, ppd)
    ppd = ppd[0]

    params = {
        "shape": visual_size,
        "ppd": ppd,
        "grating_frequency": 4 / visual_size[1],
        "target_indices": (2, 5),
        "target_size": 21*c,
        "period": "full",
        }

    stim = illusions.whites.white(
        **params,
        vbars=(v1, v3),
        vtarget=v2,
    )

    if pad:
        padding = np.array((9., 11., 9., 11.)) * c
        stim["img"] = pad_img(stim["img"], padding, ppd, val=v2)
        stim["mask"] = pad_img(stim["mask"], padding, ppd, val=0)
        params["padding"] = padding

    params.update(original_shape=SHAPES["white"],
                  original_ppd=PPD,
                  original_visual_size=np.array(SHAPES["white"])/PPD,
                  original_range=(1, 9),
                  intensity_range=(v1, v3),
                  visual_size=np.array(stim["img"].shape)/ppd,
                  shape=stim["img"].shape,
                  )
    return {**stim, **params}


def benary(shape=SHAPES["benary"], ppd=PPD, visual_size=None):
    shape = resolve_input(shape)
    visual_size = resolve_input(visual_size)
    c = get_conversion_2d(SHAPES["benary"], shape, visual_size, ppd)
    shape, visual_size, ppd = resolve(None, np.array(SHAPES["benary"]) * c, ppd)
    ppd = ppd[0]

    params = {
        "shape": 81*c,
        "ppd": ppd,
        "cross_thickness": 21*c,
        "target_size": 11*c,
        }

    stim = illusions.benary_cross.benarys_cross_rectangles(
        **params,
        vback=v3,
        vcross=v1,
        vtarget=v2,
    )

    # Padding
    padding = np.array((9, 10., 9, 10.)) * c
    stim["img"] = pad_img(stim["img"], padding, ppd, val=1.)
    stim["mask"] = pad_img(stim["mask"], padding, ppd, val=0)

    params.update(original_shape=SHAPES["benary"],
                  original_ppd=PPD,
                  original_visual_size=np.array(SHAPES["benary"])/PPD,
                  original_range=(1, 9),
                  intensity_range=(v1, v3),
                  visual_size=np.array(stim["img"].shape)/ppd,
                  shape=stim["img"].shape,
                  )
    return {**stim, **params}


def todorovic(shape=SHAPES["todorovic"], ppd=PPD, visual_size=None):
    # Note: Compared to original, targets are moved by one pixel
    shape = resolve_input(shape)
    visual_size = resolve_input(visual_size)
    c = get_conversion_2d(SHAPES["todorovic"], shape, visual_size, ppd)
    shape, visual_size, ppd = resolve(None, np.array(SHAPES["todorovic"]) * c, ppd)
    ppd = ppd[0]

    params = {
        "shape": visual_size[0],
        "ppd": ppd,
        "target_size": 41*c,
        "covers_size": 31*c,
        "covers_offset": 20*c,
        }

    stim1 = illusions.todorovic.todorovic_rectangle(
        **params,
        vback=0.,
        vtarget=0.5,
        vcovers=1.,
    )
    stim2 = illusions.todorovic.todorovic_rectangle(
        **params,
        vback=1.,
        vtarget=0.5,
        vcovers=0.,
    )

    # Increase target index of right stimulus half
    mask2 = stim2["mask"] + 1
    mask2[mask2 == 1] = 0

    # Stacking
    img = np.hstack([stim1["img"], stim2["img"]])
    mask = np.hstack([stim1["mask"], mask2])

    params.update(original_shape=SHAPES["todorovic"],
                  original_ppd=PPD,
                  original_visual_size=np.array(SHAPES["todorovic"])/PPD,
                  original_range=(1, 9),
                  intensity_range=(v1, v3),
                  visual_size=np.array(img.shape)/ppd,
                  shape=img.shape,
                  )
    return {"img": img, "mask": mask, **params}


def checkerboard_contrast_contrast(shape=SHAPES["checkerboard_contrast_contrast"],
                                   ppd=PPD, visual_size=None, pad=PAD):
    shape = resolve_input(shape)
    visual_size = resolve_input(visual_size)
    c = get_conversion_2d(SHAPES["checkerboard_contrast_contrast"], shape, visual_size, ppd)
    shape, visual_size, ppd = resolve(None,
                                      np.array(SHAPES["checkerboard_contrast_contrast"]) * c,
                                      ppd)
    ppd = ppd[0]

    params = {
        "ppd": ppd,
        "check_size": 10*c,
        "target_shape": (4, 4),
        "tau": 0.5,
        "alpha": 0.5,
        }

    stim1 = illusions.checkerboards.contrast_contrast(
        **params,
        board_shape=(8, 8),
        vcheck1=v1,
        vcheck2=v3,
    )

    stim2 = illusions.checkerboards.contrast_contrast(
        **params,
        board_shape=(4, 4),
        vcheck1=v1,
        vcheck2=v3,
    )

    # Increase target index of right stimulus half
    img2, mask2 = stim2["img"], stim2["mask"] + 1
    mask2[mask2 == 1] = 0

    # Padding
    padding = np.array((20., 20., 20., 20.)) * c
    if pad:
        padding1 = np.array((9., 11., 9., 11.)) * c
        padding = np.array(padding1) + padding
        stim1['img'] = pad_img(stim1['img'], padding1, ppd=ppd, val=v2)
        stim1['mask'] = pad_img(stim1['mask'], padding1, ppd=ppd, val=0)
        params["padding"] = padding1
    img2 = pad_img(img2, padding, ppd=ppd, val=v2)
    mask2 = pad_img(mask2, padding, ppd=ppd, val=0)

    # Stacking
    img = np.hstack([stim1['img'], img2])
    mask = np.hstack([stim1['mask'], mask2])

    params.update(original_shape=SHAPES["checkerboard_contrast_contrast"],
                  original_ppd=PPD,
                  original_visual_size=np.array(SHAPES["checkerboard_contrast_contrast"])/PPD,
                  original_range=(1, 9),
                  intensity_range=(v1, v3),
                  visual_size=np.array(img.shape)/ppd,
                  shape=img.shape,
                  board_shape_left=(8, 8),
                  board_shape_right=(4, 4),
                  )
    return {"img": img, "mask": mask, **params}


def checkerboard(shape=SHAPES["checkerboard"], ppd=PPD, visual_size=None, pad=PAD):
    shape = resolve_input(shape)
    visual_size = resolve_input(visual_size)
    c = get_conversion_2d(SHAPES["checkerboard"], shape, visual_size, ppd)
    shape, visual_size, ppd = resolve(None, np.array(SHAPES["checkerboard"]) * c, ppd)
    ppd = ppd[0]

    params = {
        "ppd": ppd,
        "board_shape": (8, 8),
        "check_size": 10*c,
        "target_indices": ((3, 2), (5, 5)),
        "extend_targets": False,
        }

    stim = illusions.checkerboards.contrast(
        **params,
        vcheck1=v1,
        vcheck2=v3,
        vtarget=v2,
    )

    if pad:
        padding = np.array((9., 11., 9., 11.)) * c
        stim["img"] = pad_img(stim["img"], padding, ppd=ppd, val=v2)
        stim["mask"] = pad_img(stim["mask"], padding, ppd=ppd, val=0)
        params["padding"] = padding

    params.update(original_shape=SHAPES["checkerboard"],
                  original_ppd=PPD,
                  original_visual_size=np.array(SHAPES["checkerboard"])/PPD,
                  original_range=(1, 9),
                  intensity_range=(v1, v3),
                  visual_size=np.array(stim["img"].shape)/ppd,
                  shape=stim["img"].shape,
                  )
    return {**stim, **params}


def checkerboard_extended(shape=SHAPES["checkerboard_extended"], ppd=PPD, visual_size=None,
                          pad=PAD):
    shape = resolve_input(shape)
    visual_size = resolve_input(visual_size)
    c = get_conversion_2d(SHAPES["checkerboard_extended"], shape, visual_size, ppd)
    shape, visual_size, ppd = resolve(None, np.array(SHAPES["checkerboard_extended"]) * c, ppd)
    ppd = ppd[0]

    params = {
        "ppd": ppd,
        "board_shape": (8, 8),
        "check_size": 10*c,
        "target_indices": ((3, 2), (5, 5)),
        "extend_targets": True,
        }

    stim = illusions.checkerboards.contrast(
        **params,
        vcheck1=v1,
        vcheck2=v3,
        vtarget=v2,
    )

    if pad:
        padding = np.array((9., 11., 9., 11.)) * c
        stim["img"] = pad_img(stim["img"], padding, ppd=ppd, val=v2)
        stim["mask"] = pad_img(stim["mask"], padding, ppd=ppd, val=0)
        params["padding"] = padding

    params.update(original_shape=SHAPES["checkerboard_extended"],
                  original_ppd=PPD,
                  original_visual_size=np.array(SHAPES["checkerboard_extended"])/PPD,
                  original_range=(1, 9),
                  intensity_range=(v1, v3),
                  visual_size=np.array(stim["img"].shape)/ppd,
                  shape=stim["img"].shape,
                  )
    return {**stim, **params}


def white_anderson(shape=SHAPES["white_anderson"], ppd=PPD, visual_size=None, pad=PAD):
    shape = resolve_input(shape)
    visual_size = resolve_input(visual_size)
    c = get_conversion_2d(SHAPES["white_anderson"], shape, visual_size, ppd)
    shape, visual_size, ppd = resolve(None, np.array(SHAPES["white_anderson"]) * c, ppd)
    ppd = ppd[0]

    params = {
        "shape": visual_size,
        "ppd": ppd,
        "grating_frequency": 5. / visual_size[1],
        "target_indices_top": (2,),
        "target_indices_bottom": (7,),
        "target_center_offset": visual_size[0]/10.,
        "target_size": visual_size[0]/5.,
        "stripe_center_offset": visual_size[0]/5.,
        "stripe_size": visual_size[0]/5.,
        "period": "full",
        }

    stim = illusions.whites.white_anderson(
        **params,
        vbars=(v3, v1),
        vtarget=v2,
        vstripes=(v1, v3),
    )

    if pad:
        padding = np.array((9., 11., 9., 11.)) * c
        stim["img"] = pad_img(stim["img"], padding, ppd=ppd, val=v2)
        stim["mask"] = pad_img(stim["mask"], padding, ppd=ppd, val=0)
        params["padding"] = padding

    params.update(original_shape=SHAPES["white_anderson"],
                  original_ppd=PPD,
                  original_visual_size=np.array(SHAPES["white_anderson"])/PPD,
                  original_range=(1, 9),
                  intensity_range=(v1, v3),
                  visual_size=np.array(stim["img"].shape)/ppd,
                  shape=stim["img"].shape,
                  )
    return {**stim, **params}


def white_howe(shape=SHAPES["white_howe"], ppd=PPD, visual_size=None, pad=PAD):
    shape = resolve_input(shape)
    visual_size = resolve_input(visual_size)
    c = get_conversion_2d(SHAPES["white_howe"], shape, visual_size, ppd)
    shape, visual_size, ppd = resolve(None, np.array(SHAPES["white_howe"]) * c, ppd)
    ppd = ppd[0]

    params = {
        "shape": visual_size,
        "ppd": ppd,
        "grating_frequency": 5. / visual_size[1],
        "target_indices_top": (2,),
        "target_indices_bottom": (7,),
        "target_center_offset": visual_size[0]/5.,
        "target_size": visual_size[0]/5.,
        "period": "full",
        }

    stim = illusions.whites.white_howe(
        **params,
        vbars=(v3, v1),
        vtarget=v2,
        vstripes=(v1, v3),
    )

    if pad:
        padding = np.array((9., 11., 9., 11.)) * c
        stim["img"] = pad_img(stim["img"], padding, ppd=ppd, val=v2)
        stim["mask"] = pad_img(stim["mask"], padding, ppd=ppd, val=0)
        params["padding"] = padding

    params.update(original_shape=SHAPES["white_howe"],
                  original_ppd=PPD,
                  original_visual_size=np.array(SHAPES["white_howe"])/PPD,
                  original_range=(1, 9),
                  intensity_range=(v1, v3),
                  visual_size=np.array(stim["img"].shape)/ppd,
                  shape=stim["img"].shape,
                  )
    return {**stim, **params}


def white_yazdanbakhsh(shape=SHAPES["white_yazdanbakhsh"], ppd=PPD, visual_size=None, pad=PAD):
    shape = resolve_input(shape)
    visual_size = resolve_input(visual_size)
    c = get_conversion_2d(SHAPES["white_yazdanbakhsh"], shape, visual_size, ppd)
    shape, visual_size, ppd = resolve(None, np.array(SHAPES["white_yazdanbakhsh"]) * c, ppd)
    ppd = ppd[0]

    params = {
        "shape": visual_size,
        "ppd": ppd,
        "grating_frequency": 4. / visual_size[1],
        "target_indices_top": (2,),
        "target_indices_bottom": (5,),
        "target_center_offset": 0.,
        "target_size": visual_size[0]/4.,
        "gap_size": visual_size[0]/10.,
        "period": "full",
        }

    stim = illusions.whites.white_yazdanbakhsh(
        **params,
        vbars=(v1, v3),
        vtarget=v2,
        vstripes=(v3, v1),
    )

    if pad:
        padding = np.array((9., 11., 9., 11.)) * c
        stim["img"] = pad_img(stim["img"], padding, ppd=ppd, val=v2)
        stim["mask"] = pad_img(stim["mask"], padding, ppd=ppd, val=0)
        params["padding"] = padding

    params.update(original_shape=SHAPES["white_yazdanbakhsh"],
                  original_ppd=PPD,
                  original_visual_size=np.array(SHAPES["white_yazdanbakhsh"])/PPD,
                  original_range=(1, 9),
                  intensity_range=(v1, v3),
                  visual_size=np.array(stim["img"].shape)/ppd,
                  shape=stim["img"].shape,
                  )
    return {**stim, **params}


if __name__ == "__main__":
    from stimuli.utils import plot_stimuli

    stims = gen_all(skip=True)
    plot_stimuli(stims, mask=False)
