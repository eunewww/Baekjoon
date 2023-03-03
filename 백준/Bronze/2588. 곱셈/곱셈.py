# 첫번째
a = int(input())
b = int(input())
print(a*(b%10),a*((b//10)%10),a*((b//10)//10),a*b,sep='\n')

# 두번째 
# import sys
# a= int(sys.stdin.readline().strip())
# b= list(map(int, sys.stdin.readline().strip()))
# result = 0
# b.reverse()

# for i, v in enumerate(b):
#     print(a*v)
#     result += a*v*(10**i)

# print(result)
