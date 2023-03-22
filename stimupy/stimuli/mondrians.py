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
    mondrian_positions=None,
    mondrian_sizes=None,
    mondrian_intensities=None,
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
    mondrian_positions : Sequence[tuple, ... ] or None (default)
        position (y, x) of each Mondrian in degrees visual angle
    mondrian_sizes : Sequence[tuple, ... ] or None (default)
        size (height, width, depth) of Mondrian parallelograms in degrees visual angle;
        if only one number is given, squares will be drawn
    mondrian_intensities : Sequence[Number, ... ] or None (default)
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
    if mondrian_positions is None:
        raise ValueError("mondrians() missing argument 'mondrian_positions' which is not 'None'")
    if mondrian_sizes is None:
        raise ValueError("mondrians() missing argument 'mondrian_sizes' which is not 'None'")
    if mondrian_intensities is None:
        raise ValueError("mondrians() missing argument 'mondrian_intensities' which is not 'None'")

    # Resolve resolution
    shape, visual_size, ppd = resolution.resolve(shape=shape, visual_size=visual_size, ppd=ppd)
    if len(np.unique(ppd)) > 1:
        raise ValueError("ppd should be equal in x and y direction")

    img = np.ones(shape) * intensity_background
    mask = np.zeros(shape)

    n_mondrians = len(mondrian_positions)

    if isinstance(mondrian_intensities, (float, int)):
        mondrian_intensities = (mondrian_intensities,) * n_mondrians

    if isinstance(mondrian_sizes, (float, int)):
        mondrian_sizes = ((mondrian_sizes, mondrian_sizes),) * n_mondrians

    if any(
        len(lst) != n_mondrians
        for lst in [mondrian_positions, mondrian_sizes, mondrian_intensities]
    ):
        raise Exception(
            "There need to be as many mondrian_positions as there are "
            "mondrian_sizes and mondrian_intensities."
        )

    mondrian_positions_px = []
    mondrian_shapes = []

    for m in range(n_mondrians):
        try:
            if len(mondrian_positions[m]) != 2:
                raise ValueError("Mondrian position tuples should be (ypos, xpos)")
        except Exception:
            raise ValueError("Mondrian position tuples should be (ypos, xpos)")

        ypos, xpos = resolution.lengths_from_visual_angles_ppd(mondrian_positions[m], ppd[0])
        individual_shapes = resolution.lengths_from_visual_angles_ppd(mondrian_sizes[m], ppd[0])

        try:
            if len(individual_shapes) == 2:
                depth = 0
                individual_shapes = individual_shapes + [
                    depth,
                ]
            elif len(individual_shapes) == 3:
                depth = mondrian_sizes[m][2]
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
        mondrian_positions_px.append(tuple([ypos, xpos]))
        mondrian_shapes.append(tuple(individual_shapes))

        # Create parallelogram
        patch = parallelogram(
            visual_size=(mondrian_sizes[m][0], mondrian_sizes[m][1] + np.abs(depth)),
            ppd=ppd,
            parallelogram_size=(mondrian_sizes[m][0], mondrian_sizes[m][1], depth),
            intensity_background=intensity_background,
            intensity_parallelogram=mondrian_intensities[m],
        )

        # Place it into Mondrian mosaic
        yshape, xshape = patch["img"].shape
        if ypos < 0 or xpos < 0:
            raise ValueError("There are no negative position coordinates")
        if (ypos + yshape > shape[0]) or (xpos + xshape > shape[1]):
            raise ValueError("Not all Mondrians fit into the stimulus")
        mask_large = np.zeros(shape)
        mask_large[ypos : ypos + yshape, xpos : xpos + xshape] = patch["shape_mask"]

        img[mask_large == 1] = mondrian_intensities[m]
        mask[mask_large == 1] = m + 1

    stim = {
        "img": img,
        "mondrian_mask": mask.astype(int),
        "ppd": ppd,
        "visual_size": visual_size,
        "shape": shape,
        "mondrian_positions": tuple(mondrian_positions),
        "mondrian_positions_px": tuple(mondrian_positions_px),
        "mondrian_sizes": tuple(mondrian_sizes),
        "mondrian_shapes": tuple(mondrian_shapes),
        "mondrian_intensities": tuple(mondrian_intensities),
        "intensity_background": intensity_background,
    }
    return stim


def corrugated_mondrian(
    visual_size=None,
    ppd=None,
    shape=None,
    mondrian_depths=None,
    mondrian_intensities=None,
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
    mondrian_depths : Sequence[Number, ... ], Number, or None (default)
        depth of Mondrian parallelograms per row
    mondrian_intensities : nested tuples
        intensities of mondrians; as many tuples as there are rows and as many
        numbers in each tuple as there are columns
    target_indices : nested tuples
        indices of targets; as many tuples as there are targets with (y, x) indices
    intensity_background : float
        intensity value for background
    intensity_target : float or None
            target intensity value. If None, use values defined in mondrian_intensities

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
    if mondrian_depths is None:
        raise ValueError(
            "corrugated_mondrians() missing argument 'mondrian_depths' which is not 'None'"
        )
    if mondrian_intensities is None:
        raise ValueError(
            "corrugated_mondrians() missing argument 'mondrian_intensities' which is not 'None'"
        )

    # Resolve resolution
    shape, visual_size, ppd = resolution.resolve(shape=shape, visual_size=visual_size, ppd=ppd)
    if len(np.unique(ppd)) > 1:
        raise ValueError("ppd should be equal in x and y direction")
    nrows = len(mondrian_intensities)
    ncols = len(mondrian_intensities[0])

    if isinstance(mondrian_depths, (float, int)):
        mondrian_depths = (mondrian_depths,) * nrows

    if len(mondrian_depths) != nrows:
        raise ValueError(
            "Unclear number of Mondrians in y-direction, check elements "
            "in mondrian_intensities and mondrian_depths"
        )

    height, width = visual_size
    mdepths_px = resolution.lengths_from_visual_angles_ppd(mondrian_depths, ppd[0])
    max_depth = np.abs(np.array(mdepths_px)).max()
    sum_depth = np.abs(np.array(mdepths_px).sum())
    red_depth = np.maximum(max_depth, sum_depth + max_depth)
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
    ints = []
    tlist = []
    target_counter = 1

    for r in range(nrows):
        xst = xstarts[r]
        if mondrian_depths[r] < 0:
            xst -= int(mondrian_depths[r] * ppd[0])

        for c in range(ncols):
            if c != ncols - 1:
                msize = (mheight_px / ppd[0], (mwidth_px + 1) / ppd[1], mondrian_depths[r])
            else:
                msize = (mheight_px / ppd[0], mwidth_px / ppd[1], mondrian_depths[r])
            mpos = (yst / ppd[0], xst / ppd[1])
            mint = mondrian_intensities[r][c]

            sizes.append(msize)
            poses.append(mpos)
            ints.append(mint)

            if (target_indices is not None) and (r, c) in target_indices:
                tlist.append(target_counter)

            xst += mwidth_px
            target_counter += 1
        yst += mheight_px

    stim = mondrian(
        visual_size=visual_size,
        ppd=ppd,
        shape=shape,
        mondrian_positions=poses,
        mondrian_sizes=sizes,
        mondrian_intensities=ints,
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

    if len(np.unique(stim["img"][target_mask != 0])) > 1:
        raise Exception("targets are not equiluminant.")
    return stim


def overview(**kwargs):
    """Generate example stimuli from this module

    Returns
    -------
    stims : dict
        dict with all stimuli containing individual stimulus dicts.
    """
    default_params = {
        "ppd": 30,
    }
    default_params.update(kwargs)

    # fmt: off
    stimuli = {
        "mondrian1": mondrian(**default_params,
                              visual_size=8,
                              mondrian_positions=((0, 0), (0, 4), (1, 3), (4, 4), (5, 1)),
                              mondrian_sizes=3,
                              mondrian_intensities=np.random.rand(5)),
        "mondrian2": mondrian(**default_params,
                              visual_size=10,
                              mondrian_positions=((0, 0), (8, 4), (1, 6), (4, 4), (5, 1)),
                              mondrian_sizes=((3, 4, 1), (2, 2, 0), (5, 4, -1), (3, 4, 1), (5, 2, 0)),
                              mondrian_intensities=np.random.rand(5)),
        "mondrian3": mondrian(**default_params,
                              visual_size=(2,6),
                              mondrian_positions=((0, 0), (0, 2)),
                              mondrian_sizes=((2, 2, 0), (2, 2, 0)),
                              mondrian_intensities=(0.2, 0.8)),
        "mondrian4": mondrian(**default_params,
                              visual_size=(2,6),
                              mondrian_positions=((0, 0), (0, 2)),
                              mondrian_sizes=((2, 2, 1), (2, 2, 1)),
                              mondrian_intensities=(0.2, 0.8)),
        "corrugated_mondrian": corrugated_mondrian(**default_params,
                                                   visual_size=10,
                                                   mondrian_depths=(1, 0, -1, 0),
                                                   mondrian_intensities=(
                                                       (0.4, 0.75, 0.4, 0.75),
                                                       (0.75, 0.4, 0.75, 1.0),
                                                       (0.4, 0.75, 0.4, 0.75),
                                                       (0.0, 0.4, 0.0, 0.4)),
                                                   target_indices=((1, 1), (3, 1)))
    }
    # fmt: on

    return stimuli


if __name__ == "__main__":
    from stimupy.utils import plot_stimuli

    stims = overview()
    plot_stimuli(stims, mask=True, save=None)
