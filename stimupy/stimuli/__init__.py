from stimupy.stimuli import *

__all__ = [
    "overview",
    "benarys",
    "bullseyes",
    "checkerboards",
    "cornsweets",
    "cubes",
    "delboeufs",
    "dungeons",
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


if __name__ == "__main__":
    from stimupy.utils import plot_stimuli

    stims = overview()
    plot_stimuli(stims, mask=False, save=None)
