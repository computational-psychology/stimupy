from stimupy.components import lines
from stimupy.components.shapes import disc
from stimupy.utils import make_two_sided

__all__ = ["delboeuf", "two_sided"]


def delboeuf(
    visual_size=None,
    ppd=None,
    shape=None,
    outer_radius=None,
    outer_line_width=0,
    target_radius=None,
    intensity_outer_line=0.0,
    intensity_target=0.0,
    intensity_background=1.0,
):
    """Delboeuf's (1865) stimulus

    Parameters
    ----------
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of grating, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of grating, in pixels
    outer_radius : Number
        radius of outer circle
    outer_line_width : Number
        line width of outer circle in degrees visual angle
        if 0 (default), set line width to 1 px
    target_radius : Number
        radius of target circle
    intensity_outer_line : Number
        intensity value of outer circle line (default: 0)
    intensity_target : Number
        intensity value of target (default: 0)
    intensity_background : Number
        intensity value of background (default: 1)

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for the target (key: "target_mask"),
        and additional keys containing stimulus parameters

    References
    ----------
    Delboeuf, F. J. (1865).
        Note sur certaines illusions d'optique:
        Essai d'une théorie psychophysique de la maniere
        dont l'oeil apprécie les distances et les angles.
        Bulletins de l'Académie Royale des Sciences, Lettres et
        Beaux-arts de Belgique, 19, 195-216.
    """
    if outer_radius is None:
        raise ValueError("delboeuf() missing argument 'outer_radius' which is not 'None'")
    if target_radius is None:
        raise ValueError("delboeuf() missing argument 'target_radius' which is not 'None'")

    outer = lines.circle(
        visual_size=visual_size,
        ppd=ppd,
        shape=shape,
        radius=outer_radius,
        line_width=outer_line_width,
        intensity_line=intensity_outer_line - intensity_background,
        intensity_background=0,
    )

    inner = disc(
        radius=target_radius,
        intensity_disc=intensity_target - intensity_background,
        visual_size=visual_size,
        ppd=ppd,
        shape=shape,
        intensity_background=0,
    )

    inner["img"] = outer["img"] + inner["img"] + intensity_background
    inner["line_mask"] = outer["line_mask"]
    inner["outer_radius"] = outer_radius
    inner["target_radius"] = target_radius
    inner["target_mask"] = inner.pop("ring_mask")
    inner["outer_line_width"] = outer["line_width"]
    inner["intensity_outer_line"] = intensity_outer_line
    inner["intensity_target"] = intensity_target
    return inner


two_sided = make_two_sided(
    delboeuf,
    two_sided_params=(
        "outer_radius",
        "outer_line_width",
        "target_radius",
        "intensity_target",
        "intensity_outer_line",
    ),
)


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
        "delboeuf": delboeuf(**default_params, target_radius=1, outer_radius=4),
        "delboeuf_2sided": two_sided(**default_params, target_radius=1, outer_radius=(2, 1.1)),
    }
    # fmt: on

    return stimuli


if __name__ == "__main__":
    from stimupy.utils import plot_stimuli

    stims = overview()
    plot_stimuli(stims, mask=False, save=None)
