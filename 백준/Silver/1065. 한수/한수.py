import sys

n = int(sys.stdin.readline().strip())

if n < 99:
    hs = n
else:
    hs = 99
    for i in range(100,n+1):
        i = list(map(int,str(i)))
        hs += (i[0]-i[1]) == (i[1]-i[2])

print(hs)



# N = int(input())
# 
# if N > 99:
#     num = 99 
#     for n in range(100, N+1):
#         a = list(map(int, str(n))) #N은 최대 1000
#         if a[0]-a[1] == a[1]-a[2]: num += 1
#     print(num)
# else : print(N)
