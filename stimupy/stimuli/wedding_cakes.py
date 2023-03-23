import numpy as np

from stimupy.utils import resolution
from stimupy.utils.filters import convolve

__all__ = [
    "wedding_cake",
]


def wedding_cake(
    visual_size=None,
    ppd=None,
    shape=None,
    L_size=None,
    target_height=None,
    target_indices1=None,
    target_indices2=None,
    intensity_bars=(1.0, 0.0),
    intensity_target=0.5,
):
    """Wedding cake stimulus

    Parameters
    ----------
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of grating, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of grating, in pixels
    L_size : (float, float, float)
        size of individual jags (height, width, thickness) in degree visual angle
    target_height : float
        height of targets in degree visual angle
    target_indices1 : nested tuples
        target indices with intensity1-value; as many tuples as there are targets
        each with (y, x) indices
    target_indices2 : nested tuples
        target indices with intensity2-value; as many tuples as there are targets
        each with (y, x) indices
    intensity_bars : (float, float)
        intensity values of the bars
    intensity_target : float
        intensity value of targets

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for the target (key: "target_mask"),
        and additional keys containing stimulus parameters

    References
    ----------
    Clifford, C. W. G., & Spehar, B. (2003).
        Using colour to disambiguate contrast and assimilation in White's effect.
        Journal of Vision, 3, 294a.
        https://doi.org/10.1167/3.9.294
    """
    if L_size is None:
        raise ValueError("wedding_cake() missing argument 'L_size' which is not 'None'")

    # Resolve resolution
    shape, visual_size, ppd_ = resolution.resolve(shape=shape, visual_size=visual_size, ppd=ppd)
    if len(np.unique(ppd)) > 1:
        raise ValueError("ppd should be equal in x and y direction")
    if visual_size[1] < visual_size[0] * 0.75 or visual_size[1] > visual_size[0] * 1.25:
        raise ValueError(
            "wedding_cake not available for images with very different heights+widths"
        )

    nY, nX = shape
    Ly, Lx, Lw = resolution.lengths_from_visual_angles_ppd(L_size, np.unique(ppd))
    Lyh, Lxh = int(Ly / 2) + 1, int(Lx / 2) + 1
    if Lw > Ly / 2:
        raise ValueError("L-thickness should not exceed L_height / 2")

    # Create L-shaped patch
    L_patch = np.zeros([Ly, Lx])
    L_patch[0:Lw, 0:Lx] = 1
    L_patch[0:Ly, Lx - Lw : :] = 1

    # We initially create a larger image array to avoid boundary problems
    nY, nX = nY * 2, nX * 2

    # Create grid-like array to create wedding cake pattern
    array1 = np.zeros([nY, nX])
    ys, xs = np.arange(0, nY, Ly - Lw), np.arange(0, nX, Lx)
    n = np.minimum(len(ys), len(xs))
    array1[ys[0:n], xs[0:n]] = np.arange(1, n + 1)

    array2 = np.zeros([nY, nX])
    ys, xs = np.arange(0, nY, Lw * 2), np.arange(0, nX, Lw * 2)
    n = np.minimum(len(ys), len(xs))
    array2[ys[0:n], xs[0:n]] = np.arange(1, n + 1)
    array2 = np.rot90(array2)
    amax = int((array2.max() + 1) / 2)

    array3 = convolve(array1, array2, "same")

    if target_indices1 is not None and target_height is not None:
        # Create target patch2
        theight = resolution.lengths_from_visual_angles_ppd(target_height, np.unique(ppd))
        tpatch1 = np.zeros(L_patch.shape)
        tpatch1[int(Ly / 2 - theight / 2) : int(Ly / 2 + theight / 2), Lx - Lw : :] = (
            -intensity_bars[1] + intensity_target
        )

        array_t1 = np.zeros(array3.shape)
        for ty, tx in target_indices1:
            arr1 = np.copy(array1)
            arr2 = np.copy(array2)
            arr1[arr1 != ty + 2] = 0
            arr2[arr2 != tx + amax] = 0
            array_t1 += convolve(arr1, arr2, "same")
        array_t1[array_t1 < 1] = 0
        array_t1[array_t1 > 1] = 1
        t1 = np.round(convolve(array_t1, tpatch1, "same"), 5)
        t1 = t1[Lyh : Lyh + int(nY / 2), Lxh : Lxh + int(nX / 2)]

    else:
        t1 = np.zeros([int(nY / 2), int(nX / 2)])

    if target_indices2 is not None and target_height is not None:
        # Create target patch2
        theight = resolution.lengths_from_visual_angles_ppd(target_height, np.unique(ppd))
        tpatch2 = np.zeros(L_patch.shape)
        tpatch2[int(Ly / 2 - theight / 2) : int(Ly / 2 + theight / 2), Lx - Lw : :] = (
            -intensity_bars[0] + intensity_target
        )

        array_t2 = np.zeros(array3.shape)
        for ty, tx in target_indices2:
            arr1 = np.copy(array1)
            arr2 = np.copy(array2)
            arr1[arr1 != ty + 2] = 0
            arr2[arr2 != tx + amax] = 0
            array_t2 += convolve(arr1, arr2, "same")
        array_t2[array_t2 < 1] = 0
        array_t2[array_t2 > 1] = 1
        t2 = np.round(convolve(array_t2, tpatch2, "same"), 5)
        t2 = t2[Lyh - Lw : Lyh + int(nY / 2) - Lw, Lxh + Lw : Lxh + int(nX / 2) + Lw]

    else:
        t2 = np.zeros([int(nY / 2), int(nX / 2)])

    # Create wedding cake pattern
    imgt = convolve(array3, L_patch, "same")
    imgt = np.round(imgt)
    img = np.copy(imgt)
    img[imgt > 1] = intensity_bars[1]
    img[imgt < 1] = intensity_bars[0]
    img = img[Lyh : Lyh + int(nY / 2), Lxh : Lxh + int(nX / 2)]

    # Create target mask
    mask = np.abs(t1 * 1.0 / intensity_target) + np.abs(t2 * 2.0 / intensity_target)
    mask = np.round(mask).astype(int)

    # Add targets
    img = img + t1
    img = img + t2

    stim = {
        "img": img,
        "target_mask": mask.astype(int),
        "shape": shape,
        "visual_size": visual_size,
        "ppd": ppd,
        "L_size": L_size,
        "target_height": target_height,
        "intensity_bars": intensity_bars,
        "intensity_target": intensity_target,
        "target_indices1": target_indices1,
        "target_indices2": target_indices2,
    }

    return stim


def overview(**kwargs):
    """Generate example stimuli from this module

    Returns
    -------
    stims : dict
        dict with all stimuli containing individual stimulus dicts.
    """
    default_params = {
        "visual_size": 15,
        "ppd": 10,
    }
    default_params.update(kwargs)

    # fmt: off
    stimuli = {
        "wedding_cake": wedding_cake(**default_params,
                                     L_size= (4, 3, 1),
                                     target_height=1,
                                     target_indices1=((2, 2), (2, 1)),
                                     target_indices2=((2, -1), (2, 0)),
                                     )
    }
    # fmt: on

    return stimuli


if __name__ == "__main__":
    from stimupy.utils import plot_stimuli

    stims = overview()
    plot_stimuli(stims, mask=False, save=None)
