import random

x = random.__doc__
__doc__ = "module tryit"
print(x)
y = (__doc__, __name__, __file__)
print(f'type(y) {type(y)} y = {y}')
