# With Encapsulation & With Setter - Getter

class Student:
    def __init__(self,name,marks):
        self.__name = name # private variable
        self.__marks = marks # private variable
    
    def display_info(self):
        print(f"{self.__name} has {self.__marks} marks")
        
    # setter 
    def set_marks(self,marks):
        if 0 <= marks <=100:
            self.__marks = marks
        else:
            print("Invalid Marks, only 0-100 allowed")
                
    # getter 
    def get_marks(self):
        return self.__marks
    
s1 = Student("ravi",95)    
# s1.display_info()

s1.set_marks(200)
print(s1.get_marks())


