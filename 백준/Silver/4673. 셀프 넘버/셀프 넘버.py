num = list(range(1,10001))

for n in range(1,10001):
    dn = n + sum(int(i) for i in str(n))
    if dn in num:
        num.remove(dn)

print(*num, sep='\n')