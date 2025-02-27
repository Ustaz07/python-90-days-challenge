# Love calclator

name1 = input("Enter the first Full name: ")
name2 = input("Enter the second Full name: ")

lower_name1 = name1.lower()
lower_name2 = name2.lower()

names = lower_name1 + lower_name2

love = "TRUE LOVE"

namea = names.count("t")
nameb = names.count("r")
namec = names.count("u")
named = names.count("e")

namee = names.count("l")
namef = names.count("o")
nameg = names.count("v")
nameh = names.count("e")

total_names1 = namea + nameb + namec + named
total_names2 = namee + namef + nameg + nameh

str_total_names1 = str(namea + nameb + namec + named)
str_total_names2 = str(namee + namef + nameg + nameh)

cummlative_total = total_names1 + total_names2
str_cummlative_total = str_total_names1 + str_total_names2

print(str_total_names1)
print(str_total_names2)

if (total_names1 >= 9):
    print(f"Your score is {str_cummlative_total} %, you are coke & mintos")
elif (total_names1 == 4 or 5):
    print(f"Your score is {str_cummlative_total} %, you are together.")
else:
    print(f"Your score is {str_cummlative_total} %.")


# print(cummlative_total + "%")

