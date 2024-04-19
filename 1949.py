import sys
sys.setrecursionlimit(10**6)
n = int(sys.stdin.readline())
people = [0] + list(map(int, sys.stdin.readline().split()))
tree = [[] for _ in range(n + 1)]
dp = [[0, 0] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)

def dfs(node):
    visited[node] = True
    dp[node][1] += people[node]
    for child in tree[node]:
        if not visited[child]:
            dfs(child)
            dp[node][0] += max(dp[child][0], dp[child][1])
            dp[node][1] += dp[child][0]

dfs(1)
print(max(dp[1]))