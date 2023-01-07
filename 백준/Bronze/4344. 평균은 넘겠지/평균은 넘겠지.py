n = int(input())
cases = [list(map(int, input().split())) for i in range(n)]
for case in cases:
    aver = sum(case[1:])/case[0]
    rate = 100* sum(1 for i in case[1:] if i > aver)/case[0]
    print("%.3f%%" %rate)