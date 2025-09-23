# Dictionary Methods / Operations

dict_data = {"a":"Apple", "b":"banana"}
print(dict_data)

# update() : adds / updates items in dict 
# dict_data.update() 
# ney key -> add
dict_data.update({"c":"cherry"})
print(dict_data)

# existing key -> update 
dict_data.update({"a":"avocado"})
print(dict_data)

# pop() : removes the item with key 
dict_data = {"a":"Apple", "b":"banana"}
print(dict_data)
# dict_data.pop() # TypeError: pop expected at least 1 argument, got 0
dict_data.pop("a")
# dict_data.pop("c") # KeyError: 'c'
print(dict_data)

# popitem() : removes the last item 
dict_data = {"a":"Apple", "b":"banana"}
print(dict_data)
# dict_data.popitem("a") # TypeError: dict.popitem() takes no arguments (1 given)
dict_data.popitem()
print(dict_data)

# clear() : empties the dictionary
dict_data = {"a":"Apple", "b":"banana"}
print(dict_data)
dict_data.clear()
print(dict_data)

# get() : used to get the value for key 
dict_data = {"a":"Apple", "b":"banana"}
print(dict_data)
# dict_data.get() # TypeError: get expected at least 1 argument, got 0
print(dict_data.get("a"))
print(dict_data.get("c"))

# keys() : used to get keys 
dict_data = {"a":"Apple", "b":"banana"}
print(dict_data)
print(dict_data.keys())
only_key = dict_data.keys()
for key in only_key:
    print(key)
    
# values() : used to get values 
dict_data = {"a":"Apple", "b":"banana"}
print(dict_data)
only_values = dict_data.values()
print(only_values)
for value in only_values:
    print(value)
    
# items() : gets both keys and values
dict_data = {"a":"Apple", "b":"banana"}
print(dict_data)
print(dict_data.items())
data = dict_data.items()
for item in data:
    print(item)
    print(item[0])
    
# copy() : make a shallow copy 
dict_data = {"a":"Apple", "b":"banana"}
print(dict_data)
backup = dict_data.copy()
print(backup)

backup.update({"c":"cherry"})
print(dict_data)
print(backup)

# soft copy
dict_data = {"a":"Apple", "b":"banana"}
print(dict_data)
backup = dict_data
print(backup)

backup.update({"c":"cherry"})
print(dict_data)
print(backup)

# setdefault() : returns value of a key, 
# if not present it sets 
# if key present, will not update 
print("========")
dict_data = {"a":"Apple", "b":"banana"}
print(dict_data)
# dict_data.setdefault() # TypeError: setdefault expected at least 1 argument, got 0
data = dict_data.setdefault("b","blueberry")
print(data)

dict_data = {"a":"Apple", "b":"banana"}
print(dict_data)
print(dict_data.setdefault("c","cherry"))
print(dict_data)