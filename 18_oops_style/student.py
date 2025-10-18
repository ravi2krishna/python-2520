# Student Class 

class Student:
    
    # class variable -> class data common to all students
    institute_name = "Edify"
    
    # one more constructor for basic info -> below approach is overloading not allowed in python
    # def __init__(self,student_id,student_name):
    #     # identity info
    #     self.student_id = student_id
    #     self.student_name = student_name
    
    # instance data specific to each student 
    def __init__(self,student_id,student_name,student_age=None,student_email=None,student_mobile_number=None):
        # identity info
        self.student_id = student_id
        self.student_name = student_name
        self.student_age = student_age
        self.student_email = student_email
        self.student_mobile_number = student_mobile_number
        
        # calculations info
        self.total_sessions_attended = 0
        self.attendance_credits = 0
        self.performance_credits = 0
        self.final_credits = 0
        self.trainer_rating = 0

    # hover like functionality -> display basic info 
    def student_basic_info(self):
        print("========== Basic Student Info ==========")
        print(f"Student ID : {self.student_id}")
        print(f"Student Name : {self.student_name}")
    
    # click like functionality -> display complete info 
    def student_complete_info(self):
        print("========== Basic Complete Info ==========")
        print(f"Student ID : {self.student_id}")
        print(f"Student Name : {self.student_name}")
        print(f"Student Age : {self.student_age}")
        print(f"Student Email : {self.student_email}")
        print(f"Student Mobile No : {self.student_mobile_number}")
        
    # calculate sessions attended credits 
    def sessions_credits_cal(self):
        total_sessions_attended = int(input("Enter Total Sessions Attended: "))
        self.total_sessions_attended = total_sessions_attended
        
        if total_sessions_attended >= 30:
            self.attendance_credits += 5
        elif total_sessions_attended >= 20:
            self.attendance_credits += 3
        else:
            self.attendance_credits = 0
        return self.attendance_credits
    

    # calculate performance credits based o score 
    def performance_credits_cal(self, score):
        if score >= 85:
            self.performance_credits += 5
        elif score >= 60:
            self.performance_credits += 3
        else:
            self.performance_credits = 0
        return self.performance_credits
    
    # calculate achievement (based on above two calculations)
    def achievement_status(self):
        self.final_credits = self.sessions_credits_cal() + self.performance_credits_cal(90)
        if self.final_credits >= 10:
            print("Got 🥇")
        elif self.final_credits >= 8:
            print("Got 🥈")
        else:
            print("Got 🥉")
            
    # give trainer rating 
    def trainer_rating_cal(self):
        self.trainer_rating = int(input("Enter Trainer Rating (1-5): "))
        if self.trainer_rating >=5 :
            return 5000
        else:
            return 0