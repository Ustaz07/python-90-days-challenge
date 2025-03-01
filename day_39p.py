# import random
# # # Rock, Scossors and paper
# # # The rule is ---->Paper(0)---->Rock(1)---->Scissor(2)---->

# # human_coice = int(input("Enter ---->Paper(0)---->Rock(1)---->Scissor(2)----> to guese: "))

# # comp_choice = random.randint(0,2)
# # print(comp_choice)

# # if (comp_choice > human_coice):
# #     print("You win")
# # if (human_coice > comp_choice):
# #     print("Computer win")
# # if (comp_choice == 2 and human_coice == 0):
# #     print("Computer win")
# # if (human_coice == 2 and comp_choice == 0):
# #     print("You win")
# # if (human_coice == comp_choice):
# #     print("It is a draw")
# # else:
# #     print("Yo lose because of invalid selection!!!")




# human_coice = int(input("Enter ---->Paper(0)---->Rock(1)---->Scissor(2)----> to guese: "))

# comp_choice = random.randint(0,2)
# print(comp_choice)

# if (0 >= human_coice <= 2):
#     if (comp_choice > human_coice):
#         print("You win")
#     if (human_coice > comp_choice):
#         print("Computer win")
#     if (comp_choice == 2 and human_coice == 0):
#         print("Computer win")
#     if (human_coice == 2 and comp_choice == 0):
#         print("You win")
#     if (human_coice == comp_choice):
#         print("It is a draw")
# else:
#     print("You lose because of invalid selection!!!")







# import random

# human_choice = int(input("Enter ---->Paper(0)---->Rock(1)---->Scissor(2)----> to guess: "))
# comp_choice = random.randint(0, 2)
# print(f"Computer chose: {comp_choice}")

# if 0 <= human_choice <= 2:
#     if human_choice == comp_choice:
#         print("It's a draw!")
#     elif (human_choice - comp_choice) % 3 == 2:  # Fixed condition
#         print("You win!")
#     else:
#         print("Computer wins!")
# else:
#     print("Invalid choice! You lose.")



import random

# (0) Paper -------> (1) Rock -----------> (2) Scissors

selection = input("Select (0) for Paper, (1) for Rock, (2) for Scissors : ")

select = int(selection)

print(select)
user_choice = select
comp_choice = random.randint(0,2)

if (user_choice < comp_choice):
    print("User wins")
elif (user_choice > comp_choice):
    print("Comp. wins")
elif (user_choice == 0 and comp_choice == 2):
    print("Comp. wins")
elif (user_choice == 2 and comp_choice == 0):
    print("User wins")
elif (user_choice == comp_choice):
    print("It is a draw")
else:
    print("Wrong input, try again")



















