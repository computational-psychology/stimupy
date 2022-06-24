import numpy as np
from stimuli.components import square_wave
from stimuli.utils import degrees_to_pixels, get_annulus_mask


def white(
    shape=(10, 10),
    ppd=50,
    frequency=0.4,
    high=1.0,
    low=0.0,
    target=0.5,
    period="ignore",
    start="low",
    target_indices=(2, -3),
    target_height=None,
    targets_offset=0,
    orientation="horizontal",
):
    """
    Whites's illusion

    Parameters
    ----------
    shape : (float, float)
        The shape of the illustion in degrees of visual angle (height, width)
    ppd : int
        pixels per degree (visual angle)
    frequency : float
        frequency of the grid in cycles per degree visual angle
    high : float
        value of the bright stripes
    low : float
        value of the dark stripes
    target : float
        value for target
    period : string in ['ignore', 'full', 'half']
        see square_wave.py for details about this
    start : string in ['low','high']
        whether to start with a bright or a low stripes
    target_indices : (int, )
        indices of the stripes where the target(s) will be placed. There will be as many targets as indices specified.
    target_height : float
        height of the target in degrees visual angle. If it's None, the target will be 1/3 of the illusion height
    targets_offset : int
        Vertical offset of the target in pixels
    orientation : string in ['horizontal', 'vertical']
        orientation of the illusion

    Returns
    -------
    A stimulus object
    """

    height_px, width_px = degrees_to_pixels(shape, ppd)

    if target_height is None:
        target_height_px = degrees_to_pixels(shape[1] / 3, ppd)
    else:
        target_height_px = degrees_to_pixels(target_height, ppd)

    img, pixels_per_cycle = square_wave(
        shape, ppd, frequency, high, low, period, start
    )
    mask = np.zeros((height_px, width_px))

    height, width = img.shape
    phase_width = pixels_per_cycle // 2
    y_start = height // 2 - target_height_px // 2 - targets_offset
    y_end = y_start + target_height_px

    for i, index in enumerate(target_indices):
        if index >= 0:
            x_start = (index - 1) * phase_width
        else:
            # Calculate the number of phases based on resolution of grating:
            phases = int(2 * (int(shape[1] * ppd / phase_width) // 2))
            x_start = int((phases + index) * phase_width)
        x_end = x_start + phase_width
        img[y_start:y_end, x_start:x_end] = target
        mask[y_start:y_end, x_start:x_end] = i + 1.0

    if orientation == "vertical":
        img = np.rot90(img, 3)
        mask = np.rot90(mask, 3)

    return {"img": img, "mask": mask}


def circular_white(
    radius=5,
    ppd=50,
    frequency=1.0,
    high=1.0,
    low=0.0,
    target=0.5,
    target_indices=(2, 6),
    start="low",
):
    """
    Circular Whites's illusion

    Parameters
    ----------
    radius : float
        radius of the circle in degrees visual angle
    ppd : int
        pixels per degree (visual angle)
    frequency : float
        frequency of the circles in cycles per degree visual angle
    high : float
        value of the bright stripes
    low : float
        value of the dark stripes
    target : float
        value for target
    target_indices : (int, )
        indices of the stripes where the target(s) will be placed. There will be as many targets as indices specified.
    start : string in ['low','high']
        whether to start with a bright or a low stripes

    Returns
    ----------
    A stimulus object
    """

    height, width = (degrees_to_pixels(radius * 2, ppd),) * 2
    pixels_per_cycle = degrees_to_pixels(1.0 / (frequency * 2), ppd) * 2
    circle_width = pixels_per_cycle // 2
    n_cycles = (max(height, width)) // (circle_width * 2)

    st = low if start == "low" else high
    other = high if start == "low" else low
    img = np.ones((height, width)) * target
    mask = np.zeros((height, width))

    mask_counter = 1
    for i in range(0, n_cycles):
        radius = circle_width * i
        annulus_mask = get_annulus_mask(
            (height, width),
            (height // 2, width // 2),
            radius,
            radius + circle_width,
        )
        img[annulus_mask] = st if i % 2 == 0 else other
        if i in target_indices:
            img[annulus_mask] = target
            mask[annulus_mask] = mask_counter
            mask_counter += 1
        else:
            img[annulus_mask] = st if i % 2 == 0 else other

    return {"img": img, "mask": mask}


def wheel_of_fortune_white(
    radius=10,
    ppd=50,
    n_cycles=5,
    target_width=0.7,
    target_indices=None,
    target_start=0.5,
    angle_shift=0,
    high=1.0,
    low=0.0,
    target=0.5,
    start="high",
):
    # TODO: make this faster
    """
    Wheel of fortune Whites's illusion

    Parameters
    ----------
    radius : float
        radius of the circle in degrees visual angle
    ppd : int
        pixels per degree (visual angle)
    n_cycles : int
        number of full grid cycles in the circle
    target_width :  float in interval [0,1]
        width of the target, 1 means target goes from center all the way to the edge of the circle
    target_indices : (int, )
        indices of the stripes where the target(s) will be placed
    target_start : float in interval [0,1]
        specify where the target starts relative to the radius
    angle_shift : float
        rotate the circle for specified amount of radians
    high : float
        value of the bright stripes
    low : float
        value of the dark stripes
    target : float
        value for target
    start : string in ['low','high']
        whether to start with a bright or a low stripes

    Returns
    ----------
    A stimulus object
    """

    n_parts = n_cycles * 2
    n_grid = degrees_to_pixels(radius, ppd) * 2
    n_numbers = n_grid * 2

    if target_indices is None:
        target_indices = (0, n_parts // 2)

    # Create a circle
    x = np.linspace(0, 2 * np.pi, int(n_numbers))

    xx = np.cos(x)
    xx_min = np.abs(xx.min())
    xx += xx_min
    xx_max = xx.max()
    xx = xx / xx_max * (n_grid - 1)

    yy = np.sin(x)
    yy_min = np.abs(yy.min())
    yy += yy_min
    yy_max = yy.max()
    yy = yy / yy_max * (n_grid - 1)

    img = np.zeros([n_grid, n_grid]) + 0.5
    mask = np.zeros([n_grid, n_grid])

    st = high if start == "high" else low
    other = low if start == "high" else high

    # Divide circle in n_parts parts:
    x = np.linspace(0 + angle_shift, 2 * np.pi + angle_shift, int(n_parts + 1))

    mask_counter = 1
    for i in range(len(x) - 1):
        xxx = np.linspace(x[i], x[i + 1], int(n_numbers))
        xxxx = np.cos(xxx)
        xxxx += xx_min
        xxxx = xxxx / xx_max * (n_grid - 1)

        yyyy = np.sin(xxx)
        yyyy += yy_min
        yyyy = yyyy / yy_max * (n_grid - 1)

        for j in range(int(n_numbers)):
            sep_x = np.linspace(n_grid / 2, xxxx[j], int(n_numbers))
            sep_y = np.linspace(n_grid / 2, yyyy[j], int(n_numbers))
            # Switch between bright and dark areas:
            if i % 2 == 0:
                img[sep_x.astype(int), sep_y.astype(int)] = st
            else:
                img[sep_x.astype(int), sep_y.astype(int)] = other

            if i in target_indices:
                # Place a single target inside the area
                img[
                    sep_x[
                        int(
                            n_numbers * (target_start - target_width / 2)
                        ) : int(n_numbers * (target_start + target_width / 2))
                    ].astype(int),
                    sep_y[
                        int(
                            n_numbers * (target_start - target_width / 2)
                        ) : int(n_numbers * (target_start + target_width / 2))
                    ].astype(int),
                ] = target

                mask[
                    sep_x[
                        int(
                            n_numbers * (target_start - target_width / 2)
                        ) : int(n_numbers * (target_start + target_width / 2))
                    ].astype(int),
                    sep_y[
                        int(
                            n_numbers * (target_start - target_width / 2)
                        ) : int(n_numbers * (target_start + target_width / 2))
                    ].astype(int),
                ] = mask_counter
        mask_counter += 1

    mask_vals = np.unique(mask)
    mask_vals = mask_vals[1:]
    for i, val in enumerate(mask_vals):
        mask[mask == val] = i + 1

    return {"img": img, "mask": mask}


def white_anderson(
    shape=(5, 5),
    ppd=40,
    frequency=2,
    stripe_height=1,
    stripe_ypos=(1, 3),
    target_height=1,
    target_indices_top=(5,),
    target_offsets_top=(0.5,),
    target_indices_bottom=(12,),
    target_offsets_bottom=(-0.5,),
    vbars=(1.0, 0.0),
    vtarget=0.5,
    vtopstripe=1.0,
    vbotstripe=0.0,
):
    """
    Anderson's White stimulus

    Parameters
    ----------
    shape : (float, float)
        The shape of the illustion in degrees of visual angle (height, width)
    ppd : int
        pixels per degree (visual angle)
    frequency : float
        frequency of the grid in cycles per degree visual angle
    stripe_height : float
        height of the stripes in degrees visual angle
    stripe_ypos : (float, float)
        y coordinate of top and bottom stripe
    target_height : float
        target height in degrees visual angle
    target_indices_top : (int, )
        bar indices where the top target(s) will be placed
    target_offsets_top : (float, )
        vertical offsets of top targets
    target_indices_bottom : (int, )
        bar indices where the bottom target(s) will be placed
    target_offsets_bottom : (float, )
        vertical offsets of bottom targets
    vbars : (float, float)
        values of grating bars
    vtarget : float
        value for target
    vtopstripe : float
        value of top stripe
    vbotstripe : float
        value of bottom stripe

    Returns
    -------
    A stimulus dictionary with the stimulus ['img'] and target mask ['mask']
    """
    height, width = degrees_to_pixels(shape, ppd)
    pixels_per_cycle = degrees_to_pixels(1.0 / (frequency * 2), ppd) * 2
    stripe_ypos = degrees_to_pixels(stripe_ypos, ppd).astype(int)
    stripe_height = degrees_to_pixels(stripe_height, ppd)

    img = np.ones((height, width)) * vbars[1]
    mask = np.zeros((height, width))

    index = [
        i + j
        for i in range(pixels_per_cycle // 2)
        for j in range(0, width, pixels_per_cycle)
        if i + j < width
    ]

    # Create grating and add top and bottom stripes
    img[:, index] = vbars[0]
    img[stripe_ypos[0] : stripe_ypos[0] + stripe_height, :] = vtopstripe
    img[stripe_ypos[1] : stripe_ypos[1] + stripe_height, :] = vbotstripe

    target_height = degrees_to_pixels(target_height, ppd)
    target_offsets_top = tuple(
        degrees_to_pixels(x, ppd) for x in target_offsets_top
    )
    target_offsets_bottom = tuple(
        degrees_to_pixels(x, ppd) for x in target_offsets_bottom
    )

    # Add top targets
    for i, ind in enumerate(target_indices_top):
        st = int(pixels_per_cycle / 2 * ind)
        end = int(st + pixels_per_cycle / 2)
        img[0 : stripe_ypos[1] :, st:end] = vbotstripe
        offset = target_offsets_top[i]
        target_start = (
            stripe_ypos[0] + (stripe_height - target_height) // 2 + offset
        )
        target_end = target_start + target_height
        img[target_start:target_end, st:end] = vtarget
        mask[target_start:target_end, st:end] = 1

    # Add bottom targets
    for i, ind in enumerate(target_indices_bottom):
        st = int(pixels_per_cycle / 2 * ind)
        end = int(st + pixels_per_cycle / 2)
        img[stripe_ypos[0] + stripe_height : :, st:end] = vtopstripe
        offset = target_offsets_bottom[i]
        target_start = stripe_ypos[1] + offset
        target_end = target_start + target_height
        img[target_start:target_end, st:end] = vtarget
        mask[target_start:target_end, st:end] = 2
    return {"img": img, "mask": mask}


def white_howe(
    shape=(5, 5),
    ppd=40,
    frequency=2,
    stripe_height=1,
    stripe_ypos=(1, 3),
    target_height=1,
    target_indices_top=(5,),
    target_indices_bottom=(12,),
    vbars=(1.0, 0.0),
    vtarget=0.5,
    vtopstripe=1.0,
    vbotstripe=0.0,
):
    """
    Howe's White stimulus

    Parameters
    ----------
    shape : (float, float)
        The shape of the illustion in degrees of visual angle (height, width)
    ppd : int
        pixels per degree (visual angle)
    frequency : float
        frequency of the grid in cycles per degree visual angle
    stripe_height : float
        height of the stripes in degrees visual angle
    stripe_ypos : (float, float)
        y coordinate of top and bottom stripe
    target_height : float
        target height in degrees visual angle
    target_indices_top : (int, )
        bar indices where the top target(s) will be placed
    target_indices_bottom : (int, )
        bar indices where the bottom target(s) will be placed
    vbars : (float, float)
        values of grating bars
    vtarget : float
        value for target
    vtopstripe : float
        value of top stripe
    vbotstripe : float
        value of bottom stripe

    Returns
    -------
    A stimulus dictionary with the stimulus ['img'] and target mask ['mask']
    """
    return white_anderson(
        shape=shape,
        ppd=ppd,
        frequency=frequency,
        stripe_height=stripe_height,
        stripe_ypos=stripe_ypos,
        target_height=target_height,
        target_indices_top=target_indices_top,
        target_offsets_top=np.zeros(len(target_indices_top)),
        target_indices_bottom=target_indices_bottom,
        target_offsets_bottom=np.zeros(len(target_indices_bottom)),
        vbars=vbars,
        vtarget=vtarget,
        vtopstripe=vtopstripe,
        vbotstripe=vbotstripe,
    )


def white_yazdanbakhsh(
    shape=(5, 5),
    ppd=40,
    frequency=2,
    stripe_height=0.2,
    target_height=1,
    target_indices_top=(5,),
    target_ypos_top=(1.5,),
    target_indices_bottom=(12,),
    target_ypos_bottom=(3.0,),
    vbars=(1.0, 0.0),
    vtarget=0.5,
    vtopstripe=1.0,
    vbotstripe=0.0,
):
    """
    Yazsdanbakhsh's White stimulus

    Parameters
    ----------
    shape : (float, float)
        The shape of the illustion in degrees of visual angle (height, width)
    ppd : int
        pixels per degree (visual angle)
    frequency : float
        frequency of the grid in cycles per degree visual angle
    stripe_height : float
        height of the stripes in degrees visual angle
    target_height : float
        target height in degrees visual angle
    target_indices_top : (int, )
        bar indices where the top target(s) will be placed
    target_ypos_top : (float, )
        y coordinates of top targets
    target_indices_bottom : (int, )
        bar indices where the bottom target(s) will be placed
    target_ypos_bottom : (float, )
        y coordinates of bottom targets
    vbars : (float, float)
        values of grating bars
    vtarget : float
        value for target
    vtopstripe : float
        value of top stripe
    vbotstripe : float
        value of bottom stripe

    Returns
    -------
    A stimulus dictionary with the stimulus ['img'] and target mask ['mask']
    """
    height, width = degrees_to_pixels(shape, ppd)
    pixels_per_cycle = degrees_to_pixels(1.0 / (frequency * 2), ppd) * 2
    stripe_height = degrees_to_pixels(stripe_height, ppd)

    img = np.ones((height, width)) * vbars[1]
    mask = np.zeros((height, width))

    index = [
        i + j
        for i in range(pixels_per_cycle // 2)
        for j in range(0, width, pixels_per_cycle)
        if i + j < width
    ]

    # Create grating
    img[:, index] = vbars[0]

    target_height = degrees_to_pixels(target_height, ppd)
    target_ypos_top = tuple(degrees_to_pixels(x, ppd) for x in target_ypos_top)
    target_ypos_bottom = tuple(
        degrees_to_pixels(x, ppd) for x in target_ypos_bottom
    )

    # Add top targets
    for i, ind in enumerate(target_indices_top):
        st = int(pixels_per_cycle / 2 * ind)
        end = int(st + pixels_per_cycle / 2)
        target_start = target_ypos_top[i]
        target_end = target_start + target_height
        img[target_start - stripe_height : target_start, st:end] = vtopstripe
        img[target_end : target_end + stripe_height, st:end] = vtopstripe
        img[target_start:target_end, st:end] = vtarget
        mask[target_start:target_end, st:end] = 1

    # Add bottom targets
    for i, ind in enumerate(target_indices_bottom):
        st = int(pixels_per_cycle / 2 * ind)
        end = int(st + pixels_per_cycle / 2)
        target_start = target_ypos_bottom[i]
        target_end = target_start + target_height
        img[target_start - stripe_height : target_start, st:end] = vbotstripe
        img[target_end : target_end + stripe_height, st:end] = vbotstripe
        img[target_start:target_end, st:end] = vtarget
        mask[target_start:target_end, st:end] = 2
    return {"img": img, "mask": mask}


def white_zigzag(
    ppd=10,
    L_size=(10.0, 10.0, 2.0),
    L_distance=2.0,
    L_repeats=(3.0, 3.0),
    target_height=4.0,
    target_idx_v1=((-1, 0), (0, 0), (1, 0)),
    target_idx_v2=None,
    v1=0.0,
    v2=1.0,
    vtarget=0.5,
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
    target_idx_v1 : nested tuples
        target indices with v1-value; as many tuples as there are targets each with (y, x) indices;
        (0, 0) places a target in the center
    target_idx_v2 : nested tuples
        target indices with v2-value; as many tuples as there are targets each with (y, x) indices;
        (0, 0) places a target in the center
    v1 : float
        first value for grating
    v2 : float
        second value for grating
    vtarget : float
        value for target(s)

    Returns
    -------
    A stimulus dictionary with the stimulus ['img'] and target mask ['mask']
    """
    Ly, Lx, Lw = degrees_to_pixels(L_size, ppd)
    Ld = degrees_to_pixels(L_distance, ppd)
    Lywd, Lxwd = Ly, Lx
    nL = L_repeats
    theight = degrees_to_pixels(target_height, ppd)

    mval2 = 2
    if target_idx_v1 is None:
        target_idx_v1 = ()
        mval2 = 1
    if target_idx_v2 is None:
        target_idx_v2 = ()

    if len(L_size) != 3:
        raise Exception("L_size needs to have a length of 3")

    if isinstance(nL, (int, float)):
        nL = (nL, nL)
    if np.min(nL) < 2:
        raise Exception("L_repeats should be larger than 1")

    # Create grid patch
    L_patch = np.zeros([Ly, Lx])
    L_patch[0:Lw, 0:Lx] = v1 - v2
    L_patch[0:Ly, Lx - Lw : :] = v1 - v2
    L_patch[0:Lw, 0:Lw] = (v1 - v2) / 2.0
    L_patch[Ly - Lw : :, Lx - Lw : :] = (v1 - v2) / 2.0

    # Create target and mask patch 1
    tpatch1 = np.zeros([Ly, Lx])
    tpatch1[
        int(Ly / 2 - theight / 2) : int(Ly / 2 + theight / 2), Lx - Lw : :
    ] = (vtarget - v1)
    mpatch1 = np.zeros([Ly, Lx])
    mpatch1[
        int(Ly / 2 - theight / 2) : int(Ly / 2 + theight / 2), Lx - Lw : :
    ] = 1

    # Create target and mask patch 2
    tpatch2 = np.zeros([Ly, Lx])
    tpatch2[
        int(Ly / 2 - theight / 2) : int(Ly / 2 + theight / 2),
        Lx - Lw - Ld : Lx - Lw,
    ] = (
        vtarget - v2
    )
    mpatch2 = np.zeros([Ly, Lx])
    mpatch2[
        int(Ly / 2 - theight / 2) : int(Ly / 2 + theight / 2),
        Lx - Lw - Ld : Lx - Lw,
    ] = mval2

    # Create image slightly larger than needed
    img = np.ones([int(Lywd * (nL[0] + 2)), int(Lxwd * (nL[1] + 2))]) * v2
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
                if (tr, tc) == target_idx_v1 or (tr, tc) in target_idx_v1:
                    img[
                        idx_y[i] + ny : idx_y[i] + ny + Ly,
                        idx_x[i] + mx : idx_x[i] + mx + Lx,
                    ] += tpatch1
                    mask[
                        idx_y[i] + ny : idx_y[i] + ny + Ly,
                        idx_x[i] + mx : idx_x[i] + mx + Lx,
                    ] += mpatch1
                if (tr, tc) == target_idx_v2 or (tr, tc) in target_idx_v2:
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
                if (tr, -tc) == target_idx_v1 or (tr, -tc) in target_idx_v1:
                    img[
                        idx_y[i] + my : idx_y[i] + my + Ly,
                        idx_x[i] + nx : idx_x[i] + nx + Lx,
                    ] += tpatch1
                    mask[
                        idx_y[i] + my : idx_y[i] + my + Ly,
                        idx_x[i] + nx : idx_x[i] + nx + Lx,
                    ] += mpatch1
                if (tr, -tc) == target_idx_v2 or (tr, -tc) in target_idx_v2:
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
    mask = mask[
        Lywd : Lywd + int(Lywd * nL[0]), Lxwd : Lxwd + int(Lxwd * nL[1])
    ]
    return {"img": img, "mask": mask}


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    from stimuli.utils import plot_stimuli

    stims = {
        "White's effect": white(),
        "Circular White's effect": circular_white(),
        "Wheel-of-fortune": wheel_of_fortune_white(),
        "Anderson's variation": white_anderson(),
        "Yazdanbakhsh variation": white_yazdanbakhsh(),
        "Howe's variation": white_howe(),
        "Wedding cake illusion": white_zigzag(),
    }

    plot_stimuli(stims)
    plt.show()
