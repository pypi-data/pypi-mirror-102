import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="ezinputs",
    version="1.0.0",
    description="Easily manage getting user inputs for all data types",
    long_description=README,
    long_description_content_type="text/markdown",
    author="Will Johnson",
    license="MIT",
    packages=["ezinputs"]
)
