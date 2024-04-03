test = int(input())
coins = [1, 10, 25]
for _ in range(test):
    choco = int(input())
    answer = 0
    dp = [10 ** 15 for _ in range(100)]
    dp[0] = 0
    for c in coins:
        for i in range(c, 100):
            dp[i] = min(dp[i], dp[i - c] + 1)
    while choco:
        answer += dp[choco % 100]
        choco //= 100
    print(answer)
