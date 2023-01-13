import numpy as np
from PIL import Image, ImageDraw
import copy
import warnings

from stimuli.utils import resolution

__all__ = [
    "line",
]


def line(
    visual_size=None,
    ppd=None,
    shape=None,
    line_position=None,
    line_length=None,
    line_width=0,
    rotation=0,
    intensity_line=1,
    intensity_background=0,
    origin="corner",
    ):
    """Draw a line given the input parameters

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
    rotation : float
        rotation of grating in degrees (default: 0 = horizontal)
    intensity_line : Number
        intensity value of the line (default: 1)
    intensity_background : Number
        intensity value of the background (default: 0)
    origin : "corner", "mean" or "center"
        if "corner": set origin to upper left corner (default)
        if "mean" or "center": set origin to center (closest existing value to mean)

    Returns
    ----------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for each target (key: "mask"),
        and additional keys containing stimulus parameters
    """
    
    # Resolve resolution
    shape, visual_size, ppd = resolution.resolve(shape=shape, visual_size=visual_size, ppd=ppd)
    alpha = [np.cos(np.deg2rad(rotation)), np.sin(np.deg2rad(rotation))]
    
    if isinstance(line_position, (float, int)) and line_position is not None:
        line_position = (line_position, line_position)

    if line_position is None:
        origin = "center"
        line_position = (-line_length*alpha[0] / 2,
                         -line_length*alpha[1] / 2)
    
    if origin == "corner":
        position = (line_position[0]*ppd[0], line_position[1]*ppd[1])
    elif origin == "center" or "mean":
        position = (int(np.round(line_position[0]*ppd[0]+shape[0]/2)),
                    int(np.round(line_position[1]*ppd[1]+shape[1]/2)))
    else:
        raise ValueError("origin must be corner, center or mean")
    
    line_width_old = copy.deepcopy(line_width)
    line_width = np.round(line_width*ppd[0]) / ppd[0]
    if line_width != line_width:
        warnings.warn(f"Rounding line_width; {line_width_old} -> {line_width}")
    if line_width == 0:
        warnings.warn("line_width == 0 -> using line_width of 1px")
    
    # Create Pillow Image object
    img = Image.new("RGB", (shape.width, shape.height))
    
    # Calculate line coordinates
    coords = (position[::-1], (int(np.round(position[1]+line_length*alpha[1]*ppd[1])),
                               int(np.round(position[0]+line_length*alpha[0]*ppd[0]))))
    
    # Create line image
    ImageDraw.Draw(img).line(coords, width=int(line_width*ppd[0]))
    
    # Convert to numpy array, create mask and adapt intensities
    img = np.array(img)[:,:,0] / 255
    mask = copy.deepcopy(img)
    img = img * (intensity_line - intensity_background) + intensity_background
    
    stim = {
        "img": img,
        "mask": mask.astype(int),
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
    line_seperation=None,
    rotation=0,
    intensity_lines=(0, 1),
    ):
    """Draw a two centered parallel lines given the input parameters

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
    line_seperation : Number
        distance between line centers, in degrees visual angle
    rotation : float
        rotation of grating in degrees (default: 0 = horizontal)
    intensity_lines : (Number, Number)
        intensity value of the line (default: (0, 1));
        background intensity is the mean of these two values

    Returns
    ----------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for each target (key: "mask"),
        and additional keys containing stimulus parameters
    """
    if line_seperation == 0:
        raise ValueError("line_seperation should not be 0")
    if line_width > line_seperation:
        raise ValueError("line_width cannot be larger than line_seperation")
    
    intensity_background = (intensity_lines[0] + intensity_lines[1]) / 2
    alpha1 = [np.cos(np.deg2rad(rotation)), np.sin(np.deg2rad(rotation))]
    alpha2 = [np.cos(np.deg2rad(rotation+90)), np.sin(np.deg2rad(rotation+90))]

    line_position1 = (-line_length*alpha1[0]/2 + line_seperation/2*alpha2[0],
                      -line_length*alpha1[1]/2 + line_seperation/2*alpha2[1])
    
    line_position2 = (-line_length*alpha1[0]/2 - line_seperation/2*alpha2[0],
                      -line_length*alpha1[1]/2 - line_seperation/2*alpha2[1])

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
        intensity_line=intensity_lines[1]-intensity_background,
        intensity_background=0,
        origin="center",
        )
    
    stim1["img"] = stim1["img"] + stim2["img"]
    
    return stim1


if __name__ == "__main__":
    from stimuli.utils.plotting import plot_stimuli

    p1 = {
        "visual_size": (10, 5),
        "ppd": 10,
        "line_length": 2,
        "line_width": 0.01,
        "rotation": 30,
        # "line_position": (5, 1),
        # "origin": "center"
    }

    stims = {
        "line": line(**p1),
        "dipole": dipole(**p1, line_seperation=1),
    }
    plot_stimuli(stims, mask=False)
