# Exception Handling 

# When there are no errors -> NOTHING TO HANDLE 
print("Program Execution Started")

num1 = 10
num2 = 5

print(num1/num2)

print("Program Execution Completed")

print("=" * 50)

# When there are errors -> 
print("Program Execution Started")

num1 = 10
num2 = 0

# print(num1/num2) # ZeroDivisionError: division by zero

print("Program Execution Completed")

print("=" * 50)

# When there are errors -> how to handle by yourself
print("Program Execution Started")

num1 = 10
num2 = 0

try:
    print(num1/num2) # ZeroDivisionError: division by zero
except:
    print("OOPS! You cannot divide number by zero - it's a MATH rule")
    print("Check More Info - https://en.wikipedia.org/wiki/Division_by_zero")

print("Program Execution Completed")

print("=" * 50)

# When there are multiple errors 
print("Program Execution Started")
data = [1,2,'python',0,5]
data = [1,2,5]

# TypeError: unsupported operand type(s) for /: 'int' and 'str'
# ZeroDivisionError: division by zero
# in future one more issue

for num in data:
    print(1/num)

print("Program Execution Completed")

print("=" * 50)

# When there are multiple errors -> More of generic errors 
print("Program Execution Started")
data = [1,2,'python',0,5]

# TypeError: unsupported operand type(s) for /: 'int' and 'str'
# ZeroDivisionError: division by zero
# in future one more issue

for num in data:
    try:
        print(1/num)
    except:
        print("OOPS! Some Problem Occurred")
        
print("Program Execution Completed")

print("=" * 50)

# When there are multiple errors -> Need To Present Specific Error
print("Program Execution Started")
data = [1,2,'python',0,5]

# TypeError: unsupported operand type(s) for /: 'int' and 'str'
# ZeroDivisionError: division by zero
# in future one more issue

for num in data:
    try:
        print(1/num)
    except:
        print("OOPS! Some Problem Occurred")
    # except: # this is not correct way
    #     print("OOPS! Some Problem Occurred")
        
print("Program Execution Completed")

print("=" * 50)

# When there are multiple errors -> Need To Present Specific Error
print("Program Execution Started")
data = [1,2,'python',0,5]

# TypeError: unsupported operand type(s) for /: 'int' and 'str'
# ZeroDivisionError: division by zero
# in future one more issue

for num in data:
    try:
        print(1/num)
    except TypeError:
        print("OOPS! Don't pass string, we cannot divide a string with number")
    except ZeroDivisionError: # this is not correct way
        print("OOPS! You cannot divide number by zero - it's a MATH rule")
        print("Check More Info - https://en.wikipedia.org/wiki/Division_by_zero")
        
print("Program Execution Completed")

print("=" * 50)

# When there are errors -> without else
print("Program Execution Started")

num1 = 10
num2 = 0

try:
    print(num1/num2) # ZeroDivisionError: division by zero
except:
    print("OOPS! You cannot divide number by zero - it's a MATH rule")
    print("Check More Info - https://en.wikipedia.org/wiki/Division_by_zero")

print("Calculation Successful")
print("Program Execution Completed")

print("=" * 50)

# When there are errors -> with else & finally 
print("Program Execution Started")

num1 = 10
num2 = 5

try:
    print(num1/num2) # authentication - username and password correct
except:
    print("OOPS! You cannot divide number by zero - it's a MATH rule")
    print("Check More Info - https://en.wikipedia.org/wiki/Division_by_zero")
else:
    print("Calculation Successful") # if authentication success -> proceed to prompt OTP
finally:
    print("Program Execution Completed - Closing All Connections")

print("=" * 50)

# User Defined Exception 
# InvalidAgeException
# InvalidEmailException
class InvalidScoreError(Exception):
    pass 

try:
    score = int(input("Enter Score 0-100 "))
    if score < 0 or score > 100:
        raise InvalidScoreError("Score Must be between (0-100)")
    print("Your Score Is Valid")
except InvalidScoreError as e :
    print("Error: ",e)
