import random
# # Tossing a coin,

# coin = input("Press ENTER to toss the coin: ")

# toss = random.randint(0,1)

# print(toss)



# Second method of tosing a coin.

toss = int(input("Guese either head(1) or tail(0) to toss the coin & press enter: "))

print(toss)

random = random.randint(0,1)

print(random)

# to_string = str(toss)


if (random == toss):
    print("you win.")
elif (random != toss):
    print("You loose.")
# elif (toss == to_string):
#     print("You must select either head or tail.")
# else:
#     print("Select wisely.")


