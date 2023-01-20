alph = 'abcdefghijklmnopqrstuvwxyz'
s = input()
result = [s.index(i) if i in s else -1 for i in alph]
print(*result,sep=' ')