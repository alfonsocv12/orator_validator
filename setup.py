import setuptools, sys

with open("README.rst", 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name="orator_validator",
    version="0.1.1",
    author="Alfonso Villalobos",
    author_email="alfonso@codepeat.com",
    long_description=long_description,
    packages=setuptools.find_packages(),
    classifiers=[
        "Progamming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.7'
)
