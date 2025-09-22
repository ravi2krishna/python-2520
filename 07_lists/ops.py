# List Related Operations

# append() : adds an element to the end of the list 
num_list = [10,20,30,40,50] 
print(num_list)

# num_list.append() # TypeError: list.append() takes exactly one argument (0 given)
num_list.append(60)
print(num_list)

# num_list.append(70,80,90) # TypeError: list.append() takes exactly one argument (3 given)
print(num_list)

# extend() : adds an iterable to the end of the list 
num_list = [10,20,30,40,50] 
print(num_list)
# num_list.extend(60) # TypeError: 'int' object is not iterable
num_list.extend([60,70,80])
print(num_list)

num_list.extend(["employee","hy"])
print(num_list)

num_list.append(["employee","hy"])
print(num_list)

print(num_list[10])
print(num_list[10][1])

# insert() : insert at specific position (index)
num_list = [10,20,40,50] 
print(num_list)
# num_list.insert(30) # TypeError: insert expected 2 arguments, got 1
num_list.insert(2,30)
print(num_list)

num_list.insert(10,30) # adding at end, if out of range index is given
print(num_list)

num_list.insert(0,5) # insert moves the positions
print(num_list)

# use assignment operator 
num_list = [10,20,30,40,50] 
print(num_list)
num_list[0] = 5 # Lists are mutable
print(num_list)

# pop() : remove last element 
num_list = [10,20,30,40,50] 
print(num_list)
num_list.pop()
print(num_list)

num_list = [10,20,30,40,50] 
print(num_list)
num_list.pop(3)
print(num_list)

num_list = [10,20,30,40,50] 
print(num_list)
# num_list.pop(10) # IndexError: pop index out of range
print(num_list)

# remove() : remove element based on value, not index
num_list = [10,20,30,40,50] 
print(num_list)
# num_list.remove() # TypeError: list.remove() takes exactly one argument (0 given)
# num_list.remove(0) # ValueError: list.remove(x): x not in list
num_list.remove(20)
print(num_list)

num_list = [10,20,30,40,50,10,70,10] 
print(num_list)
num_list.remove(10) # only first occurrence 
print(num_list)

# remove all occurrences
num_list = [10,20,30,40,50,10,70,10] 
print(num_list)

# logic to remove all 
while 10 in num_list:
    num_list.remove(10)
print(num_list)

# clear() : removes all elements, empties list 
num_list = [10,20,30,40,50,10,70,10] 
print(num_list)
num_list.clear()
print(num_list)

# NOTE : Lists can be modified (Mutable Objects)

# index(): used to get index position of specified value 
num_list = [10,20,30,40,50] 
print(num_list)

# num_list.index() # TypeError: index expected at least 1 argument, got 0
# num_list.index(100) # ValueError: 100 is not in list
print(num_list.index(40))

list_nums = [10, 20, 30, 20, 40, 20, 10, 20, 10, 20, 10]
print(num_list.index(20))

print(list_nums.index(20,4,8)) # 5 stop at 8

print(list_nums.index(20,5)) # stop at end 

# count() : count the occurrences 
list_nums = [10, 20, 30, 20, 40, 20, 10, 20, 10, 20, 10]
# count_10 = list_nums.count() # TypeError: list.count() takes exactly one argument (0 given)
count_10 = list_nums.count(10)
print(count_10)

print(list_nums.count(40))
print(list_nums.count(80))

# reverse() : reverses the list, performs inplace operation
num_list = [10,20,30,40,50] 
print(num_list)
value = num_list.reverse()
print(value)
print(num_list)

num_list = [10,20,30,40,50]  
print(num_list)
# [50, 40, 30, 20, 10]
print(num_list[::-1])
print(num_list)

# sort() : sorts the list, inplace operation, default is ascending order  
num_list = [10,50,40,20,30]  
print(num_list)
print(num_list.sort())
print(num_list)

print(num_list.sort(reverse=True))
print(num_list)

text_list = ["c","python","java"]
text_list.sort()
print(text_list)

mixed_list = [10,20,"c","python",50]
# mixed_list.sort() # TypeError: '<' not supported between instances of 'str' and 'int'
print(mixed_list)

# copy() : creates a backup copy (shallow copy), when we modify backup, original is not affected
num_list = [10,50,40,20,30]  
print(num_list)
backup = num_list.copy()
print(backup)

num_list.append(60)
print("original ",num_list)
print("backup ",backup)

# soft copy : when we modify backup, original is affected (use = operator)
num_list = [10,50,40,20,30]  
print(num_list)
backup = num_list
print(backup)

num_list.append(60)
print("original ",num_list)
print("backup ",backup)