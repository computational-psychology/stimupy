import nox


@nox.session(python=["3.8", "3.9", "3.10", "3.11"])
def tests(session):
    session.install("-r", "requirements.txt")
    session.install(".")
    session.run("pytest")


@nox.session(python="3.11")
def lint(session):
    # Run the linters (via pre-commit)
    session.install("pre-commit")
    session.run("pre-commit", "run", "--all-files", *session.posargs)
