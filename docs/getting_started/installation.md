# Installing

:::::{tab-set}

::::{tab-item} pip
`stimupy` is not (yet) available on PyPI
-- but if it was, one could:

```python
pip install stimupy
```

For now, could do:

```python
pip install 'stimupy @ https://github.com/computational-psychology/stimupy'
```

::::

::::{tab-item} conda-forge
Surely this must also be possible...
::::

::::{tab-item} source (GitHub)

1. Clone the repository from GitHub (TUB):

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
pip install -e .
```

for an editable install;
this makes changes to files immediately usable,
rather than having to reinstall the package after every change.
:::
::::
:::::


## Dependencies
Dependencies should be automatically installed (at least using `pip`).
`stimupy`s required dependencies are:
- numpy
- scipy
- matplotlib
- Pillow
- pandas