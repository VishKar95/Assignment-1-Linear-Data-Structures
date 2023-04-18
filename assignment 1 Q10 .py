class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
        
    def push(self, item):
        self.stack.append(item)
        if not self.min_stack or item <= self.min_stack[-1]:
            self.min_stack.append(item)
            
    def pop(self):
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        return self.stack.pop()
        
    def get_min(self):
        return self.min_stack[-1]


stack = MinStack()
stack.push(5)
stack.push(2)
stack.push(7)
stack.push(1)
print(stack.get_min())  # Output: 1
stack.pop()
print(stack.get_min())  # Output: 2
