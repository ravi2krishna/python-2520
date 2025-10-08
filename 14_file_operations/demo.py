# Working With Files & Directories 

# Syntax - 1
file = open("file.txt","r") # # FileNotFoundError: [Errno 2] No such file or directory: 'file_new.txt'
print(file)
print(file.closed) 
file.close()
print(file.closed) 

# Syntax - 2
with open("file.txt","r") as file_data:
    print(file_data)
print(file_data.closed) 

# Reading Data -> reading whole file content
with open("file.txt","r") as file_data:
    print(file_data.read())
    
# Reading Data -> reading character wise 
with open("file.txt","r") as file_data:
    for char in file_data.read():
        print(char)

# Reading Data -> reading word wise 
with open("file.txt","r") as file_data:
    for word in file_data.read().split():
        print(word)
        
# Reading Data -> reading line wise 
with open("file.txt","r") as file_data:
    print(file_data.readline())
    print(file_data.readline().strip())

# Reading Data -> reading all lines
with open("file.txt","r") as file_data:
    print(file_data.readlines())
    
with open("file.txt","r") as file_data:
    list_data = file_data.readlines()
    for line in list_data:
        print(line.strip())
        
# Write Mode -> Create File 
with open("write.txt","w") as file_data:
    print(file_data)
    
# Write Mode -> Update
with open("write.txt","w") as file_data:
    file_data.write("hello")
    
# Write Mode -> Update Multiple Lines
with open("write.txt","w") as file_data:
    file_data.writelines(["this is line one \n","this is line two"])

# Write Mode -> Update Multiple Lines
with open("write.txt","w") as file_data:
    file_data.writelines(["this is line three \n","this is line four"])
    
# Write Mode -> Update Multiple Lines Overwrites
with open("write.txt","w") as file_data:
    file_data.writelines(["this is line one \n","this is line two \n"])

# Append Mode -> Update Multiple Lines Appends
with open("write.txt","a") as file_data:
    file_data.writelines(["this is line three \n","this is line four\n"])
    
# Append Mode -> Update Multiple Lines Appends
with open("new.txt","a") as file_data:
    file_data.writelines(["this is line three \n","this is line four\n"])