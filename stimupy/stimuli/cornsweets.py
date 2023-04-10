import numpy as np

from stimupy.components.edges import cornsweet as cornsweet_edge

__all__ = [
    "cornsweet",
]


def cornsweet(
    visual_size=None,
    ppd=None,
    shape=None,
    ramp_width=None,
    rotation=0.0,
    intensity_edges=(0.0, 1.0),
    intensity_plateau=0.5,
    exponent=2.75,
):
    """Draw rectangular Cornsweet edge stimulus.

    The 2D luminance profile of the stimulus is defined as
    Left side:
    v = vtarget + (1 - X / w) ** a * (intensity_max-vtarget) for the ramp and v = vtarget beyond.
    Right side:
    v = vtarget - (1 - X / w) ** a * (intensity_min-vtarget) for the ramp and v = vtarget beyond.
    X is the distance to the edge, w is the width of the ramp, a is a variable
    determining the steepness of the ramp, vtarget is the luminance of the targets and
    intensity_max/intensity_min are the max/min luminances.

    Parameters
    ----------
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of grating, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of grating, in pixels
    ramp_width : float
        width of luminance ramp in degrees of visual angle
    rotation : float, optional
        rotation (in degrees), counterclockwise, by default 0.0 (horizonal)
    intensity_edges : (float, float)
        intensity of edges
    intensity_plateau : float
        intensity value of plateau
    exponent : float
        determines steepness of ramp (default is 2.75. 1 would be linear)

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for each target (key: "target_mask"),
        and additional keys containing stimulus parameters

    References
    ----------
    Boyaci, H., Fang, F., Murray, S.O., Kersten, D. (2007).
        Responses to lightness variations in early human visual cortex.
        Current Biology 17, 989-993.
        https://doi.org/10.1016/j.cub.2007.05.005
    Cornsweet, T. (1970).
        Visual perception. Academic press.
        https://doi.org/10.1016/B978-0-12-189750-5.X5001-5
    """

    stim = cornsweet_edge(
        visual_size=visual_size,
        ppd=ppd,
        shape=shape,
        ramp_width=ramp_width,
        rotation=rotation,
        intensity_edges=intensity_edges,
        intensity_plateau=intensity_plateau,
        exponent=exponent,
    )

    # Generate the target mask
    mask = np.where(stim["d1"] == 1, stim["edge_mask"], 0) + np.where(
        stim["d2"] == 1, stim["edge_mask"], 0
    )
    stim["target_mask"] = mask.astype(int)
    return stim


def overview(**kwargs):
    """Generate example stimuli from this module

    Returns
    -------
    stims : dict
        dict with all stimuli containing individual stimulus dicts.
    """
    default_params = {"visual_size": 15, "ppd": 30}
    default_params.update(kwargs)

    # fmt: off
    stimuli = {
        "cornsweet": cornsweet(**default_params, ramp_width=3)
    }
    # fmt: on

    return stimuli


if __name__ == "__main__":
    from stimupy.utils import plot_stimuli

    stims = overview()
    plot_stimuli(stims, mask=False, save=None)
