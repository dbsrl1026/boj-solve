n, k = map(int, input().split())

dp = []

for i in range(5):
    dp.append(k ** i)

for i in range(5, 7):
    temp = dp[i - 1] * k - dp[i - 5] * 2
    dp.append(temp)

for i in range(7, n + 1):
    temp = dp[i - 1] * k - dp[i - 5] * 2 + dp[i - 7]
    dp.append(temp % 1000000009)
print(dp[n])
