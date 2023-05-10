# Contribute documentation

## How the documentation is organized
All documentation lives in the `docs` subdirectory,
and consists of a collection of Markdown (`.md`) files,
specifically in the [MyST Markdown](https://jupyterbook.org/en/stable/content/myst.html) flavor
(as well as some ReStructured Text).

The documentation is generally organized along [The Documentation System](https://documentation.divio.com/),
consisting of the following categories:
- learning-oriented tutorials, under <project:getting_started/getting_started>
- understanding-oriented <project:topic_guides/topic_guides>
- information-oriented <project:reference/reference>


## Building the documentation
`stimupy`'s documentation is build using [Jupyter Book](https://jupyterbook.org/en/stable/intro.html)
which is installed as part of the `[docs]` extra dependencies.
To compile the documentation locally (from the toplevel directory):
```
jupyter-book build --all docs/
```
which will then provide an output message on how to view the locally-built documentation.

## Executable content
Some pages are pure (MyST) Markdown files;
others (e.g. the tutorials) are executable notebooks, in the same MyST Markdown format.
These MyST Notebooks can contain both Markdown syntax,
as well as `code-cell` blocks which are executed during the build
and their output is "woven" into the resulting page.
These MyST Notebooks have a YAML frontmatter
directing [JupyText](https://jupytext.readthedocs.io/en/latest/)
how to convert them.

## Contributing back to `stimupy`

0. **Edit** documentation
1. **Commit & Push** changes to your fork
    - We use [conventional commit](https://www.conventionalcommits.org/en/v1.0.0/) messages;
    for documentation please start your commit message(s) with `docs: ...`
2. **Pull request** from your fork to our repository
    - GitHub Actions will automatically run tests and linters
    - If linters fail, run `black`, `pyupgrade` and `flake8` --
      either separately or all together through `pre-commit`:
      `pre-commit run --all-files`
3. Changes will be reviewed by one of the maintainers