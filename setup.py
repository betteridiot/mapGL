from os import path
from setuptools import setup, find_packages

# Use setuptools instead of distutils because it preferentially ignores pyx files
# opting to use .c files instead
from setuptools.extension import Extension


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
    long_description = readme(),
    long_description_content_type = "text/markdown",
    url = "https://github.com/adadiehl/mapGL",
    packages = find_packages(),
    classifiers = [
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "Programming Language :: Cython",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Natural Language :: English"
    ],
    keywords = "words about your project",
    include_package_data = True,
    zip_safe = False,
)
