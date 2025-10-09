# Working With CSV Files

import csv

# READING 

# Read Data Of My CSV File
with open("14_file_operations/students.csv","r") as file_data:
    csv_reader = csv.reader(file_data)
    # print(csv_reader)
    for row in csv_reader:
        print(row)

print("="*60)
    
# Assume, We have 10000 customer 
# Requirement : Fetch me customers from Hyderabad
find_by_city = "pune"
with open("14_file_operations/students.csv","r") as file_data:
    csv_reader = csv.reader(file_data)
    # Get Location/Hyderabad Customers
    for row in csv_reader:
        # List works on index basis 
        # print(row[3])
        if row[3] == find_by_city:
            print(row)

print("="*60)

# Requirement : Fetch me customers using gmail
find_by_mail = "@gmail.com"
with open("14_file_operations/students.csv","r") as file_data:
    csv_reader = csv.reader(file_data)
    # Get Location/Hyderabad Customers
    for row in csv_reader:
        # List works on index basis 
        # print(row[3])
        if row[1].endswith(find_by_mail):
            print(row)
            
print("="*60)

# Using DictReader
with open("14_file_operations/students.csv","r") as file_data:
    csv_reader = csv.DictReader(file_data)
    print(csv_reader.fieldnames)
    for row in csv_reader:
        print(row) 

print("="*60)

# Assume, We have 10000 customer 
# Requirement : Fetch me customers from Hyderabad
find_by_city = "pune"
with open("14_file_operations/students.csv","r") as file_data:
    csv_reader = csv.DictReader(file_data)
    # Get Location/Hyderabad Customers
    for row in csv_reader:
        if row["address"] == find_by_city:
            print(row)

print("="*60)
         
# Requirement : Fetch me customers using gmail
find_by_mail = "@gmail.com"
with open("14_file_operations/students.csv","r") as file_data:
    csv_reader = csv.DictReader(file_data)
    # Get gmail Customers
    for row in csv_reader:
        # List works on index basis 
        # print(row[3])
        if row["email"].endswith(find_by_mail):
            print(row)

print("="*60)
            
# WRITING 

with open("14_file_operations/employees.csv","w") as file_data:
    csv_writer = csv.writer(file_data)
    csv_writer.writerow(['name', 'email', 'mobile', 'address'])
    csv_writer.writerow(['ravi', 'ravi@gmail.com', '998998998', 'hyderabad'])
    csv_writer.writerows([['ramu', 'ramu@outlook.com', '998998998', 'bangalore'],
['suresh', 'suresh@gmail.com', '998998998', 'pune'],
['mahesh', 'mahesh@yahoo.com', '998998998', 'chennai']])
    
    
# APPENDING 

with open("14_file_operations/employees.csv","a") as file_data:
    csv_writer = csv.writer(file_data)
    csv_writer.writerow(['name', 'email', 'mobile', 'address'])
    csv_writer.writerow(['ravi', 'ravi@gmail.com', '998998998', 'hyderabad'])
    csv_writer.writerows([['ramu', 'ramu@outlook.com', '998998998', 'bangalore'],
['suresh', 'suresh@gmail.com', '998998998', 'pune'],
['mahesh', 'mahesh@yahoo.com', '998998998', 'chennai']])
    csv_writer.writerows([['ramu', 'ramu@outlook.com', '998998998', 'bangalore'],
['suresh', 'suresh@gmail.com', '998998998', 'pune'],
['mahesh', 'mahesh@yahoo.com', '998998998', 'chennai']])
    
fieldnames = ['name', 'email', 'mobile', 'address']   
with open("14_file_operations/students.csv","w") as file_data:
    csv_writer = csv.DictWriter(file_data,fieldnames=fieldnames)
    csv_writer.writeheader()
    csv_writer.writerow({ 'email': 'suresh@gmail.com', 'name': 'suresh', 'mobile': '998998998', 'address': 'pune'})