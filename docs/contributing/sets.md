# Contribrute a stimulus (set)

## Add a stimulus set
- Create a new file in `stimupy/papers`
- Add only stimuli that use `stimupy` functionality
- Each stimulus should be its own function
- Each function should only take a `ppd` argument;
  it should replicate the exact size and geometry of the stimulus,
  allowing only the resolution (i.e., pixels per degree) to be changed.
- Also create a corresponding `tests/papers_my_paper.py` file


## Edit or add a stimulus function
- To contribute a stimulus function, add it to the corresponding module


## Contributing back to `stimupy`

0. **Edit** code/documentation
1. **Commit & Push** changes to your fork
    - We use [conventional commit](https://www.conventionalcommits.org/en/v1.0.0/) messages.
    For bugfixes, please start your commit message(s) with `fix: ...`.
    For add features (e.g., stimuli, set), please start your commit message(s) with `feat: ...`.
2. **Pull request** from your fork to our repository
    - GitHub Actions will automatically run tests and linters
    - If linters fail, run `black`, `pyupgrade` and `flake8` --
      either separately or all together through `pre-commit`:
      `pre-commit run --all-files`
3. Changes will be reviewed by one of the maintainers