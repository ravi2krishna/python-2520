# Trainer Entity
from person import AbstractPerson
# inheritance 
class Trainer(AbstractPerson):
    
    def __init__(self, trainer_id=None, trainer_name=None, trainer_age=None, trainer_email=None, trainer_mobile=None):
        # super().__init__(id, name, age, email, mobile)
        AbstractPerson.__init__(self,id=trainer_id,name=trainer_name,age=trainer_age,email=trainer_email,mobile=trainer_mobile)
    
    # trainer payment calculation
    def sessions_payment_cal(self,s1):
        total_sessions_taken = 0
        total_sessions_taken = int(input("Enter Total Sessions Taken: "))
        base_pay_per_session = 2000
        payment_for_sessions = total_sessions_taken * base_pay_per_session
        
        # get student rating here 
        # s1 = Student()
        print("========= Student Rating Given =========")
        training_bonus = s1.trainer_rating_cal()
        total_payment = payment_for_sessions + training_bonus
        print("========= Trainer Payment =========")
        print(f"Total Trainer Payment: {total_payment}")