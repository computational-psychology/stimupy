from stimupy.stimuli import *

__all__ = [
    "overview",
    "plot_overview",
    "benarys",
    "bullseyes",
    "checkerboards",
    "cornsweets",
    "cubes",
    "delboeufs",
    "dungeons",
    "edges",
    "gabors",
    "gratings",
    "hermanns",
    "mondrians",
    "mueller_lyers",
    "plaids",
    "ponzos",
    "rings",
    "sbcs",
    "todorovics",
    "waves",
    "wedding_cakes",
    "whites",
]


def overview(skip=False):
    """Generate example stimuli from this module

    Returns
    -------
    dict[str, dict]
        Dict mapping names to individual stimulus dicts
    """
    stimuli = {}
    for stimmodule_name in __all__:
        if stimmodule_name in ["overview", "plot_overview"]:
            continue

        print(f"Generating stimuli from {stimmodule_name}")
        # Get a reference to the actual module
        stimmodule = globals()[stimmodule_name]
        try:
            stims = stimmodule.overview()

            # Accumulate
            stimuli.update(stims)
        except NotImplementedError as e:
            if not skip:
                raise e
            # Skip stimuli that aren't implemented
            print("-- not implemented")
            pass

    return stimuli


def plot_overview(mask=False, save=None, units="deg"):
    """Plot overview of examples in this module (and submodules)

    Parameters
    ----------
    mask : bool or str, optional
        If True, plot mask on top of stimulus image (default: False).
        If string is provided, plot this key from stimulus dictionary as mask
    save : None or str, optional
        If None (default), do not save the plot.
        If string is provided, save plot under this name.
    units : "px", "deg" (default), or str
        what units to put on the axes, by default degrees visual angle ("deg").
        If a str other than "deg"(/"degrees") or "px"(/"pix"/"pixels") is passed,
        it must be the key to a tuple in stim

    """
    from stimupy.utils import plot_stimuli

    stims = overview(skip=True)
    plot_stimuli(stims, mask=mask, units=units, save=save)


if __name__ == "__main__":
    plot_overview()
