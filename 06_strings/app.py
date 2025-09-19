# Enhanced Student Grade Tracker Solution

print("="*50)
print("         Enhanced Student Grade Tracker")
print("="*50)

# Student ID 
student_id_valid = False

while not student_id_valid:
    student_id = input("Enter ID: ")
    
    # check for positive number & non-alphabet (-101)
    if student_id.startswith("-") and student_id[1:].isdigit():
        print("Please Enter Positive Numbers Only")
    elif student_id.isdigit():
        student_id = int(student_id)
        if student_id > 0:
            student_id_valid = True
        else:
            print("Zero Not Allowed")
    else:
        print("Enter Numbers Only")
    
print(student_id)
        
        
        
    
