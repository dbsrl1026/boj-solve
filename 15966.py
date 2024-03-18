n = int(input())
arr = list(map(int,input().split()))

dp = [0 for _ in range(1000001)]

for v in arr:
    dp[v] = max(dp[v], dp[v-1] + 1)

print(max(dp))