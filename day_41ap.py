### Set:- Is a list

set1 = {10, True, 'Jenny', 1.11}
set2 = {1, 2, -10, 10,  0, 53}

print(set1)
print(set2)

set3 = {} # Not allowed for empty set it will print dictionary.
set4 = set() # This is empty set.
  
print(type(set3))
print(type(set1))

set5 = {99}

set1.add(99)

print(set1)
print(len(set1))

set1.remove(1.11)
print(set1)

# set1.remove(100)

set1.discard('Jenny')
print(set1)

set2.clear()
print(set2)

popped = set1.pop()
print(set1)

print(popped)

set1.add((45, 39, 77))
print(set1)














