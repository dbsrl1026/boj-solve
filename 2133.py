n = int(input())

if n % 2 == 1:
    print(0)
    exit(0)
elif n == 2:
    print(3)
    exit(0)
dp = {}
dp[0] = 1
dp[2] = 3

for i in range(4, n + 1 , 2):
    temp = 0
    dp[i] = dp[i -2] * 3
    for j in range(4, i + 1, 2):
        dp[i] += dp[i-j] * 2

print(dp[n])
