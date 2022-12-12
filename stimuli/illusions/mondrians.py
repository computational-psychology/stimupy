import numpy as np
from stimuli.components import parallelogram
from stimuli.utils import degrees_to_pixels


__all__ = [
    "corrugated_mondrians",
]

def corrugated_mondrians(
    ppd=None,
    widths=None,
    heights=None,
    depths=None,
    target_indices=None,
    intensities=None,
    intensity_background=0.5,
):
    """
    Corrugated mondrians

    Parameters
    ----------
    ppd : int
        pixels per degree (visual angle)
    widths : float
        width of rectangles in degree visual angle
    heights : float or tuple of floats
        height of rectangles; if single float, all rectangles have the same height
    depths : float or tuple of floats
        depth of rectangles; as many depths as there are rows
    target_indices : nested tuples
        indices of targets; as many tuples as there are targets each with (x, y) indices
    intensities : nested tuples
        intensities of indiidual rectangles; as many tuples as there are rows and as many numbers in each
        tuple as there are columns
    intensity_background : float
        value for background

    Returns
    -------
    A stimulus dictionary with the stimulus ['img'] and target mask ['mask']
    """

    if isinstance(heights, (float, int)):
        heights = [heights] * len(depths)

    if any(len(lst) != len(heights) for lst in [depths, intensities]):
        raise Exception("heights, depths, and intensities need the same length.")

    widths_px = degrees_to_pixels(widths, ppd)
    heights_px = degrees_to_pixels(heights, ppd)
    depths_px = degrees_to_pixels(depths, ppd)

    nrows = len(depths)
    ncols = len(intensities[0])
    height = int(np.array(heights_px).sum())
    width = int(widths_px * ncols + np.abs(np.array(depths_px)).sum())
    img = np.ones([height, width]) * intensity_background
    mask = np.zeros([height, width])
    mval = 1

    # Initial y coordinates
    yst = 0
    yen = int(heights_px[0])

    # Calculate initial x coordinates
    xstarts = np.cumsum(np.hstack([0, depths_px]))
    temp = np.hstack([depths_px, 0])
    temp[temp > 0] = 0.0
    xstarts += temp
    xstarts += np.abs(xstarts.min())

    for r in range(nrows):
        xst = xstarts[r]
        xen = xst + int(widths_px + np.abs(depths_px[r]))

        for c in range(ncols):
            stim = parallelogram(
                visual_size=(heights[r], widths+abs(depths[r])),
                ppd=ppd,
                parallelogram_depth=depths[r],
                intensity_background=0.,
                intensity_parallelogram=intensities[r][c] - intensity_background,
                )
            
            img[yst:yen, xst:xen] += stim["img"]

            if (r, c) in target_indices:
                mask[yst:yen, xst:xen] += stim["mask"] * mval
                mval += 1

            xst += widths_px
            xen += widths_px
        yst += heights_px[r]
        yen += heights_px[r]

    # Find and delete all irrelevant columns:
    idx = np.argwhere(np.all(img == intensity_background, axis=0))
    img = np.delete(img, idx, axis=1)
    mask = np.delete(mask, idx, axis=1)

    if len(np.unique(img[mask != 0])) > 1:
        raise Exception("targets are not equiluminant.")
    
    stim = {
        "img": img,
        "mask": mask.astype(int),
        "ppd": ppd,
        "visual_size": np.array(img.shape) / ppd,
        "shape": img.shape,
        "widths": widths,
        "heights": heights,
        "depths": depths,
        "intensity_background": intensity_background,
        "intensities": intensities,
        "target_indices": target_indices,
        }
    return stim


if __name__ == "__main__":
    from stimuli.utils import plot_stim
    
    params = {
        "ppd": 10,
        "widths": 2.0,
        "heights": 2.0,
        "depths": (0.0, 1.0, 0.0, -1.0),
        "target_indices": ((1, 1), (3, 1)),
        "intensities": (
            (0.4, 0.75, 0.4, 0.75),
            (0.75, 0.4, 0.75, 1.0),
            (0.4, 0.75, 0.4, 0.75),
            (0.0, 0.4, 0.0, 0.4),)
        }

    stim = corrugated_mondrians(**params)
    plot_stim(stim, stim_name="Corrugated mondrians", mask=True, save=None)
