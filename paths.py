import sys


def paths():
    print('\nPythonPaths\tFrom : ', __file__, '\n')
    for x in sys.path:
        print(x)


if __name__ == '__main__':
    paths()
