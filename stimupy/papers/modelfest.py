"""Modelfest dataset from Carney et al (1999) https://doi.org/10.1117/12.348473

This module reproduces all of the stimuli from the Modelfest dataset
prior to the spatiotemporal extension as described in Carney et al (1999)
but normalized between 0 and 1.
More information on Modelfest can be found here:
https://www.visionscience.com/data/modelfest/

Each stimulus is provided by a separate function,
a full list can be found as stimupy.papers.modelfest.__all__

The output of each of these functions is a stimulus dictionary.

For a visual representation of all the stimuli and their mask,
simply run this module as a script:

    $ python stimuli/papers/modelfest.py

Attributes
----------
__all__ (list of str): list of all stimulus-functions
    that are exported by this module when executing
        >>> from stimupy.papers.modelfest import *

References
-----------
Carney, T., Klein, S. A., Tyler, C. W., Silverstein, A. D., Beutter, B., Levi, D.,
    ... & Eckstein, M. P. (1999).
    Development of an image/threshold database
    for designing and testing human vision models.
    Proceedings of SPIE, 3644, 542-551.
    https://doi.org/10.1117/12.348473
"""

from pathlib import Path

import numpy as np
import pandas as pd

from stimupy import checkerboards
from stimupy.components import gaussians, lines, shapes
from stimupy.components.edges import gaussian as gaussian_edge
from stimupy.components.waves import bessel
from stimupy.noises.binaries import binary as binary_noise
from stimupy.stimuli.gabors import gabor
from stimupy.stimuli.plaids import gabors as plaid
from stimupy.utils import pad_dict_to_shape, resize_dict, roll_dict, stack_dicts

__all__ = [
    "GaborPatch1",
    "GaborPatch2",
    "GaborPatch3",
    "GaborPatch4",
    "GaborPatch5",
    "GaborPatch6",
    "GaborPatch7",
    "GaborPatch8",
    "GaborPatch9",
    "GaborPatch10",
    "GaborPatch11",
    "GaborPatch12",
    "GaborPatch13",
    "GaborPatch14",
    "ElongatedGabor15",
    "ElongatedGabor16",
    "ElongatedGabor17",
    "Baguette18",
    "Baguette19",
    "Baguette20",
    "Baguette21",
    "Subthreshold22",
    "Subthreshold23",
    "Subthreshold24",
    "Subthreshold25",
    "Gaussians26",
    "Gaussians27",
    "Gaussians28",
    "Gaussians29",
    "Edge30",
    "Line31",
    "Dipole32",
    "GaborString33",
    "GaborString34",
    "Noise35",
    "Orientation36",
    "Orientation37",
    "Plaids38",
    "Plaids39",
    "Disk40",
    "Bessel41",
    "Checkerboard42",
    "NaturalScene43",
]

# Default values:
PPD = 120  # pixel size of 0.5 arcmin
PPD2 = 60  # pixel size of 1 arcmin (pixel replication)

mean_lum = 0.5

df = pd.read_csv(Path(__file__).parents[0] / "modelfest_data.csv", header=None)
participants = df[0]


def gen_all(ppd=PPD, skip=False):
    stims = {}  # save the stimulus-dicts in a larger dict, with name as key
    for stim_name in __all__:
        print(f"Generating modelfest.{stim_name}")

        # Get a reference to the actual function
        func = globals()[stim_name]
        try:
            stim = func(ppd=ppd)

            # Accumulate
            stims[stim_name] = stim
        except NotImplementedError as e:
            if not skip:
                raise e
            # Skip stimuli that aren't implemented
            print("-- not implemented")
            pass

    return stims


def GaborPatch1(ppd=PPD):
    """GaborPatch1 with fixed size in degrees, Carney et al (1999)
    Frequency: 1.12 cpd
    Gaussian window: sx=sy=0.5 deg

    Parameters
    ----------
    ppd : Sequence[Number, Number], Number, or None
        pixels per degree [vertical, horizontal]

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img") and additional keys containing
        stimulus parameters

    References
    ----------
    Carney, T., Klein, S. A., Tyler, C. W., Silverstein, A. D., Beutter, B., Levi, D.,
        ... & Eckstein, M. P. (1999).
        Development of an image/threshold database
        for designing and testing human vision models.
        Proceedings of SPIE, 3644, 542-551.
        https://doi.org/10.1117/12.348473
    """

    params = {
        "visual_size": 256 / PPD,
        "ppd": ppd,
        "frequency": 1.12,
        "sigma": 0.5,
        "rotation": -90,
        "phase_shift": 90,
        "origin": "center",
    }

    stim = gabor(**params)

    v = 1
    experimental_data = {
        "participants": participants,
        "thresholds1": df[v],
        "thresholds2": df[v + 1],
        "thresholds3": df[v + 2],
        "thresholds4": df[v + 3],
    }
    return {**stim, "experimental_data": experimental_data}


def GaborPatch2(ppd=PPD):
    """GaborPatch2 with fixed size in degrees, Carney et al (1999)
    Frequency: 2 cpd
    Gaussian window: sx=sy=0.5 deg

    Parameters
    ----------
    ppd : Sequence[Number, Number], Number, or None
        pixels per degree [vertical, horizontal]

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img") and additional keys containing
        stimulus parameters

    References
    ----------
    Carney, T., Klein, S. A., Tyler, C. W., Silverstein, A. D., Beutter, B., Levi, D.,
        ... & Eckstein, M. P. (1999).
        Development of an image/threshold database
        for designing and testing human vision models.
        Proceedings of SPIE, 3644, 542-551.
        https://doi.org/10.1117/12.348473
    """

    params = {
        "visual_size": 256 / PPD,
        "ppd": ppd,
        "frequency": 2,
        "sigma": 0.5,
        "rotation": -90,
        "phase_shift": 90,
        "origin": "center",
    }

    stim = gabor(**params)

    v = 5
    experimental_data = {
        "participants": participants,
        "thresholds1": df[v],
        "thresholds2": df[v + 1],
        "thresholds3": df[v + 2],
        "thresholds4": df[v + 3],
    }
    return {**stim, "experimental_data": experimental_data}


def GaborPatch3(ppd=PPD):
    """GaborPatch3 with fixed size in degrees, Carney et al (1999)
    Frequency: 2.83 cpd
    Gaussian window: sx=sy=0.5 deg

    Parameters
    ----------
    ppd : Sequence[Number, Number], Number, or None
        pixels per degree [vertical, horizontal]

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img") and additional keys containing
        stimulus parameters

    References
    ----------
    Carney, T., Klein, S. A., Tyler, C. W., Silverstein, A. D., Beutter, B., Levi, D.,
        ... & Eckstein, M. P. (1999).
        Development of an image/threshold database
        for designing and testing human vision models.
        Proceedings of SPIE, 3644, 542-551.
        https://doi.org/10.1117/12.348473
    """

    params = {
        "visual_size": 256 / PPD,
        "ppd": ppd,
        "frequency": 2.83,
        "sigma": 0.5,
        "rotation": -90,
        "phase_shift": 90,
        "origin": "center",
    }

    stim = gabor(**params)

    v = 9
    experimental_data = {
        "participants": participants,
        "thresholds1": df[v],
        "thresholds2": df[v + 1],
        "thresholds3": df[v + 2],
        "thresholds4": df[v + 3],
    }
    return {**stim, "experimental_data": experimental_data}


def GaborPatch4(ppd=PPD):
    """GaborPatch4 with fixed size in degrees, Carney et al (1999)
    Frequency: 4 cpd
    Gaussian window: sx=sy=0.5 deg

    Parameters
    ----------
    ppd : Sequence[Number, Number], Number, or None
        pixels per degree [vertical, horizontal]

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img") and additional keys containing
        stimulus parameters

    References
    ----------
    Carney, T., Klein, S. A., Tyler, C. W., Silverstein, A. D., Beutter, B., Levi, D.,
        ... & Eckstein, M. P. (1999).
        Development of an image/threshold database
        for designing and testing human vision models.
        Proceedings of SPIE, 3644, 542-551.
        https://doi.org/10.1117/12.348473
    """

    params = {
        "visual_size": 256 / PPD,
        "ppd": ppd,
        "frequency": 4,
        "sigma": 0.5,
        "rotation": -90,
        "phase_shift": 90,
        "origin": "center",
    }

    stim = gabor(**params)

    v = 13
    experimental_data = {
        "participants": participants,
        "thresholds1": df[v],
        "thresholds2": df[v + 1],
        "thresholds3": df[v + 2],
        "thresholds4": df[v + 3],
    }
    return {**stim, "experimental_data": experimental_data}


def GaborPatch5(ppd=PPD):
    """GaborPatch5 with fixed size in degrees, Carney et al (1999)
    Frequency: 5.66 cpd
    Gaussian window: sx=sy=0.5 deg

    Parameters
    ----------
    ppd : Sequence[Number, Number], Number, or None
        pixels per degree [vertical, horizontal]

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img") and additional keys containing
        stimulus parameters

    References
    ----------
    Carney, T., Klein, S. A., Tyler, C. W., Silverstein, A. D., Beutter, B., Levi, D.,
        ... & Eckstein, M. P. (1999).
        Development of an image/threshold database
        for designing and testing human vision models.
        Proceedings of SPIE, 3644, 542-551.
        https://doi.org/10.1117/12.348473
    """

    params = {
        "visual_size": 256 / PPD,
        "ppd": ppd,
        "frequency": 5.66,
        "sigma": 0.5,
        "rotation": -90,
        "phase_shift": 90,
        "origin": "center",
    }

    stim = gabor(**params)

    v = 17
    experimental_data = {
        "participants": participants,
        "thresholds1": df[v],
        "thresholds2": df[v + 1],
        "thresholds3": df[v + 2],
        "thresholds4": df[v + 3],
    }
    return {**stim, "experimental_data": experimental_data}


def GaborPatch6(ppd=PPD):
    """GaborPatch6 with fixed size in degrees, Carney et al (1999)
    Frequency: 8 cpd
    Gaussian window: sx=sy=0.5 deg

    Parameters
    ----------
    ppd : Sequence[Number, Number], Number, or None
        pixels per degree [vertical, horizontal]

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img") and additional keys containing
        stimulus parameters

    References
    ----------
    Carney, T., Klein, S. A., Tyler, C. W., Silverstein, A. D., Beutter, B., Levi, D.,
        ... & Eckstein, M. P. (1999).
        Development of an image/threshold database
        for designing and testing human vision models.
        Proceedings of SPIE, 3644, 542-551.
        https://doi.org/10.1117/12.348473
    """

    params = {
        "visual_size": 256 / PPD,
        "ppd": ppd,
        "frequency": 8,
        "sigma": 0.5,
        "rotation": -90,
        "phase_shift": 90,
        "origin": "center",
    }

    stim = gabor(**params)

    v = 21
    experimental_data = {
        "participants": participants,
        "thresholds1": df[v],
        "thresholds2": df[v + 1],
        "thresholds3": df[v + 2],
        "thresholds4": df[v + 3],
    }
    return {**stim, "experimental_data": experimental_data}


def GaborPatch7(ppd=PPD):
    """GaborPatch7 with fixed size in degrees, Carney et al (1999)
    Frequency: 11.3 cpd
    Gaussian window: sx=sy=0.5 deg

    Parameters
    ----------
    ppd : Sequence[Number, Number], Number, or None
        pixels per degree [vertical, horizontal]

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img") and additional keys containing
        stimulus parameters

    References
    ----------
    Carney, T., Klein, S. A., Tyler, C. W., Silverstein, A. D., Beutter, B., Levi, D.,
        ... & Eckstein, M. P. (1999).
        Development of an image/threshold database
        for designing and testing human vision models.
        Proceedings of SPIE, 3644, 542-551.
        https://doi.org/10.1117/12.348473
    """

    params = {
        "visual_size": 256 / PPD,
        "ppd": ppd,
        "frequency": 11.3,
        "sigma": 0.5,
        "rotation": -90,
        "phase_shift": 90,
        "origin": "center",
    }

    stim = gabor(**params)

    v = 25
    experimental_data = {
        "participants": participants,
        "thresholds1": df[v],
        "thresholds2": df[v + 1],
        "thresholds3": df[v + 2],
        "thresholds4": df[v + 3],
    }
    return {**stim, "experimental_data": experimental_data}


def GaborPatch8(ppd=PPD):
    """GaborPatch8 with fixed size in degrees, Carney et al (1999)
    Frequency: 16 cpd
    Gaussian window: sx=sy=0.5 deg

    Parameters
    ----------
    ppd : Sequence[Number, Number], Number, or None
        pixels per degree [vertical, horizontal]

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img") and additional keys containing
        stimulus parameters

    References
    ----------
    Carney, T., Klein, S. A., Tyler, C. W., Silverstein, A. D., Beutter, B., Levi, D.,
        ... & Eckstein, M. P. (1999).
        Development of an image/threshold database
        for designing and testing human vision models.
        Proceedings of SPIE, 3644, 542-551.
        https://doi.org/10.1117/12.348473
    """

    params = {
        "visual_size": 256 / PPD,
        "ppd": ppd,
        "frequency": 16,
        "sigma": 0.5,
        "rotation": -90,
        "phase_shift": 90,
        "origin": "center",
    }

    stim = gabor(**params)

    v = 29
    experimental_data = {
        "participants": participants,
        "thresholds1": df[v],
        "thresholds2": df[v + 1],
        "thresholds3": df[v + 2],
        "thresholds4": df[v + 3],
    }
    return {**stim, "experimental_data": experimental_data}


def GaborPatch9(ppd=PPD):
    """GaborPatch9 with fixed size in degrees, Carney et al (1999)
    Frequency: 22.6 cpd
    Gaussian window: sx=sy=0.5 deg

    Parameters
    ----------
    ppd : Sequence[Number, Number], Number, or None
        pixels per degree [vertical, horizontal]

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img") and additional keys containing
        stimulus parameters

    References
    ----------
    Carney, T., Klein, S. A., Tyler, C. W., Silverstein, A. D., Beutter, B., Levi, D.,
        ... & Eckstein, M. P. (1999).
        Development of an image/threshold database
        for designing and testing human vision models.
        Proceedings of SPIE, 3644, 542-551.
        https://doi.org/10.1117/12.348473
    """

    params = {
        "visual_size": 256 / PPD,
        "ppd": ppd,
        "frequency": 22.6,
        "sigma": 0.5,
        "rotation": -90,
        "phase_shift": 90,
        "origin": "center",
    }

    stim = gabor(**params)

    v = 33
    experimental_data = {
        "participants": participants,
        "thresholds1": df[v],
        "thresholds2": df[v + 1],
        "thresholds3": df[v + 2],
        "thresholds4": df[v + 3],
    }
    return {**stim, "experimental_data": experimental_data}


def GaborPatch10(ppd=PPD):
    """GaborPatch10 with fixed size in degrees, Carney et al (1999)
    Frequency: 30 cpd
    Gaussian window: sx=sy=0.5 deg

    Parameters
    ----------
    ppd : Sequence[Number, Number], Number, or None
        pixels per degree [vertical, horizontal]

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img") and additional keys containing
        stimulus parameters

    References
    ----------
    Carney, T., Klein, S. A., Tyler, C. W., Silverstein, A. D., Beutter, B., Levi, D.,
        ... & Eckstein, M. P. (1999).
        Development of an image/threshold database
        for designing and testing human vision models.
        Proceedings of SPIE, 3644, 542-551.
        https://doi.org/10.1117/12.348473
    """

    params = {
        "visual_size": 256 / PPD,
        "ppd": ppd,
        "frequency": 30,
        "sigma": 0.5,
        "rotation": -90,
        "phase_shift": 90,
        "origin": "center",
    }

    stim = gabor(**params)

    v = 37
    experimental_data = {
        "participants": participants,
        "thresholds1": df[v],
        "thresholds2": df[v + 1],
        "thresholds3": df[v + 2],
        "thresholds4": df[v + 3],
    }
    return {**stim, "experimental_data": experimental_data}


def GaborPatch11(ppd=PPD):
    """GaborPatch11 with fixed size in cycles (~1 octave), Carney et al (1999)
    Frequency: 2 cpd
    Gaussian window: sx=sy=0.28 deg

    Parameters
    ----------
    ppd : Sequence[Number, Number], Number, or None
        pixels per degree [vertical, horizontal]

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img") and additional keys containing
        stimulus parameters

    References
    ----------
    Carney, T., Klein, S. A., Tyler, C. W., Silverstein, A. D., Beutter, B., Levi, D.,
        ... & Eckstein, M. P. (1999).
        Development of an image/threshold database
        for designing and testing human vision models.
        Proceedings of SPIE, 3644, 542-551.
        https://doi.org/10.1117/12.348473
    """

    params = {
        "visual_size": 256 / PPD,
        "ppd": ppd,
        "frequency": 2,
        "sigma": 0.28,
        "rotation": -90,
        "phase_shift": 90,
        "origin": "center",
    }

    stim = gabor(**params)

    v = 41
    experimental_data = {
        "participants": participants,
        "thresholds1": df[v],
        "thresholds2": df[v + 1],
        "thresholds3": df[v + 2],
        "thresholds4": df[v + 3],
    }
    return {**stim, "experimental_data": experimental_data}


def GaborPatch12(ppd=PPD):
    """GaborPatch12 with fixed size in cycles (~1 octave), Carney et al (1999)
    Frequency: 4 cpd
    Gaussian window: sx=sy=0.14 deg

    Parameters
    ----------
    ppd : Sequence[Number, Number], Number, or None
        pixels per degree [vertical, horizontal]

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img") and additional keys containing
        stimulus parameters

    References
    ----------
    Carney, T., Klein, S. A., Tyler, C. W., Silverstein, A. D., Beutter, B., Levi, D.,
        ... & Eckstein, M. P. (1999).
        Development of an image/threshold database
        for designing and testing human vision models.
        Proceedings of SPIE, 3644, 542-551.
        https://doi.org/10.1117/12.348473
    """

    params = {
        "visual_size": 256 / PPD,
        "ppd": ppd,
        "frequency": 4,
        "sigma": 0.14,
        "rotation": -90,
        "phase_shift": 90,
        "origin": "center",
    }

    stim = gabor(**params)

    v = 45
    experimental_data = {
        "participants": participants,
        "thresholds1": df[v],
        "thresholds2": df[v + 1],
        "thresholds3": df[v + 2],
        "thresholds4": df[v + 3],
    }
    return {**stim, "experimental_data": experimental_data}


def GaborPatch13(ppd=PPD):
    """GaborPatch13 with fixed size in cycles (~1 octave), Carney et al (1999)
    Frequency: 8 cpd
    Gaussian window: sx=sy=0.07 deg

    Parameters
    ----------
    ppd : Sequence[Number, Number], Number, or None
        pixels per degree [vertical, horizontal]

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img") and additional keys containing
        stimulus parameters

    References
    ----------
    Carney, T., Klein, S. A., Tyler, C. W., Silverstein, A. D., Beutter, B., Levi, D.,
        ... & Eckstein, M. P. (1999).
        Development of an image/threshold database
        for designing and testing human vision models.
        Proceedings of SPIE, 3644, 542-551.
        https://doi.org/10.1117/12.348473
    """

    params = {
        "visual_size": 256 / PPD,
        "ppd": ppd,
        "frequency": 8,
        "sigma": 0.07,
        "rotation": -90,
        "phase_shift": 90,
        "origin": "center",
    }

    stim = gabor(**params)

    v = 49
    experimental_data = {
        "participants": participants,
        "thresholds1": df[v],
        "thresholds2": df[v + 1],
        "thresholds3": df[v + 2],
        "thresholds4": df[v + 3],
    }
    return {**stim, "experimental_data": experimental_data}


def GaborPatch14(ppd=PPD):
    """GaborPatch14 with fixed size in cycles (~1 octave), Carney et al (1999)
    Frequency: 16 cpd
    Gaussian window: sx=sy=0.035 deg

    Parameters
    ----------
    ppd : Sequence[Number, Number], Number, or None
        pixels per degree [vertical, horizontal]

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img") and additional keys containing
        stimulus parameters

    References
    ----------
    Carney, T., Klein, S. A., Tyler, C. W., Silverstein, A. D., Beutter, B., Levi, D.,
        ... & Eckstein, M. P. (1999).
        Development of an image/threshold database
        for designing and testing human vision models.
        Proceedings of SPIE, 3644, 542-551.
        https://doi.org/10.1117/12.348473
    """

    params = {
        "visual_size": 256 / PPD,
        "ppd": ppd,
        "frequency": 16,
        "sigma": 0.035,
        "rotation": -90,
        "phase_shift": 90,
        "origin": "center",
    }

    stim = gabor(**params)

    v = 53
    experimental_data = {
        "participants": participants,
        "thresholds1": df[v],
        "thresholds2": df[v + 1],
        "thresholds3": df[v + 2],
        "thresholds4": df[v + 3],
    }
    return {**stim, "experimental_data": experimental_data}


def ElongatedGabor15(ppd=PPD):
    """ElongatedGabor15, Carney et al (1999)
    Frequency: 4 cpd
    Gaussian window: sy=0.28 (~0.5octave); sx=0.5 deg

    Parameters
    ----------
    ppd : Sequence[Number, Number], Number, or None
        pixels per degree [vertical, horizontal]

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img") and additional keys containing
        stimulus parameters

    References
    ----------
    Carney, T., Klein, S. A., Tyler, C. W., Silverstein, A. D., Beutter, B., Levi, D.,
        ... & Eckstein, M. P. (1999).
        Development of an image/threshold database
        for designing and testing human vision models.
        Proceedings of SPIE, 3644, 542-551.
        https://doi.org/10.1117/12.348473
    """

    params = {
        "visual_size": 256 / PPD,
        "ppd": ppd,
        "frequency": 4,
        "sigma": (0.28, 0.5),
        "rotation": -90,
        "phase_shift": 90,
        "origin": "center",
    }

    stim = gabor(**params)

    v = 57
    experimental_data = {
        "participants": participants,
        "thresholds1": df[v],
        "thresholds2": df[v + 1],
        "thresholds3": df[v + 2],
        "thresholds4": df[v + 3],
    }
    return {**stim, "experimental_data": experimental_data}


def ElongatedGabor16(ppd=PPD):
    """ElongatedGabor16, Carney et al (1999)
    Frequency: 8 cpd
    Gaussian window: sy=0.14 (~0.5octave); sx=0.5 deg

    Parameters
    ----------
    ppd : Sequence[Number, Number], Number, or None
        pixels per degree [vertical, horizontal]

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img") and additional keys containing
        stimulus parameters

    References
    ----------
    Carney, T., Klein, S. A., Tyler, C. W., Silverstein, A. D., Beutter, B., Levi, D.,
        ... & Eckstein, M. P. (1999).
        Development of an image/threshold database
        for designing and testing human vision models.
        Proceedings of SPIE, 3644, 542-551.
        https://doi.org/10.1117/12.348473
    """

    params = {
        "visual_size": 256 / PPD,
        "ppd": ppd,
        "frequency": 8,
        "sigma": (0.14, 0.5),
        "rotation": -90,
        "phase_shift": 90,
        "origin": "center",
    }

    stim = gabor(**params)

    v = 61
    experimental_data = {
        "participants": participants,
        "thresholds1": df[v],
        "thresholds2": df[v + 1],
        "thresholds3": df[v + 2],
        "thresholds4": df[v + 3],
    }
    return {**stim, "experimental_data": experimental_data}


def ElongatedGabor17(ppd=PPD):
    """ElongatedGabor17, Carney et al (1999)
    Frequency: 16 cpd
    Gaussian window: sy=0.07 (~0.5octave); sx=0.5 deg

    Parameters
    ----------
    ppd : Sequence[Number, Number], Number, or None
        pixels per degree [vertical, horizontal]

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img") and additional keys containing
        stimulus parameters

    References
    ----------
    Carney, T., Klein, S. A., Tyler, C. W., Silverstein, A. D., Beutter, B., Levi, D.,
        ... & Eckstein, M. P. (1999).
        Development of an image/threshold database
        for designing and testing human vision models.
        Proceedings of SPIE, 3644, 542-551.
        https://doi.org/10.1117/12.348473
    """

    params = {
        "visual_size": 256 / PPD,
        "ppd": ppd,
        "frequency": 16,
        "sigma": (0.07, 0.5),
        "rotation": -90,
        "phase_shift": 90,
        "origin": "center",
    }

    stim = gabor(**params)

    v = 65
    experimental_data = {
        "participants": participants,
        "thresholds1": df[v],
        "thresholds2": df[v + 1],
        "thresholds3": df[v + 2],
        "thresholds4": df[v + 3],
    }
    return {**stim, "experimental_data": experimental_data}


def Baguette18(ppd=PPD):
    """Baguette18 (elongated Gabors; varying aspect ratios), Carney et al (1999)
    Frequency: 4 cpd
    Gaussian window: sy=0.14 (~1octave); sx=0.28 deg (~2octaves)

    Parameters
    ----------
    ppd : Sequence[Number, Number], Number, or None
        pixels per degree [vertical, horizontal]

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img") and additional keys containing
        stimulus parameters

    References
    ----------
    Carney, T., Klein, S. A., Tyler, C. W., Silverstein, A. D., Beutter, B., Levi, D.,
        ... & Eckstein, M. P. (1999).
        Development of an image/threshold database
        for designing and testing human vision models.
        Proceedings of SPIE, 3644, 542-551.
        https://doi.org/10.1117/12.348473
    """

    params = {
        "visual_size": 256 / PPD,
        "ppd": ppd,
        "frequency": 4,
        "sigma": (0.14, 0.28),
        "rotation": -90,
        "phase_shift": 90,
        "origin": "center",
    }

    stim = gabor(**params)

    v = 69
    experimental_data = {
        "participants": participants,
        "thresholds1": df[v],
        "thresholds2": df[v + 1],
        "thresholds3": df[v + 2],
        "thresholds4": df[v + 3],
    }
    return {**stim, "experimental_data": experimental_data}


def Baguette19(ppd=PPD):
    """Baguette19 (elongated Gabors; varying aspect ratios), Carney et al (1999)
    Frequency: 4 cpd
    Gaussian window: sy=0.14 (~1octave); sx=0.5 deg

    Parameters
    ----------
    ppd : Sequence[Number, Number], Number, or None
        pixels per degree [vertical, horizontal]

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img") and additional keys containing
        stimulus parameters

    References
    ----------
    Carney, T., Klein, S. A., Tyler, C. W., Silverstein, A. D., Beutter, B., Levi, D.,
        ... & Eckstein, M. P. (1999).
        Development of an image/threshold database
        for designing and testing human vision models.
        Proceedings of SPIE, 3644, 542-551.
        https://doi.org/10.1117/12.348473
    """

    params = {
        "visual_size": 256 / PPD,
        "ppd": ppd,
        "frequency": 4,
        "sigma": (0.14, 0.5),
        "rotation": -90,
        "phase_shift": 90,
        "origin": "center",
    }

    stim = gabor(**params)

    v = 73
    experimental_data = {
        "participants": participants,
        "thresholds1": df[v],
        "thresholds2": df[v + 1],
        "thresholds3": df[v + 2],
        "thresholds4": df[v + 3],
    }
    return {**stim, "experimental_data": experimental_data}


def Baguette20(ppd=PPD):
    """Baguette20 (elongated Gabors; varying aspect ratios), Carney et al (1999)
    Frequency: 4 cpd
    Gaussian window: sy=0.28 (~2octave); sx=0.14 deg (~1octave)

    Parameters
    ----------
    ppd : Sequence[Number, Number], Number, or None
        pixels per degree [vertical, horizontal]

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img") and additional keys containing
        stimulus parameters

    References
    ----------
    Carney, T., Klein, S. A., Tyler, C. W., Silverstein, A. D., Beutter, B., Levi, D.,
        ... & Eckstein, M. P. (1999).
        Development of an image/threshold database
        for designing and testing human vision models.
        Proceedings of SPIE, 3644, 542-551.
        https://doi.org/10.1117/12.348473
    """

    params = {
        "visual_size": 256 / PPD,
        "ppd": ppd,
        "frequency": 4,
        "sigma": (0.28, 0.14),
        "rotation": -90,
        "phase_shift": 90,
        "origin": "center",
    }

    stim = gabor(**params)

    v = 77
    experimental_data = {
        "participants": participants,
        "thresholds1": df[v],
        "thresholds2": df[v + 1],
        "thresholds3": df[v + 2],
        "thresholds4": df[v + 3],
    }
    return {**stim, "experimental_data": experimental_data}


def Baguette21(ppd=PPD):
    """Baguette20 (elongated Gabors; varying aspect ratios), Carney et al (1999)
    Frequency: 4 cpd
    Gaussian window: sy=0.5 deg; sx=0.14 deg (~1octave)

    Parameters
    ----------
    ppd : Sequence[Number, Number], Number, or None
        pixels per degree [vertical, horizontal]

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img") and additional keys containing
        stimulus parameters

    References
    ----------
    Carney, T., Klein, S. A., Tyler, C. W., Silverstein, A. D., Beutter, B., Levi, D.,
        ... & Eckstein, M. P. (1999).
        Development of an image/threshold database
        for designing and testing human vision models.
        Proceedings of SPIE, 3644, 542-551.
        https://doi.org/10.1117/12.348473
    """

    params = {
        "visual_size": 256 / PPD,
        "ppd": ppd,
        "frequency": 4,
        "sigma": (0.5, 0.14),
        "rotation": -90,
        "phase_shift": 90,
        "origin": "center",
    }

    stim = gabor(**params)

    v = 81
    experimental_data = {
        "participants": participants,
        "thresholds1": df[v],
        "thresholds2": df[v + 1],
        "thresholds3": df[v + 2],
        "thresholds4": df[v + 3],
    }
    return {**stim, "experimental_data": experimental_data}


def Subthreshold22(ppd=PPD):
    """Subthreshold22 (compound Gabor), Carney et al (1999)
    Frequencies: 2 cpd & 2*sqrt(2) cpd
    Gaussian window: sy=sx=0.5 deg

    Parameters
    ----------
    ppd : Sequence[Number, Number], Number, or None
        pixels per degree [vertical, horizontal]

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img") and additional keys containing
        stimulus parameters

    References
    ----------
    Carney, T., Klein, S. A., Tyler, C. W., Silverstein, A. D., Beutter, B., Levi, D.,
        ... & Eckstein, M. P. (1999).
        Development of an image/threshold database
        for designing and testing human vision models.
        Proceedings of SPIE, 3644, 542-551.
        https://doi.org/10.1117/12.348473
    """

    params = {
        "visual_size": 256 / PPD,
        "ppd": ppd,
        "sigma": 0.5,
        "rotation": -90,
        "phase_shift": 90,
        "origin": "center",
    }

    stim1 = gabor(**params, frequency=2)
    stim2 = gabor(**params, frequency=2 * np.sqrt(2))

    stim1["img"] = stim1["img"] / 2 + stim2["img"] / 2
    stim1["grating_mask2"] = stim2["grating_mask"]
    stim1["frequency2"] = stim2["frequency"]
    stim1["phase_width2"] = stim2["phase_width"]
    stim1["n_phases2"] = stim2["n_phases"]

    v = 85
    experimental_data = {
        "participants": participants,
        "thresholds1": df[v],
        "thresholds2": df[v + 1],
        "thresholds3": df[v + 2],
        "thresholds4": df[v + 3],
    }
    return {**stim1, "experimental_data": experimental_data}


def Subthreshold23(ppd=PPD):
    """Subthreshold23 (compound Gabor), Carney et al (1999)
    Frequencies: 2 cpd & 4 cpd
    Gaussian window: sy=sx=0.5 deg

    Parameters
    ----------
    ppd : Sequence[Number, Number], Number, or None
        pixels per degree [vertical, horizontal]

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img") and additional keys containing
        stimulus parameters

    References
    ----------
    Carney, T., Klein, S. A., Tyler, C. W., Silverstein, A. D., Beutter, B., Levi, D.,
        ... & Eckstein, M. P. (1999).
        Development of an image/threshold database
        for designing and testing human vision models.
        Proceedings of SPIE, 3644, 542-551.
        https://doi.org/10.1117/12.348473
    """

    params = {
        "visual_size": 256 / PPD,
        "ppd": ppd,
        "sigma": 0.5,
        "rotation": -90,
        "phase_shift": 90,
        "origin": "center",
    }

    stim1 = gabor(**params, frequency=2)
    stim2 = gabor(**params, frequency=4)

    stim1["img"] = stim1["img"] / 2 + stim2["img"] / 2
    stim1["grating_mask2"] = stim2["grating_mask"]
    stim1["frequency2"] = stim2["frequency"]
    stim1["phase_width2"] = stim2["phase_width"]
    stim1["n_phases2"] = stim2["n_phases"]

    v = 89
    experimental_data = {
        "participants": participants,
        "thresholds1": df[v],
        "thresholds2": df[v + 1],
        "thresholds3": df[v + 2],
        "thresholds4": df[v + 3],
    }
    return {**stim1, "experimental_data": experimental_data}


def Subthreshold24(ppd=PPD):
    """Subthreshold24 (compound Gabor), Carney et al (1999)
    Frequencies: 4 cpd & 4*sqrt(2) cpd
    Gaussian window: sy=sx=0.5 deg

    Parameters
    ----------
    ppd : Sequence[Number, Number], Number, or None
        pixels per degree [vertical, horizontal]

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img") and additional keys containing
        stimulus parameters

    References
    ----------
    Carney, T., Klein, S. A., Tyler, C. W., Silverstein, A. D., Beutter, B., Levi, D.,
        ... & Eckstein, M. P. (1999).
        Development of an image/threshold database
        for designing and testing human vision models.
        Proceedings of SPIE, 3644, 542-551.
        https://doi.org/10.1117/12.348473
    """

    params = {
        "visual_size": 256 / PPD,
        "ppd": ppd,
        "sigma": 0.5,
        "rotation": -90,
        "phase_shift": 90,
        "origin": "center",
    }

    stim1 = gabor(**params, frequency=4)
    stim2 = gabor(**params, frequency=4 * np.sqrt(2))

    stim1["img"] = stim1["img"] / 2 + stim2["img"] / 2
    stim1["grating_mask2"] = stim2["grating_mask"]
    stim1["frequency2"] = stim2["frequency"]
    stim1["phase_width2"] = stim2["phase_width"]
    stim1["n_phases2"] = stim2["n_phases"]

    v = 93
    experimental_data = {
        "participants": participants,
        "thresholds1": df[v],
        "thresholds2": df[v + 1],
        "thresholds3": df[v + 2],
        "thresholds4": df[v + 3],
    }
    return {**stim1, "experimental_data": experimental_data}


def Subthreshold25(ppd=PPD):
    """Subthreshold24 (compound Gabor), Carney et al (1999)
    Frequencies: 4 cpd & 8 cpd
    Gaussian window: sy=sx=0.5 deg

    Parameters
    ----------
    ppd : Sequence[Number, Number], Number, or None
        pixels per degree [vertical, horizontal]

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img") and additional keys containing
        stimulus parameters

    References
    ----------
    Carney, T., Klein, S. A., Tyler, C. W., Silverstein, A. D., Beutter, B., Levi, D.,
        ... & Eckstein, M. P. (1999).
        Development of an image/threshold database
        for designing and testing human vision models.
        Proceedings of SPIE, 3644, 542-551.
        https://doi.org/10.1117/12.348473
    """

    params = {
        "visual_size": 256 / PPD,
        "ppd": ppd,
        "sigma": 0.5,
        "rotation": -90,
        "phase_shift": 90,
        "origin": "center",
    }

    stim1 = gabor(**params, frequency=4)
    stim2 = gabor(**params, frequency=8)

    stim1["img"] = stim1["img"] / 2 + stim2["img"] / 2
    stim1["grating_mask2"] = stim2["grating_mask"]
    stim1["frequency2"] = stim2["frequency"]
    stim1["phase_width2"] = stim2["phase_width"]
    stim1["n_phases2"] = stim2["n_phases"]

    v = 97
    experimental_data = {
        "participants": participants,
        "thresholds1": df[v],
        "thresholds2": df[v + 1],
        "thresholds3": df[v + 2],
        "thresholds4": df[v + 3],
    }
    return {**stim1, "experimental_data": experimental_data}


def Gaussians26(ppd=PPD):
    """Gaussians26, Carney et al (1999)
    Gaussian window: sy=sx=0.5 deg

    Parameters
    ----------
    ppd : Sequence[Number, Number], Number, or None
        pixels per degree [vertical, horizontal]

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img") and additional keys containing
        stimulus parameters

    References
    ----------
    Carney, T., Klein, S. A., Tyler, C. W., Silverstein, A. D., Beutter, B., Levi, D.,
        ... & Eckstein, M. P. (1999).
        Development of an image/threshold database
        for designing and testing human vision models.
        Proceedings of SPIE, 3644, 542-551.
        https://doi.org/10.1117/12.348473
    """

    params = {
        "visual_size": 256 / PPD,
        "ppd": ppd,
        "sigma": 0.5,
        "intensity_max": 1,
        "origin": "center",
    }

    stim = gaussians.gaussian(**params)
    stim["img"] = stim["img"] / 2 + 0.5

    v = 101
    experimental_data = {
        "participants": participants,
        "thresholds1": df[v],
        "thresholds2": df[v + 1],
        "thresholds3": df[v + 2],
        "thresholds4": df[v + 3],
    }
    return {**stim, "experimental_data": experimental_data}


def Gaussians27(ppd=PPD):
    """Gaussians27, Carney et al (1999)
    Gaussian window: sy=sx=8.43 arcmin

    Parameters
    ----------
    ppd : Sequence[Number, Number], Number, or None
        pixels per degree [vertical, horizontal]

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img") and additional keys containing
        stimulus parameters

    References
    ----------
    Carney, T., Klein, S. A., Tyler, C. W., Silverstein, A. D., Beutter, B., Levi, D.,
        ... & Eckstein, M. P. (1999).
        Development of an image/threshold database
        for designing and testing human vision models.
        Proceedings of SPIE, 3644, 542-551.
        https://doi.org/10.1117/12.348473
    """

    params = {
        "visual_size": 256 / PPD,
        "ppd": ppd,
        "sigma": 8.43 / 60,
        "intensity_max": 1,
        "origin": "center",
    }

    stim = gaussians.gaussian(**params)
    stim["img"] = stim["img"] / 2 + 0.5

    v = 105
    experimental_data = {
        "participants": participants,
        "thresholds1": df[v],
        "thresholds2": df[v + 1],
        "thresholds3": df[v + 2],
        "thresholds4": df[v + 3],
    }
    return {**stim, "experimental_data": experimental_data}


def Gaussians28(ppd=PPD):
    """Gaussians28, Carney et al (1999)
    Gaussian window: sy=sx=2.106 arcmin

    Parameters
    ----------
    ppd : Sequence[Number, Number], Number, or None
        pixels per degree [vertical, horizontal]

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img") and additional keys containing
        stimulus parameters

    References
    ----------
    Carney, T., Klein, S. A., Tyler, C. W., Silverstein, A. D., Beutter, B., Levi, D.,
        ... & Eckstein, M. P. (1999).
        Development of an image/threshold database
        for designing and testing human vision models.
        Proceedings of SPIE, 3644, 542-551.
        https://doi.org/10.1117/12.348473
    """

    params = {
        "visual_size": 256 / PPD,
        "ppd": ppd,
        "sigma": 2.106 / 60,
        "intensity_max": 1,
        "origin": "center",
    }

    stim = gaussians.gaussian(**params)
    stim["img"] = stim["img"] / 2 + 0.5

    v = 109
    experimental_data = {
        "participants": participants,
        "thresholds1": df[v],
        "thresholds2": df[v + 1],
        "thresholds3": df[v + 2],
        "thresholds4": df[v + 3],
    }
    return {**stim, "experimental_data": experimental_data}


def Gaussians29(ppd=PPD):
    """Gaussians29, Carney et al (1999)
    Gaussian window: sy=sx=1.05 arcmin

    Parameters
    ----------
    ppd : Sequence[Number, Number], Number, or None
        pixels per degree [vertical, horizontal]

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img") and additional keys containing
        stimulus parameters

    References
    ----------
    Carney, T., Klein, S. A., Tyler, C. W., Silverstein, A. D., Beutter, B., Levi, D.,
        ... & Eckstein, M. P. (1999).
        Development of an image/threshold database
        for designing and testing human vision models.
        Proceedings of SPIE, 3644, 542-551.
        https://doi.org/10.1117/12.348473
    """

    params = {
        "visual_size": 256 / PPD,
        "ppd": ppd,
        "sigma": 1.05 / 60,
        "intensity_max": 1,
        "origin": "center",
    }

    stim = gaussians.gaussian(**params)
    stim["img"] = stim["img"] / 2 + 0.5

    v = 113
    experimental_data = {
        "participants": participants,
        "thresholds1": df[v],
        "thresholds2": df[v + 1],
        "thresholds3": df[v + 2],
        "thresholds4": df[v + 3],
    }
    return {**stim, "experimental_data": experimental_data}


def Edge30(ppd=PPD):
    """Edge30, Carney et al (1999)
    Gaussian window: sy=sx=0.5 deg

    Parameters
    ----------
    ppd : Sequence[Number, Number], Number, or None
        pixels per degree [vertical, horizontal]

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img") and additional keys containing
        stimulus parameters

    References
    ----------
    Carney, T., Klein, S. A., Tyler, C. W., Silverstein, A. D., Beutter, B., Levi, D.,
        ... & Eckstein, M. P. (1999).
        Development of an image/threshold database
        for designing and testing human vision models.
        Proceedings of SPIE, 3644, 542-551.
        https://doi.org/10.1117/12.348473
    """

    stim = gaussian_edge(visual_size=256 / PPD, ppd=ppd, rotation=-90, sigma=0.5)

    v = 117
    experimental_data = {
        "participants": participants,
        "thresholds1": df[v],
        "thresholds2": df[v + 1],
        "thresholds3": df[v + 2],
        "thresholds4": df[v + 3],
    }
    return {**stim, "experimental_data": experimental_data}


def Line31(ppd=PPD):
    """Line31: line x Gaussian, Carney et al (1999)
    Line width: 0.5 arcmin
    Gaussian window: sy=sx=0.5 deg

    Parameters
    ----------
    ppd : Sequence[Number, Number], Number, or None
        pixels per degree [vertical, horizontal]

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img") and additional keys containing
        stimulus parameters

    References
    ----------
    Carney, T., Klein, S. A., Tyler, C. W., Silverstein, A. D., Beutter, B., Levi, D.,
        ... & Eckstein, M. P. (1999).
        Development of an image/threshold database
        for designing and testing human vision models.
        Proceedings of SPIE, 3644, 542-551.
        https://doi.org/10.1117/12.348473
    """

    stim = lines.line(
        visual_size=256 / PPD,
        ppd=ppd,
        line_length=256 / PPD,
        line_width=0.5 / 60,
        rotation=90,
        intensity_background=0.5,
    )
    window = gaussians.gaussian(visual_size=256 / PPD, ppd=ppd, sigma=0.5)

    img = (stim["img"] - 0.5) * window["img"] + 0.5
    stim["img"] = img
    stim["sigma"] = window["sigma"]

    v = 121
    experimental_data = {
        "participants": participants,
        "thresholds1": df[v],
        "thresholds2": df[v + 1],
        "thresholds3": df[v + 2],
        "thresholds4": df[v + 3],
    }
    return {**stim, "experimental_data": experimental_data}


def Dipole32(ppd=PPD):
    """Dipole32: lines x Gaussian, Carney et al (1999)
    Line width: 3 px =
    Seperation: 1 px =
    Gaussian window: sy=sx=0.5 deg

    Parameters
    ----------
    ppd : Sequence[Number, Number], Number, or None
        pixels per degree [vertical, horizontal]

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img") and additional keys containing
        stimulus parameters

    References
    ----------
    Carney, T., Klein, S. A., Tyler, C. W., Silverstein, A. D., Beutter, B., Levi, D.,
        ... & Eckstein, M. P. (1999).
        Development of an image/threshold database
        for designing and testing human vision models.
        Proceedings of SPIE, 3644, 542-551.
        https://doi.org/10.1117/12.348473
    """

    stim = lines.dipole(
        visual_size=256 / PPD,
        ppd=ppd,
        line_length=256 / PPD,
        line_width=1 / PPD,
        line_gap=2 / PPD,
        rotation=270,
    )
    stim = roll_dict(stim, -1, axes=0)
    window = gaussians.gaussian(visual_size=256 / PPD, ppd=ppd, sigma=0.5)

    img = (stim["img"] - 0.5) * window["img"] + 0.5
    stim["img"] = img
    stim["sigma"] = window["sigma"]

    v = 125
    experimental_data = {
        "participants": participants,
        "thresholds1": df[v],
        "thresholds2": df[v + 1],
        "thresholds3": df[v + 2],
        "thresholds4": df[v + 3],
    }
    return {**stim, "experimental_data": experimental_data}


def GaborString33(ppd=PPD):
    """GaborString33 - 5 collinear in-phase Gabors, Carney et al (1999)
    Frequency: 8 cpd
    Gaussian window of individual Gabors: sx=sy=0.07 deg (~1octave)
    Seperation: 5sx

    Parameters
    ----------
    ppd : Sequence[Number, Number], Number, or None
        pixels per degree [vertical, horizontal]

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img") and additional keys containing
        stimulus parameters

    References
    ----------
    Carney, T., Klein, S. A., Tyler, C. W., Silverstein, A. D., Beutter, B., Levi, D.,
        ... & Eckstein, M. P. (1999).
        Development of an image/threshold database
        for designing and testing human vision models.
        Proceedings of SPIE, 3644, 542-551.
        https://doi.org/10.1117/12.348473
    """

    params = {
        "visual_size": 256 / PPD / 6,
        "ppd": ppd,
        "frequency": 8,
        "sigma": 0.07,
        "rotation": -90,
        "phase_shift": 90,
        "origin": "center",
    }

    stim = gabor(**params)

    # Stack collinear Gabors horizontally and pad
    stimc = stack_dicts(stim, stim)
    stimc = stack_dicts(stimc, stimc)
    stimc = stack_dicts(stimc, stim)
    stimc = pad_dict_to_shape(stimc, (256, 256), pad_value=0.5)

    stim["img"] = stimc["img"]
    stim["grating_mask"] = stimc["grating_mask"]
    stim["visual_size"] = stimc["visual_size"]
    stim["shape"] = stimc["shape"]
    stim = roll_dict(stim, (-1, -1), axes=(0, 1))

    v = 129
    experimental_data = {
        "participants": participants,
        "thresholds1": df[v],
        "thresholds2": df[v + 1],
        "thresholds3": df[v + 2],
        "thresholds4": df[v + 3],
    }
    return {**stim, "experimental_data": experimental_data}


def GaborString34(ppd=PPD):
    """GaborString33 - 5 collinear out-of-phase Gabors, Carney et al (1999)
    Frequency: 8 cpd
    Gaussian window of individual Gabors: sx=sy= deg (~1octave)
    Seperation: 5sx

    Parameters
    ----------
    ppd : Sequence[Number, Number], Number, or None
        pixels per degree [vertical, horizontal]

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img") and additional keys containing
        stimulus parameters

    References
    ----------
    Carney, T., Klein, S. A., Tyler, C. W., Silverstein, A. D., Beutter, B., Levi, D.,
        ... & Eckstein, M. P. (1999).
        Development of an image/threshold database
        for designing and testing human vision models.
        Proceedings of SPIE, 3644, 542-551.
        https://doi.org/10.1117/12.348473
    """

    params = {
        "visual_size": 256 / PPD / 6,
        "ppd": ppd,
        "frequency": 8,
        "sigma": 0.07,
        "rotation": -90,
        "origin": "center",
    }

    stim1 = gabor(**params, phase_shift=-90)
    stim2 = gabor(**params, phase_shift=90)

    # Stack collinear Gabors horizontally and pad
    stimc = stack_dicts(stim2, stim1)
    stimc = stack_dicts(stimc, stim2)
    stimc = stack_dicts(stimc, stim1)
    stimc = stack_dicts(stimc, stim2)
    stimc = pad_dict_to_shape(stimc, (256, 256), pad_value=0.5)

    stim1["img"] = stimc["img"]
    stim1["grating_mask"] = stimc["grating_mask"]
    stim1["visual_size"] = stimc["visual_size"]
    stim1["shape"] = stimc["shape"]
    stim1["phase_shift2"] = stim2["phase_shift"]
    stim1 = roll_dict(stim1, (-1, -1), axes=(0, 1))

    v = 133
    experimental_data = {
        "participants": participants,
        "thresholds1": df[v],
        "thresholds2": df[v + 1],
        "thresholds3": df[v + 2],
        "thresholds4": df[v + 3],
    }
    return {**stim1, "experimental_data": experimental_data}


def Noise35_random(ppd=PPD):
    """Noise35 - binary noise x Gaussian, Carney et al (1999)
    Gaussian window: sy=sx=0.5 deg

    Parameters
    ----------
    ppd : Sequence[Number, Number], Number, or None
        pixels per degree [vertical, horizontal]

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img") and additional keys containing
        stimulus parameters

    References
    ----------
    Carney, T., Klein, S. A., Tyler, C. W., Silverstein, A. D., Beutter, B., Levi, D.,
        ... & Eckstein, M. P. (1999).
        Development of an image/threshold database
        for designing and testing human vision models.
        Proceedings of SPIE, 3644, 542-551.
        https://doi.org/10.1117/12.348473
    """

    stim = binary_noise(visual_size=256 / PPD, ppd=ppd / 2, rms_contrast=1)
    stim = resize_dict(stim, (2, 2))
    window = gaussians.gaussian(visual_size=256 / PPD, ppd=ppd, sigma=0.5)

    img = stim["img"] * window["img"]
    stim["img"] = img / 2 + 0.5
    stim["mask"] = np.zeros(img.shape).astype(int)
    return stim


def Noise35(ppd=PPD):
    """Noise35 - binary noise x Gaussian, Carney et al (1999)
    Gaussian window: sy=sx=0.5 deg

    Parameters
    ----------
    ppd : Sequence[Number, Number], Number, or None
        pixels per degree [vertical, horizontal]

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img") and additional keys containing
        stimulus parameters

    References
    ----------
    Carney, T., Klein, S. A., Tyler, C. W., Silverstein, A. D., Beutter, B., Levi, D.,
        ... & Eckstein, M. P. (1999).
        Development of an image/threshold database
        for designing and testing human vision models.
        Proceedings of SPIE, 3644, 542-551.
        https://doi.org/10.1117/12.348473
    """
    # Read natural image from Modelfest
    img = read_tif(Path(__file__).parents[0] / "modelfest_noise.tif")
    img = img / 255

    stim = {
        "img": img,
        "visual_size": (256 / PPD, 256 / PPD),
        "shape": img.shape,
        "ppd": PPD,
        "intensity_range": (img.min(), img.max()),
    }

    v = 169
    experimental_data = {
        "participants": participants,
        "thresholds1": df[v],
        "thresholds2": df[v + 1],
        "thresholds3": df[v + 2],
        "thresholds4": df[v + 3],
    }
    mask = np.zeros(img.shape).astype(int)
    return {**stim, "mask": mask, "experimental_data": experimental_data}


def Orientation36(ppd=PPD):
    """Orientation36 - oriented Gabor, Carney et al (1999)
    Frequency: 4 cpd
    Rotation: 45 deg
    Gaussian window: sx=sy=0.14 deg (~1octave)

    Parameters
    ----------
    ppd : Sequence[Number, Number], Number, or None
        pixels per degree [vertical, horizontal]

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img") and additional keys containing
        stimulus parameters

    References
    ----------
    Carney, T., Klein, S. A., Tyler, C. W., Silverstein, A. D., Beutter, B., Levi, D.,
        ... & Eckstein, M. P. (1999).
        Development of an image/threshold database
        for designing and testing human vision models.
        Proceedings of SPIE, 3644, 542-551.
        https://doi.org/10.1117/12.348473
    """

    params = {
        "visual_size": 256 / PPD,
        "ppd": ppd,
        "frequency": 4,
        "sigma": 0.14,
        "rotation": -45,
        "phase_shift": 90,
        "origin": "center",
    }

    stim = gabor(**params)

    v = 141
    experimental_data = {
        "participants": participants,
        "thresholds1": df[v],
        "thresholds2": df[v + 1],
        "thresholds3": df[v + 2],
        "thresholds4": df[v + 3],
    }
    return {**stim, "experimental_data": experimental_data}


def Orientation37(ppd=PPD):
    """Orientation37 - oriented Gabor, Carney et al (1999)
    Frequency: 4 cpd
    Rotation: 0 deg
    Gaussian window: sx=sy=0.14 deg (~1octave)

    Parameters
    ----------
    ppd : Sequence[Number, Number], Number, or None
        pixels per degree [vertical, horizontal]

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img") and additional keys containing
        stimulus parameters

    References
    ----------
    Carney, T., Klein, S. A., Tyler, C. W., Silverstein, A. D., Beutter, B., Levi, D.,
        ... & Eckstein, M. P. (1999).
        Development of an image/threshold database
        for designing and testing human vision models.
        Proceedings of SPIE, 3644, 542-551.
        https://doi.org/10.1117/12.348473
    """

    params = {
        "visual_size": 256 / PPD,
        "ppd": ppd,
        "frequency": 4,
        "sigma": 0.14,
        "rotation": 0,
        "phase_shift": 90,
        "origin": "center",
    }

    stim = gabor(**params)

    v = 145
    experimental_data = {
        "participants": participants,
        "thresholds1": df[v],
        "thresholds2": df[v + 1],
        "thresholds3": df[v + 2],
        "thresholds4": df[v + 3],
    }
    return {**stim, "experimental_data": experimental_data}


def Plaids38(ppd=PPD):
    """Plaids38 - compound Gabors, Carney et al (1999)
    Frequency: 4 cpd
    Rotation: 0 & 90 deg
    Gaussian window: sx=sy=0.14 deg (~1octave)

    Parameters
    ----------
    ppd : Sequence[Number, Number], Number, or None
        pixels per degree [vertical, horizontal]

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img") and additional keys containing
        stimulus parameters

    References
    ----------
    Carney, T., Klein, S. A., Tyler, C. W., Silverstein, A. D., Beutter, B., Levi, D.,
        ... & Eckstein, M. P. (1999).
        Development of an image/threshold database
        for designing and testing human vision models.
        Proceedings of SPIE, 3644, 542-551.
        https://doi.org/10.1117/12.348473
    """

    params = {
        "visual_size": 256 / PPD,
        "ppd": ppd,
        "frequency": 4,
        "sigma": 0.14,
        "phase_shift": 90,
        "origin": "center",
        "round_phase_width": False,
    }

    stim = plaid(
        gabor_parameters1={**params, "rotation": 0},
        gabor_parameters2={**params, "rotation": -90},
    )

    v = 149
    experimental_data = {
        "participants": participants,
        "thresholds1": df[v],
        "thresholds2": df[v + 1],
        "thresholds3": df[v + 2],
        "thresholds4": df[v + 3],
    }
    return {**stim, "experimental_data": experimental_data}


def Plaids39(ppd=PPD):
    """Plaids39 - compound Gabors, Carney et al (1999)
    Frequency: 4 cpd
    Rotation: 45 & 90 deg
    Gaussian window: sx=sy=0.14 deg (~1octave)

    Parameters
    ----------
    ppd : Sequence[Number, Number], Number, or None
        pixels per degree [vertical, horizontal]

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img") and additional keys containing
        stimulus parameters

    References
    ----------
    Carney, T., Klein, S. A., Tyler, C. W., Silverstein, A. D., Beutter, B., Levi, D.,
        ... & Eckstein, M. P. (1999).
        Development of an image/threshold database
        for designing and testing human vision models.
        Proceedings of SPIE, 3644, 542-551.
        https://doi.org/10.1117/12.348473
    """

    params = {
        "visual_size": 256 / PPD,
        "ppd": ppd,
        "frequency": 4,
        "sigma": 0.14,
        "phase_shift": 90,
        "origin": "center",
    }

    stim = plaid(
        gabor_parameters1={**params, "rotation": -45},
        gabor_parameters2={**params, "rotation": -90},
    )

    v = 153
    experimental_data = {
        "participants": participants,
        "thresholds1": df[v],
        "thresholds2": df[v + 1],
        "thresholds3": df[v + 2],
        "thresholds4": df[v + 3],
    }
    return {**stim, "experimental_data": experimental_data}


def Disk40(ppd=PPD):
    """Disk40 - Carney et al (1999)
    Diameter: 0.25 deg

    Parameters
    ----------
    ppd : Sequence[Number, Number], Number, or None
        pixels per degree [vertical, horizontal]

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img") and additional keys containing
        stimulus parameters

    References
    ----------
    Carney, T., Klein, S. A., Tyler, C. W., Silverstein, A. D., Beutter, B., Levi, D.,
        ... & Eckstein, M. P. (1999).
        Development of an image/threshold database
        for designing and testing human vision models.
        Proceedings of SPIE, 3644, 542-551.
        https://doi.org/10.1117/12.348473
    """

    stim = shapes.disc(
        visual_size=256 / PPD, ppd=ppd, radius=0.125, origin="center", intensity_background=0.5
    )
    stim = roll_dict(stim, (-2, -2), axes=(0, 1))

    v = 157
    experimental_data = {
        "participants": participants,
        "thresholds1": df[v],
        "thresholds2": df[v + 1],
        "thresholds3": df[v + 2],
        "thresholds4": df[v + 3],
    }
    return {**stim, "experimental_data": experimental_data}


def Bessel41(ppd=PPD):
    """Bessel41 - Bessel x Gaussian, Carney et al (1999)
    Frequency: 4cpd
    Gaussian window: sy=sx=0.5 deg

    Parameters
    ----------
    ppd : Sequence[Number, Number], Number, or None
        pixels per degree [vertical, horizontal]

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img") and additional keys containing
        stimulus parameters

    References
    ----------
    Carney, T., Klein, S. A., Tyler, C. W., Silverstein, A. D., Beutter, B., Levi, D.,
        ... & Eckstein, M. P. (1999).
        Development of an image/threshold database
        for designing and testing human vision models.
        Proceedings of SPIE, 3644, 542-551.
        https://doi.org/10.1117/12.348473
    """

    stim = bessel(visual_size=256 / PPD, ppd=ppd, frequency=4, origin="center")
    window = gaussians.gaussian(visual_size=256 / PPD, ppd=ppd, sigma=0.5)
    stim["sigma"] = window["sigma"]

    # Apply Gaussian windows to Bessel
    stim["img"] = (stim["img"] - stim["img"].mean()) * window["img"]

    # Set "background" intensity to 0.5 and make sure that max intensity = 1
    stim["img"] = stim["img"] / stim["img"].max() / 2 + 0.5

    v = 161
    experimental_data = {
        "participants": participants,
        "thresholds1": df[v],
        "thresholds2": df[v + 1],
        "thresholds3": df[v + 2],
        "thresholds4": df[v + 3],
    }
    return {**stim, "experimental_data": experimental_data}


def Checkerboard42(ppd=PPD):
    """Checkerboard42 - Checkerboard x Gaussian, Carney et al (1999)
    Frequency: 4cpd fundamental
    Gaussian window: sy=sx=0.5 deg

    Parameters
    ----------
    ppd : Sequence[Number, Number], Number, or None
        pixels per degree [vertical, horizontal]

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img") and additional keys containing
        stimulus parameters

    References
    ----------
    Carney, T., Klein, S. A., Tyler, C. W., Silverstein, A. D., Beutter, B., Levi, D.,
        ... & Eckstein, M. P. (1999).
        Development of an image/threshold database
        for designing and testing human vision models.
        Proceedings of SPIE, 3644, 542-551.
        https://doi.org/10.1117/12.348473
    """
    params = {
        "visual_size": 256 / PPD,
        "ppd": ppd,
        "frequency": 2.81,
        "rotation": -45,
        "round_phase_width": False,
        "intensity_checks": (1.0, 0.0),
    }

    stim = checkerboards.checkerboard(**params)
    window = gaussians.gaussian(visual_size=256 / PPD, ppd=ppd, sigma=0.5)

    img = (stim["img"] - 0.5) * window["img"] + 0.5
    stim["img"] = img
    stim["sigma"] = window["sigma"]

    v = 165
    experimental_data = {
        "participants": participants,
        "thresholds1": df[v],
        "thresholds2": df[v + 1],
        "thresholds3": df[v + 2],
        "thresholds4": df[v + 3],
    }
    return {**stim, "experimental_data": experimental_data}


def NaturalScene43(ppd=PPD):
    """NaturalScene43 - Natural image x Gaussian, Carney et al (1999)
    Gaussian window: sy=sx=0.5 deg

    Parameters
    ----------
    ppd : Sequence[Number, Number], Number, or None
        pixels per degree [vertical, horizontal]

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img") and additional keys containing
        stimulus parameters

    References
    ----------
    Carney, T., Klein, S. A., Tyler, C. W., Silverstein, A. D., Beutter, B., Levi, D.,
        ... & Eckstein, M. P. (1999).
        Development of an image/threshold database
        for designing and testing human vision models.
        Proceedings of SPIE, 3644, 542-551.
        https://doi.org/10.1117/12.348473
    """

    # Read natural image from Modelfest
    img = read_tif(Path(__file__).parents[0] / "modelfest_natural_scene.tif")
    img = img / 255

    stim = {
        "img": img,
        "visual_size": (256 / PPD, 256 / PPD),
        "shape": img.shape,
        "ppd": PPD,
        "intensity_range": (img.min(), img.max()),
    }

    v = 169
    experimental_data = {
        "participants": participants,
        "thresholds1": df[v],
        "thresholds2": df[v + 1],
        "thresholds3": df[v + 2],
        "thresholds4": df[v + 3],
    }
    mask = np.zeros(img.shape).astype(int)
    return {**stim, "mask": mask, "experimental_data": experimental_data}


def read_tif(filename):
    from PIL import Image

    img = np.array(Image.open(filename)).astype(float)
    return img


def compare(o1, s1, filename):
    import matplotlib.pyplot as plt

    o1 = o1 / 255
    s1 = s1 / 1
    vmin, vmax = 0, 1

    plt.figure(figsize=(20, 6))
    plt.subplot(141), plt.imshow(o1, vmin=vmin, vmax=vmax), plt.title("Original")
    plt.subplot(142), plt.imshow(s1, vmin=vmin, vmax=vmax), plt.title("Our implementation")
    plt.subplot(143), plt.imshow(o1 - s1, vmin=-vmax, vmax=vmax), plt.title(
        "Difference"
    ), plt.colorbar()
    plt.subplot(144), plt.plot(o1[:, 128], label="Original")
    plt.plot(s1[:, 128], label="Our implementation"), plt.legend()
    plt.savefig("./comparisons/" + filename)
    plt.close()


def compare_all():
    import os

    if not os.path.exists("./comparisons/"):
        os.makedirs("./comparisons/")

    for stim_name in __all__:
        func = globals()[stim_name]
        o1 = read_tif(str(Path(__file__).parents[0]) + "/modelfest/" + stim_name + ".tif")
        s1 = func()["img"]
        compare(o1, s1, stim_name + ".png")


if __name__ == "__main__":
    from stimupy.utils import plot_stimuli

    stims = gen_all(skip=True)
    plot_stimuli(stims, mask=False, units="visual_size")
    # compare_all()
