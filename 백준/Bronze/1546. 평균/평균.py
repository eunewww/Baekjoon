N = int(input())
r = list(map(int, input().split()))
max_r = max(r)
print(round(sum(i/max_r*100 for i in r)/N,5))