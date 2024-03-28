import sys
from collections import defaultdict
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())
tree = defaultdict(list)
for _ in range(n - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
dp = [[0, 1] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]

def dfs(now):
    visited[now] = True
    for next in tree[now]:
        if visited[next] is False:
            dfs(next)
            dp[now][0] += dp[next][1]
            dp[now][1] += min(dp[next])

dfs(1)
print(min(dp[1]))