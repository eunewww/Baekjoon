import sys

n = int(sys.stdin.readline().strip())

def SRP():
    case = sys.stdin.readline().split()
    word = ''
    for i in case[1]:
        word +=i*int(case[0])
    print(word)

for i in range(n): SRP()
