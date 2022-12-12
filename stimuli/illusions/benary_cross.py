import numpy as np
import warnings
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
    visual_size=None,
    ppd=None,
    cross_thickness=None,
    target_size=None,
    target_type="r",
    target_orientation=0,
    target_x=None,
    target_y=None,
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
    
    # Create cross
    img = cross(
        visual_size=visual_size,
        ppd=ppd,
        cross_arm_ratios=1.,
        cross_thickness=cross_thickness,
        intensity_background=intensity_background,
        intensity_cross=intensity_cross,
        )["img"]

    # Add targets
    stim = add_targets(img,
                       ppd,
                       target_size,
                       target_type,
                       target_orientation,
                       target_x,
                       target_y,
                       intensity_target,
                       )

    # Add missing parameter information
    stim["cross_thickness"] = cross_thickness
    stim["intensity_background"] = intensity_background
    stim["intensity_cross"] = intensity_cross
    return stim


def benarys_cross_rectangles(
    visual_size=None,
    ppd=None,
    cross_thickness=None,
    target_size=None,
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
    if target_size is None:
        raise ValueError("target_size cannot be None")
    if isinstance(target_size, (float, int)):
        target_size = (target_size, target_size)
    if target_size[0] > cross_thickness:
        raise ValueError("Target size is larger than cross thickness")

    # Calculate target placement for classical Benarys cross
    target_x = (
        (visual_size[1] - cross_thickness) / 2.0 - target_size[1],
        visual_size[1] - target_size[1],
    )

    target_y = (
        (visual_size[0] - cross_thickness) / 2.0 - target_size[0],
        (visual_size[0] - cross_thickness) / 2.0,
    )

    stim = benarys_cross_generalized(
        visual_size=visual_size,
        ppd=ppd,
        cross_thickness=cross_thickness,
        target_size=target_size,
        target_type=("r",) * 2,
        target_orientation=0.,
        target_x=np.round(np.array(target_x) * ppd) / ppd,
        target_y=np.round(np.array(target_y) * ppd) / ppd,
        intensity_background=intensity_background,
        intensity_cross=intensity_cross,
        intensity_target=intensity_target,
    )
    return stim


def benarys_cross_triangles(
    visual_size=None,
    ppd=None,
    cross_thickness=None,
    target_size=None,
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
    if target_size is None:
        raise ValueError("target_size cannot be None")
    if isinstance(target_size, (float, int)):
        target_size = (target_size, target_size)
    if target_size[0] > cross_thickness:
        raise ValueError("Target size is larger than cross thickness")

    # Calculate target placement for classical Benarys cross
    target_x = (
        (visual_size[1] - cross_thickness) / 2.0 - target_size[0],
        (visual_size[1] + cross_thickness) / 2.0,
    )

    target_y = (
        (visual_size[0] - cross_thickness) / 2.0 - target_size[0],
        (visual_size[0] - cross_thickness) / 2.0,
    )

    stim = benarys_cross_generalized(
        visual_size=visual_size,
        ppd=ppd,
        cross_thickness=cross_thickness,
        target_size=target_size,
        target_type=("t",)*2,
        target_orientation=(90.0, 45.0),
        target_x=np.round(np.array(target_x) * ppd) / ppd,
        target_y=np.round(np.array(target_y) * ppd) / ppd,
        intensity_background=intensity_background,
        intensity_cross=intensity_cross,
        intensity_target=intensity_target,
    )
    return stim


def todorovic_benary_generalized(
    visual_size=None,
    ppd=None,
    L_width=None,
    target_size=None,
    target_type="r",
    target_orientation=0,
    target_x=None,
    target_y=None,
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

    L_size = (visual_size[0] / 2, visual_size[0] / 2, L_width, visual_size[1] - L_width)
    top, bottom, left, right = degrees_to_pixels(L_size, ppd)
    width, height = left + right, top + bottom
    
    # Create stimulus without targets
    img = np.ones((height, width)) * intensity_background
    img[:, 0:left] = intensity_cross
    img[height - bottom : :, 0 : width - left] = intensity_cross

    # Add targets
    stim = add_targets(img,
                       ppd,
                       target_size,
                       target_type,
                       target_orientation,
                       target_x,
                       target_y,
                       intensity_target,
                       )

    # Add missing parameter information
    stim["L_width"] = L_width
    stim["intensity_background"] = intensity_background
    stim["intensity_cross"] = intensity_cross
    return stim


def todorovic_benary_rectangles(
    visual_size=None,
    ppd=None,
    L_width=None,
    target_size=None,
    intensity_background=1.0,
    intensity_cross=0.0,
    intensity_target=0.5,
):
    """
    Todorovic version of Benary's Cross stimulus with two rectangular targets
    and default placement

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
    if target_size is None:
        raise ValueError("target_size cannot be None")
    if isinstance(target_size, (float, int)):
        target_size = (target_size, target_size)

    # Calculate target placement for classical Todorovic-Benary
    target_x = (L_width, visual_size[1] - L_width - target_size[1])
    target_y = (visual_size[0] / 2.0 - target_size[0], visual_size[0] / 2.0)

    stim = todorovic_benary_generalized(
        visual_size=visual_size,
        ppd=ppd,
        L_width=L_width,
        target_size=target_size,
        target_type=("r",) * 2,
        target_orientation=0,
        target_x=np.round(np.array(target_x) * ppd) / ppd,
        target_y=np.round(np.array(target_y) * ppd) / ppd,
        intensity_background=intensity_background,
        intensity_cross=intensity_cross,
        intensity_target=intensity_target,
    )
    return stim


def todorovic_benary_triangles(
    visual_size=None,
    ppd=None,
    L_width=None,
    target_size=None,
    intensity_background=1.0,
    intensity_cross=0.0,
    intensity_target=0.5,
):
    """
    Todorovic version of Benary's Cross stimulus with two triangular targets
    and default placement

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
    if target_size is None:
        raise ValueError("target_size cannot be None")
    if isinstance(target_size, (float, int)):
        target_size = (target_size, target_size)
    else:
        raise ValueError("target_size should be a single float")

    # Calculate target placement for classical Todorovic-Benary
    target_x = (L_width, visual_size[1] - L_width - target_size[1])
    target_y = (visual_size[0] / 2.0 - target_size[0], visual_size[0] / 2.0)

    stim = todorovic_benary_generalized(
        visual_size=visual_size,
        ppd=ppd,
        L_width=L_width,
        target_size=target_size,
        target_type=("t",) * 2,
        target_orientation=(0.0, 180.0),
        target_x=np.round(np.array(target_x) * ppd) / ppd,
        target_y=np.round(np.array(target_y) * ppd) / ppd,
        intensity_background=intensity_background,
        intensity_cross=intensity_cross,
        intensity_target=intensity_target,
    )
    return stim


def add_targets(
        img,
        ppd,
        target_size,
        target_type,
        target_orientation,
        target_x,
        target_y,
        intensity_target,
        ):
    """Add targets to Benary-like stimulus

    Parameters
    ----------
    img : 2d numpy array
        image to which targets will be added
    ppd : int
        pixels per degree (visual angle)
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
    intensity_target : float
        intensity value for target

    Returns
    -------
    A stimulus dictionary with the stimulus ['img'] and target mask ['mask']
    """

    mask = np.zeros(img.shape)
    
    # If any target information is missing, dont add targets
    if ((target_size is None) or
        (target_type is None) or
        (target_orientation is None) or
        (target_x is None) or
        (target_y is None)):
            warnings.warn("Target information is missing - no target added")
            stim = {
                "target_size": None,
                "target_type": None,
                "target_orientation": None,
                "target_x": None,
                "target_y": None,
                "intensity_target": None,
                }

    # Re-format all target information and add targets
    else:
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
    
        theight, twidth = degrees_to_pixels(target_size, ppd)
        ty = degrees_to_pixels(target_y, ppd)
        tx = degrees_to_pixels(target_x, ppd)
    
        if (twidth + np.array(tx)).max() > img.shape[1]:
            raise ValueError("Rightmost target does not fit in image.")
        if (theight + np.array(ty)).max() > img.shape[0]:
            raise ValueError("Lowest target does not fit in image.")
    
        # Add targets:
        for i in range(len(target_x)):
            if target_type[i] == "r":
                tpatch = np.ones([theight, twidth]) * intensity_target
    
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
            tpatch = tpatch[~np.all(tpatch == 0, axis=1)]  # Remove zero-rows
            tpatch = tpatch[:, ~np.all(tpatch == 0, axis=0)]  # Remove zero-cols
            mpatch = np.copy(tpatch)
            mpatch[mpatch != 0] = i + 1
            theight_, twidth_ = tpatch.shape
    
            # Only change the target parts of the image:
            ipatch = img[ty[i]:ty[i]+theight_, tx[i]:tx[i]+twidth_]
            ipatch[tpatch == intensity_target] = 0.
            tpatch = tpatch + ipatch
    
            img[ty[i]:ty[i]+theight_, tx[i]:tx[i]+twidth_] = tpatch
            mask[ty[i]:ty[i]+theight_, tx[i]:tx[i]+twidth_] = mpatch

        stim = {
            "target_size": target_size,
            "target_type": target_type,
            "target_orientation": target_orientation,
            "target_x": target_x,
            "target_y": target_y,
            "intensity_target": intensity_target,
            }
    
    stim["img"] = img
    stim["mask"] = mask.astype(int)
    stim["shape"] = stim["img"].shape
    stim["visual_size"] =  np.array(img.shape) / ppd
    stim["ppd"] = ppd
    return stim


if __name__ == "__main__":
    from stimuli.utils import plot_stimuli
    
    params_benary = {
        "visual_size": 10,
        "ppd": 20,
        "cross_thickness": 2,
        "target_size": 1,
        }
    
    params_todo = {
        "visual_size": 10,
        "ppd": 20,
        "target_size": 1,
        "L_width": 2,
        }
    
    target_pos = {
        "target_x": (3, 6, 3, 6),
        "target_y": (4, 6, 6, 4),
        }

    # fmt: off
    stims = {
        "Benary-general": benarys_cross_generalized(**params_benary, **target_pos),
        "Benary-rectangles": benarys_cross_rectangles(**params_benary),
        "Benary-triangles": benarys_cross_triangles(**params_benary),
        "Todorovic-benary-general": todorovic_benary_generalized(**params_todo, **target_pos),
        "Todorovic-benary-rectangles": todorovic_benary_rectangles(**params_todo),
        "Todorovic-benary-triangles": todorovic_benary_triangles(**params_todo),
    }
    plot_stimuli(stims, mask=True, save=None)
