# Data Types

# Numeric Types 

# int 
data = 10
print(type(data))

# float
data = 10.5
print(type(data))

# complex 
data = 3 + 5j
print(type(data))

# string
data = "python"
print(type(data))

# boolean 
data = False
print(type(data))

# List (homogenous data)
data = [10,20,30,40,50]
data = [101,"Ravi",True] 
print(type(data))

# Tuple (heterogenous data)
data = (101,"Ravi",True)
data = (10,20,30,40,50)
print(type(data))

# Set 
data = {10,20,30,40,50}
print(type(data))

# Dictionary
data = {"name":"Ravi", "id":101, "location":"hyd"}
print(type(data))

# None Type
x = None
print(type(x))

# User defined datatype
class Student:
    # logics
    pass # syntax 
student_john = Student()
print(type(student_john)) # <class '__main__.Student'> --> __main__ indicates user defined datatype

# Type Conversion 
a = 10 # int 
print(type(a))
b = 3.5 # float
print(type(b)) 
c = a + b # dynamic 
print(c)
print(type(c))

# Type Casting
pi = 3.14 # float 
print(type(pi))
print(pi) 

# req round of pi and give whole number
pi_round_int = int(pi)
print(type(pi_round_int))
print(pi_round_int) 

rating = "4"
print(type(rating))
# increment_rating = rating + 1 # TypeError: can only concatenate str (not "int") to str
increment_rating = int(rating) + 1
print(increment_rating)
print(type(increment_rating))

new_rating = "four" # incompatible conversion 
print(type(rating))
# increment_rating = new_rating + 1 # TypeError: can only concatenate str (not "int") to str
# increment_rating = int(new_rating) + 1 # ValueError: invalid literal for int() with base 10: 'four'

num = 10
print(type(10))