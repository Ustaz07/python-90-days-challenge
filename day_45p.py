# Maximum number from a list of numbers.
# max() and are not allowed. only split() and range() are allowed.

list1 = input("Enter the list of numbers separated by space: ")
splitted_list = list1.split()

print(splitted_list)
print(type(splitted_list))

#to traverse we used for loop
count = 0
for i in splitted_list:
    count = count + 1
print(count)

#to convert to int we use range
for i in range(0,count):
    splitted_list[i] = int(splitted_list[i])
print(splitted_list)

#to find the max
max_number = splitted_list[0]
for number in splitted_list:
    if number > max_number:
        max_number = number
print(max_number)








# # How to find maximum number

# numbers = [33, -7, 31, 55, 0]
# maximum_number = numbers[0]
# for number in numbers:
#     if number > maximum_number:
#         maximum_number = number
# print(maximum_number)







# numbers = [1,-2,33,4,5]
# max_number = numbers[3]
# for n in numbers:
#     if n > max_number:
#         max_number = n
# print(max_number)





# numbers = [1,-2,33,4,5]
# number = numbers[0]
# for n in numbers:
#     if n > number:
#         number = n
# print(number)







# number_list = [1,22,3]
# max_number = number_list[0]
# print(max_number)
# for number in number_list:
#     if number > max_number:
#         max_number = number
# print(max_number)








# # Program to find maximum number from a list of numbers
# # Dont used max() only used split() and range() functions.

# list1 = input("Enter the list of numbers separated by space: ")
# splitted_list = list1.split()

# print(splitted_list)
# print(type(splitted_list))

# #to traverse we used for loop
# count = 0
# for i in splitted_list:
#     count = count + 1
# print(count)

# #to convert to int we use range
# for i in range(0,count):
#     splitted_list[i] = int(splitted_list[i])
# print(splitted_list)

# #to find the max

# max_number = splitted_list[0]
# for i in splitted_list:
#     if i > max_number:
#         max_number = i
# print(max_number)


