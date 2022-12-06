import numpy as np
from scipy.signal import fftconvolve
from stimuli.utils import degrees_to_pixels


# TODO: constrain allowed stimulus sizes

i1 = 1
i2 = 2
def wedding_cake_stimulus(
    visual_size=(20., 15.),
    ppd=32.,
    L_size=(4., 4, 1.),
    target_height=2.,
    target_indices1=((i1, -1), (i1, 0), (i1, 1), (i1, 2)),
    target_indices2=((i2, 0), (i2, 1), (i2, 2), (i2, 3)),
    intensity_grating=(1., 0.),
    intensity_target=0.5,
):
    """
    Wedding cake stimulus

    Parameters
    ----------
    visual_size : (float, float)
        The shape of the stimulus in degrees of visual angle. (y,x)
    ppd : int
        pixels per degree (visual angle)
    L_size : (float, float, float)
        size of individual jags (height, width, thickness) in degree visual angle
    target_height : float
        height of targets in degree visual angle
    target_indices1 : nested tuples
        target indices with intensity1-value; as many tuples as there are targets
        each with (y, x) indices
    target_indices2 : nested tuples
        target indices with intensity2-value; as many tuples as there are targets
        each with (y, x) indices
    intensity_grating : (float, float)
        intensity values of the grating
    intensity_target : float
        intensity value of targets

    Returns
    -------
    A stimulus dictionary with the stimulus ['img'] and target mask ['mask']
    """

    nY, nX = degrees_to_pixels(visual_size, ppd)
    Ly, Lx, Lw = degrees_to_pixels(L_size, ppd)
    Lyh, Lxh = int(Ly / 2)+1, int(Lx / 2)+1
    theight = degrees_to_pixels(target_height, ppd)
    
    # Create L-shaped patch
    L_patch = np.zeros([Ly, Lx])
    L_patch[0:Lw, 0:Lx] = 1
    L_patch[0:Ly, Lx - Lw : :] = 1
    
    # Create target patches
    tpatch1 = np.zeros(L_patch.shape)
    tpatch1[int(Ly/2 - theight/2):int(Ly/2+theight/2),
            Lx-Lw::] = -intensity_grating[1] + intensity_target
    
    tpatch2 = np.zeros(L_patch.shape)
    tpatch2[int(Ly/2 - theight/2):int(Ly/2+theight/2),
            Lx-Lw::] = -intensity_grating[0] + intensity_target
    
    
    # We initially create a larger image array to avoid boundary problems
    nY, nX = nY*2, nX*2

    # Create grid-like array to create wedding cake pattern
    array1 = np.zeros([nY, nX])
    ys, xs = np.arange(0, nY, Ly-Lw), np.arange(0, nX, Lx)
    n = np.minimum(len(ys), len(xs))
    array1[ys[0:n], xs[0:n]] = np.arange(1, n+1)

    array2 = np.zeros([nY, nX])
    ys, xs = np.arange(0, nY, Lw*2), np.arange(0, nX, Lw*2)
    n = np.minimum(len(ys), len(xs))
    array2[ys[0:n], xs[0:n]] = np.arange(1, n+1)
    array2 = np.rot90(array2)
    amax = int( (array2.max()+1) / 2)

    array3 = fftconvolve(array1, array2, "same")

    if target_indices1 is not None:
        array_t1 = np.zeros(array3.shape)
        for (ty, tx) in target_indices1:
            arr1 = np.copy(array1)
            arr2 = np.copy(array2)
            arr1[arr1!=ty+2] = 0
            arr2[arr2!=tx+amax] = 0
            array_t1 += fftconvolve(arr1, arr2, "same")
        array_t1[array_t1<1] = 0
        array_t1[array_t1>1] = 1
        t1 = np.round(fftconvolve(array_t1, tpatch1, "same"), 5)
        t1 = t1[Lyh:Lyh+int(nY/2), Lxh:Lxh+int(nX/2)]

    else:
        t1 = np.zeros([int(nY/2), int(nX/2)])
    
    if target_indices2 is not None:
        array_t2 = np.zeros(array3.shape)
        for (ty, tx) in target_indices2:
            arr1 = np.copy(array1)
            arr2 = np.copy(array2)
            arr1[arr1!=ty+2] = 0
            arr2[arr2!=tx+amax] = 0
            array_t2 += fftconvolve(arr1, arr2, "same")
        array_t2[array_t2<1] = 0
        array_t2[array_t2>1] = 1
        t2 = np.round(fftconvolve(array_t2, tpatch2, "same"), 5)
        t2 = t2[Lyh-Lw:Lyh+int(nY/2)-Lw, Lxh+Lw:Lxh+int(nX/2)+Lw]

    else:
        t2 = np.zeros([int(nY/2), int(nX/2)])

    # Create wedding cake pattern
    imgt = fftconvolve(array3, L_patch, "same")
    imgt = np.round(imgt)
    img = np.copy(imgt)
    img[imgt > 1] = intensity_grating[1]
    img[imgt < 1] = intensity_grating[0]
    img = img[Lyh:Lyh+int(nY/2), Lxh:Lxh+int(nX/2)]
    
    # Create target mask
    mask = np.abs(t1 * 1./intensity_target) + np.abs(t2 * 2./intensity_target)
    mask = np.round(mask).astype(int)
    
    # Add targets
    img = img + t1
    img = img + t2
    
    stim = {
        "img": img,
        "mask": mask.astype(int),
        "shape": img.shape,
        "visual_size": np.array(img.shape) / ppd,
        "ppd": ppd,
        "L_size": L_size,
        "target_height": target_height,
        "intensity_grating": intensity_grating,
        "intensity_target": intensity_target,
        "target_indices1": target_indices1,
        "target_indices2": target_indices2,
    }
    
    return stim




if __name__ == "__main__":
    import matplotlib.pyplot as plt
    from stimuli.utils import plot_stimuli

    stims = {
        "Wedding cake new": wedding_cake_stimulus(),
    }

    plot_stimuli(stims, mask=False)
    plt.show()
