import sys

def primecheck(a):
    check= 1*(a>1)
    sr = int(a**0.5)
    for i in range(2,sr+1):
        if (a % i == 0):
            check = 0
            break
    return check
     
n = int(sys.stdin.readline().strip())
numbers = list(map(int, sys.stdin.readline().split()))
answer = sum(primecheck(i) for i in numbers)
print(answer)
