import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="einnovationlabs-python-lib",
    version="0.0.1",
    author="Developer Team",
    author_email="dev@einnovationlabs.com",
    description="A package for e-innovation labs' utility functions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/einnovationlabs/einnovationlabs-python-lib",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)