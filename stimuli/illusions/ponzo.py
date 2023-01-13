from stimuli.utils import resolution, stack_dicts
from stimuli.components import lines


__all__ = [
    "ponzo_illusion",
]

def ponzo_illusion(
    visual_size=None,
    ppd=None,
    shape=None,
    outer_lines_length=None,
    outer_lines_width=0,
    outer_lines_angle=15,
    target_lines_length=None,
    target_lines_width=0,
    target_seperation=None,
    intensity_lines=1.0,
    intensity_background=0.0,
):
    """
    Hermann grid

    Parameters
    ----------
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of grating, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of grating, in pixels
    element_size : (float, float, float)
        height, width and thickness of individual elements in degree visual angle
    intensity_background : float
        value of background
    intensity_grid : float
        value of grid

    Returns
    -------
    A stimulus dictionary with the stimulus ['img'] and target mask ['mask']
    
    References
    ----------
    Hermann L (1870). Eine Erscheinung simultanen Contrastes". Pflügers Archiv
        fuer die gesamte Physiologie. 3: 13–15. https://doi.org/10.1007/BF01855743
    """
    # Resolve resolution
    shape, visual_size, ppd = resolution.resolve(shape=shape, visual_size=visual_size, ppd=ppd)
    
    if outer_lines_angle < -45 or outer_lines_angle > 45:
        raise ValueError("outer_lines_angle should be between -45 and 45 deg")
    
    line1 = lines.line(
        ppd=ppd,
        shape=(shape[0], shape[1]/2),
        line_position=None,
        line_length=outer_lines_length,
        line_width=outer_lines_width,
        rotation=-outer_lines_angle,
        intensity_line=intensity_lines-intensity_background,
        intensity_background=0,
        origin="center",
        )

    line2 = lines.line(
        ppd=ppd,
        shape=(shape[0], shape[1]/2),
        line_position=None,
        line_length=outer_lines_length,
        line_width=outer_lines_width,
        rotation=outer_lines_angle,
        intensity_line=intensity_lines-intensity_background,
        intensity_background=0,
        origin="center",
        )
    line2["mask"] *= 2
    
    line_position1 = (-target_seperation/2, -target_lines_length/2)
    line_position2 = (target_seperation/2, -target_lines_length/2)

    line3 = lines.line(
        ppd=ppd,
        shape=shape,
        line_position=line_position1,
        line_length=target_lines_length,
        line_width=target_lines_width,
        rotation=90,
        intensity_line=intensity_lines-intensity_background,
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
        intensity_line=intensity_lines-intensity_background,
        intensity_background=0,
        origin="center",
        )
    
    line1 = stack_dicts(line1, line2)
    line1["img"] = line1["img"] + line3["img"] + line4["img"]
    line1["lines_mask"] = line1["mask"] + line3["mask"]*3 + line4["mask"]*4
    line1["mask"] = line3["mask"] + line4["mask"]*2
    return line1
        


if __name__ == "__main__":
    from stimuli.utils import plot_stim
    p1 = {
        "visual_size": 10,
        "ppd": 20,
        "outer_lines_length": 8,
        "outer_lines_angle" : 10,
        "target_lines_length": 3,
        "target_seperation": 5,
        }

    stim = ponzo_illusion(**p1)
    plot_stim(stim, stim_name="Ponzo", mask=True, save=None)
