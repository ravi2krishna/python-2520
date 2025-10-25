# Contracts for entities like Student, Trainer, Admin etc 

from abc import ABC, abstractmethod

class Personable(ABC):
    # set person details like Student, Trainer, Admin etc 
    @abstractmethod
    def set_personal_details(self,id,name,age,email,mobile):
        pass 
    
    # display person details like Student, Trainer, Admin etc 
    @abstractmethod
    def person_complete_info(self):
        pass 
    
# in future make payments as mandatory for every entity
class Payables(ABC):    
    @abstractmethod
    def person_payment_info(self):
        pass