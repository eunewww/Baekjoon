assn = list(int(input()) for i in range(28))
no_assn = [i+1 for i in range(30) if (i+1) not in assn ]
print(*no_assn)