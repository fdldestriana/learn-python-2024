# Created by : Fadly Destriana Rusmana
# Date : 2024-07-07
# Description : Learn the exception in python

# exception occures even in syntatically correct code
# zerro division error
# print(0/0)

# create a custom exception object and throw it using raise keyword
def create_zero_division_error():
    numerator = input("Please input the numerator: ")
    denominator = input("Please input the denominator: ")

    numerator = int(numerator)
    denominator = int(denominator)
    if denominator == 0:
        raise Exception(f"The denominator should not be zerro: {denominator}")
    return numerator / denominator

def create_zero_division_error_assert():
    numerator = input("Please input the numerator: ")
    denominator = input("Please input the denominator: ")

    numerator = int(numerator)
    denominator = int(denominator)
    assert(denominator > 0), f"The denominator should not be zerro {denominator}"

    return numerator/denominator


print(create_zero_division_error())
print(create_zero_division_error_assert())

# in production, we optimize the code and the assertion can be removed by the reason of optimization
# assertion is good for debugging, but don't use it in prodcution
# if we use bare except, all the exceptions will be catched as Exception, and it can hide the errorrs
# so it is recommend to catch the specific exception
# if the code did not encounter any exceptions, we can use else
def linux_interaction():
    import sys 
    if "linux" not in sys.platform:
        raise RuntimeError("Function can only run on Linux system.")
    print("Doing Linux things.")

def windows_interaction():
    import sys
    if "windows" not in sys.platform:
        raise PlatformException("Function can only run on Windows system.")
    print("Doing Windows things.")

# creatig custom exception
class PlatformException(Exception):
    """Incompatible platform"""

try:
    linux_interaction()
except:
    print("The Linux function was not executed")
else:
    # we can attempt to make a nested try...catch block within this else
    print("Doing even more Linux things.")
finally:
    # use finally to do anything wether there is any exception or not, it can be used to disposed the connection to db or some file
    print("Cleaning up, irrespective of any exceptions.")

try:
    windows_interaction()
except PlatformException as err:
    print(err) 
    print("The Windows function was not executed")





























