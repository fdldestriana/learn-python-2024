# Created by : Fadly Destriana Rusmana
# Date : 2024-07-11
# Description : Learn list comprehension in python

# with list comprehension we can create a list base on an existing list
# if we do not use list comprehension, while we want to create
# a list from fruits that contains a letters, we have to use for loop


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)

# using list comprehension
# the syntax newfruits = [expression for item in iterable if condition == True]
newfruits = [x for x in fruits if "a" in x]
apples = [x for x in fruits if x == "apple"]
print(newfruits)
print(apples)

fruits2 = [x for x in fruits]
print(fruits2)

numbers = [x for x in range(10)]
print(numbers)

# numbers with if statement
numbers2 = [x for x in range(10) if x < 5]
print(numbers2)

# upper name fruits
fruits_upper = [x.upper() for x in fruits]
print(fruits_upper)
hellos = ["hello" for x in fruits]
print(hellos)

newfruits2 = [x if x != "banana" else "orange" for x in fruits]
print(newfruits2)

# more on list comprehension
squares = []
for x in range(10):
    squares.append(x**2)
print(squares)

# the same way
squares2 = list(map(lambda x: x**2, range(10)))
print(squares2)

# using list comprehension
squares3 = [x**2 for x in range(10)]
print(squares3)
