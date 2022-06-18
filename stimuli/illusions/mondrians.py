import numpy as np
from stimuli.utils import degrees_to_pixels, plot_stim
from stimuli.components import parallelogram


def corrugated_mondrians(
        ppd=10,
        widths=2.,
        heights=2.,
        depths=(0., 1., 0., -1.),
        values=((0.4, 0.75, 0.4, 0.75),
                (0.75, 0.4, 0.75, 1.),
                (0.4, 0.75, 0.4, 0.75),
                (0., 0.4, 0., 0.4)),
        target_idx=((1, 1), (3, 1)),
        vback=0.5
        ):

    if isinstance(heights, (float, int)):
        heights = [heights]*len(depths)

    if any(len(lst) != len(heights) for lst in [depths, values]):
        raise Exception("heights, depths, and values need the same length.")

    widths_px = degrees_to_pixels(widths, ppd)
    heights_px = degrees_to_pixels(heights, ppd)
    depths_px = degrees_to_pixels(depths, ppd)

    nrows = len(depths)
    ncols = len(values[0])
    height = int(np.array(heights_px).sum())
    width = int(widths_px*ncols + np.abs(np.array(depths_px)).sum())
    img = np.ones([height, width]) * vback
    mask = np.zeros([height, width])
    mval = 1

    # Initial y coordinates
    yst = 0
    yen = int(heights_px[0])

    # Calculate initial x coordinates
    xstarts = np.cumsum(np.hstack([0, depths_px]))
    temp = np.hstack([depths_px, 0])
    temp[temp > 0] = 0.
    xstarts += temp
    xstarts += np.abs(xstarts.min())

    for r in range(nrows):
        xst = xstarts[r]
        xen = xst + int(widths_px + np.abs(depths_px[r]))

        for c in range(ncols):
            img[yst:yen, xst:xen] += parallelogram(ppd, (heights[r], widths, depths[r]), 0., values[r][c]-vback)

            if (r, c) in target_idx:
                mask[yst:yen, xst:xen] += parallelogram(ppd, (heights[r], widths, depths[r]), 0, mval)
                mval += 1

            xst += widths_px
            xen += widths_px
        yst += heights_px[r]
        yen += heights_px[r]

    # Find and delete all irrelevant columns:
    idx = np.argwhere(np.all(img == vback, axis=0))
    img = np.delete(img, idx, axis=1)
    mask = np.delete(mask, idx, axis=1)

    if len(np.unique(img[mask != 0])) > 1:
        raise Exception("targets are not equiluminant.")
    return {"img": img, "mask": mask}


if __name__ == "__main__":
    stim = corrugated_mondrians()
    plot_stim(stim, mask=True)
