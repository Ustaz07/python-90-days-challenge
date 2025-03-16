# # count = 0
# # x = 0,23,452
# # for i in x:
# #     count = count + 1
# #     print(count)

# # x = 0
# # for i in range(0,9):
# #     x[i] = int(x[i])
# #     print(x)





# # # for i in range(0,1000000,3):
# # #     # print(i)
# # #     print(min())
# # #     print(max())
# # #     print(sum())

# # list3 = []
# # for i in range(0,1000000,3):
# #     list3.append(i)
# # print(list3)
# # print(min(list3))
# # print(max(list3))
# # print(sum(list3))    







# Program to cal. average height from the list of heights
# sum() and len() funct. are not allowed, only split() and range() are allowed.

heights = input("Enter the list of heights separated by space: ")
splitted_heights = heights.split()

print(splitted_heights)
print(type(splitted_heights))

#to traverse we used for loop
count = 0
for i in splitted_heights:
    count = count + 1
    print(count)


for i in range(0,count):
    splitted_heights[i] = int(splitted_heights[i])
print(splitted_heights)

total = 0
for i in splitted_heights:
    total = total + i
print(total)

average = total/count
print(int(average))
print("Average height is: ", round(average))


