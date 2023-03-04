import sys

w, h = map(int, sys.stdin.readline().split())
n = int(sys.stdin.readline().strip())

cutw = [0,w]
cuth = [0,h]

for i in range(n):
    check, cut = map(int,sys.stdin.readline().split())
    if check == 0:
        cuth.append(cut)
    else: cutw.append(cut)

def maxl(a):
    piece = []
    a.sort()
    for i in range(len(a)-1):
        piece.append(a[i+1] - a[i])
    return max(piece)

area = maxl(cutw)*maxl(cuth)
print(area)