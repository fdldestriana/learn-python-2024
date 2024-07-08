# Created by : Fadly Destriana Rusmana
# Date : 2024-07-07
# Description : Learn the exception in python

# decorator in python is used to add functionality of a function without modifying the existing code 
# function in python is a first class citizens, so it can be passed as an argument, variable etc
def plus_one(number):
    return number + 1

add_one = plus_one
print(add_one(5))

# defining function within a function for familiarize with decorator later
def plus_two(number):
    def add_two(number):
        return number + 2
    
    result = add_two(number)
    return result

print(plus_two(4))

# passing a function to another function as an argumnet
# we are gonna using function plus_one which has been declared above
def function_call(function):
    number_to_add = 5
    return function(number_to_add)

# we do not need to add parenthesis for plus_one here, because it is a higher order function
print(function_call(plus_one))
# the code below would resulting the TypeError 
# print(function_call(plus_one(1)))

# returning another fucntion from a function
def function_hello():
    def say_hi():
        return "Hi"

    return say_hi

# the function_hello below returning the say_hi
# so the variable hello should have the parenthesis to calling the say_hi() that returned
hello = function_hello()
print(hello())

# the critical point to get along with decorator is by understanding the enclosing function
def print_message(message):
    "Enclosing function"
    def message_sender():
        "Nested function"
        print(message)

    message_sender()

print_message("some random message")

# decorator in python
def uppercase_string(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    
    return wrapper

def say_hi():
    return "Hi there"

decorate = uppercase_string(say_hi)
print(decorate())

# a simple way to apply decorator
@uppercase_string
def say_hello():
    return "Hello there"

print(say_hello())

# applying multiple decorator, the functions called in order
def split_string(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string
    
    return wrapper

# the order of decorator can be see below
# @lastdecorator
# @middledecorator
# @firstdecorator
# def function_name():
#     pass

@split_string
@uppercase_string
def greet():
    return "hi there"

print(greet())

# accepting arguments in decorator functions
def decorator_with_arguments(function):
    def wrapper_accepting_arguments(arg1, arg2):
        print("My arguments are: {0} {1}".format(arg1, arg2))
        function(arg1, arg2)
    return wrapper_accepting_arguments

@decorator_with_arguments
def cities(city1, city2):
    print("Cities I love are {0} and {1}".format(city1, city2))

cities("Nairoby", "Accara")

# defining the general decorator
def a_decorator_passing_arbitrary_arguments(function_to_decorate):
    def wrapper_accepting_arbitrary_arguments(*args, **kwargs):
        print("The positional arguments are", args)
        print("The keyword arguments are", kwargs)
        function_to_decorate(*args, **kwargs)
    return wrapper_accepting_arbitrary_arguments

@a_decorator_passing_arbitrary_arguments
def function_with_no_argument():
    print("No arguments here.")

function_with_no_argument()

@a_decorator_passing_arbitrary_arguments
def function_with_arguments(a, b, c):
    print(a, b, c)

function_with_arguments(1,2,3)

@a_decorator_passing_arbitrary_arguments
def function_with_keyword_arguments(**kwargs):
    print("This has shown keyword arguments", kwargs)

function_with_keyword_arguments(first_name="Derrick", last_name="Mwitti")

# passing arguments to the decorator
def decorator_maker_with_arguments(decorator_arg1, decorator_arg2, decorator_arg3):
    import functools
    def decorator(func):
        @functools.wraps(func)
        def wrapper(function_arg1, function_arg2, function_arg3) :
            "This is the wrapper function"
            print("The wrapper can access all the variables\n"
                  "\t- from the decorator maker: {0} {1} {2}\n"
                  "\t- from the function call: {3} {4} {5}\n"
                  "and pass them to the decorated function"
                  .format(decorator_arg1, decorator_arg2,decorator_arg3,
                          function_arg1, function_arg2,function_arg3))
            return func(function_arg1, function_arg2,function_arg3)

        return wrapper

    return decorator

pandas = "Pandas"
@decorator_maker_with_arguments(pandas, "Numpy","Scikit-learn")
def decorated_function_with_arguments(function_arg1, function_arg2,function_arg3):
    "This the doc of this function"
    print("This is the decorated function and it only knows about its arguments: {0}"
           " {1}" " {2}".format(function_arg1, function_arg2,function_arg3))

decorated_function_with_arguments(pandas, "Science", "Tools")
print(decorated_function_with_arguments.__name__)
print(decorated_function_with_arguments.__doc__)








