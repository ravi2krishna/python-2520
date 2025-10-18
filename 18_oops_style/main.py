# Main Logic 

from student import Student
from trainer import Trainer

def main():

    # For Hover Functionality 
    s1 = Student(101,"John")

    # For Click Functionality 
    s2 = Student(102,"Mike",20,"mike@gmail.com","990909090")

    # calling basic student info 
    s1.student_basic_info()

    # calling complete student info 
    s2.student_complete_info()

    # Calling calculation functionalities 
    s1.achievement_status()

    # Trainer Functionality 
    t1 = Trainer(101,"Ravi")

    # calling basic trainer info 
    t1.trainer_info()

    # calling payment functionality 
    t1.sessions_payment_cal(s1)

main()

