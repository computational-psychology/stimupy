import numpy as np
from stimuli.components import disc_and_rings
from stimuli.utils import degrees_to_pixels, resize_array, pad_img_to_shape


def circular_white(
    shape=(10, 10),
    ppd=18,
    frequency=1,
    vdiscs=(0., 1.),
    vbackground=0.2,
    vtarget=0.5,
    target_indices=(3, 6,),
    ssf=1,
):
    """
    Circular White stimulus

    Parameters
    ----------
    shape : (float, float)
        The shape of the stimulus in degrees of visual angle. (y,x)
    ppd : int
        pixels per degree (visual angle)
    frequency : float
        the spatial frequency of the circular grating in cycles per degree
    vdiscs : (float, float)
        intensity values of discs
    vbackground : float
        value of background
    vtarget : float
        value of target discs
    target_indices : (int, )
        indices of target discs
    ssf : int (optional)
          the supersampling-factor used for anti-aliasing if >1. Default is 1.
          Warning: produces smoother circles but might introduce gradients that affect vision!

    Returns
    ----------
    A stimulus dictionary with the stimulus ['img'] and target mask ['mask']
    """

    height_px, width_px = degrees_to_pixels(shape, ppd)
    cycle_width_px = degrees_to_pixels(1. / (frequency*2), ppd) * 2
    radius = (cycle_width_px / 2) / ppd
    n_discs = np.minimum(height_px, width_px) // cycle_width_px

    if target_indices is None:
        target_indices = ()
    if isinstance(target_indices, (float, int)):
        target_indices = (target_indices,)
    if isinstance(shape, (float, int)):
        shape = (shape, shape)
    if len(shape) != 2:
        raise ValueError("shape needs to be a single float or a tuple of two floats")
    if len(vdiscs) != 2:
        raise ValueError("vdiscs needs to be a tuple of two floats")
    if not isinstance(vtarget, (float, int)):
        raise ValueError("vtarget should be a single float / int")
    if not isinstance(frequency, (float, int)):
        raise ValueError("frequency should be a single float / int")
    if degrees_to_pixels(1./frequency, ppd) % 2 != 0:
        frequency_used = 1. / cycle_width_px*ppd
        freqs = (frequency, frequency_used)
        print("Warning: Circular White frequency changed from %f to %f ensure an even-numbered cycle width!" % freqs)
    if n_discs < 1:
        raise ValueError("No circle fits in requested shape! Increase frequency or shape")

    radii = []
    vdiscs_img = []
    vdics_mask = []
    mask_counter = 1
    for i in range(n_discs):
        radii.append(radius*(i+1))
        if i in target_indices:
            vdiscs_img.append(vtarget)
            vdics_mask.append(mask_counter)
            mask_counter += 1
        elif i not in target_indices and i % 2 == 0:
            vdiscs_img.append(vdiscs[0])
            vdics_mask.append(0)
        elif i not in target_indices and i % 2 == 1:
            vdiscs_img.append(vdiscs[1])
            vdics_mask.append(0)

    img = disc_and_rings(ppd, radii, vbackground, vdiscs_img, ssf)
    mask = disc_and_rings(ppd, radii, 0, vdics_mask, ssf)

    # Pad to desired size
    img = pad_img_to_shape(img, np.array(shape)*ppd, vbackground)
    mask = pad_img_to_shape(mask, np.array(shape)*ppd, 0)

    # Target masks should only cover areas where target intensity is exactly vtarget
    cond = ((img != vtarget) & (mask != 0))
    mask[cond] = 0
    return {"img": img, "mask": mask.astype(int)}


def radial_white(
    shape=(10, 12),
    ppd=20,
    n_segments=8,
    rotate=3*np.pi,
    target_width=2.5,
    target_center=2.5,
    target_indices=(0, 1, 2, 3, 4),
    vslices=(1., 0.),
    vbackground=0.3,
    vtarget=0.5,
    ssf=1,
):
    """
    Radial White stimulus

    Parameters
    ----------
    shape : (float, float)
        The shape of the stimulus in degrees of visual angle. (y,x)
    ppd : int
        pixels per degree (visual angle)
    n_segments : int
        number of cycles in stimulus (= half number of slices)
    rotate : float
        orientation of circle in radians
    target_width : float
        target width given the slice shape in deg
    target_center : float
        target center within slice in deg
    target_indices : int or (int, )
        indices of target slices
    vslices : (float, float)
        intensity values of slices
    vtarget : float
        value of target discs
    ssf : int (optional)
          the supersampling-factor used for anti-aliasing if >1. Default is 1.
          Warning: produces smoother circles but might introduce gradients that affect vision!

    Returns
    ----------
    A stimulus dictionary with the stimulus ['img'] and target mask ['mask']
    """

    shape_px = degrees_to_pixels(np.minimum(shape[0], shape[1]), ppd) * ssf
    x = np.arange(-int(shape_px/2), int(shape_px/2))
    img = np.ones([shape_px, shape_px]) * vbackground
    mask = np.zeros([shape_px, shape_px])
    rotate = rotate % (2*np.pi)

    if target_indices is None:
        target_indices = ()
    if isinstance(target_indices, (float, int)):
        target_indices = (target_indices,)
    if isinstance(shape, (float, int)):
        shape = (shape, shape)
    if not isinstance(n_segments, (float, int)):
        raise ValueError("n_segments should be a single float or int")
    if not n_segments % 2 == 0:
        raise ValueError("n_segments should be even-numbered")
    if not isinstance(target_width, (float, int)):
        raise ValueError("target_width should be a single float or int")
    if not isinstance(target_center, (float, int)):
        raise ValueError("target_center should be a single float or int")
    if (target_center-target_width/2)*ppd < 0 or (target_center+target_width/2)*ppd > shape_px/2:
        raise ValueError("Warning: targets do not fully fit into stimulus")
    if not isinstance(rotate, (float, int)):
        raise ValueError("rotate should be a single float or int")
    if len(vslices) != 2:
        raise ValueError("vdiscs needs to be a tuple of two floats")

    # Create circle (i.e. radial part)
    yy, xx = np.meshgrid(x, x)
    radial = np.sqrt(yy**2. + xx**2.)
    radial[radial > x.max()] = 0
    radial[int(shape_px/2), int(shape_px/2)] = 1

    tradial = np.copy(radial)
    tradial[tradial < ppd*(target_center - target_width/2)] = 0
    tradial[tradial > ppd*(target_center + target_width/2)] = 0

    # Calculate angular part
    angular = np.arctan2(yy, xx)
    angular = angular - angular.min() + rotate
    angular[angular > 2*np.pi] -= 2*np.pi
    angular[angular == 0] = 0.0001

    # Divide circle in nparts:
    theta = np.linspace(0, 2*np.pi, n_segments+1)
    theta[theta > 2*np.pi] -= 2*np.pi
    for i in range(n_segments):
        ang = np.copy(angular)
        ang[angular <= theta[i]] = 0
        ang[angular > theta[i+1]] = 0
        indices = ang * radial
        tindices = ang * tradial
        img[indices != 0] = vslices[i % 2]

        if i in target_indices:
            img[tindices != 0] = vtarget
            mask[tindices != 0] = target_indices.index(i) + 1

    # downsample the stimulus by local averaging along rows and columns
    sampler = resize_array(np.eye(img.shape[0] // ssf), (1, ssf))
    img = np.dot(sampler, np.dot(img, sampler.T)) / ssf**2
    mask = np.dot(sampler, np.dot(mask, sampler.T)) / ssf**2

    # Pad to desired size
    img = pad_img_to_shape(img, np.array(shape)*ppd, vbackground)
    mask = pad_img_to_shape(mask, np.array(shape)*ppd, 0)

    # Target masks should only cover areas where target intensity is exactly vtarget
    cond = ((img != vtarget) & (mask != 0))
    mask[cond] = 0

    return {"img": img, "mask": mask}


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    from stimuli.utils import plot_stimuli

    stims = {
        "Circular White's effect": circular_white(),
        "Radial white": radial_white(),
    }

    plot_stimuli(stims, mask=False)
    plt.show()
