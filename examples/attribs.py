"""
Module attribs.py
    Creates a class and a function and then
    shows the attributes with dir()
"""

class SomeClass:
    pass

def SomeFunction():
    pass

classattributes = dir(SomeClass)
functionattributes = dir(SomeFunction())

if __name__ == "__main__":
    print(__doc__)
    print(f"classattributes of SomeClass: \n{classattributes}\n\nfunctionattributes of SomeFunction:\n{functionattributes}\n")
    print(f"Last Class-attrib = {classattributes[len(classattributes)-1]}\n\nPath = ", __file__)
