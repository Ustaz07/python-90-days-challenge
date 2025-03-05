#**************** difference (-) and difference_update
#**************** symmetric and symmetric_update

#**************** difference (-)
set1 = {'Sman', 'Gmj', 'Ibm'}
set2 = {'Ibm', 'Qsm', 'Dkk'}
set3 = {'Ankur', 'Pradeep'}
set4 = {'Jenny', 'Ibm', 'Gmj'}

print(set1.difference(set2))
print(set1 - set2)

print(set1.difference('Ankur', 'Pradeep'))

print(set1.difference(set3, set4))
print(set1 - set3 - set4)


#*************** difference_update
set1.difference_update(set2)
print(set1)


#************** Symmetric_difference: Are elements in A and B but not both
print(set1.symmetric_difference(set2))

print(set1 ^ set2)

#print(set1.symmetric_difference(set2, set3)) # Multiple argments not allowed here.
print(set1 ^ set2 ^ set3) # Here it is allowed


#************** Symmetric_difference_update 
set1.symmetric_difference_update(set3)
print(set1)

set3.symmetric_difference_update(('Jiya', 'Aakash'))
print(set3)









