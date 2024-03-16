n, s = map(int, input().split())
arr = list(map(int, input().split()))


def dfs(i, add):
    if i == n - 1:
        r = 0
        if add + arr[i] == s:
            r += 1
        if add == s:
            r += 1
        return r
    return dfs(i + 1, add + arr[i]) + dfs(i + 1, add)

ans = dfs(0, 0)
if s == 0:
    ans -=1
print(ans)