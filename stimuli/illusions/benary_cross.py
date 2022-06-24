import numpy as np
from scipy.ndimage import rotate
from stimuli.components import cross, triangle
from stimuli.utils import degrees_to_pixels


def benarys_cross(
    ppd=10.0,
    cross_size=(8.0, 8.0, 8.0, 8.0),
    cross_thickness=5.0,
    target_size=(2.0, 2.0),
    target_type=("r", "r"),
    target_ori=(0.0, 0.0),
    target_posx=(6.0, 19.0),
    target_posy=(6.0, 8.0),
    vback=1.0,
    vcross=0.0,
    vtarget=0.5,
):
    """
    Benary's Cross Illusion

    Parameters
    ----------
    ppd : int
        pixels per degree (visual angle)
    cross_size : (float, float, float, float)
        size of the cross' arms in degrees visual angle in form (top, bottom, left, right)
    cross_thickness : float
        width of the cross bars in degrees visual angle
    target_size : (float, float)
        size of all target(s) in degrees visual angle
    target_type : tuple of strings
        type of targets to use; option: r (rectangle), t (triangle); as many targets as types
    target_ori : tuple of floats
        tuple with orientation of targets in deg, as many targets as orientations
    target_posx : tuple of floats
        tuple with x coordinates of targets in degrees, as many targets as coordinates
    target_posy : tuple of floats
        tuple with y coordinates of targets in degrees, as many targets as coordinates
    vback : float
        background value
    vcross : float
        cross value
    vtarget : float
        target value

    Returns
    -------
    A stimulus dictionary with the stimulus ['img'] and target mask ['mask']
    """
    if any(
        len(lst) != len(target_type)
        for lst in [target_ori, target_posx, target_posy]
    ):
        raise Exception(
            "target_type, target_ori, target_posx and target_posy need the"
            " same length."
        )

    target_y_px, target_x_px = degrees_to_pixels(target_size, ppd)
    tposy = degrees_to_pixels(target_posy, ppd)
    tposx = degrees_to_pixels(target_posx, ppd)

    img = cross(ppd, cross_size, cross_thickness, vback, vcross)
    mask = np.zeros((img.shape[0], img.shape[1]))

    if (target_x_px + np.array(tposx)).max() > img.shape[1]:
        raise Exception("Leftmost target does not fit in image.")
    if (target_y_px + np.array(tposy)).max() > img.shape[0]:
        raise Exception("Lowest target does not fit in image.")

    # Add targets:
    for i in range(len(target_posx)):
        if target_type[i] == "r":
            tpatch = np.zeros([target_y_px, target_x_px]) + vtarget

        elif target_type[i] == "t":
            tpatch = triangle(
                ppd, (target_size[0], target_size[1]), 0.0, vtarget
            )

        else:
            raise Exception("You can only use r or t as shapes")

        # Rotate, resize to original shape and clean
        tpatch = rotate(tpatch, angle=target_ori[i])
        tpatch[tpatch < vtarget * 0.9] = 0.0
        tpatch[tpatch > vtarget * 0.9] = vtarget
        tpatch = tpatch[
            ~np.all(tpatch == 0, axis=1)
        ]  # Remove all rows with only zeros
        tpatch = tpatch[
            :, ~np.all(tpatch == 0, axis=0)
        ]  # Remove all cols with only zeros
        mpatch = np.copy(tpatch)
        mpatch[mpatch != 0] = i + 1

        # Only change the target parts if the image:
        ipatch = img[
            tposy[i] : tposy[i] + tpatch.shape[0],
            tposx[i] : tposx[i] + tpatch.shape[1],
        ]
        ipatch[tpatch == vtarget] = 0.0
        tpatch = tpatch + ipatch

        img[
            tposy[i] : tposy[i] + tpatch.shape[0],
            tposx[i] : tposx[i] + tpatch.shape[1],
        ] = tpatch
        mask[
            tposy[i] : tposy[i] + tpatch.shape[0],
            tposx[i] : tposx[i] + tpatch.shape[1],
        ] = mpatch
    return {"img": img, "mask": mask}


def todorovic_benary(
    ppd=10.0,
    L_size=(8.0, 8.0, 2.0, 14.0),
    target_size=(2.0, 2.0),
    target_type=("r", "r"),
    target_ori=(0.0, 0.0),
    target_posx=(2.0, 12.0),
    target_posy=(6.0, 8.0),
    vback=1.0,
    vcross=0.0,
    vtarget=0.5,
):
    """
    Todorovic Benary's Cross Illusion

    Parameters
    ----------
    ppd : int
        pixels per degree (visual angle)
    L_size : (float, float, float, float)
        size of the L's arms in degrees visual angle in form (height-top-L, height-bottom-L,
        width-finger-Ls, width-basis-Ls)
    target_size : (float, float)
        size of all target(s) in degrees visual angle
    target_type : tuple of strings
        type of targets to use; option: r (rectangle), t (triangle); as many targets as types
    target_ori : tuple of floats
        tuple with orientation of targets in deg, as many targets as orientations
    target_posx : tuple of floats
        tuple with x coordinates of targets in degrees, as many targets as coordinates
    target_posy : tuple of floats
        tuple with y coordinates of targets in degrees, as many targets as coordinates
    vback : float
        background value
    vcross : float
        cross value
    vtarget : float
        target value

    Returns
    -------
    A stimulus dictionary with the stimulus ['img'] and target mask ['mask']
    """
    if any(
        len(lst) != len(target_type)
        for lst in [target_ori, target_posx, target_posy]
    ):
        raise Exception(
            "target_type, target_ori, target_posx and target_posy need to be"
            " of same length."
        )

    (
        L_top_px,
        L_bottom_px,
        L_left_px,
        L_right_px,
    ) = degrees_to_pixels(L_size, ppd)
    target_y_px, target_x_px = degrees_to_pixels(target_size, ppd)
    tposy = degrees_to_pixels(target_posy, ppd)
    tposx = degrees_to_pixels(target_posx, ppd)
    width = L_left_px + L_right_px
    height = L_top_px + L_bottom_px

    if (target_x_px + np.array(tposx)).max() > width:
        raise Exception("Leftmost target does not fit in image.")
    if (target_y_px + np.array(tposy)).max() > height:
        raise Exception("Lowest target does not fit in image.")

    img = np.ones((height, width)) * vback
    mask = np.zeros((height, width))

    img[:, 0:L_left_px] = vcross
    img[height - L_bottom_px : :, 0 : width - L_left_px] = vcross

    # Add targets:
    for i in range(len(target_posx)):
        if target_type[i] == "r":
            tpatch = np.zeros([target_y_px, target_x_px]) + vtarget

        elif target_type[i] == "t":
            tpatch = triangle(
                ppd, (target_size[0], target_size[1]), 0.0, vtarget
            )

        else:
            raise Exception("You can only use r or t as shapes")

        # Rotate, resize to original shape and clean
        tpatch = rotate(tpatch, angle=target_ori[i])
        tpatch[tpatch < vtarget * 0.9] = 0.0
        tpatch[tpatch > vtarget * 0.9] = vtarget
        tpatch = tpatch[
            ~np.all(tpatch == 0, axis=1)
        ]  # Remove all rows with only zeros
        tpatch = tpatch[
            :, ~np.all(tpatch == 0, axis=0)
        ]  # Remove all cols with only zeros
        mpatch = np.copy(tpatch)
        mpatch[mpatch != 0] = i + 1

        # Only change the target parts if the image:
        ipatch = img[
            tposy[i] : tposy[i] + tpatch.shape[0],
            tposx[i] : tposx[i] + tpatch.shape[1],
        ]
        ipatch[tpatch == vtarget] = 0.0
        tpatch = tpatch + ipatch

        img[
            tposy[i] : tposy[i] + tpatch.shape[0],
            tposx[i] : tposx[i] + tpatch.shape[1],
        ] = tpatch
        mask[
            tposy[i] : tposy[i] + tpatch.shape[0],
            tposx[i] : tposx[i] + tpatch.shape[1],
        ] = mpatch
    return {"img": img, "mask": mask}


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    from stimuli.utils import plot_stimuli

    stims = {
        "Benary's cross": benarys_cross(),
        "Todorovic' version of Benary's cross": todorovic_benary(),
    }
    ax = plot_stimuli(stims)
    plt.show()
