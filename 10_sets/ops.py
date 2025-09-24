# Set Operations / Methods

# add() : add element to set 
s1 = {10,20,30,40,50}
# s1.add() # TypeError: set.add() takes exactly one argument (0 given)
s1.add(60)
print(s1)

# update() : add multiple elements(iterables) to set 
s1 = {10,20,30,40,50}
s1.update([60,70,80])
print(s1)

# remove() : remove elements 
s1 = {10,20,30,40,50}
# s1.remove() # TypeError: set.remove() takes exactly one argument (0 given)
s1.remove(30)
# s1.remove(70) # KeyError: 70
print(s1)

# discard() : remove element if found, no error if not found
s1 = {10,20,30,40,50}
s1.discard(30)
print(s1)
s1.discard(70) 
print(s1)

# pop() : removes random element 
s1 = {10,20,30,40,50}
# s1.pop(10) # TypeError: set.pop() takes no arguments (1 given)
s1.pop()
print(s1)
s1.pop()
print(s1)

# clear() : removes and empties 
s1 = {10,20,30,40,50}
s1.clear()
print(s1)

s1 = {10,20,30,40,50}
l1 = list(s1)
l1.sort()
print(l1[0])

# Sets are Mutable above methods confirm that 
print("copy")
# copy() : makes a copy
s1 = {10,20,30,40,50}
backup = s1.copy()
print(s1)
print(backup)
backup.pop()
print(backup)
print(s1)

# soft copy
s1 = {10,20,30,40,50}
backup = s1
print(backup is s1)
print(s1)
print(backup)
backup.pop()
print(backup)
print(s1) # object is same for both 

# special functions from set 

s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}

# union() : combine both the sets 
print(s1.union(s2))
print(s1|s2) 

# intersection() : extract common elements
print(s1.intersection(s2))
print(s1 & s2)
print(s1)
print(s2)

# intersection_update() : extract common elements, also update the calling set
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}
print(s1.intersection_update(s2))
print(s1)
print(s2)

# difference(): removes the elements 
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}
print(s1.difference(s2))
print(s1 - s2)
print(s1)
print(s2)

# difference_update(): removes the elements and update calling set
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}
print(s1.difference_update(s2))
print(s1)
print(s2)

# symmetric_difference : removes common elements and takes the combined elements left in both
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}
print(s1.symmetric_difference(s2))
print(s1 ^ s2)
print(s1)
print(s2)

# symmetric_difference_update : removes common elements and takes the combined elements left in both, and updates calling set
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}
print(s1.symmetric_difference_update(s2))
print(s1)
print(s2)

# issubset() : checks if given set is subset of another set 
s1 = {10,20,30,40,50}
s2 = {40,50}
s3 = {80,90}
print(s2.issubset(s1))
print(s3.issubset(s1))

# issuperset() : checks if given set is superset of another set 
print(s1.issuperset(s2))
print(s1.issuperset(s3))

# isdisjoint() : check if sets have no common elements 
print(s1.isdisjoint(s2))
print(s3.isdisjoint(s1))