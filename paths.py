__doc__ = """ Module paths is an experimental module

"""
import sys


def paths():
    """ Print the paths from sys.path 
            this is a local method made by JW.Eken
            it has no special meaning, so if you want
            to get rid of it, !!! BE MY GUEST !!!
    """

    print('\nPythonPaths\tFrom : ', __file__, '\n')
    for key in sys.path:
        print(key)


if __name__ == '__main__':
    paths()
    
