# Checkerboard Factory
Create images of 3-dimensional checkerboards and optionally a transparent rectangle covering a part of the board.

![3D checkerboard](./example_images/checkerboard_stacked.png)

### Example Usage
```
f = CheckerboardFactory()
f.find_checkerboard(n_checks=8)
f.build_image(tau=2, alpha=.5, camera_offset=(1, 0, 0))
checkerboard = f.get_checkerboard()
cutout = f.get_cutout()
stacked = f.get_stacked()
```

### Requires
- PovRay
- PIL
- Numpy

# Texture Factory
Create 2-dimensional textures with an optional transparent circle covering layered over the center.

Supports random textures and alternating checkerboard patterns.

![Texture Random](./example_images/texture_random.png)
![Texture Checkerboard](./example_images/texture_checkerboard.png)

### Example Usage
```
f_c = TextureFactory('checkerboard', 10, image_width=200)
img_c = f_c.get_image(.5, .75, circle_radius=50, bg_luminosity=.5)
f_r = TextureFactory('random', 2, image_width=200)
img_r = f_r.get_image(1, .5, circle_radius=50)
```

### Requires
- Numpy