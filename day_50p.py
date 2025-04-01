# Loop: we used loop when we want to execute statements multiple times.
# While loop: Is used when you want to execute a block of statement repeatedly, untill a given condition is true. 
# We used while loop when we dont know the no of times the statement will be executed.
# sentinel value.......

count = 0
while count <= 5:
    print(count)
    count = count + 1


list1 = [1, 2, 0, 5, 6]
while list1:
    print("Hi Jenny!")
    pop = list1.pop()
    print(pop)


# Whlie...else loop; in this the else part execute only after successfully completing the while loop part not 
#forcefully like using a break statement

count = 0
while count <= 5:
    print(count)
    count = count + 1
else:
    print("Succesfully completed the while part, now in else block")
print("Out from the loop")



count = 0
while count <= 5:
    print(count)
    count = count + 1
    if count == 3:
        break
else:
    print("Succesfully completed the while part, now in else block")
print("Out from the loop")



count = 1
while count < 1:
    print(count)
    count = count + 1
else:
    print("Succesfull")
print("Out of loop")







# count = 0
# while True:
#     print(count)
#     count = count + 1
#     # if count == 5:
#     #     break
# else:
#     print("In else block")
# print("Out from the loop")






# # Comparison b/w while...loop & for...loop
# number = int(input("Enter a no (-1 to quite) : "))
# while number != -1:
#     print(number)
#     number = int(input("Enter a no (-1 to quite) : "))
# else:
#     print("Succesfull completion of while block")
# print("Now out of else block")




# # Calculate the sum of positive integer; either positive or negative, if user enter 0 quite!!!
# number = int(input("Enter a no either positive or negative to Calculate the sum (0 to quite) : "))
# while number != 0:
#     summ = number ** 2
#     print(summ)
#     break



# number = int(input("Enter a no either positive or negative to Calculate the sum (0 to quite) : "))
# total = 0
# while number != 0:
#     total = total + number
#     number = int(input("Enter a no either positive or negative to Calculate the sum (0 to quite) : "))
# print(total)









number = int(input("Enter a no, (0 to quit): "))
total = 0
while number !=0:
    total = total + number
    print(total)
    number = int(input("Enter a no, (0 to quit): "))











