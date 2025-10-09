# Working with File & Directory Operations 

import os 
import shutil

# Create Directory / Folder 
folder_name = "students_data"

if not os.path.exists(folder_name):
    os.makedirs(folder_name)
    print(f"{folder_name} created")
    
# Create File Inside students_data
with open(f"{folder_name}/info.txt","w") as file:
    file.write("Student Ravi")
    
# Delete File 
os.remove(f"{folder_name}/info.txt")
print("File Deleted")

# Delete Empty Folders  
if not os.path.exists("test"):
    os.makedirs("test")
os.rmdir("test")  
print("Folder Deleted") # Directory not empty: 'students_data'

# Delete Non Empty Folders
# os.rmdir(folder_name)  
shutil.rmtree(folder_name)
print("Folder Deleted") # Directory not empty: 'students_data'

