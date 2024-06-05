n = int(input())
ans = 0
steal = []
for _ in range(n):
    l = int(input())
    zems = list(map(int, input().split()))
    dp = []
    dp.append([zems[0],0])
    for i in range(1, l):
        if dp[i-1][0] > 0:
            dp.append([dp[i-1][0] + zems[i],dp[i-1][1] - 1])
        else:
            dp.append([zems[i], 0])

    max_val = max(dp)
    max_index = dp.index(max_val)
    ans += max_val[0]
    steal.append([max_index+1 + max_val[1], max_index+1])

print(ans)
for temp in steal:
    print(*temp)