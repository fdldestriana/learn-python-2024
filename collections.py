# Created by : Fadly Destriana Rusmana
# Date : 2024-07-07
# Description : Learn list, set, tuple and dictionary in python

# tuple is immutable
a_tuple = tuple(range(1000))
print("The size of a tuple", a_tuple.__sizeof__())
a_tuple = (1, 2, 3, 4, 5, 6, 6)
print(a_tuple)
for i in a_tuple:
    print(i)

# list is mutable
a_list = list(range(1000))
print("The size of a list", a_list.__sizeof__())
a_list = [1, 2, 3, 4, 5]
print(a_list)
for i in a_list:
    print(i)

# set is immutable and does not allow to contain duplicated data
a_set = set(range(1000))
print("The size of a set", a_set.__sizeof__())
# the second of number 5 would not be printed
a_set = {1, 2, 3, 4, 5, 5} 
print(a_set)
for i in a_set:
    print(i)

# dictionary is mutable and contains key-value pairs as it's data
a_dictionary = dict()
print("The size of a dict", a_dictionary.__sizeof__())
a_dictionary = {
    "one" : 1,
    "two" : 2,
    "three" : 3,
    "four" : 4,
    "five" : 5
}
for k in a_dictionary:
    print(k, a_dictionary[k])
