"""Stimuli from Robinson, Hammon & de Sa (2007)
https://doi.org/10.1016/j.visres.2007.02.017

This module reproduces all of the stimuli used by Robinson,
Hammon & de Sa (2007) as they were provided to the model described
in that paper.

Each stimulus is provided by a separate function,
a full list can be found as stimuli.papers.RHS2007.__all__

The output of each of these functions is a stimulus dictionary.

For a visual representation of all the stimuli and their mask,
simply run this module as a script:

    $ python stimuli/papers/RHS2007.py

Attributes
----------
__all__ (list of str): list of all stimulus-functions
    that are exported by this module when executing
        >>> from stimuli.papers.domijan2015 import *

References
-----------
Robinson, A. E., Hammon, P. S., & de Sa, V. R. (2007). Explaining brightness
illusions using spatial filtering and local response normalization. Vision
research, 47(12), 1631-1644. https://doi.org/10.1016/j.visres.2007.02.017
"""

import numpy as np

from stimuli import illusions
from stimuli.utils import (
    pad_by_visual_size,
    pad_to_shape,
    pad_to_visual_size,
    resolution,
)

__all__ = [
    "WE_thick",
    "WE_thin_wide",
    "WE_dual",
    "WE_anderson",
    "WE_howe",
    "WE_zigzag",
    "WE_radial_thick_small",
    "WE_radial_thick",
    "WE_radial_thin_small",
    "WE_radial_thin",
    "WE_circular1",
    "WE_circular05",
    "WE_circular025",
    "grating_induction",
    "sbc_large",
    "sbc_small",
    "todorovic_equal",
    "todorovic_in_large",
    "todorovic_in_small",
    "todorovic_out",
    "checkerboard_016",
    "checkerboard_0938",
    "checkerboard209",
    "corrugated_mondrian",
    "benary_cross",
    "todorovic_benary1_2",
    "todorovic_benary3_4",
    "todorovic_benary1_2_3_4",
    "bullseye_thin",
    "bullseye_thick",
]

VISEXTENT = (32.0, 32.0)
PPD = 32
v1, v2, v3 = 0.0, 0.5, 1.0


def gen_all(ppd=PPD, pad=True, skip=False):
    stims = {}  # save the stimulus-dicts in a larger dict, with name as key
    for stim_name in __all__:
        print(f"Generating RHS2007.{stim_name}")

        # Get a reference to the actual function
        func = globals()[stim_name]
        try:
            stim = func(ppd=ppd, pad=pad)

            # Accumulate
            stims[stim_name] = stim
        except NotImplementedError as e:
            if not skip:
                raise e
            # Skip stimuli that aren't implemented
            print("-- not implemented")
            pass

    return stims


def WE_thick(ppd=PPD, pad=True):
    """White stimulus as shown in Robinson, Hammon, & de Sa (2007) Fig 1a.
    Grating size: 12x16 deg
    Grating frequency: 0.25 cpd
    Target size: 4x2 deg

    Parameters
    ----------
    ppd : int
        Resolution of stimulus in pixels per degree. (default: 32)
    pad : bool
        If True, include padding to 32x32 deg (default: True)

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "mask")
        and additional keys containing stimulus parameters

    References
    -----------
    Blakeslee, B., & McCourt, M. E. (1999). A multiscale spatial ﬁltering account of the
        White eﬀect, simultaneous brightness contrast and grating induction. Vision
        Research, 39, 4361–4377.
    White, M. (1979). A new eﬀect of pattern on perceived lightness. Perception, 8, 413–416.
    """

    height, width = 12.0, 16.0
    params = {
        "ppd": ppd,
        "grating_frequency": 4.0 / width,
        "intensity_bars": (v1, v3),
        "intensity_target": v2,
        "target_indices": (2, 5),
        "target_size": 4.0,
        "period": "full",
    }

    stim = illusions.whites.white(
        visual_size=(height, width),
        **params,
    )

    if pad:
        stim["img"] = pad_to_visual_size(stim["img"], VISEXTENT, ppd, pad_value=v2)
        stim["mask"] = pad_to_visual_size(stim["mask"], VISEXTENT, ppd, pad_value=0)

    params.update(
        visual_size=np.array(stim["img"].shape) / ppd,
        shape=stim["img"].shape,
        intensity_range=(v1, v3),
    )
    return {**stim, **params}


def WE_thin_wide(ppd=PPD, pad=True):
    """White stimulus as shown in Robinson, Hammon, & de Sa (2007) Fig 1b.
    Grating size: 12x16 deg
    Grating frequency: 0.5 cpd
    Target size: 2x1 deg

    Parameters
    ----------
    ppd : int
        Resolution of stimulus in pixels per degree. (default: 32)
    pad : bool
        If True, include padding to 32x32 deg (default: True)

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "mask")
        and additional keys containing stimulus parameters

    References
    -----------
    Blakeslee, B., & McCourt, M. E. (1999). A multiscale spatial ﬁltering account of the
        White eﬀect, simultaneous brightness contrast and grating induction. Vision
        Research, 39, 4361–4377.
    White, M. (1979). A new eﬀect of pattern on perceived lightness. Perception, 8, 413–416.
    """

    height, width = 12.0, 16.0
    params = {
        "ppd": ppd,
        "grating_frequency": 8.0 / width,
        "intensity_bars": (v3, v1),
        "intensity_target": v2,
        "target_indices": (3, 12),
        "target_size": 2.0,
        "period": "full",
    }

    stim = illusions.whites.white(
        visual_size=(height, width),
        **params,
    )

    if pad:
        stim["img"] = pad_to_visual_size(stim["img"], VISEXTENT, ppd, pad_value=v2)
        stim["mask"] = pad_to_visual_size(stim["mask"], VISEXTENT, ppd, pad_value=0)

    params.update(
        visual_size=np.array(stim["img"].shape) / ppd,
        shape=stim["img"].shape,
        intensity_range=(v1, v3),
    )
    return {**stim, **params}


def WE_dual(ppd=PPD, pad=True):
    """Dual White stimulus as shown in Robinson, Hammon, & de Sa (2007) Fig 1c.
    Grating sizes: 6x8 deg
    Grating frequency: 0.5 cpd
    Target size: 2x1 deg

    Parameters
    ----------
    ppd : int
        Resolution of stimulus in pixels per degree. (default: 32)
    pad : bool
        If True, include padding to 32x32 deg (default: True)

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "mask")
        and additional keys containing stimulus parameters
    """

    height, width = 6.0, 8.0
    params = {
        "ppd": ppd,
        "grating_frequency": 4.0 / width,
        "intensity_bars": (v1, v3),
        "intensity_target": v2,
        "target_indices": (2, 5),
        "target_size": 2.0,
        "period": "full",
    }

    stim1 = illusions.whites.white(
        visual_size=(height, width),
        **params,
    )

    stim2 = illusions.whites.white(
        visual_size=(height, width),
        **params,
    )
    stim2["img"] = np.rot90(stim2["img"], 3)
    stim2["mask"] = np.rot90(stim2["mask"], 3)

    if pad:
        shape = np.array(resolution.shape_from_visual_size_ppd(VISEXTENT, ppd)) / (1, 2)
    else:
        shape = np.max([stim1["img"].shape, stim2["img"].shape], axis=1)
    stim1["img"] = pad_to_shape(stim1["img"], shape, pad_value=v2)
    stim1["mask"] = pad_to_shape(stim1["mask"], shape, pad_value=0)
    stim2["img"] = pad_to_shape(stim2["img"], shape, pad_value=v2)
    stim2["mask"] = pad_to_shape(stim2["mask"], shape, pad_value=0)

    stim = {
        "img": np.hstack((stim1["img"], stim2["img"])),
        "mask": np.hstack((stim1["mask"], stim2["mask"])),
    }

    params.update(
        visual_size=np.array(stim["img"].shape) / ppd,
        shape=stim["img"].shape,
        intensity_range=(v1, v3),
    )
    return {**stim, **params}


def WE_anderson(ppd=PPD, pad=True):
    """Anderson variation of White stimulus as shown in Robinson, Hammon, & de Sa (2007) Fig 1d.
    Grating size: 16x16 deg
    Grating frequency: 0.5 cpd
    Target size: 3.2x1 deg

    Parameters
    ----------
    ppd : int
        Resolution of stimulus in pixels per degree. (default: 32)
    pad : bool
        If True, include padding to 32x32 deg (default: True)

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "mask")
        and additional keys containing stimulus parameters

    References
    -----------
    Anderson, B. L. (2001). Contrasting theories of White’s illusion. Perception, 30, 1499–1501
    Blakeslee, B., Pasieka, W., & McCourt, M. E. (2005). Oriented multiscale spatial ﬁltering
        and contrast normalization: a parsimonious model of brightness induction in a continuum
        of stimuli including White, Howe and simultaneous brightness contrast. Vision Research,
        45, 607–615.
    """

    height, width = 16.0, 16.0
    params = {
        "ppd": ppd,
        "grating_frequency": 8.0 / width,
        "intensity_bars": (v1, v3),
        "intensity_target": v2,
        "target_indices_top": (5,),
        "target_indices_bottom": (10,),
        "target_center_offset": height / 10.0,
        "target_size": height / 5.0,
        "intensity_stripes": (v1, v3),
        "stripe_center_offset": height / 5.0,
        "stripe_size": height / 5.0,
        "period": "full",
    }

    stim = illusions.whites.white_anderson(
        visual_size=(height, width),
        **params,
    )

    if pad:
        stim["img"] = pad_to_visual_size(stim["img"], VISEXTENT, ppd, pad_value=v2)
        stim["mask"] = pad_to_visual_size(stim["mask"], VISEXTENT, ppd, pad_value=0)

    params.update(
        visual_size=np.array(stim["img"].shape) / ppd,
        shape=stim["img"].shape,
        intensity_range=(v1, v3),
    )
    return {**stim, **params}


def WE_howe(ppd=PPD, pad=True):
    """Howe variation of White stimulus as shown in Robinson, Hammon, & de Sa (2007) Fig 1e.
    Grating size: 16x16 deg
    Grating frequency: 0.5 cpd
    Target size: 3.2x1 deg

    Parameters
    ----------
    ppd : int
        Resolution of stimulus in pixels per degree. (default: 32)
    pad : bool
        If True, include padding to 32x32 deg (default: True)

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "mask")
        and additional keys containing stimulus parameters

    References
    -----------
    Blakeslee, B., Pasieka, W., & McCourt, M. E. (2005). Oriented multiscale spatial ﬁltering
        and contrast normalization: a parsimonious model of brightness induction in a continuum
        of stimuli including White, Howe and simultaneous brightness contrast. Vision Research,
        45, 607–615.
    Howe, P. D. L. (2001). A comment on the Anderson (1997), the Todorovic (1997), and the Ross
        and Pessoa (2000) explanations of White’s eﬀect. Perception, 30, 1023–1026
    """

    height, width = 16.0, 16.0
    params = {
        "ppd": ppd,
        "grating_frequency": 8.0 / width,
        "intensity_bars": (v1, v3),
        "intensity_target": v2,
        "target_indices_top": (5,),
        "target_indices_bottom": (10,),
        "target_center_offset": height / 5.0,
        "target_size": height / 5.0,
        "intensity_stripes": (v1, v3),
        "period": "full",
    }

    stim = illusions.whites.white_howe(
        visual_size=(height, width),
        **params,
    )

    if pad:
        stim["img"] = pad_to_visual_size(stim["img"], VISEXTENT, ppd, pad_value=v2)
        stim["mask"] = pad_to_visual_size(stim["mask"], VISEXTENT, ppd, pad_value=0)

    params.update(
        visual_size=np.array(stim["img"].shape) / ppd,
        shape=stim["img"].shape,
        intensity_range=(v1, v3),
    )
    return {**stim, **params}


def WE_zigzag(ppd=PPD, pad=True):
    """Wedding cake stimulus as shown in Robinson, Hammon, & de Sa (2007) Fig 1f.

    Parameters
    ----------
    ppd : int
        Resolution of stimulus in pixels per degree. (default: 32)
    pad : bool
        If True, include padding to 32x32 deg (default: True)

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "mask")
        and additional keys containing stimulus parameters

    References
    -----------
    Cliﬀord, C. W. G., & Spehar, B. (2003). Using colour to disambiguate contrast and
        assimilation in White’s eﬀect. Journal of Vision, 3, 294a.
    """

    i1, i2 = -1, 0
    stim = illusions.wedding_cake.wedding_cake_stimulus(
        ppd=PPD,
        L_size=(4.0, 5, 1.0),
        L_repeats=(3.5, 3.4),
        target_height=2.0,
        target_idx_intensity1=((i1, -1), (i1, -0), (i1, 1), (i1, 2)),
        target_idx_intensity2=((i2, -1), (i2, -0), (i2, 1), (i2, -2)),
        intensity1=0.0,
        intensity2=1.0,
        intensity_target=0.5,
    )

    if pad:
        stim["img"] = pad_to_visual_size(stim["img"], VISEXTENT, ppd, pad_value=0.5)
        stim["mask"] = pad_to_visual_size(stim["mask"], VISEXTENT, ppd, pad_value=0)

    return stim


def WE_radial_thick_small(ppd=PPD, pad=True):
    """Radial White stimulus as shown in Robinson, Hammon, & de Sa (2007) Fig 1g.
    Circle size: 16x16 deg
    Number of segments: 14
    Target length: 4 deg

    Parameters
    ----------
    ppd : int
        Resolution of stimulus in pixels per degree. (default: 32)
    pad : bool
        If True, include padding to 32x32 deg (default: True)

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "mask")
        and additional keys containing stimulus parameters

    References
    -----------
    Anstis, S. (2003). White’s eﬀect in brightness & color. Online Demonstration
    """

    n_cycles = 7
    params = {
        "ppd": ppd,
        "n_segments": n_cycles * 2,
        "rotate": np.pi / n_cycles / 2,
        "target_indices": (0, n_cycles),
        "target_width": 4.0,
        "target_center": 4.5,
        "intensity_slices": (v3, v1),
        "intensity_background": v2,
        "intensity_target": v2,
    }

    stim = illusions.circular.radial_white(
        visual_size=(16, 16),
        **params,
    )

    if pad:
        stim["img"] = pad_to_visual_size(stim["img"], VISEXTENT, ppd, pad_value=v2)
        stim["mask"] = pad_to_visual_size(stim["mask"], VISEXTENT, ppd, pad_value=0)

    params.update(
        visual_size=np.array(stim["img"].shape) / ppd,
        shape=stim["img"].shape,
        intensity_range=(v1, v3),
    )
    return {**stim, **params}


def WE_radial_thick(ppd=PPD, pad=True):
    """Radial White stimulus as shown in Robinson, Hammon, & de Sa (2007) Fig 1h.
    Circle size: 24x24 deg
    Number of segments: 18
    Target length: 4 deg

    Parameters
    ----------
    ppd : int
        Resolution of stimulus in pixels per degree. (default: 32)
    pad : bool
        If True, include padding to 32x32 deg (default: True)

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "mask")
        and additional keys containing stimulus parameters

    References
    -----------
    Anstis, S. (2003). White’s eﬀect in brightness & color. Online Demonstration
    """

    n_cycles = 9
    params = {
        "ppd": ppd,
        "n_segments": n_cycles * 2,
        "rotate": np.pi / n_cycles / 2,
        "target_indices": (0, n_cycles),
        "target_width": 4.0,
        "target_center": 6.0,
        "intensity_slices": (v3, v1),
        "intensity_background": v2,
        "intensity_target": v2,
    }

    stim = illusions.circular.radial_white(
        visual_size=(24, 24),
        **params,
    )

    if pad:
        stim["img"] = pad_to_visual_size(stim["img"], VISEXTENT, ppd, pad_value=v2)
        stim["mask"] = pad_to_visual_size(stim["mask"], VISEXTENT, ppd, pad_value=0)

    params.update(
        visual_size=np.array(stim["img"].shape) / ppd,
        shape=stim["img"].shape,
        intensity_range=(v1, v3),
    )
    return {**stim, **params}


def WE_radial_thin_small(ppd=PPD, pad=True):
    """Radial White stimulus as shown in Robinson, Hammon, & de Sa (2007) Fig 1i.
    Circle size: 16x16 deg
    Number of segments: 26
    Target length: 2 deg

    Parameters
    ----------
    ppd : int
        Resolution of stimulus in pixels per degree. (default: 32)
    pad : bool
        If True, include padding to 32x32 deg (default: True)

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "mask")
        and additional keys containing stimulus parameters

    References
    -----------
    Anstis, S. (2003). White’s eﬀect in brightness & color. Online Demonstration
    """

    n_cycles = 13
    params = {
        "ppd": ppd,
        "n_segments": n_cycles * 2,
        "rotate": np.pi / n_cycles / 2,
        "target_indices": (0, n_cycles),
        "target_width": 2.0,
        "target_center": 4.0,
        "intensity_slices": (v3, v1),
        "intensity_background": v2,
        "intensity_target": v2,
    }

    stim = illusions.circular.radial_white(
        visual_size=(16, 16),
        **params,
    )

    if pad:
        stim["img"] = pad_to_visual_size(stim["img"], VISEXTENT, ppd, pad_value=v2)
        stim["mask"] = pad_to_visual_size(stim["mask"], VISEXTENT, ppd, pad_value=0)

    params.update(
        visual_size=np.array(stim["img"].shape) / ppd,
        shape=stim["img"].shape,
        intensity_range=(v1, v3),
    )
    return {**stim, **params}


def WE_radial_thin(ppd=PPD, pad=True):
    """Radial White stimulus as shown in Robinson, Hammon, & de Sa (2007) Fig 1j.
    Circle size: 24x24 deg
    Number of segments: 42
    Target length: 2 deg

    Parameters
    ----------
    ppd : int
        Resolution of stimulus in pixels per degree. (default: 32)
    pad : bool
        If True, include padding to 32x32 deg (default: True)

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "mask")
        and additional keys containing stimulus parameters

    References
    -----------
    Anstis, S. (2003). White’s eﬀect in brightness & color. Online Demonstration
    """

    n_cycles = 21
    params = {
        "ppd": ppd,
        "n_segments": n_cycles * 2,
        "rotate": np.pi / n_cycles / 2,
        "target_indices": (0, n_cycles),
        "target_width": 2.0,
        "target_center": 6.0,
        "intensity_slices": (v3, v1),
        "intensity_background": v2,
        "intensity_target": v2,
    }

    stim = illusions.circular.radial_white(
        visual_size=(24, 24),
        **params,
    )

    if pad:
        stim["img"] = pad_to_visual_size(stim["img"], VISEXTENT, ppd, pad_value=v2)
        stim["mask"] = pad_to_visual_size(stim["mask"], VISEXTENT, ppd, pad_value=0)

    params.update(
        visual_size=np.array(stim["img"].shape) / ppd,
        shape=stim["img"].shape,
        intensity_range=(v1, v3),
    )
    return {**stim, **params}


def WE_circular1(ppd=PPD, pad=True):
    """Ring (or circular White) stimulus as shown in Robinson, Hammon, & de Sa (2007) Fig 1k.
    Circle size: 16x16 deg
    Ring frequency: 0.5 cpd
    Ring width: 1 deg

    Parameters
    ----------
    ppd : int
        Resolution of stimulus in pixels per degree. (default: 32)
    pad : bool
        If True, include padding to 32x32 deg (default: True)

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "mask")
        and additional keys containing stimulus parameters

    References
    -----------
    Howe, P. D. L. (2005). White’s eﬀect: removing the junctions but preserving the strength
        of the illusion. Perception, 34, 557–564.
    """

    height, width = 16.0, 16.0
    params = {
        "ppd": ppd,
        "frequency": 8.0 / height,
        "target_indices": 4,
        "intensity_background": v2,
        "intensity_target": v2,
        "supersampling": 1,
    }

    stim1 = illusions.circular.circular_white(
        visual_size=(height, width),
        intensity_rings=(v3, v1),
        **params,
    )

    stim2 = illusions.circular.circular_white(
        visual_size=(height, width),
        intensity_rings=(v1, v3),
        **params,
    )
    stim2["mask"] *= 2

    stim = {
        "img": np.hstack((stim1["img"], stim2["img"])),
        "mask": np.hstack((stim1["mask"], stim2["mask"])),
    }

    if pad:
        stim["img"] = pad_to_visual_size(stim["img"], VISEXTENT, ppd, pad_value=v2)
        stim["mask"] = pad_to_visual_size(stim["mask"], VISEXTENT, ppd, pad_value=0)

    params.update(
        visual_size=np.array(stim["img"].shape) / ppd,
        shape=stim["img"].shape,
        intensity_range=(v1, v3),
    )
    return {**stim, **params}


def WE_circular05(ppd=PPD, pad=True):
    """Ring (or circular White) stimulus as shown in Robinson, Hammon, & de Sa (2007) Fig 1l.
    Circle size: 16x16 deg
    Ring frequency: 1 cpd
    Ring width: 0.5 deg

    Parameters
    ----------
    ppd : int
        Resolution of stimulus in pixels per degree. (default: 32)
    pad : bool
        If True, include padding to 32x32 deg (default: True)

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "mask")
        and additional keys containing stimulus parameters

    References
    -----------
    Howe, P. D. L. (2005). White’s eﬀect: removing the junctions but preserving the strength
        of the illusion. Perception, 34, 557–564.
    """

    height, width = 16.0, 16.0
    params = {
        "ppd": ppd,
        "frequency": 16.0 / height,
        "target_indices": 10,
        "intensity_background": v2,
        "intensity_target": v2,
        "supersampling": 1,
    }

    stim1 = illusions.circular.circular_white(
        visual_size=(height, width),
        intensity_rings=(v3, v1),
        **params,
    )

    stim2 = illusions.circular.circular_white(
        visual_size=(height, width),
        intensity_rings=(v1, v3),
        **params,
    )
    stim2["mask"] *= 2

    stim = {
        "img": np.hstack((stim1["img"], stim2["img"])),
        "mask": np.hstack((stim1["mask"], stim2["mask"])),
    }

    if pad:
        stim["img"] = pad_to_visual_size(stim["img"], VISEXTENT, ppd, pad_value=v2)
        stim["mask"] = pad_to_visual_size(stim["mask"], VISEXTENT, ppd, pad_value=0)

    params.update(
        visual_size=np.array(stim["img"].shape) / ppd,
        shape=stim["img"].shape,
        intensity_range=(v1, v3),
    )
    return {**stim, **params}


def WE_circular025(ppd=PPD, pad=True):
    """Ring (or circular White) stimulus as shown in Robinson, Hammon, & de Sa (2007) Fig 1m.
    Circle size: 16x16 deg
    Ring frequency: 2 cpd
    Ring width: 0.25 deg

    Parameters
    ----------
    ppd : int
        Resolution of stimulus in pixels per degree. (default: 32)
    pad : bool
        If True, include padding to 32x32 deg (default: True)

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "mask")
        and additional keys containing stimulus parameters

    References
    -----------
    Howe, P. D. L. (2005). White’s eﬀect: removing the junctions but preserving the strength
        of the illusion. Perception, 34, 557–564.
    """

    height, width = 16.0, 16.0
    params = {
        "ppd": ppd,
        "frequency": 32.0 / height,
        "target_indices": 22,
        "intensity_background": v2,
        "intensity_target": v2,
        "supersampling": 1,
    }

    stim1 = illusions.circular.circular_white(
        visual_size=(height, width),
        intensity_rings=(v3, v1),
        **params,
    )

    stim2 = illusions.circular.circular_white(
        visual_size=(height, width),
        intensity_rings=(v1, v3),
        **params,
    )
    stim2["mask"] *= 2

    stim = {
        "img": np.hstack((stim1["img"], stim2["img"])),
        "mask": np.hstack((stim1["mask"], stim2["mask"])),
    }

    if pad:
        stim["img"] = pad_to_visual_size(stim["img"], VISEXTENT, ppd, pad_value=v2)
        stim["mask"] = pad_to_visual_size(stim["mask"], VISEXTENT, ppd, pad_value=0)

    params.update(
        visual_size=np.array(stim["img"].shape) / ppd,
        shape=stim["img"].shape,
        intensity_range=(v1, v3),
    )
    return {**stim, **params}


def grating_induction(ppd=PPD, pad=True):
    """Grating induction as shown in Robinson, Hammon, & de Sa (2007) Fig 1n.
    Circle size: 12x16 deg
    Grating frequency: 0.25 cpd
    Target size: 1x16 deg

    Parameters
    ----------
    ppd : int
        Resolution of stimulus in pixels per degree. (default: 32)
    pad : bool
        If True, include padding to 32x32 deg (default: True)

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "mask")
        and additional keys containing stimulus parameters

    References
    -----------
    Blakeslee, B., & McCourt, M. E. (1999). A multiscale spatial ﬁltering account of the
        White eﬀect, simultaneous brightness contrast and grating induction. Vision
        Research, 39, 4361–4377.
    McCourt, M. E. (1982). A spatial frequency dependent grating-induction effect. Vision
        Research, 22, 119–134.
    """

    height, width = 12.0, 16.0
    params = {
        "ppd": ppd,
        "frequency": 4.0 / width,
        "target_height": 1.0,
        "blur": 10,
        "start": "high",
    }

    stim = illusions.grating_induction.grating_illusion(
        shape=(height, width),
        **params,
    )

    if pad:
        stim["img"] = pad_to_visual_size(stim["img"], VISEXTENT, ppd, pad_value=v2)
        stim["mask"] = pad_to_visual_size(stim["mask"], VISEXTENT, ppd, pad_value=0)

    params.update(
        visual_size=np.array(stim["img"].shape) / ppd,
        shape=stim["img"].shape,
        intensity_range=(v1, v3),
    )
    return {**stim, **params}


def sbc_large(ppd=PPD, pad=True):
    """Simultaneous brightness contrast as shown in Robinson, Hammon, & de Sa (2007) Fig 1o.
    Stimulus size: 13x31 deg
    Target sizes: 3x3 deg

    Parameters
    ----------
    ppd : int
        Resolution of stimulus in pixels per degree. (default: 32)
    pad : bool
        If True, include padding to 32x32 deg (default: True)

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "mask")
        and additional keys containing stimulus parameters

    References
    -----------
    Blakeslee, B., & McCourt, M. E. (1999). A multiscale spatial ﬁltering account of the
        White eﬀect, simultaneous brightness contrast and grating induction. Vision
        Research, 39, 4361–4377.
    """

    params = {
        "ppd": ppd,
        "target_size": 3.0,
        "intensity_target": v2,
    }

    stim1 = illusions.sbc.simultaneous_contrast(
        visual_size=(13.0, 15.5),
        intensity_background=0.0,
        **params,
    )
    stim2 = illusions.sbc.simultaneous_contrast(
        visual_size=(13.0, 15.5),
        intensity_background=1.0,
        **params,
    )
    mask2 = stim2["mask"] + 1
    mask2[mask2 == 1] = 0

    stim = {
        "img": np.hstack((stim1["img"], stim2["img"])),
        "mask": np.hstack((stim1["mask"], mask2)),
    }

    if pad:
        stim["img"] = pad_to_visual_size(stim["img"], VISEXTENT, ppd, pad_value=v2)
        stim["mask"] = pad_to_visual_size(stim["mask"], VISEXTENT, ppd, pad_value=0)

    params.update(
        visual_size=np.array(stim["img"].shape) / ppd,
        shape=stim["img"].shape,
        intensity_range=(v1, v3),
    )
    return {**stim, **params}


def sbc_small(ppd=PPD, pad=True):
    """Simultaneous brightness contrast as shown in Robinson, Hammon, & de Sa (2007) Fig 1p.
    Stimulus size: 13x31 deg
    Target sizes: 1x1 deg

    Parameters
    ----------
    ppd : int
        Resolution of stimulus in pixels per degree. (default: 32)
    pad : bool
        If True, include padding to 32x32 deg (default: True)

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "mask")
        and additional keys containing stimulus parameters

    References
    -----------
    Blakeslee, B., & McCourt, M. E. (1999). A multiscale spatial ﬁltering account of the
        White eﬀect, simultaneous brightness contrast and grating induction. Vision
        Research, 39, 4361–4377.
    """

    params = {
        "ppd": ppd,
        "target_size": 1.0,
        "intensity_target": v2,
    }

    stim1 = illusions.sbc.simultaneous_contrast(
        visual_size=(13.0, 15.5),
        intensity_background=0.0,
        **params,
    )
    stim2 = illusions.sbc.simultaneous_contrast(
        visual_size=(13.0, 15.5),
        intensity_background=1.0,
        **params,
    )
    mask2 = stim2["mask"] + 1
    mask2[mask2 == 1] = 0

    stim = {
        "img": np.hstack((stim1["img"], stim2["img"])),
        "mask": np.hstack((stim1["mask"], mask2)),
    }

    if pad:
        stim["img"] = pad_to_visual_size(stim["img"], VISEXTENT, ppd, pad_value=v2)
        stim["mask"] = pad_to_visual_size(stim["mask"], VISEXTENT, ppd, pad_value=0)

    params.update(
        visual_size=np.array(stim["img"].shape) / ppd,
        shape=stim["img"].shape,
        intensity_range=(v1, v3),
    )
    return {**stim, **params}


def todorovic_equal(ppd=PPD, pad=True):
    """Todorovic stimulus - equal as shown in Robinson, Hammon, & de Sa (2007) Fig 1q.
    Stimulus size: 13x31 deg
    Target size: 8x8 deg

    Parameters
    ----------
    ppd : int
        Resolution of stimulus in pixels per degree. (default: 32)
    pad : bool
        If True, include padding to 32x32 deg (default: True)

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "mask")
        and additional keys containing stimulus parameters

    References
    -----------
    Blakeslee, B., & McCourt, M. E. (1999). A multiscale spatial ﬁltering account of the
        White eﬀect, simultaneous brightness contrast and grating induction. Vision
        Research, 39, 4361–4377.
    Pessoa, L., Baratoff, G., Neumann, H., & Todorovic, D. (1998). Lightness and junctions:
        variations on White’s display. Investigative Ophthalmology and Visual Science
        (Supplement), 39, S159.
    """

    params = {
        "ppd": ppd,
        "target_arms_size": 3.2,
        "target_thickness": 1.6,
        "covers_size": 3.2,
        "intensity_target": v2,
    }

    stim1 = illusions.todorovic.todorovic_cross(
        visual_size=(13.0, 15.5),
        intensity_background=1.0,
        intensity_covers=0.0,
        **params,
    )
    stim2 = illusions.todorovic.todorovic_cross(
        visual_size=(13.0, 15.5),
        intensity_background=0.0,
        intensity_covers=1.0,
        **params,
    )
    mask2 = stim2["mask"] + 1
    mask2[mask2 == 1] = 0

    stim = {
        "img": np.hstack((stim1["img"], stim2["img"])),
        "mask": np.hstack((stim1["mask"], mask2)),
    }

    if pad:
        stim["img"] = pad_to_visual_size(stim["img"], VISEXTENT, ppd, pad_value=v2)
        stim["mask"] = pad_to_visual_size(stim["mask"], VISEXTENT, ppd, pad_value=0)

    params.update(
        visual_size=np.array(stim["img"].shape) / ppd,
        shape=stim["img"].shape,
        intensity_range=(v1, v3),
    )
    return {**stim, **params}


def todorovic_in_large(ppd=PPD, pad=True):
    """Todorovic stimulus - in as shown in Robinson, Hammon, & de Sa (2007) Fig 1r.
    Stimulus size: 13x31 deg
    Target size: 5.3x5.3 deg

    Parameters
    ----------
    ppd : int
        Resolution of stimulus in pixels per degree. (default: 32)
    pad : bool
        If True, include padding to 32x32 deg (default: True)

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "mask")
        and additional keys containing stimulus parameters

    References
    -----------
    Blakeslee, B., & McCourt, M. E. (1999). A multiscale spatial ﬁltering account of the
        White eﬀect, simultaneous brightness contrast and grating induction. Vision
        Research, 39, 4361–4377.
    Todorovic, D. (1997). Lightness and junctions. Perception, 26, 379–395.
    """

    params = {
        "ppd": ppd,
        "target_size": 5.3,
        "covers_size": 3.2,
        "covers_offset": 2.4,
        "intensity_target": v2,
    }

    stim1 = illusions.todorovic.todorovic_rectangle(
        visual_size=(13.0, 15.5),
        intensity_background=1.0,
        intensity_covers=0.0,
        **params,
    )
    stim2 = illusions.todorovic.todorovic_rectangle(
        visual_size=(13.0, 15.5),
        intensity_background=0.0,
        intensity_covers=1.0,
        **params,
    )
    mask2 = stim2["mask"] + 1
    mask2[mask2 == 1] = 0

    stim = {
        "img": np.hstack((stim1["img"], stim2["img"])),
        "mask": np.hstack((stim1["mask"], mask2)),
    }

    if pad:
        stim["img"] = pad_to_visual_size(stim["img"], VISEXTENT, ppd, pad_value=v2)
        stim["mask"] = pad_to_visual_size(stim["mask"], VISEXTENT, ppd, pad_value=0)

    params.update(
        visual_size=np.array(stim["img"].shape) / ppd,
        shape=stim["img"].shape,
        intensity_range=(v1, v3),
    )
    return {**stim, **params}


def todorovic_in_small(ppd=PPD, pad=True):
    """Todorovic stimulus - in as shown in Robinson, Hammon, & de Sa (2007) Fig 1s.
    Stimulus size: 13x31 deg
    Target size: 3x3 deg

    Parameters
    ----------
    ppd : int
        Resolution of stimulus in pixels per degree. (default: 32)
    pad : bool
        If True, include padding to 32x32 deg (default: True)

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "mask")
        and additional keys containing stimulus parameters

    References
    -----------
    Blakeslee, B., & McCourt, M. E. (1999). A multiscale spatial ﬁltering account of the
        White eﬀect, simultaneous brightness contrast and grating induction. Vision
        Research, 39, 4361–4377.
    Todorovic, D. (1997). Lightness and junctions. Perception, 26, 379–395.
    """

    params = {
        "ppd": ppd,
        "target_arms_size": 0.7,
        "target_thickness": 1.6,
        "covers_size": 3.2,
        "intensity_target": v2,
    }

    stim1 = illusions.todorovic.todorovic_cross(
        visual_size=(13.0, 15.5),
        intensity_background=1.0,
        intensity_covers=0.0,
        **params,
    )
    stim2 = illusions.todorovic.todorovic_cross(
        visual_size=(13.0, 15.5),
        intensity_background=0.0,
        intensity_covers=1.0,
        **params,
    )
    mask2 = stim2["mask"] + 1
    mask2[mask2 == 1] = 0

    stim = {
        "img": np.hstack((stim1["img"], stim2["img"])),
        "mask": np.hstack((stim1["mask"], mask2)),
    }

    if pad:
        stim["img"] = pad_to_visual_size(stim["img"], VISEXTENT, ppd, pad_value=v2)
        stim["mask"] = pad_to_visual_size(stim["mask"], VISEXTENT, ppd, pad_value=0)

    params.update(
        visual_size=np.array(stim["img"].shape) / ppd,
        shape=stim["img"].shape,
        intensity_range=(v1, v3),
    )
    return {**stim, **params}


def todorovic_out(ppd=PPD, pad=True):
    """Todorovic stimulus - out as shown in Robinson, Hammon, & de Sa (2007) Fig 1t.
    Stimulus size: 13x31 deg
    Target size: 9.4x9.4 deg (note: in RHS2007, it says 8.7x8.7 deg, however that does not
                              match with Fig 1t)

    Parameters
    ----------
    ppd : int
        Resolution of stimulus in pixels per degree. (default: 32)
    pad : bool
        If True, include padding to 32x32 deg (default: True)

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "mask")
        and additional keys containing stimulus parameters

    References
    -----------
    Blakeslee, B., & McCourt, M. E. (1999). A multiscale spatial ﬁltering account of the
        White eﬀect, simultaneous brightness contrast and grating induction. Vision
        Research, 39, 4361–4377.
    Pessoa, L., Baratoff, G., Neumann, H., & Todorovic, D. (1998). Lightness and junctions:
        variations on White’s display. Investigative Ophthalmology and Visual Science
        (Supplement), 39, S159.
    """

    params = {
        "ppd": ppd,
        "target_arms_size": 3.9,
        "target_thickness": 1.6,
        "covers_size": 3.2,
        "intensity_target": v2,
    }

    stim1 = illusions.todorovic.todorovic_cross(
        visual_size=(13.0, 15.5),
        intensity_background=1.0,
        intensity_covers=0.0,
        **params,
    )
    stim2 = illusions.todorovic.todorovic_cross(
        visual_size=(13.0, 15.5),
        intensity_background=0.0,
        intensity_covers=1.0,
        **params,
    )
    mask2 = stim2["mask"] + 1
    mask2[mask2 == 1] = 0

    stim = {
        "img": np.hstack((stim1["img"], stim2["img"])),
        "mask": np.hstack((stim1["mask"], mask2)),
    }

    if pad:
        stim["img"] = pad_to_visual_size(stim["img"], VISEXTENT, ppd, pad_value=v2)
        stim["mask"] = pad_to_visual_size(stim["mask"], VISEXTENT, ppd, pad_value=0)

    params.update(
        visual_size=np.array(stim["img"].shape) / ppd,
        shape=stim["img"].shape,
        intensity_range=(v1, v3),
    )
    return {**stim, **params}


def checkerboard_016(ppd=PPD, pad=True):
    """Checkerboard stimulus as shown in Robinson, Hammon, & de Sa (2007) Fig 1u.
    Stimulus size: 6.25x15.9375 deg
    Target size: 0.156x0.156 deg

    Parameters
    ----------
    ppd : int
        Resolution of stimulus in pixels per degree. (default: 32)
    pad : bool
        If True, include padding to 32x32 deg (default: True)

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "mask")
        and additional keys containing stimulus parameters

    References
    -----------
    Blakeslee, B., & McCourt, M. E. (2004). A uniﬁed theory of brightness contrast and
        assimilation incorporating oriented multi-scale spatial ﬁltering and contrast
        normalization. Vision Research, 44, 2483–2503.
    DeValois, R. L., & DeValois, K. K. (1988). Spatial vision. New York: Oxford University Press.
    """

    nchecks_height, nchecks_width = 40, 102
    target_row = nchecks_height // 2
    params = {
        "ppd": ppd,
        "board_shape": (nchecks_height, nchecks_width),
        "check_visual_size": (5 / 32, 5 / 32),
        "targets": ((target_row, 16), (target_row, 85)),
        "extend_targets": False,
        "intensity_low": v3,
        "intensity_high": v1,
        "intensity_target": v2,
    }
    stim = illusions.checkerboards.checkerboard(**params)

    if pad:
        stim["img"] = pad_to_visual_size(stim["img"], VISEXTENT, ppd, pad_value=v2)
        stim["mask"] = pad_to_visual_size(stim["mask"], VISEXTENT, ppd, pad_value=0)

    params.update(
        visual_size=np.array(stim["img"].shape) / ppd,
        shape=stim["img"].shape,
        intensity_range=(v1, v3),
    )
    return {**stim, **params}


def checkerboard_0938(ppd=PPD, pad=True):
    """Checkerboard stimulus as shown in Robinson, Hammon, & de Sa (2007) Fig 1v.
    Stimulus size: 6.5625x23.4375 deg
    Target size: 0.938x0.938 deg

    Parameters
    ----------
    ppd : int
        Resolution of stimulus in pixels per degree. (default: 32)
    pad : bool
        If True, include padding to 32x32 deg (default: True)

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "mask")
        and additional keys containing stimulus parameters

    References
    -----------
    Blakeslee, B., & McCourt, M. E. (2004). A uniﬁed theory of brightness contrast and
        assimilation incorporating oriented multi-scale spatial ﬁltering and contrast
        normalization. Vision Research, 44, 2483–2503.
    DeValois, R. L., & DeValois, K. K. (1988). Spatial vision. New York: Oxford University Press.
    """

    nchecks_height, nchecks_width = 7, 25
    target_row = nchecks_height // 2
    params = {
        "ppd": ppd,
        "board_shape": (nchecks_height, nchecks_width),
        "check_visual_size": (30 / 32, 30 / 32),
        "targets": ((target_row, 6), (target_row, 17)),
        "extend_targets": False,
        "intensity_low": v1,
        "intensity_high": v3,
        "intensity_target": v2,
    }
    stim = illusions.checkerboards.checkerboard(**params)

    if pad:
        stim["img"] = pad_to_visual_size(stim["img"], VISEXTENT, ppd, pad_value=v2)
        stim["mask"] = pad_to_visual_size(stim["mask"], VISEXTENT, ppd, pad_value=0)

    params.update(
        visual_size=np.array(stim["img"].shape) / ppd,
        shape=stim["img"].shape,
        intensity_range=(v1, v3),
    )
    return {**stim, **params}


def checkerboard209(ppd=PPD, pad=True):
    """Checkerboard stimulus as shown in Robinson, Hammon, & de Sa (2007) Fig 1w.
    Stimulus size: 6.28125x20.9375 deg
    Target size: 2.09x2.09 deg

    Parameters
    ----------
    ppd : int
        Resolution of stimulus in pixels per degree. (default: 32)
    pad : bool
        If True, include padding to 32x32 deg (default: True)

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "mask")
        and additional keys containing stimulus parameters

    References
    -----------
    Blakeslee, B., & McCourt, M. E. (2004). A uniﬁed theory of brightness contrast and
        assimilation incorporating oriented multi-scale spatial ﬁltering and contrast
        normalization. Vision Research, 44, 2483–2503.
    DeValois, R. L., & DeValois, K. K. (1988). Spatial vision. New York: Oxford University Press.
    """

    nchecks_height, nchecks_width = 3, 10
    target_row = nchecks_height // 2
    params = {
        "ppd": ppd,
        "board_shape": (nchecks_height, nchecks_width),
        "check_visual_size": (67 / 32, 67 / 32),
        "targets": ((target_row, 2), (target_row, 7)),
        "extend_targets": False,
        "intensity_low": v1,
        "intensity_high": v3,
        "intensity_target": v2,
    }
    stim = illusions.checkerboards.checkerboard(**params)

    if pad:
        stim["img"] = pad_to_visual_size(stim["img"], VISEXTENT, ppd, pad_value=v2)
        stim["mask"] = pad_to_visual_size(stim["mask"], VISEXTENT, ppd, pad_value=0)

    params.update(
        visual_size=np.array(stim["img"].shape) / ppd,
        shape=stim["img"].shape,
        intensity_range=(v1, v3),
    )
    return {**stim, **params}


def corrugated_mondrian(ppd=PPD, pad=True):
    """Corrugated Mondrians as shown in Robinson, Hammon, & de Sa (2007) Fig 1x.

    Parameters
    ----------
    ppd : int
        Resolution of stimulus in pixels per degree. (default: 32)
    pad : bool
        If True, include padding to 32x32 deg (default: True)

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "mask")
        and additional keys containing stimulus parameters

    References
    -----------
    Blakeslee, B., & McCourt, M. E. (2001). A multiscale spatial filtering account of the
        Wertheimer-Benary effect and the corrugated Mondrian. Vision Research, 41, 2487–2502.
    Adelson, E. H. (1993). Perceptual organization and the judgment of brightness. Science,
        262, 2042–2044.
    """

    v1, v2, v3, v4 = 0.0, 0.4, 0.75, 1.0
    values = (
        (v3, v2, v3, v2, v3),
        (v4, v3, v2, v3, v4),
        (v3, v2, v3, v2, v3),
        (v2, v1, v2, v1, v2),
        (v3, v2, v3, v2, v3),
    )
    params = {
        "ppd": ppd,
        "widths": 2.0,
        "heights": 2.0,
        "depths": (0.0, -1.0, 0.0, 1.0, 0.0),
        "target_idx": ((1, 2), (3, 2)),
        "intensities": values,
        "intensity_background": 0.5,
    }

    stim = illusions.mondrians.corrugated_mondrians(**params)

    if pad:
        stim["img"] = pad_to_visual_size(stim["img"], VISEXTENT, ppd, pad_value=0.5)
        stim["mask"] = pad_to_visual_size(stim["mask"], VISEXTENT, ppd, pad_value=0)

    params.update(
        visual_size=np.array(stim["img"].shape) / ppd,
        shape=stim["img"].shape,
        intensity_range=(v1, v4),
    )
    return {**stim, **params}


def benary_cross(ppd=PPD, pad=True):
    """Benarys cross as shown in Robinson, Hammon, & de Sa (2007) Fig 1y.

    Parameters
    ----------
    ppd : int
        Resolution of stimulus in pixels per degree. (default: 32)
    pad : bool
        If True, include padding to 32x32 deg (default: True)

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "mask")
        and additional keys containing stimulus parameters

    References
    -----------
    Blakeslee, B., & McCourt, M. E. (2001). A multiscale spatial filtering account of the
        Wertheimer-Benary effect and the corrugated Mondrian. Vision Research, 41, 2487–2502.
    Benary, W. (1924). Beobachtungen zu einem Experiment über Helligkeitskontrast.
        Psychologische Forschung, 5, 131–142.
    """

    params = {
        "ppd": ppd,
        "cross_thickness": 4.0,
        "target_size": 2.5,
        "intensity_background": v3,
        "intensity_cross": v1,
        "intensity_target": v2,
    }

    stim = illusions.benary_cross.benarys_cross_triangles(
        visual_size=(13, 23),
        **params,
    )
    stim["img"] = np.fliplr(stim["img"])
    stim["mask"] = np.fliplr(stim["mask"])
    stim["mask"][stim["mask"] != 0] = np.abs(stim["mask"][stim["mask"] != 0] - 3)

    if pad:
        stim["img"] = pad_by_visual_size(stim["img"], ((0.0, 0.0), (4.0, 4.0)), ppd, pad_value=v3)
        stim["mask"] = pad_by_visual_size(stim["mask"], ((0.0, 0.0), (4.0, 4.0)), ppd, pad_value=0)
        stim["img"] = pad_to_visual_size(stim["img"], VISEXTENT, ppd, pad_value=v2)
        stim["mask"] = pad_to_visual_size(stim["mask"], VISEXTENT, ppd, pad_value=0)

    params.update(
        visual_size=np.array(stim["img"].shape) / ppd,
        shape=stim["img"].shape,
        intensity_range=(v1, v3),
    )
    return {**stim, **params}


def todorovic_benary1_2(ppd=PPD, pad=True):
    """Todorovic variation of Benarys cross as shown in Robinson, Hammon, & de Sa (2007) Fig 1z.
    Only contains the first two targets (1-2).

    Parameters
    ----------
    ppd : int
        Resolution of stimulus in pixels per degree. (default: 32)
    pad : bool
        If True, include padding to 32x32 deg (default: True)

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "mask")
        and additional keys containing stimulus parameters

    References
    -----------
    Blakeslee, B., & McCourt, M. E. (2001). A multiscale spatial filtering account of the
        Wertheimer-Benary effect and the corrugated Mondrian. Vision Research, 41, 2487–2502.
    Todorovic, D. (1997). Lightness and junctions. Perception, 26, 379–395.
    """

    params = {
        "ppd": ppd,
        "L_width": 2.5,
        "target_size": 2.5,
        "target_type": ("t", "t"),
        "target_ori": (0.0, 180.0),
        "target_posx": (2.5, 26.0),
        "target_posy": (4.0, 6.5),
        "intensity_background": v3,
        "intensity_cross": v1,
        "intensity_target": v2,
    }

    stim = illusions.benary_cross.todorovic_benary_generalized(
        visual_size=(13.0, 31.0),
        **params,
    )

    if pad:
        stim["img"] = pad_to_visual_size(stim["img"], VISEXTENT, ppd, pad_value=v2)
        stim["mask"] = pad_to_visual_size(stim["mask"], VISEXTENT, ppd, pad_value=0)

    params.update(
        visual_size=np.array(stim["img"].shape) / ppd,
        shape=stim["img"].shape,
        intensity_range=(v1, v3),
    )
    return {**stim, **params}


def todorovic_benary3_4(ppd=PPD, pad=True):
    """Todorovic variation of Benarys cross as shown in Robinson, Hammon, & de Sa (2007) Fig 1z.
    Only contains the last two targets (3-4).

    Parameters
    ----------
    ppd : int
        Resolution of stimulus in pixels per degree. (default: 32)
    pad : bool
        If True, include padding to 32x32 deg (default: True)

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "mask")
        and additional keys containing stimulus parameters

    References
    -----------
    Blakeslee, B., & McCourt, M. E. (2001). A multiscale spatial filtering account of the
        Wertheimer-Benary effect and the corrugated Mondrian. Vision Research, 41, 2487–2502.
    Todorovic, D. (1997). Lightness and junctions. Perception, 26, 379–395.
    """

    params = {
        "ppd": ppd,
        "L_width": 2.5,
        "target_size": 2.5,
        "target_type": ("t", "t"),
        "target_ori": (45.0, 225.0),
        "target_posx": (9.5, 18.0),
        "target_posy": (6.5, 6.5 - np.sqrt(12.5) / 2.0 + 1 / ppd),
        "intensity_background": v3,
        "intensity_cross": v1,
        "intensity_target": v2,
    }

    stim = illusions.benary_cross.todorovic_benary_generalized(
        visual_size=(13.0, 31.0),
        **params,
    )

    if pad:
        stim["img"] = pad_to_visual_size(stim["img"], VISEXTENT, ppd, pad_value=v2)
        stim["mask"] = pad_to_visual_size(stim["mask"], VISEXTENT, ppd, pad_value=0)

    params.update(
        visual_size=np.array(stim["img"].shape) / ppd,
        shape=stim["img"].shape,
        intensity_range=(v1, v3),
    )
    return {**stim, **params}


def todorovic_benary1_2_3_4(ppd=PPD, pad=True):
    """Todorovic variation of Benarys cross as shown in Robinson, Hammon, & de Sa (2007) Fig 1z.
    Contains all four targets (1-2-3-4).

    Parameters
    ----------
    ppd : int
        Resolution of stimulus in pixels per degree. (default: 32)
    pad : bool
        If True, include padding to 32x32 deg (default: True)

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "mask")
        and additional keys containing stimulus parameters

    References
    -----------
    Blakeslee, B., & McCourt, M. E. (2001). A multiscale spatial filtering account of the
        Wertheimer-Benary effect and the corrugated Mondrian. Vision Research, 41, 2487–2502.
    Todorovic, D. (1997). Lightness and junctions. Perception, 26, 379–395.
    """

    params = {
        "ppd": ppd,
        "L_width": 2.5,
        "target_size": 2.5,
        "target_type": ("t", "t", "t", "t"),
        "target_ori": (0.0, 45.0, 225.0, 180.0),
        "target_posx": (2.5, 9.5, 18.0, 26.0),
        "target_posy": (4.0, 6.5, 6.5 - np.sqrt(12.5) / 2.0 + 1 / ppd, 6.5),
        "intensity_background": v3,
        "intensity_cross": v1,
        "intensity_target": v2,
    }

    stim = illusions.benary_cross.todorovic_benary_generalized(
        visual_size=(13.0, 31.0),
        **params,
    )

    if pad:
        stim["img"] = pad_to_visual_size(stim["img"], VISEXTENT, ppd, pad_value=v2)
        stim["mask"] = pad_to_visual_size(stim["mask"], VISEXTENT, ppd, pad_value=0)

    params.update(
        visual_size=np.array(stim["img"].shape) / ppd,
        shape=stim["img"].shape,
        intensity_range=(v1, v3),
    )
    return {**stim, **params}


def bullseye_thin(ppd=PPD, pad=True):
    """Bullseye stimulus as shown in Robinson, Hammon, & de Sa (2007) Fig 1aa.
    Contains all four targets (1-2-3-4).
    Ring width: 0.1 deg

    Parameters
    ----------
    ppd : int
        Resolution of stimulus in pixels per degree. (default: 32)
    pad : bool
        If True, include padding to 32x32 deg (default: True)

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "mask")
        and additional keys containing stimulus parameters

    References
    -----------
    Bindman, D., & Chubb, C. (2004). Brightness assimilation in bullseye displays. Vision
        Research, 44, 309–319.
    """

    params = {
        "ppd": ppd,
        "n_rings": 8,
        "ring_width": 0.1,
        "intensity_target": v2,
    }

    stim1 = illusions.bullseye.bullseye_stimulus(
        **params,
        intensity_rings=(v3, v1),
    )
    stim2 = illusions.bullseye.bullseye_stimulus(
        **params,
        intensity_rings=(v1, v3),
    )

    # Individual padding
    if pad:
        stim1["img"] = pad_to_visual_size(stim1["img"], np.array(VISEXTENT) / 2, ppd, pad_value=v2)
        stim1["mask"] = pad_to_visual_size(
            stim1["mask"], np.array(VISEXTENT) / 2, ppd, pad_value=0
        )
        stim2["img"] = pad_to_visual_size(stim2["img"], np.array(VISEXTENT) / 2, ppd, pad_value=v2)
        stim2["mask"] = pad_to_visual_size(
            stim2["mask"], np.array(VISEXTENT) / 2, ppd, pad_value=0
        )

    # Increase target index of right stimulus half
    stim2["mask"] = stim2["mask"] + 1
    stim2["mask"][stim2["mask"] == 1] = 0

    stim = {
        "img": np.hstack((stim1["img"], stim2["img"])),
        "mask": np.hstack((stim1["mask"], stim2["mask"])),
    }

    # Full padding
    if pad:
        stim["img"] = pad_to_visual_size(stim["img"], VISEXTENT, ppd, pad_value=v2)
        stim["mask"] = pad_to_visual_size(stim["mask"], VISEXTENT, ppd, pad_value=0)

    params.update(
        visual_size=np.array(stim["img"].shape) / ppd,
        shape=stim["img"].shape,
        intensity_range=(v1, v3),
    )
    return {**stim, **params}


def bullseye_thick(ppd=PPD, pad=True):
    """Bullseye stimulus as shown in Robinson, Hammon, & de Sa (2007) Fig 1bb.
    Contains all four targets (1-2-3-4).
    Ring width: 0.2 deg

    Parameters
    ----------
    ppd : int
        Resolution of stimulus in pixels per degree. (default: 32)
    pad : bool
        If True, include padding to 32x32 deg (default: True)

    Returns
    -------
    dict of str
        dict with the stimulus (key: "img") and target mask (key: "mask")
        and additional keys containing stimulus parameters

    References
    -----------
    Bindman, D., & Chubb, C. (2004). Brightness assimilation in bullseye displays. Vision
        Research, 44, 309–319.
    """

    params = {
        "ppd": ppd,
        "n_rings": 6,
        "ring_width": 0.2,
        "intensity_target": v2,
    }

    stim1 = illusions.bullseye.bullseye_stimulus(
        **params,
        intensity_rings=(v3, v1),
    )
    stim2 = illusions.bullseye.bullseye_stimulus(
        **params,
        intensity_rings=(v1, v3),
    )

    # Individual padding
    if pad:
        stim1["img"] = pad_to_visual_size(stim1["img"], np.array(VISEXTENT) / 2, ppd, pad_value=v2)
        stim1["mask"] = pad_to_visual_size(
            stim1["mask"], np.array(VISEXTENT) / 2, ppd, pad_value=0
        )
        stim2["img"] = pad_to_visual_size(stim2["img"], np.array(VISEXTENT) / 2, ppd, pad_value=v2)
        stim2["mask"] = pad_to_visual_size(
            stim2["mask"], np.array(VISEXTENT) / 2, ppd, pad_value=0
        )

    # Increase target index of right stimulus half
    stim2["mask"] = stim2["mask"] + 1
    stim2["mask"][stim2["mask"] == 1] = 0

    stim = {
        "img": np.hstack((stim1["img"], stim2["img"])),
        "mask": np.hstack((stim1["mask"], stim2["mask"])),
    }

    # Full padding
    if pad:
        stim["img"] = pad_to_visual_size(stim["img"], VISEXTENT, ppd, pad_value=v2)
        stim["mask"] = pad_to_visual_size(stim["mask"], VISEXTENT, ppd, pad_value=0)

    params.update(
        visual_size=np.array(stim["img"].shape) / ppd,
        shape=stim["img"].shape,
        intensity_range=(v1, v3),
    )
    return {**stim, **params}


if __name__ == "__main__":
    from stimuli.utils import plot_stimuli

    stims = gen_all(pad=True, skip=True)
    plot_stimuli(stims, mask=False)
