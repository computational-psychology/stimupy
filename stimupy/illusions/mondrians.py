import numpy as np

from stimupy.components.mondrians import mondrians
from stimupy.utils import degrees_to_pixels, resolution

__all__ = [
    "corrugated_mondrians",
]


def corrugated_mondrians(
    visual_size=None,
    ppd=None,
    shape=None,
    mondrian_depths=None,
    mondrian_intensities=None,
    target_indices=None,
    intensity_background=0.5,
):
    """Corrugated Mondrians

    Parameters
    ----------
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of image, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of image, in pixels
    mondrian_depths : Sequence[Number, ... ], NUmber, or None (default)
        depth of Mondrian parallelograms per row
    mondrian_intensities : nested tuples
        intensities of mondrians; as many tuples as there are rows and as many
        numbers in each tuple as there are columns
    target_indices : nested tuples
        indices of targets; as many tuples as there are targets with (y, x) indices
    intensity_background : float
        intensity value for background

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
    mdepths_px = degrees_to_pixels(mondrian_depths, ppd[0])
    max_depth = np.abs(np.array(mdepths_px)).max()
    sum_depth = np.array(mdepths_px).sum()
    red_depth = np.maximum(max_depth, sum_depth)
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

    stim = mondrians(
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

    if len(np.unique(stim["img"][target_mask != 0])) > 1:
        raise Exception("targets are not equiluminant.")
    return stim


if __name__ == "__main__":
    from stimupy.utils import plot_stim

    p = {
        "visual_size": 10,
        "ppd": 30,
        "mondrian_depths": (1, 0, -1, 0),
        "mondrian_intensities": (
            (0.4, 0.75, 0.4, 0.75),
            (0.75, 0.4, 0.75, 1.0),
            (0.4, 0.75, 0.4, 0.75),
            (0.0, 0.4, 0.0, 0.4),
        ),
        "target_indices": ((1, 1), (3, 1)),
    }

    stim = corrugated_mondrians(**p)
    plot_stim(stim, stim_name="corrugated_mondrians", mask=True, save=None)
