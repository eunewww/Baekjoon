import sys
a,b,c,d = map(int, sys.stdin.readline().split())
d = [a,b,abs(c-a), abs(d-b)]
print(min(d))