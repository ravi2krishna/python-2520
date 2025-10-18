# Trainer Class 

from student import Student

class Trainer:
    
    # instance data specific to each trainer 
    def __init__(self,trainer_id,trainer_name):
        # identity info
        self.trainer_id = trainer_id
        self.trainer_name = trainer_name
        
        # calculations info
        self.total_sessions_taken = 0
        self.payment_for_sessions = 0
        self.training_bonus = 0
        self.total_payment = 0
        
    # trainer info
    def trainer_info(self):
        print("========== Trainer Info ==========")
        print(f"Trainer ID : {self.trainer_id}")
        print(f"Trainer Name : {self.trainer_name}")
        
    # trainer payment calculation
    def sessions_payment_cal(self,s1):
        self.total_sessions_taken = int(input("Enter Total Sessions Taken: "))
        base_pay_per_session = 2000
        self.payment_for_sessions = self.total_sessions_taken * base_pay_per_session
        
        # get student rating here 
        # s1 = Student()
        print("========= Student Rating Given =========")
        self.training_bonus = s1.trainer_rating_cal()
        self.total_payment = self.payment_for_sessions + self.training_bonus
        print("========= Trainer Payment =========")
        print(f"Total Trainer Payment: {self.total_payment}")
        