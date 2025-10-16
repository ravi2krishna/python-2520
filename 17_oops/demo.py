# OOPS Basics 

data = 10
# print(type(data))

# class
class Employee:
    pass

# object 
emp_obj = Employee()
# print(type(emp_obj))

# Student -> Real World Entity
class Student:
    # attributes / variables 
    student_name = "Ravi"
    student_email = "ravi@gmail.com"
    
    # statements 
    print("Student Name: ",student_name)
    print("Student Email: ",student_email)
    
# function (outside the class)
def student_fun():
    #  variables 
    student_name = "John"
    student_email = "john@gmail.com"
    # statements 
    print("Student Name: ",student_name)
    print("Student Email: ",student_email)
    
# for functions call is must    
student_fun()

# Student -> Real World Entity
class Student:
    # attributes / variables 
    student_name = "mike"
    student_email = "mike@gmail.com"
    
    # method
    def info(self):
        # student_email = "john@gmail.com"
        print("Student Name: ",self.student_name)
        print("Student Email: ",self.student_email) 

student_one_obj = Student()
student_two_obj = Student()
student_three_obj = Student()
# method call is required 
student_one_obj.info() # TypeError: Student.info() takes 0 positional arguments but 1 was given
student_two_obj.info()
student_three_obj.info()

# __init__() -> Constructor
class Student:
    
    # class variable is shared across all objects 
    institute_name = "Edify"
    
    # Constructor
    def __init__(self,student_name,student_email):
        if not Student.validate_email(student_email):
            raise ValueError("Invalid Email Address")
        # instance variables
        self.student_name = student_name 
        self.student_email = student_email    
        
    # instance method
    def info(self):
        # student_email = "john@gmail.com"
        # Accessing instance variables 
        print("Student Name: ",self.student_name)
        print("Student Email: ",self.student_email) 
        
        # Accessing class variables 
        print("Student Institute: ",Student.institute_name) # recommended 
        # print("Student Institute Via Object: ",self.institute_name) # not recommended 
    
    # class method    
    @classmethod
    def change_institute(cls,new_name):
        cls.institute_name = new_name # recommended
        # Student.institute_name = new_name 
        # Accessing instance data inside a class method is not possible
        # print("Accessing Instance Data: ",self.student_name)
        
    
    # static method -> utility 
    @staticmethod
    def validate_email(email):
        return "@" in email and "." in email
            
ravi_obj = Student("ravi","ravi@gmail.com")
john_obj = Student("john","john@gmail.com")
mike_obj = Student("mike","mike@gmail.com")
print("="*50)
ravi_obj.info()
john_obj.info()
mike_obj.info()

# change the institute 
Student.change_institute("Digital Edify")
print("="*50)
ravi_obj.info()
john_obj.info()
mike_obj.info()

# calling static method 
print(Student.validate_email("test@gmail.com"))
print(Student.validate_email("test"))

