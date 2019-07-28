# Dummy forward model

This module contains a forward model that accepts `ni` parameters in a file
and returns `no` parameters in an output file. The input parameters are
values of points with equal separation from `0` to `1`. The output values are
the interpolated values at `no` points with equal separation from `0` to `1`.

## Requirements

* Python 2.7 or higher or Python 3.6 or higher

## Installation

    python -m pip install .

## Usage

    dummyfm <input-file>

where

* `<input-file>` is a file name that contains `ni` values separated by
   whitespaces

## Options

* `-n <num-output>` specifies the number of output values (default: 1000)
* `-o <output-file>` specifies the output file name (default: `output.txt`)
* `-t <interp-type>` specifies the interpolation type, either: `linear`,
  `quadratic`, or `cubic` (default: `quadratic`)
