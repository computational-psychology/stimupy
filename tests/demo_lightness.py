import matplotlib.pyplot as plt
from stimuli import lightness

# %% Cornsweet / Todorovic
a = lightness.cornsweet((10, 10), 10, 0.5)
b = lightness.todorovic(a, 2, 2)

plt.figure()
plt.imshow(a, vmin=0, vmax=1, cmap="gray")
plt.show()
plt.figure()
plt.imshow(b, vmin=0, vmax=1, cmap="gray")
plt.show()

# %% Square Wave
c = lightness.square_wave((10, 10), 10, 0.5, 2)

plt.figure()
plt.imshow(c, vmin=0, vmax=1, cmap="gray")
plt.show()

# %% White's Illusion BMCC
d = lightness.whites_illusion_bmcc((10, 10), 10, 0.5, 2)
e1, e2 = lightness.contours_white_bmmc((10, 10), 10, 0.5, 2, contour_width=3)

plt.figure()
plt.imshow(d, vmin=0, vmax=1, cmap="gray")
plt.show()
plt.figure()
plt.imshow(e1, vmin=0, vmax=1, cmap="gray")
plt.show()
plt.figure()
plt.imshow(e2, vmin=0, vmax=1, cmap="gray")
plt.show()

# %% White's Illusion Gil
f = lightness.whites_illusion_gil((10, 10), 10, 0.5, 2)

plt.figure()
plt.imshow(f, vmin=0, vmax=1, cmap="gray")
plt.show()

# %% Disc and Ring
g = lightness.disc_and_ring((10, 10), [4, 2], [0.5, 1.0])

plt.figure()
plt.imshow(g, vmin=0, vmax=1, cmap="gray")
plt.show()
