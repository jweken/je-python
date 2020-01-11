from lib.calculations import *
try:
    result = Decimal(220)/Decimal(70.01)
except ZeroDivisionError as err:
    print('Division by Zero error in ', __file__, ':(4,35)')
else:
    print(result != pi)

r = range(0, 110, 1)
for x in r:
    p = result - Decimal(x*0.00001)
    if p <= pi:
        print(x, p)
        break

# this prints a large integer value
# a to the power b
k = 789**719
print(f'Print the result of k = 789**719:\n{k}')

print('type of "result" :=', type(result))
print(sin(pi*(3/2)))
print(randombytes(16))

if __name__ == '__main__':
    ()
