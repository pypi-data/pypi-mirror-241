from setuptools import setup, find_packages
import os


VERSION = '1.0'
DESCRIPTION = 'Single-cell data preprocessing for multiple samples.'


# Setting up
setup(
    name="scprel",
    version=VERSION,
    author="GPuzanov (Grigory Puzanov)",
    author_email="<grigorypuzanov@gmail.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['omnipath', 'infercnvpy', 'anndata', 'decoupler', 'hdf5plugin', 'scanpy', 'scrublet', 'adjustText', 'wget'],
    keywords=['python', 'single-cell', 'scRNA-seq', 'single-cell quality control', 'single-cell data preparation', 'single-cell multiple samples', 'samples concatenation'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)