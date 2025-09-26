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
            
            # set for skills
            skills = set()
            while True:
                skill_input = input("Enter Skill or type done: ")
                if skill_input == "done":
                    break
                skills.add(skill_input.title())
            
            # save the student details
            students[student_id] = {
                "name": name,
                "scores": scores,
                "skills": skills
            }
            print("Student Saved")
            
            # for our confirmation
            print(students)
                    
    elif choice == "2":
        print("Updating Student Logic")
        student_id = input("Enter ID To Update: ")
        if student_id in students:
            new_name = input("Enter New Name: ").title()
            students[student_id]["name"] = new_name
            print("Student Name Updated")
        else:
            print("ID Doesn't Exist to Update")
        
        # for our confirmation
        print(students)
        
        
    elif choice == "3":
        print("Deleting Student Logic")
        student_id = input("Enter ID To Delete: ")
        if student_id in students:
            remove = students.pop(student_id)
            print(remove)
        else:
            print("ID Doesn't Exist to Delete")
        
        # for our confirmation
        print(students)
        
    elif choice == "4":
        print("Listing Students Logic")
        for sid, data in students.items():
            name = data["name"]
            scores = data["scores"]
            
            avg = sum(scores)/len(scores)
            high_score = max(scores)
            low_score = min(scores)
            
            skills = data["skills"]
            skills_count = len(skills)
            
            print("="*50)
            print("STUDENT DETAILS")
            print("="*50)
            
            print(f"ID: {sid}")
            print(f"NAME: {name}")
            print(f"ALL SCORES: {scores}")
            print(f"AVG SCORE: {avg}")
            print(f"HIGH SCORE: {high_score}")
            print(f"LOWEST SCORE: {low_score}")
            print(f"ALL SKILLS: {skills}")
            print(f"NO OF SKILLS: {skills_count}")
            
        
    elif choice == "5":
        print("Exit System")
        print("="*50)
        print("CONTACT ADMIN FOR MORE INFORMATION")
        print(f"ADMIN CONTACT NO: {ADMIN_INFO[0]}")
        print(f"ADMIN EMAIL ID: {ADMIN_INFO[1]}")
        print("="*50)
        break
    else:
        print("Invalid Option, Only Select (1-5)")    
    
        
    
    