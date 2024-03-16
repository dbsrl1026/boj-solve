nc = int(input())
chu = list(map(int, input().split()))
nm = int(input())
marble = list(map(int, input().split()))

dp = [[False] * (sum(chu) + 1) for _ in range(nc + 1)]
dp[0][0] = True

for i in range(nc):
    for j in range(sum(chu) + 1):
        if dp[i][j]:
            dp[i + 1][j] = True
            dp[i + 1][abs(j - chu[i])] = True
            dp[i + 1][j + chu[i]] = True
answer = ['N' for _ in range(nm)]
for k,v in enumerate(marble):
    for i in range(nc+1):
        if dp[i][v]:
            answer[k] = 'Y'
print(' '.join(answer))