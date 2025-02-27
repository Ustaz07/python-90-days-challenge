# # Operators in python: Are symbol use to perform operation on values(eg 3+5) or variables(eg a+b).
# # In (5+3), + is an Operator &  5 & 3 is are Operand.
# # Example of Operator are: Arithmet, Relational/comparison, Logical, Assignment, Bitwise, Identity, Membership.

# # Arithmetic are +, -, *, /, %

# floor division (//) eg 4//2 gives int not float 
# power (**) eg 2**3





### ARITHMETIC (PEMDAS); the Precedence IS CALLED (PEMDAS) 
We use Precedence & Associativity to solve it. 
Parenthesis: ()
Exponent: **
MUltiplication & Division: *, /, //, %
Addition & Sbstraction: +, -

# NOTE THAT ONCE THE Precedence IS THE SAME THEN ASSOCIATIVITY COMES IN TO PLAY. eg in case of *, /, //, % and these +, - 
# where by ASSOCIATIVITY rule says for MUltiplication we go from Left --> Right, for Addition we go from Left --> Right,
# while for power we go from Right --> Left.

# a = 5+2*(3-1)+10/5

# print(a)

# weight in kg & height in meters

weight = input("Enter the weight in kg: ")
height = input("Enter the height in meters: ")



int_weight = int(weight)
float_height = float(height)

Body_Mass_Index = int_weight/(float_height ** 2)

print(Body_Mass_Index)

print(type(int_weight))
print(type(float_height))
