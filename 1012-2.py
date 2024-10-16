from collections import deque

t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    grid = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    for i in range(k):
        a, b = map(int, input().split())
        grid[b][a] = 1
    cnt = 0


    def bfs(i, j):
        dx = [1, 0, -1, 0]
        dy = [0, -1, 0, 1]
        queue = deque()
        queue.append((i, j))
        while queue:
            x, y = queue.popleft()
            for l in range(4):
                newX = x + dx[l]
                newY = y + dy[l]
                if 0 <= newX < n and 0 <= newY < m and grid[newX][newY] == 1 and visited[newX][newY] == False:
                    visited[newX][newY] = True
                    queue.append((newX,newY))

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1 and visited[i][j] == False:
                cnt += 1
                visited[i][j] = True
                bfs(i, j)
    print(cnt)
