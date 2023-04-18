'''
Infix, prefix, and postfix are three different ways of writing arithmetic expressions.

Infix notation is the standard notation for writing arithmetic expressions in which the operator is placed between the 
operands, such as 2 + 3 or (4 * 5) - 6.

Prefix notation, also called Polish notation, is a way of writing arithmetic expressions in which the operator is placed 
before the operands, such as + 2 3 or - * 4 5 6.

Postfix notation, also called reverse Polish notation, is a way of writing arithmetic expressions in which the operator is 
placed after the operands, such as 2 3 + or 4 5 * 6 -.

Here's a Python program to convert a postfix expression to a prefix expression:
'''

def postfix_to_prefix(expression):
    stack = []
    for char in expression:
        if char.isdigit():
            stack.append(char)
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            stack.append(char + operand1 + operand2)
    return stack.pop()

expression = "23+45*-"
print(postfix_to_prefix(expression))  # Output: -*+2345
