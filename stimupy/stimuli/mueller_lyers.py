import copy

import numpy as np

from stimupy.components import lines
from stimupy.utils import resolution, stack_dicts

__all__ = [
    "mueller_lyer",
    "two_sided",
]


def mueller_lyer(
    visual_size=None,
    ppd=None,
    shape=None,
    outer_lines_length=None,
    outer_lines_angle=45,
    target_length=None,
    line_width=0,
    intensity_outer_lines=1.0,
    intensity_target=0.5,
    intensity_background=0.0,
):
    """Mueller-Lyer's (1896) illusion

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
    outer_lines_angle : Number
        angle of outer lines in degrees. Must be between -180 and 180 degrees.
    target_length : Number
        length of target line in degrees visual angle
    line_width :
        line width in degrees visual angle; if 0 (default), line width is 1 px
    intensity_outer_lines : Number
        intensity value of outer lines
    intensity_target : Number
        intensity value of target line
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
    Mueller-Lyer, F. (1896).
        Zur Lehre von den optischen Taeuschungen.
        Ueber Kontrast und Konfluxion.
        Zeitschrift fuer Psychologie und Physiologie der Sinnesorgane, IX, 1-16.
    """
    if outer_lines_length is None:
        raise ValueError(
            "mueller_lyer() missing argument 'outer_lines_length' which is not 'None'"
        )
    if target_length is None:
        raise ValueError("mueller_lyer() missing argument 'target_length' which is not 'None'")

    # Resolve resolution
    shape, visual_size, ppd = resolution.resolve(shape=shape, visual_size=visual_size, ppd=ppd)

    if outer_lines_angle > 180:
        outer_lines_angle -= 360

    if outer_lines_angle < -180 or outer_lines_angle > 180:
        raise ValueError("outer_lines_angle should be between -180 and 180 deg")

    angle1 = copy.deepcopy(outer_lines_angle) + 90
    angle2 = -angle1 - 180
    angle4 = copy.deepcopy(outer_lines_angle) - 90
    angle3 = -angle4 - 180

    target_line = lines.line(
        visual_size=visual_size,
        ppd=ppd,
        shape=shape,
        line_position=None,
        line_length=target_length,
        line_width=line_width,
        rotation=90,
        intensity_line=intensity_target - intensity_background,
        intensity_background=0,
        origin="center",
    )

    oline1 = lines.line(
        visual_size=visual_size,
        ppd=ppd,
        shape=shape,
        line_position=(0, -target_length / 2),
        line_length=outer_lines_length,
        line_width=line_width,
        rotation=angle1,
        intensity_line=intensity_outer_lines - intensity_background,
        intensity_background=0,
        origin="center",
    )

    oline2 = lines.line(
        visual_size=visual_size,
        ppd=ppd,
        shape=shape,
        line_position=(0, -target_length / 2),
        line_length=outer_lines_length,
        line_width=line_width,
        rotation=angle2,
        intensity_line=intensity_outer_lines - intensity_background,
        intensity_background=0,
        origin="center",
    )

    oline3 = lines.line(
        visual_size=visual_size,
        ppd=ppd,
        shape=shape,
        line_position=(0, target_length / 2),
        line_length=outer_lines_length,
        line_width=line_width,
        rotation=angle3,
        intensity_line=intensity_outer_lines - intensity_background,
        intensity_background=0,
        origin="center",
    )

    oline4 = lines.line(
        visual_size=visual_size,
        ppd=ppd,
        shape=shape,
        line_position=(0, target_length / 2),
        line_length=outer_lines_length,
        line_width=line_width,
        rotation=angle4,
        intensity_line=intensity_outer_lines - intensity_background,
        intensity_background=0,
        origin="center",
    )

    # Add outer lines together
    olines = oline1["img"] + oline2["img"] + oline3["img"] + oline4["img"]
    omasks1 = oline1["line_mask"] * 2 + oline2["line_mask"] * 3
    omasks2 = oline3["line_mask"] * 4 + oline4["line_mask"] * 5

    target_line["img"] += olines
    target_line["img"] = np.where(
        target_line["img"] > intensity_outer_lines, intensity_outer_lines, target_line["img"]
    )

    target_line["line_mask"] += omasks1
    target_line["line_mask"] = np.where(target_line["line_mask"] > 3, 3, target_line["line_mask"])
    target_line["line_mask"] += omasks2
    target_line["line_mask"] = np.where(target_line["line_mask"] > 5, 5, target_line["line_mask"])

    target_line["target_mask"] = np.where(target_line["line_mask"] == 1, 1, 0).astype(int)
    target_line["outer_lines_length"] = outer_lines_length
    target_line["outer_lines_angle"] = outer_lines_angle
    target_line["target_length"] = target_length
    target_line["line_width"] = line_width
    target_line["intensity_outer_lines"] = intensity_outer_lines
    target_line["intensity_target"] = intensity_target
    target_line["intensity_background"] = intensity_background
    return target_line


def two_sided(
    visual_size=None,
    ppd=None,
    shape=None,
    outer_lines_length=None,
    outer_lines_angle=45,
    target_length=None,
    line_width=0,
    intensity_outer_lines=1.0,
    intensity_target=0.5,
    intensity_background=0.0,
):
    """Two-sided Mueller-Lyer's (1896) illusion

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
    outer_lines_angle : Number
        angle of outer lines in degrees. Must be between -180 and 180 degrees.
    target_length : Number
        length of target line in degrees visual angle
    line_width :
        line width in degrees visual angle; if 0 (default), line width is 1 px
    intensity_outer_lines : Number
        intensity value of outer lines
    intensity_target : Number
        intensity value of target line
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
    Mueller-Lyer, F. (1896).
        Zur Lehre von den optischen Taeuschungen.
        Ueber Kontrast und Konfluxion.
        Zeitschrift fuer Psychologie und Physiologie der Sinnesorgane, IX, 1-16.
    """
    # Resolve resolution
    shape, visual_size, ppd = resolution.resolve(shape=shape, visual_size=visual_size, ppd=ppd)

    stim1 = mueller_lyer(
        visual_size=(visual_size[0], visual_size[1] / 2),
        ppd=ppd,
        outer_lines_length=outer_lines_length,
        outer_lines_angle=outer_lines_angle,
        target_length=target_length,
        line_width=line_width,
        intensity_outer_lines=intensity_outer_lines,
        intensity_target=intensity_target,
        intensity_background=intensity_background,
    )

    stim2 = mueller_lyer(
        visual_size=(visual_size[0], visual_size[1] / 2),
        ppd=ppd,
        outer_lines_length=outer_lines_length,
        outer_lines_angle=outer_lines_angle + 90,
        target_length=target_length,
        line_width=line_width,
        intensity_outer_lines=intensity_outer_lines,
        intensity_target=intensity_target,
        intensity_background=intensity_background,
    )

    stim = stack_dicts(stim1, stim2)
    stim["shape"] = shape
    stim["visual_size"] = visual_size
    return stim


def overview(**kwargs):
    """Generate example stimuli from this module

    Returns
    -------
    stims : dict
        dict with all stimuli containing individual stimulus dicts.
    """
    default_params = {
        "visual_size": 10,
        "ppd": 30,
    }
    default_params.update(kwargs)

    stim_params = {
        "outer_lines_length": 1,
        "outer_lines_angle": 45,
        "target_length": 3,
        "line_width": 0.1,
    }

    # fmt: off
    stimuli = {
        "mueller_lyer": mueller_lyer(**default_params, **stim_params),
        "mueller_lyer_2sided": two_sided(**default_params, **stim_params),
    }
    # fmt: on

    return stimuli


if __name__ == "__main__":
    from stimupy.utils import plot_stimuli

    stims = overview()
    plot_stimuli(stims, mask=False, save=None)
