
from collections import deque

N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]


def bfs(start):
    queue = deque([start])
    visited[start[0]][start[1]] = True
    union = [start]
    sum_population = arr[start[0]][start[1]]

    while queue:
        x, y = queue.popleft()
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if L <= abs(arr[x][y] - arr[nx][ny]) <= R:
                    queue.append((nx, ny))
                    visited[nx][ny] = True
                    union.append((nx, ny))
                    sum_population += arr[nx][ny]
    for x, y in union:
        arr[x][y] = sum_population // len(union)
    return len(union) > 1


cnt = 0
while True:
    visited = [[False] * N for _ in range(N)]
    moved = False
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                if bfs((i, j)):
                    moved = True
    if not moved:
        break
    cnt += 1

print(cnt)
