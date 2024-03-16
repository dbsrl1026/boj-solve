import sys
from collections import deque


def bfs(n, arr, a, b):
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    queue = deque()
    queue.append((a, b))
    arr[a][b]= 2
    cnt = 0
    while queue:
        x, y = queue.popleft()
        cnt+=1
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if tx >= 0 and tx < n and ty >= 0 and ty < n and arr[tx][ty] == 1:
                queue.append((tx, ty))
                arr[tx][ty] = arr[x][y]+1
    return cnt


n = int(sys.stdin.readline())
arr = []
for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().rstrip())))

result = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            result.append(bfs(n, arr, i, j))
result = sorted(result)
print(len(result))
for i, v in enumerate(result):
    print(v)
