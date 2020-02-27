"""
Module dir.py
    Creates a class and a function and then
    shows the atrributes with dir()
"""


class SomeClass:
    pass


def SomeFunction():
    pass


classattributes = dir(SomeClass)
functionattributes = dir(SomeFunction())

if __name__ == "__main__":
    print(__doc__)
    print(classattributes, "\n\n", functionattributes)
    print(classattributes[len(classattributes)-1], "\nPath = ", __file__)
