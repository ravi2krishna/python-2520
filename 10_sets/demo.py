# Sets 

empty_set = {}
print(type(empty_set))

empty_set = set()
print(type(empty_set))

# nums set 
num_set = {10,20,30,40,50}
print(type(num_set))

print(num_set) # no insertion order 

# print(num_set[2]) # TypeError: 'set' object is not subscriptable

num_set = {10,20,30,20,40,10,50}
print(type(num_set))
print(num_set)

text_set = {"one","two","three"}
print(text_set)

mixed_set = {10,20,30,"one","two","three"}
print(mixed_set)

num_set = {10,20,30,40,50}
print(num_set)

# loop 
for num in num_set:
    print(num)
    
print(dir(num_set)) # sets are mutable 

num_set = {10,20,30,40,50}
list_nums = list(num_set)
print([list_nums[0]])

# frozenset -> immutable version of set 
fs = frozenset({10,20,30,40,50})
print(type(fs))
print(fs)

print(dir(fs))


# new_set = {list(num_set),num_set}
# print(new_set)