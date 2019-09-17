from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="squacapipy",
    version="0.1",
    author="Jon Connolly",
    author_email="joncon@uw.edu",
    description="A python packagae for SQAUC API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pnsn/squacapipy",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
