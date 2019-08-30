__doc__ = """ Module paths is an experimental module

"""
import sys


def paths():
    """ Print the paths from sys.path\n 
            this is a local method made by JW.Eken\n
            it has no special meaning, so if you want
            to get rid of it, \n!!! BE MY GUEST !!!
    """
    print('\nPythonPaths\tFrom : ', __file__, '\n')
    for key in sys.path:
        print(key)


if __name__ == '__main__':
    paths()
