import sys

def fac(x):
    if x > 0:
        return x*fac(x-1)
    else:
        return 1

n = int(sys.stdin.readline().strip())
print(fac(n))