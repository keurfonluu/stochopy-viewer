import glob
import os
import shutil

from invoke import task

import stochopy_viewer


@task
def tag(c):
    c.run("git tag v{}".format(stochopy_viewer.__version__))
    c.run("git push --tags")


@task
def clean(c, bytecode=False):
    patterns = [
        "stochopy_viewer.egg-info",
    ]

    if bytecode:
        patterns += glob.glob("**/*.pyc", recursive=True)
        patterns += glob.glob("**/__pycache__", recursive=True)

    for pattern in patterns:
        if os.path.isfile(pattern):
            os.remove(pattern)
        else:
            shutil.rmtree(pattern, ignore_errors=True)


@task
def black(c):
    c.run("black -t py36 stochopy_viewer")


@task
def docstring(c):
    c.run("docformatter -r -i --blank --wrap-summaries 88 --wrap-descriptions 88 --pre-summary-newline stochopy_viewer")


@task
def isort(c):
    c.run("isort -rc stochopy_viewer")


@task
def format(c):
    c.run("invoke isort black docstring")
