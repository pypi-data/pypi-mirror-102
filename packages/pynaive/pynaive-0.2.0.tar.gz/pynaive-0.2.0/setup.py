"""Sets up the package."""


import os.path
import setuptools


def read_long_description() -> str:
    """Returns the content of README.md file."""
    cwd = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(cwd, "README.md")) as f:
        return f.read()

setuptools.setup(
    name="pynaive",
    version="0.2.0",
    description="A toy project to demonstrate " \
                "Python development environment and toolchain",
    long_description=read_long_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/ktrushin/pynaive",
    author="Konstantin Trushin",
    author_email="konstantin.trushin@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    packages=["naive"],
    include_package_data=True,
    install_requires=[],
    entry_points={}
)
