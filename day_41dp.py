#disjoint, subset, superset, their methods and operators
#Note that: clear is a method but del is a keyword
# No operator for disjoint

set1 = {1, 2, 3, 4, 5}
set2 = {4, 10, 7, 8, -10}
set3 = {3, 5}

#*****disjoint*****
print("disjoint")
print(set1.isdisjoint(set2))
print(set3.isdisjoint(set2))
print(set3.isdisjoint(['Gmj', 'Ibm']))


#*****disjoint*****
print("issubset")
print(set1.issubset(set2))
print(set3.issubset(set1))


#*****issubset using operator (<=)*****
print(set3 <= set1)


#*****superset using operator (>=)*****
print("superset")
print(set1 >= set3)


#********  clear and del  ********
print("clear() and del")
print(set2)
set2.clear()
print(set2)

print(set3)
del set3
# print(set3) #it has deleted the whole set thats why it says not defined.



