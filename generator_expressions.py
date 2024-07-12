# Created by : Fadly Destriana Rusmana
# Date : 2024-07-12
# Description : Learn expression generator in python
from sys import getsizeof

# creating list in python
my_list = [0, 1, 1, 2, 3]
# less preferrable
my_list = list()

string = "string"
list(string)
print(string)

# list comprehension
comp_list = [x * 2 for x in range(10)]
print(comp_list)
comp_list = [x**2 for x in range(7) if x % 2 == 0]
print(comp_list)

# the advance use of list comprehension is to combine two or more lists
nums = [1, 2, 3, 4, 5]
letters = ["A", "B", "C", "D", "E"]
nums_letters = [[n, l] for n in nums for l in letters]
print(nums_letters)

iter_string = "some text"
comp_list = [x for x in iter_string if x != " "]
print(comp_list)

# comprehension for dict
dict_comp = {x: chr(65 + x) for x in range(1, 11)}
print(type(dict_comp))
print(dict_comp)

# set comprehension
set_comp = {x**3 for x in range(10) if x % 2 == 0}
print(type(set_comp))
print(set_comp)

# benefits of using list comprehension
# 1. ease
# 2. improved execution speed
# 3. no modifications existing list, create new list

print(hasattr(comp_list, "__iter__"))
print(dir(comp_list))

# this is the behind process of the loop
iterable_string = iter(iter_string)
print(next(iterable_string))
print(next(iterable_string))
print(next(iterable_string))
print(next(iterable_string))
print(next(iterable_string))
print(next(iterable_string))
print(next(iterable_string))
print(next(iterable_string))
print(next(iterable_string))
# print(next(iterable_string)) would produce a traceback, StopIteration


# generator is an iterable that created using a function that uses yield statement
def my_gen():
    for x in range(5):
        yield x


gen = my_gen()
print(
    gen
)  # would print <generator object my_gen at 0x7cdb16d48350> differ from print(some_list)
for x in gen:
    print(x)

# take a look a the different if we print some list and some generator object
list_comp = [x**2 for x in range(10) if x % 2 == 0]
gen_exp = (x**2 for x in range(10) if x % 2 == 0)
print(list_comp)
print(gen_exp)

# the main advantage of using generator over the list is it takes much less memory
my_comp = [x * 5 for x in range(1000)]
my_gen = (x * 5 for x in range(1000))
print(getsizeof(my_comp))
print(getsizeof(my_gen))
