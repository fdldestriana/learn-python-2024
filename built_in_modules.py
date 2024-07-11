# Created by : Fadly Destriana Rusmana
# Date : 2024-07-09
# Description : Learn the built in modules in python

# we can gather information of all modules that are available with help('module') on the python interpreter
import math
print(math.sqrt(100))
print(math.radians(30))
print(math.degrees(math.pi/6))
print(math.log(10))
print(math.e**100)
print((math.pow(4,4)))

import os
os.mkdir("./tempdir/")
os.rmdir("./tempdir/")
print(os.getcwd())
print(os.listdir("/home/fadly/portfolios"))

import random
print(random.random())
print(random.randint(1, 100))
print(random.randrange(1, 10))
print(random.randrange(1, 10, 2))
print(random.choice('computer'))
print(random.choice([12,23,45,56,67,65,43]))
print(random.choice([12,23,45,56,67,65,43]))
numbers = [12,23,45,56,67,65,43]
random.shuffle(numbers)
print(numbers)

import sys
print(sys.version)
print(sys.path)
