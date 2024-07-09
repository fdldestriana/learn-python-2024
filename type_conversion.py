# Created by : Fadly Destriana Rusmana
# Date : 2024-07-07
# Description : Learn type convertion in python

integer_number = 123
float_number = 1.23

# implicit type convertion
new_number = integer_number + float_number
print(f'New integer number {new_number}')
print("Data type", type(new_number))

# explicit type convertion
num_string = '12'
num_integer = 23
num_string = int(num_string)

print("Data type num_string after type casting", type(num_string))
