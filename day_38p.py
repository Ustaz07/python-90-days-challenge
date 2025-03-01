# Exercise

list1 = [1,1,1]
list2 = [1,1,1]
list3 = [1,1,1]
final_list = [list1, list2, list3]

dimension = input("Please enter the dimension of location to hide money e.g. 33: ")
# print(dimension)
row = int(dimension[0])
column = int(dimension[1])

row_selected = final_list[row-1]
row_selected[column-1] = "X"

print(f"The location is: \n {list1} \n {list2} \n {list3}")






# # Create a 3x3 grid
# grid = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]

# # Ask the user for the location
# dimension = input("Please enter the dimension of location to hide money (e.g., 33): ")

# # Convert input to row and column (subtract 1 because list indexing starts from 0)
# row = int(dimension[0]) - 1
# column = int(dimension[1]) - 1

# # Mark the location with 'X'
# grid[row][column] = "X"

# # Display the grid
# for row in grid:
#     print(row)



#WELCOME BACK EXERCISEs

