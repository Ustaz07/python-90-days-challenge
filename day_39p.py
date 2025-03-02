# import random

# human_choice = int(input("Enter ---->Paper(0)---->Rock(1)---->Scissor(2)----> to guess: "))
# comp_choice = random.randint(0, 2)
# print(f"Computer chose: {comp_choice}")

# print(human_choice)
# print(comp_choice)

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

paper = '''
    -------
---'   ____)
     (______)
     (_______)
     (_______)
----_(_____)

'''

rock = '''
    -------
---'   ____)
     __________)
     ____________)
     ___________)
----_________)

'''

scissors = '''
    -------
---'   ____)___
     __________)
     ____________)
     (____)
----_(___)

'''
images = [paper, rock, scissors]

# (0) Paper -------> (1) Rock -----------> (2) Scissors

selection = int(input("Select (0) for Paper, (1) for Rock, (2) for Scissors : "))

user_choice = selection
comp_choice = random.randint(0,2)


print("comp_choice")
print(images[comp_choice])

if (user_choice < 0 or user_choice >2):
    print("This is a wrong input try again")
else:
    print("user_choice")
    print(images[user_choice])

    if (user_choice == comp_choice):
        print("It is a draw")
    elif (user_choice < comp_choice):
        print("User wins")
    elif (user_choice > comp_choice):
        print("Comp. wins")
    elif (user_choice == 0 and comp_choice == 2):
        print("Comp. wins")
    elif (user_choice == 2 and comp_choice == 0):
        print("User wins")
    else:
        print("Wrong selection")





