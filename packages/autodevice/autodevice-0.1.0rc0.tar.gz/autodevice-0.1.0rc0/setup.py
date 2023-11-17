
__module_name__ = "setup.py"
__author__ = "Michael E. Vinyard"
__email__ = "mvinyard.ai@gmail.com"
__package__ = "autodevice"


# -- import packages: ---------------------------------------------------------
import setuptools
import re
import os
import sys


# -- fetch requirements packages: ---------------------------------------------
with open('requirements.txt') as f:
    __requirements__ = f.read().splitlines()

with open(f'{__package__}/__version__.py') as v:
    exec(v.read())


# -- run setup: ---------------------------------------------------------------
setuptools.setup(
    name=__package__,
    version=__version__,
    python_requires=">3.9.0",
    author=__author__,
    author_email=__email__,
    url="https://github.com/mvinyard/autodevice",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    description="Automatically assign available hardware on the fly, in-line with PyTorch code.",
    packages=setuptools.find_packages(),
    install_requires=__requirements__,
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Programming Language :: Python :: 3.9",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
    ],
    license="MIT",
)
