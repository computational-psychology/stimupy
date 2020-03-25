# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 13:08:01 2020

@author: max
"""
import numpy as np
import matplotlib.pyplot as plt


class TextureFactory(object):
    """
    A factory to generate simple patterns with variable transparency circles.
    Example Usage:
    >>> f_c = TextureFactory('checkerboard', 10, image_width=200)
    >>> img_c = f_c.get_image(.5, .25, bg_luminance=.5)
    >>> f_r = TextureFactory('random', 2, image_width=200)
    >>> img_r = f_r.get_image(1, .5)

    Parameters
    ----------
    mode : {'random', 'checkerboard'}
        random: A texture where the luminance value of each block is uniformly drawn from the given luminance_values.
        checkerboard: An alternating pattern of blocks with the given luminance_values.
    block_width : int
        Determines the "granularity" of the texture.
    luminance_values : tuple[float], optional
    image_width : int, optional
    """
    def __init__(self, mode, block_width, luminance_values=(0., 1.), image_width=480):
        self.image_width = image_width

        if mode == 'random':
            n_blocks = int(np.ceil(image_width / block_width))
            r = np.random.choice(luminance_values, (n_blocks, n_blocks))
            t = np.repeat(np.repeat(r, block_width, axis=0), block_width, axis=1)
            self.texture = t[:image_width, :image_width]
        elif mode == 'checkerboard':
            self.texture = np.ndarray((image_width, image_width))
            for i, j in np.ndindex((image_width, image_width)):
                x = (i // block_width) % 2
                y = (j // block_width) % 2
                self.texture[i, j] = luminance_values[0] if x == y else luminance_values[1]
        else:
            raise ValueError("invalid mode")

    def get_image(self, tau, alpha, circle_radius=150, bg_luminance=None, stack_option='none'):
        """
        Adds the transparency circle and optionally a cutout background, and returns the image.
        Underlying texture remains unchanged for reuse.

        Parameters
        ----------
        tau, alpha: float
            alpha blending params of transparency circle.
        circle_radius : int, optional
        bg_luminance : float or None, optional
            If None, it renders transparency against the texture.
            If not None, the circle is cut out and set against a background with the given luminance.
        stack_option : {'none', 'horizontal', 'vertical', 'both'}, optional
            If set to something other than 'none', the image is computed twice:
            once with given bg_luminance and once with bg_luminance=None;
            the two results are then stacked vertically, horizontally, or both.
            Note that the dimensions of the image will differ from the specified image_width.

        Returns
        -------
        np.ndarray
            Grayscale image as a square matrix with values between 0 and 1.
        """
        image = self.texture.copy()

        # compute distances from image center (=radius) of each pixel
        x = np.linspace(-0.5 * self.image_width, 0.5 * self.image_width, self.image_width)
        radii = np.sqrt((x ** 2)[np.newaxis] + (x ** 2)[:, np.newaxis])

        # add transparent circle
        idx = radii <= circle_radius
        image[idx] = alpha * image[idx] + (1 - alpha) * tau

        before_cutout = image.copy()

        # cut out center and fill in background
        if bg_luminance is not None:
            idx = radii > circle_radius
            image[idx] = bg_luminance

        if stack_option == 'none':
            return image
        elif stack_option == 'horizontal':
            return np.block([before_cutout, image])
        elif stack_option == 'vertical':
            return np.block([[before_cutout], [image]])
        elif stack_option == 'both':
            return np.block([[before_cutout, image], [image, before_cutout]])
        else:
            raise ValueError('Invalid value given for stack_option.')


def main():
    # compute texture with n-dimensional checkerboard pattern
    n = 10
    image_width = 480
    block_width = image_width // n
    f = TextureFactory('checkerboard', block_width, image_width=image_width)

    # add a transparent circle layer to the image
    tau = .5
    alpha = .25
    img1 = f.get_image(tau, alpha)
    # cut out the circle and set it against a background of given luminance
    img2 = f.get_image(tau, alpha, bg_luminance=.5)

    plt.figure()
    plt.imshow(img1, cmap='gray', vmin=0, vmax=1)
    plt.show()
    plt.figure()
    plt.imshow(img2, cmap='gray', vmin=0, vmax=1)
    plt.show()

    # compute random texture of blocks with given size
    block_width = 10
    f = TextureFactory('random', block_width, image_width=image_width)
    # get a comparable stacked version of original and cutout
    img = f.get_image(1, .5, bg_luminance=.5, stack_option='horizontal')

    plt.figure()
    plt.imshow(img, cmap='gray', vmin=0, vmax=1)
    plt.show()


if __name__ == "__main__":
    main()
