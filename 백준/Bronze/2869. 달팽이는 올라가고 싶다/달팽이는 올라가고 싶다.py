a,b,v = map(int, input().split()) 
day = (v-a)//(a-b) + ((v-a)%(a-b)>0) + 1
print(day)