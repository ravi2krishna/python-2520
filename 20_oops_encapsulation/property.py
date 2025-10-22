# Using @property
# With Encapsulation & With Setter - Getter

class Student:
    def __init__(self,name,marks):
        self.__name = name # private variable
        self.__marks = marks # private variable
        
    # @property -> which is like getter
    @property
    def marks(self):
        return self.__marks
    
    # @value.setter -> which is like setter 
    @marks.setter 
    def marks(self,marks):
        if 0 <= marks <=100:
            self.__marks = marks
        else:
            print("Invalid Marks, only 0-100 allowed")    
    
s1 = Student("ravi",95)    
# s1.display_info()

print(s1.marks)

s1.marks = 200
print(s1.marks)

