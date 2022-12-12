import numpy as np
from scipy.ndimage import rotate
from stimuli.components import cross, triangle
from stimuli.utils import degrees_to_pixels


__all__ = [
    "benarys_cross_generalized",
    "benarys_cross_rectangles",
    "benarys_cross_triangles",
    "todorovic_benary_generalized",
    "todorovic_benary_rectangles",
    "todorovic_benary_triangles",
]

def benarys_cross_generalized(
    visual_size=(21.0, 21.0),
    ppd=18.0,
    cross_thickness=5.0,
    target_size=(2.0, 2.0),
    target_type=("r", "r"),
    target_orientation=(0.0, 0.0),
    target_x=(6.0, 19.0),
    target_y=(6.0, 8.0),
    intensity_background=1.0,
    intensity_cross=0.0,
    intensity_target=0.5,
):
    """
    Benary's Cross Illusion

    Parameters
    ----------
    visual_size : float or (float, float)
        size of the stimulus in degrees of visual angle (height, width)
    ppd : int
        pixels per degree (visual angle)
    cross_thickness : float
        width of the cross bars in degrees visual angle
    target_size : (float, float)
        size of all target(s) in degrees visual angle
    target_type : tuple of strings
        type of targets to use; option: r (rectangle), t (triangle); as many targets as types
    target_orientation : tuple of floats
        tuple with orientation of targets in deg, as many targets as orientations
    target_x : tuple of floats
        tuple with x coordinates of targets in degrees, as many targets as coordinates
    target_y : tuple of floats
        tuple with y coordinates of targets in degrees, as many targets as coordinates
    intensity_background : float
        intensity value for background
    intensity_cross : float
        intensity value for cross
    intensity_target : float
        intensity value for target

    Returns
    -------
    A stimulus dictionary with the stimulus ['img'] and target mask ['mask']
    """
    if isinstance(visual_size, (float, int)):
        visual_size = (visual_size, visual_size)
    if isinstance(target_size, (float, int)):
        target_size = (target_size, target_size)
    if isinstance(target_type, (str)):
        target_type = [target_type]
    if isinstance(target_orientation, (float, int)):
        target_orientation = [target_orientation]
    if isinstance(target_x, (float, int)):
        target_x = [target_x]
    if isinstance(target_y, (float, int)):
        target_y = [target_y]
    if np.min(target_x) < 0:
        raise ValueError("Leftmost target does not fit into image")
    if np.min(target_y) < 0:
        raise ValueError("Topmost target does not fit into image")

    n_targets = np.max(
        np.array([len(target_type), len(target_orientation), len(target_x), len(target_y)])
    )

    if len(target_type) == 1:
        target_type = target_type * n_targets
    if len(target_orientation) == 1:
        target_orientation = target_orientation * n_targets
    if len(target_x) == 1:
        target_x = target_x * n_targets
    if len(target_y) == 1:
        target_y = target_y * n_targets

    if any(len(lst) != n_targets for lst in [target_orientation, target_x, target_y]):
        raise Exception(
            "target_type, target_orientation, target_x and target_y need the same length."
        )

    target_y_px, target_x_px = degrees_to_pixels(target_size, ppd)
    ty = degrees_to_pixels(target_y, ppd)
    tx = degrees_to_pixels(target_x, ppd)

    img = cross(
        visual_size=visual_size,
        ppd=ppd,
        cross_arm_ratios=1.,
        cross_thickness=cross_thickness,
        intensity_background=intensity_background,
        intensity_cross=intensity_cross,
        )["img"]
    mask = np.zeros((img.shape[0], img.shape[1]))

    if (target_x_px + np.array(tx)).max() > img.shape[1]:
        raise ValueError("Rightmost target does not fit in image.")
    if (target_y_px + np.array(ty)).max() > img.shape[0]:
        raise ValueError("Lowest target does not fit in image.")

    # Add targets:
    for i in range(len(target_x)):
        if target_type[i] == "r":
            tpatch = np.zeros([target_y_px, target_x_px]) + intensity_target

        elif target_type[i] == "t":
            tpatch = triangle(
                visual_size=target_size,
                ppd=ppd,
                intensity_background=0.0,
                intensity_triangle=intensity_target,
                )["img"]

        else:
            raise Exception("You can only use r or t as shapes")

        # Rotate, resize to original shape and clean
        tpatch = rotate(tpatch, angle=target_orientation[i])
        thresh = 0.7
        tpatch[tpatch < intensity_target * thresh] = 0.0
        tpatch[tpatch > intensity_target * thresh] = intensity_target
        tpatch = tpatch[~np.all(tpatch == 0, axis=1)]  # Remove all rows with only zeros
        tpatch = tpatch[:, ~np.all(tpatch == 0, axis=0)]  # Remove all cols with only zeros
        mpatch = np.copy(tpatch)
        mpatch[mpatch != 0] = i + 1

        # Only change the target parts if the image:
        ipatch = img[
            ty[i] : ty[i] + tpatch.shape[0],
            tx[i] : tx[i] + tpatch.shape[1],
        ]
        ipatch[tpatch == intensity_target] = 0.0
        tpatch = tpatch + ipatch

        img[
            ty[i] : ty[i] + tpatch.shape[0],
            tx[i] : tx[i] + tpatch.shape[1],
        ] = tpatch
        mask[
            ty[i] : ty[i] + tpatch.shape[0],
            tx[i] : tx[i] + tpatch.shape[1],
        ] = mpatch

    # Make sure that stimulus size is as requested
    img = img[0 : int(visual_size[0] * ppd), 0 : int(visual_size[1] * ppd)]
    mask = mask[0 : int(visual_size[0] * ppd), 0 : int(visual_size[1] * ppd)]

    stim = {
        "img": img,
        "mask": mask.astype(int),
        "shape": img.shape,
        "visual_size": np.array(img.shape) / ppd,
        "ppd": ppd,
        "cross_thickness": cross_thickness,
        "target_size": target_size,
        "target_type": target_type,
        "target_orientation": target_orientation,
        "target_x": target_x,
        "target_y": target_y,
        "intensity_background": intensity_background,
        "intensity_cross": intensity_cross,
        "intensity_target": intensity_target,
    }

    return stim


def benarys_cross_rectangles(
    visual_size=(21.0, 21.0),
    ppd=20,
    cross_thickness=5.0,
    target_size=(3.0, 4.0),
    intensity_background=1.0,
    intensity_cross=0.0,
    intensity_target=0.5,
):
    """
    Benary's Cross stimulus with two rectangular targets with default placement

    Parameters
    ----------
    visual_size : float or (float, float)
        size of the stimulus in degrees of visual angle (height, width)
    ppd : int
        pixels per degree (visual angle)
    cross_thickness : float
        width of the cross bars in degrees visual angle
    target_size : (float, float)
        size of all target(s) in degrees visual angle
    intensity_background : float
        intensity value for background
    intensity_cross : float
        intensity value for cross
    intensity_target : float
        intensity value for target

    Returns
    -------
    A stimulus dictionary with the stimulus ['img'] and target mask ['mask']
    """

    if isinstance(visual_size, (float, int)):
        visual_size = (visual_size, visual_size)
    if isinstance(target_size, (float, int)):
        target_size = (target_size, target_size)
    if target_size[0] > cross_thickness:
        raise ValueError("Target size is larger than cross thickness")

    # Calculate parameters for classical Benarys cross with two targets
    target_type = ("r",) * 2
    target_ori = (0.0, 0.0)
    target_x = (
        (visual_size[1] - cross_thickness) / 2.0 - target_size[1],
        visual_size[1] - target_size[1],
    )
    target_x = np.round(np.array(target_x) * ppd) / ppd
    target_y = (
        (visual_size[0] - cross_thickness) / 2.0 - target_size[0],
        (visual_size[0] - cross_thickness) / 2.0,
    )
    target_y = np.round(np.array(target_y) * ppd) / ppd
    stim = benarys_cross_generalized(
        visual_size=visual_size,
        ppd=ppd,
        cross_thickness=cross_thickness,
        target_size=target_size,
        target_type=target_type,
        target_orientation=target_ori,
        target_x=target_x,
        target_y=target_y,
        intensity_background=intensity_background,
        intensity_cross=intensity_cross,
        intensity_target=intensity_target,
    )
    return stim


def benarys_cross_triangles(
    visual_size=(21.0, 21.0),
    ppd=20,
    cross_thickness=5.2,
    target_size=4.0,
    intensity_background=1.0,
    intensity_cross=0.0,
    intensity_target=0.5,
):
    """
    Benary's Cross stimulus with two triangular targets with default placement

    Parameters
    ----------
    visual_size : float or (float, float)
        size of the stimulus in degrees of visual angle (height, width)
    ppd : int
        pixels per degree (visual angle)
    cross_thickness : float
        width of the cross bars in degrees visual angle
    target_size : float
        size of adjacent and opposite of target triangle in degrees visual angle
    intensity_background : float
        intensity value for background
    intensity_cross : float
        intensity value for cross
    intensity_target : float
        intensity value for target

    Returns
    -------
    A stimulus dictionary with the stimulus ['img'] and target mask ['mask']
    """

    if isinstance(visual_size, (float, int)):
        visual_size = (visual_size, visual_size)
    if isinstance(target_size, (float, int)):
        target_size = (target_size, target_size)
    else:
        raise ValueError("target_size should be a single float")
    if target_size[0] > cross_thickness:
        raise ValueError("Target size is larger than cross thickness")

    # Calculate parameters for classical Benarys cross with two targets
    target_type = ("t",) * 2
    target_ori = (90.0, 45.0)
    target_x = (
        (visual_size[1] - cross_thickness) / 2.0 - target_size[0],
        (visual_size[1] + cross_thickness) / 2.0,
    )
    target_x = np.round(np.array(target_x) * ppd) / ppd
    target_y = (
        (visual_size[0] - cross_thickness) / 2.0 - target_size[0],
        (visual_size[0] - cross_thickness) / 2.0,
    )
    target_y = np.round(np.array(target_y) * ppd) / ppd

    stim = benarys_cross_generalized(
        visual_size=visual_size,
        ppd=ppd,
        cross_thickness=cross_thickness,
        target_size=target_size,
        target_type=target_type,
        target_orientation=target_ori,
        target_x=target_x,
        target_y=target_y,
        intensity_background=intensity_background,
        intensity_cross=intensity_cross,
        intensity_target=intensity_target,
    )
    return stim


def todorovic_benary_generalized(
    visual_size=(16.0, 16.0),
    ppd=10.0,
    L_width=2.0,
    target_size=(2.0, 2.0),
    target_type=("r", "r"),
    target_orientation=(0.0, 0.0),
    target_x=(2.0, 12.0),
    target_y=(6.0, 8.0),
    intensity_background=1.0,
    intensity_cross=0.0,
    intensity_target=0.5,
):
    """
    Todorovic Benary's Cross Illusion

    Parameters
    ----------
    visual_size : float or (float, float)
        size of the stimulus in degrees of visual angle (height, width)
    ppd : int
        pixels per degree (visual angle)
    L_width : float
        width of L in degree visual angle
    target_size : (float, float)
        size of all target(s) in degrees visual angle
    target_type : tuple of strings
        type of targets to use; option: r (rectangle), t (triangle); as many targets as types
    target_orientation : tuple of floats
        tuple with orientation of targets in deg, as many targets as orientations
    target_x : tuple of floats
        tuple with x coordinates of targets in degrees, as many targets as coordinates
    target_y : tuple of floats
        tuple with y coordinates of targets in degrees, as many targets as coordinates
    intensity_background : float
        intensity value for background
    intensity_cross : float
        intensity value for cross
    intensity_target : float
        intensity value for target

    Returns
    -------
    A stimulus dictionary with the stimulus ['img'] and target mask ['mask']
    """
    if isinstance(visual_size, (float, int)):
        visual_size = (visual_size, visual_size)
    if isinstance(target_size, (float, int)):
        target_size = (target_size, target_size)
    if isinstance(target_type, (str)):
        target_type = [target_type]
    if isinstance(target_orientation, (float, int)):
        target_orientation = [target_orientation]
    if isinstance(target_x, (float, int)):
        target_x = [target_x]
    if isinstance(target_y, (float, int)):
        target_y = [target_y]
    if np.min(target_x) < 0:
        raise ValueError("Leftmost target does not fit into image")
    if np.min(target_y) < 0:
        raise ValueError("Topmost target does not fit into image")

    n_targets = np.max(
        np.array([len(target_type), len(target_orientation), len(target_x), len(target_y)])
    )

    if len(target_type) == 1:
        target_type = target_type * n_targets
    if len(target_orientation) == 1:
        target_orientation = target_orientation * n_targets
    if len(target_x) == 1:
        target_x = target_x * n_targets
    if len(target_y) == 1:
        target_y = target_y * n_targets

    if any(len(lst) != n_targets for lst in [target_orientation, target_x, target_y]):
        raise Exception(
            "target_type, target_orientation, target_x and target_y need the same length."
        )

    L_size = (visual_size[0] / 2, visual_size[0] / 2, L_width, visual_size[1] - L_width)

    (
        L_top_px,
        L_bottom_px,
        L_left_px,
        L_right_px,
    ) = degrees_to_pixels(L_size, ppd)
    target_y_px, target_x_px = degrees_to_pixels(target_size, ppd)
    ty = degrees_to_pixels(target_y, ppd)
    tx = degrees_to_pixels(target_x, ppd)
    width = L_left_px + L_right_px
    height = L_top_px + L_bottom_px

    if (target_x_px + np.array(tx)).max() > width:
        raise Exception("Leftmost target does not fit in image.")
    if (target_y_px + np.array(ty)).max() > height:
        raise Exception("Lowest target does not fit in image.")

    img = np.ones((height, width)) * intensity_background
    mask = np.zeros((height, width))

    img[:, 0:L_left_px] = intensity_cross
    img[height - L_bottom_px : :, 0 : width - L_left_px] = intensity_cross

    # Add targets:
    for i in range(len(target_x)):
        if target_type[i] == "r":
            tpatch = np.zeros([target_y_px, target_x_px]) + intensity_target

        elif target_type[i] == "t":
            tpatch = triangle(
                visual_size=target_size,
                ppd=ppd,
                intensity_background=0.0,
                intensity_triangle=intensity_target,
                )["img"]

        else:
            raise Exception("You can only use r or t as shapes")

        # Rotate, resize to original shape and clean
        tpatch = rotate(tpatch, angle=target_orientation[i])
        thresh = 0.7
        tpatch[tpatch < intensity_target * thresh] = 0.0
        tpatch[tpatch > intensity_target * thresh] = intensity_target
        tpatch = tpatch[~np.all(tpatch == 0, axis=1)]     # Remove rows with only zeros
        tpatch = tpatch[:, ~np.all(tpatch == 0, axis=0)]  # Remove cols with only zeros
        mpatch = np.copy(tpatch)
        mpatch[mpatch != 0] = i + 1

        # Only change the target parts if the image:
        ipatch = img[
            ty[i] : ty[i] + tpatch.shape[0],
            tx[i] : tx[i] + tpatch.shape[1],
        ]
        ipatch[tpatch == intensity_target] = 0.0
        tpatch = tpatch + ipatch

        img[
            ty[i] : ty[i] + tpatch.shape[0],
            tx[i] : tx[i] + tpatch.shape[1],
        ] = tpatch
        mask[
            ty[i] : ty[i] + tpatch.shape[0],
            tx[i] : tx[i] + tpatch.shape[1],
        ] = mpatch

    stim = {
        "img": img,
        "mask": mask.astype(int),
        "shape": img.shape,
        "visual_size": np.array(img.shape) / ppd,
        "ppd": ppd,
        "L_width": L_width,
        "target_size": target_size,
        "target_type": target_type,
        "target_orientation": target_orientation,
        "target_x": target_x,
        "target_y": target_y,
        "intensity_background": intensity_background,
        "intensity_cross": intensity_cross,
        "intensity_target": intensity_target,
    }

    return stim


def todorovic_benary_rectangles(
    visual_size=(21.0, 21.0),
    ppd=20,
    L_width=5.0,
    target_size=(3.0, 4.0),
    intensity_background=1.0,
    intensity_cross=0.0,
    intensity_target=0.5,
):
    """
    Todorovic version of Benary's Cross stimulus with two rectangular targets and default placement

    Parameters
    ----------
    visual_size : float or (float, float)
        size of the stimulus in degrees of visual angle (height, width)
    ppd : int
        pixels per degree (visual angle)
    L_width : float
        width of L in degree visual angle
    target_size : (float, float)
        size of all target(s) in degrees visual angle
    intensity_background : float
        intensity value for background
    intensity_cross : float
        intensity value for cross
    intensity_target : float
        intensity value for target

    Returns
    -------
    A stimulus dictionary with the stimulus ['img'] and target mask ['mask']
    """

    if isinstance(visual_size, (float, int)):
        visual_size = (visual_size, visual_size)
    if isinstance(target_size, (float, int)):
        target_size = (target_size, target_size)

    # Calculate parameters for classical Benarys cross with two targets
    target_type = ("r",) * 2
    target_ori = (0.0, 0.0)
    target_x = (L_width, visual_size[1] - L_width - target_size[1])
    target_x = np.round(np.array(target_x) * ppd) / ppd
    target_y = (visual_size[0] / 2.0 - target_size[0], visual_size[0] / 2.0)
    target_y = np.round(np.array(target_y) * ppd) / ppd
    stim = todorovic_benary_generalized(
        visual_size=visual_size,
        ppd=ppd,
        L_width=L_width,
        target_size=target_size,
        target_type=target_type,
        target_orientation=target_ori,
        target_x=target_x,
        target_y=target_y,
        intensity_background=intensity_background,
        intensity_cross=intensity_cross,
        intensity_target=intensity_target,
    )
    return stim


def todorovic_benary_triangles(
    visual_size=(21.0, 21.0),
    ppd=20,
    L_width=5.2,
    target_size=4.0,
    intensity_background=1.0,
    intensity_cross=0.0,
    intensity_target=0.5,
):
    """
    Todorovic version of Benary's Cross stimulus with two triangular targets and default placement

    Parameters
    ----------
    visual_size : float or (float, float)
        size of the stimulus in degrees of visual angle (height, width)
    ppd : int
        pixels per degree (visual angle)
    L_width : float
        width of L in degree visual angle
    target_size : float
        size of adjacent and opposite of target triangle in degrees visual angle
    intensity_background : float
        intensity value for background
    intensity_cross : float
        intensity value for cross
    intensity_target : float
        intensity value for target

    Returns
    -------
    A stimulus dictionary with the stimulus ['img'] and target mask ['mask']
    """

    if isinstance(visual_size, (float, int)):
        visual_size = (visual_size, visual_size)
    if isinstance(target_size, (float, int)):
        target_size = (target_size, target_size)
    else:
        raise ValueError("target_size should be a single float")

    # Calculate parameters for classical Benarys cross with two targets
    target_type = ("t",) * 2
    target_ori = (0.0, 180.0)
    target_x = (L_width, visual_size[1] - L_width - target_size[1])
    target_x = np.round(np.array(target_x) * ppd) / ppd
    target_y = (visual_size[0] / 2.0 - target_size[0], visual_size[0] / 2.0)
    target_y = np.round(np.array(target_y) * ppd) / ppd

    stim = todorovic_benary_generalized(
        visual_size=visual_size,
        ppd=ppd,
        L_width=L_width,
        target_size=target_size,
        target_type=target_type,
        target_orientation=target_ori,
        target_x=target_x,
        target_y=target_y,
        intensity_background=intensity_background,
        intensity_cross=intensity_cross,
        intensity_target=intensity_target,
    )
    return stim


if __name__ == "__main__":
    from stimuli.utils import plot_stimuli

    stims = {
        "Benary's cross - generalized": benarys_cross_generalized(),
        "Benary's cross - rectangles": benarys_cross_rectangles(),
        "Benary's cross - triangles": benarys_cross_triangles(),
        "Todorovic' Benary - generalized": todorovic_benary_generalized(),
        "Todorovic' Benary - rectangles": todorovic_benary_rectangles(),
        "Todorovic' Benary - triangles": todorovic_benary_triangles(),
    }
    plot_stimuli(stims, mask=True, save=None)
