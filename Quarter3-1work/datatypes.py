# Numeric Types - These store numbers  
integer_num = 7  # int (A whole number)  
print(integer_num)  

float_num = 3.141  # float (A decimal number)  
print(float_num)

complex_num = 3 + 4j  # complex (A number with real and imaginary parts)  
print(complex_num)

# would you like to know this values with their types you write this:
print(type(integer_num))
print(type(float_num))
print(type(complex_num))



# Sequence Types - These store ordered collections  
string_value = "Hello world"  # str (A sequence of characters)  
print(string_value)

list_values = [1, 2, 3, 4]  # list (A mutable sequence, can be changed) 
print(list_values)  # list values also write in string

list_values = ["sir","madam"]
print(list_values)  

tuple_values = (20, 30, 40)  # tuple (An immutable sequence, cannot be changed)  
print(tuple_values)

range_values = range(5)  # range (Generates numbers from 0 to 4)  
print(range_values)

# would you like to know this values with their types you write this:
print(type(string_value))
print(type(list_values))
print(type(tuple_values))
print(type(range_values))



# Set Types - These store unique, unordered collections  
set_values = {1, 2, 3, 4}  # set (Mutable, does not allow duplicates)
print(set_values)

frozen_set_values = frozenset({5, 6, 7})  # frozenset (Immutable set, cannot be changed)  
print(frozen_set_values)

# Mapping Type - Stores key-value pairs  
dictionary_values = {"name": "Neha", "age": 23}  # dict (Mutable, allows key-value access)  
print(dictionary_values)

# Boolean Type - Stores True or False values  
is_python = True  # bool (Represents a truth value) 
print(is_python)

is_difficult = False # bool (Represents a false value)
print(is_difficult)
# would you like to know this values with their types you write this:
print(type(set_values))
print(type(frozen_set_values))
print(type(dictionary_values))
print(type(is_python))
print(type(is_difficult))


# None Type - Represents the absence of a value  
empty_value = None  # NoneType (Used when a variable has no value)  
print(empty_value)







# you have to write this code in other syntax like this:

# Numeric Types 
num:int = 40
print(num)

float_num:float = 40.5
print(float_num)

complex_num:complex = 2 + 3j 
print(complex_num)

# And also know their types :
print(type(num))
print(type(float_num))
print(type(complex_num))

# Sequence Types 
str_values:str = "HELLO,GIAIC Students" # str (Sequence of characters)
print(str_values)

subjects:list[str] = ["Maths", "English", "Accounting"] # list (Ordered collection)
print(subjects)

tuple_data:tuple = ("Apple", "Mango", "Orange")
print(tuple_data)

# And also know their types :
print(type(str_values))
print(type(subjects))
print(type(tuple_data))

# Set Types
set_values: set[int] = {1, 2, 3, 4}  # set (Mutable, unordered)
print(set_values)

frozen_set_values: frozenset[int] = frozenset({5, 6, 7})  # frozenset (Immutable set)
print(frozen_set_values)

# And also know their types :
print(type(set_values))
print(type(frozen_set_values))


# Mapping Type
dictionary_values: dict[str, int] = {"name": "Neha", "FatherName": "Muhammad Fahim"}  # dict (Key-Value pairs)
print(dictionary_values)

print(type(dictionary_values))

# Boolean Type
is_python_easy: bool = True  # boolean
print(is_python_easy)

print(type(is_python_easy))