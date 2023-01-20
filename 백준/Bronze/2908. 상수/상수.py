nums = input().split()
answer = max(int(i[-1::-1]) for i in nums)
print(answer)