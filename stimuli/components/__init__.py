import numpy as np

from .components import *
from .components import image_base


def mask_elements(
    orientation,
    edges,
    rotation=0.0,
    shape=None,
    visual_size=None,
    ppd=None,
):
    """Generate mask with integer indices for consecutive elements

    Parameters
    ----------
    orientation : any of keys in stimuli.components.image_base()
        which dimension to mask over
    edges : Sequence[Number]
        upper-limit of each consecutive elements
    rotation : float, optional
        angle of rotation (in degrees) of segments,
        counterclockwise away from 3 o'clock, by default 0.0
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of image, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of image, in pixels

    Returns
    ----------
    dict[str, Any]
        mask with integer index for each angular segment (key: "mask"),
        and additional keys containing stimulus parameters
    """

    # Set up coordinates
    base = image_base(shape=shape, visual_size=visual_size, ppd=ppd, rotation=rotation)
    distances = base[orientation]

    # Mark elements with integer idx-value
    mask = np.zeros(shape, dtype=int)
    for idx, edge in zip(reversed(range(len(edges))), reversed(edges)):
        mask[distances <= edge] = int(idx + 1)

    # Assemble output
    return {
        "mask": mask,
        "edges": edges,
        "orientation": orientation,
        "rotation": base["rotation"],
        "shape": base["shape"],
        "visual_size": base["visual_size"],
        "ppd": base["ppd"],
    }
