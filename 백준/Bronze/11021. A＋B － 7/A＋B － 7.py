import sys
n = int(sys.stdin.readline().rstrip())
result = [sum(map(int, sys.stdin.readline().rstrip().split())) for i in range(n)]

for i, v in enumerate(result, start=1):
    print("Case #{}: {}".format(i,v))