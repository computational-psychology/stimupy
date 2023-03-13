import nox


@nox.session(python="3.11")
def tests(session):
    session.install("-r", "requirements.txt")
    session.install(".")
    session.run("pytest")
