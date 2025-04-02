# Loop control statements: Break, continue & pass (They are used to change the flow of execution of loop)
# Control statements can only be used within for and while loop.

# break:  break statement terminates the current loop and resumes execution at the next statement.
#   break: is use to exit the loop completely.

# continue: The continue statement returns the control to the beginning of the while loop. 
# continue: continue with the next iteration.
#   continue: is use to skip a section of the loop and continue with the next iteration.

# pass: The pass statement is used  when a statement is required syntactically but you do not want any 
#   command or code to execute.  The pass is a null operation; useful in places where your code has not been written 
#   yet (eg loop, class, function, control statement, method etc). 
#   continue: is use to do nothing.




#BREAK..................................

count = 1
while count <= 10:
    print(count)
    count = count + 1
    if count == 7:
        break
    print("Hi")
print("Out from the loop")




list1 = ["hi", "hello", "welcome"]
names = ["sman", "ibm", "gmj"]

for item in list1:
    for name in names:
        print(item, name)
        if item == "hello" and name == "ibm":
            break
    print("Out of first loop")
print("Out of second loop")



#CONTINUE..................................................

count = 1
while count <= 10:
    print(count)
    count = count + 1
    if count == 7:
        continue
    print("Hi")
print("Out from the loop")





#PASS.............................................
for i in range(5):
    pass













