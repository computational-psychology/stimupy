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

# White, two-rows
{py:func}`stimupy.stimuli.whites.white_two_rows`

```{pyodide}
:skip-embed:

import param

class WhiteTwoRowsParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    frequency = param.Number(default=1, bounds=(0, 2), step=0.1, doc="Frequency in cpd")
    rotation = param.Number(default=0, bounds=(0, 360), step=1, doc="Rotation in degrees")
    intensity_bars_low = param.Number(default=0, bounds=(0, 1), step=0.01, doc="Low bar intensity")
    intensity_bars_high = param.Number(default=1, bounds=(0, 1), step=0.01, doc="High bar intensity")
    intensity_target = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="Target intensity")
    target_indices_top = param.List(default=[1], doc="Top target indices")
    target_indices_bottom = param.List(default=[1], doc="Bottom target indices")
    target_center_offset = param.Number(default=2.0, bounds=(0, 5), step=0.1, doc="Target center offset")
    target_heights = param.Number(default=2.0, bounds=(0.5, 5), step=0.1, doc="Target heights")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "frequency": self.frequency,
            "rotation": self.rotation,
            "intensity_bars": (self.intensity_bars_low, self.intensity_bars_high),
            "intensity_target": self.intensity_target,
            "target_indices_top": self.target_indices_top,
            "target_indices_bottom": self.target_indices_bottom,
            "target_center_offset": self.target_center_offset,
            "target_heights": self.target_heights,
        }
```

```{pyodide}
:skip-embed:

from stimupy.stimuli.whites import white_two_rows
from stimupy._docs.display_stimulus import InteractiveStimDisplay

# Create and display the interactive white_two_rows
white_two_rows_params = WhiteTwoRowsParams()
disp = InteractiveStimDisplay(white_two_rows, white_two_rows_params)
disp.layout
```