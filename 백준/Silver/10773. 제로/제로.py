import sys

class Stack:
    def __init__(self, capacity):
        self.stk = [None] * capacity
        self.capacity = capacity
        self.ptr = 0
    
    def push(self, value):
        self.stk[self.ptr] = value
        self.ptr += 1

    def pop(self):
        self.ptr -= 1
        return self.stk[self.ptr]
    
k = int(sys.stdin.readline().strip())
a = Stack(k)


for _ in range(k):
    n = int(sys.stdin.readline().strip())
    if n == 0:
        a.pop()
    else:
        a.push(n)

print(sum(a.stk[:a.ptr]))