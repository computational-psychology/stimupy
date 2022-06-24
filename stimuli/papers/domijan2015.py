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

PPD = 10


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


def dungeon(ppd=PPD):
    return illusions.dungeon.dungeon_illusion(
        ppd=ppd,
        n_cells=5,
        target_radius=1,
        cell_size=1.0,
        padding=(0.9, 1.1, 0.9, 1.1),
        back=1.0,
        grid=9.0,
        target=5.0,
        double=True,
    )


def cube(ppd=PPD):
    return illusions.cube.cube_illusion(
        ppd=ppd,
        n_cells=4,
        target_length=2,
        cell_long=1.5,
        cell_short=1.1,
        corner_cell_width=1.8,
        corner_cell_height=1.8,
        cell_spacing=0.5,
        padding=(0.9, 1.0, 0.9, 1.0),
        occlusion_overlap=(0.7, 0.7, 0.7, 0.7),
        back=1.0,
        grid=9.0,
        target=5.0,
        double=True,
    )


def grating(ppd=PPD):
    return illusions.grating.grating_illusion(
        ppd=ppd,
        n_bars=5,
        target_length=1,
        bar_width=1.0,
        bar_height=8.1,
        padding=(0.9, 1.0, 0.9, 1.1),
        back=1,
        grid=9,
        target=5,
        double=True,
    )


def rings(ppd=PPD):
    v1, v2, v3 = 1.0, 5.0, 9.0
    pad = (0.9, 1.0, 0.9, 1.0)
    stim1 = illusions.rings.ring_stimulus(
        ppd=ppd,
        n_rings=8,
        target_idx=4,
        ring_width=0.5,
        vring1=v1,
        vring2=v3,
        vtarget=v2,
    )
    stim2 = illusions.rings.ring_stimulus(
        ppd=ppd,
        n_rings=8,
        target_idx=3,
        ring_width=0.5,
        vring1=v1,
        vring2=v3,
        vtarget=v2,
    )

    # Padding
    img1, mask1 = pad_img(stim1["img"], pad, ppd, v1), pad_img(
        stim1["mask"], pad, ppd, 0
    )
    img2, mask2 = pad_img(stim2["img"], pad, ppd, v1), pad_img(
        stim2["mask"], pad, ppd, 0
    )

    # Increase target index of right stimulus half
    mask2 = mask2 + 1
    mask2[mask2 == 1] = 0

    # Stacking
    img_stacked = np.hstack([img1, img2])
    mask_stacked = np.hstack([mask1, mask2])
    return {"img": img_stacked, "mask": mask_stacked}


def bullseye(ppd=PPD):
    v1, v2, v3 = 1.0, 5.0, 9.0
    pad = (0.9, 1.0, 0.9, 1.0)
    stim1 = illusions.bullseye.bullseye_stimulus(
        ppd=ppd,
        n_rings=8,
        ring_width=0.5,
        vring1=v1,
        vring2=v3,
        vtarget=v2,
    )
    stim2 = illusions.bullseye.bullseye_stimulus(
        ppd=ppd,
        n_rings=8,
        ring_width=0.5,
        vring1=v3,
        vring2=v1,
        vtarget=v2,
    )

    # Padding
    img1, mask1 = pad_img(stim1["img"], pad, ppd, v1), pad_img(
        stim1["mask"], pad, ppd, 0
    )
    img2, mask2 = pad_img(stim2["img"], pad, ppd, v1), pad_img(
        stim2["mask"], pad, ppd, 0
    )

    # Increase target index of right stimulus half
    mask2 = mask2 + 1
    mask2[mask2 == 1] = 0

    # Stacking
    img_stacked = np.hstack([img1, img2])
    mask_stacked = np.hstack([mask1, mask2])
    return {"img": img_stacked, "mask": mask_stacked}


def simultaneous_brightness_contrast(ppd=PPD):
    stim1 = illusions.sbc.simultaneous_contrast(
        ppd=ppd,
        im_size=(10.0, 10.0),
        target_size=(2.1, 2.1),
        target_pos=(3.9, 3.9),
        vback=9.0,
        vtarget=5.0,
    )
    stim2 = illusions.sbc.simultaneous_contrast(
        ppd=ppd,
        im_size=(10.0, 10.0),
        target_size=(2.1, 2.1),
        target_pos=(3.9, 3.9),
        vback=1.0,
        vtarget=5.0,
    )

    # Increase target index of right stimulus half
    mask2 = stim2["mask"] + 1
    mask2[mask2 == 1] = 0

    # Stacking
    img_stacked = np.hstack([stim1["img"], stim2["img"]])
    mask_stacked = np.hstack([stim1["mask"], mask2])
    return {"img": img_stacked, "mask": mask_stacked}


def white(ppd=PPD):
    height, width, = (
        8.1,
        8.0,
    )
    n_cycles = 4
    frequency = n_cycles / width
    stim = illusions.whites.white(
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
    )

    padding = (0.9, 1.0, 0.9, 1.1)
    stim["img"] = pad_img(stim["img"], padding, ppd, val=5.0)
    stim["mask"] = pad_img(stim["mask"], padding, ppd, val=0)
    return stim


def benary(ppd=PPD):
    stim = illusions.benary_cross.benarys_cross(
        ppd=PPD,
        cross_size=(3.0, 3.0, 3.0, 3.0),
        cross_thickness=2.1,
        target_type=("r", "r"),
        target_ori=(0.0, 0.0),
        target_size=(1.1, 1.1),
        target_posx=(1.9, 7.0),
        target_posy=(1.9, 3.0),
        vback=9.0,
        vcross=1.0,
        vtarget=5.0,
    )

    padding = (0.9, 1.0, 0.9, 1.0)
    stim["img"] = pad_img(stim["img"], padding, ppd, val=9.0)
    stim["mask"] = pad_img(stim["mask"], padding, ppd, val=0)
    return stim


def todorovic(ppd=PPD):
    stim1 = illusions.todorovic.todorovic_in(
        im_size=(10.0, 10.0),
        ppd=ppd,
        target_size=(4.1, 4.1),
        target_pos=(2.9, 2.9),
        covers_height=3.1,
        covers_width=3.1,
        covers_posx=(1.4, 5.4, 1.4, 5.4),
        covers_posy=(1.4, 5.4, 5.4, 1.4),
        vback=1.0,
        vtarget=5.0,
        vcovers=9.0,
    )
    stim2 = illusions.todorovic.todorovic_in(
        im_size=(10.0, 10.0),
        ppd=ppd,
        target_size=(4.1, 4.1),
        target_pos=(2.9, 2.9),
        covers_height=3.1,
        covers_width=3.1,
        covers_posx=(1.4, 5.4, 1.4, 5.4),
        covers_posy=(1.4, 5.4, 5.4, 1.4),
        vback=9.0,
        vtarget=5.0,
        vcovers=1.0,
    )

    # Increase target index of right stimulus half
    mask2 = stim2["mask"] + 1
    mask2[mask2 == 1] = 0

    # Stacking
    img_stacked = np.hstack([stim1["img"], stim2["img"]])
    mask_stacked = np.hstack([stim1["mask"], mask2])
    return {"img": img_stacked, "mask": mask_stacked}


def checkerboard_contrast_contrast(ppd=PPD):
    # TODO: add mask
    return illusions.checkerboard_contrast_contrast.checkerboard_contrast_contrast_effect(
        ppd=ppd,
        n_checks=8,
        check_size=1.0,
        target_length=4,
        padding=(0.9, 1.1, 0.9, 1.1),
        check1=1.0,
        check2=9.0,
        tau=5,
        alpha=0.5,
    )


def checkerboard(ppd=PPD):
    stim = illusions.checkerboard_sbc.checkerboard_contrast(
        ppd=ppd,
        board_shape=(8, 8),
        check_size=1.0,
        targets_coords=((3, 2), (5, 5)),
        extend_targets=False,
        check1=1.0,
        check2=9.0,
        target=5.0,
    )

    padding = (0.9, 1.1, 0.9, 1.1)
    img = pad_img(stim["img"], padding, ppd=10, val=5.0)
    mask = pad_img(stim["mask"], padding, ppd=10, val=0)

    return {"img": img, "mask": mask}


def checkerboard_extended(ppd=PPD):
    stim = illusions.checkerboard_sbc.checkerboard_contrast(
        ppd=ppd,
        board_shape=(8, 8),
        check_size=1.0,
        targets_coords=((3, 2), (5, 5)),
        extend_targets=True,
        check1=1.0,
        check2=9.0,
        target=5.0,
    )

    padding = (0.9, 1.1, 0.9, 1.1)
    img = pad_img(stim["img"], padding, ppd=ppd, val=5.0)
    mask = pad_img(stim["mask"], padding, ppd=ppd, val=0)

    return {"img": img, "mask": mask}


def white_yazdanbakhsh(ppd=PPD):
    (
        height,
        width,
    ) = (8.0, 8.0)
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
        vbars=(1.0, 9.0),
        vtarget=5.0,
        vtopstripe=9.0,
        vbotstripe=1.0,
    )
    padding = (0.9, 1.1, 0.9, 1.1)
    img = pad_img(stim["img"], padding, ppd=ppd, val=5.0)
    mask = pad_img(stim["mask"], padding, ppd=ppd, val=0)
    return {"img": img, "mask": mask}


def white_anderson(ppd=PPD):
    (
        height,
        width,
    ) = (10.0, 10.0)
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
        vbars=(9.0, 1.0),
        vtarget=5.0,
        vtopstripe=1.0,
        vbotstripe=9.0,
    )
    padding = (0.9, 1.1, 0.9, 1.1)
    img = pad_img(stim["img"], padding, ppd=ppd, val=5.0)
    mask = pad_img(stim["mask"], padding, ppd=ppd, val=0)
    return {"img": img, "mask": mask}


def white_howe(ppd=PPD):
    (
        height,
        width,
    ) = (10.0, 10.0)
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
        vbars=(9.0, 1.0),
        vtarget=5.0,
        vtopstripe=1.0,
        vbotstripe=9.0,
    )
    padding = (0.9, 1.1, 0.9, 1.1)
    img = pad_img(stim["img"], padding, ppd=ppd, val=5.0)
    mask = pad_img(stim["mask"], padding, ppd=ppd, val=0)
    return {"img": img, "mask": mask}


if __name__ == "__main__":
    from stimuli.utils import plot_stimuli

    stims = gen_all(skip=True)

    plot_stimuli(stims, mask=False)
