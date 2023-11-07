import sys

print("Enter the expression you would like to evaluate.(NO SPACES)")
expression = input()


# This could maybe be the first function finding the first value and then iterating
temp = 0
ans = 0
try:
    f_num = float(expression[0])
    op = expression[1]
    s_num = float(expression[2])
    if op == '+':
        temp = f_num + s_num
    elif op == '-':
        temp = f_num - s_num
    elif op == '*':
        temp = f_num * s_num
    elif op == '/':
        temp = f_num / s_num
    else:
        print("Error. Invalid Expression")
        sys.exit()
except:
    print("Error. Invalid Expression")
    sys.exit()

if len(expression) == 3:
    ans = temp
    print("This expression evaluates to: "  + str(ans))
else:
    print("There is more work to do beyond this point.")
























"""
import sys

# This is a basic calculator that performs an operation on two numbers

# Entering First Number
print("Select the first number.")
try:
    f_num = float(input())
except ValueError:
    print("Error not a valid number. Calculator Terminated.")
    sys.exit()
    
# Entering an Operator 
print("Select one of the following Operators: +, -, *, /")
operator = input()

# Entering Second Number
print("Select the second number.")
try:
    s_num = float(input())
except ValueError:
    print("Error not a valid number. Calculator Terminated.")
    sys.exit()

# Performing Computation
equals = 0

if operator == '+':
    equals = f_num + s_num
elif operator == '-':
    equals = f_num - s_num
elif operator == '*':
    equals = f_num * s_num
elif operator == "/":
    equals = f_num / s_num
else:
    print("Error invalid operator. Calculator Terminated.")
    sys.exit()

# Displaying Results 
print("The results of your calculation: " + str(equals))

"""
