N = int(input())
line = list(map(int, input().split()))
v = int(input())
answer = sum(1 for i in line if i == v)

print(answer)