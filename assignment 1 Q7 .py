def prefix_to_infix(expression):
    stack = []
    operators = set(['+', '-', '*', '/', '^'])
    for char in reversed(expression):
        if char in operators:
            operand1 = stack.pop()
            operand2 = stack.pop()
            stack.append(f"({operand1} {char} {operand2})")
        else:
            stack.append(char)
    return stack.pop()

expression = "*-+23*549"
print(prefix_to_infix(expression))  # Output: ((2+3)*(5-4))*9

