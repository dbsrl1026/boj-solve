import math
import sys
a,b,c = map(int, sys.stdin.readline().split())
memo = {1:a%c}
def dnc(a,b,c):
    if b not in memo:
        memo[b] = dnc(a,int(b/2),c)*dnc(a,math.ceil(b/2),c)%c
    return memo[b]

print(dnc(a,b,c))