# # LIST IS A COLLECTION OF THINGS ENCLOSE IN A SQARE BRACKET & SEPARATED BY A COMMA.
# # WE CAN PERFORM MANY OPERATIONS ON LIST e.g. sort, reverse, extend, append, count, length, minimum, maximum

number = [1, 2, 3, 4, 5]
names = ["Shams", "Sman", "Gamji", "Kusa", "Ibm"]
mix_list = [1, "Jenny", True, 10.10]

print(number)
print(names)
print(mix_list)

print(mix_list[1])
print(mix_list[-1])




# SLICING : Means to cut part of a list.

numbers = [10, 7, 15, -3]

print(len(numbers))

# All these 4 are the same mention all the content of a slice.
print(numbers[0:4])
print(numbers[0:])
print(numbers[:4])
print(numbers[:])

print(numbers[1:3]) # note that index 3 is excluded in the slide from the rule.



# SLICING AND STEPS

print(numbers[0:3:2])




test = [2, 3, 5, 7, 9, 15, 17, 3, 9]
print(len(test))

print(test[1:5:2])

test.sort() 
print(test)     # print works  only on a separate line for sort

test.reverse()
print(test)     # print works  only on a separate line for reverse

print(max(test))
print(min(test))

test.append(47)
print(test)     # print works  only on a separate line for append

test.insert(1,3)
print(test)     # print works  only on a separate line for insert. note that insert add to the list at a specific index

test.extend([73, 75, 77])
print(test)     # print works  only on a separate line for extend. note that extend add to the list at the end of the line

test[0] = 97
print(test)

test[1:4] = [100, 200, 300]
print(test)

test.remove(97)
print(test)

print(test.pop())
print(test)         # Remove and return last element in the list

test.pop(1)
print(test)

print(test.count(3))
print(test)         # Count occurence of item in the list


