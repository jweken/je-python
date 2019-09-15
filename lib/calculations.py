from math import *
from decimal import *
from random import *


def randombytes(x: int):
    """ a list of x random bytes
    """

    bytelist = []
    for p in range(0, 255, 1):
        bytelist.append(p)

    bytelist = choices(bytelist, k=x)
    return bytelist


if __name__ == '__main__':
    randombytes(16)
