import random
# # Password Generator
# # Work on easy and hard level
# # use random no's, for loop, range,  small abc, capital ABC, no's 0 to 9, symbols

# print("Welcome to password Generator!: ")

# letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", 
# "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", 
# "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", 
# "U", "V", "W", "X", "Y", "Z",]

# symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+", "-", "=", 
# "/", ":", "|", ";", "~", "'", "`",]

# numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

# n_letters = int(input("How many letters would you like in your password?: "))

# n_symbols = int(input("How many symbols would you like?: "))

# n_numbers = int(input("How many no's would you like?: "))

# # for i in range(0,)

# print(n_letters)
# print(n_symbols)
# print(n_numbers)
# print(type(n_letters))
# print(type(n_symbols))
# print(type(n_numbers))

# password = ""
# for i in range(0,n_letters):
#     char = random.choice(letters)
#     password = password + char
# print(password)

# for i in range(0,n_numbers):
#     char = random.choice(numbers)
#     password = password + char
# print(password)

# for i in range(0,n_symbols):
#     char = random.choice(symbols)
#     password = password + char
# print(password)





# Password Generator
# Work on easy and hard level
# use random no's, for loop, range,  small abc, capital ABC, no's 0 to 9, symbols

print("Welcome to password Generator!: ")

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", 
"o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", 
"E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", 
"U", "V", "W", "X", "Y", "Z",]

symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+", "-", "=", 
"/", ":", "|", ";", "~", "'", "`",]

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

n_letters = int(input("How many letters would you like in your password?: "))

n_symbols = int(input("How many symbols would you like?: "))

n_numbers = int(input("How many no's would you like?: "))

# for i in range(0,)

print(n_letters)
print(n_symbols)
print(n_numbers)
print(type(n_letters))
print(type(n_symbols))
print(type(n_numbers))

password = []                      # we take the password as list[] instead of string""
char = []
for i in range(0,n_letters):
    
    char = random.choice(letters)
    password = password + char


for i in range(0,n_numbers):
    char = random.choice(numbers)
    password = password + char


for i in range(0,n_symbols):
    char = random.choice(symbols)
    password = password + char
print(password)

password = random.shuffle(password)
print(password)



















