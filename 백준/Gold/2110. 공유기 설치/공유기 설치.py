import sys

n,c = map(int, sys.stdin.readline().split())
x = [int(sys.stdin.readline().strip()) for _ in range(n)]
x.sort()


ls = 0
rs = x[-1]-x[0]
result = 0

while ls <= rs:
    dist = (ls+rs)//2
    cnt = 1
    locate = x[0]
    for i in range(1,n):
        if x[i] - locate >= dist:
            locate = x[i]
            cnt +=1
    if cnt >= c:
        result = dist
        ls = dist+1
    else:
        rs = dist-1
print(result)