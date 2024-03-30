n = int(input())
maze = list(map(int, input().split()))
dp = [10000] * n
dp[0] = 0
for i in range(n):
    for j in range(1, maze[i] + 1):
        if i + j < n:
            dp[i + j] = min(dp[i + j], dp[i] + 1)
if dp[n - 1] == 10000:
    print(-1)
else:
    print(dp[n - 1])
