import numpy as np
from scipy.ndimage import rotate
from stimuli.components import cross, triangle
from stimuli.utils import degrees_to_pixels


def benarys_cross_generalized(
    visual_size=(21., 21.),
    ppd=18.0,
    cross_thickness=5.0,
    target_size=(2.0, 2.0),
    target_type=("r", "r"),
    target_ori=(0.0, 0.0),
    target_posx=(6.0, 19.0),
    target_posy=(6.0, 8.0),
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
    target_ori : tuple of floats
        tuple with orientation of targets in deg, as many targets as orientations
    target_posx : tuple of floats
        tuple with x coordinates of targets in degrees, as many targets as coordinates
    target_posy : tuple of floats
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
    if any(
        len(lst) != len(target_type)
        for lst in [target_ori, target_posx, target_posy]
    ):
        raise Exception(
            "target_type, target_ori, target_posx and target_posy need the"
            " same length."
        )

    cross_size = np.array((visual_size[0],)*2 + (visual_size[1],)*2) - cross_thickness
    cross_size = cross_size / 2.
    target_y_px, target_x_px = degrees_to_pixels(target_size, ppd)
    tposy = degrees_to_pixels(target_posy, ppd)
    tposx = degrees_to_pixels(target_posx, ppd)

    img = cross(ppd, cross_size, cross_thickness, intensity_background, intensity_cross)
    mask = np.zeros((img.shape[0], img.shape[1]))

    if (target_x_px + np.array(tposx)).max() > img.shape[1]:
        raise ValueError("Rightmost target does not fit in image.")
    if (target_y_px + np.array(tposy)).max() > img.shape[0]:
        raise ValueError("Lowest target does not fit in image.")

    # Add targets:
    for i in range(len(target_posx)):
        if target_type[i] == "r":
            tpatch = np.zeros([target_y_px, target_x_px]) + intensity_target

        elif target_type[i] == "t":
            tpatch = triangle(
                ppd, (target_size[0], target_size[1]), 0.0, intensity_target
            )

        else:
            raise Exception("You can only use r or t as shapes")

        # Rotate, resize to original shape and clean
        tpatch = rotate(tpatch, angle=target_ori[i])
        thresh = 0.7
        tpatch[tpatch < intensity_target * thresh] = 0.0
        tpatch[tpatch > intensity_target * thresh] = intensity_target
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
        ipatch[tpatch == intensity_target] = 0.0
        tpatch = tpatch + ipatch

        img[
            tposy[i] : tposy[i] + tpatch.shape[0],
            tposx[i] : tposx[i] + tpatch.shape[1],
        ] = tpatch
        mask[
            tposy[i] : tposy[i] + tpatch.shape[0],
            tposx[i] : tposx[i] + tpatch.shape[1],
        ] = mpatch

    # Make sure that stimulus size is as requested
    img = img[0:int(visual_size[0]*ppd), 0:int(visual_size[1]*ppd)]
    mask = mask[0:int(visual_size[0]*ppd), 0:int(visual_size[1]*ppd)]

    params = {"shape": img.shape,
              "visual_size": np.array(img.shape)/ppd,
              "ppd": ppd,
              "cross_thickness": cross_thickness,
              "target_size": target_size,
              "target_type": target_type,
              "target_ori": target_ori,
              "target_posx": target_posx,
              "target_posy": target_posy,
              "intensity_background": intensity_background,
              "intensity_cross": intensity_cross,
              "intensity_target": intensity_target,
              }

    return {"img": img, "mask": mask, **params}


def benarys_cross_rectangles(
    visual_size=(21., 21.),
    ppd=20,
    cross_thickness=5.,
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
    target_ori = (0., 0.)
    target_posx = ((visual_size[1]-cross_thickness)/2. - target_size[1],
                   visual_size[1]-target_size[1])
    target_posx = np.round(np.array(target_posx) * ppd) / ppd
    target_posy = ((visual_size[0]-cross_thickness)/2. - target_size[0],
                   (visual_size[0]-cross_thickness)/2.)
    target_posy = np.round(np.array(target_posy) * ppd) / ppd
    stim = benarys_cross_generalized(visual_size,
                                     ppd,
                                     cross_thickness,
                                     target_size,
                                     target_type,
                                     target_ori,
                                     target_posx,
                                     target_posy,
                                     intensity_background,
                                     intensity_cross,
                                     intensity_target)
    return stim


def benarys_cross_triangles(
    visual_size=(21., 21.),
    ppd=20,
    cross_thickness=5.2,
    target_size=4.,
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
    target_ori = (90., 45.)
    target_posx = ((visual_size[1]-cross_thickness)/2. - target_size[0],
                   (visual_size[1]+cross_thickness)/2.)
    target_posx = np.round(np.array(target_posx) * ppd) / ppd
    target_posy = ((visual_size[0]-cross_thickness)/2. - target_size[0],
                   (visual_size[0]-cross_thickness)/2.)
    target_posy = np.round(np.array(target_posy) * ppd) / ppd
    stim = benarys_cross_generalized(visual_size, ppd, cross_thickness, target_size, target_type,
                                     target_ori, target_posx, target_posy, intensity_background, intensity_cross, intensity_target)
    return stim


def todorovic_benary_generalized(
    visual_size=(16., 16.),
    ppd=10.0,
    L_width=2.,
    target_size=(2.0, 2.0),
    target_type=("r", "r"),
    target_ori=(0.0, 0.0),
    target_posx=(2.0, 12.0),
    target_posy=(6.0, 8.0),
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
    target_ori : tuple of floats
        tuple with orientation of targets in deg, as many targets as orientations
    target_posx : tuple of floats
        tuple with x coordinates of targets in degrees, as many targets as coordinates
    target_posy : tuple of floats
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
    if any(
        len(lst) != len(target_type)
        for lst in [target_ori, target_posx, target_posy]
    ):
        raise Exception(
            "target_type, target_ori, target_posx and target_posy need to be"
            " of same length."
        )
    L_size = (visual_size[0]/2, visual_size[0]/2, L_width, visual_size[1]-L_width)

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

    img = np.ones((height, width)) * intensity_background
    mask = np.zeros((height, width))

    img[:, 0:L_left_px] = intensity_cross
    img[height - L_bottom_px : :, 0 : width - L_left_px] = intensity_cross

    # Add targets:
    for i in range(len(target_posx)):
        if target_type[i] == "r":
            tpatch = np.zeros([target_y_px, target_x_px]) + intensity_target

        elif target_type[i] == "t":
            tpatch = triangle(
                ppd, (target_size[0], target_size[1]), 0.0, intensity_target
            )

        else:
            raise Exception("You can only use r or t as shapes")

        # Rotate, resize to original shape and clean
        tpatch = rotate(tpatch, angle=target_ori[i])
        thresh = 0.7
        tpatch[tpatch < intensity_target * thresh] = 0.0
        tpatch[tpatch > intensity_target * thresh] = intensity_target
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
        ipatch[tpatch == intensity_target] = 0.0
        tpatch = tpatch + ipatch

        img[
            tposy[i] : tposy[i] + tpatch.shape[0],
            tposx[i] : tposx[i] + tpatch.shape[1],
        ] = tpatch
        mask[
            tposy[i] : tposy[i] + tpatch.shape[0],
            tposx[i] : tposx[i] + tpatch.shape[1],
        ] = mpatch

    params = {"shape": img.shape,
              "visual_size": np.array(img.shape)/ppd,
              "ppd": ppd,
              "L_width": L_width,
              "target_size": target_size,
              "target_type": target_type,
              "target_ori": target_ori,
              "target_posx": target_posx,
              "target_posy": target_posy,
              "intensity_background": intensity_background,
              "intensity_cross": intensity_cross,
              "intensity_target": intensity_target,
              }

    return {"img": img, "mask": mask, **params}


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    from stimuli.utils import plot_stimuli

    stims = {
        "Benary's cross - generalized": benarys_cross_generalized(),
        "Benary's cross - rectangles": benarys_cross_rectangles(),
        "Benary's cross - triangles": benarys_cross_triangles(),
        "Todorovic' version of Benary's cross": todorovic_benary_generalized(),
    }
    ax = plot_stimuli(stims)
    plt.show()
