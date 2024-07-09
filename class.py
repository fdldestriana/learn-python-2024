# Created by : Fadly Destriana Rusmana
# Date : 2024-07-08
# Description : Learn the exception in python

class MyClass:
    """"A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'

x = MyClass()
print(x.i)
print(x.f())
print(x.__doc__)

class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

y = Complex(realpart=3.0, imagpart=-4.5)
z = Complex(realpart=3.0, imagpart=-4.5)
print(y.r)
print(y.i)
print(str(y))

print(z.r)
print(z.i)
print(str(z))

class Dog:
    # class variable, in Dart it might a static variable
    kind = 'canine'

    def __init__(self, name) -> None:
        self.name = name
        self.tricks = []

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')
print(d.kind)
print(e.kind)
print(d.name)
print(e.name)

d.add_trick('run')
d.add_trick('jump')
d.add_trick('frisbee')
print(d.tricks)
print(e.tricks)

# inheritance
class Pitbull(Dog):
    pass

jack = Pitbull('Jack')
print(jack.name)
print(jack.tricks)
jack.add_trick('climb')
print(jack.tricks)

# multiple inheritance
class Base1:
    pass

class Base2:
    pass

class Base3:
    pass

class DerivedClassName(Base1, Base2, Base3):
    pass

# private variable
class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for i in iterable:
            self.items_list.append(i)

    __update = update

map = Mapping(["1, 2, 3"])
map2 = Mapping(["4, 5, 6"])
print(map.items_list)
print(map2.items_list)






