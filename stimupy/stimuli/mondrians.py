import itertools

import numpy as np

from stimupy.components.shapes import parallelogram
from stimupy.utils import resolution

__all__ = [
    "mondrian",
    "corrugated_mondrian",
]


def mondrian(
    visual_size=None,
    ppd=None,
    shape=None,
    positions=None,
    sizes=None,
    intensities=None,
    intensity_background=0.5,
):
    """Draw Mondrian of given size and intensity at given position

    Parameters
    ----------
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of image, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of image, in pixels
    positions : Sequence[tuple, ... ] or None (default)
        position (y, x) of each Mondrian in degrees visual angle
    sizes : Sequence[tuple, ... ] or None (default)
        size (height, width, depth) of Mondrian parallelograms in degrees visual angle;
        if only one number is given, squares will be drawn
    intensities : Sequence[Number, ... ] or None (default)
        intensity values of each Mondrian, if only one number is given
        all will have the same intensity
    intensity_background : float
        intensity value of background

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for each Mondrian (key: "mondrian_mask"),
        and additional keys containing stimulus parameters
    """
    if positions is None:
        raise ValueError("mondrians() missing argument 'positions' which is not 'None'")
    if sizes is None:
        raise ValueError("mondrians() missing argument 'sizes' which is not 'None'")
    if intensities is None:
        raise ValueError("mondrians() missing argument 'intensities' which is not 'None'")

    # Resolve resolution
    shape, visual_size, ppd = resolution.resolve(shape=shape, visual_size=visual_size, ppd=ppd)
    if len(np.unique(ppd)) > 1:
        raise ValueError("ppd should be equal in x and y direction")

    img = np.ones(shape) * intensity_background
    mask = np.zeros(shape)

    n_mondrians = len(positions)
    ints = itertools.cycle(intensities)

    if isinstance(sizes, (float, int)):
        sizes = ((sizes, sizes),) * n_mondrians

    if any(len(lst) != n_mondrians for lst in [positions, sizes]):
        raise Exception("As many positions as sizes required.")

    epositions_px = []
    eshapes = []

    for m in range(n_mondrians):
        try:
            if len(positions[m]) != 2:
                raise ValueError("Position tuples should be (ypos, xpos)")
        except Exception:
            raise ValueError("Position tuples should be (ypos, xpos)")

        ypos, xpos = resolution.lengths_from_visual_angles_ppd(positions[m], ppd[0])
        individual_shapes = resolution.lengths_from_visual_angles_ppd(sizes[m], ppd[0])

        try:
            if len(individual_shapes) == 2:
                depth = 0
                individual_shapes = individual_shapes + [
                    depth,
                ]
            elif len(individual_shapes) == 3:
                depth = sizes[m][2]
            else:
                raise ValueError(
                    "Mondrian size tuples should be (height, width) for "
                    "rectangles or (height, width, depth) for parallelograms"
                )
        except Exception:
            raise ValueError(
                "Mondrian size tuples should be (height, width) for"
                "rectangles or (height, width, depth) for parallelograms"
            )

        if depth < 0:
            xpos += int(depth * ppd[0])
        epositions_px.append(tuple([ypos, xpos]))
        eshapes.append(tuple(individual_shapes))

        # Create parallelogram
        patch = parallelogram(
            visual_size=(sizes[m][0], sizes[m][1] + np.abs(depth)),
            ppd=ppd,
            parallelogram_size=(sizes[m][0], sizes[m][1], depth),
        )

        # Place it into Mondrian mosaic
        yshape, xshape = patch["img"].shape
        if ypos < 0 or xpos < 0:
            raise ValueError("There are no negative position coordinates")
        if (ypos + yshape > shape[0]) or (xpos + xshape > shape[1]):
            raise ValueError("Not all Mondrians fit into the stimulus")
        mask_large = np.zeros(shape)
        mask_large[ypos : ypos + yshape, xpos : xpos + xshape] = patch["parallelogram_mask"]

        img[mask_large == 1] = next(ints)
        mask[mask_large == 1] = m + 1

    stim = {
        "img": img,
        "mondrian_mask": mask.astype(int),
        "ppd": ppd,
        "visual_size": visual_size,
        "shape": shape,
        "positions": tuple(positions),
        "sizes": tuple(sizes),
        "intensities": tuple(intensities),
        "intensity_background": intensity_background,
    }
    return stim


def corrugated_mondrian(
    visual_size=None,
    ppd=None,
    shape=None,
    nrows=None,
    ncols=None,
    depths=0,
    intensities=(0, 1),
    target_indices=None,
    intensity_background=0.5,
    intensity_target=None,
):
    """Corrugated Mondrian

    Parameters
    ----------
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of image, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of image, in pixels
    depths : Sequence[Number, ... ], Number, or None (default)
        depth of Mondrian parallelograms per row
    intensities : nested tuples
        intensities of mondrians; as many tuples as there are rows and as many
        numbers in each tuple as there are columns
    target_indices : nested tuples
        indices of targets; as many tuples as there are targets with (y, x) indices
    intensity_background : float
        intensity value for background
    intensity_target : float
            target intensity. If None, use values defined in intensities

    Returns
    ------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for each target (key: "target_mask"),
        and additional keys containing stimulus parameters

    References
    ----------
    Adelson, E. H. (1993).
        Perceptual organization and the judgment of brightness.
        Science, 262, 2042-2044.
        https://doi.org/10.1126/science.8266102
    """

    # Resolve resolution
    shape, visual_size, ppd = resolution.resolve(shape=shape, visual_size=visual_size, ppd=ppd)
    if len(np.unique(ppd)) > 1:
        raise ValueError("ppd should be equal in x and y direction")

    if nrows is None:
        nrows = len(intensities)

    try:
        if ncols is None:
            ncols = len(intensities[0])
    except Exception():
        ncols = nrows

    if isinstance(depths, (float, int)):
        depths = (depths,) * nrows

    if len(depths) != nrows:
        raise ValueError("Unclear number of rows. Check nrows, intensities and depths.")

    ints = itertools.cycle(tuple(np.array(intensities).flatten()))

    height, width = visual_size
    mdepths_px = resolution.lengths_from_visual_angles_ppd(depths, ppd[0])

    s1 = sum(i for i in mdepths_px if i > 0)
    s2 = sum(-i for i in mdepths_px if i < 0)
    sum_depth = np.maximum(abs(s1), abs(s2))
    r1 = np.cumsum(np.array(mdepths_px)).max()
    r2 = np.cumsum(np.array(mdepths_px)).min()
    red_depth = np.maximum(abs(r1), abs(r2))
    red_depth = np.maximum(red_depth, sum_depth)
    mheight_px, mwidth_px = int(shape[0] / nrows), int((shape[1] - red_depth) / ncols)

    # Initial y coordinates
    yst = 0

    # Calculate initial x coordinates
    xstarts = np.cumsum(np.hstack([0, mdepths_px]))
    temp = np.hstack([mdepths_px, 0])
    temp[temp > 0] = 0.0
    xstarts += temp
    xstarts += np.abs(xstarts.min())

    sizes = []
    poses = []
    intenses = []
    tlist = []
    target_counter = 1
    counter = 0

    for r in range(nrows):
        xst = xstarts[r]
        if depths[r] < 0:
            xst -= int(depths[r] * ppd[0])

        for c in range(ncols):
            if c != ncols - 1:
                msize = (mheight_px / ppd[0], (mwidth_px + 1) / ppd[1], depths[r])
            else:
                msize = (mheight_px / ppd[0], mwidth_px / ppd[1], depths[r])
            mpos = (yst / ppd[0], xst / ppd[1])
            mint = next(ints)

            sizes.append(msize)
            poses.append(mpos)
            intenses.append(mint)

            if (target_indices is not None) and (r, c) in target_indices:
                tlist.append(target_counter)

            xst += mwidth_px
            target_counter += 1
            counter += 1
        yst += mheight_px

    stim = mondrian(
        visual_size=visual_size,
        ppd=ppd,
        shape=shape,
        positions=poses,
        sizes=sizes,
        intensities=intenses,
        intensity_background=intensity_background,
    )

    target_mask = np.zeros(shape)
    for t in range(len(tlist)):
        target_mask[stim["mondrian_mask"] == tlist[t]] = t + 1

    stim["target_mask"] = target_mask.astype(int)
    stim["target_indices"] = target_indices

    if intensity_target is not None:
        for t in range(len(tlist)):
            stim["img"] = np.where(target_mask == t + 1, intensity_target, stim["img"])

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

    # fmt: off
    stimuli = {
        "mondrian": mondrian(**default_params,
                             positions=((0, 0), (8, 4), (1, 6), (4, 4), (5, 1)),
                             sizes=((3, 4, 1), (2, 2, 0), (5, 4, -1), (3, 4, 1), (5, 2, 0)),
                             intensities=np.random.rand(5)),
        "corrugated_mondrian": corrugated_mondrian(**default_params,
                                                   depths=(1, 0, -1, 0),
                                                   intensities=np.random.rand(4, 4),
                                                   target_indices=((1, 1), (3, 1))),
        "corrugated_mondrian2": corrugated_mondrian(**default_params,
                                                    nrows=5,
                                                    ncols=5,
                                                    depths=(1, -1, 0, -1, 1),
                                                    intensities=(0, 1))
    }
    # fmt: on

    return stimuli


if __name__ == "__main__":
    from stimupy.utils import plot_stimuli

    stims = overview()
    plot_stimuli(stims, mask=False, save=None)
