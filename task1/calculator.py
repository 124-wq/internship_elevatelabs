print("Calculator: press x to exit")
while(True):
    op1 = int(input("operand 1: "))
    op2 = int(input("operand 2: "))
    operator = input("operator(+,-,*,/,%):")
    if operator == '+':
        print(op1 + op2)
    elif operator =='-':
        print(op1-op2)
    elif operator =='*':
        print(op1*op2)
    elif operator =='/':
        print(op1/op2)
    elif operator =='%':
        print(op1%op2)
    elif operator == 'x':
        break
    else:
        print("invalid operator")