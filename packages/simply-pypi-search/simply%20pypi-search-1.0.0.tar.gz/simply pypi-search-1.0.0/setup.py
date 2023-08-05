import pathlib
import setuptools
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="simply pypi-search",
    version="1.0.0",
    description="A simply tool to search for packages on pypi.org",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/mccoderpy/simply-pypi-search",
    author="mccoder.py",
    author_email="mccuber04@outlook.de",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    include_package_data=True,
    install_requires=["aiohttp", "bs4"],
    python_requires=">=3.6"
)