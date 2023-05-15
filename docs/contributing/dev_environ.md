# Setting up a development environment

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
