# Installing

:::::{tab-set}

::::{tab-item} pip {fab}`python`
`pip` can install `stimupy` directly from GitHub (the `main` branch)

```python
pip install https://github.com/computational-psychology/stimupy/zipball/main
```

:::{admonition} Install a different version
    :class: dropdown

From a specific branch, e.g. (`main`)[https://github.com/computational-psychology/stimupy/tree/main]:
```python
pip install https://github.com/computational-psychology/stimupy/archive/refs/heads/main.zip
```

From a specific tag, e.g. `v1.0.0`:
```python
pip install https://github.com/computational-psychology/stimupy/archive/tags/v1.0.0.zip
```

From a specific commit, e.g., (`9e37617`)[https://github.com/computational-psychology/stimupy/tree/9e37617]:
```python
pip install https://github.com/computational-psychology/stimupy/archive/9e37617.zip
```
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