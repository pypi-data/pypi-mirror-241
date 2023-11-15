Kringle
=======

|PyPI Version| |PyPI - Python Version|

A solution manager for Advent of Code.

Usage 
-----

Kringle is opinionated. It expects that it is being run from within a directory with the
following structure::

    - cwd
    |
    | - solution.py
    | - input.txt

Within solution.py, it expects three functions:

``parse(data: str)``: Takes the contents of the input.txt file as a string, and returns
the parsed data.

``part_1()``: Solves part 1 of the challenge.

``part_2()``: Solves part 2 of the challenge.
    
In order to run the solution, call ``kringle`` from within the directory containing the
solution and input files.

.. |PyPI Version|
    image:: https://img.shields.io/pypi/v/northpole.svg
    :target: https://pypi.org/project/northpole

.. |PyPI - Python Version|
    image:: https://img.shields.io/pypi/pyversions/northpole.svg
    :target: https://pypi.org/project/northpole