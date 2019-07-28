import os
from setuptools import setup, find_packages
from dummyfm.version import get_version

setup(
    name='Dummy Forward Model',
    version=get_version(),
    description='Dummy forward model for illustration purpose',
    url='https://github.com/mfkasim91/dummy-forward-model',
    author='mfkasim91',
    author_email='firman.kasim@gmail.com',
    license='MIT',
    packages=find_packages(),
    python_requires=">=2.7",
    install_requires=[
        "numpy>=1.8.2",
        "scipy>=0.15",
        "matplotlib>=1.5.3",
    ],
    entry_points={
        "console_scripts": [
            "dummyfm=dummyfm.main:main"
        ]
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Physics",
        "Topic :: Scientific/Engineering :: Mathematics",
        "License :: OSI Approved :: MIT License",

        "Programming Language :: Python :: 2.7"
    ],
    keywords="simulation dummy",
    zip_safe=False
)
