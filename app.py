import tests.covidtest as covidtest
import lib.covid

from named_unicode import random_example
from paths import showpaths
from private.tryout import sinh, cosh

showpaths()
random_example()
result = sinh(45)/cosh(45)
print(f'tanh(45) = {result}')
