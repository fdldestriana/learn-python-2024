# Created by : Fadly Destriana Rusmana
# Date : 2024-07-09
# Description : Learn the magic methods in python

# the dunder are not able to be called individually, they must be called from the class
from re import X


num = 10
res = num.__add__(5)
print(res)

# __new__ method, called first while instantiating a class, then call the __init__ method
class Employee:
    def __new__(cls):
        print("__new__ magic method is called")
        inst = object.__new__(cls)
        return inst
    
    def __init__(self):
        print("__init__ magic method is called")
        self.name = 'Satya'
        self.salary = 1000

    def __str__(self):
        return 'name : ' + self.name + ' salary : ' + str(self.salary)

satya = Employee()

# __str__ method, like toString in Dart
num = 12
val = int.__str__(num)
print(type(val))
print(satya)

# __ge__ mehtod, this is the method that use in the operator >=
class Distance:
    def __init__(self, x, y):
        self.ft = x
        self.inch = y

    def __ge__(self, x):
        val1 = self.ft * 12 + self.inch
        val2 = x.ft * 12 + x.inch
        if val1 >= val2:
            return True
        else: 
            return False

d1 = Distance(2, 1)
d2 = Distance(4, 10)
print(d1>=d2)





