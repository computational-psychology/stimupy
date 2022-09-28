import numpy as np
from stimuli.components.checkerboard import checkerboard as board
from stimuli.utils import degrees_to_pixels, resolution


def mask_from_idx(checkerboard_stim, check_idc):
    board_shape = checkerboard_stim["board_shape"]

    check_size = checkerboard_stim["check_visual_size"]
    ppd = checkerboard_stim["ppd"]

    check_size_px = resolution.shape_from_visual_size_ppd(check_size, ppd)

    mask = np.zeros(checkerboard_stim["shape"])
    for coords in check_idc:
        if (
            coords[0] < 0
            or coords[0] > coords[0]
            or coords[1] < 0
            or coords[1] > board_shape[1]
        ):
            raise ValueError(
                f"Cannot provide mask for check {coords} outside board {board_shape}"
            )
        ypos = int(coords[0] * check_size_px.height)
        xpos = int(coords[1] * check_size_px.width)
        mask[
            ypos : ypos + int(check_size_px.height),
            xpos : xpos + int(check_size_px.width),
        ] = 1

    return mask


def extend_target_idx(target_idx, offsets=[(-1, 0), (0, -1), (0, 0), (0, 1), (1, 0)]):
    extended_idc = []
    for offset in offsets:
        new_idx = (target_idx[0] + offset[0], target_idx[1] + offset[1])
        extended_idc.append(new_idx)
    return extended_idc


def add_targets(checkerboard_stim, targets, extend_targets=False, intensity_target=0.5):
    mask = np.zeros(checkerboard_stim["shape"])
    for i, target in enumerate(targets):
        if extend_targets:
            target_idc = extend_target_idx(target)
        else:
            target_idc = [target]
        for target_idx in target_idc:
            mask += mask_from_idx(checkerboard_stim, (target_idx,)) * (i + 1)
    img = np.where(mask, intensity_target, checkerboard_stim["img"])

    checkerboard_stim["img"] = img
    checkerboard_stim["mask"] = mask
    return checkerboard_stim


def checkerboard(
    shape=None,
    ppd=None,
    visual_size=None,
    board_shape=None,
    check_visual_size=None,
    targets=None,
    extend_targets=False,
    intensity_low=0.0,
    intensity_high=1.0,
    intensity_target=0.5,
):
    stim = board(
        ppd=ppd,
        shape=shape,
        visual_size=visual_size,
        board_shape=board_shape,
        check_visual_size=check_visual_size,
        intensity_low=intensity_low,
        intensity_high=intensity_high,
    )

    if targets is not None:
        stim = add_targets(
            stim,
            targets=targets,
            extend_targets=extend_targets,
            intensity_target=intensity_target,
        )

    return stim


# def contrast(
#     ppd=30,
#     board_shape=(8, 8),
#     check_size=1.0,
#     target_indices=((3, 2), (5, 5)),
#     extend_targets=False,
#     vcheck1=0.0,
#     vcheck2=1.0,
#     vtarget=0.5,
# ):
#     check_size_px = degrees_to_pixels(check_size, ppd)
#     nchecks_height, nchecks_width = board_shape

#     img = checkerboard(ppd, board_shape, check_size, vcheck1, vcheck2)
#     mask = np.zeros(img.shape)

#     for i, coords in enumerate(target_indices):
#         ypos = int(coords[0] * check_size_px)
#         xpos = int(coords[1] * check_size_px)
#         img[ypos : ypos + check_size_px, xpos : xpos + check_size_px] = vtarget
#         mask[ypos : ypos + check_size_px, xpos : xpos + check_size_px] = i + 1

#     if extend_targets:
#         for i, coords in enumerate(target_indices):
#             for idx in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
#                 ypos = int(coords[0] * check_size_px + idx[0] * check_size_px)
#                 xpos = int(coords[1] * check_size_px + idx[1] * check_size_px)
#                 img[ypos : ypos + check_size_px, xpos : xpos + check_size_px] = vtarget
#                 mask[ypos : ypos + check_size_px, xpos : xpos + check_size_px] = i + 1
#     return {"img": img, "mask": mask}


def contrast_contrast(
    shape=None,
    ppd=None,
    visual_size=None,
    board_shape=None,
    check_visual_size=None,
    target_shape=(2, 3),
    intensity_low=0.0,
    intensity_high=1.0,
    tau=0.5,
    alpha=0.2,
):
    """
    Contrast-contrast effect on checkerboard with square transparency layer.

    Parameters
    ----------
    ppd : int
        pixels per degree (visual angle)
    board shape : (int, int)
        number of checks in y, x direction
    check_size : float
        size of a check in degrees visual angle
    targets_shape : (int, int)
        number of checks with transparecny in y, x direction
    vcheck1 : float
        first check value
    vcheck2 : float
        other check value
    tau : float
        tau of transparency (i.e. value of transparent medium)
    alpha : float
        alpha of transparency (i.e. how transparant the medium is)

    Returns
    -------
    A stimulus dictionary with the stimulus ['img'] and target mask ['mask']
    """

    stim = board(
        ppd=ppd,
        shape=shape,
        visual_size=visual_size,
        board_shape=board_shape,
        check_visual_size=check_visual_size,
        intensity_low=intensity_low,
        intensity_high=intensity_high,
    )
    img = stim["img"]

    check_size_px = resolution.shape_from_visual_size_ppd(
        visual_size=check_visual_size, ppd=stim["ppd"]
    )
    target_idx = np.zeros(img.shape, dtype=bool)
    tposy = (img.shape[0] - target_shape[0] * check_size_px.height) // 2
    tposx = (img.shape[1] - target_shape[1] * check_size_px.width) // 2
    target_idx[
        tposy : tposy + target_shape[0] * check_size_px[0],
        tposx : tposx + target_shape[1] * check_size_px[1],
    ] = True
    img[target_idx] = alpha * img[target_idx] + (1 - alpha) * tau

    mask = np.zeros(img.shape)
    mask[target_idx] = 1

    return {"img": img, "mask": mask}


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    from stimuli.utils import plot_stimuli

    DEFAULT_PPD = 32

    stims = {
        "Checkerboard (brightness)": checkerboard(
            ppd=32,
            board_shape=(8, 8),
            check_visual_size=(2, 2),
            targets=[(3, 2), (5, 5)],
        ),
        "Checkerboard contrast-contrast": contrast_contrast(
            ppd=32, board_shape=(8, 8), check_visual_size=(2, 2), target_shape=(4, 4)
        ),
    }
    ax = plot_stimuli(stims, mask=False)
    plt.show()
