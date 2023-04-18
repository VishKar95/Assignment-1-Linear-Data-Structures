def are_brackets_balanced(code):
    stack = []
    for char in code:
        if char in ['(', '[', '{']:
            stack.append(char)
        elif char in [')', ']', '}']:
            if not stack:
                return False
            if char == ')' and stack[-1] != '(':
                return False
            if char == ']' and stack[-1] != '[':
                return False
            if char == '}' and stack[-1] != '{':
                return False
            stack.pop()
    return not stack

code = "for i in range(10): print(i)"
print(are_brackets_balanced(code))  # Output: True

code = "if x == 1: print('x is 1')"
print(are_brackets_balanced(code))  # Output: True

code = "if x == 1: print('x is 1')"
print(are_brackets_balanced(code + ")"))  # Output: False
