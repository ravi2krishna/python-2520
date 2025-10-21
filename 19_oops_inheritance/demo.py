# Discussing Inheritance in terms of LMS we are using 
# Student -> Watch Videos 
# VideoAdmin -> Add Videos, Watch Videos 
# SuperAdmin -> Delete Videos, Add Videos, Watch Videos 

# No Inheritance 
class Student:
    # watch videos 
    def watch_videos(self):
        print("="*50)
        print("Functionality For Watching Video")
        print("W")
        print("a")
        print("t")
        print("c")
        print("h")
        print("i") 
        print("n") 
        print("g")
        print("v") 
        print("i") 
        print("d") 
        print("e") 
        print("o")  
        print(".")  
        print(".")  
        print(".")  
        print("="*50)
        
class VideoAdmin:
    # watch videos 
    def watch_videos(self):
        print("="*50)
        print("Functionality For Watching Video")
        print("W")
        print("a")
        print("t")
        print("c")
        print("h")
        print("i") 
        print("n") 
        print("g")
        print("v") 
        print("i") 
        print("d") 
        print("e") 
        print("o")  
        print(".")  
        print(".")  
        print(".")  
        print("="*50) 
        
    # add videos 
    def add_videos(self):
        print("="*50)
        print("Functionality For Adding Video")
        print("A")
        print("d")
        print("d")
        print("i") 
        print("n") 
        print("g")
        print("v") 
        print("i") 
        print("d") 
        print("e") 
        print("o")  
        print(".")  
        print(".")  
        print(".")  
        print("="*50) 
        
class SuperAdmin:
    # watch videos 
    def watch_videos(self):
        print("="*50)
        print("Functionality For Watching Video")
        print("W")
        print("a")
        print("t")
        print("c")
        print("h")
        print("i") 
        print("n") 
        print("g")
        print("v") 
        print("i") 
        print("d") 
        print("e") 
        print("o")  
        print(".")  
        print(".")  
        print(".")  
        print("="*50) 
        
    # add videos 
    def add_videos(self):
        print("="*50)
        print("Functionality For Adding Video")
        print("A")
        print("d")
        print("d")
        print("i") 
        print("n") 
        print("g")
        print("v") 
        print("i") 
        print("d") 
        print("e") 
        print("o")  
        print(".")  
        print(".")  
        print(".")  
        print("="*50) 
        
    # delete videos 
    def delete_videos(self):
        print("="*50)
        print("Functionality For Deleting Video")
        print("D")
        print("e")
        print("l")
        print("e") 
        print("t") 
        print("i") 
        print("n") 
        print("g")
        print("v") 
        print("i") 
        print("d") 
        print("e") 
        print("o")  
        print(".")  
        print(".")  
        print(".")  
        print("="*50) 
        
# Test Features 
print("Student User")
student_user = Student()
student_user.watch_videos()

print("Video Admin User")
video_admin_user = VideoAdmin()
video_admin_user.watch_videos()
video_admin_user.add_videos()

print("Super Admin User")
super_admin_user = SuperAdmin()
super_admin_user.watch_videos()
super_admin_user.add_videos()
super_admin_user.delete_videos()