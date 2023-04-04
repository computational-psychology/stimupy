import warnings

import numpy as np

from stimupy.components.shapes import cross, rectangle, triangle
from stimupy.utils import resolution

__all__ = [
    "cross_generalized",
    "cross_rectangles",
    "cross_triangles",
    "todorovic_generalized",
    "todorovic_rectangles",
    "todorovic_triangles",
]


def cross_generalized(
    visual_size=None,
    ppd=None,
    shape=None,
    cross_thickness=None,
    target_size=None,
    target_type="r",
    target_rotation=0.0,
    target_x=None,
    target_y=None,
    intensity_background=1.0,
    intensity_cross=0.0,
    intensity_target=0.5,
):
    """Benary's Cross Illusion

    Parameters
    ----------
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of grating, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of grating, in pixels
    cross_thickness : float
        width of the cross bars in degrees visual angle
    target_size : (float, float)
        size of all target(s) in degrees visual angle
    target_type : tuple of strings
        type of targets to use; option: r (rectangle), t (triangle); as many targets as types
    target_rotation : tuple of floats, or float
        tuple with rotation of targets in deg, counterclockwise, as many targets as rotations
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
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for each target (key: "target_mask"),
        and additional keys containing stimulus parameters

    References
    ----------
    Benary, W. (1924).
        Beobachtungen zu einem Experiment über Helligkeitskontrast.
        Psychologische Forschung, 5, 131-142.
        https://doi.org/10.1007/BF00402398
    """
    if cross_thickness is None:
        raise ValueError(
            "cross_generalized() missing argument 'cross_thickness' which is not 'None'"
        )

    # Create cross
    cross_stim = cross(
        visual_size=visual_size,
        ppd=ppd,
        shape=shape,
        cross_size=visual_size,
        cross_arm_ratios=1.0,
        cross_thickness=cross_thickness,
        intensity_background=intensity_background,
        intensity_cross=intensity_cross,
    )

    # Add targets
    stim = add_targets(
        cross_stim["img"],
        np.unique(ppd),
        target_size,
        target_type,
        target_rotation,
        target_x,
        target_y,
        intensity_target,
    )

    del cross_stim["img"]
    return {**stim, **cross_stim}


def cross_rectangles(
    visual_size=None,
    ppd=None,
    shape=None,
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
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of grating, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of grating, in pixels
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
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for each target (key: "target_mask"),
        and additional keys containing stimulus parameters

    References
    ----------
    Benary, W. (1924).
        Beobachtungen zu einem Experiment über Helligkeitskontrast.
        Psychologische Forschung, 5, 131-142.
        https://doi.org/10.1007/BF00402398
    """
    if cross_thickness is None:
        raise ValueError(
            "cross_rectangles() missing argument 'cross_thickness' which is not 'None'"
        )

    # Resolve resolution
    shape, visual_size, ppd = resolution.resolve(shape=shape, visual_size=visual_size, ppd=ppd)
    if len(np.unique(ppd)) > 1:
        raise ValueError("ppd should be equal in x and y direction")

    if target_size is None:
        raise ValueError("target_size cannot be None")
    if isinstance(target_size, (float, int)):
        target_size = (target_size, target_size)
    if target_size[0] > cross_thickness:
        raise ValueError("Target size is larger than cross thickness")

    # Calculate target placement for classical Benarys cross
    theight, twidth = resolution.shape_from_visual_size_ppd(target_size, ppd)
    cheight, cwidth = resolution.shape_from_visual_size_ppd(cross_thickness, ppd)

    target_x = (
        (shape[1] / 2 - cwidth / 2 - twidth) / ppd[1],
        (shape[1] - twidth) / ppd[1],
    )

    target_y = (
        (shape[0] / 2 - cheight / 2 - theight) / ppd[0],
        (shape[0] / 2 - cheight / 2) / ppd[0],
    )

    stim = cross_generalized(
        visual_size=visual_size,
        ppd=ppd,
        shape=shape,
        cross_thickness=cross_thickness,
        target_size=target_size,
        target_type=("r",) * 2,
        target_rotation=0.0,
        target_x=np.round(np.array(target_x) * ppd) / ppd,
        target_y=np.round(np.array(target_y) * ppd) / ppd,
        intensity_background=intensity_background,
        intensity_cross=intensity_cross,
        intensity_target=intensity_target,
    )
    return stim


def cross_triangles(
    visual_size=None,
    ppd=None,
    shape=None,
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
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of grating, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of grating, in pixels
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
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for each target (key: "target_mask"),
        and additional keys containing stimulus parameters

    References
    ----------
     Benary, W. (1924).
        Beobachtungen zu einem Experiment über Helligkeitskontrast.
        Psychologische Forschung, 5, 131-142.
        https://doi.org/10.1007/BF00402398
    """
    if cross_thickness is None:
        raise ValueError(
            "cross_triangles() missing argument 'cross_thickness' which is not 'None'"
        )

    # Resolve resolution
    shape, visual_size, ppd = resolution.resolve(shape=shape, visual_size=visual_size, ppd=ppd)
    if len(np.unique(ppd)) > 1:
        raise ValueError("ppd should be equal in x and y direction")

    if target_size is None:
        raise ValueError("target_size cannot be None")
    if isinstance(target_size, (float, int)):
        target_size = (target_size, target_size)
    if target_size[0] != target_size[1]:
        raise ValueError("target needs to have the same height and width")
    if np.sqrt(target_size[0] ** 2 * 2.0) / 2.0 > cross_thickness:
        raise ValueError("Target size is larger than cross thickness")

    # Calculate target placement for classical Benarys cross
    theight, twidth = resolution.shape_from_visual_size_ppd(target_size, ppd)
    cheight, cwidth = resolution.shape_from_visual_size_ppd(cross_thickness, ppd)

    target_x = (
        (shape[1] / 2 - cwidth / 2 - twidth) / ppd[1],
        (shape[1] / 2 + cwidth / 2) / ppd[1],
    )

    target_y = (
        (shape[0] / 2 - cheight / 2 - theight) / ppd[0],
        (shape[0] / 2 - cheight / 2) / ppd[0],
    )

    stim = cross_generalized(
        visual_size=visual_size,
        ppd=ppd,
        shape=shape,
        cross_thickness=cross_thickness,
        target_size=target_size,
        target_type=("t",) * 2,
        target_rotation=(90.0, 45.0),
        target_x=np.round(np.array(target_x) * ppd) / ppd,
        target_y=np.round(np.array(target_y) * ppd) / ppd,
        intensity_background=intensity_background,
        intensity_cross=intensity_cross,
        intensity_target=intensity_target,
    )
    return stim


def todorovic_generalized(
    visual_size=None,
    ppd=None,
    shape=None,
    L_width=None,
    target_size=None,
    target_type="r",
    target_rotation=0.0,
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
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of grating, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of grating, in pixels
    L_width : float
        width of L in degree visual angle
    target_size : (float, float)
        size of all target(s) in degrees visual angle
    target_type : tuple of strings
        type of targets to use; option: r (rectangle), t (triangle); as many targets as types
    target_rotation : tuple of floats, or float
        tuple with rotation of targets in deg, counterclockwise, as many targets as rotations
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
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for each target (key: "target_mask"),
        and additional keys containing stimulus parameters

    References
    ----------
    Benary, W. (1924).
        Beobachtungen zu einem Experiment über Helligkeitskontrast.
        Psychologische Forschung, 5, 131-142.
        https://doi.org/10.1007/BF00402398
    """
    if L_width is None:
        raise ValueError("todorovic_generalized() missing argument 'L_width' which is not 'None'")

    # Resolve resolution
    shape, visual_size, ppd = resolution.resolve(shape=shape, visual_size=visual_size, ppd=ppd)
    if len(np.unique(ppd)) > 1:
        raise ValueError("ppd should be equal in x and y direction")

    if L_width > visual_size[1] / 2:
        raise ValueError("L_width cannot be larger than stimulus_width / 2")

    L_size = (visual_size[0] / 2, visual_size[0] / 2, L_width, visual_size[1] - L_width)
    top, bottom, left, right = resolution.lengths_from_visual_angles_ppd(L_size, np.unique(ppd))
    width, height = left + right, top + bottom

    # Create stimulus without targets
    mask = np.zeros(shape).astype(int)
    mask[:, 0:left] = 1
    mask[height - bottom : :, 0 : width - left] = 1
    img = np.where(mask, intensity_cross, intensity_background)

    # Add targets
    stim = add_targets(
        img,
        np.unique(ppd),
        target_size,
        target_type,
        target_rotation,
        target_x,
        target_y,
        intensity_target,
    )

    # Add missing parameter information
    stim["visual_size"] = visual_size
    stim["ppd"] = ppd
    stim["shape"] = shape
    stim["L_width"] = L_width
    stim["intensity_background"] = intensity_background
    stim["intensity_cross"] = intensity_cross
    stim["L_mask"] = mask
    return stim


def todorovic_rectangles(
    visual_size=None,
    ppd=None,
    shape=None,
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
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of grating, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of grating, in pixels
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
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for each target (key: "target_mask"),
        and additional keys containing stimulus parameters

    References
    ----------
    Benary, W. (1924).
        Beobachtungen zu einem Experiment über Helligkeitskontrast.
        Psychologische Forschung, 5, 131-142.
        https://doi.org/10.1007/BF00402398
    """
    if L_width is None:
        raise ValueError("todorovic_rectangles() missing argument 'L_width' which is not 'None'")

    # Resolve resolution
    shape, visual_size, ppd = resolution.resolve(shape=shape, visual_size=visual_size, ppd=ppd)
    if len(np.unique(ppd)) > 1:
        raise ValueError("ppd should be equal in x and y direction")

    if target_size is None:
        raise ValueError("target_size cannot be None")
    if isinstance(target_size, (float, int)):
        target_size = (target_size, target_size)

    # Calculate target placement for classical Todorovic-Benary
    target_x = (L_width, visual_size[1] - L_width - target_size[1])
    target_y = (visual_size[0] / 2.0 - target_size[0], visual_size[0] / 2.0)

    stim = todorovic_generalized(
        visual_size=visual_size,
        ppd=ppd,
        L_width=L_width,
        target_size=target_size,
        target_type=("r",) * 2,
        target_rotation=0.0,
        target_x=np.round(np.array(target_x) * ppd) / ppd,
        target_y=np.round(np.array(target_y) * ppd) / ppd,
        intensity_background=intensity_background,
        intensity_cross=intensity_cross,
        intensity_target=intensity_target,
    )
    return stim


def todorovic_triangles(
    visual_size=None,
    ppd=None,
    shape=None,
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
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of grating, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of grating, in pixels
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
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for each target (key: "target_mask"),
        and additional keys containing stimulus parameters

    References
    ----------
     Benary, W. (1924).
        Beobachtungen zu einem Experiment über Helligkeitskontrast.
        Psychologische Forschung, 5, 131-142.
        https://doi.org/10.1007/BF00402398
    """
    if L_width is None:
        raise ValueError("todorovic_triangles() missing argument 'L_width' which is not 'None'")

    # Resolve resolution
    shape, visual_size, ppd = resolution.resolve(shape=shape, visual_size=visual_size, ppd=ppd)
    if len(np.unique(ppd)) > 1:
        raise ValueError("ppd should be equal in x and y direction")

    if target_size is None:
        raise ValueError("target_size cannot be None")
    if isinstance(target_size, (float, int)):
        target_size = (target_size, target_size)
    else:
        raise ValueError("target_size should be a single float")

    # Calculate target placement for classical Todorovic-Benary
    target_x = (L_width, visual_size[1] - L_width - target_size[1])
    target_y = (visual_size[0] / 2.0 - target_size[0], visual_size[0] / 2.0)

    stim = todorovic_generalized(
        visual_size=visual_size,
        ppd=ppd,
        L_width=L_width,
        target_size=target_size,
        target_type=("t",) * 2,
        target_rotation=(0.0, 180.0),
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
    target_rotation,
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
    target_rotation : tuple of floats, or float
        tuple with rotation of targets in deg, counterclockwise, as many targets as rotations
    target_x : tuple of floats
        tuple with x coordinates of targets in degrees, as many targets as coordinates
    target_y : tuple of floats
        tuple with y coordinates of targets in degrees, as many targets as coordinates
    intensity_target : float
        intensity value for target

    Returns
    -------
    dict[str, Any]
        dict with the updated stimulus (key: "img"),
        mask with integer index for each target (key: "target_mask"),
        and additional keys containing stimulus parameters
    """

    mask = np.zeros(img.shape)

    # If any target information is missing, dont add targets
    if (
        (target_size is None)
        or (target_type is None)
        or (target_rotation is None)
        or (target_x is None)
        or (target_y is None)
    ):
        warnings.warn("Target information is missing - no target added")
        stim = {
            "target_size": None,
            "target_type": None,
            "target_rotation": None,
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
        if isinstance(target_rotation, (float, int)):
            target_rotation = [target_rotation]
        if isinstance(target_x, (float, int)):
            target_x = [target_x]
        if isinstance(target_y, (float, int)):
            target_y = [target_y]
        if np.min(target_x) < 0:
            raise ValueError("Leftmost target does not fit into image")
        if np.min(target_y) < 0:
            raise ValueError("Topmost target does not fit into image")

        n_targets = np.max(
            np.array([len(target_type), len(target_rotation), len(target_x), len(target_y)])
        )

        if len(target_type) == 1:
            target_type = target_type * n_targets
        if len(target_rotation) == 1:
            target_rotation = target_rotation * n_targets
        if len(target_x) == 1:
            target_x = target_x * n_targets
        if len(target_y) == 1:
            target_y = target_y * n_targets

        if any(len(lst) != n_targets for lst in [target_rotation, target_x, target_y]):
            raise Exception(
                "target_type, target_rotation, target_x and target_y need the same length."
            )

        theight, twidth = resolution.lengths_from_visual_angles_ppd(target_size, ppd)
        ty = resolution.lengths_from_visual_angles_ppd(target_y, ppd)
        tx = resolution.lengths_from_visual_angles_ppd(target_x, ppd)

        if isinstance(ty, (int, float)):
            ty = (ty,)
            tx = (tx,)

        if (twidth + np.array(tx)).max() > img.shape[1]:
            raise ValueError("Rightmost target does not fit in image.")
        if (theight + np.array(ty)).max() > img.shape[0]:
            raise ValueError("Lowest target does not fit in image.")

        # Add targets:
        for i in range(len(target_x)):
            if target_type[i] == "r":
                target = rectangle(
                    shape=[theight * 2, twidth * 2],
                    ppd=ppd,
                    rectangle_size=(theight / ppd, twidth / ppd),
                    intensity_rectangle=intensity_target,
                    intensity_background=0,
                    rotation=target_rotation[i],
                )
                mpatch = target["rectangle_mask"][~np.all(target["rectangle_mask"] == 0, axis=1)]
                tpatch = target["img"][~np.all(target["rectangle_mask"] == 0, axis=1)]

            elif target_type[i] == "t":
                target = triangle(
                    shape=[theight * 3, twidth * 3],
                    ppd=ppd,
                    triangle_size=(theight / ppd, twidth / ppd),
                    intensity_background=0,
                    intensity_triangle=intensity_target,
                    rotation=target_rotation[i],
                    include_corners=True,
                )
                mpatch = target["triangle_mask"][~np.all(target["triangle_mask"] == 0, axis=1)]
                tpatch = target["img"][~np.all(target["triangle_mask"] == 0, axis=1)]

            else:
                raise Exception("You can only use r or t as shapes")

            # Remove zero-rows and -columns
            tpatch = tpatch[:, ~np.all(mpatch == 0, axis=0)]
            mpatch = mpatch[:, ~np.all(mpatch == 0, axis=0)]
            theight_, twidth_ = tpatch.shape

            if ty[i] + theight_ > img.shape[0] or tx[i] + twidth_ > img.shape[1]:
                raise ValueError("At least one target does not fully fit into stimulus")

            # Only change the target parts of the image:
            mlarge = np.zeros(img.shape)
            mlarge[ty[i] : ty[i] + theight_, tx[i] : tx[i] + twidth_] = mpatch
            tlarge = np.zeros(img.shape)
            tlarge[ty[i] : ty[i] + theight_, tx[i] : tx[i] + twidth_] = tpatch
            img = np.where(mlarge, tlarge, img)
            mask = np.where(mlarge, i + 1, mask)

        stim = {
            "target_size": target_size,
            "target_type": target_type,
            "target_rotation": target_rotation,
            "target_x": target_x,
            "target_y": target_y,
            "intensity_target": intensity_target,
        }

    stim["img"] = img
    stim["target_mask"] = mask.astype(int)
    return stim


def overview(**kwargs):
    """Generate example stimuli from this module

    Returns
    -------
    stims : dict
        dict with all stimuli containing individual stimulus dicts.
    """
    default_params = {
        "visual_size": 10,
        "ppd": 30,
    }
    default_params.update(kwargs)

    params_benary = {
        "target_size": 1,
        "cross_thickness": 2,
    }

    params_todo = {
        "target_size": 1,
        "L_width": 2,
    }

    target_pos = {
        "target_x": (3, 6, 3, 6),
        "target_y": (4, 6, 6, 4),
    }

    # fmt: off
    stimuli = {
        "benarys_cross_general": cross_generalized(**default_params, **params_benary, **target_pos),
        "benarys_cross_rectangles": cross_rectangles(**default_params, **params_benary),
        "benarys_cross_triangles": cross_triangles(**default_params, **params_benary),
        "benarys_todorovic_general": todorovic_generalized(**default_params, **params_todo, **target_pos),
        "benarys_todorovic_rectangles": todorovic_rectangles(**default_params, **params_todo),
        "benarys_todorovic_triangles": todorovic_triangles(**default_params, **params_todo),
    }
    # fmt: on

    return stimuli


if __name__ == "__main__":
    from stimupy.utils import plot_stimuli

    stims = overview()
    plot_stimuli(stims, mask=False, save=None)
