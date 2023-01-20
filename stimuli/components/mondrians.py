import numpy as np

from stimuli.components.shapes import parallelogram
from stimuli.utils import resolution, degrees_to_pixels

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
        mondrian_sizes = ((mondrian_sizes, mondrian_sizes), ) * n_mondrians

    if any(len(lst) != n_mondrians for lst in [mondrian_positions, mondrian_sizes, mondrian_intensities]):
        raise Exception("There need to be as many mondrian_positions as there are "
                        "mondrian_sizes and mondrian_intensities.")

    mondrian_positions_px = []
    mondrian_shapes = []

    for m in range(n_mondrians):
        try:
            if len(mondrian_positions[m]) != 2:
                raise ValueError("Mondrian position tuples should be (ypos, xpos)")
        except Exception:
            raise ValueError("Mondrian position tuples should be (ypos, xpos)")

        ypos, xpos = degrees_to_pixels(mondrian_positions[m], ppd[0])
        individual_shapes = degrees_to_pixels(mondrian_sizes[m], ppd[0])

        try:
            if len(individual_shapes) == 2:
                depth = 0
                individual_shapes = individual_shapes + [depth,]
            elif len(individual_shapes) == 3:
                depth = mondrian_sizes[m][2]
            else:
                raise ValueError("Mondrian size tuples should be (height, width) for "
                                 "rectangles or (height, width, depth) for parallelograms")
        except Exception:
            raise ValueError("Mondrian size tuples should be (height, width) for"
                             "rectangles or (height, width, depth) for parallelograms")
        
        if depth < 0:
            xpos += int(depth*ppd[0])
        mondrian_positions_px.append(tuple([ypos, xpos]))
        mondrian_shapes.append(tuple(individual_shapes))

        # Create parallelogram
        patch = parallelogram(
            visual_size=(mondrian_sizes[m][0], mondrian_sizes[m][1]+np.abs(depth)),
            ppd=ppd,
            parallelogram_size=(mondrian_sizes[m][0], mondrian_sizes[m][1], depth),
            intensity_background=intensity_background,
            intensity_parallelogram=mondrian_intensities[m],
        )
        
        # Place it into Mondrian mosaic
        yshape, xshape = patch["img"].shape
        if ypos < 0 or xpos < 0:
            raise ValueError("There are no negative position coordinates")
        if (ypos+yshape > shape[0]) or (xpos+xshape > shape[1]):
            raise ValueError("Not all Mondrians fit into the stimulus")
        mask_large = np.zeros(shape)
        mask_large[ypos:ypos+yshape, xpos:xpos+xshape] = patch["mask"]

        img[mask_large == 1] = mondrian_intensities[m]
        mask[mask_large == 1] = m+1
    
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
    from stimuli.utils.plotting import plot_stimuli
    
    p1 = {
        "mondrian_positions": ((0,0), (0,4), (1,3), (4,4), (5,1)),
        "mondrian_sizes": 3,
        "mondrian_intensities": np.random.rand(5),
        }
    
    p2 = {
        "mondrian_positions": ((0,0), (8,4), (1,6), (4,4), (5,1)),
        "mondrian_sizes": ((3,4,1), (2,2,0), (5,4,-1), (3,4,1), (5,2,0)),
        "mondrian_intensities": np.random.rand(5),
        }
    
    p3 = {
        "mondrian_positions": ((0,0), (0, 2)),
        "mondrian_sizes": ((2,2,0), (2,2,0)),
        "mondrian_intensities": (0.2, 0.8),
        }
    
    p4 = {
        "mondrian_positions": ((0,0), (0, 2)),
        "mondrian_sizes": ((2,2,1), (2,2,1)),
        "mondrian_intensities": (0.2, 0.8),
        }
    
    stims = {
        "mondrians1": mondrians(visual_size=8, ppd=10, **p1),
        "mondrians2": mondrians(visual_size=10, ppd=10, **p2),
        "mondrians3": mondrians(visual_size=(2, 6), ppd=10, **p3),
        "mondrians4": mondrians(visual_size=(2, 6), ppd=10, **p4),
        }
    
    plot_stimuli(stims)