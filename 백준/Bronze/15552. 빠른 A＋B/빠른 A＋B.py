import sys
n = int(sys.stdin.readline().rstrip())
result = [sum(map(int, sys.stdin.readline().rstrip().split())) for i in range(n)]
print(*result, sep= '\n')