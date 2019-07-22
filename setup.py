from os import path
from setuptools import setup


def version_info():
    here = path.abspath(path.dirname(__file__))
    with open(path.join(here, 'version'), encoding = 'utf-8') as vers:
        return vers.read().strip()

    
def readme():
    here = path.abspath(path.dirname(__file__))
    with open(path.join(here, 'README.md'), encoding='utf-8') as md:
        return md.read()

    
setup(
    name = "mapGL",
    version = version_info(),
    author = "Adam Diehl",
    author_email = "adadiehl@umich.edu",
    description = "Prediction of lineage-specific gain and loss of sequence elements using phylogenetic maximum parsimony.",
    long_description = readme(), # https://packaging.python.org/guides/making-a-pypi-friendly-readme/#including-your-readme-in-your-package-s-metadata
    long_description_content_type = "text/markdown",
    url = "https://github.com/adadiehl/mapGL",
    packages = setuptools.find_packages(),
    classifiers = [
        "Programming Language :: Python :: 3",
        "Programming Language :: Cython",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
