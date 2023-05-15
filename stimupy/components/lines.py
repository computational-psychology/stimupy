import copy
import warnings

import numpy as np
from PIL import Image, ImageDraw

from stimupy.components.shapes import ellipse as ellipse_shape
from stimupy.utils import resolution

__all__ = [
    "line",
    "dipole",
    "ellipse",
    "circle",
]


def line(
    visual_size=None,
    ppd=None,
    shape=None,
    line_position=None,
    line_length=None,
    line_width=0,
    rotation=0.0,
    intensity_line=1,
    intensity_background=0,
    origin="corner",
):
    """Draw a line

    Parameters
    ----------
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of image, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of image, in pixels
    line_position : Sequence[Number, Number], Number, or None (default)
        line position (y, x) given the chosen origin;
        if None (default), the lines will go through the image center
    line_length : Number
        length of the line, in degrees visual angle
    line_width : Number
        width of the line, in degrees visual angle;
        if line_width=0 (default), line will be one pixel wide
    rotation : float, optional
        rotation (in degrees), counterclockwise, by default 0.0 (horizontal)
    intensity_line : Number
        intensity value of the line (default: 1)
    intensity_background : Number
        intensity value of the background (default: 0)
    origin : "corner", "mean" or "center"
        if "corner": set origin to upper left corner (default)
        if "mean" or "center": set origin to center (closest existing value to mean)

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for each line (key: "line_mask"),
        and additional keys containing stimulus parameters
    """
    if line_length is None:
        raise ValueError("line() missing argument 'line_length' which is not 'None'")

    # Resolve resolution
    shape, visual_size, ppd = resolution.resolve(shape=shape, visual_size=visual_size, ppd=ppd)
    alpha = [np.cos(np.deg2rad(rotation)), np.sin(np.deg2rad(rotation))]

    if isinstance(line_position, (float, int)) and line_position is not None:
        line_position = (line_position, line_position)

    if line_position is None:
        origin = "center"
        line_position = (-line_length * alpha[0] / 2, -line_length * alpha[1] / 2)

    if origin == "corner":
        position = (line_position[0] * ppd[0], line_position[1] * ppd[1])
    elif origin == "center" or "mean":
        position = (
            int(np.round(line_position[0] * ppd[0] + shape[0] / 2)),
            int(np.round(line_position[1] * ppd[1] + shape[1] / 2)),
        )
    else:
        raise ValueError("origin must be corner, center or mean")

    line_width_old = copy.deepcopy(line_width)
    line_width = np.round(line_width * ppd[0]) / ppd[0]
    if line_width != line_width:
        warnings.warn(f"Rounding line_width; {line_width_old} -> {line_width}")
    if line_width == 0:
        warnings.warn("line_width == 0 -> using line_width of 1px")

    # Create Pillow Image object
    img = Image.new("RGB", (shape.width, shape.height))

    # Calculate line coordinates
    coords = (
        position[::-1],
        (
            int(np.round(position[1] + line_length * alpha[1] * ppd[1])),
            int(np.round(position[0] + line_length * alpha[0] * ppd[0])),
        ),
    )

    # Create line image
    ImageDraw.Draw(img).line(coords, width=int(line_width * ppd[0]))

    # Convert to numpy array, create mask and adapt intensities
    img = np.array(img)[:, :, 0] / 255
    mask = copy.deepcopy(img)
    img = img * (intensity_line - intensity_background) + intensity_background

    stim = {
        "img": img,
        "line_mask": mask.astype(int),
        "visual_size": visual_size,
        "ppd": ppd,
        "shape": shape,
        "line_position": line_position,
        "line_length": line_length,
        "line_width": line_width,
        "rotation": rotation,
        "intensity_line": intensity_line,
        "intensity_background": intensity_background,
        "origin": origin,
    }
    return stim


def dipole(
    visual_size=None,
    ppd=None,
    shape=None,
    line_length=None,
    line_width=0,
    line_gap=None,
    rotation=0.0,
    intensity_lines=(0, 1),
):
    """Draw a two centered parallel lines

    Parameters
    ----------
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of image, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of image, in pixels
    line_length : Number
        length of the line, in degrees visual angle
    line_width : Number
        width of the line, in degrees visual angle;
        if line_width=0 (default), line will be one pixel wide
    line_gap : Number
        distance between line centers, in degrees visual angle
    rotation : float, optional
        rotation (in degrees), counterclockwise, by default 0.0 (horizonal)
    intensity_lines : (Number, Number)
        intensity value of the line (default: (0, 1));
        background intensity is the mean of these two values

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for each line (key: "line_mask"),
        and additional keys containing stimulus parameters
    """
    if line_length is None:
        raise ValueError("dipole() missing argument 'line_length' which is not 'None'")
    if line_gap is None:
        raise ValueError("dipole() missing argument 'line_gap' which is not 'None'")
    if line_gap == 0:
        raise ValueError("line_gap should be larger than 0")

    intensity_background = (intensity_lines[0] + intensity_lines[1]) / 2
    alpha1 = [np.cos(np.deg2rad(rotation)), np.sin(np.deg2rad(rotation))]
    alpha2 = [np.cos(np.deg2rad(rotation + 90)), np.sin(np.deg2rad(rotation + 90))]

    line_position1 = (
        -line_length * alpha1[0] / 2 + line_gap / 2 * alpha2[0],
        -line_length * alpha1[1] / 2 + line_gap / 2 * alpha2[1],
    )

    line_position2 = (
        -line_length * alpha1[0] / 2 - line_gap / 2 * alpha2[0],
        -line_length * alpha1[1] / 2 - line_gap / 2 * alpha2[1],
    )

    stim1 = line(
        visual_size=visual_size,
        ppd=ppd,
        shape=shape,
        line_position=line_position1,
        line_length=line_length,
        line_width=line_width,
        rotation=rotation,
        intensity_line=intensity_lines[0],
        intensity_background=intensity_background,
        origin="center",
    )

    stim2 = line(
        visual_size=visual_size,
        ppd=ppd,
        shape=shape,
        line_position=line_position2,
        line_length=line_length,
        line_width=line_width,
        rotation=rotation,
        intensity_line=intensity_lines[1] - intensity_background,
        intensity_background=0,
        origin="center",
    )

    stim1["img"] = stim1["img"] + stim2["img"]
    stim1["line_mask"] = (stim1["line_mask"] + stim2["line_mask"] * 2).astype(int)
    stim1["line_gap"] = line_gap
    stim1["intensity_lines"] = intensity_lines
    del stim1["intensity_line"]

    if line_width == 0:
        line_width = 1 / np.unique(stim1["ppd"])
    if line_width >= line_gap:
        raise ValueError("line_width should not be larger than line_gap")

    return stim1


def ellipse(
    visual_size=None,
    ppd=None,
    shape=None,
    radius=None,
    line_width=0,
    intensity_line=1,
    intensity_background=0,
):
    """Draw an ellipse

    Parameters
    ----------
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of image, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of image, in pixels
    radius : Sequence[Number, Number], Number or None (default)
        ellipse radius [ry, rx] in degrees visual angle
    line_width : Number
        width of the line, in degrees visual angle;
        if line_width=0 (default), line will be one pixel wide
    intensity_line : Number
        intensity value of the line (default: 1)
    intensity_background : Number
        intensity value of the background (default: 0)

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for each line (key: "line_mask"),
        and additional keys containing stimulus parameters
    """
    if radius is None:
        raise ValueError("ellipse() missing argument 'radius' which is not 'None'")

    # Resolve resolution
    shape, visual_size, ppd = resolution.resolve(shape=shape, visual_size=visual_size, ppd=ppd)
    if line_width * ppd[0] == 0:
        line_width_ = 1 / ppd[0]
    else:
        line_width_ = line_width

    stim = ellipse_shape(
        radius=np.array(radius),
        intensity_ellipse=intensity_line,
        visual_size=visual_size,
        ppd=ppd,
        shape=shape,
        intensity_background=intensity_background,
        origin="mean",
    )

    stim2 = ellipse_shape(
        radius=np.array(radius) - line_width_,
        visual_size=visual_size,
        ppd=ppd,
        shape=shape,
        origin="mean",
    )

    stim["img"] = np.where(stim2["ellipse_mask"] == 1, intensity_background, stim["img"])
    stim["line_mask"] = np.where(stim2["ellipse_mask"] == 1, 0, stim["ellipse_mask"])
    stim["intensity_line"] = intensity_line
    stim["line_width"] = line_width
    del stim["ellipse_mask"], stim["intensity_ellipse"]
    return stim


def circle(
    visual_size=None,
    ppd=None,
    shape=None,
    radius=None,
    line_width=0,
    intensity_line=1,
    intensity_background=0,
):
    """Draw a circle given the input parameters

    Parameters
    ----------
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of image, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of image, in pixels
    radius : Number
        radius of circle in degrees visual angle
    line_width : Number
        width of the line, in degrees visual angle;
        if line_width=0 (default), line will be one pixel wide
    intensity_line : Number
        intensity value of the line (default: 1)
    intensity_background : Number
        intensity value of the background (default: 0)

    Returns
    ----------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for each line (key: "line_mask"),
        and additional keys containing stimulus parameters
    """
    if radius is None:
        raise ValueError("circle() missing argument 'radius' which is not 'None'")
    if not isinstance(radius, (int, float)):
        raise ValueError("radius should be a single number")

    stim = ellipse(
        visual_size=visual_size,
        ppd=ppd,
        shape=shape,
        radius=radius,
        line_width=line_width,
        intensity_line=intensity_line,
        intensity_background=intensity_background,
    )
    return stim


def overview(**kwargs):
    """Generate example stimuli from this module

    Returns
    -------
    stims : dict
        dict with all stimuli containing individual stimulus dicts.
    """
    default_params = {
        "visual_size": (10, 10),
        "ppd": 10,
    }
    default_params.update(kwargs)

    p = {
        "line_length": 2,
        "line_width": 0.01,
        "rotation": 30,
    }

    # fmt: off
    stimuli = {
        "lines_line": line(**default_params, **p, origin="center"),
        "lines_dipole": dipole(**default_params, **p, line_gap=1),
        "lines_circle": circle(**default_params, radius=3),
        "lines_ellipse": ellipse(**default_params, radius=(3, 4)),}
    # fmt: on

    return stimuli


if __name__ == "__main__":
    from stimupy.utils import plot_stimuli

    stims = overview()
    plot_stimuli(stims, mask=False, save=None)
