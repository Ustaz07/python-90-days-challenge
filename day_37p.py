# Nested list : As the name says it is a list, but in nested form.

lst = [10, 34, 90, [45, 78, -3], 89]

print(len(lst))
print(lst[3][2])
print(lst[len(lst)-1])

print(lst[3][0:2])

print(lst[3][::2])

lst1 = [10, 34, 90, ['Mohan', 'Shyam', 'Ram'], 89]

print(lst1[3][-1])

print(lst1[3][2])