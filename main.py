""" 
    This is random text
    in main.py
 """


def ShowBasicInfo():
    print(__doc__)
    print(__file__)


def _test():
    import doctest
    doctest.testmod()


if __name__ == "__main__":
    ShowBasicInfo()
    _test()
