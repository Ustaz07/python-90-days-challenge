import random
# # # Random choice game in a restaurant between 5 friends.

# # friends_names = input("Enter the names of five friends separate by comma(,): ")

# # text_splitted = friends_names.split(",")

# # print(text_splitted)

# # print(random.choice(text_splitted))




# # Second method game in a restaurant between 5 friends.
# friends_names = input("Enter the names of five friends separate by comma(,): ")
# friends_names_splitted = friends_names.split(",")
# print(friends_names_splitted)

# access_index_random = friends_names_splitted[1]
# random_names = random.randint(0,4)
# print(random_names)




# SPEED TEST EXEERCISE
names = input("Enter names of separated by comma: ")

text_split = names.split(",")
length = len(text_split)
text_split_no = random.randint(0,length)
print(text_split_no)

# pay = random.randint(0,text_split[-1])

print(f"{text_split_no} will pay the bill")