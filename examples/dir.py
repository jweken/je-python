"""
Module dir.py
    Creates a class and a function and then
    shows the atrributes with dir()
"""


class X:
    pass


Z = dir(X)


def XX():
    pass


Z1 = dir(XX())

if __name__ == "__main__":
    print(__doc__)
    print(Z,"\n\n",Z1)
    print(Z[len(Z)-1], "\nPath = ", __file__)
