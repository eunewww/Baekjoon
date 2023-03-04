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
for i in range(n):
    number = int(sys.stdin.readline().strip())
    n1, n2 = int(number/2), int(number/2)

    while True:
        if (primecheck(n1) ==1)*(primecheck(n2) == 1):
            print(n1, n2)
            break
        else:
            n1 -=1
            n2 +=1
