import sys
from collections import deque


def bfs(grid, i, j,n, m):
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    queue = deque()
    queue.append((i, j))
    while queue:
        x, y= queue.popleft()
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if tx>=0  and tx<n and ty>=0 and ty<m and grid[tx][ty]==-1:
                queue.append((tx,ty))
                grid[tx][ty] = grid[x][y]+1
    return grid


n, m = map(int, sys.stdin.readline().split())

grid =[[-1] *m for _ in range(n)]
for i in range(n):
    tmp = list(map(int, sys.stdin.readline().split()))
    for j in range(m):
        if tmp[j] == 0:
            grid[i][j] = 0
        elif tmp[j] == 2:
            grid[i][j] = 0
            startX, startY = i, j
grid = bfs(grid, startX, startY,n, m)

answer =''
for i in range(n):
    print(*grid[i])
print(answer)
