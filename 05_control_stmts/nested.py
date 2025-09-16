# Nested Conditionals : Conditionals inside Conditionals
age = int(input("Enter Your Age: "))
has_id = input("Do you have id (yes/no)?: ")

# print(has_id == "yes")

if age >= 18:  # break
    if has_id == "yes":
        print("You can Vote")
    else:
        print("You need an ID to Vote")
else:
    print("You are too young to Vote")
    
    
# Nested Loops : Loops inside Loops
# Math Table 
# 1 X 1 = 1
# 1 X 2 = 2
# 1 X 3 = 3
# .
# .
# 1 X 10 = 10

# 2 X 1 = 2
# 2 X 2 = 4
# 2 X 3 = 6
# .
# .
# 2 X 10 = 10

# 3 X 1 = 2
# 3 X 2 = 4

# for with nested
for row in range(1,6):
    for column in range(1,6):
        print(f"{row} X {column} = {row*column}")
    print("--------------")

# while with nested 
# while (condition):
#             statements
row = 1
while row < 6:
    column = 1
    while column < 6:
        print(f"{row} X {column} = {row*column}")
        column+=1 
    print("--------------")
    row+=1

        