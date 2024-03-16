import heapq
import sys

t = 0
while True:
    t += 1
    n = int(sys.stdin.readline())
    if n == 0:
        break
    grid = []
    for i in range(n):
        grid.append(list(map(int, sys.stdin.readline().split())))
    visited = [[False] * n for _ in range(n)]
    heap = [(grid[0][0], 0, 0)]
    while heapq:
        cost, x, y = heapq.heappop(heap)
        if x == n - 1 and y == n - 1:
            break
        if x > 0 and visited[x - 1][y] == False:
            heapq.heappush(heap, (cost + grid[x - 1][y], x - 1, y))
            visited[x - 1][y] = True
        if y > 0 and visited[x][y - 1] == False:
            heapq.heappush(heap, (cost + grid[x][y - 1], x, y - 1))
            visited[x][y - 1] = True
        if x < n - 1 and visited[x + 1][y] == False:
            heapq.heappush(heap, (cost + grid[x + 1][y], x + 1, y))
            visited[x + 1][y] = True
        if y < n - 1 and visited[x][y + 1] == False:
            heapq.heappush(heap, (cost + grid[x][y + 1], x, y + 1))
            visited[x][y + 1] = True
    print("Problem " + str(t) + ": " + str(cost))
