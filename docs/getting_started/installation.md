# Installation

## Installing

`stimupy` can be installed in several ways.
For most usecases, i.e., to _use_ the functions in `stimupy`,
we recommend installing from PyPI using `pip`.

To adapt or contribute code, you will have to get the _source_ code from GitHub.

:::::{tab-set}

::::{tab-item} pip {fab}`python`
`pip` can install the latest version of `stimupy` directly from PyPI

```python
pip install stimupy
```

:::{admonition} Install a different version
    :class: dropdown

`pip` by default install the latest version of package.
To install a different version, simply specify the version number,
either an exact version:
```python
pip install "stimupy==1.0.0"
```
or a conditional version:
```python
pip install "stimupy<=1.0.0"
```
(for any version before `1.0.0`).

`stimupy` uses approximately [Semantic Versioning](https://semver.org/) /
[PEP440](https://peps.python.org/pep-0440/).
This means that versions with the same MAJOR version number are backwards compatible:
code written using version `1.N.x` will work under `1.N+1.x`
but is not guaranteed to work under version `2.x.x`.
Versions with higher MINOR version number (`x.N+1.x`) introduce new features.
Versions with higher PATCH number (`x.x.N+1`) fix bugs.

:::
::::


::::{tab-item} source {fab}`github`

1. Clone the repository from GitHub:

    ```bash
    git clone git@github.com:computational-psychology/stimupy.git
    ```

2. `stimupy` can then be installed using pip.
    From top-level directory run:

    ```python
    pip install .
    ```

    to install to your local python library.

:::{admonition} For developers
    :class: dropdown

```python
pip install -e .[dev,docs]
```

for an editable install (`-e`) which makes changes to files immediately usable,
rather than having to reinstall the package after every change;
and to install the development and documentation dependencies.
:::
::::

:::::


## Dependencies
Dependencies should be automatically installed (at least using `pip`).
`stimupy`s required dependencies are:
- [NumPy](numpy)
- [SciPy](scipy)
- [MatPlotLib](matplotlib)
- [Pillow](pillow)
- [Pandas](pandas)

This documentation contains [interactive demos](../reference/demos),
in the form of Jupyter Notebooks.
To run this, additional dependencies are required:
  - Jupyter Notebook (or JupyterLab)
  - panel
These demo notebooks can also be opened on Binder,
which should install all the necessary dependencies automatically.