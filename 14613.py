W, L, D = map(float, input().split())
dp = [[0 for _ in range(3500)] for _ in range(21)]
dp[0][2000] = 1.0

for i in range(20):
    for j in range(1000,3000):
        if dp[i][j] > 0:
            dp[i + 1][j + 50] += dp[i][j] * W
            dp[i + 1][j - 50] += dp[i][j] * L
            dp[i + 1][j] += dp[i][j] * D
b = sum(dp[20][1000:1500])
s = sum(dp[20][1500:2000])
g = sum(dp[20][2000:2500])
p = sum(dp[20][2500:3000])
d = dp[20][3000]

print(f'{b:.8f}')
print(f'{s:.8f}')
print(f'{g:.8f}')
print(f'{p:.8f}')
print(f'{d:.8f}')