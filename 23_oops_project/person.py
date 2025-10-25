# Common Person Class of abstract 

from contracts import Personable

class AbstractPerson(Personable):
    
    def __init__(self,id=None,name=None,age=None,email=None,mobile=None):
        # Private Attributes -> Encapsulation
        self.__id = id
        self.__name = name
        self.__age = age
        self.__email = email
        self.__mobile = mobile
    
    # using property in pythonic way for getters & setters 
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self,value):
        self.__id = value
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,value):
        self.__name = value
    
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self,value):
        self.__age = value
    
    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self,value):
        self.__email = value
        
    @property
    def mobile(self):
        return self.__mobile
    
    @mobile.setter
    def mobile(self,value):
        self.__mobile = value
        
    # Implementation of personable -> override (polymorphism)
    def set_personal_details(self,id,name,age,email,mobile):
        # set set person details
        self.id = id
        self.name = name 
        self.age = age
        self.email = email
        self.mobile = mobile
        
    # Implementation of personable -> override (polymorphism)
    def person_complete_info(self):
        # display person details 
        print("============= Complete Information =============") 
        print(f"ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")
        print(f"Mobile: {self.mobile}")
        
        
    