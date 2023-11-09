# Evaluating Expression with Eval

while(1):
    print("Enter an expression you would like to evaluate.(press q to quit)")
    exp = input()

    if exp == 'q':
        break
    try:
        result = eval(exp)
        print("result: " + str(result))
    except:
        print("Error: Invalid Expression")


"""
import sys

def Calculate(first_num, operator, second_num):

    try:
        first_num = float(first_num)
        second_num = float(second_num)
    except ValueError:
        return "Error: Invalid Number" 
    
    if operator == '+':
        value = first_num + second_num
    elif operator == '-':
        value = first_num - second_num
    elif operator == '*':
        value = first_num * second_num
    elif operator == '/':
        if second_num == 0:
            return "Error: Division By Zero"
        else:
            value = first_num / second_num
    else:
        return "Invalid Operator"

    return value

# The main function

while(1):
    print("Enter The first Number.(Enter q) to quit")
    first_num = input()

    if first_num == 'q':
        break

    print("Enter Operator. (+,-,*,/)")
    operator = input()

    print("Enter Second Number.")
    second_num = input()

    value = Calculate(first_num, operator, second_num)
    print(value)

"""

"""
import sys

# Receiving input from user
print("Enter the expression you would like to evaluate.(NO SPACES)")
expression = input()


# Finding result of first operation
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
        sys.exit()
except:
    print("Error. Invalid Expression")
    sys.exit()
    
# Returning result if only one operation
if len(expression) == 3:
    ans = temp
    print("This expression evaluates to: "  + str(ans))

# Otherwise perforiming iteratvley
else:
    try:
        for i in range(3,len(expression)):
            if expression[i] == '+':
                temp = temp + float(expression[i+1])
            elif expression[i] == '-':
                temp = temp - float(expression[i+1])
            elif expression[i] == '*':
                temp = temp * float(expression[i+1])
            elif expression[i] == '/':
                temp = temp / float(expression[i+1])
    except:
        print("Error. Invalid Expression")
        sys.exit()

    # Returning Result 
    ans = temp
    print("This expression evaluates to: " + str(ans))
"""


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
