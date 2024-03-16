import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().rstrip())))
queue = deque()
queue.append((0, 0, 1, 1))
visited = {(0, 0): 1}
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
while queue:
    x, y, cnt, life = queue.popleft()
    if x == n - 1 and y == m - 1:
        print(cnt)
        exit()
    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]
        if 0 <= tx < n and 0 <= ty < m:
            if (tx, ty) not in visited:
                if arr[tx][ty] == 0:
                    queue.append((tx, ty, cnt + 1, life))
                    visited[(tx, ty)] = life
                elif life == 1:
                    queue.append((tx, ty, cnt + 1, 0))
                    visited[(tx, ty)] = 0
            elif visited[(tx, ty)] == 0 and life ==1 and arr[tx][ty] == 0:
                queue.append((tx, ty, cnt + 1, life))
                visited[(tx, ty)] = life


print(-1)