# Tuples 

# empty tuple
empty_tuple = ()
print(type(empty_tuple))
print(empty_tuple)

# empty tuple using class
empty_tuple = tuple()
print(type(empty_tuple))
print(empty_tuple)

# tuple data 
num_tuple = (10,20,30,40,50) # homogenous 
print(num_tuple)

num_tuple = tuple((10,20,30,40,50))
print(num_tuple)

text_tuple = ("python","cloud","django","ai")
print(text_tuple)

mixed_tuple = (10,20,30,"python","cloud",5.5,True) # heterogenous 
print(mixed_tuple)

single_element = (10)
print(single_element)

single_element = tuple([10])
print(single_element)

# Access data 
num_tuple = (10,20,30,40,50) # homogenous 
print(num_tuple)

# access individual element use indexing 
print(num_tuple[0]) 
print(num_tuple[3]) 
print(num_tuple[-1])

# access range of elements use slicing
print(num_tuple[::])
print(num_tuple[1:3:])
print(num_tuple[0:5:2])

# list looping
num_tuple = (10,20,30,40,50) # homogenous 
print(num_tuple)
# print(dir(num_list))
for num in num_tuple:
    print(num)
print("==========")

# use operators
for num in num_tuple:
    print(num * 5)
print("==========")

# use conditionals
num_tuple = (10,20,30,43,77,40,50) # homogenous 
for num in num_tuple:
    if num % 2 == 0:
        print("even",num)

# Duplicates allowed       
num_tuple = (10,20,30,40,50,20,10) # homogenous 
print(num_tuple)
print(dir(num_tuple))

list_order_ids = [1019202,2829282,1029202,819182,9090902]
print(type(list_order_ids))
print(list_order_ids)

# unknowingly 
list_order_ids.clear()
print(list_order_ids)

list_order_ids = [1019202,2829282,1029202,819182,9090902]
read_only_order_ids = tuple(list_order_ids)
# read_only_order_ids.clear() # AttributeError: 'tuple' object has no attribute 'clear'
num_of_orders = len(read_only_order_ids)
print(num_of_orders)

list_data = list(read_only_order_ids)
print(list_data)