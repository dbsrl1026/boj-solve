import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
arr = []
for i in range(n):
    arr.append(list(sys.stdin.readline().rstrip()))
    for j in range(m):
        if arr[i][j] == 'I':
            startX = i;
            startY = j
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
visited = {(startX, startY): True}
queue = deque()
queue.append((startX, startY))
cnt = 0
while queue:
    x, y = queue.popleft()
    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]
        if tx >= 0 and tx < n and ty >= 0 and ty < m and (tx, ty) not in visited and arr[tx][ty] != 'X':
            queue.append((tx, ty))
            visited[(tx, ty)] = True
            if arr[tx][ty] == 'P':
                cnt += 1
if cnt == 0:
    print('TT')
else:
    print(cnt)
