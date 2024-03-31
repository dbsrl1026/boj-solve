n = int(input())

dp = [[[0, 0, 0, 0, 0] for _ in range(10)] for _ in range(n + 1)]

if n == 1:
    print(10)
    exit(0)

for i in range(10):
    dp[1][i][2] = 1

for i in range(2, n + 1):
    for j in range(10):
        if j < 9:
            dp[i][j][0] = dp[i - 1][j + 1][1]
            dp[i][j][1] = dp[i - 1][j + 1][2] + dp[i - 1][j + 1][3] + dp[i - 1][j + 1][4]
        if j > 0:
            dp[i][j][3] = dp[i - 1][j - 1][2] + dp[i - 1][j - 1][1] + dp[i - 1][j - 1][0]
            dp[i][j][4] = dp[i - 1][j - 1][3]

answer =0
for j in range(10):
    for k in range(5):
        answer += dp[n][j][k]

print(answer%1000000007)