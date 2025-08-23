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

```{attention}
To run locally, the code for these interactive demos requires
a [Jupyter Notebook](https://jupyter.org/) environment,
and the [Panel extension](https://panel.holoviz.org/).
```

# Parallelogram
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
