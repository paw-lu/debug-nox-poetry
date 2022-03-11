import nox
from nox_poetry import session


@session(python="3.10")
def install(session):
    session.install(".")
