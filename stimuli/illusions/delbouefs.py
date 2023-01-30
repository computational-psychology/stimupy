from stimuli.components import lines
from stimuli.components.shapes import disc


__all__ = [
    "delboeuf",
]

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
    """
    Delboeuf stimulus

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
    ----------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for the target (key: "target_mask"),
        and additional keys containing stimulus parameters
    
    References
    ----------
    Delboeuf, F. J. (1865). Note sur certaines illusions d’optique: Essai d'une
        théorie psychophysique de la maniere dont l’oeil apprécie les distances
        et les angles. Bulletins de l’Académie Royale des Sciences, Lettres et
        Beaux-arts de Belgique, 19, 195-216.
    """

    outer = lines.circle(
        visual_size=visual_size,
        ppd=ppd,
        shape=shape,
        radius=outer_radius,
        line_width=outer_line_width,
        intensity_line=intensity_outer_line-intensity_background,
        intensity_background=0,
        )
    
    inner = disc(
        radius=target_radius,
        intensity_discs=intensity_target-intensity_background,
        visual_size=visual_size,
        ppd=ppd,
        shape=shape,
        intensity_background=0,
        )

    inner["img"] = outer["img"] + inner["img"] + intensity_background
    inner["line_mask"] = outer["line_mask"]
    return inner
        


if __name__ == "__main__":
    from stimuli.utils import plot_stim
    p1 = {
        "visual_size": 10,
        "ppd": 30,
        "outer_radius": 4,
        "target_radius": 3,
        }

    stim = delboeuf(**p1)
    plot_stim(stim, stim_name="delboeuf", mask=True, save=None)
