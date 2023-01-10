N = int(input())

if N > 99:
    num = 99 
    for n in range(100, N+1):
        a = list(map(int, str(n))) #N은 최대 1000
        if a[0]-a[1] == a[1]-a[2]: num += 1
    print(num)
else : print(N)
