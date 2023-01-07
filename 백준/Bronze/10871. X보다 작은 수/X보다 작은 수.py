N ,X = map(int ,input().split())
A = list(map(int, input().split()))
answer = list(x for x in A if x < X)
print(*answer)