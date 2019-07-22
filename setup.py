from pathlib import PurePath
from setuptools import setup, find_packages, Extension
import numpy as np

    
def readme():
    with open(PurePath(__file__).parent.absolute() / 'README.md'), encoding='utf-8') as md:
        return md.read()

    
setup(
    name = "mapGL",
    version = "0.0.1",
    author = "Adam Diehl",
    author_email = "adadiehl@umich.edu",
    description = "Prediction of lineage-specific gain and loss of sequence elements using phylogenetic maximum parsimony.",
    long_description = readme(),
    long_description_content_type = "text/markdown",
    url = "https://github.com/adadiehl/mapGL",
    packages = find_packages(),
    
    
    # It is better to provide the *.c files that are
    # constructed on the build system instead of *.pyx
    # files. This is because you don't want to assume that
    # the end-user has Cython or wants to use Cython to
    # build your package. http://docs.cython.org/en/latest/src/userguide/source_files_and_compilation.html#distributing-cython-modules 
    ext_modules = [Extension("*", ["*.c"])], # Use globs here to capture all your .c files
    include_dirs = [np.get_include()]
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
    # zip_safe = False,
)
