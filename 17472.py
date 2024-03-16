from collections import deque

n, m = map(int, input().split())
grid = []
islandNum = 0
arr = []
for i in range(n):
    grid.append(list(map(int, input().split())))


def numbering(x, y, num):
    if 0 <= x < n and 0 <= y < m and grid[x][y] == 1:
        grid[x][y] = num
        numbering(x + 1, y, num)
        numbering(x, y + 1, num)
        numbering(x - 1, y, num)
        numbering(x, y - 1, num)


for i in range(n):
    for j in range(m):
        if grid[i][j] == 1:
            islandNum += 1
            if islandNum > 1:
                numbering(i, j, islandNum)
for i in range(n):
    for j in range(m):
        if m > 0 and grid[i][j] == 0 and grid[i][j - 1] != 0:
            a = grid[i][j - 1]
            for k in range(j + 1, m):
                if grid[i][k] != 0:
                    if k - j > 1:
                        b = grid[i][k]
                        arr.append((k - j, a, b))
                    break
        if n > 0 and grid[i][j] == 0 and grid[i - 1][j] != 0:
            a = grid[i - 1][j]
            for k in range(i + 1, n):
                if grid[k][j] != 0:
                    if k - i > 1:
                        b = grid[k][j]
                        arr.append((k - i, a, b))
                    break

arr = deque(sorted(arr))
root = [i for i in range(islandNum + 1)]
weight_sum = 0


def findroot(x):
    if x != root[x]:
        root[x] = findroot(root[x])
    return root[x]


while arr:
    w, a, b = arr.popleft()
    aroot = findroot(a)
    broot = findroot(b)
    if aroot != broot:
        if aroot < broot:
            root[broot] = aroot
        else:
            root[aroot] = broot
        weight_sum += w
if len(set(root)) > 2:
    print(-1)
else:
    print(weight_sum)
