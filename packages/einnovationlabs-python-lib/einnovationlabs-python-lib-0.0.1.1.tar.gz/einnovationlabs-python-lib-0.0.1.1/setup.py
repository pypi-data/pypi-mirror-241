import setuptools
from einnovationlabs.version import __version__


def get_description():
    with open("README.md", "r") as fh:
        return fh.read()

setuptools.setup(
    name="einnovationlabs-python-lib",
    version=__version__,
    author="einnovationlabs Developer Team",
    author_email="dev@einnovationlabs.com",
    description="A package for einnovationlabs' utility functions",
    long_description=get_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/einnovationlabs/einnovationlabs-python-lib",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
