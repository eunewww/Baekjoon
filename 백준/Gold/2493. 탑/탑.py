import sys

n = int(sys.stdin.readline().strip())
tops = list(map(int,sys.stdin.readline().split()))
stack = []
ans = [0]*n

for i in range(n):
    while stack and tops[stack[-1]]<tops[i]:
        stack.pop()
    if stack :
        ans[i] = stack[-1] + 1
    stack.append(i)
    
print(' '.join(map(str,ans)))