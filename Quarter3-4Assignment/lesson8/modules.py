# 1. Built-in Modules (Example: math)
import math
print("Square root of 34:", math.sqrt(34))
print("Value of Pi:", math.pi)

# 5. Functions in Python
# (a) Defining a Global Function
def my_function():
    print("Hello! World")

# Calling the function
my_function()

# (b) Function with Arguments and Return Value
def multiply(x, y):
    return x * y

print("Multiplication of 5 and 4:", multiply(5, 4))

# (c) Function with Default Parameters
def greet(name="Guest"):
    print("Hello,", name)

greet("Albert")
greet()




# 1) Built-in Functions
print("Hello! World")

# 2) Functions defined in built-in modules
import random
print(random.random())

# 3) User-defined Functions
def my_function():
    print("Hello! Student of GIAIC")

my_function()

# Function with a return statement
def greetings():
    "This is a function that returns a greeting message."
    return "Hello World!"

message = greetings()
print(message)

# Function Arguments
def greetings(name):
    print("Hello {}".format(name))

greetings("Ali")
greetings("Omar")
greetings("Usman")

# Keyword Arguments
def printinfo(name, age):
    print("Name:", name)
    print("Age", age)

printinfo(age=50, name="Arif")

# Default Arguments
def printinfo(name, age=35):
    print("Name:", name)
    print("Age", age)

printinfo(age=50, name="Arif")
printinfo(name="Arif")

# Calling function with different arguments
my_function(fname="Ali", lname="Osman")
my_function(fname="Ali", lname="Osman", course="Python - 101", day="Saturday", time="1400 - 1800")
my_function(fname="Arif", lname="Rozani", course="101 - 201", day="Saturday | Sunday", role="Student")

# Generator Function
def simple_generator():
    yield 1
    yield 2
    yield 3

# Create a generator object
gen = simple_generator()
print(gen, " : ", type(gen))

# Iterate over the generator
for value in gen:
    print(value, " : ", type(value))

# Recursive Function: Factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Example usage
print(f"Factorial of 5 is {factorial(5)}")

# Recursive Function: Fibonacci Sequence
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Example usage
print(f"Fibonacci of 6 is {fibonacci(6)}")



