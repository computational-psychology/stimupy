# Lightness
This submodule contains functions for creating common stimuli used in
lightness/brightness research as numpy arrays (or save them as raster art).

All stimuli are freely parameterizable, see docstrings of individual functions
for details.


### Example usage
```python
from stimuli import lightness
import matplotlib.pyplot as plt
```
#### Cornsweet 

A rectangular Cornsweet edge stimulus.

![Cornsweet](lightness/example_images/cornsweet.png)
```python
a = lightness.cornsweet((10, 10), 10, .5)

plt.figure()
plt.imshow(a, vmin=0, vmax=1, cmap='gray')
plt.show()
```

#### Todorovic

A checkerboard illusion by appropriately aligning COC stimuli, in the way demonstrated by Todorovic (1987)

![Todorovic](lightness/example_images/todorovic.png)

```python
a = lightness.cornsweet((10, 10), 10, .5)

plt.figure()
plt.imshow(b, vmin=0, vmax=1, cmap='gray')
plt.show()
```

#### Square Wave
![Square Wave](lightness/example_images/square_wave.png)
```python
c = lightness.square_wave((10, 10), 10, .5, 2)

plt.figure()
plt.imshow(c, vmin=0, vmax=1, cmap='gray')
plt.show()

```
#### White's Illusion - Blakeslee and McCourt (1999)
![White's Illusion BMCC](lightness/example_images/whites_illusion_bmcc.png)

![Contours dark](lightness/example_images/contours_white_bmcc_dark.png)
![Contours bright](lightness/example_images/contours_white_bmcc_bright.png)
```python
d = lightness.whites_illusion_bmcc((10, 10), 10, .5, 2)
e1, e2 = lightness.contours_white_bmmc((10, 10), 10, .5, 2, contour_width=3)

plt.figure()
plt.imshow(d, vmin=0, vmax=1, cmap='gray')
plt.show()
plt.figure()
plt.imshow(e1, vmin=0, vmax=1, cmap='gray')
plt.show()
plt.figure()
plt.imshow(e2, vmin=0, vmax=1, cmap='gray')
plt.show()

```
#### White's Illusion - Gilchrist
![White's Illusion Gilchrist](lightness/example_images/whites_illusion_gil.png)
```python
f = lightness.whites_illusion_gil((10, 10), 10, .5, 2)

plt.figure()
plt.imshow(f, vmin=0, vmax=1, cmap='gray')
plt.show()

```
#### Disc and Ring
![Disk and Ring](lightness/example_images/disc_and_ring.png)
```python
g = lightness.disc_and_ring((10, 10), [4, 2], [0.5, 1.])

plt.figure()
plt.imshow(g, vmin=0, vmax=1, cmap='gray')
plt.show()
```