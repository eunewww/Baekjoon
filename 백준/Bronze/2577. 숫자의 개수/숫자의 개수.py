m = 1
for _ in range(3):
    m *= int(input()) 

numbers = list(map(int, str(m)))
for i in range(10):
    result = sum(1 for number in numbers if i == number)
    print(result)