# Operators

# Arithmetic Operators
num1 = 3
num2 = 2
print(f"Sum of {num1} and {num2} is {num1+num2}")
print(f"Difference of {num1} and {num2} is {num1-num2}")
print(f"Product of {num1} and {num2} is {num1*num2}")
print(f"Division of {num1} and {num2} is {num1/num2}")
print(f"Modulus of {num1} and {num2} is {num1%num2}")

print(num1//num2)
print(num1**num2) # 3 ^ 2

# Compound Assignment Operators
num = 10
num = num + 5 # without Compound Assignment Operators
print(num)

num = 10
num+=5
print(num) # with Compound Assignment Operators
num*=5
print(num)

count = 1
# increment count 
count += 1
print(count)

count = 10
# decrement count 
count -= 1
print(count)

# Comparison Operators 
a = 10
b = 5
c = 3
d = 2

print(a == b)
print(a > b)
print(a < b)

# Logical Operators 
res_and = a > b and c < d # T and F -> F
print(res_and)
res_and = a > b and c > d # T and T -> T
print(res_and)

res_or = a > b or c < d # T or F -> T
print(res_or)

res_or = a > b # T
print(not res_or) # F

# Membership Operators
# string is a sequence data type
data = "python is language"
is_z_present = "z" in data
print(is_z_present)
is_p_present = "p" in data
print(is_p_present)

is_python_present = "python" in data
print(is_python_present)

# employees 
id = 105
emp_ids = [101,102,103,104,106,107,108,109,110]
is_id_present = id in emp_ids
print(is_id_present)

is_id_not_present = id not in emp_ids
print(is_id_not_present)

# Identity Operators
num1 = 10
num2 = 10
print(num1 == num2) # Comparison of values
print(num1 is num2) # Comparison of memory


a = [10,20]
b = [10,20] 

print(a == b) # Comparison of values
print(a is b) # Comparison of memory

# Bitwise Operators

num1 = 5 # 0000000000000101
num2 = 3 # 0000000000000011
         # 000000000000111 (|)
         # 0000000000000001 (&)

print(num1 & num2) 
print(num1 | num2) 