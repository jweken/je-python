import os

directories = os.walk('.')

for dirs, subdirs, filenames in directories:
    print(dirs)
