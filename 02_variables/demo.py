# Working With Variables

# Assigning Data
student_name = "ravi"
student_age = 20
student_gpa = 9.5
student_passed = True

# Retrieve Data
print(student_name)
print(student_age)
print(student_gpa)
print(student_passed)

# Get Identity / Memory Address
print(id(student_name))
print(id(student_age))
print(id(student_gpa))
print(id(student_passed))

# Get Type Of Data
print(type(student_name))
print(type(student_age))
print(type(student_gpa))
print(type(student_passed))

# In python a variable can change during the execution 
dynamic_data = 10
print(type(dynamic_data))
dynamic_data = "10"
print(type(dynamic_data))
dynamic_data = 10.0
print(type(dynamic_data))
dynamic_data = True
print(type(dynamic_data))

# Python Memory Model
a = 10
print(id(a))
b = 20
print(id(b))
c = 10
print(id(c))

# a,b,c int values which is simple data type (one only value)

# python has complex data types (more than one value)

list_nums_a = [10,20,30,40,50] # list is created using [value1,value2,....,value-n]
print(type(list_nums_a))
print(id(list_nums_a))

list_nums_b= [10,20,30,40,50]
print(type(list_nums_b))
print(id(list_nums_b))

# To access data inside list we use index -> index starts from 0 1 2 ...
#  0. 1. 2. 3. 4. 
# [10,20,30,40,50]
print(list_nums_a) # print entire list 
print(list_nums_b) # print entire list 

print(list_nums_a[0])
print(list_nums_b[2])

print(id(a))
print(id(c))
print(id(list_nums_a[0]))
print(id(list_nums_b[0]))

# Observations to be made 
x = "Python "
y = "is "
z = "easy"

# print(xyz) # NameError: name 'xyz' is not defined

# print Python is easy
print(x+y+z) # Concatenation

x = 10
y = 20
z = 30

print(x+y+z) # Addition Operator

# name and age
name = "Ravi"
age = 20
# print("My name is "+name+ " and my age is "+age) # TypeError: can only concatenate str (not "int") to str

# My name is Ravi and my age is 20

# old style of python
print("My name is ",name + " and my age is ",age)

# print("My name is ",name + " and my age is ",age + "after 5 years my age is ",age+5)
# TypeError: unsupported operand type(s) for +: 'int' and 'str'

# new style of python (f-strings)
print("My name is {name} and my age is {age} after 5 years my age is {age+5}") # no f-strings

print(f"My name is {name} and my age is {age} after 5 years my age is {age+5}") # f-strings

# working with multiple variables
x = 10
y = 20
z = 30
print(x)
print(y)
print(z)

# above can also be done
x,y,z = 10,20,30 # always LHS == RHS
print(x)
print(y)
print(z)

# x,y,z = 10,20,30,40 # ValueError: too many values to unpack (expected 3)
print(x)
print(y)
print(z)

a = 10
b = 20
c = 10
d = 10

a = c = d = 10
print(a)
print(c)
print(d)