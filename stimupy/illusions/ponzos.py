from stimupy.components import lines
from stimupy.utils import resolution, stack_dicts

__all__ = [
    "ponzo",
]


def ponzo(
    visual_size=None,
    ppd=None,
    shape=None,
    outer_lines_length=None,
    outer_lines_width=0,
    outer_lines_angle=15,
    target_lines_length=None,
    target_lines_width=0,
    target_distance=None,
    intensity_outer_lines=1.0,
    intensity_target_lines=0.5,
    intensity_background=0.0,
):
    """Ponzo's (1910) illusion

    Parameters
    ----------
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of grating, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of grating, in pixels
    outer_lines_length : Number
        length of outer lines in degrees visual angle
    outer_lines_width : Number
        line width of outer lines in degrees visual angle
        if 0 (default), set line width to 1 px
    outer_lines_angle : Number
        angle of outer lines in degrees. Must be between -45 and 45 degrees.
    target_lines_length : Number
        length of target lines in degrees visual angle
    target_lines_width :
        line width of target lines in degrees visual angle
        if 0 (default), set line width to 1 px
    target_distance : Number
        distance between target lines in degrees visual angle
    intensity_outer_lines : Number or (Number, Number)
        intensity value(s) of outer lines
    intensity_target_lines : Number or (Number, Number)
        intensity value(s) of target lines
    intensity_background : Number
        intensity value of background

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for each target (key: "target_mask"),
        and additional keys containing stimulus parameters

    References
    ----------
    Ponzo, M. (1910).
        Intorno ad alcune illusioni nel campo delle sensazioni tattili,
        sull'illusione di Aristotele e fenomeni analoghi.
        Wilhelm Engelmann.
    """
    if outer_lines_length is None:
        raise ValueError("ponzo() missing argument 'outer_lines_length' which is not 'None'")
    if target_lines_length is None:
        raise ValueError("ponzo() missing argument 'target_lines_length' which is not 'None'")
    if target_distance is None:
        raise ValueError("ponzo() missing argument 'target_distance' which is not 'None'")

    # Resolve resolution
    shape, visual_size, ppd = resolution.resolve(shape=shape, visual_size=visual_size, ppd=ppd)

    if outer_lines_angle < -45 or outer_lines_angle > 45:
        raise ValueError("outer_lines_angle should be between -45 and 45 deg")
    if isinstance(intensity_outer_lines, (float, int)):
        intensity_outer_lines = (intensity_outer_lines, intensity_outer_lines)
    if isinstance(intensity_target_lines, (float, int)):
        intensity_target_lines = (intensity_target_lines, intensity_target_lines)

    line1 = lines.line(
        ppd=ppd,
        shape=(shape[0], shape[1] / 2),
        line_position=None,
        line_length=outer_lines_length,
        line_width=outer_lines_width,
        rotation=-outer_lines_angle,
        intensity_line=intensity_outer_lines[0] - intensity_background,
        intensity_background=0,
        origin="center",
    )

    line2 = lines.line(
        ppd=ppd,
        shape=(shape[0], shape[1] / 2),
        line_position=None,
        line_length=outer_lines_length,
        line_width=outer_lines_width,
        rotation=outer_lines_angle,
        intensity_line=intensity_outer_lines[1] - intensity_background,
        intensity_background=0,
        origin="center",
    )

    line_position1 = (-target_distance / 2, -target_lines_length / 2)
    line_position2 = (target_distance / 2, -target_lines_length / 2)

    line3 = lines.line(
        ppd=ppd,
        shape=shape,
        line_position=line_position1,
        line_length=target_lines_length,
        line_width=target_lines_width,
        rotation=90,
        intensity_line=intensity_target_lines[0] - intensity_background,
        intensity_background=0,
        origin="center",
    )

    line4 = lines.line(
        ppd=ppd,
        shape=shape,
        line_position=line_position2,
        line_length=target_lines_length,
        line_width=target_lines_width,
        rotation=90,
        intensity_line=intensity_target_lines[1] - intensity_background,
        intensity_background=0,
        origin="center",
    )

    line1 = stack_dicts(line1, line2)
    line1["img"] += line3["img"] + line4["img"] + intensity_background
    line1["line_mask"] += line3["line_mask"] * 3 + line4["line_mask"] * 4
    line1["target_mask"] = line3["line_mask"] + line4["line_mask"] * 2
    return line1


if __name__ == "__main__":
    from stimupy.utils import plot_stim

    p1 = {
        "visual_size": 10,
        "ppd": 20,
        "outer_lines_length": 8,
        "outer_lines_angle": 10,
        "target_lines_length": 3,
        "target_distance": 5,
    }

    stim = ponzo(**p1)
    plot_stim(stim, stim_name="ponzo", mask=True, save=None)
