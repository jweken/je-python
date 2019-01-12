#! usr/bin/env python

"""
Demonstrates the range() builtin-function
"""


def squaredemo(arg: None):
    """Print the square of the first 'arg' integers."""

    print("\nde naam van het bestand: ", __file__, "\n")
    squares = []
    if arg != None:
        for x in range(0, arg):
            squares.append(x*x)
    return squares
