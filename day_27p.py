# Updated version Body Mass Index (BMI) to tell if over weight, normal or under weight

# Under weight: <= 18.4
# Normal weight 18.5  to 24.9
# Over weight 25.0 to 29.9
# Obese >= 30
# weight in kg(int) and height in meters(float)

weight = int(input("Enter the weight in kg: "))
height = float(input("Enter the height in meters: "))

BMI = round(weight/(height ** 2))

# print(BMI)

if (BMI <= 18.4):
    print(f"Your weight is {BMI} kg/m2, You are under weight.")
elif (BMI <= 24.9):
    print(f"Your weight is {BMI} kg/m2, You have normal weight.")
elif (BMI <= 29.9):
    print(f"Your weight is {BMI} kg/m2, You are Over weight.")
else:
    print(f"Your weight is {BMI} kg/m2, You are Obese.")











