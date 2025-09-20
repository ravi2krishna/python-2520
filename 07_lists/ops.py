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