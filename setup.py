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
    name="ford-prefect",
    version=VERSION,
    author="Jordan Matelsky",
    author_email="opensource@matelsky.com",
    description="MyFord API",
    license="Apache 2.0",
    keywords="ford car api myford",
    url="https://github.com/PyMyFord/prefect/tarball/" + VERSION,
    packages=find_packages(),
    install_requires=["requests"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
    ],
)
