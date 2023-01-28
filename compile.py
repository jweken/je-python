"""compile"""

from compileall import compile_dir
# This compiles *.py recursively, starting from the current directory
# Look for documentation in:


compile_dir('.', force=True)
