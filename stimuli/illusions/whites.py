import numpy as np
import stimuli
import matplotlib.pyplot as plt
from stimuli.utils import degrees_to_pixels, pad_img

def white(shape=(10,10), ppd=50, frequency=0.5, high=1.0, low=0.0, target=0.5, period='ignore', start='high', target_indices=(2,5),
                target_height=None, targets_offset=0, orientation = 'horizontal', padding=(2,2,2,2)):

    height_px, width_px = degrees_to_pixels(shape, ppd)

    if target_height is None:
        target_height_px = degrees_to_pixels(shape[1]/3, ppd)
    else:
        target_height_px = degrees_to_pixels(target_height, ppd)

    img, pixels_per_cycle = stimuli.illusions.square_wave(shape, ppd, frequency, high, low, period, start)
    mask = np.zeros((height_px, width_px))

    height, width = img.shape
    phase_width = pixels_per_cycle //2
    y_start = height//2 - target_height_px//2 - targets_offset
    y_end = y_start + target_height_px

    for index in target_indices:
        x_start = index*phase_width
        x_end = x_start+phase_width
        img[y_start:y_end, x_start:x_end] = target
        mask[y_start:y_end, x_start:x_end] = True

    if orientation == 'vertical':
        img = np.rot90(img, 3)
        mask = np.rot90(mask, 3)

    img = pad_img(img, padding, ppd, target)
    mask = pad_img(mask, padding, ppd, 0)

    return (img, mask)



def circular_white(radius=5, ppd=50, frequency=1, high=1., low=0., target=.5, target_indices=(2,5), start='low', padding=(2,2,2,2)):
    """
    frequency: cycles per degree
    """

    height, width = (degrees_to_pixels(radius*2, ppd),)*2
    pixels_per_cycle = degrees_to_pixels(1. / (frequency*2) , ppd) * 2
    circle_width = pixels_per_cycle//2
    n_cycles = (max(height, width))//(circle_width*2)

    st = low if start == 'low' else high
    other = high if start == 'low' else low
    img = np.ones((height, width))*target
    mask = np.zeros((height, width))

    for i in range(0, n_cycles):
        radius = circle_width*i
        annulus_mask = stimuli.utils.get_annulus_mask((height, width), (height//2, width//2), radius, radius+circle_width-1)
        img[annulus_mask] = st if i%2==0 else other
        if i in target_indices:
            img[annulus_mask] = target
            mask[annulus_mask] = True
        else:
            img[annulus_mask] = st if i % 2 == 0 else other

    img = pad_img(img, padding, ppd, target)
    mask = pad_img(mask, padding, ppd, 0)

    return (img, mask)


def wheel_of_fortune_white(radius=10, ppd=50, n_cycles=5, target_width=0.7, target_indices=None, angle_shift=0, high=1.0, low=0., target=.5, start='high', padding=(1,1,1,1)):
    #TODO: make this faster

    # Inputs:
    #   - n_parts: number of black and white parts within circle (int), it
    #              should be even numbered to avoid asymmetry
    #   - target_width: relative width of the targets between 0 and 1 (float)

    # Decide on resolution for the grid.
    # The lower the resolution, the worse the wheel of fortune will look


    n_parts=n_cycles*2
    n_grid = stimuli.utils.degrees_to_pixels(radius, ppd)*2
    n_numbers = n_grid*2

    if target_indices is None:
        target_indices = (0, n_parts // 2)

    # Create a circle
    x = np.linspace(0, 2*np.pi, int(n_numbers))

    xx = np.cos(x)
    xx_min = np.abs(xx.min())
    xx += xx_min
    xx_max = xx.max()
    xx = xx / xx_max * (n_grid-1)

    yy = np.sin(x)
    yy_min = np.abs(yy.min())
    yy += yy_min
    yy_max = yy.max()
    yy = yy / yy_max * (n_grid-1)

    img = np.zeros([n_grid, n_grid]) + 0.5
    mask = np.zeros([n_grid, n_grid])

    st = high if start=='high' else low
    other = low if start=='high' else high

    # Divide circle in n_parts parts:
    x = np.linspace(0+angle_shift, 2*np.pi+angle_shift, int(n_parts+1))

    for i in range(len(x)-1):
        xxx = np.linspace(x[i], x[i+1], int(n_numbers))
        xxxx = np.cos(xxx)
        xxxx += xx_min
        xxxx = xxxx / xx_max * (n_grid-1)

        yyyy = np.sin(xxx)
        yyyy += yy_min
        yyyy = yyyy / yy_max * (n_grid-1)

        for j in range(int(n_numbers)):
            sep_x = np.linspace(n_grid/2, xxxx[j], int(n_numbers))
            sep_y = np.linspace(n_grid/2, yyyy[j], int(n_numbers))
            # Switch between bright and dark areas:
            if i % 2 == 0:
                img[sep_x.astype(int), sep_y.astype(int)] = st
            else:
                img[sep_x.astype(int), sep_y.astype(int)] = other

            if i in target_indices:
                # Place a single target inside the area
                img[sep_x[int(n_numbers * (0.5 - target_width / 2)):int(n_numbers * (0.5 + target_width / 2))].astype(int),
                     sep_y[int(n_numbers * (0.5 - target_width / 2)):int(n_numbers * (0.5 + target_width / 2))].astype(int)] = 0.5

                mask[sep_x[int(n_numbers * (0.5 - target_width / 2)):int(n_numbers * (0.5 + target_width / 2))].astype(int),
                    sep_y[int(n_numbers * (0.5 - target_width / 2)):int(n_numbers * (0.5 + target_width / 2))].astype(int)] = True

    img = pad_img(img, padding, ppd, target)
    mask = pad_img(mask, padding, ppd, 0)

    return (img, mask)


def white_anderson(shape=(5,5), ppd=40, frequency=2, height_bars=1, height_horizontal_top=1, target_height=1, target_indices_top=(5,), target_offsets_top=(0.5,),
                   target_indices_bottom=(12,), target_offsets_bottom=(-0.5,), high=1., low=0., target=.5, top='low', padding=(1,1,1,1)):

    height, width = degrees_to_pixels(shape, ppd)
    pixels_per_cycle = degrees_to_pixels(1. / (frequency*2) , ppd) * 2
    height_bars, height_horizontal_top = degrees_to_pixels(height_bars, ppd), degrees_to_pixels(height_horizontal_top, ppd)
    spacing_bottom = height - 3*height_bars - height_horizontal_top

    top = low if top=='low' else high
    bottom = high if top==low else low

    img = np.ones((height, width))*bottom
    mask = np.zeros((height, width))

    index = [i + j for i in range(pixels_per_cycle // 2)
             for j in range(0, width, pixels_per_cycle)
             if i + j < width]

    img[:height_bars*2 + height_horizontal_top, index] = top
    img[-height_bars:, index] = top
    img[height_bars:height_bars+height_horizontal_top,:] = top

    target_height = stimuli.utils.degrees_to_pixels(target_height, ppd)
    target_offsets_top = tuple(stimuli.utils.degrees_to_pixels(x, ppd) for x in target_offsets_top)
    target_offsets_bottom = tuple(stimuli.utils.degrees_to_pixels(x, ppd) for x in target_offsets_bottom)


    for i, ind in enumerate(target_indices_top):
        st = int(pixels_per_cycle/2 * ind)
        end = int(st + pixels_per_cycle/2)
        img[:height_bars*2+height_horizontal_top,st:end] = bottom
        offset = target_offsets_top[i]
        target_start = height_bars + (height_horizontal_top-target_height)//2 + offset
        target_end = target_start + target_height
        img[target_start:target_end, st:end] = target
        mask[target_start:target_end, st:end] = True

    for i, ind in enumerate(target_indices_bottom):
        st = int(pixels_per_cycle/2 * ind)
        end = int(st + pixels_per_cycle/2)
        img[height_bars+height_horizontal_top:,st:end] = top
        offset = target_offsets_bottom[i]
        target_start = -height_bars - spacing_bottom + offset
        target_end = target_start + target_height
        img[target_start:target_end, st:end] = target
        mask[target_start:target_end, st:end] = True

    img = pad_img(img, padding, ppd, target)
    mask = pad_img(mask, padding, ppd, 0)
    return (img, mask)

def RHS2007_WE_thick():
    total_height, total_width, ppd = (32,)*3
    height, width = 12, 16
    n_cycles = 4
    frequency = n_cycles / width
    padding_horizontal = (total_width - width) / 2
    padding_vertical = (total_height - height) / 2
    padding = (padding_vertical, padding_vertical, padding_horizontal, padding_horizontal)
    target_height = stimuli.utils.degrees_to_pixels(4, ppd)
    img = stimuli.illusions.whites.white(shape=(height, width), ppd=ppd, frequency=frequency, start='low', target_indices=(2, 5), padding=padding, target_height=target_height)
    return img

def RHS2007_WE_thin_wide():
    total_height, total_width, ppd = (32,)*3
    height, width = 12, 16
    n_cycles = 8
    frequency = n_cycles / width
    padding_horizontal = (total_width - width) / 2
    padding_vertical = (total_height - height) / 2
    padding = (padding_vertical, padding_vertical, padding_horizontal, padding_horizontal)
    target_height = stimuli.utils.degrees_to_pixels(4, ppd)
    img = stimuli.illusions.whites.white(shape=(height, width), ppd=ppd, frequency=frequency, start='low', target_indices=(3, 12), padding=padding, target_height=target_height)
    return img

def RHS2007_WE_dual():
    total_height, total_width, ppd = (32,)*3
    height, width = 6, 8
    n_cycles = 4
    frequency = n_cycles / width

    padding_horizontal1, padding_vertical1 = (total_width / 2 - width) / 2, (total_height - height) / 2
    padding1 = (padding_vertical1, padding_vertical1, padding_horizontal1, padding_horizontal1)
    padding_horizontal2, padding_vertical2 = (total_width / 2 - height) / 2, (total_height - width) / 2
    padding2 = (padding_vertical2, padding_vertical2, padding_horizontal2, padding_horizontal2)

    target_height = stimuli.utils.degrees_to_pixels(2, ppd)
    img1 = stimuli.illusions.whites.white(shape=(height, width), ppd=ppd, frequency=frequency, start='low', target_indices=(2, 5), padding=padding1, target_height=target_height)
    img2 = stimuli.illusions.whites.white(shape=(height, width), ppd=ppd, frequency=frequency, start='low', target_indices=(2, 5), padding=padding2, target_height=target_height, orientation='vertical')
    img = np.hstack((img1, img2))
    return img

def RHS2007_WE_anderson():
    total_height, total_width, ppd = (32,)*3
    height, width = 16, 16
    n_cycles = 8
    frequency = n_cycles / width
    height_bars = height / 5
    height_horizontal = height_bars
    target_height = height_bars
    padding_horizontal = (total_width - width) / 2
    padding_vertical = (total_height - height) / 2
    padding = (padding_vertical, padding_vertical, padding_horizontal, padding_horizontal)
    img = stimuli.illusions.whites.white_anderson(shape=(height, width), ppd=ppd, frequency=frequency, target_height=target_height,
                                                  target_indices_top=(5,), target_offsets_top=(target_height / 2,), target_indices_bottom=(10,), target_offsets_bottom=(-target_height / 2,),
                                                  height_bars=height_bars, height_horizontal_top=height_horizontal, padding=padding)
    return img

def RHS2007_WE_howe():
    total_height, total_width, ppd = (32,)*3
    height, width = 16, 16
    n_cycles = 8
    frequency = n_cycles / width
    height_bars = height / 5
    height_horizontal = height_bars
    target_height = height_bars
    padding_horizontal = (total_width - width) / 2
    padding_vertical = (total_height - height) / 2
    padding = (padding_vertical, padding_vertical, padding_horizontal, padding_horizontal)
    img = stimuli.illusions.whites.white_anderson(shape=(height, width), ppd=ppd, frequency=frequency, target_height=target_height,
                                                  target_indices_top=(5,), target_offsets_top=(0,), target_indices_bottom=(10,), target_offsets_bottom=(0,),
                                                  height_bars=height_bars, height_horizontal_top=height_horizontal, padding=padding)
    return img

def RHS2007_WE_radial_thick_small():
    total_height, total_width, ppd = (32,)*3
    radius = 8
    padding = ((total_width - 2 * radius) / 2,) * 4
    n_cycles = 7
    img = stimuli.illusions.whites.wheel_of_fortune_white(radius=radius, ppd=ppd, n_cycles=n_cycles, angle_shift=np.pi / n_cycles / 2, target_indices=(n_cycles - 1, 2 * n_cycles - 1), target_width=0.5, padding=padding)
    return img

def RHS2007_WE_radial_thick():
    total_height, total_width, ppd = (32,)*3
    radius = 12
    padding = ((total_width - 2 * radius) / 2,) * 4
    n_cycles = 9
    img = stimuli.illusions.whites.wheel_of_fortune_white(radius=radius, ppd=ppd, n_cycles=n_cycles, angle_shift=np.pi / n_cycles / 2, target_indices=(n_cycles - 1, 2 * n_cycles - 1), target_width=0.5, padding=padding)
    return img

def RHS2007_WE_radial_thin_small():
    total_height, total_width, ppd = (32,)*3
    radius = 8
    padding = ((total_width - 2 * radius) / 2,) * 4
    n_cycles = 13
    img = stimuli.illusions.whites.wheel_of_fortune_white(radius=radius, ppd=ppd, n_cycles=n_cycles, angle_shift=np.pi / n_cycles / 2, target_indices=(n_cycles - 1, 2 * n_cycles - 1), target_width=0.5, padding=padding)
    return img

def RHS2007_WE_radial_thin():
    total_height, total_width, ppd = (32,)*3
    radius = 12
    padding = ((total_width - 2 * radius) / 2,) * 4
    n_cycles = 21
    img = stimuli.illusions.whites.wheel_of_fortune_white(radius=radius, ppd=ppd, n_cycles=n_cycles, angle_shift=np.pi / n_cycles / 2, target_indices=(n_cycles - 1, 2 * n_cycles - 1), target_width=0.5, padding=padding)
    return img

def RHS2007_WE_circular1():
    total_height, total_width, ppd = (32,)*3
    radius = 8
    n_cycles = 4
    frequency = n_cycles / radius
    padding_vertical = (total_height - 2 * radius) / 2
    padding = (padding_vertical, padding_vertical, 0, 0)
    img1 = stimuli.illusions.whites.circular_white(radius=radius, ppd=ppd, frequency=frequency, target_indices=(4,), start='high', padding=padding)
    img2 = stimuli.illusions.whites.circular_white(radius=radius, ppd=ppd, frequency=frequency, target_indices=(4,), start='low', padding=padding)
    img = np.hstack((img1, img2))
    return img

def RHS2007_WE_circular05():
    total_height, total_width, ppd = (32,)*3
    radius = 8
    n_cycles = 8
    frequency = n_cycles / radius
    padding_vertical = (total_height - 2 * radius) / 2
    padding = (padding_vertical, padding_vertical, 0, 0)
    img1 = stimuli.illusions.whites.circular_white(radius=radius, ppd=ppd, frequency=frequency, target_indices=(4,), start='high', padding=padding)
    img2 = stimuli.illusions.whites.circular_white(radius=radius, ppd=ppd, frequency=frequency, target_indices=(4,), start='low', padding=padding)
    img = np.hstack((img1, img2))
    return img

def RHS2007_WE_circular025():
    total_height, total_width, ppd = (32,)*3
    radius = 8
    n_cycles = 16
    frequency = n_cycles / radius
    padding_vertical = (total_height - 2 * radius) / 2
    padding = (padding_vertical, padding_vertical, 0, 0)
    img1 = stimuli.illusions.whites.circular_white(radius=radius, ppd=ppd, frequency=frequency, target_indices=(4,), start='high', padding=padding)
    img2 = stimuli.illusions.whites.circular_white(radius=radius, ppd=ppd, frequency=frequency, target_indices=(4,), start='low', padding=padding)
    img = np.hstack((img1, img2))
    return img

def domijan2015_white():
    height, width, ppd = 8.1, 8., 10
    n_cycles = 4
    frequency = n_cycles/width
    return white(shape=(height, width), ppd=ppd, frequency=frequency, high=9., low=1., target=5., period='ignore', start='low',
                 target_indices=(2,5), target_height=2.1, targets_offset=0, orientation='horizontal', padding=(.9, 1., .9, 1.1))



if __name__ == '__main__':
    import matplotlib.pyplot as plt

    img, mask = white()
    plt.subplot(4,2,1)
    plt.imshow(img, cmap='gray')
    plt.subplot(4,2,2)
    plt.imshow(mask, cmap='gray')

    img, mask = circular_white()
    plt.subplot(4, 2, 3)
    plt.imshow(img, cmap='gray')
    plt.subplot(4, 2, 4)
    plt.imshow(mask, cmap='gray')

    img, mask = wheel_of_fortune_white()
    plt.subplot(4, 2, 5)
    plt.imshow(img, cmap='gray')
    plt.subplot(4, 2, 6)
    plt.imshow(mask, cmap='gray')

    img, mask = white_anderson()
    plt.subplot(4, 2, 7)
    plt.imshow(img, cmap='gray')
    plt.subplot(4, 2, 8)
    plt.imshow(mask, cmap='gray')

    plt.tight_layout()
    plt.show()
