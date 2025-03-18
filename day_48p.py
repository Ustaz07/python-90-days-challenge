# FizzBuzz interview Question

# Program to print nos from 1 - 100
# no divisible by 3 print Fizz
# no divisible by 5 print Buzz
# no divisible by both 3 & 5 print FizzBuzz

count = 0
for i in range(0,100,1):
    count = count + 1
    if (count % 3 == 0) and (count % 5 == 0):
        print("FizzBuzz")
    elif count % 3 == 0:
        print("Fizz")
    elif count % 5 == 0:
        print("Buzz")
    else:
        print(count)







