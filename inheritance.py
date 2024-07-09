# Created by : Fadly Destriana Rusmana
# Date : 2024-07-08
# Description : Learn the exception in python

# parent class called base class 
# child class called derived class

# create parent class
class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def print_name(self):
        print(self.fname, self.lname)

x = Person('John', 'Doe')
x.print_name()

# create child class
class Student(Person):
    # there are two ways to override the init function but still inherit the parent's
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        # add property
        self.graduate_year = year

    # def __init__(self, fname, lname):
    #     Person.__init__(fname, lname)
    #     self.graduate_year = 2019

    # add method
    def wellcome(self):
        print("Wellcome", self.fname, self.lname, "to the class of", self.graduate_year)

y = Student('Mike', 'Olsen', 2019)
y.print_name()
y.wellcome()
print((y.graduate_year))

# another example
class Animal:
    def speak(self):
        print("Animal speaking")

class Dog(Animal):
    def bark(self):
        print("Dog barking")
    
    # method overriding
    def speak(self):
        print("Animal barking")


d = Dog()
d.bark()
d.speak()

# multilevel inheritence
class DogChild(Dog):
    def eat(self):
        print("Eating bread ...")

e = DogChild()
e.bark()
e.speak()
e.eat()

# multiple inheritence
class Calculation1:
    def summation(self, a, b):
        return a + b

class Calculation2:
    def multiplication(self, a, b):
        return a * b

class Derived(Calculation1, Calculation2):
    def divide(self, a, b):
        return a / b

derived = Derived()
print(derived.summation(1, 2))
print(derived.multiplication(1, 2))
print(derived.divide(1, 2))

# issubclass function
print(issubclass(Derived, Calculation2))
print(issubclass(Calculation1, Calculation2))

# isinstance function
print(isinstance(derived, Derived)) # -> TRUE
print(isinstance(derived, Calculation1)) # -> TRUE

# real life example of method overriding
class Bank:
    def getroi(self) -> int:
        return 10

class SBI(Bank):
    def getroi(self) -> int:
        return 7

class ICICI(Bank):
    def getroi(self) -> int:
        return 8

b1 = Bank()
b2 = SBI()
b3 = ICICI()

print(b1.getroi())
print(b2.getroi())
print(b3.getroi())

# data abstraction
class Employee:
    __count = 0
    def __init__(self) -> None:
        Employee.__count = Employee.__count + 1

    def display(self):
        print(("The number of the employees are : ", Employee.__count))

emp1 = Employee()
emp2 = Employee()

print(emp1.display()) # -> 2
print(emp2.display()) # -> 2
# the employess would be 2 because the private __count is a class variable that shared along the objects
print(emp1.__count)
print(emp2.__count)
