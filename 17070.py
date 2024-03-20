#dp
n = int(input())
grid = []
dp = [[[0] * 3 for _ in range(n)] for _ in range(n)]
for i in range(n):
    grid.append(list(map(int, input().split())))
for i in range(n):
    if grid[0][i] == 1:
        break
    dp[0][i] = [1, 0, 0]
grid[1][0] = 1
for i in range(1, n):
    for j in range(1, n):
        if grid[i][j] == 0:
            dp[i][j][0] = dp[i][j - 1][0] + dp[i][j - 1][1]
            dp[i][j][2] = dp[i - 1][j][2] + dp[i - 1][j][1]
            if grid[i - 1][j] == 0 and grid[i][j - 1] == 0:
                dp[i][j][1] = sum(dp[i - 1][j - 1])
print(sum(dp[n-1][n-1]))

