import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
arr = []
for i in range(n):
    arr.append(list(map(int,sys.stdin.readline().rstrip())))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
visited = {}
queue = deque()
queue.append((0, 0))
while queue:
    x, y = queue.popleft()
    if x == n - 1 and y == m - 1:
        break
    visited[(x,y)] = True
    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]
        if tx >= 0 and tx < n and ty >= 0 and ty < m and arr[tx][ty] == 1 and (tx, ty) not in visited:
            queue.append((tx, ty))
            arr[tx][ty] = arr[x][y] +1
print(arr[n-1][m-1])
