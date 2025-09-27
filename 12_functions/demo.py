# without function

a = 10
b = 5

# math operations
print(a+b)
print(a-b)
print(a*b)
print(a/b)

a = 20
b = 10

# math operations
print(a+b)
print(a-b)
print(a*b)
print(a/b)

a = 200
b = 100

# math operations
print(a+b)
print(a-b)
print(a*b)
print(a/b)

print("=========")

# with function
def maths_ops():
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)

# call function with 20 & 10
a = 20
b = 10
maths_ops()
a = 10
b = 5
maths_ops()
a = 200
b = 100
maths_ops()

print("=========")

# with function using parameters
def maths_ops(a,b):
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)
    
# maths_ops() # TypeError: maths_ops() missing 2 required positional arguments: 'a' and 'b'
maths_ops(10,5)
maths_ops(20,10)
maths_ops(200,100)

# a,b are parameters 
# 10,5 are arguments 
print("=========")

# Positional Arguments 
def login(username,password):
    if username == "ravi" and password == "1234":
        print("Login Success")
    else:
        print("Login Failed")

login("1234","ravi") # order messed up
login("ravi","1234") # order is correct
# login() # login() missing 2 required positional arguments: 'username' and 'password'
# login("ravi") # TypeError: login() missing 1 required positional argument: 'password'

# employee info function
def employee_info(emp_name,emp_email,emp_location):
    print(f"Hi {emp_name}, your email is {emp_email} and work location is {emp_location}")

employee_info("hyderabad","ravi","ravi@gmail.com")
employee_info("john","john@gmail.com","pune")
# employee_info("krishna","pune")

# Keyword Arguments
def employee_info(emp_name,emp_email,emp_location):
    print(f"Hi {emp_name}, your email is {emp_email} and work location is {emp_location}")
    
employee_info("hyderabad","ravi","ravi@gmail.com") # positional   
# passed explicitly by specifying the name
employee_info(emp_location="hyderabad",emp_name="ravi",emp_email="ravi@gmail.com") # keyword
print("=========")

# Default Arguments
def employee_info(emp_name,emp_email,emp_location,company_name="Google"):
    print(f"Hi {emp_name}, your email is {emp_email} working for {company_name} at {emp_location} location")

employee_info(emp_location="hyderabad",emp_name="ravi",emp_email="ravi@gmail.com")
employee_info(emp_location="pune",emp_name="john",emp_email="john@gmail.com")   
employee_info(emp_location="bangalore",emp_name="krishna",emp_email="krishna@gmail.com")    
employee_info(emp_location="new york",emp_name="mark",emp_email="mark@gmail.com",company_name="META")    