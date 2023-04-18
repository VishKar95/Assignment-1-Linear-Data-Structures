'''
The Tower of Hanoi is a classic problem in computer science and mathematics that involves moving a stack of discs of different 
sizes from one peg to another, using a third peg as an intermediate. The problem has the following rules:

Only one disc can be moved at a time.
Each move consists of taking the upper disc from one of the stacks and placing it on top of another stack or on an empty peg.
No larger disc may be placed on top of a smaller disc.
Here's a Python program to implement the Tower of Hanoi algorithm recursively:
'''

def tower_of_hanoi(n, source, destination, auxiliary):
    
    if n == 1:
        print(f"Move disc 1 from {source} to {destination}")
        return
    tower_of_hanoi(n-1, source, auxiliary, destination)
    print(f"Move disc {n} from {source} to {destination}")
    tower_of_hanoi(n-1, auxiliary, destination, source)

tower_of_hanoi(3, 'A', 'C', 'B')

