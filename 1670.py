n = int(input())

dp = {}
dp[0] = 1
dp[2] = 1

if n == 2:
    print(1)
    exit(0)
for i in range(4, n + 1, 2):
    dp[i] = 0
    for j in range(0, i//2, 2):
        left = j
        right = i - j - 2
        if left != right:
            dp[i] += dp[left] * dp[right] * 2
        else:
            dp[i] += dp[left] * dp[right]
    dp[i] %=987654321
print(dp[n])
