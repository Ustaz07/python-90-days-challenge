# Index Error: As the name says, it is error when accessing index that does not exist in list, topple, set, string etc.
# nOTE that always: Index = [length-1] for every given set because it start from the offset 0 at the beginning.

names = ["Jenny", "Piya", "Payal"]

print(names[5])   # This will give index error
# print(names[3])   # This will give index error
# print(names[-1])  # This will give index error


length = len(names)

print(length)
print(names[length-1])





