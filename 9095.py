import sys

test = int(sys.stdin.readline())
memo = {1: 1, 2: 2, 3: 4}

def topDown(n):
    if n not in memo:
        memo[n] = topDown(n-1) + topDown(n-2) + topDown(n-3)
    return memo[n]
for _ in range(test):
    n = int(sys.stdin.readline())
    print(topDown(n))
