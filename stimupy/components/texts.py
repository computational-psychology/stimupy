import numpy as np
from PIL import Image, ImageDraw, ImageFont

from stimupy.utils import pad_dict_to_visual_size, resolution

__all__ = [
    "text",
]


def text(
    text,
    visual_size=None,
    ppd=None,
    shape=None,
    intensity_text=0.0,
    intensity_background=0.5,
    fontsize=36,
    align="center",
    # direction="ltr",
):
    """Draw given text into a (numpy) image-array

    If no shape is provided / can be resolved,
    tightly fits the bounding box of the drawn text.

    Parameters
    ----------
    text : str
        Text to draw
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of image, in degrees visual angle
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of image, in pixels
    intensity_text : float, optional
        intensity of text in range (0.0; 1.0), by default 0.0
    intensity_background : float, optional
        intensity value of background in range (0.0; 1.0), by default 0.5
    fontsize : int, optional
        font size, by default 36
    align : "left", "center" (default), "right"
        alignment of text, by default "center"

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for the text (key: "text_mask"),
        and additional keys containing stimulus parameters
    """

    # Try to resolve resolution
    try:
        shape, visual_size, ppd = resolution.resolve(shape=shape, visual_size=visual_size, ppd=ppd)
    except resolution.TooManyUnknownsError:
        shape = resolution.validate_shape(shape)
        visual_size = resolution.validate_visual_size(visual_size)
        ppd = resolution.validate_ppd(ppd)

    # Get font
    font = ImageDraw.ImageDraw.font
    if not font:
        try:
            # Not all machines will have Arial installed...
            font = ImageFont.truetype(
                "arial.ttf",
                fontsize,
                encoding="unic",
            )
        except OSError:
            font = ImageFont.load_default()

    # Determine dimensions of total text
    n_lines = len(text.split("\n"))
    max_length = 0
    for line in text.split("\n"):
        max_length = max(int(font.getlength(line)), max_length)
    _, top, _, bottom = font.getbbox(text)
    text_width = max_length
    text_height = int(top + bottom) * n_lines
    text_shape = (text_height, text_width)

    # Instantiate grayscale image of correct shape (in pixels)
    img = Image.new("L", (text_width, text_height), 0)
    draw = ImageDraw.Draw(img)

    # Draw text into this image
    draw.text(
        (0, 0),
        text,
        fill=1,
        font=font,
        align=align,
        # direction=direction
    )

    # Turn into mask-array
    mask = np.array(img)
    img = np.where(mask, intensity_text, intensity_background)

    # Package as dict
    stim = {
        "img": img,
        "text_mask": mask,
        "text_shape": text_shape,
    }

    # Resolve resolution
    if not shape or shape == (None, None):
        shape = text_shape
    shape, visual_size, ppd = resolution.resolve(shape=shape, visual_size=visual_size, ppd=ppd)

    # Pad
    stim = pad_dict_to_visual_size(stim, visual_size=visual_size, ppd=ppd, pad_value=0.5)

    # Output
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
        "ppd": 32,
    }
    default_params.update(kwargs)

    # fmt: off
    stimuli = {
        "text(), single line": text(text="hello world", **default_params),
        "text(), multiline": text(text="hello\nworld", **default_params)
    }
    # fmt: on

    return stimuli


if __name__ == "__main__":
    from stimupy.utils import plot_stimuli

    stims = overview()
    plot_stimuli(stims, mask=False, save=None)
