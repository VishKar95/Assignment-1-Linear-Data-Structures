def reverse_stack(stack):
    if len(stack) == 0:
        return
    top = stack.pop()
    reverse_stack(stack)
    insert_at_bottom(stack, top)
    
def insert_at_bottom(stack, item):
    if len(stack) == 0:
        stack.append(item)
        return
    top = stack.pop()
    insert_at_bottom(stack, item)
    stack.append(top)


stack = [1, 2, 3, 4, 5]
reverse_stack(stack)
print(stack)  # Output: [5, 4, 3, 2, 1]
