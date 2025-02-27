"""Stimuli and data from Schmittwilken, Wichmann, & Maertens (2024)
https://doi.org/10.1016/j.visres.2024.108450

This module reproduces all stimuli used by Schmittwilken, Wichmann, & Maertens
(2024) with random noise instances, and provides the corresponding raw
sensitivity functions of each subject and the average observer.

Each stimulus is provided by a separate function,
a full list can be found as stimupy.papers.schmittwilken2024.__all__

The output of each of these functions is a stimulus dictionary.

For a visual representation of all the stimuli, simply run this module as a
script:

    $ python stimuli/papers/schmittwilken2024.py

Attributes
----------
__all__ (list of str): list of all stimulus-functions
    that are exported by this module when executing
        >>> from stimupy.papers.schmittwilken2024 import *

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

__all__ = [
    "lsfEdge_none",
    "lsfEdge_white",
    "lsfEdge_pink",
    "lsfEdge_brown",
    "lsfEdge_NB05",
    "lsfEdge_NB3",
    "lsfEdge_NB9",
    "msfEdge_none",
    "msfEdge_white",
    "msfEdge_pink",
    "msfEdge_brown",
    "msfEdge_NB05",
    "msfEdge_NB3",
    "msfEdge_NB9",
    "hsfEdge_none",
    "hsfEdge_white",
    "hsfEdge_pink",
    "hsfEdge_brown",
    "hsfEdge_NB05",
    "hsfEdge_NB3",
    "hsfEdge_NB9",
    
]

PPD = 44.

# Default stimulus parameters
stim_params = {
    "stim_size": 4.,       # in deg
    "ppd": 44.,            # pixels per degree
    "mean_lum": 100.,      # in cd/m**2
    "edge_exponent": 1.,   # affect ramp of Cornsweet edges
    "noise_contrast": 0.2  # in rms
    }


# Load experimental data
df = pd.read_csv(Path(__file__).parents[0] / "schmittwilken2024_data.csv")
# participants = df[0]


def _create_edge(contrast, edgeWidth, stim_params):
    e = cornsweet_edge(
        visual_size=stim_params["stim_size"],
        ppd=stim_params["ppd"],
        ramp_width=edgeWidth,
        exponent=stim_params["edge_exponent"],
        intensity_edges=[-1, 1],
        intensity_plateau=0,
        )
    eImg = e["img"]
    e["mean_lum"] = stim_params["mean_lum"]
    e["img"] = contrast * e["mean_lum"] * eImg/eImg.std() + e["mean_lum"]
    e["edge_contrast"] = contrast
    e["intensity_plateau"] = e["mean_lum"]
    e["intensity_edges"] = (e["img"].min(), e["img"].max())
    del e["d1"]
    del e["d2"]
    return e

def _create_noise(n, stim_params):
    sp = stim_params
    ssize = sp["stim_size"]
    ppd = sp["ppd"]
    rms = sp["noise_contrast"] * sp["mean_lum"]
    
    if n == "none":
        noise = np.zeros([int(ssize*ppd), int(ssize*ppd)])
    elif n == "white":
        noise = create_whitenoise(visual_size=ssize, ppd=ppd, pseudo_noise=True)["img"]
    elif n == "pink":
        noise = create_pinknoise(visual_size=ssize, ppd=ppd, exponent=1., pseudo_noise=True)["img"]
    elif n == "brown":
        noise = create_pinknoise(visual_size=ssize, ppd=ppd, exponent=2., pseudo_noise=True)["img"]
    elif n == "NB05":
        noise = create_narrownoise(visual_size=ssize, ppd=ppd, center_frequency=0.5, bandwidth=1., pseudo_noise=True)["img"]
    elif n == "NB3":
        noise = create_narrownoise(visual_size=ssize, ppd=ppd, center_frequency=3, bandwidth=1., pseudo_noise=True)["img"]
    elif n == "NB9":
        noise = create_narrownoise(visual_size=ssize, ppd=ppd, center_frequency=9, bandwidth=1., pseudo_noise=True)["img"]

    if not n=="none":
        noise = noise - noise.mean()
        noise = noise / noise.std() * rms
    return noise

def _warnPPD(ppd):
    if ppd != 44:
        warnings.warn("Changing the ppd might affect human performance. "
                      "Comparability with experimental data is not"
                      "guaranteed for ppd!=44")

def _warnContrast(contrastID):
    if (contrastID<0) or (contrastID>4):
        raise ValueError("'contrastID' needs to be within 0 and 4")
    


# %% Low spatial frequency edge (0.5 cpd)
def lsfEdge_none(ppd=PPD, contrastID=4):
    _warnContrast(contrastID)
    _warnPPD(ppd)
        
    c = np.linspace(1e-05, 0.005, 5)[contrastID]
    edge = _create_edge(contrast=c, edgeWidth=0.95, stim_params=stim_params)
    n = "none"
    noise = _create_noise(n, stim_params)
    
    edge["edge"] = edge["img"]
    edge["noise"] = noise
    edge["img"] = edge["img"] + noise
    edge["noise_contrast"] = stim_params["noise_contrast"]
    edge["noise_type"] = n
    edge["experimental_data"] = df[(df.noise==n) & (df.edge==0.95)].reset_index(drop=True)
    return edge


def lsfEdge_white(ppd=PPD, contrastID=4):
    _warnContrast(contrastID)
    _warnPPD(ppd)
        
    c = np.linspace(1e-05, 0.015, 5)[contrastID]
    edge = _create_edge(contrast=c, edgeWidth=0.95, stim_params=stim_params)
    n = "white"
    noise = _create_noise(n, stim_params)
    
    edge["edge"] = edge["img"]
    edge["noise"] = noise
    edge["img"] = edge["img"] + noise
    edge["noise_contrast"] = stim_params["noise_contrast"]
    edge["noise_type"] = n
    edge["experimental_data"] = df[(df.noise==n) & (df.edge==0.95)].reset_index(drop=True)
    return edge

def lsfEdge_pink(ppd=PPD, contrastID=4):
    _warnContrast(contrastID)
    _warnPPD(ppd)
        
    c = np.linspace(1e-05, 0.05, 5)[contrastID]
    edge = _create_edge(contrast=c, edgeWidth=0.95, stim_params=stim_params)
    n = "pink"
    noise = _create_noise(n, stim_params)
    
    edge["edge"] = edge["img"]
    edge["noise"] = noise
    edge["img"] = edge["img"] + noise
    edge["noise_contrast"] = stim_params["noise_contrast"]
    edge["noise_type"] = n
    edge["experimental_data"] = df[(df.noise==n) & (df.edge==0.95)].reset_index(drop=True)
    return edge

def lsfEdge_brown(ppd=PPD, contrastID=4):
    _warnContrast(contrastID)
    _warnPPD(ppd)
        
    c = np.linspace(1e-05, 0.01, 5)[contrastID]
    edge = _create_edge(contrast=c, edgeWidth=0.95, stim_params=stim_params)
    n = "brown"
    noise = _create_noise(n, stim_params)
    
    edge["edge"] = edge["img"]
    edge["noise"] = noise
    edge["img"] = edge["img"] + noise
    edge["noise_contrast"] = stim_params["noise_contrast"]
    edge["noise_type"] = n
    edge["experimental_data"] = df[(df.noise==n) & (df.edge==0.95)].reset_index(drop=True)
    return edge

def lsfEdge_NB05(ppd=PPD, contrastID=4):
    _warnContrast(contrastID)
    _warnPPD(ppd)
        
    c = np.linspace(1e-05, 0.0075, 5)[contrastID]
    edge = _create_edge(contrast=c, edgeWidth=0.95, stim_params=stim_params)
    n = "NB05"
    noise = _create_noise(n, stim_params)
    
    edge["edge"] = edge["img"]
    edge["noise"] = noise
    edge["img"] = edge["img"] + noise
    edge["noise_contrast"] = stim_params["noise_contrast"]
    edge["noise_type"] = n
    edge["experimental_data"] = df[(df.noise==n) & (df.edge==0.95)].reset_index(drop=True)
    return edge

def lsfEdge_NB3(ppd=PPD, contrastID=4):
    _warnContrast(contrastID)
    _warnPPD(ppd)
        
    c = np.linspace(1e-05, 0.03, 5)[contrastID]
    edge = _create_edge(contrast=c, edgeWidth=0.95, stim_params=stim_params)
    n = "NB3"
    noise = _create_noise(n, stim_params)
    
    edge["edge"] = edge["img"]
    edge["noise"] = noise
    edge["img"] = edge["img"] + noise
    edge["noise_contrast"] = stim_params["noise_contrast"]
    edge["noise_type"] = n
    edge["experimental_data"] = df[(df.noise==n) & (df.edge==0.95)].reset_index(drop=True)
    return edge

def lsfEdge_NB9(ppd=PPD, contrastID=4):
    _warnContrast(contrastID)
    _warnPPD(ppd)
        
    c = np.linspace(1e-05, 0.0075, 5)[contrastID]
    edge = _create_edge(contrast=c, edgeWidth=0.95, stim_params=stim_params)
    n = "NB9"
    noise = _create_noise(n, stim_params)
    
    edge["edge"] = edge["img"]
    edge["noise"] = noise
    edge["img"] = edge["img"] + noise
    edge["noise_contrast"] = stim_params["noise_contrast"]
    edge["noise_type"] = n
    edge["experimental_data"] = df[(df.noise==n) & (df.edge==0.95)].reset_index(drop=True)
    return edge

# %% Mid spatial frequency edge (3 cpd)
def msfEdge_none(ppd=PPD, contrastID=4):
    _warnContrast(contrastID)
    _warnPPD(ppd)
        
    c = np.linspace(1e-05, 0.004, 5)[contrastID]
    edge = _create_edge(contrast=c, edgeWidth=0.95, stim_params=stim_params)
    n = "none"
    noise = _create_noise(n, stim_params)
    
    edge["edge"] = edge["img"]
    edge["noise"] = noise
    edge["img"] = edge["img"] + noise
    edge["noise_contrast"] = stim_params["noise_contrast"]
    edge["noise_type"] = n
    edge["experimental_data"] = df[(df.noise==n) & (df.edge==0.15)].reset_index(drop=True)
    return edge


def msfEdge_white(ppd=PPD, contrastID=4):
    _warnContrast(contrastID)
    _warnPPD(ppd)
        
    c = np.linspace(1e-05, 0.0125, 5)[contrastID]
    edge = _create_edge(contrast=c, edgeWidth=0.95, stim_params=stim_params)
    n = "white"
    noise = _create_noise(n, stim_params)
    
    edge["edge"] = edge["img"]
    edge["noise"] = noise
    edge["img"] = edge["img"] + noise
    edge["noise_contrast"] = stim_params["noise_contrast"]
    edge["noise_type"] = n
    edge["experimental_data"] = df[(df.noise==n) & (df.edge==0.15)].reset_index(drop=True)
    return edge

def msfEdge_pink(ppd=PPD, contrastID=4):
    _warnContrast(contrastID)
    _warnPPD(ppd)
        
    c = np.linspace(1e-05, 0.03, 5)[contrastID]
    edge = _create_edge(contrast=c, edgeWidth=0.95, stim_params=stim_params)
    n = "pink"
    noise = _create_noise(n, stim_params)
    
    edge["edge"] = edge["img"]
    edge["noise"] = noise
    edge["img"] = edge["img"] + noise
    edge["noise_contrast"] = stim_params["noise_contrast"]
    edge["noise_type"] = n
    edge["experimental_data"] = df[(df.noise==n) & (df.edge==0.15)].reset_index(drop=True)
    return edge

def msfEdge_brown(ppd=PPD, contrastID=4):
    _warnContrast(contrastID)
    _warnPPD(ppd)
        
    c = np.linspace(1e-05, 0.006, 5)[contrastID]
    edge = _create_edge(contrast=c, edgeWidth=0.95, stim_params=stim_params)
    n = "brown"
    noise = _create_noise(n, stim_params)
    
    edge["edge"] = edge["img"]
    edge["noise"] = noise
    edge["img"] = edge["img"] + noise
    edge["noise_contrast"] = stim_params["noise_contrast"]
    edge["noise_type"] = n
    edge["experimental_data"] = df[(df.noise==n) & (df.edge==0.15)].reset_index(drop=True)
    return edge

def msfEdge_NB05(ppd=PPD, contrastID=4):
    _warnContrast(contrastID)
    _warnPPD(ppd)
        
    c = np.linspace(1e-05, 0.003, 5)[contrastID]
    edge = _create_edge(contrast=c, edgeWidth=0.95, stim_params=stim_params)
    n = "NB05"
    noise = _create_noise(n, stim_params)
    
    edge["edge"] = edge["img"]
    edge["noise"] = noise
    edge["img"] = edge["img"] + noise
    edge["noise_contrast"] = stim_params["noise_contrast"]
    edge["noise_type"] = n
    edge["experimental_data"] = df[(df.noise==n) & (df.edge==0.15)].reset_index(drop=True)
    return edge

def msfEdge_NB3(ppd=PPD, contrastID=4):
    _warnContrast(contrastID)
    _warnPPD(ppd)
        
    c = np.linspace(1e-05, 0.015, 5)[contrastID]
    edge = _create_edge(contrast=c, edgeWidth=0.95, stim_params=stim_params)
    n = "NB3"
    noise = _create_noise(n, stim_params)
    
    edge["edge"] = edge["img"]
    edge["noise"] = noise
    edge["img"] = edge["img"] + noise
    edge["noise_contrast"] = stim_params["noise_contrast"]
    edge["noise_type"] = n
    edge["experimental_data"] = df[(df.noise==n) & (df.edge==0.15)].reset_index(drop=True)
    return edge

def msfEdge_NB9(ppd=PPD, contrastID=4):
    _warnContrast(contrastID)
    _warnPPD(ppd)
        
    c = np.linspace(1e-05, 0.0075, 5)[contrastID]
    edge = _create_edge(contrast=c, edgeWidth=0.95, stim_params=stim_params)
    n = "NB9"
    noise = _create_noise(n, stim_params)
    
    edge["edge"] = edge["img"]
    edge["noise"] = noise
    edge["img"] = edge["img"] + noise
    edge["noise_contrast"] = stim_params["noise_contrast"]
    edge["noise_type"] = n
    edge["experimental_data"] = df[(df.noise==n) & (df.edge==0.15)].reset_index(drop=True)
    return edge

# %% High spatial frequency edge (9 cpd)
def hsfEdge_none(ppd=PPD, contrastID=4):
    _warnContrast(contrastID)
    _warnPPD(ppd)
        
    c = np.linspace(1e-05, 0.003, 5)[contrastID]
    edge = _create_edge(contrast=c, edgeWidth=0.95, stim_params=stim_params)
    n = "none"
    noise = _create_noise(n, stim_params)
    
    edge["edge"] = edge["img"]
    edge["noise"] = noise
    edge["img"] = edge["img"] + noise
    edge["noise_contrast"] = stim_params["noise_contrast"]
    edge["noise_type"] = n
    edge["experimental_data"] = df[(df.noise==n) & (df.edge==0.048)].reset_index(drop=True)
    return edge


def hsfEdge_white(ppd=PPD, contrastID=4):
    _warnContrast(contrastID)
    _warnPPD(ppd)
        
    c = np.linspace(1e-05, 0.015, 5)[contrastID]
    edge = _create_edge(contrast=c, edgeWidth=0.95, stim_params=stim_params)
    n = "white"
    noise = _create_noise(n, stim_params)
    
    edge["edge"] = edge["img"]
    edge["noise"] = noise
    edge["img"] = edge["img"] + noise
    edge["noise_contrast"] = stim_params["noise_contrast"]
    edge["noise_type"] = n
    edge["experimental_data"] = df[(df.noise==n) & (df.edge==0.048)].reset_index(drop=True)
    return edge

def hsfEdge_pink(ppd=PPD, contrastID=4):
    _warnContrast(contrastID)
    _warnPPD(ppd)
        
    c = np.linspace(1e-05, 0.015, 5)[contrastID]
    edge = _create_edge(contrast=c, edgeWidth=0.95, stim_params=stim_params)
    n = "pink"
    noise = _create_noise(n, stim_params)
    
    edge["edge"] = edge["img"]
    edge["noise"] = noise
    edge["img"] = edge["img"] + noise
    edge["noise_contrast"] = stim_params["noise_contrast"]
    edge["noise_type"] = n
    edge["experimental_data"] = df[(df.noise==n) & (df.edge==0.048)].reset_index(drop=True)
    return edge

def hsfEdge_brown(ppd=PPD, contrastID=4):
    _warnContrast(contrastID)
    _warnPPD(ppd)
        
    c = np.linspace(1e-05, 0.004, 5)[contrastID]
    edge = _create_edge(contrast=c, edgeWidth=0.95, stim_params=stim_params)
    n = "brown"
    noise = _create_noise(n, stim_params)
    
    edge["edge"] = edge["img"]
    edge["noise"] = noise
    edge["img"] = edge["img"] + noise
    edge["noise_contrast"] = stim_params["noise_contrast"]
    edge["noise_type"] = n
    edge["experimental_data"] = df[(df.noise==n) & (df.edge==0.048)].reset_index(drop=True)
    return edge

def hsfEdge_NB05(ppd=PPD, contrastID=4):
    _warnContrast(contrastID)
    _warnPPD(ppd)
        
    c = np.linspace(1e-05, 0.005, 5)[contrastID]
    edge = _create_edge(contrast=c, edgeWidth=0.95, stim_params=stim_params)
    n = "NB05"
    noise = _create_noise(n, stim_params)
    
    edge["edge"] = edge["img"]
    edge["noise"] = noise
    edge["img"] = edge["img"] + noise
    edge["noise_contrast"] = stim_params["noise_contrast"]
    edge["noise_type"] = n
    edge["experimental_data"] = df[(df.noise==n) & (df.edge==0.048)].reset_index(drop=True)
    return edge

def hsfEdge_NB3(ppd=PPD, contrastID=4):
    _warnContrast(contrastID)
    _warnPPD(ppd)
        
    c = np.linspace(1e-05, 0.006, 5)[contrastID]
    edge = _create_edge(contrast=c, edgeWidth=0.95, stim_params=stim_params)
    n = "NB3"
    noise = _create_noise(n, stim_params)
    
    edge["edge"] = edge["img"]
    edge["noise"] = noise
    edge["img"] = edge["img"] + noise
    edge["noise_contrast"] = stim_params["noise_contrast"]
    edge["noise_type"] = n
    edge["experimental_data"] = df[(df.noise==n) & (df.edge==0.048)].reset_index(drop=True)
    return edge

def hsfEdge_NB9(ppd=PPD, contrastID=4):
    _warnContrast(contrastID)
    _warnPPD(ppd)
        
    c = np.linspace(1e-05, 0.015, 5)[contrastID]
    edge = _create_edge(contrast=c, edgeWidth=0.95, stim_params=stim_params)
    n = "NB9"
    noise = _create_noise(n, stim_params)
    
    edge["edge"] = edge["img"]
    edge["noise"] = noise
    edge["img"] = edge["img"] + noise
    edge["noise_contrast"] = stim_params["noise_contrast"]
    edge["noise_type"] = n
    edge["experimental_data"] = df[(df.noise==n) & (df.edge==0.048)].reset_index(drop=True)
    return edge


# %%
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


if __name__ == "__main__":
    from stimupy.utils import plot_stimuli

    stims = gen_all(skip=True)
    plot_stimuli(stims, mask=False, units="visual_size", vmin=0, vmax=200)
