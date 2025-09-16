# Branching Statements (Jump Statements) 

# break : exit/break loop
for num in range(1,11):
    print(num)
print("----------")    
for num in range(1,11):
    if num == 5:
        break # stop from 5
    print(num)
print("----------")     
# continue : skip the current Iteration in loop 
for num in range(1,11):
    if num == 5:
        continue # skip 5 
    print(num)
    
# pass : acts as a Placeholder, for doing nothing 
emp_salary = 10001
if emp_salary > 10000:
    # statements : i don't know 
    # pass # in future i will come back to this 
    # after a week
    print("High Salary")

for i in range(5):
    if i == 3:
        pass # do something in future 
    print(i)