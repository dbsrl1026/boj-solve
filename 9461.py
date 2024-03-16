import sys

test = int(sys.stdin.readline())
memo = {1:1, 2:1,3:1,4:2,5:2,6:3,7:4,8:5}
def topDown(n):
    if n not in memo:
        memo[n] = topDown(n-1)+topDown(n-5)
    return memo[n]
for _ in range(test):
    n = int(sys.stdin.readline())
    print(topDown(n))