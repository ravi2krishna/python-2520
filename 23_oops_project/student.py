# Student Entity
from person import AbstractPerson
# inheritance 
class Student(AbstractPerson):
    
    # class variable -> class data common to all students
    institute_name = "Edify"
    
    def __init__(self, student_id=None, student_name=None, student_age=None, student_email=None, student_mobile=None):
        # super().__init__(id, name, age, email, mobile)
        AbstractPerson.__init__(self,id=student_id,name=student_name,age=student_age,email=student_email,mobile=student_mobile)
    
    # calculate sessions attended credits 
    def sessions_credits_cal(self):
        # local variables
        total_sessions_attended = 0
        attendance_credits = 0
        total_sessions_attended = int(input("Enter Total Sessions Attended: "))
        total_sessions_attended = total_sessions_attended
        
        if total_sessions_attended >= 30:
            attendance_credits = 5
        elif total_sessions_attended >= 20:
            attendance_credits += 3
        else:
            attendance_credits = 0
        return attendance_credits
    
    # calculate performance credits based o score 
    def performance_credits_cal(self, score):
        # local variable
        performance_credits = 0
        if score >= 85:
            performance_credits = 5
        elif score >= 60:
            performance_credits = 3
        else:
            performance_credits = 0
        return performance_credits
    
    # calculate achievement (based on above two calculations)
    def achievement_status(self):
        final_credits = 0
        final_credits = self.sessions_credits_cal() + self.performance_credits_cal(90)
        if final_credits >= 10:
            print("Got 🥇")
        elif final_credits >= 8:
            print("Got 🥈")
        else:
            print("Got 🥉")
            
    # give trainer rating 
    def trainer_rating_cal(self):
        trainer_rating = 0
        trainer_rating = int(input("Enter Trainer Rating (1-5): "))
        if trainer_rating >=5 :
            return 5000
        else:
            return 0