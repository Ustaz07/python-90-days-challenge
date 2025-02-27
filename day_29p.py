# # height = float(input("Please enter your height in meters: "))

# # child = 150
# # young = 250
# # adult = 500

# # if (height >= 3):
# #     print("You can ride.")
# #     age = int(input("input age: "))
# #     if (age < 12):
# #         option = input("Do you want a photo with 50 Rs addition charges? (Y/N): ")
# #         if (option == "y" or option == "Y"):
# #             print(f"Pay {child + 50} Rs")
# #         elif (option == "n" or option == "N"):
# #             print(f"Pay {child}")
# #         else:
# #             print("input invalid choose a yes(Y) or no(N) from the options")
# #     elif (age <= 18):
# #         option = input("Do you want a photo with 50 Rs addition charges? (Y/N): ")
# #         if (option == "y" or option == "Y"):
# #             print(f"Pay {young + 50} Rs")
# #         elif (option == "n" or option == "N"):
# #             print(f"Pay {young}")
# #         else:
# #             print("input invalid choose a yes(Y) or no(N) from the options")
# #     else:
# #         option = input("Do you want a photo with 50 Rs addition charges? (Y/N): ")
# #         if (option == "y" or option == "Y"):
# #             print(f"Pay {adult + 50} Rs")
# #         elif (option == "n" or option == "N"):
# #             print(f"Pay {adult}")
# #         else:
# #             print("input invalid choose a yes(Y) or no(N) from the options")
# # else:
# #     print("You can not ride.")
# #     print("Bye")




# height = float(input("Please enter your height in meters: "))

# child = 150
# young = 250
# adult = 500

# if (height >= 3):
#     print("You can ride.")
#     age = int(input("input age: "))
#     option = input("Do you want a photo with 50 Rs addition charges? (Y/N): ")
#     if (age < 12):
#         # option = input("Do you want a photo with 50 Rs addition charges? (Y/N): ")
#         if (option == "y" or option == "Y"):
#             print(f"Pay {child + 50} Rs")
#         elif (option == "n" or option == "N"):
#             print(f"Pay {child}")
#         else:
#             print("input invalid choose a yes(Y) or no(N) from the options")
#     elif (age <= 18):
#         # option = input("Do you want a photo with 50 Rs addition charges? (Y/N): ")
#         if (option == "y" or option == "Y"):
#             print(f"Pay {young + 50} Rs")
#         elif (option == "n" or option == "N"):
#             print(f"Pay {young}")
#         else:
#             print("input invalid choose a yes(Y) or no(N) from the options")
#     else:
#         # option = input("Do you want a photo with 50 Rs addition charges? (Y/N): ")
#         if (option == "y" or option == "Y"):
#             print(f"Pay {adult + 50} Rs")
#         elif (option == "n" or option == "N"):
#             print(f"Pay {adult}")
#         else:
#             print("input invalid choose a yes(Y) or no(N) from the options")
# else:
#     print("You can not ride.")
#     print("Bye")




# However, to make the code cleaner and avoid duplication, we can also 
# restructure it like this:
height = float(input("Please enter your height in meters: "))

child = 150
young = 250
adult = 500

if (height >= 3):
    print("You can ride.")
    age = int(input("input age: "))
    option = input("Do you want a photo with 50 Rs addition charges? (Y/N): ")
    
    price = child if age < 12 else young if age <= 18 else adult
    
    if (option == "y" or option == "Y"):
        print(f"Pay {price + 50} Rs")
    elif (option == "n" or option == "N"):
        print(f"Pay {price} Rs")
    else:
        print("input invalid choose a yes(Y) or no(N) from the options")
else:
    print("You can not ride.")
    print("Bye")