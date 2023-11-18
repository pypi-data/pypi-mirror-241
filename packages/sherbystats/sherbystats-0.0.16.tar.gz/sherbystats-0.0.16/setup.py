import setuptools


setuptools.setup(
    name="sherbystats",
    version="0.0.16",
    author="Ryan Gosselin",
    author_email="ryan.gosselin@usherbrooke.ca",
    url="https://www.usherbrooke.ca/gchimiquebiotech/departement/professeurs/ryan-gosselin/",
    packages=["sherbystats"],
    description="Ryan @ UdeS",
    long_description="Python for GCH711:\
    \n\
    \nanova\
    \nbinaire\
    \nbinaire3D\
    \ndoe\
    \nmlr\
    \nnormplot\
    \ternaire\
    \nxlsread",
    long_description_content_type="text/markdown",
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)