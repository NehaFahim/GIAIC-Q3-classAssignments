# Python Special Keywords 

# 1. Control Flow Keywords (Program ka flow control karte hain)
x = 10

if x > 5:  # Agar x 5 se bada hai toh yeh chalega
    print("x is greater than 5")

for i in range(3):  # Loop jo 3 baar chalega
    print(f"Loop iteration {i}")

# 2. Exception Handling Keywords (Errors ko handle karte hain)
try:
    result = 10 / 0  # Yeh error dega (ZeroDivisionError)
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

# 3. Function & Class Keywords (Functions aur Objects banane ke liye)
def greet(name):
    """Yeh function naam ko print karega"""
    return f"Hello, {name}!"

print(greet("Students"))

class Student:
    """Yeh ek class hai jo student ka naam store karegi"""
    def __init__(self, name):
        self.name = name

student1 = Student("Ali")
print("Student Name:", student1.name)
