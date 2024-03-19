#dp
n = int(input())

dp = [[0,0] for _ in range(100000)]
dp[1] = [1,0]
dp[2] = [1,0]
if n < 3:
    print(1)
    exit(0)
for i in range(3,n+1):
    dp[i][0] = dp[i-1][0] + dp[i-1][1]
    dp[i][1] = dp[i-2][0]

print((dp[n][0] +dp[n][1]) % 1000000009)