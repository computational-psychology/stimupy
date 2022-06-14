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
]


def dungeon():
    return illusions.dungeon.dungeon_illusion(
        ppd=10,
        n_cells=5,
        target_radius=1,
        cell_size=1.0,
        padding=(0.9, 1.1, 0.9, 1.1),
        back=1.0,
        grid=9.0,
        target=5.0,
        double=True,
    )


def cube():
    return illusions.cube.cube_illusion(
        ppd=10,
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


def grating():
    return illusions.grating.grating_illusion(
        ppd=10,
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


def rings():
    return illusions.rings.ring_pattern(
        ppd=10,
        n_rings=8,
        target_pos_l=4,
        target_pos_r=3,
        ring_width=0.5,
        padding=(0.9, 1.0, 0.9, 1.0),
        back=1.0,
        rings=9.0,
        target=5.0,
        invert_rings=False,
        double=True,
    )


def bullseye():
    return illusions.bullseye.bullseye_illusion(
        n_rings=8,
        ring_width=0.5,
        target_pos_l=0,
        target_pos_r=0,
        padding=(0.9, 1.0, 0.9, 1.0),
        back=1.0,
        rings=9.0,
        target=5.0,
    )


def simultaneous_brightness_contrast():
    return illusions.sbc.simultaneous_brightness_contrast(
        ppd=10,
        target_shape=(2.1, 2.1),
        inner_padding=(3.9, 4.0, 3.9, 4.0),
        padding=(0, 0, 0, 0),
        left=9.0,
        right=1.0,
        target=5.0,
    )


def white():
    height, width, ppd = 8.1, 8.0, 10
    n_cycles = 4
    frequency = n_cycles / width
    return illusions.whites.white(
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
        padding_val=5.0,
    )


def benary():
    return illusions.benary_cross.benarys_cross(
        ppd=10,
        cross_size=(3, 3, 3, 3),
        cross_thickness=2.1,
        padding=(0.9, 1.0, 0.9, 1.0),
        target_size=1.1,
        back=9.0,
        cross=1.0,
        target=5.0,
    )


def todorovic():
    return illusions.todorovic.todorovic_illusion(
        target_shape=(4.1, 4.1),
        ppd=10,
        covers_shape=(3.1, 3.1),
        spacing=(1.5, 1.5, 1.5, 1.5),
        padding=(2.9, 3.0, 2.9, 3.0),
        grid=9.0,
        back=1.0,
        target=5.0,
    )


def checkerboard_contrast_contrast():
    # TODO: add mask
    return illusions.checkerboard_contrast_contrast.checkerboard_contrast_contrast_effect(
        ppd=10,
        n_checks=8,
        check_size=1.0,
        target_length=4,
        padding=(0.9, 1.1, 0.9, 1.1),
        check1=1.0,
        check2=9.0,
        tau=5,
        alpha=0.5,
    )


def checkerboard():
    stim = illusions.checkerboard_sbc.checkerboard_contrast(
        ppd=10,
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


def checkerboard_extended():
    stim = illusions.checkerboard_sbc.checkerboard_contrast(
        ppd=10,
        board_shape=(8, 8),
        check_size=1.0,
        targets_coords=((3, 2), (5, 5)),
        extend_targets=True,
        check1=1.0,
        check2=9.0,
        target=5.0,
    )
    padding = (0.9, 1.1, 0.9, 1.1)
    img = pad_img(stim["img"], padding, ppd=10, val=5.0)
    mask = pad_img(stim["mask"], padding, ppd=10, val=0)

    return {"img": img, "mask": mask}


if __name__ == "__main__":
    import math

    import matplotlib.pyplot as plt
    import numpy as np

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
