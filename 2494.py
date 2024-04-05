n = int(input())
now = list(input())
now = list(map(int, now))
target = list(input())
target = list(map(int, target))

dp = [[0] * 10 for _ in range(n + 1)]
path = [[0] * 10 for _ in range(n + 1)]

for i in range(n-1, -1, -1):
    for j in range(10):
        move = (target[i] - now[i] - j) % 10
        left = move + dp[i + 1][(move + j) % 10]
        right = 10 - move + dp[i + 1][j]
        if left < right:
            dp[i][j] = left
            path[i][j] = move
        else:
            dp[i][j] = right
            path[i][j] = move - 10
print(dp[0][0])
j = 0
for i in range(n):
    p = path[i][j]
    print(i + 1, p)
    if p > 0:
        j = (p + j) % 10
