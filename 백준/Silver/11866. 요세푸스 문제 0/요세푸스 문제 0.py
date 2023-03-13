import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
result = []
que = deque()

for i in range(1, n+1):
    que.append(i)

while que:
    for i in range(k-1):
        que.append(que.popleft())
    result.append(que.popleft())

print("<",end='')
print(*result, sep=', ', end='')
print(">")
