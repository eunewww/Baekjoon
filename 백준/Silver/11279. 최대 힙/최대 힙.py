import sys
import heapq

n = int(sys.stdin.readline().strip())
h = [] #힙

for i in range(n):
    cal = int(sys.stdin.readline().strip())
    if cal == 0:
        if len(h) == 0:
            print(0)
        else:
            print(heapq.heappop(h)[1])
    else:
        heapq.heappush(h,(-1*cal, cal))