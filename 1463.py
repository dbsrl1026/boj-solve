import sys

n = int(sys.stdin.readline())
memo = {1:0, 2: 1, 3: 1}

for i in range(4, n + 1):
    if i % 3 != 0 and i % 2 != 0:
        memo[i] = memo[i - 1] + 1
    elif i % 3 == 0 and i % 2 != 0:
        memo[i] = min(memo[i - 1], memo[int(i / 3)]) + 1
    elif i % 3 != 0 and i % 2 == 0:
        memo[i] = min(memo[i - 1], memo[int(i / 2)]) + 1
    else:
        memo[i] = min(memo[i - 1], memo[int(i / 2)], memo[int(i / 3)]) + 1

print(memo[n])
