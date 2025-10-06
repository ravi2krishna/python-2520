# Student Management System (Student/Product/Employee etc)

# Simulate a menu based application 

# System Info On Start up

SYSTEM_INFO = ("Edify Technologies", "Student Management System","v1")
ADMIN_INFO = ("9090880","admin@edify.com")

# set student details in below dict
students = {}

# adding student via function 
def add_student():
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

# updating student via function 
def update_student():
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

# deleting student via function
def delete_student():
        print("Deleting Student Logic")
        student_id = input("Enter ID To Delete: ")
        if student_id in students:
            remove = students.pop(student_id)
            print(remove)
        else:
            print("ID Doesn't Exist to Delete")
        
        # for our confirmation
        print(students)
        
# read students data via function
def read_students():
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

# search by skill ==> loop & condition  (filter)
def search_students():
    skill_to_search = input("Enter Skill To Search: ")
    filtered_students = list(filter(lambda s: skill_to_search in students[s]['skills'], students))
    print(filtered_students)
    
    if filtered_students:
        print(f"Students With Skills {skill_to_search}: ")
        for sid in filtered_students:
            print(f"ID: {sid}   |   Name: {students[sid]['name']}")
    else:
        print(f"No students found with skill {skill_to_search}")

# exit system via function
def exit_system():
        print("Exit System")
        print("="*50)
        print("CONTACT ADMIN FOR MORE INFORMATION")
        print(f"ADMIN CONTACT NO: {ADMIN_INFO[0]}")
        print(f"ADMIN EMAIL ID: {ADMIN_INFO[1]}")
        print("="*50)

# Build Menu System 
while True:
    print("Choose an option: ")
    print("1 - Add Student")
    print("2 - Update Student")
    print("3 - Delete Student")
    print("4 - List Student")
    print("5 - Search Student By Skill")
    print("6 - Exit System")
    
    choice = input("Enter Choice (1-6): ")
    
    # student add 
    if choice == "1":
        add_student()       
    elif choice == "2":
        update_student()  
    elif choice == "3":
        delete_student()
    elif choice == "4":
        read_students()
    elif choice == "5":
        search_students()
    elif choice == "6":
        exit_system()
        break
    else:
        print("Invalid Option, Only Select (1-6)")    
    
        
    
    