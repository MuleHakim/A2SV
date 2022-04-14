from math import ceil
 
 
n,m,a = map(int,input().split())
 
temp = ceil((n/a))
temp1 = ceil((m/a))
print(temp*temp1)
