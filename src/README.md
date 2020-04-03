# Contrast Measures
Various function that calculate contrast metrics.

### Example usage

```python
from stimuli import contrast_metrics as cm
import numpy as np

arr = np.random.randint(2, 10, (10, 10))
cm.SAM(arr)
cm.SAMLG(arr)
cm.SDMC(arr)
cm.SAW(arr)
cm.SAWLG(arr)
cm.RMS(arr)
cm.SD(arr)
cm.SDLG(arr)

mask = arr > 5
cm.SAM(arr, mask=mask, mode="chunk", chunk_size=2)
```

# Lightness
This submodule contains functions for creating common stimuli used in
lightness/brightness research as numpy arrays (or save them as raster art).

All stimuli are freely parameterizable, see docstrings of individual functions
for details.


### Example usage
```python
from stimuli import lightness
import matplotlib.pyplot as plt

# %% Cornsweet / Todorovic
a = lightness.cornsweet((30, 30), 30, .5)
b = lightness.todorovic(a, 2, 2)

plt.figure()
plt.imshow(a, vmin=0, vmax=1, cmap='gray')
plt.show()
plt.figure()
plt.imshow(b, vmin=0, vmax=1, cmap='gray')
plt.show()

# %% Square Wave
c = lightness.square_wave((10, 10), 30, .5, 2)

plt.figure()
plt.imshow(c, vmin=0, vmax=1, cmap='gray')
plt.show()

# %% White's Illusion BMCC
d = lightness.whites_illusion_bmcc((10, 10), 30, .5, 2)
e1, e2 = lightness.contours_white_bmmc((10, 10), 30, .5, 2)

plt.figure()
plt.imshow(d, vmin=0, vmax=1, cmap='gray')
plt.show()
plt.figure()
plt.imshow(e1, vmin=0, vmax=1, cmap='gray')
plt.show()
plt.figure()
plt.imshow(e2, vmin=0, vmax=1, cmap='gray')
plt.show()

# %% White's Illusion Gil
f = lightness.whites_illusion_gil((10, 10), 30, .5, 2)

plt.figure()
plt.imshow(f, vmin=0, vmax=1, cmap='gray')
plt.show()

# %% Disc and Ring
g = lightness.disc_and_ring((10, 10), [4, 2], [0.5, 1.])

plt.figure()
plt.imshow(g, vmin=0, vmax=1, cmap='gray')
plt.show()
```

# Utils
Helper functions for padding, resizing, computing Munsell values, and
converting pixel values to degrees of visual angle.
