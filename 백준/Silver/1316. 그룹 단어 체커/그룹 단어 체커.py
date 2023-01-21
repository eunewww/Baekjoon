n = int(input())
count = 0

for i in range(n):
    word =  input()
    check = '#'
    for i in word:
        if (i != check[-1]) :
            check += i
    if len(check[1:]) == len(set(word)):
        count +=1

print(count)