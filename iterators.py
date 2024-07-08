# Created by : Fadly Destriana Rusmana
# Date : 2024-07-07
# Description : Learn iterators in python

# Iterator is an object that contains a countable number of values
# iterator is an object that implements the iterator protocol, __iter__() and __next__()

# return an iterator from a tuple
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))

mystr = "banana"
myit = iter(mystr)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

# for loop actually creates an iterator object and execute __next__() for each loop
for i in mytuple:
    print(i)

for i in mystr:
    print(i)

class MyNumber:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass = MyNumber()
myiter = iter(myclass)

# it is safe if we use the for loop
for i in myiter:
    print(i)

# it is unsafe if we do not use the for loop, the exception would be raised
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))












