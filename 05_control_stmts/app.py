# Student Grade Tracker Solution
# Variables - Operators - Control Statements

# -> Student ID -> Student Name  -> Attendance 
student_id = input("Enter your ID: ")
student_name = input("Enter your Name: ")
student_attendance = int(input("Enter your Attendance: "))

total_score = 0
number_of_scores = 0

continue_input = "yes"

while continue_input == "yes":
    current_score = int(input(f"Enter Score {number_of_scores+1}: "))
    continue_input = input("Do you want to continue (yes/no)? ")
    # increment score count 
    number_of_scores+=1
    # update the total score by adding current given score 
    total_score = total_score + current_score
    
# Average score 
average_score = total_score / number_of_scores

# Grade the Student
if average_score >= 85:
    print("A")
elif average_score >= 70:
    print("B")
elif average_score >= 50:
    print("C")
else:
   print("FAIL")

# Attendance Criteria 
attendance_status = "WARNING LOW ATTENDANCE" if student_attendance < 75 else "OK GOOD ATTENDANCE"

print("Student Name: "+student_name)
print(f"Student Total Score: {total_score}")
# print("Student Total Score: " +total_score) 
print(f"Student Number Of Scores: {number_of_scores}")
print(f"Student Average Score: {average_score}")
print("Student Attendance Status: "+attendance_status)

# Award Eligibility
if average_score >= 85 and student_attendance > 75:
    print("Got Awarded")