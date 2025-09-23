# Dictionary 

# empty dict
empty_dict = {}
print(type(empty_dict))
print(empty_dict)

# empty dict using class
empty_dict = dict()
print(type(empty_dict))
print(empty_dict)

# store data
dict_nums = {1:10,2:20,3:30}
print(type(dict_nums))
print(dict_nums)

dict_text = {"one":"ten","two":"twenty","three":"thirty"}
print(dict_text)

mixed_data = {1:10,"two":"twenty","three":3}
print(mixed_data)

dict_nums = {1:10,2:20,3:30,2:200}
print(dict_nums)

# duplicates with keys 
dict_nums = {1:10,2:20,3:30,2:200}
print(dict_nums)

# duplicates with values 
dict_nums = {1:10,2:20,3:30,4:20}
print(dict_nums)

# keys cannot be mutable (lists are mutable)
# dict_data = {[10]:100} # TypeError: unhashable type: 'list'
dict_data = {"data":[10,20,30]}
print(dict_data)
dict_data = {(10):100}
print(dict_data)

# dictionary data
students = {
   "101": {
       "name": "Ravi",
       "email": "ravi@gmail.com",
       "course": "Python"
   },
   "102": {
       "name": "Anjali",
       "email": "anjali@gmail.com",
       "course": "Java"
   },
   "103": {
       "name": "John",
       "email": "john@yahoo.com",
       "course": "DevOps"
   }
}

print(type(students))
print(students)

# print(students[0]) # KeyError: 0

# Access data 
# print(students[101]) KeyError: 101
print(students["101"]) 
print(students["101"]["email"])

# want to perform operations
id = "101"
if students[id]["email"].endswith("@gmail.com"):
    print("Google ID - Okay")
else:
    print("Only Google ID Accepted ")
    
# loop data 
dict_nums = {1:10,2:20,3:30}
print(dict_nums)
print(dict_nums[2])

# only we get keys
for data in dict_nums:
    print(data)
    
print(dir(dict_nums))