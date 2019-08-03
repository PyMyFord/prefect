import codecs
import os
import re
from setuptools import setup, find_packages

VERSION = "0.0.1"

"""
git tag {VERSION}
git push --tags
python setup.py sdist
python setup.py bdist_wheel --universal
twine upload dist/*
"""


def read(*parts):
    with codecs.open(os.path.join(HERE, *parts), "r") as fp:
        return fp.read()


HERE = os.path.abspath(os.path.dirname(__file__))

setup(
    name="prefect",
    version=VERSION,
    author="Jordan Matelsky",
    author_email="opensource@matelsky.com",
    description="Ford API",
    license="Aache 2.0",
    keywords="ford car api",
    url="https://github.com/j6k4m8/prefect/tarball/" + VERSION,
    packages=find_packages(),
    install_requires=["requests"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
    ],
)