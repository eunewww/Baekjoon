n = int(input())
cases = [input() for i in range(n)]
for case in cases:
    b = case.split("X")
    result = sum(len(i)*(len(i)+1)/2 for i in b)
    print(int(result))