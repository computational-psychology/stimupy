---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.5
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

```{tip}
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/computational-psychology/stimupy/HEAD?urlpath=lab/tree/docs/reference/demos/components/shapes.md)
 to get interactivity
```
```{attention}
To run locally, the code for these interactive demos requires
a [Jupyter Notebook](https://jupyter.org/) environment,
and the [Panel extension](https://panel.holoviz.org/).
```

# Components - Shapes
{py:mod}`stimupy.components.shapes`



## Rectangle
{py:func}`stimupy.components.shapes.rectangle`

```{code-cell} ipython3
import param

class RectangleParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    rectangle_height = param.Integer(default=3, bounds=(1, 6), doc="")
    rectangle_width = param.Integer(default=3, bounds=(1, 6), doc="")
    rectangle_position_x = param.Number(default=3.0, bounds=(0, 10.0), step=0.01, doc="")
    rectangle_position_y = param.Number(default=3.0, bounds=(0, 10.0), step=0.01, doc="")
    intensity_rectangle = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="")
    intensity_background = param.Number(default=0.0, bounds=(0, 1), step=0.01, doc="")
    rotation = param.Integer(default=0, bounds=(0, 360), doc="")
    mask = param.Boolean(default=False, doc="")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "rectangle_size": (self.rectangle_height, self.rectangle_width),
            "rectangle_position": (self.rectangle_position_x, self.rectangle_position_y),
            "intensity_rectangle": self.intensity_rectangle,
            "intensity_background": self.intensity_background,
            "rotation": self.rotation,
        }
```

```{code-cell} ipython3
from stimupy.components.shapes import rectangle
import sys
from pathlib import Path

# Add the _static directory to the path to import display_stimulus
sys.path.append(str((Path().resolve().parents[2] / "_static")))
from display_stimulus import InteractiveStimDisplay

# Create and display the interactive rectangle
rectangle_params = RectangleParams()
disp = InteractiveStimDisplay(rectangle, rectangle_params)
disp.layout
```

## Triangle
{py:func}`stimupy.components.shapes.triangle`

```{code-cell} ipython3
import param

class TriangleParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    triangle_height = param.Number(default=3, bounds=(1, 10), step=0.01, doc="")
    triangle_width = param.Number(default=3, bounds=(1, 10), step=0.01, doc="")
    rotation = param.Integer(default=0, bounds=(0, 360), doc="")
    intensity_triangle = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="")
    intensity_background = param.Number(default=0., bounds=(0, 1), step=0.01, doc="")
    include_corners = param.Boolean(default=True, doc="")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "triangle_size": (self.triangle_height, self.triangle_width),
            "rotation": self.rotation,
            "intensity_triangle": self.intensity_triangle,
            "intensity_background": self.intensity_background,
            "include_corners": self.include_corners,
        }
```

```{code-cell} ipython3
from stimupy.components.shapes import triangle
import sys
from pathlib import Path

# Add the _static directory to the path to import display_stimulus
sys.path.append(str((Path().resolve().parents[2] / "_static")))
from display_stimulus import InteractiveStimDisplay

# Create and display the interactive triangle
triangle_params = TriangleParams()
disp = InteractiveStimDisplay(triangle, triangle_params)
disp.layout
```

## Cross
{py:func}`stimupy.components.shapes.cross`

```{code-cell} ipython3
import param

class CrossParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    cross_height = param.Integer(default=4, bounds=(1, 8), doc="")
    cross_width = param.Integer(default=4, bounds=(1, 8), doc="")
    cross_thickness_height = param.Number(default=1.0, bounds=(0.5, 3), step=0.1, doc="")
    cross_thickness_width = param.Number(default=1.0, bounds=(0.5, 3), step=0.1, doc="")
    cross_arm_ratio1 = param.Number(default=1.0, bounds=(0.1, 5.0), step=0.1, doc="")
    cross_arm_ratio2 = param.Number(default=1.0, bounds=(0.1, 5.0), step=0.1, doc="")
    rotation = param.Integer(default=0, bounds=(0, 360), doc="")
    intensity_cross = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="")
    intensity_background = param.Number(default=0., bounds=(0, 1), step=0.01, doc="")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "cross_size": (self.cross_height, self.cross_width),
            "cross_thickness": (self.cross_thickness_height, self.cross_thickness_width),
            "cross_arm_ratios": (self.cross_arm_ratio1, self.cross_arm_ratio2),
            "rotation": self.rotation,
            "intensity_cross": self.intensity_cross,
            "intensity_background": self.intensity_background,
        }
```

```{code-cell} ipython3
from stimupy.components.shapes import cross
import sys
from pathlib import Path

# Add the _static directory to the path to import display_stimulus
sys.path.append(str((Path().resolve().parents[2] / "_static")))
from display_stimulus import InteractiveStimDisplay

# Create and display the interactive cross
cross_params = CrossParams()
disp = InteractiveStimDisplay(cross, cross_params)
disp.layout
```

## Parallelogram
{py:func}`stimupy.components.shapes.parallelogram`

```{code-cell} ipython3
import param

class ParallelogramParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    parallelogram_height = param.Integer(default=3, bounds=(1, 6), doc="")
    parallelogram_width = param.Integer(default=3, bounds=(1, 6), doc="")
    parallelogram_depth = param.Number(default=1.0, bounds=(-3.0, 3.0), step=0.1, doc="")
    rotation = param.Integer(default=0, bounds=(0, 360), doc="")
    intensity_parallelogram = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="")
    intensity_background = param.Number(default=0., bounds=(0, 1), step=0.01, doc="")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "parallelogram_size": (self.parallelogram_height, self.parallelogram_width, self.parallelogram_depth),
            "rotation": self.rotation,
            "intensity_parallelogram": self.intensity_parallelogram,
            "intensity_background": self.intensity_background,
        }
```

```{code-cell} ipython3
from stimupy.components.shapes import parallelogram
import sys
from pathlib import Path

# Add the _static directory to the path to import display_stimulus
sys.path.append(str((Path().resolve().parents[2] / "_static")))
from display_stimulus import InteractiveStimDisplay

# Create and display the interactive parallelogram
parallelogram_params = ParallelogramParams()
disp = InteractiveStimDisplay(parallelogram, parallelogram_params)
disp.layout
```

## Ellipse
{py:func}`stimupy.components.shapes.ellipse`

```{code-cell} ipython3
import param

class ShapeEllipseParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    radius_height = param.Number(default=3, bounds=(1, 6), step=0.1, doc="")
    radius_width = param.Number(default=4, bounds=(1, 6), step=0.1, doc="")
    rotation = param.Integer(default=0, bounds=(0, 360), doc="")
    intensity_ellipse = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="")
    intensity_background = param.Number(default=0., bounds=(0, 1), step=0.01, doc="")
    origin = param.Selector(default="mean", objects=['mean', 'corner', 'center'], doc="")
    restrict_size = param.Boolean(default=True, doc="")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "radius": (self.radius_height, self.radius_width),
            "rotation": self.rotation,
            "intensity_ellipse": self.intensity_ellipse,
            "intensity_background": self.intensity_background,
            "origin": self.origin,
            "restrict_size": self.restrict_size,
        }
```

```{code-cell} ipython3
from stimupy.components.shapes import ellipse
import sys
from pathlib import Path

# Add the _static directory to the path to import display_stimulus
sys.path.append(str((Path().resolve().parents[2] / "_static")))
from display_stimulus import InteractiveStimDisplay

# Create and display the interactive ellipse
ellipse_params = ShapeEllipseParams()
disp = InteractiveStimDisplay(ellipse, ellipse_params)
disp.layout
```

## Circle
{py:func}`stimupy.components.shapes.circle`

```{code-cell} ipython3
import param

class ShapeCircleParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    radius = param.Number(default=3, bounds=(1, 6), step=0.1, doc="")
    intensity_circle = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="")
    intensity_background = param.Number(default=0., bounds=(0, 1), step=0.01, doc="")
    origin = param.Selector(default="mean", objects=['mean', 'corner', 'center'], doc="")
    restrict_size = param.Boolean(default=True, doc="")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "radius": self.radius,
            "intensity_circle": self.intensity_circle,
            "intensity_background": self.intensity_background,
            "origin": self.origin,
            "restrict_size": self.restrict_size,
        }
```

```{code-cell} ipython3
from stimupy.components.shapes import circle
import sys
from pathlib import Path

# Add the _static directory to the path to import display_stimulus
sys.path.append(str((Path().resolve().parents[2] / "_static")))
from display_stimulus import InteractiveStimDisplay

# Create and display the interactive circle
circle_params = ShapeCircleParams()
disp = InteractiveStimDisplay(circle, circle_params)
disp.layout
```

## Wedge
{py:func}`stimupy.components.shapes.wedge`

```{code-cell} ipython3
import param

class ShapeWedgeParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    angle = param.Number(default=45, bounds=(1, 360), step=1, doc="")
    radius = param.Number(default=4, bounds=(1, 8), step=0.1, doc="")
    inner_radius = param.Number(default=0, bounds=(0, 3), step=0.1, doc="")
    rotation = param.Integer(default=0, bounds=(0, 360), doc="")
    intensity_wedge = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="")
    intensity_background = param.Number(default=0., bounds=(0, 1), step=0.01, doc="")
    origin = param.Selector(default="mean", objects=['mean', 'corner', 'center'], doc="")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "angle": self.angle,
            "radius": self.radius,
            "inner_radius": self.inner_radius,
            "rotation": self.rotation,
            "intensity_wedge": self.intensity_wedge,
            "intensity_background": self.intensity_background,
            "origin": self.origin,
        }
```

```{code-cell} ipython3
from stimupy.components.shapes import wedge
import sys
from pathlib import Path

# Add the _static directory to the path to import display_stimulus
sys.path.append(str((Path().resolve().parents[2] / "_static")))
from display_stimulus import InteractiveStimDisplay

# Create and display the interactive wedge
wedge_params = ShapeWedgeParams()
disp = InteractiveStimDisplay(wedge, wedge_params)
disp.layout
```

## Disc
{py:func}`stimupy.components.shapes.disc`

```{code-cell} ipython3
import param

class DiscParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    radius = param.Number(default=3, bounds=(1, 6), step=0.01, doc="")
    intensity_disc = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="")
    intensity_background = param.Number(default=0., bounds=(0, 1), step=0.01, doc="")
    origin = param.Selector(default="mean", objects=['mean', 'corner', 'center'], doc="")
    add_mask = param.Boolean(default=False, doc="")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "radius": self.radius,
            "intensity_disc": self.intensity_disc,
            "intensity_background": self.intensity_background,
            "origin": self.origin,
        }
```

```{code-cell} ipython3
from stimupy.components.shapes import disc
import sys
from pathlib import Path

# Add the _static directory to the path to import display_stimulus
sys.path.append(str((Path().resolve().parents[2] / "_static")))
from display_stimulus import InteractiveStimDisplay

# Create and display the interactive disc
disc_params = DiscParams()
disp = InteractiveStimDisplay(disc, disc_params)
disp.layout
```

## Annulus
{py:func}`stimupy.components.shapes.annulus`

```{code-cell} ipython3
import param

class ShapeAnnulusParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    radius1 = param.Number(default=2, bounds=(1, 4), step=0.1, doc="")
    radius2 = param.Number(default=4, bounds=(3, 6), step=0.1, doc="")
    intensity_ring = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="")
    intensity_background = param.Number(default=0., bounds=(0, 1), step=0.01, doc="")
    origin = param.Selector(default="mean", objects=['mean', 'corner', 'center'], doc="")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "radii": (self.radius1, self.radius2),
            "intensity_ring": self.intensity_ring,
            "intensity_background": self.intensity_background,
            "origin": self.origin,
        }
```

```{code-cell} ipython3
from stimupy.components.shapes import annulus
import sys
from pathlib import Path

# Add the _static directory to the path to import display_stimulus
sys.path.append(str((Path().resolve().parents[2] / "_static")))
from display_stimulus import InteractiveStimDisplay

# Create and display the interactive annulus
annulus_params = ShapeAnnulusParams()
disp = InteractiveStimDisplay(annulus, annulus_params)
disp.layout
```

## Ring
{py:func}`stimupy.components.shapes.ring`

```{code-cell} ipython3
import param

class RingParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    radius1 = param.Number(default=2, bounds=(1, 4), step=0.01, doc="")
    radius2 = param.Number(default=4, bounds=(3, 6), step=0.01, doc="")
    intensity_ring = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="")
    intensity_background = param.Number(default=0., bounds=(0, 1), step=0.01, doc="")
    origin = param.Selector(default="mean", objects=['mean', 'corner', 'center'], doc="")
    add_mask = param.Boolean(default=False, doc="")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "radii": (self.radius1, self.radius2),
            "intensity_ring": self.intensity_ring,
            "intensity_background": self.intensity_background,
            "origin": self.origin,
        }
```

```{code-cell} ipython3
from stimupy.components.shapes import ring
import sys
from pathlib import Path

# Add the _static directory to the path to import display_stimulus
sys.path.append(str((Path().resolve().parents[2] / "_static")))
from display_stimulus import InteractiveStimDisplay

# Create and display the interactive ring
ring_params = RingParams()
disp = InteractiveStimDisplay(ring, ring_params)
disp.layout
```
