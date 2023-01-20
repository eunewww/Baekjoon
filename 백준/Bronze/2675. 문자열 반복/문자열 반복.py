n = int(input())
S = [input().split() for i in range(n)]
for s in S:
    answer = ''.join(list(int(s[0])*i for i in s[1]))
    print(answer)