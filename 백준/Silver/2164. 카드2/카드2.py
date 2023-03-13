import sys


class Que:
    def __init__(self, capacity):
        self.no = 0 #현재 데이터 개수
        self.front = 0 #맨앞 원소 커서
        self.rear = 0   #맨끝 원소 커서
        self.que = [None] * capacity
        self.capacity = capacity
    
    def size(self): 
        return self.no
    
    def empty(self):
        return self.no <= 0 
    
    def push(self, value):
        self.que[self.rear] = value
        self.rear += 1
        self.no += 1
        if self.rear == self.capacity:
            self.rear = 0 

    def pop(self):
        if self.empty():
            return -1
        else:
            value = self.que[self.front]
            self.front +=1
            self.no -= 1
            if self.front == self.capacity:
                self.front = 0
            return value
    
    def frontf(self):
        if self.empty():
            return -1
        else:
            return self.que[self.front]

    def back(self):
        if self.empty():
            return -1
        else:
            return self.que[self.rear-1]    


n = int(sys.stdin.readline().strip())
a = Que(n)

for i in range(n):
    a.push(i+1)

while a.size() > 1:
    a.pop()
    tmp = a.pop()
    a.push(tmp)

print(a.frontf())