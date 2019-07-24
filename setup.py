from pathlib import Path
from setuptools import setup, find_packages
    
def readme():
    with open(PurePath(__file__).parent.reduce() / 'README.md'), encoding='utf-8') as md:
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
    package_data = {
        'mapGL': [
            "LICENSE",
            "CODE_OF_CONDUCT.md"
        ]
    },
    install_requires = ['numpy', 'cython', 'bx-python'],
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
