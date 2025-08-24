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

# Anderson
{py:func}`stimupy.stimuli.whites.anderson`

```{pyodide}
:skip-embed:

import param

class AndersonParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")

    frequency = param.Number(default=1, bounds=(0, 2), step=0.1, doc="Frequency in cpd")
    intensity_bars_low = param.Number(default=0, bounds=(0, 1), step=0.01, doc="Low bar intensity")
    intensity_bars_high = param.Number(default=1, bounds=(0, 1), step=0.01, doc="High bar intensity")
    intensity_target = param.Number(default=0.5, bounds=(0, 1), step=0.01, doc="Target intensity")
    target_indices_top = param.List(default=[1], doc="Top target indices")
    target_indices_bottom = param.List(default=[2], doc="Bottom target indices")
    target_center_offset = param.Number(default=2.0, bounds=(0, 5), step=0.1, doc="Target center offset")
    target_height = param.Number(default=2.0, bounds=(1, 5), step=0.1, doc="Target height")
    intensity_stripes_low = param.Number(default=0, bounds=(0, 1), step=0.01, doc="Low stripe intensity")
    intensity_stripes_high = param.Number(default=1, bounds=(0, 1), step=0.01, doc="High stripe intensity")
    stripe_center_offset = param.Number(default=2, bounds=(-5, 5), step=0.1, doc="Stripe center offset")
    stripe_height = param.Number(default=1.0, bounds=(0.5, 3), step=0.1, doc="Stripe height")

    def get_stimulus_params(self):
        return {
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "frequency": self.frequency,
            "intensity_bars": (self.intensity_bars_low, self.intensity_bars_high),
            "intensity_target": self.intensity_target,
            "target_indices_top": self.target_indices_top,
            "target_indices_bottom": self.target_indices_bottom,
            "target_center_offset": self.target_center_offset,
            "target_height": self.target_height,
            "intensity_stripes": (self.intensity_stripes_low, self.intensity_stripes_high),
            "stripe_center_offset": self.stripe_center_offset,
            "stripe_height": self.stripe_height,
        }
```

```{pyodide}
:skip-embed:

from stimupy.stimuli.whites import anderson
from stimupy._docs.display_stimulus import InteractiveStimDisplay

# Create and display the interactive anderson
anderson_params = AndersonParams()
disp = InteractiveStimDisplay(anderson, anderson_params)
disp.layout
```