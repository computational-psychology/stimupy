import numpy as np

from stimupy.components import draw_regions, mask_elements, waves
from stimupy.components.shapes import rectangle
from stimupy.utils.utils import round_to_vals

__all__ = [
    "frames",
    "sine_wave",
    "square_wave",
]


def mask_frames(
    edges,
    shape=None,
    visual_size=None,
    ppd=None,
    origin="mean",
):
    """Generate mask with integer indices for sequential square frames

    Parameters
    ----------
    edges : Sequence[Number, ...]
        upper-limit of each frame, in degrees visual angle
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of image, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of image, in pixels
    origin : "corner", "mean" or "center"
        if "corner": set origin to upper left corner
        if "mean": set origin to hypothetical image center (default)
        if "center": set origin to real center (closest existing value to mean)

    Returns
    -------
    dict[str, Any]
        mask with integer index for each frame (key: "frame_mask"),
        and additional keys containing stimulus parameters
    """
    stim = mask_elements(
        orientation="cityblock",
        edges=edges,
        rotation=0.0,
        shape=shape,
        visual_size=visual_size,
        ppd=ppd,
        origin=origin,
    )
    stim["frame_mask"] = stim["mask"]
    del stim["mask"]
    return stim


def frames(
    visual_size=None,
    ppd=None,
    shape=None,
    radii=None,
    intensity_frames=(1.0, 0.0),
    intensity_background=0.5,
    origin="mean",
):
    """Draw sequential set of square frames with specified radii

    Parameters
    ----------
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of image, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of image, in pixels
    radii : Sequence[Number]
        radii of each frame, in degrees visual angle
    intensity_frames : Sequence[float, ...]
        intensity value for each frame, by default (1.0, 0.0).
        Can specify as many intensities as number of frame_widths;
        If fewer intensities are passed than frame_widhts, cycles through intensities
    intensity_background : float, optional
        intensity value of background, by default 0.5
    origin : "corner", "mean" or "center"
        if "corner": set origin to upper left corner
        if "mean": set origin to hypothetical image center (default)
        if "center": set origin to real center (closest existing value to mean)

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for each frame (key: "frame_mask"),
        and additional keys containing stimulus parameters
    """
    if radii is None:
        raise ValueError("frames() missing argument 'radii' which is not 'None'")

    if np.diff(radii).min() < 0:
        raise ValueError("radii need to monotonically increase")

    # Get frames mask
    stim = mask_frames(
        edges=radii,
        shape=shape,
        visual_size=visual_size,
        ppd=ppd,
        origin=origin,
    )

    # Draw image
    stim["img"] = draw_regions(
        stim["frame_mask"], intensities=intensity_frames, intensity_background=intensity_background
    )
    return stim


def sine_wave(
    visual_size=None,
    ppd=None,
    shape=None,
    frequency=None,
    n_frames=None,
    frame_width=None,
    phase_shift=0,
    period="ignore",
    intensity_frames=(0.0, 1.0),
    intensity_background=0.5,
    origin="mean",
    clip=False,
):
    """Draw a sine-wave using cityblock distances over the whole image

    Parameters
    ----------
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of image, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of image, in pixels
    frequency : Number, or None (default)
        spatial frequency of grating, in cycles per degree visual angle
    n_frames : int, or None (default)
        number of frames in the grating
    frame_width : Number, or None (default)
        width of a single frame, in degrees visual angle
    phase_shift : float
        phase shift of grating in degrees
    period : "full", "half", "ignore" (default)
        whether to ensure the grating only has "full" periods,
        half "periods", or no guarantees ("ignore")
    intensity_frames : Sequence[float, float]
        min and max intensity of sine-wave, by default (0.0, 1.0)
    intensity_background : float (optional)
        intensity value of background, by default 0.5
    origin : "corner", "mean" or "center"
        if "corner": set origin to upper left corner
        if "mean": set origin to hypothetical image center (default)
        if "center": set origin to real center (closest existing value to mean)
    clip : Bool
        if True, clip stimulus to image size (default: False)

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for each frame (key: "frame_mask"),
        and additional keys containing stimulus parameters
    """
    lst = [visual_size, ppd, shape, frequency, n_frames, frame_width]
    if len([x for x in lst if x is not None]) < 3:
        raise ValueError(
            "'grating()' needs 3 non-None arguments for resolving from 'visual_size', "
            "'ppd', 'shape', 'frequency', 'n_frames', 'frame_width'"
        )

    sw = waves.sine(
        visual_size=visual_size,
        ppd=ppd,
        shape=shape,
        frequency=frequency,
        n_phases=n_frames,
        phase_width=frame_width,
        period=period,
        rotation=0,
        phase_shift=phase_shift,
        intensities=intensity_frames,
        origin=origin,
        round_phase_width=False,
        base_type="cityblock",
    )

    if clip:
        if origin == "corner":
            rsize = min(sw["visual_size"]) / 2
            rect = rectangle(
                visual_size=sw["visual_size"],
                ppd=sw["ppd"],
                rectangle_size=rsize,
                rectangle_position=(0, 0),
            )
        else:
            rsize = min(sw["visual_size"])
            rect = rectangle(
                visual_size=sw["visual_size"],
                ppd=sw["ppd"],
                rectangle_size=rsize,
            )
        sw["img"] = np.where(rect["shape_mask"], sw["img"], intensity_background)
        sw["mask"] = np.where(rect["shape_mask"], sw["mask"], 0)

    # Create stimulus dict
    stim = {
        "img": sw["img"],
        "frame_mask": sw["mask"].astype(int),
        "visual_size": sw["visual_size"],
        "ppd": sw["ppd"],
        "shape": sw["shape"],
        "origin": origin,
        "frequency": sw["frequency"],
        "frame_width": sw["phase_width"],
        "n_frames": sw["n_phases"],
        "period": period,
        "intensity_frames": intensity_frames,
    }
    return stim


def square_wave(
    visual_size=None,
    ppd=None,
    shape=None,
    frequency=None,
    n_frames=None,
    frame_width=None,
    phase_shift=0,
    period="ignore",
    intensity_frames=(0.0, 1.0),
    intensity_background=0.5,
    origin="mean",
    clip=False,
):
    """Draw a square-wave using cityblock distances over the whole image

    Parameters
    ----------
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of image, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of image, in pixels
    frequency : Number, or None (default)
        spatial frequency of grating, in cycles per degree visual angle
    n_frames : int, or None (default)
        number of frames in the grating
    frame_width : Number, or None (default)
        width of a single frame, in degrees visual angle
    phase_shift : float
        phase shift of grating in degrees
    period : "full", "half", "ignore" (default)
        whether to ensure the grating only has "full" periods,
        half "periods", or no guarantees ("ignore")
    intensity_frames : Sequence[float, float]
        min and max intensity of square-wave, by default (0.0, 1.0)
    intensity_background : float (optional)
        intensity value of background, by default 0.5
    origin : "corner", "mean" or "center"
        if "corner": set origin to upper left corner
        if "mean": set origin to hypothetical image center (default)
        if "center": set origin to real center (closest existing value to mean)
    clip : Bool
        if True, clip stimulus to image size (default: False)

    Returns
    ----------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for each frame (key: "frame_mask"),
        and additional keys containing stimulus parameters
    """

    stim = sine_wave(
        visual_size=visual_size,
        ppd=ppd,
        shape=shape,
        frequency=frequency,
        n_frames=n_frames,
        frame_width=frame_width,
        phase_shift=phase_shift,
        period=period,
        intensity_frames=intensity_frames,
        origin=origin,
        clip=False,
    )

    # Round sine-wave to create square wave
    stim["img"] = round_to_vals(stim["img"], intensity_frames)

    if clip:
        if origin == "corner":
            rsize = min(stim["visual_size"]) / 2
            rect = rectangle(
                visual_size=stim["visual_size"],
                ppd=stim["ppd"],
                rectangle_size=rsize,
                rectangle_position=(0, 0),
            )
        else:
            rsize = min(stim["visual_size"])
            rect = rectangle(
                visual_size=stim["visual_size"],
                ppd=stim["ppd"],
                rectangle_size=rsize,
            )
        stim["img"] = np.where(rect["shape_mask"], stim["img"], intensity_background)
        stim["frame_mask"] = np.where(rect["shape_mask"], stim["frame_mask"], 0)
    return stim


if __name__ == "__main__":
    from stimupy.utils import plot_stimuli

    stims = {
        "frames": frames(visual_size=(8, 16), frame_radii=(1, 2, 3), ppd=32),
        # "grating": grating(visual_size=(8, 16), ppd=32, frequency=1.0),
        "sine_wave": sine_wave(visual_size=(8, 16), ppd=32, frequency=0.5),
        "square_wave": square_wave(visual_size=(8, 16), ppd=32, frequency=0.5),
    }

    plot_stimuli(stims, mask=False, save=None)
