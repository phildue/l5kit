#!/usr/bin/env python
from setuptools import find_packages, setup

from l5kit import __version__


setup(
    name="l5kit",
    version=__version__,
    description="Woven by Toyota Autonomous Vehicle Research library",
    author="Woven by Toyota",
    author_email="l5kit@woven-planet.global",
    url="https://github.com/woven-planet/l5kit",
    license="apache2",
    install_requires=[
        "imageio",
        "matplotlib",
        "numpy",
        "opencv-contrib-python-headless",
        "protobuf",
        "pymap3d",
        "scipy",
        "setuptools",
        "torch",
        "torchvision",
        "tqdm",
        "transforms3d",
        "zarr",
        "pyyaml",
        "notebook",
        "ptable",
        "ipywidgets",
        "shapely",
        "typing_extensions",
        "bokeh",
        "importlib-metadata",
        "gym",
        "typed-ast"
    ],
    extras_require={
        "dev": ["pytest", "mypy", "types-PyYAML", "setuptools", "twine", "wheel", "pytest-cov",
                "flake8", "isort", "Sphinx", "recommonmark",
                "pre-commit", "sphinx-press-theme"]
    },
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
