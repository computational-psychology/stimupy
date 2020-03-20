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
    >>> img_c = f_c.get_image(.5, .75, circle_radius=50, bg_luminosity=.5)
    >>> f_r = TextureFactory('random', 2, image_width=200)
    >>> img_r = f_r.get_image(1, .5, circle_radius=50)

    Parameters
    ----------
    mode : {'random', 'checkerboard'}
        random: A texture where the luminosity value of each block is uniformly drawn from the given luminosities.
        checkerboard: An alternating pattern of blocks with the given luminosities.
    block_width : int
        Determines the "granularity" of the texture.
    luminosities : tuple[float], optional
    image_width : int, optional
    """
    def __init__(self, mode, block_width, luminosities=(0., 1.), image_width=480):
        self.image_width = image_width

        if mode == 'random':
            n_blocks = int(np.ceil(image_width / block_width))
            r = np.random.choice(luminosities, (n_blocks, n_blocks))
            t = np.repeat(np.repeat(r, block_width, axis=0), block_width, axis=1)
            self.texture = t[:image_width, :image_width]
        elif mode == 'checkerboard':
            self.texture = np.ndarray((image_width, image_width))
            for i, j in np.ndindex((image_width, image_width)):
                x = (i // block_width) % 2
                y = (j // block_width) % 2
                self.texture[i, j] = luminosities[0] if x == y else luminosities[1]
        else:
            raise ValueError("invalid mode")

    def get_image(self, tau, alpha, circle_radius=150, bg_luminosity=None):
        """
        Adds the transparency circle and optionally a cutout background, and returns the image.
        Underlying texture remains unchanged for reuse.

        Parameters
        ----------
        tau, alpha: float
            alpha blending params of transparency circle.
        circle_radius : int
        bg_luminosity : float or None
            If not None, the circle is cut out and set against the given background luminosity.

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
        image[idx] = (1 - alpha) * image[idx] + alpha * tau

        # cut out center and fill in background
        if bg_luminosity is not None:
            idx = radii > circle_radius
            image[idx] = bg_luminosity

        return image


def main():
    f_c = TextureFactory('checkerboard', 10, image_width=200)
    img_c = f_c.get_image(.5, .75, circle_radius=50, bg_luminosity=.5)
    f_r = TextureFactory('random', 2, image_width=200)
    img_r = f_r.get_image(1, .5, circle_radius=50)

    plt.imshow(img_r, cmap='gray', vmin=0, vmax=1)
    plt.show()
    plt.imshow(img_c, cmap='gray', vmin=0, vmax=1)
    plt.show()


if __name__ == "__main__":
    main()
