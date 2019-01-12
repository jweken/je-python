# This compiles *.py recursively, starting from the current directory
# Look for documentation in:

from compileall import compile_dir

compile_dir('.', force=True)
