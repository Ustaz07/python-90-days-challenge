# f-string 

name = "Krishna"
age = 30
height = 1.6

# Using typecast and concatination(+)
print("My name is: " +name + " I am " +str(age) + " years old and my height is " + str(height) + " meters." )
print("My name is: " +name, "I am " +str(age), "years old and my height is " + str(height), "meters." )

# Using , 
print("My name is:" ,name, "I am" ,age, "years old and my height is" ,height, "meters." )

# Using f_string 
print(f"My name is: {name} I am {age} years old and my height is {height} meters.")