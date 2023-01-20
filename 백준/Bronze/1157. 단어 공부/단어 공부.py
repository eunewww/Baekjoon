word = input().upper()
max = 0
for s in set(word):
    count = sum(1 for i in word if s == i)
    if count > max: 
        max = count
        answer = s
    elif count == max:
        answer +=s

print(answer if len(answer) ==1 else '?')