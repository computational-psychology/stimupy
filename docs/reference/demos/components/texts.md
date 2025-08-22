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
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/computational-psychology/stimupy/HEAD?urlpath=lab/tree/docs/reference/demos/components/texts.md)
 to get interactivity
```
```{attention}
To run locally, the code for these interactive demos requires
a [Jupyter Notebook](https://jupyter.org/) environment,
and the [Panel extension](https://panel.holoviz.org/).
```

# Components - Texts
{py:mod}`stimupy.components.texts`


## Text
{py:func}`stimupy.components.texts.text`

```{code-cell} ipython3
import param

class TextParams(param.Parameterized):
    # Image size parameters
    height = param.Integer(default=10, bounds=(1, 20), doc="Height in degrees")
    width = param.Integer(default=10, bounds=(1, 20), doc="Width in degrees")
    ppd = param.Integer(default=20, bounds=(1, 40), doc="Pixels per degree")
    
    # Text parameters
    text_content = param.String(default="Hello World", doc="Text content")
    fontsize = param.Integer(default=30, bounds=(1, 60), doc="Font size")
    align = param.Selector(default="center", objects=["left", "center", "right"], doc="Text alignment")
    # direction = param.Selector(default="ltr", objects=["ltr", "rtl"], doc="Text direction")
    
    # Intensity parameters
    intensity_text = param.Number(default=1.0, bounds=(0, 1), step=0.01, doc="Text intensity")
    intensity_background = param.Number(default=0.0, bounds=(0, 1), step=0.01, doc="Background intensity")
    
    # Additional parameters
    add_mask = param.Boolean(default=False, doc="Add mask to visualization")

    def get_stimulus_params(self):
        return {
            "text": self.text_content,
            "visual_size": (self.height, self.width),
            "ppd": self.ppd,
            "intensity_text": self.intensity_text,
            "intensity_background": self.intensity_background,
            "fontsize": self.fontsize,
            "align": self.align,
            # "direction": self.direction,
        }
```

```{code-cell} ipython3
from stimupy.components.texts import text
import sys
from pathlib import Path

# Add the _static directory to the path to import display_stimulus
sys.path.append(str((Path().resolve().parents[2] / "_static")))
from display_stimulus import InteractiveStimDisplay

# Create and display the interactive text
text_params = TextParams()
disp = InteractiveStimDisplay(text, text_params)
disp.layout
```