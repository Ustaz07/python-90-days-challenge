# Exercise to check if a given no is even or odd

number = int(input("Enter a whole no of your choice: "))

check = number % 2 # to check for even & odd 

if(check == 0):
    print(f"The no is {number}: ")
    print("The no is even")
else:
    print(f"The no is {number}: ")
    print("The no is odd")

