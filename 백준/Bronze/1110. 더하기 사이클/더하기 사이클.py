a = int(input())
n = 0
if a < 10: a *= 10
b = a

while True:
    c = (b//10 + b%10)%10 + 10*(b%10)
    n += 1
    if a == c : break
    else: b = c

print(n)
