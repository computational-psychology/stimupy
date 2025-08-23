"""Stimuli and data from Schmittwilken, Wichmann, & Maertens (2024)

This module reproduces all stimuli used by Schmittwilken, Wichmann, & Maertens
(2024) with random noise instances, and provides the corresponding detection
data of each subject and the average observer.

Each stimulus is provided by a separate function,
which can be listed using

    >>> import stimupy.papers.schmittwilken2024
    >>> help(stimupy.papers.schmittwilken2024)

The output of each of these functions is a stimulus dictionary.

For a visual representation of all the stimuli
simply run this module from the shell

    $ python -m stimupy.papers.schmittwilken2024

References
----------
Schmittwilken, L., Wichmann, F. A., & Maertens, M. (2024).
    Standard models of spatial vision mispredict edge sensitivity at low
    spatial frequencies. Vision Research, 222 , 108450.
    https://doi.org/10.1016/j.visres.2024.108450
"""

from pathlib import Path
import numpy as np
import warnings
import pandas as pd

from stimupy.stimuli.cornsweets import cornsweet_edge
from stimupy.noises.whites import white as create_whitenoise
from stimupy.noises.narrowbands import narrowband as create_narrownoise
from stimupy.noises.naturals import one_over_f as create_pinknoise
from stimupy.utils import rotate_dict

__all__ = [
    "edge05_none",
    "edge05_white",
    "edge05_pink",
    "edge05_brown",
    "edge05_NB05",
    "edge05_NB3",
    "edge05_NB9",
    "edge3_none",
    "edge3_white",
    "edge3_pink",
    "edge3_brown",
    "edge3_NB05",
    "edge3_NB3",
    "edge3_NB9",
    "edge9_none",
    "edge9_white",
    "edge9_pink",
    "edge9_brown",
    "edge9_NB05",
    "edge9_NB3",
    "edge9_NB9",
]

# Default stimulus parameters
PPD = 44.0
visual_size = 4.0  # in deg
mean_lum = 100  # in cd/m2
edge_exponent = 1.0  # affects ramp steepness of Cornsweet edge
noise_contrast = 0.2  # in rms (std / mean)

# Load experimental data
df = pd.read_csv(Path(__file__).parents[0] / "schmittwilken2024_data.csv")


# %% Helper functions
def gen_all(ppd=PPD, skip=False):
    stims = {}  # save the stimulus-dicts in a larger dict, with name as key
    for stim_name in __all__:
        print(f"Generating schmittwilken2024.{stim_name}")

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


def _create_edge(contrast, edgeWidth, ppd):
    """Horizontal Cornsweet edge stimulus.

    Parameters
    ----------
    contrast : float
        RMS contrast of the edge (std/mean luminance).
    edgeWidth : float
        Width of the transition zone (in degrees).
    ppd : float
        Pixels per degree, used for setting the visual size.

    Returns
    -------
    dict
        Dictionary with the stimulus (key: "img") and additional stimulus parameters.

    References
    ----------
    Schmittwilken, L., Wichmann, F. A., & Maertens, M. (2024).
        Standard models of spatial vision mispredict edge sensitivity at low spatial frequencies.
        Vision Research, 222, 108450. https://doi.org/10.1016/j.visres.2024.108450
    """
    e = cornsweet_edge(
        visual_size=visual_size,
        ppd=ppd,
        ramp_width=edgeWidth,
        exponent=edge_exponent,
        intensity_edges=[-1, 1],
        intensity_plateau=0,
    )
    e = rotate_dict(e, 1)

    eImg = e["img"]
    e["mean_lum"] = mean_lum
    e["img"] = contrast * e["mean_lum"] * eImg / eImg.std() + e["mean_lum"]
    e["edge_contrast"] = contrast
    e["intensity_plateau"] = e["mean_lum"]
    e["intensity_edges"] = (e["img"].min(), e["img"].max())
    del e["d1"]
    del e["d2"]
    return e


def _create_noise(n, ppd):
    """Noise stimulus as described in Schmittwilken et al. (2024).

    Parameters
    ----------
    n : str
        Type of noise to generate. Options: "none", "white", "pink", "brown", "NB05", "NB3", "NB9".
    ppd : float
        Pixels per degree, used to define the resolution of the generated noise.

    Returns
    -------
    numpy.ndarray
        2D array representing the generated noise (rms=0.2).

    References
    ----------
    Schmittwilken, L., Wichmann, F. A., & Maertens, M. (2024).
        Standard models of spatial vision mispredict edge sensitivity at low spatial frequencies.
        Vision Research, 222, 108450. https://doi.org/10.1016/j.visres.2024.108450
    """
    if n == "none":
        noise = np.zeros([int(visual_size * ppd), int(visual_size * ppd)])
    elif n == "white":
        noise = create_whitenoise(visual_size=visual_size, ppd=ppd, pseudo_noise=True)["img"]
    elif n == "pink":
        noise = create_pinknoise(
            visual_size=visual_size, ppd=ppd, exponent=1.0, pseudo_noise=True
        )["img"]
    elif n == "brown":
        noise = create_pinknoise(
            visual_size=visual_size, ppd=ppd, exponent=2.0, pseudo_noise=True
        )["img"]
    elif n == "NB05":
        noise = create_narrownoise(
            visual_size=visual_size,
            ppd=ppd,
            center_frequency=0.5,
            bandwidth=1.0,
            pseudo_noise=True,
        )["img"]
    elif n == "NB3":
        noise = create_narrownoise(
            visual_size=visual_size, ppd=ppd, center_frequency=3, bandwidth=1.0, pseudo_noise=True
        )["img"]
    elif n == "NB9":
        noise = create_narrownoise(
            visual_size=visual_size, ppd=ppd, center_frequency=9, bandwidth=1.0, pseudo_noise=True
        )["img"]

    if not n == "none":
        noise = noise - noise.mean()
        noise = noise / noise.std() * (noise_contrast * mean_lum)
    return noise


def _warnPPD(ppd):
    if ppd != 44:
        warnings.warn(
            "Changing the ppd might affect human performance. "
            "Comparability with experimental data is not"
            "guaranteed for ppd!=44"
        )


def _warnContrast(contrastID):
    if (contrastID < 0) or (contrastID > 4):
        raise ValueError("'contrastID' needs to be within 0 and 4")


# %% Low spatial frequency edge (0.5 cpd)
def edge05_none(ppd=PPD, contrastID=4):
    """Horizontal Cornsweet edge (0.5 cpd) without noise.

    Parameters
    ----------
    ppd : float, optional
        Pixels per degree, used for setting the visual size, by default 44.
    contrastID : int, optional
        Index to select the RMS contrast of the edge from a predefined set, by default 4 (maximum contrast).

    Returns
    -------
    dict
        Dictionary with the stimulus (key: "img") and additional keys containing stimulus parameters and experimental data.

    References
    ----------
    Schmittwilken, L., Wichmann, F. A., & Maertens, M. (2024).
        Standard models of spatial vision mispredict edge sensitivity at low spatial frequencies.
        Vision Research, 222, 108450. https://doi.org/10.1016/j.visres.2024.108450
    """
    _warnContrast(contrastID)
    _warnPPD(ppd)

    c = np.linspace(1e-05, 0.005, 5)[contrastID]
    edge = _create_edge(contrast=c, edgeWidth=0.95, ppd=ppd)
    n = "none"
    noise = _create_noise(n, ppd)

    edge["edge"] = edge["img"]
    edge["noise"] = noise
    edge["img"] = edge["img"] + noise
    edge["noise_contrast"] = noise_contrast
    edge["noise_type"] = n
    edge["experimental_data"] = df[(df.noise == n) & (df.edge == 0.95)].reset_index(drop=True)
    edge["edge_contrasts"] = c
    return edge


def edge05_white(ppd=PPD, contrastID=4):
    """Horizontal Cornsweet edge (0.5 cpd) with white noise.

    Parameters
    ----------
    ppd : float, optional
        Pixels per degree, used for setting the visual size, by default 44.
    contrastID : int, optional
        Index to select the RMS contrast of the edge from a predefined set, by default 4 (maximum contrast).

    Returns
    -------
    dict
        Dictionary with the stimulus (key: "img") and additional keys containing stimulus parameters and experimental data.

    References
    ----------
    Schmittwilken, L., Wichmann, F. A., & Maertens, M. (2024).
        Standard models of spatial vision mispredict edge sensitivity at low spatial frequencies.
        Vision Research, 222, 108450. https://doi.org/10.1016/j.visres.2024.108450
    """
    _warnContrast(contrastID)
    _warnPPD(ppd)

    c = np.linspace(1e-05, 0.015, 5)
    edge = _create_edge(contrast=c[contrastID], edgeWidth=0.95, ppd=ppd)
    n = "white"
    noise = _create_noise(n, ppd)

    edge["edge"] = edge["img"]
    edge["noise"] = noise
    edge["img"] = edge["img"] + noise
    edge["noise_contrast"] = noise_contrast
    edge["noise_type"] = n
    edge["experimental_data"] = df[(df.noise == n) & (df.edge == 0.95)].reset_index(drop=True)
    edge["edge_contrasts"] = c
    return edge


def edge05_pink(ppd=PPD, contrastID=4):
    """Horizontal Cornsweet edge (0.5 cpd) with pink noise.

    Parameters
    ----------
    ppd : float, optional
        Pixels per degree, used for setting the visual size, by default 44.
    contrastID : int, optional
        Index to select the RMS contrast of the edge from a predefined set, by default 4 (maximum contrast).

    Returns
    -------
    dict
        Dictionary with the stimulus (key: "img") and additional keys containing stimulus parameters and experimental data.

    References
    ----------
    Schmittwilken, L., Wichmann, F. A., & Maertens, M. (2024).
        Standard models of spatial vision mispredict edge sensitivity at low spatial frequencies.
        Vision Research, 222, 108450. https://doi.org/10.1016/j.visres.2024.108450
    """
    _warnContrast(contrastID)
    _warnPPD(ppd)

    c = np.linspace(1e-05, 0.05, 5)
    edge = _create_edge(contrast=c[contrastID], edgeWidth=0.95, ppd=ppd)
    n = "pink"
    noise = _create_noise(n, ppd)

    edge["edge"] = edge["img"]
    edge["noise"] = noise
    edge["img"] = edge["img"] + noise
    edge["noise_contrast"] = noise_contrast
    edge["noise_type"] = n
    edge["experimental_data"] = df[(df.noise == n) & (df.edge == 0.95)].reset_index(drop=True)
    edge["edge_contrasts"] = c
    return edge


def edge05_brown(ppd=PPD, contrastID=4):
    """Horizontal Cornsweet edge (0.5 cpd) with brown noise.

    Parameters
    ----------
    ppd : float, optional
        Pixels per degree, used for setting the visual size, by default 44.
    contrastID : int, optional
        Index to select the RMS contrast of the edge from a predefined set, by default 4 (maximum contrast).

    Returns
    -------
    dict
        Dictionary with the stimulus (key: "img") and additional keys containing stimulus parameters and experimental data.

    References
    ----------
    Schmittwilken, L., Wichmann, F. A., & Maertens, M. (2024).
        Standard models of spatial vision mispredict edge sensitivity at low spatial frequencies.
        Vision Research, 222, 108450. https://doi.org/10.1016/j.visres.2024.108450
    """
    _warnContrast(contrastID)
    _warnPPD(ppd)

    c = np.linspace(1e-05, 0.01, 5)
    edge = _create_edge(contrast=c[contrastID], edgeWidth=0.95, ppd=ppd)
    n = "brown"
    noise = _create_noise(n, ppd)

    edge["edge"] = edge["img"]
    edge["noise"] = noise
    edge["img"] = edge["img"] + noise
    edge["noise_contrast"] = noise_contrast
    edge["noise_type"] = n
    edge["experimental_data"] = df[(df.noise == n) & (df.edge == 0.95)].reset_index(drop=True)
    edge["edge_contrasts"] = c
    return edge


def edge05_NB05(ppd=PPD, contrastID=4):
    """Horizontal Cornsweet edge (0.5 cpd) with narrowband noise (0.5 cpd).

    Parameters
    ----------
    ppd : float, optional
        Pixels per degree, used for setting the visual size, by default 44.
    contrastID : int, optional
        Index to select the RMS contrast of the edge from a predefined set, by default 4 (maximum contrast).

    Returns
    -------
    dict
        Dictionary with the stimulus (key: "img") and additional keys containing stimulus parameters and experimental data.

    References
    ----------
    Schmittwilken, L., Wichmann, F. A., & Maertens, M. (2024).
        Standard models of spatial vision mispredict edge sensitivity at low spatial frequencies.
        Vision Research, 222, 108450. https://doi.org/10.1016/j.visres.2024.108450
    """
    _warnContrast(contrastID)
    _warnPPD(ppd)

    c = np.linspace(1e-05, 0.0075, 5)
    edge = _create_edge(contrast=c[contrastID], edgeWidth=0.95, ppd=ppd)
    n = "NB05"
    noise = _create_noise(n, ppd)

    edge["edge"] = edge["img"]
    edge["noise"] = noise
    edge["img"] = edge["img"] + noise
    edge["noise_contrast"] = noise_contrast
    edge["noise_type"] = n
    edge["experimental_data"] = df[(df.noise == n) & (df.edge == 0.95)].reset_index(drop=True)
    edge["edge_contrasts"] = c
    return edge


def edge05_NB3(ppd=PPD, contrastID=4):
    """Horizontal Cornsweet edge (0.5 cpd) with narrowband noise (3 cpd).

    Parameters
    ----------
    ppd : float, optional
        Pixels per degree, used for setting the visual size, by default 44.
    contrastID : int, optional
        Index to select the RMS contrast of the edge from a predefined set, by default 4 (maximum contrast).

    Returns
    -------
    dict
        Dictionary with the stimulus (key: "img") and additional keys containing stimulus parameters and experimental data.

    References
    ----------
    Schmittwilken, L., Wichmann, F. A., & Maertens, M. (2024).
        Standard models of spatial vision mispredict edge sensitivity at low spatial frequencies.
        Vision Research, 222, 108450. https://doi.org/10.1016/j.visres.2024.108450
    """
    _warnContrast(contrastID)
    _warnPPD(ppd)

    c = np.linspace(1e-05, 0.03, 5)
    edge = _create_edge(contrast=c[contrastID], edgeWidth=0.95, ppd=ppd)
    n = "NB3"
    noise = _create_noise(n, ppd)

    edge["edge"] = edge["img"]
    edge["noise"] = noise
    edge["img"] = edge["img"] + noise
    edge["noise_contrast"] = noise_contrast
    edge["noise_type"] = n
    edge["experimental_data"] = df[(df.noise == n) & (df.edge == 0.95)].reset_index(drop=True)
    edge["edge_contrasts"] = c
    return edge


def edge05_NB9(ppd=PPD, contrastID=4):
    """Horizontal Cornsweet edge (0.5 cpd) with narrowband noise (9 cpd).

    Parameters
    ----------
    ppd : float, optional
        Pixels per degree, used for setting the visual size, by default 44.
    contrastID : int, optional
        Index to select the RMS contrast of the edge from a predefined set, by default 4 (maximum contrast).

    Returns
    -------
    dict
        Dictionary with the stimulus (key: "img") and additional keys containing stimulus parameters and experimental data.

    References
    ----------
    Schmittwilken, L., Wichmann, F. A., & Maertens, M. (2024).
        Standard models of spatial vision mispredict edge sensitivity at low spatial frequencies.
        Vision Research, 222, 108450. https://doi.org/10.1016/j.visres.2024.108450
    """
    _warnContrast(contrastID)
    _warnPPD(ppd)

    c = np.linspace(1e-05, 0.0075, 5)
    edge = _create_edge(contrast=c[contrastID], edgeWidth=0.95, ppd=ppd)
    n = "NB9"
    noise = _create_noise(n, ppd)

    edge["edge"] = edge["img"]
    edge["noise"] = noise
    edge["img"] = edge["img"] + noise
    edge["noise_contrast"] = noise_contrast
    edge["noise_type"] = n
    edge["experimental_data"] = df[(df.noise == n) & (df.edge == 0.95)].reset_index(drop=True)
    edge["edge_contrasts"] = c
    return edge


# %% Mid spatial frequency edge (3 cpd)
def edge3_none(ppd=PPD, contrastID=4):
    """Horizontal Cornsweet edge (3 cpd) without noise.

    Parameters
    ----------
    ppd : float, optional
        Pixels per degree, used for setting the visual size, by default 44.
    contrastID : int, optional
        Index to select the RMS contrast of the edge from a predefined set, by default 4 (maximum contrast).

    Returns
    -------
    dict
        Dictionary with the stimulus (key: "img") and additional keys containing stimulus parameters and experimental data.

    References
    ----------
    Schmittwilken, L., Wichmann, F. A., & Maertens, M. (2024).
        Standard models of spatial vision mispredict edge sensitivity at low spatial frequencies.
        Vision Research, 222, 108450. https://doi.org/10.1016/j.visres.2024.108450
    """
    _warnContrast(contrastID)
    _warnPPD(ppd)

    c = np.linspace(1e-05, 0.004, 5)
    edge = _create_edge(contrast=c[contrastID], edgeWidth=0.95, ppd=ppd)
    n = "none"
    noise = _create_noise(n, ppd)

    edge["edge"] = edge["img"]
    edge["noise"] = noise
    edge["img"] = edge["img"] + noise
    edge["noise_contrast"] = noise_contrast
    edge["noise_type"] = n
    edge["experimental_data"] = df[(df.noise == n) & (df.edge == 0.15)].reset_index(drop=True)
    edge["edge_contrasts"] = c
    return edge


def edge3_white(ppd=PPD, contrastID=4):
    """Horizontal Cornsweet edge (3 cpd) with white noise.

    Parameters
    ----------
    ppd : float, optional
        Pixels per degree, used for setting the visual size, by default 44.
    contrastID : int, optional
        Index to select the RMS contrast of the edge from a predefined set, by default 4 (maximum contrast).

    Returns
    -------
    dict
        Dictionary with the stimulus (key: "img") and additional keys containing stimulus parameters and experimental data.

    References
    ----------
    Schmittwilken, L., Wichmann, F. A., & Maertens, M. (2024).
        Standard models of spatial vision mispredict edge sensitivity at low spatial frequencies.
        Vision Research, 222, 108450. https://doi.org/10.1016/j.visres.2024.108450
    """
    _warnContrast(contrastID)
    _warnPPD(ppd)

    c = np.linspace(1e-05, 0.0125, 5)
    edge = _create_edge(contrast=c[contrastID], edgeWidth=0.95, ppd=ppd)
    n = "white"
    noise = _create_noise(n, ppd)

    edge["edge"] = edge["img"]
    edge["noise"] = noise
    edge["img"] = edge["img"] + noise
    edge["noise_contrast"] = noise_contrast
    edge["noise_type"] = n
    edge["experimental_data"] = df[(df.noise == n) & (df.edge == 0.15)].reset_index(drop=True)
    edge["edge_contrasts"] = c
    return edge


def edge3_pink(ppd=PPD, contrastID=4):
    """Horizontal Cornsweet edge (3 cpd) with pink noise.

    Parameters
    ----------
    ppd : float, optional
        Pixels per degree, used for setting the visual size, by default 44.
    contrastID : int, optional
        Index to select the RMS contrast of the edge from a predefined set, by default 4 (maximum contrast).

    Returns
    -------
    dict
        Dictionary with the stimulus (key: "img") and additional keys containing stimulus parameters and experimental data.

    References
    ----------
    Schmittwilken, L., Wichmann, F. A., & Maertens, M. (2024).
        Standard models of spatial vision mispredict edge sensitivity at low spatial frequencies.
        Vision Research, 222, 108450. https://doi.org/10.1016/j.visres.2024.108450
    """
    _warnContrast(contrastID)
    _warnPPD(ppd)

    c = np.linspace(1e-05, 0.03, 5)
    edge = _create_edge(contrast=c[contrastID], edgeWidth=0.95, ppd=ppd)
    n = "pink"
    noise = _create_noise(n, ppd)

    edge["edge"] = edge["img"]
    edge["noise"] = noise
    edge["img"] = edge["img"] + noise
    edge["noise_contrast"] = noise_contrast
    edge["noise_type"] = n
    edge["experimental_data"] = df[(df.noise == n) & (df.edge == 0.15)].reset_index(drop=True)
    edge["edge_contrasts"] = c
    return edge


def edge3_brown(ppd=PPD, contrastID=4):
    """Horizontal Cornsweet edge (3 cpd) with brown noise.

    Parameters
    ----------
    ppd : float, optional
        Pixels per degree, used for setting the visual size, by default 44.
    contrastID : int, optional
        Index to select the RMS contrast of the edge from a predefined set, by default 4 (maximum contrast).

    Returns
    -------
    dict
        Dictionary with the stimulus (key: "img") and additional keys containing stimulus parameters and experimental data.

    References
    ----------
    Schmittwilken, L., Wichmann, F. A., & Maertens, M. (2024).
        Standard models of spatial vision mispredict edge sensitivity at low spatial frequencies.
        Vision Research, 222, 108450. https://doi.org/10.1016/j.visres.2024.108450
    """
    _warnContrast(contrastID)
    _warnPPD(ppd)

    c = np.linspace(1e-05, 0.006, 5)
    edge = _create_edge(contrast=c[contrastID], edgeWidth=0.95, ppd=ppd)
    n = "brown"
    noise = _create_noise(n, ppd)

    edge["edge"] = edge["img"]
    edge["noise"] = noise
    edge["img"] = edge["img"] + noise
    edge["noise_contrast"] = noise_contrast
    edge["noise_type"] = n
    edge["experimental_data"] = df[(df.noise == n) & (df.edge == 0.15)].reset_index(drop=True)
    edge["edge_contrasts"] = c
    return edge


def edge3_NB05(ppd=PPD, contrastID=4):
    """Horizontal Cornsweet edge (3 cpd) with narrowband noise (0.5 cpd).

    Parameters
    ----------
    ppd : float, optional
        Pixels per degree, used for setting the visual size, by default 44.
    contrastID : int, optional
        Index to select the RMS contrast of the edge from a predefined set, by default 4 (maximum contrast).

    Returns
    -------
    dict
        Dictionary with the stimulus (key: "img") and additional keys containing stimulus parameters and experimental data.

    References
    ----------
    Schmittwilken, L., Wichmann, F. A., & Maertens, M. (2024).
        Standard models of spatial vision mispredict edge sensitivity at low spatial frequencies.
        Vision Research, 222, 108450. https://doi.org/10.1016/j.visres.2024.108450
    """
    _warnContrast(contrastID)
    _warnPPD(ppd)

    c = np.linspace(1e-05, 0.003, 5)
    edge = _create_edge(contrast=c[contrastID], edgeWidth=0.95, ppd=ppd)
    n = "NB05"
    noise = _create_noise(n, ppd)

    edge["edge"] = edge["img"]
    edge["noise"] = noise
    edge["img"] = edge["img"] + noise
    edge["noise_contrast"] = noise_contrast
    edge["noise_type"] = n
    edge["experimental_data"] = df[(df.noise == n) & (df.edge == 0.15)].reset_index(drop=True)
    edge["edge_contrasts"] = c
    return edge


def edge3_NB3(ppd=PPD, contrastID=4):
    """Horizontal Cornsweet edge (3 cpd) with narrowband noise (3 cpd).

    Parameters
    ----------
    ppd : float, optional
        Pixels per degree, used for setting the visual size, by default 44.
    contrastID : int, optional
        Index to select the RMS contrast of the edge from a predefined set, by default 4 (maximum contrast).

    Returns
    -------
    dict
        Dictionary with the stimulus (key: "img") and additional keys containing stimulus parameters and experimental data.

    References
    ----------
    Schmittwilken, L., Wichmann, F. A., & Maertens, M. (2024).
        Standard models of spatial vision mispredict edge sensitivity at low spatial frequencies.
        Vision Research, 222, 108450. https://doi.org/10.1016/j.visres.2024.108450
    """
    _warnContrast(contrastID)
    _warnPPD(ppd)

    c = np.linspace(1e-05, 0.015, 5)
    edge = _create_edge(contrast=c[contrastID], edgeWidth=0.95, ppd=ppd)
    n = "NB3"
    noise = _create_noise(n, ppd)

    edge["edge"] = edge["img"]
    edge["noise"] = noise
    edge["img"] = edge["img"] + noise
    edge["noise_contrast"] = noise_contrast
    edge["noise_type"] = n
    edge["experimental_data"] = df[(df.noise == n) & (df.edge == 0.15)].reset_index(drop=True)
    edge["edge_contrasts"] = c
    return edge


def edge3_NB9(ppd=PPD, contrastID=4):
    """Horizontal Cornsweet edge (3 cpd) with narrowband noise (9 cpd).

    Parameters
    ----------
    ppd : float, optional
        Pixels per degree, used for setting the visual size, by default 44.
    contrastID : int, optional
        Index to select the RMS contrast of the edge from a predefined set, by default 4 (maximum contrast).

    Returns
    -------
    dict
        Dictionary with the stimulus (key: "img") and additional keys containing stimulus parameters and experimental data.

    References
    ----------
    Schmittwilken, L., Wichmann, F. A., & Maertens, M. (2024).
        Standard models of spatial vision mispredict edge sensitivity at low spatial frequencies.
        Vision Research, 222, 108450. https://doi.org/10.1016/j.visres.2024.108450
    """
    _warnContrast(contrastID)
    _warnPPD(ppd)

    c = np.linspace(1e-05, 0.0075, 5)
    edge = _create_edge(contrast=c[contrastID], edgeWidth=0.95, ppd=ppd)
    n = "NB9"
    noise = _create_noise(n, ppd)

    edge["edge"] = edge["img"]
    edge["noise"] = noise
    edge["img"] = edge["img"] + noise
    edge["noise_contrast"] = noise_contrast
    edge["noise_type"] = n
    edge["experimental_data"] = df[(df.noise == n) & (df.edge == 0.15)].reset_index(drop=True)
    edge["edge_contrasts"] = c
    return edge


# %% High spatial frequency edge (9 cpd)
def edge9_none(ppd=PPD, contrastID=4):
    """Horizontal Cornsweet edge (9 cpd) without noise.

    Parameters
    ----------
    ppd : float, optional
        Pixels per degree, used for setting the visual size, by default 44.
    contrastID : int, optional
        Index to select the RMS contrast of the edge from a predefined set, by default 4 (maximum contrast).

    Returns
    -------
    dict
        Dictionary with the stimulus (key: "img") and additional keys containing stimulus parameters and experimental data.

    References
    ----------
    Schmittwilken, L., Wichmann, F. A., & Maertens, M. (2024).
        Standard models of spatial vision mispredict edge sensitivity at low spatial frequencies.
        Vision Research, 222, 108450. https://doi.org/10.1016/j.visres.2024.108450
    """
    _warnContrast(contrastID)
    _warnPPD(ppd)

    c = np.linspace(1e-05, 0.003, 5)
    edge = _create_edge(contrast=c[contrastID], edgeWidth=0.95, ppd=ppd)
    n = "none"
    noise = _create_noise(n, ppd)

    edge["edge"] = edge["img"]
    edge["noise"] = noise
    edge["img"] = edge["img"] + noise
    edge["noise_contrast"] = noise_contrast
    edge["noise_type"] = n
    edge["experimental_data"] = df[(df.noise == n) & (df.edge == 0.048)].reset_index(drop=True)
    edge["edge_contrasts"] = c
    return edge


def edge9_white(ppd=PPD, contrastID=4):
    """Horizontal Cornsweet edge (9 cpd) with white noise.

    Parameters
    ----------
    ppd : float, optional
        Pixels per degree, used for setting the visual size, by default 44.
    contrastID : int, optional
        Index to select the RMS contrast of the edge from a predefined set, by default 4 (maximum contrast).

    Returns
    -------
    dict
        Dictionary with the stimulus (key: "img") and additional keys containing stimulus parameters and experimental data.

    References
    ----------
    Schmittwilken, L., Wichmann, F. A., & Maertens, M. (2024).
        Standard models of spatial vision mispredict edge sensitivity at low spatial frequencies.
        Vision Research, 222, 108450. https://doi.org/10.1016/j.visres.2024.108450
    """
    _warnContrast(contrastID)
    _warnPPD(ppd)

    c = np.linspace(1e-05, 0.015, 5)
    edge = _create_edge(contrast=c[contrastID], edgeWidth=0.95, ppd=ppd)
    n = "white"
    noise = _create_noise(n, ppd)

    edge["edge"] = edge["img"]
    edge["noise"] = noise
    edge["img"] = edge["img"] + noise
    edge["noise_contrast"] = noise_contrast
    edge["noise_type"] = n
    edge["experimental_data"] = df[(df.noise == n) & (df.edge == 0.048)].reset_index(drop=True)
    edge["edge_contrasts"] = c
    return edge


def edge9_pink(ppd=PPD, contrastID=4):
    """Horizontal Cornsweet edge (9 cpd) with pink noise.

    Parameters
    ----------
    ppd : float, optional
        Pixels per degree, used for setting the visual size, by default 44.
    contrastID : int, optional
        Index to select the RMS contrast of the edge from a predefined set, by default 4 (maximum contrast).

    Returns
    -------
    dict
        Dictionary with the stimulus (key: "img") and additional keys containing stimulus parameters and experimental data.

    References
    ----------
    Schmittwilken, L., Wichmann, F. A., & Maertens, M. (2024).
        Standard models of spatial vision mispredict edge sensitivity at low spatial frequencies.
        Vision Research, 222, 108450. https://doi.org/10.1016/j.visres.2024.108450
    """
    _warnContrast(contrastID)
    _warnPPD(ppd)

    c = np.linspace(1e-05, 0.015, 5)
    edge = _create_edge(contrast=c[contrastID], edgeWidth=0.95, ppd=ppd)
    n = "pink"
    noise = _create_noise(n, ppd)

    edge["edge"] = edge["img"]
    edge["noise"] = noise
    edge["img"] = edge["img"] + noise
    edge["noise_contrast"] = noise_contrast
    edge["noise_type"] = n
    edge["experimental_data"] = df[(df.noise == n) & (df.edge == 0.048)].reset_index(drop=True)
    edge["edge_contrasts"] = c
    return edge


def edge9_brown(ppd=PPD, contrastID=4):
    """Horizontal Cornsweet edge (9 cpd) with brown noise.

    Parameters
    ----------
    ppd : float, optional
        Pixels per degree, used for setting the visual size, by default 44.
    contrastID : int, optional
        Index to select the RMS contrast of the edge from a predefined set, by default 4 (maximum contrast).

    Returns
    -------
    dict
        Dictionary with the stimulus (key: "img") and additional keys containing stimulus parameters and experimental data.

    References
    ----------
    Schmittwilken, L., Wichmann, F. A., & Maertens, M. (2024).
        Standard models of spatial vision mispredict edge sensitivity at low spatial frequencies.
        Vision Research, 222, 108450. https://doi.org/10.1016/j.visres.2024.108450
    """
    _warnContrast(contrastID)
    _warnPPD(ppd)

    c = np.linspace(1e-05, 0.004, 5)
    edge = _create_edge(contrast=c[contrastID], edgeWidth=0.95, ppd=ppd)
    n = "brown"
    noise = _create_noise(n, ppd)

    edge["edge"] = edge["img"]
    edge["noise"] = noise
    edge["img"] = edge["img"] + noise
    edge["noise_contrast"] = noise_contrast
    edge["noise_type"] = n
    edge["experimental_data"] = df[(df.noise == n) & (df.edge == 0.048)].reset_index(drop=True)
    edge["edge_contrasts"] = c
    return edge


def edge9_NB05(ppd=PPD, contrastID=4):
    """Horizontal Cornsweet edge (9 cpd) with narrowband noise (0.5 cpd).

    Parameters
    ----------
    ppd : float, optional
        Pixels per degree, used for setting the visual size, by default 44.
    contrastID : int, optional
        Index to select the RMS contrast of the edge from a predefined set, by default 4 (maximum contrast).

    Returns
    -------
    dict
        Dictionary with the stimulus (key: "img") and additional keys containing stimulus parameters and experimental data.

    References
    ----------
    Schmittwilken, L., Wichmann, F. A., & Maertens, M. (2024).
        Standard models of spatial vision mispredict edge sensitivity at low spatial frequencies.
        Vision Research, 222, 108450. https://doi.org/10.1016/j.visres.2024.108450
    """
    _warnContrast(contrastID)
    _warnPPD(ppd)

    c = np.linspace(1e-05, 0.005, 5)
    edge = _create_edge(contrast=c[contrastID], edgeWidth=0.95, ppd=ppd)
    n = "NB05"
    noise = _create_noise(n, ppd)

    edge["edge"] = edge["img"]
    edge["noise"] = noise
    edge["img"] = edge["img"] + noise
    edge["noise_contrast"] = noise_contrast
    edge["noise_type"] = n
    edge["experimental_data"] = df[(df.noise == n) & (df.edge == 0.048)].reset_index(drop=True)
    edge["edge_contrasts"] = c
    return edge


def edge9_NB3(ppd=PPD, contrastID=4):
    """Horizontal Cornsweet edge (9 cpd) with narrowband noise (3 cpd).

    Parameters
    ----------
    ppd : float, optional
        Pixels per degree, used for setting the visual size, by default 44.
    contrastID : int, optional
        Index to select the RMS contrast of the edge from a predefined set, by default 4 (maximum contrast).

    Returns
    -------
    dict
        Dictionary with the stimulus (key: "img") and additional keys containing stimulus parameters and experimental data.

    References
    ----------
    Schmittwilken, L., Wichmann, F. A., & Maertens, M. (2024).
        Standard models of spatial vision mispredict edge sensitivity at low spatial frequencies.
        Vision Research, 222, 108450. https://doi.org/10.1016/j.visres.2024.108450
    """
    _warnContrast(contrastID)
    _warnPPD(ppd)

    c = np.linspace(1e-05, 0.006, 5)
    edge = _create_edge(contrast=c[contrastID], edgeWidth=0.95, ppd=ppd)
    n = "NB3"
    noise = _create_noise(n, ppd)

    edge["edge"] = edge["img"]
    edge["noise"] = noise
    edge["img"] = edge["img"] + noise
    edge["noise_contrast"] = noise_contrast
    edge["noise_type"] = n
    edge["experimental_data"] = df[(df.noise == n) & (df.edge == 0.048)].reset_index(drop=True)
    edge["edge_contrasts"] = c
    return edge


def edge9_NB9(ppd=PPD, contrastID=4):
    """Horizontal Cornsweet edge (9 cpd) with narrowband noise (9 cpd).

    Parameters
    ----------
    ppd : float, optional
        Pixels per degree, used for setting the visual size, by default 44.
    contrastID : int, optional
        Index to select the RMS contrast of the edge from a predefined set, by default 4 (maximum contrast).

    Returns
    -------
    dict
        Dictionary with the stimulus (key: "img") and additional keys containing stimulus parameters and experimental data.

    References
    ----------
    Schmittwilken, L., Wichmann, F. A., & Maertens, M. (2024).
        Standard models of spatial vision mispredict edge sensitivity at low spatial frequencies.
        Vision Research, 222, 108450. https://doi.org/10.1016/j.visres.2024.108450
    """
    _warnContrast(contrastID)
    _warnPPD(ppd)

    c = np.linspace(1e-05, 0.015, 5)
    edge = _create_edge(contrast=c[contrastID], edgeWidth=0.95, ppd=ppd)
    n = "NB9"
    noise = _create_noise(n, ppd)

    edge["edge"] = edge["img"]
    edge["noise"] = noise
    edge["img"] = edge["img"] + noise
    edge["noise_contrast"] = noise_contrast
    edge["noise_type"] = n
    edge["experimental_data"] = df[(df.noise == n) & (df.edge == 0.048)].reset_index(drop=True)
    edge["edge_contrasts"] = c
    return edge


# %% Main script
if __name__ == "__main__":
    from stimupy.utils import plot_stimuli

    stims = gen_all(skip=True)
    plot_stimuli(stims, mask=False, units="visual_size", vmin=0, vmax=200)
