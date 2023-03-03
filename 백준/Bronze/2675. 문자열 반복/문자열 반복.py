# 첫번째 풀이
# n = int(input())
# S = [input().split() for i in range(n)]
# for s in S:
#     answer = ''.join(list(int(s[0])*i for i in s[1]))
#     print(answer)

import sys

n = int(sys.stdin.readline().strip())

def SRP():
    case = sys.stdin.readline().split()
    word = ''
    for i in case[1]:
        word +=i*int(case[0])
    print(word)

for i in range(n): SRP()


