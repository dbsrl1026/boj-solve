import sys

n = int(sys.stdin.readline())
memo = {1:1,2:3,3:5}

for i in range(4,n+1):
    memo[i] = memo[i-2]*2+memo[i-1]
print(memo[n]%10007)