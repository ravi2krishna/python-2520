from student import Student
from trainer import Trainer
# from admin import Admin 

def main():
    
    # create a student
    s = Student(101,"John",20,"john@gmail.com",909090)
    
    # display student 
    s.person_complete_info()
    
    # Calling calculation functionalities 
    s.achievement_status()
    
    # create a Trainer Functionality 
    t = Trainer(900,"Ravi",30,"ravi@gmail.com",88888)
    
    # display trainer 
    t.person_complete_info()
    
    t.sessions_payment_cal(s)
    
    # display admin 
    # a.person_complete_info()
    
    # a.add_video()
    
main()