# Created by : Fadly Destriana Rusmana
# Date : 2024-07-09
# Description : Learn the modules concept in python

def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+ b
    print()

def fib2(n):
    result = []
    a, b = 0, 1
    while a < n:
        a, b = b, a + b
    return result

# this code below will automatically run the module by just importing it
# if __name__ == "__main__":
#     import sys
#     fib(int(sys.argv[1]))

# import standart math module
import math
print("The value of pi is", math.pi)

# import with renaming
import math as m
print((m.pi))

# import only from 
from math import pi
print(pi)

# import all names
from math import *
print(pi)

# the dir
import math
print(dir(math))
print((math,__name__))















