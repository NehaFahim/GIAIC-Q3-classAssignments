# Arithmetic Operators
x = 30
y = 4
print("Arithmetic Operators:")
print("Addition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)
print("Division:", x / y)
print("Modulus:", x % y)
print("Exponentiation:", x ** y)
print("Floor Division:", x // y)            
print()

# Assignment Operators
a = 5
print("Assignment Operators:")
a += 3  # x = x + 3
print("x after += 3:", a)
a -= 2  # x = x - 2
print("x after -= 2:", a)
a *= 2  # x = x * 2
print("x after *= 2:", a)
a /= 2  # x = x / 2
print("x after /= 2:", a)
print()

# Comparison Operators
print("Comparison Operators:")
print("a == b:", x == y)
print("a != b:", x != y)
print("a > b:", x > y)
print("a < b:", x < y)
print("a >= b:", x >= y)
print("a <= b:", x <= y)
print()

# Logical Operators
print("Logical Operators:")
print("True and False:", True and False)
print("True or False:", True or False)
print("not True:", not True)
print()

# Identity Operators
print("Identity Operators:")
c = [1, 2, 3]
d = [1, 2, 3]
e = c
print("c is d:", c is d)  # False (different objects)
print("c is e:", c is e)  # True (same object)
print("c is not d:", c is not d)  # True
print()

# Membership Operators
print("Membership Operators:")
my_list = [1, 2, 3, 4, 5]
print("2 in my_list:", 2 in my_list)
print("10 not in my_list:", 10 not in my_list)
print()

# Bitwise Operators
p = 6  # 110 in binary
q = 3  # 011 in binary
print("Bitwise Operators:")
print("p & q:", p & q)  # Bitwise AND
print("p | q:", p | q)  # Bitwise OR
print("p ^ q:", p ^ q)  # Bitwise XOR
print("~p:", ~p)  # Bitwise NOT
print("p << 1:", p << 1)  # Left shift
print("p >> 1:", p >> 1)  # Right shift
