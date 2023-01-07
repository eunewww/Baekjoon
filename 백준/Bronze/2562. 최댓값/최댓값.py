numbers = list(int(input()) for i in range(9))
max = max(numbers)
print(max, numbers.index(max) + 1, sep='\n')