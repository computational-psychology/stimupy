import numpy as np

from stimupy.components.shapes import parallelogram
from stimupy.utils import resolution

__all__ = [
    "mondrians",
]


def mondrians(
    visual_size=None,
    ppd=None,
    shape=None,
    mondrian_positions=None,
    mondrian_sizes=None,
    mondrian_intensities=None,
    intensity_background=0.5,
):
    """Draw Mondrians of given size and intensity at given position

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


if __name__ == "__main__":
    from stimupy.utils.plotting import plot_stimuli

    p1 = {
        "mondrian_positions": ((0, 0), (0, 4), (1, 3), (4, 4), (5, 1)),
        "mondrian_sizes": 3,
        "mondrian_intensities": np.random.rand(5),
    }

    p2 = {
        "mondrian_positions": ((0, 0), (8, 4), (1, 6), (4, 4), (5, 1)),
        "mondrian_sizes": ((3, 4, 1), (2, 2, 0), (5, 4, -1), (3, 4, 1), (5, 2, 0)),
        "mondrian_intensities": np.random.rand(5),
    }

    p3 = {
        "mondrian_positions": ((0, 0), (0, 2)),
        "mondrian_sizes": ((2, 2, 0), (2, 2, 0)),
        "mondrian_intensities": (0.2, 0.8),
    }

    p4 = {
        "mondrian_positions": ((0, 0), (0, 2)),
        "mondrian_sizes": ((2, 2, 1), (2, 2, 1)),
        "mondrian_intensities": (0.2, 0.8),
    }

    stims = {
        "mondrians1": mondrians(visual_size=8, ppd=10, **p1),
        "mondrians2": mondrians(visual_size=10, ppd=10, **p2),
        "mondrians3": mondrians(visual_size=(2, 6), ppd=10, **p3),
        "mondrians4": mondrians(visual_size=(2, 6), ppd=10, **p4),
    }

    plot_stimuli(stims, mask=False)
