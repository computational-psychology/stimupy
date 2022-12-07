import numpy as np
import warnings

from stimuli.components.components_ import square_wave_grating, square_wave, parallelogram
from stimuli.utils import degrees_to_pixels, pad_to_visual_size, pad_to_shape


__all__ = [
    "grating_illusion",
    "grating_uniform",
    "grating_grating",
    "grating_grating_shifted",
    "grating_grating_parallelogram",
    "counterphase_induction",
]

# TODO: update docstrings

def grating_illusion(
    ppd=10,
    n_bars=8,
    target_indices=(2, 4),
    bar_shape=(8, 1.0),
    intensity_bars=(0.0, 1.0),
    intensity_target=0.5,
):
    """
    Grating illusion

    Parameters
    ----------
    ppd : int
        pixels per degree (visual angle)
    n_bars : int
        the number of vertical bars
    target_indices : tuple
        tuple with bar target indices from left to right
    bar_shape : (float, float)
        bar height and width in degrees visual angle
    intensity_bars : (float, float)
        intensity values for bars
    intensity_target : float
        intensity value for target

    Returns
    -------
    A stimulus dictionary with the stimulus ['img'] and target mask ['mask']
    """

    bar_width_px = degrees_to_pixels(bar_shape[1], ppd)
    img = square_wave_grating(
        ppd=ppd,
        n_bars=n_bars,
        bar_shape=bar_shape,
        intensity_bars=intensity_bars,
        )["img"]
    mask = np.zeros(img.shape)

    if isinstance(target_indices, (float, int)):
        target_indices = (target_indices,)

    for i, idx in enumerate(target_indices):
        img[:, idx * bar_width_px : (idx + 1) * bar_width_px] = intensity_target
        mask[:, idx * bar_width_px : (idx + 1) * bar_width_px] = i + 1
    return {"img": img, "mask": mask}


def grating_uniform(
    visual_size=(10.0, 10.0),
    ppd=10,
    target_size=(3., 3.),
    frequency=3,
    intensity_background=0.0,
    intensity_bars=(1.0, 0.5),
    intensity_target=0.5,
    period="full",
):
    """
    Grating on a uniform background

    Parameters
    ----------
    visual_size : float or (float, float)
        size of the image in degrees visual angle
    ppd : int
        pixels per degree (visual angle)
    n_bars : int
        the number of vertical bars
    bar_shape : (float, float)
        bar height and width in degrees visual angle
    intensity_background : float
        intensity value for background
    intensity_bar : float
        intensity value for bar
    intensity_target : float
        intensity value for other bar which indicates target

    Returns
    -------
    A stimulus dictionary with the stimulus ['img'] and target mask ['mask']
    """
    if isinstance(visual_size, (float, int)):
        visual_size = (visual_size, visual_size)

    img = square_wave(
        visual_size=target_size,
        ppd=ppd,
        frequency=frequency,
        intensity_bars=intensity_bars,
        period=period,
        )["img"]
    mask = np.zeros(img.shape)
    mask[img == intensity_target] = 1

    # Padding
    img = pad_to_visual_size(img=img, visual_size=visual_size, ppd=ppd, pad_value=intensity_background)
    mask = pad_to_visual_size(img=mask, visual_size=visual_size, ppd=ppd, pad_value=0)
    
    stim = {
        "img": img,
        "mask": mask.astype(int),
        "ppd": ppd,
        "visual_size": np.array(img.shape) / ppd,
        "shape": img.shape,
        "frequency": frequency,
        "period": period,
        "intensity_background": intensity_background,
        "intensity_bars": intensity_bars,
        "intensity_target": intensity_target,
        }
    return stim


def grating_grating(
    visual_size=(10.0, 10.0),
    ppd=10,
    target_size=(2.5, 2.5),
    frequency=3,
    intensity_bars=(0, 1.),
    intensity_target=(None, 0.5),
    period="full",
):
    """
    Grating on a grating

    Parameters
    ----------
    visual_size : float or (float, float)
        size of the image in degrees visual angle
    ppd : int
        pixels per degree (visual angle)
    n_bars : int
        the number of vertical bars
    bar_shape : (float, float)
        bar height and width in degrees visual angle
    intensity_bars : (float, float)
        intensity values for bars
    intensity_target : float
        value for target bar

    Returns
    -------
    A stimulus dictionary with the stimulus ['img'] and target mask ['mask']
    """
    if isinstance(visual_size, (float, int)):
        visual_size = (visual_size, visual_size)
    if isinstance(target_size, (float, int)):
        target_size = (target_size, target_size)
    
    stim = square_wave(
        visual_size=visual_size,
        ppd=ppd,
        frequency=frequency,
        intensity_bars=intensity_bars,
        period=period,
        )
    img = stim["img"]
    pixels_per_cycle = stim["pixels_per_cycle"]

    cy, cx = img.shape
    img_cut = img[int(cy/2 - target_size[0]/2 * ppd):int(cy/2 + target_size[0]/2 * ppd),
                  int(cx/2 - target_size[1]/2 * ppd):int(cx/2 + target_size[1]/2 * ppd)]
    img_cut_ = np.copy(img_cut)
    
    if intensity_target[0] is not None:
        int_target = intensity_target[0]
        img_cut[img_cut_ == intensity_bars[0]] = int_target
    if intensity_target[1] is not None:
        int_target = intensity_target[1]
        img_cut[img_cut_ == intensity_bars[1]] = int_target
    
    img[int(cy/2 - target_size[0]/2 * ppd):int(cy/2 + target_size[0]/2 * ppd),
        int(cx/2 - target_size[1]/2 * ppd):int(cx/2 + target_size[1]/2 * ppd)] = img_cut

    mask = np.zeros(img_cut.shape)
    mask[img_cut == int_target] = 1
    mask = pad_to_visual_size(mask, visual_size, ppd, 0)
    
    stim = {
        "img": img,
        "mask": mask.astype(int),
        "ppd": ppd,
        "visual_size": np.array(img.shape) / ppd,
        "shape": img.shape,
        "frequency": frequency,
        "period": period,
        "intensity_bars": intensity_bars,
        "intensity_target": intensity_target,
        "pixels_per_cycle": pixels_per_cycle,
        }
    return stim


def grating_grating_shifted(
    visual_size=(10.0, 10.0),
    ppd=10,
    target_size=(2.5, 2.5),
    frequency=3,
    intensity_bars=(0, 1.),
    intensity_target=(None, 0.5),
    period="full",
):
    """
    Grating on a shifted grating

    Parameters
    ----------
    ppd : int
        pixels per degree (visual angle)
    n_bars : int
        the number of vertical bars
    bar_shape : (float, float)
        bar height and width in degrees visual angle
    im_size : (float, float)
        height and width of stimulus in visual angle
    intensity_bars : (float, float)
        intensity values for bars
    intensity_target : float
        value for target bar

    Returns
    -------
    A stimulus dictionary with the stimulus ['img'] and target mask ['mask']
    """
    
    if isinstance(target_size, (float, int)):
        target_size = (target_size, target_size)

    stim = grating_grating(
        visual_size=visual_size,
        ppd=ppd,
        target_size=target_size,
        frequency=frequency,
        intensity_bars=intensity_bars,
        intensity_target=intensity_target,
        period=period,
        )
    img = stim["img"]
    mask = stim["mask"]
    bar_width = int(stim["pixels_per_cycle"] / 2)
    cy, cx = img.shape
    
    # Move upper grating
    img_cut = img[0:int(cy/2 - target_size[0]/2*ppd), :]
    img_cut2 = np.ones(img_cut.shape) * intensity_bars[1]
    img_cut2[:, bar_width::] = img_cut[:, 0:cx-bar_width]
    img[0:int(cy/2 - target_size[0]/2*ppd), :] = img_cut2
    
    # Move lower grating
    start = int(cy/2 + target_size[0]/2*ppd)
    img_cut = img[start::, :]
    img_cut2 = np.ones(img_cut.shape) * intensity_bars[1]
    img_cut2[:, bar_width::] = img_cut[:, 0:cx-bar_width]
    img[start::, :] = img_cut2
    
    stim = {
        "img": img,
        "mask": mask.astype(int),
        "ppd": ppd,
        "visual_size": np.array(img.shape) / ppd,
        "shape": img.shape,
        "frequency": frequency,
        "period": period,
        "intensity_bars": intensity_bars,
        "intensity_target": intensity_target,
        }
    return stim


def grating_grating_parallelogram(
    visual_size=(10.0, 10.0),
    ppd=20,
    parallelogram_size=(3., 3., 1.),
    frequency=3,
    intensity_bars=(0., 1.),
    intensity_innerbars=(1., 0.5),
    intensity_target=0.5,
    period="full",
):
    """
    Grating on a uniform background

    Parameters
    ----------
    visual_size : float or (float, float)
        size of the image in degrees visual angle
    ppd : int
        pixels per degree (visual angle)
    n_bars : int
        the number of vertical bars
    bar_shape : (float, float)
        bar height and width in degrees visual angle
    parallelogram_size: (float, float, float)
        height, width, depth of parallelogram in visual angle
    intensity_background : float
        intensity value for background
    intensity_bar : float
        intensity value for bar
    intensity_target : float
        intensity value for other bar which indicates target

    Returns
    -------
    A stimulus dictionary with the stimulus ['img'] and target mask ['mask']
    """
    if isinstance(visual_size, (float, int)):
        visual_size = (visual_size, visual_size)
    
    img1 = square_wave(
        visual_size=visual_size,
        ppd=ppd,
        frequency=frequency,
        intensity_bars=intensity_bars,
        period=period,
        )["img"]
    
    imsize_max = np.max(img1.shape)
    if imsize_max > np.min(np.array(visual_size) * ppd):
        visual_size = (imsize_max/ppd,) * 2
        
    img1 = pad_to_visual_size(img1, visual_size, ppd, intensity_bars[0])
    
    img2 = square_wave(
        visual_size=(parallelogram_size[0]+parallelogram_size[2], parallelogram_size[1]+parallelogram_size[2]),
        ppd=ppd,
        frequency=frequency,
        intensity_bars=intensity_innerbars,
        period="half",
        )["img"]
    img2 = np.rot90(img2)
    img2 = pad_to_visual_size(img2, visual_size, ppd, intensity_innerbars[0])

    parallel = parallelogram(
        visual_size=(parallelogram_size[0], parallelogram_size[1]),
        ppd=ppd,
        parallelogram_depth=parallelogram_size[2],
        intensity_background=1.,
        intensity_parallelogram=0.,
        )
    parallel["img"] = pad_to_visual_size(parallel["img"], visual_size, ppd, 1.)
    parallel["mask"] = pad_to_visual_size(parallel["mask"], visual_size, ppd, 0.)
    
    img = img1*parallel["img"] + img2*parallel["mask"]
    mask = np.zeros(img.shape)
    mask[img == intensity_target] = 1

    stim = {
        "img": img,
        "mask": mask.astype(int),
        "ppd": ppd,
        "visual_size": np.array(img.shape) / ppd,
        "shape": img.shape,
        "frequency": frequency,
        "period": period,
        "intensity_bars": intensity_bars,
        "intensity_innerbars": intensity_innerbars,
        "intensity_target": intensity_target,
        }
    return stim


def counterphase_induction(
    visual_size=(10.0, 10.0),
    ppd=40,
    frequency=3,
    target_height=3.,
    target_repetitions=4,
    target_phase=-0,
    intensity_bars=(1., 0.),
    intensity_target=0.5,
    period="full",
):
    if isinstance(visual_size, (float, int)):
        visual_size = (visual_size, visual_size)
    
    stim1 = square_wave(
        visual_size=visual_size,
        ppd=ppd,
        frequency=frequency,
        intensity_bars=intensity_bars,
        period=period,
        )
    img = stim1["img"]
    pixels_per_cycle = stim1["pixels_per_cycle"]
    
    img2 = square_wave(
        visual_size=(target_height, target_repetitions*pixels_per_cycle/ppd),
        ppd=ppd,
        frequency=frequency,
        intensity_bars=(0., intensity_target),
        period=period,
        )["img"]
    img2 = pad_to_shape(img2, img.shape, 0)
    
    # Translate phase information into pixels
    target_phasea = np.abs(target_phase)
    target_phasea = target_phasea % 360
    target_amount = target_phasea / 360.
    target_shift = target_amount * pixels_per_cycle
    target_shifti = int(np.round(target_shift))
    target_phasei = target_shifti / pixels_per_cycle * 360
    
    if target_shift != int(target_shift):
        s = np.sign(target_phase)
        warnings.warn(f"Rounding phase; {target_phase} -> {s*target_phasei}")
    
    # Shift targets by specified phase
    cy, cx = img2.shape
    if target_phase < 0:
        img2[:, 0:cx-target_shifti] = img2[:, target_shifti::]
    else:
        img2[:, target_shifti::] = img2[:, 0:cx-target_shifti]
    
    # Add targets on grating
    mask_temp = np.ones(img2.shape)
    mask_temp[img2 == intensity_target] = 0
    img = img * mask_temp + img2
    mask = np.abs(mask_temp-1)

    stim = {
        "img": img,
        "mask": mask.astype(int),
        "ppd": ppd,
        "visual_size": np.array(img.shape) / ppd,
        "shape": img.shape,
        "frequency": frequency,
        "target_height": target_height,
        "target_repetitions": target_repetitions,
        "target_phase": target_phasei,
        "period": period,
        "intensity_bars": intensity_bars,
        "intensity_target": intensity_target,
        "pixels_per_cycle": pixels_per_cycle,
        }
    return stim



if __name__ == "__main__":
    import matplotlib.pyplot as plt

    from stimuli.utils import plot_stimuli

    stims = {
        "Grating illusion": grating_illusion(),
        "Grating - uniform": grating_uniform(),
        "Grating - grating": grating_grating(),
        "Grating - grating shifted": grating_grating_shifted(),
        "Grating - grating parallelogram": grating_grating_parallelogram(),
        "Counterphase induction": counterphase_induction(),
    }

    plot_stimuli(stims, mask=True)
    plt.show()
