n = int(input())
costs = list(map(int, input().split()))
money = int(input())

dp = [-10000000 for _ in range(money + 1)]

for num in range(n-1, -1, -1):
    cost = costs[num]
    for i in range(cost, money+1):
        dp[i] = max(dp[i], num, dp[i-cost] * 10 + num)
print(dp[money])
