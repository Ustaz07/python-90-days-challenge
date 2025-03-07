#For loop : Is used for traversing a seqence. ******************
# The seqence may be string, list, tuple etc

names = ["Gmj", "Sman", "Ibm", "Qsm", "Alj"]
for name in names:
    print(names)

for list1 in ["Gmj", "Sman", "Ibm", "Qsm", "Alj"]:
    print(list1)

list2 = "Jenny"
for i in list2:
    print(i)

list5 = ['Jenny', 'Ram', 'Shyam']
for i in list5:
    print(i)
    if i == 'Ram':
        print('Hey its me')




items = [2, 4, 8, 10]

for i in items:
    square = i ** 2
    print(square)



# numbers = [1, 3, 5, 7, 9]

# squa = []
# for x in numbers:
#     squ = x ** 2
#     squa.append(squ)
#     print(squa)





numbers = [1, 3, 5, 7, 9]

squa = []
for x in numbers:
    squ = x ** 2
    squa.append(squ)
print(squa)
print("The list of squa is : ", squa)
print(f"The list of squa is: {squa}")




#******************for loop use with tuple************** 

numbers = (1, 5, 7)

squa = ()
for x in numbers:
    squ = x ** 2
    squa.append(squ)
print(squa)
print("The list of squa is : ", squa)















