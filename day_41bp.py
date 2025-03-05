# Union or (|), intersection or (&), difference (-), symmetric_difference or (^)

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 10, 11}

set3 = {'Ram', 'Shyam', 'Jenny'}
set4 = {'Jenny', 'Jiya', 'Aakash'}


#*************************************
print(set3 | set4)
print(set3.union(set4))
print(set3 | set4 | set2 | set1)

print(set3.union(set4, set2,))


#*************************************
set1.update(set2)
print(set1)

set4.update(['3000', '7000'])
print(set4)

set4 |= set1
print(set4)


#****************** intersection --------> &
set6 = {'Gmj', 'Ibm', 'Sman'}
set7 = {1, 7, 9}

print(set6.intersection(set7))


print(set6.intersection(set7, set3))


print(set3 & set4)
print(set3 & set4 & set1)

print(set4.intersection(['Aakash', 'Pradeep']))


#*************** intersection_update:- it update A with what intersect b/w A and B

set8 = {57, 99}
set9 = {57, 58}

set8.intersection_update(set9)
print(set8)



#*************** difference_update
#*************** symmetric_difference_update