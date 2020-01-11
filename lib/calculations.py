from math import *
from decimal import *
from random import *


def randombytes(count: int):
    """ a list of x random bytes
    """

    bytelist = []
    for p in range(0, 255, 1):
        bytelist.append(p)

    bytelist = choices(bytelist, k=count)
    return bytelist


def randhex(size: int, case: any):
    list = randombytes(size)
    s = ""

    for item in list:
        if item < 16:
            s += '0'

        s += format(item, case)
    return s


if __name__ == '__main__':
    print(randombytes(32))
    hstr = '{'+randhex(4, 'x')+'-'+randhex(2, 'x')+'-'+randhex(2, 'x') + \
        '-'+randhex(2, 'x')+'-'+randhex(6, 'x')+'}'
    print(hstr, len(hstr))
    print(randhex(1024, 'X'))
