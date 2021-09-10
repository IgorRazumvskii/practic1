from math import *
a = int(input())
b = int(input())
c = int(input())
discr = (b * b) - (4 * a * c)

if discr > 0:
    print((-b + sqrt(discr)) / (2 * a))
    print((-b - sqrt(discr)) / (2 * a))
elif discr == 0:
    print((-b) / (2 * a))
else:
    print('Корней нет')