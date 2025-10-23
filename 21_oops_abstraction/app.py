# With Abstraction

from abc import ABC, abstractmethod

# abstract class 
class Laptop(ABC):
    
    # abstract methods
    @abstractmethod
    def processor(self):
        pass
    
    @abstractmethod
    def ram_hdd(self):
        pass 
    
    # concrete
    def screen_saver(self):
        print("Screen Saver") 

# laptop = Laptop() # TypeError: Can't instantiate abstract class
# laptop.processor() 

# Implementation 
class Lenovo(Laptop):
    def processor(self):
        print("Lenovo Laptop Processor ") 
        
    def ram_hdd(self):
        print("Lenovo Laptop RAM & HDD ")  
        
# End user 
print("Buying Lenovo Laptop")    
lenovo = Lenovo() # TypeError: Can't instantiate abstract class Lenovo 
                # without an implementation for abstract method 'ram_hdd'
lenovo.processor()
lenovo.ram_hdd()
lenovo.screen_saver()