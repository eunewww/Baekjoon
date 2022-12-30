import sys
n = int(sys.stdin.readline().rstrip())
result = [list(map(int, sys.stdin.readline().rstrip().split())) for i in range(n)]

for i,v in enumerate(result):
    print(f'Case #{i+1}: {v[0]} + {v[1]} = {sum(v)}')