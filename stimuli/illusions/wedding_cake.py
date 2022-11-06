import numpy as np
from stimuli.utils import degrees_to_pixels


# TODO: does not allow flexible parameter changes yet. WIP
def wedding_cake_stimulus(
    ppd=10,
    L_size=(10.0, 10.0, 2.0),
    L_repeats=(3.0, 3.0),
    target_height=4.0,
    target_idx_intensity1=((-1, 0), (0, 0), (1, 0)),
    target_idx_intensity2=None,
    intensity_grating=(0.0, 1),
    intensity1=0.0,
    intensity2=1.0,
    intensity_target=0.5,
):
    """
    White zigzag stimulus (also wedding cake stimulus)

    Parameters
    ----------
    ppd : int
        pixels per degree (visual angle)
    L_size : (float, float, float)
        size of individual jags (height, width, thickness) in degree visual angle
    L_distance : float
        distance between parallel jags in degree visual angle
    L_repeats : (float, float)
        number of repeats of jags in y and x direction
    target_height : float
        height of targets in degree visual angle
    target_idx_intensity1 : nested tuples
        target indices with intensity1-value; as many tuples as there are targets each with (y, x) indices;
        (0, 0) places a target in the center
    target_idx_intensity2 : nested tuples
        target indices with intensity2-value; as many tuples as there are targets each with (y, x) indices;
        (0, 0) places a target in the center
    intensity1 : float
        first intensity value for grating
    intensity2 : float
        second intensity value for grating
    intensity_target : float
        value for target(s)

    Returns
    -------
    A stimulus dictionary with the stimulus ['img'] and target mask ['mask']
    """
    Ly, Lx, Lw = degrees_to_pixels(L_size, ppd)
    Ld = Lw
    Lywd, Lxwd = Ly, Lx
    nL = L_repeats
    theight = degrees_to_pixels(target_height, ppd)

    mval2 = 2
    if target_idx_intensity1 is None:
        target_idx_intensity1 = ()
        mval2 = 1
    if target_idx_intensity2 is None:
        target_idx_intensity2 = ()

    if len(L_size) != 3:
        raise Exception("L_size needs to have a length of 3")

    if isinstance(nL, (int, float)):
        nL = (nL, nL)
    if np.min(nL) < 2:
        raise Exception("L_repeats should be larger than 1")

    # Create grid patch
    L_patch = np.zeros([Ly, Lx])
    L_patch[0:Lw, 0:Lx] = intensity1 - intensity2
    L_patch[0:Ly, Lx - Lw : :] = intensity1 - intensity2
    L_patch[0:Lw, 0:Lw] = (intensity1 - intensity2) / 2.0
    L_patch[Ly - Lw : :, Lx - Lw : :] = (intensity1 - intensity2) / 2.0

    # Create target and mask patch 1
    tpatch1 = np.zeros([Ly, Lx])
    tpatch1[int(Ly / 2 - theight / 2) : int(Ly / 2 + theight / 2), Lx - Lw : :] = (
        intensity_target - intensity1
    )
    mpatch1 = np.zeros([Ly, Lx])
    mpatch1[int(Ly / 2 - theight / 2) : int(Ly / 2 + theight / 2), Lx - Lw : :] = 1

    # Create target and mask patch 2
    tpatch2 = np.zeros([Ly, Lx])
    tpatch2[int(Ly / 2 - theight / 2) : int(Ly / 2 + theight / 2), Lx - Lw - Ld : Lx - Lw,] = (
        intensity_target - intensity2
    )
    mpatch2 = np.zeros([Ly, Lx])
    mpatch2[
        int(Ly / 2 - theight / 2) : int(Ly / 2 + theight / 2),
        Lx - Lw - Ld : Lx - Lw,
    ] = mval2

    # Create image slightly larger than needed
    img = np.ones([int(Lywd * (nL[0] + 2)), int(Lxwd * (nL[1] + 2))]) * intensity2
    height, width = img.shape
    mask = np.zeros([height, width])

    # Create indices to place grid
    idx_y = np.arange(0, height - Ly, Ly - Lw)
    idx_x = np.arange(0, width - Lx, Lx - Lw)

    for j in range(int(np.max(nL) ** 2)):
        # Calculate starting coordinates in grid
        ny, nx = j * (Ly + Ld) - (Ly - Lw) * j, j * (Lx + Ld) - (Lx - Lw) * j
        my, mx = (
            j * (Ly - Ld - Lw * 2) - (Ly - Lw) * j,
            j * (Lx - Ld - Lw * 2) - (Lx - Lw) * j,
        )
        for i in range(np.minimum(len(idx_x), len(idx_y))):
            if idx_y[i] + ny >= 0 and idx_x[i] + mx >= 0:
                # Add grid in lower left half
                if idx_y[i] + ny < height - Ly and idx_x[i] + mx < width - Lx:
                    img[
                        idx_y[i] + ny : idx_y[i] + ny + Ly,
                        idx_x[i] + mx : idx_x[i] + mx + Lx,
                    ] += L_patch

                # Add targets in lower left half
                tr = i - int(np.minimum(len(idx_x), len(idx_y)) / 2)
                tc = j
                if (tr, tc) == target_idx_intensity1 or (tr, tc) in target_idx_intensity1:
                    img[
                        idx_y[i] + ny : idx_y[i] + ny + Ly,
                        idx_x[i] + mx : idx_x[i] + mx + Lx,
                    ] += tpatch1
                    mask[
                        idx_y[i] + ny : idx_y[i] + ny + Ly,
                        idx_x[i] + mx : idx_x[i] + mx + Lx,
                    ] += mpatch1
                if (tr, tc) == target_idx_intensity2 or (tr, tc) in target_idx_intensity2:
                    img[
                        idx_y[i] + ny + Lw : idx_y[i] + ny + Ly + Lw,
                        idx_x[i] + mx : idx_x[i] + mx + Lx,
                    ] += tpatch2
                    mask[
                        idx_y[i] + ny + Lw : idx_y[i] + ny + Ly + Lw,
                        idx_x[i] + mx : idx_x[i] + mx + Lx,
                    ] += mpatch2

            if idx_y[i] + my >= 0 and idx_x[i] + nx >= 0 and j > 0:
                # Add grid in upper right half
                if idx_y[i] + my < height - Ly and idx_x[i] + nx < width - Lx:
                    img[
                        idx_y[i] + my : idx_y[i] + my + Ly,
                        idx_x[i] + nx : idx_x[i] + nx + Lx,
                    ] += L_patch

                # Add targets in upper right half
                if (tr, -tc) == target_idx_intensity1 or (tr, -tc) in target_idx_intensity1:
                    img[
                        idx_y[i] + my : idx_y[i] + my + Ly,
                        idx_x[i] + nx : idx_x[i] + nx + Lx,
                    ] += tpatch1
                    mask[
                        idx_y[i] + my : idx_y[i] + my + Ly,
                        idx_x[i] + nx : idx_x[i] + nx + Lx,
                    ] += mpatch1
                if (tr, -tc) == target_idx_intensity2 or (tr, -tc) in target_idx_intensity2:
                    img[
                        idx_y[i] + my + Lw : idx_y[i] + my + Ly + Lw,
                        idx_x[i] + nx : idx_x[i] + nx + Lx,
                    ] += tpatch2
                    mask[
                        idx_y[i] + my + Lw : idx_y[i] + my + Ly + Lw,
                        idx_x[i] + nx : idx_x[i] + nx + Lx,
                    ] += mpatch2

    # Crop to relevant size
    img = img[Lywd : Lywd + int(Lywd * nL[0]), Lxwd : Lxwd + int(Lxwd * nL[1])]
    mask = mask[Lywd : Lywd + int(Lywd * nL[0]), Lxwd : Lxwd + int(Lxwd * nL[1])]
    return {"img": img, "mask": mask}


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    from stimuli.utils import plot_stimuli

    stims = {
        "Wedding cake stimulus": wedding_cake_stimulus(),
    }

    plot_stimuli(stims, mask=False)
    plt.show()
