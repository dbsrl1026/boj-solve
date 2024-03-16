import sys

n, m = map(int, sys.stdin.readline().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))
maxx = 0
for i in range(n):
    for j in range(m):
        # 작대기
        if j + 3 < m:
            maxx = max(maxx, arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i][j + 3])
        if i + 3 < n:
            maxx = max(maxx, arr[i][j] + arr[i + 1][j] + arr[i + 2][j] + arr[i + 3][j])
        # 네모
        if i + 1 < n and j + 1 < m:
            maxx = max(maxx, arr[i][j] + arr[i + 1][j] + arr[i][j + 1] + arr[i + 1][j + 1])
        if i + 1 < n and j + 2 < m:
            maxx = max(maxx, arr[i][j] + arr[i][j + 1] + arr[i + 1][j + 1] + arr[i][j + 2],
                       arr[i][j] + arr[i][j + 1] + arr[i + 1][j + 1] + arr[i + 1][j + 2],
                       arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j + 2],
                       arr[i][j] + arr[i + 1][j] + arr[i + 1][j + 1] + arr[i + 1][j + 2])
        if i - 1 >= 0 and j + 2 < m:
            maxx = max(maxx, arr[i][j] + arr[i][j + 1] + arr[i - 1][j + 1] + arr[i][j + 2],
                       arr[i][j] + arr[i][j + 1] + arr[i - 1][j + 1] + arr[i - 1][j + 2],
                       arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i - 1][j + 2],
                       arr[i][j] + arr[i - 1][j] + arr[i - 1][j + 1] + arr[i - 1][j + 2])
        if i + 2 < n and j + 1 < m:
            maxx = max(maxx, arr[i][j] + arr[i + 1][j] + arr[i + 1][j + 1] + arr[i + 2][j],
                       arr[i][j] + arr[i + 1][j] + arr[i + 1][j + 1] + arr[i + 2][j + 1],
                       arr[i][j] + arr[i + 1][j] + arr[i + 2][j] + arr[i + 2][j + 1],
                       arr[i][j] + arr[i][j + 1] + arr[i + 1][j + 1] + arr[i + 2][j + 1])
        if i + 2 < n and j - 1 >= 0:
            maxx = max(maxx, arr[i][j] + arr[i + 1][j] + arr[i + 1][j - 1] + arr[i + 2][j],
                       arr[i][j] + arr[i + 1][j] + arr[i + 1][j - 1] + arr[i + 2][j - 1],
                       arr[i][j] + arr[i + 1][j] + arr[i + 2][j] + arr[i + 2][j - 1],
                       arr[i][j] + arr[i][j - 1] + arr[i + 1][j - 1] + arr[i + 2][j - 1])
print(maxx)
