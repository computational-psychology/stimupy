# Contribute to `stimupy`

## Setting up a development environment
1. **Fork** the [GitHub repository](https://github.com/computational-psychology/stimupy/)
2. **Clone** the fork repository to your local machine
3. **Install**`stimupy` with the development requirements `pip install -e ".[dev]"`
    - Recommended to create an *editable* installation using 
    - `".[dev,docs]"` to also edit and build the documentation

The `stimupy` project uses a couple of development tools
to work towards more consisten code quality:

- `pytest` for unit and integration tests
- `pyupgrade` for possible syntax improvements using newer language features
- `black` for consistent code formatting
- `flake8` for all kinds of linting

These tools get installed as part of the `[dev]` extra dependencies.
Additionally, to run these more consistently, one can install:

- `nox` for automatically running tests across different Python versions
- `precommit` for automatically running formatters and linters

## Edit documentation
`stimupy`'s documentation is build using [Jupyter Book](https://jupyterbook.org/en/stable/intro.html)
which is installed as part of the `[docs]` extra dependencies.

### Building the documentation
To compile the documentation locally (from the toplevel directory):
```
jupyter-book build --all docs/
```

### How the documentation is organized
All documentation lives in the `docs` subdirectory,
and consists of a collection of Markdown (`.md`) files,
specifically in the [MyST Markdown](https://jupyterbook.org/en/stable/content/myst.html) flavor
(as well as some ReStructured Text).

The documentation is generally organized along [The Documentation System](https://documentation.divio.com/),
consisting of the following categories:
- learning-oriented tutorials, under <project:getting_started/getting_started>
- understanding-oriented <project:topic_guides/topic_guides>
- information-oriented <project:reference/reference>

### Executable content
Some pages are pure (MyST) Markdown files;
others (e.g. the tutorials) are executable notebooks, in the same MyST Markdown format.
These MyST Notebooks can contain both Markdown syntax,
as well as `code-cell` blocks which are executed during the build
and their output is "woven" into the resulting page.
These MyST Notebooks have a YAML frontmatter
directing [JupyText](https://jupytext.readthedocs.io/en/latest/)
how to convert them.




## Add a stimulus set

- Create a new file in `stimupy/papers`
- Add only stimuli that use `stimupy` functionality
- Each stimulus should be its own function
- Each function should only take a `ppd` argument;
  it should replicate the exact size and geometry of the stimulus,
  allowing only the resolution (i.e., pixels per degree) to be changed.
- Also create a corresponding tests file


## Edit or add a stimulus function
- To contribute a stimulus function, add it to the corresponding module


## Contributing back to `stimupy`

0. **Edit** code/documentation
1. **Commit & Push** changes to your fork
2. **Pull request** from your fork to our repository
    - GitHub Actions will automatically run tests and linters
    - If linters fail, run `black`, `pyupgrade` and `flake8` --
      either separately or all together through `pre-commit`:
      `pre-commit run --all-files`
3. Changes will be reviewed by one of the maintainers
