import sys
n, k = map(int,sys.stdin.readline().split())
coin = []
for _ in range(n):
    coin.append(int(sys.stdin.readline()))
coin = sorted(coin)
dp = [0 for _ in range(k+1)]
dp[0] = 1
for c in coin:
    for i in range(k+1):
        if i>=c:
            dp[i] += dp[i-c]
print(dp[k])
