from collections import deque


def ShortestPath(grid):
    n = len(grid)
    if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
        return -1

    def bfs():
        curX = 0
        curY = 0
        visited = [[False] * n for _ in range(n)]
        length = [[0] * n for _ in range(n)]
        dX = [1, 1, 1, 0, -0, -1, -1, -1]
        dY = [0, 1, -1, 1, -1, 1, 0, -1]
        queue = deque()
        queue.append((0, 0))
        while queue:
            curX, curY = queue.popleft()
            visited[curX][curY] = True
            for i in range(8):
                nextX = curX + dX[i]
                nextY = curY + dY[i]
                if nextX > -1 and nextX < n and nextY > -1 and nextY < n:
                    if grid[nextX][nextY] == 0 and not visited[nextX][nextY]:
                        queue.append((nextX, nextY))
                        length[nextX][nextY] = length[curX][curY] + 1
                        if nextX == n - 1 and nextY == n - 1:
                            return length[nextX][nextY]
        return -1

    length = bfs()
    return length


length = ShortestPath(grid=[
    [0, 0, 0],
    [1, 1, 0],
    [1, 1, 0]
])
print(length)
