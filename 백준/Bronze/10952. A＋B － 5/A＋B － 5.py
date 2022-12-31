import sys
while True:
    a = sum(map(int, sys.stdin.readline().rstrip().split()))
    if a == 0: break
    else: print(a)