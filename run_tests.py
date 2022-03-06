import doctest
import os

import pytest


def run_tests():
    pytest.main()


def run_doctests():
    for file in os.listdir("examples/"):
        if not file.endswith(".md"):
            continue
        filepath = os.path.join("examples/", file)
        doctest.testfile(filepath, optionflags=doctest.ELLIPSIS, raise_on_error=True)
