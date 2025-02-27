# Type casting: it its also call type conversion
# Type checking(type())

length = len("Jenny Khatri")

new_length = str(length) 

print("Your name has " + new_length + " character")

print(type(length))
print(type(new_length))


"""

int()
float()
str()

"""

print(int("10") + int("10"))

print(int("10") + float("17"))

name = "123"

print(7 + int(name))

# take 3 no & add
a = input("Enter the first no: ")
b = input("Enter the second no: ")

c = int(a) + int(b)
print(c)