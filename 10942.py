import sys
input = sys.stdin.readline
n = int(input())
nums =[-1] + list(map(int, input().split()))
m = int(input())
dp = [{i:True} for i in range(n+1)]

for i in range(2,n+1):
    if nums[i] == nums[i-1]:
        dp[i][i-1] =True
    for s in dp[i-1]:
        if nums[i] == nums[s-1]:
            dp[i][s-1] = True

for _ in range(m):
    s,e = map(int, input().split())
    if s in dp[e]:
        print(1)
    else:
        print(0)