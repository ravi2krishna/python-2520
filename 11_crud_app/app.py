# Student Management System (Student/Product/Employee etc)

# Simulate a menu based application 

# System Info On Start up

SYSTEM_INFO = ("Edify Technologies", "Student Management System","v1")
ADMIN_INFO = ("9090880","admin@edify.com")

# set student details in below dict
students = {}

# Build Menu System 
while True:
    print("Choose an option: ")
    print("1 - Add Student")
    print("2 - Update Student")
    print("3 - Delete Student")
    print("4 - List Student")
    print("5 - Exit System")
    
    choice = input("Enter Choice (1-5): ")
    
    # student add 
    if choice == "1":
        print("Adding Student Logic")
        student_id = input("Enter ID: ")
        if student_id in students:
            print("ID Already Exist, Try with different ID")
        else:
            name = input("Enter Name: ").title()
            
            # list for scores
            scores = []
            while True:
                score_input = input("Enter Score or type done: ")
                if score_input == "done":
                    break
                if score_input.isdigit():
                    score = int(score_input)
                    if 0 <= score <=100:
                        scores.append(score)
                    else:
                        print("Score Should be 0-100 ")
                else:
                    print("Score Should Numbers Only")
            
        
        
    elif choice == "2":
        print("Updating Student Logic")
    elif choice == "3":
        print("Deleting Student Logic")
    elif choice == "4":
        print("Listing Students Logic")
    elif choice == "5":
        print("Exit System")
        break
    else:
        print("Invalid Option, Only Select (1-5)")    
    
        
    
    