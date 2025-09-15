# Indentation

# normal statements
print("Hello")
print("Morning") # IndentationError: unexpected indent

# conditional with Indentation
if 5 > 2:
    print("yes thats true") # IndentationError: expected an indented block
    print("incorrect indentation") # IndentationError: unindent does not match any outer indentation level
    
if True:
    print("this is good")
    print("this is not good")
    print("this is also good")

print("this is also good")

# Conditional Statements

# if Statements : runs block of code, if the condition is true
# if (condition):
#     statements
num = -10
if (num > 0):
    print("Number is positive")

# check if given number is in range of 10 to 20
number = 23
if ( number >= 10 and number <=20 ):
    print("Number is in range")

# check if number is positive or negative
num = 10
if (num > 0):
    print("Number is positive")
else:
    print("Number is negative")
    
# Typical Voting App
age = 20
if age >= 18:
    print("You can Vote")
else:
    print("You cannot Vote")


# conversions
data = 3.14
print(data)

int_converted_data = int(data)
print(int_converted_data)

int_converted_data_float = float(int_converted_data)
print(int_converted_data_float)

int_data = 10
int_data_to_str = str(int_data)
print(int_data_to_str)



# input() : used to take input from keyboard
name = input("Enter Your Name: ")
print("Welcome: "+name)

age = input("Enter Your Age: ")
age = int(age)
if age >= 18: # # TypeError: '>='x not supported between instances of 'str' and 'int'
    print("You can Vote")
else:
    print("You cannot Vote")

# above using ternary operator
# variable = value_if_true if condition else value_if_false
age = int(input("Enter Your Age: "))
status = "You can Vote" if age >= 18 else "You cannot Vote"
print(status)

# elif ladder 
marks = int(input("Enter Your Marks: "))
if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
elif marks >= 60:
    print("C")
elif marks >= 50:
    print("D")
elif marks >= 35:
    print("E")        
else:
    print("Failed")
    
# match case
choice = int(input("Enter Your Choice: 1 - Python, 2 - Java, 3 - C#: "))
match choice:
    case 1:
        print("Python")
    case 2:
        print("Java")
    case 3:
        print("C#")
    case _:
        print("Select Only (1-3)")