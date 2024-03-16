import sys

n,r,c = map(int,sys.stdin.readline().split())
loc = 0
for i in range(1,n+1):
    temp = 2**(n-i)
    if r >= temp:
        loc += 2*temp**2
        r-=temp
    if c >= temp:
        loc += temp**2
        c-=temp

print(loc)