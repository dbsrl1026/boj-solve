while 1:
    t = int(input())
    if t == 0:
        exit(0)
    dp = [[1] + [0] * (t + 1) for _ in range(t + 1)]
    for i in range(1, t + 1):
        for j in range(1, i + 1):
            dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
    print(dp[t][t])
