# find if a given no is leaf year or not
# algorithm
# 1) Check if the year is divisible by 4.
# 2) If not, Check if the year is divisible by 100.
# 3) if not, Check if the year is divisible by 400.
# 4) if the year is divisible by 400 it is a leaf year.
# 5) if the year is not divisible by 400 it is not a leaf year.

# 1) if the year is evenly divisible by 4, go to step 2. Other wise, go to step 5.
# 2) if the year is evenly divisible by 100, go to step 3. Other wise, go to step 4.
# 3) if the year is evenly divisible by 400, go to step 4. Other wise, go to step 5.

# 4) The  year is a leaf year (it has 366 days)
# 5) The  year is not a leaf year (it has 365 days)


# condition
# 1) if the year is multiple of 400
# 2) if the year is multiple of 4 and not multiple of 100.



# year = int(input("Enter a year to check if it is a leaf year:- "))

# if (year % 4 == 0):
#     print("This is a leaf year.")
# elif (year % 100 == 0):
#     print("This is a leaf year.")
# elif (year % 400 == 0):
#     print("This is a leaf year.")
# else:
#     print("This is NOT a leaf year.")




year = int(input("Enter a year to check if it is a leaf year:- "))

if (year % 400 == 0):
    print("This is a leaf year (It is multiple of 400).")
elif (year % 4 == 0):
    if (year % 100 != 0):
        print("This is a leaf year (It is multiple of 4 NOT multiple of 100).")
    else:
        print("This is NOT a leaf year (It is multiple of 4 and 100).")
else:
    print("This is not a leap year (It is not divisible by 400 or divisible by 4 but not by 100).")
