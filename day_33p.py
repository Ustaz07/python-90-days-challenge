import random

# Random Module : Is an inbuild function in python used to generate speudo random
# numbers.
# first you write the name of the module then the function.

a = random.randint(1, 7)
print(a)

b = random.randrange(1, 7)
print(b)

c = random.random()
print(c)

d = random.uniform(1, 7)
print(d)

l = [1, 3, 5, 7, 9]
e = random.choice(l)
print(e)

random.shuffle(l)
print(l)



