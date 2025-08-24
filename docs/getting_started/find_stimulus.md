---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# How to find a stimulus

`stimupy` offers many ways to discover stimulus functions --
whether you're exploring what's available or searching for a specific stimulus.  
This guide covers both discovery using (this) **online documentation**
and from **within Python** discovery methods.


## In this documentation

### Search bar

If you're looking for a specific function
or want to check whether `stimupy` includes a certain stimulus (e.g., **Gabors**),
use the **search bar** on any of these pages.  
It will return all relevant pages, examples, and API references for your search term.

### Overviews of all modules and functions

You can browse a complete overview of submodules and functions in the **[stimupy API reference](../reference/api.md)**.  
This list mirrors `stimupy`'s modular structure and contains:

- All submodules
- All functions (with documentation)
- Direct links to their definitions

For a more visual approach, explore our **[interactive demos](../reference/demos)**.
These show both high-level and low-level modules, and how they can be used.

### Visual overview *(coming soon)*

A quick, visual overview of available stimuli will be added in a future update.

---

## From within Python

If you're already working in Python
and simply need to refresh your memory about a submodule or function name, 
`stimupy` provides built-in tools to help.

### Visual overviews

Both `stimupy.components` and `stimupy.stimuli` include a **`plot_overview()`** function
that displays an example of each available stimulus.

Example for `components`:
```{code-cell}
from stimupy import components

components.plot_overview()
```

Example for `stimuli`:
```{code-cell}
from stimupy import stimuli

stimuli.plot_overview()
```

Example for `noises`:
```{code-cell}
from stimupy import noises

noises.plot_overview()
```


### Autocompletion in interactive interpreters

Most consoles and IDEs that you may use (IPython, Jupyter Notebook, Spyder, VSCode, ...)
should be able to autocomplete while typing, usually using <TAB>:

```
>>> stimupy.<TAB>
```

### Using `help()` to list contents

You can use Python's built-in `help()` function
to inspect submodules, functions, and their documentation.
For modules, this will also list all its submodules and functions.

**Top-level overview:**

```{code-cell}
:tags: [output_scroll]
import stimupy

help(stimupy)
```

**High-level submodule:**

```{code-cell}
:tags: [output_scroll]
from stimupy import components

help(components)
```

**Low-level submodule:**

```{code-cell}
:tags: [output_scroll]
from stimupy.components import shapes

help(shapes)
```

<!-- ## How stimupy is organized -->
```{include} ../user_guide/organization.md
:heading-offset: 1
```
